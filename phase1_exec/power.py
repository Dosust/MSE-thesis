"""Deterministic radial-distribution verification solver.

The implementation uses backward/forward sweep in per-unit complex variables.
It is intended to verify the declared radial electrical equations before any
Phase-1 validation or hypothesis testing.
"""
from dataclasses import dataclass
from typing import Dict, List, Mapping, Sequence, Tuple


@dataclass(frozen=True)
class Branch:
    parent: int
    child: int
    r_pu: float
    x_pu: float

    @property
    def impedance(self) -> complex:
        return complex(self.r_pu, self.x_pu)


@dataclass(frozen=True)
class RadialSolution:
    voltage: Mapping[int, complex]
    branch_current: Mapping[Tuple[int, int], complex]
    iterations: int
    converged: bool


def _validate_tree(
    branches: Sequence[Branch], slack: int
) -> Tuple[List[int], Dict[int, List[int]], Dict[int, Branch]]:
    children: Dict[int, List[int]] = {}
    incoming: Dict[int, Branch] = {}
    nodes = {slack}
    for br in branches:
        if br.child == slack:
            raise ValueError("slack bus cannot have an incoming branch")
        if br.child in incoming:
            raise ValueError("radial network requires one parent per non-slack bus")
        incoming[br.child] = br
        children.setdefault(br.parent, []).append(br.child)
        nodes.add(br.parent)
        nodes.add(br.child)
    for n in children:
        children[n].sort()

    order: List[int] = []
    stack = [slack]
    seen = set()
    while stack:
        node = stack.pop()
        if node in seen:
            raise ValueError("cycle detected")
        seen.add(node)
        order.append(node)
        for child in reversed(children.get(node, [])):
            stack.append(child)
    if seen != nodes:
        raise ValueError("network is disconnected from slack")
    return order, children, incoming


def solve_radial_bfs(
    branches: Sequence[Branch],
    loads_pu: Mapping[int, complex],
    slack: int = 1,
    slack_voltage: complex = 1.0 + 0.0j,
    tol: float = 1e-12,
    max_iter: int = 200,
) -> RadialSolution:
    """Solve a radial constant-power load flow with backward/forward sweep.

    ``loads_pu`` uses the positive-consumption convention S=P+jQ.
    """
    order, _, incoming = _validate_tree(branches, slack)
    voltage: Dict[int, complex] = {n: slack_voltage for n in order}
    branch_current: Dict[Tuple[int, int], complex] = {
        (br.parent, br.child): 0.0 + 0.0j for br in branches
    }

    for iteration in range(1, max_iter + 1):
        injection: Dict[int, complex] = {}
        for n in order:
            if n == slack:
                injection[n] = 0.0 + 0.0j
                continue
            v = voltage[n]
            if abs(v) < 1e-14:
                raise ArithmeticError("near-zero bus voltage in current calculation")
            s_load = loads_pu.get(n, 0.0 + 0.0j)
            injection[n] = (s_load / v).conjugate()

        downstream_current: Dict[int, complex] = {n: injection[n] for n in order}
        for n in reversed(order[1:]):
            br = incoming[n]
            current = downstream_current[n]
            branch_current[(br.parent, br.child)] = current
            downstream_current[br.parent] = (
                downstream_current.get(br.parent, 0.0 + 0.0j) + current
            )

        new_voltage: Dict[int, complex] = {slack: slack_voltage}
        for n in order[1:]:
            br = incoming[n]
            parent_v = new_voltage[br.parent]
            current = branch_current[(br.parent, br.child)]
            new_voltage[n] = parent_v - br.impedance * current

        error = max(abs(new_voltage[n] - voltage[n]) for n in order)
        voltage = new_voltage
        if error <= tol:
            return RadialSolution(voltage, dict(branch_current), iteration, True)

    return RadialSolution(voltage, dict(branch_current), max_iter, False)


def branch_flow_residuals(
    branches: Sequence[Branch],
    loads_pu: Mapping[int, complex],
    solution: RadialSolution,
    slack: int = 1,
) -> Dict[str, float]:
    """Return maximum absolute residuals of the declared branch-flow equations."""
    _, children, _ = _validate_tree(branches, slack)
    s_flow: Dict[Tuple[int, int], complex] = {}
    ell: Dict[Tuple[int, int], float] = {}
    for edge, current in solution.branch_current.items():
        parent, _ = edge
        s_flow[edge] = solution.voltage[parent] * current.conjugate()
        ell[edge] = abs(current) ** 2

    max_p = 0.0
    max_q = 0.0
    max_v = 0.0
    max_i = 0.0
    for br in branches:
        edge = (br.parent, br.child)
        s_ij = s_flow[edge]
        outgoing = sum(
            (s_flow[(br.child, k)] for k in children.get(br.child, [])),
            0.0 + 0.0j,
        )
        load = loads_pu.get(br.child, 0.0 + 0.0j)
        rhs = outgoing + load + br.impedance * ell[edge]
        max_p = max(max_p, abs(s_ij.real - rhs.real))
        max_q = max(max_q, abs(s_ij.imag - rhs.imag))

        vi2 = abs(solution.voltage[br.parent]) ** 2
        vj2 = abs(solution.voltage[br.child]) ** 2
        p = s_ij.real
        q = s_ij.imag
        rhs_v = (
            vi2
            - 2.0 * (br.r_pu * p + br.x_pu * q)
            + (br.r_pu ** 2 + br.x_pu ** 2) * ell[edge]
        )
        max_v = max(max_v, abs(vj2 - rhs_v))

        rhs_i = (p * p + q * q) / vi2 if vi2 > 0.0 else float("inf")
        max_i = max(max_i, abs(ell[edge] - rhs_i))

    return {
        "p_balance": max_p,
        "q_balance": max_q,
        "voltage_drop": max_v,
        "current_relation": max_i,
        "max": max(max_p, max_q, max_v, max_i),
    }


def add_real_load(
    loads_pu: Mapping[int, complex], bus: int, delta_p_pu: float
) -> Dict[int, complex]:
    """Return a new load map with an added real-power demand at one bus."""
    result = dict(loads_pu)
    result[bus] = result.get(bus, 0.0 + 0.0j) + complex(delta_p_pu, 0.0)
    return result
