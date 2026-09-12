"""Deterministic transportation/access mechanics for Phase-1 verification."""
from dataclasses import dataclass
import heapq
from math import inf, isfinite
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


Edge = Tuple[int, int]


@dataclass(frozen=True)
class RoadLink:
    u: int
    v: int
    capacity: float
    free_time: float
    alpha: float = 0.15
    beta: float = 4.0


def bpr_time(link: RoadLink, flow: float) -> float:
    if link.capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if flow < 0.0:
        raise ValueError("flow must be nonnegative")
    return link.free_time * (1.0 + link.alpha * (flow / link.capacity) ** link.beta)


def bpr_derivative(link: RoadLink, flow: float) -> float:
    """Derivative dt_a/dx_a of the separable BPR link cost."""
    if link.capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if flow < 0.0:
        raise ValueError("flow must be nonnegative")
    if link.beta <= 0.0 or link.alpha == 0.0:
        return 0.0
    if flow == 0.0 and link.beta > 1.0:
        return 0.0
    return (
        link.free_time
        * link.alpha
        * link.beta
        * flow ** (link.beta - 1.0)
        / link.capacity ** link.beta
    )


def _adjacency(
    links: Sequence[RoadLink], closed: Optional[Iterable[Edge]] = None
) -> Dict[int, List[RoadLink]]:
    closed_set = set() if closed is None else set(closed)
    adj: Dict[int, List[RoadLink]] = {}
    for link in links:
        if (link.u, link.v) in closed_set:
            continue
        adj.setdefault(link.u, []).append(link)
    for u in adj:
        adj[u].sort(key=lambda edge: (edge.v, edge.free_time, edge.capacity))
    return adj


def _single_source_predecessors(
    links: Sequence[RoadLink],
    costs: Mapping[Edge, float],
    source: int,
    closed: Optional[Iterable[Edge]] = None,
) -> Tuple[Dict[int, float], Dict[int, Tuple[int, Edge]]]:
    """Deterministic Dijkstra tree for one origin."""
    adj = _adjacency(links, closed)
    dist: Dict[int, float] = {source: 0.0}
    prev: Dict[int, Tuple[int, Edge]] = {}
    heap: List[Tuple[float, int]] = [(0.0, source)]
    while heap:
        distance, u = heapq.heappop(heap)
        if distance != dist.get(u):
            continue
        for link in adj.get(u, []):
            edge = (link.u, link.v)
            new_distance = distance + costs[edge]
            old = dist.get(link.v, inf)
            if new_distance < old - 1e-15:
                dist[link.v] = new_distance
                prev[link.v] = (u, edge)
                heapq.heappush(heap, (new_distance, link.v))
    return dist, prev


def _path_from_predecessors(
    source: int,
    target: int,
    dist: Mapping[int, float],
    prev: Mapping[int, Tuple[int, Edge]],
) -> Tuple[float, Tuple[Edge, ...]]:
    if source == target:
        return 0.0, tuple()
    if target not in dist:
        return inf, tuple()
    path: List[Edge] = []
    node = target
    while node != source:
        if node not in prev:
            return inf, tuple()
        parent, edge = prev[node]
        path.append(edge)
        node = parent
    path.reverse()
    return dist[target], tuple(path)


def shortest_path(
    links: Sequence[RoadLink],
    costs: Mapping[Edge, float],
    source: int,
    target: int,
    closed: Optional[Iterable[Edge]] = None,
) -> Tuple[float, Tuple[Edge, ...]]:
    dist, prev = _single_source_predecessors(links, costs, source, closed)
    return _path_from_predecessors(source, target, dist, prev)


def all_or_nothing(
    links: Sequence[RoadLink],
    costs: Mapping[Edge, float],
    od: Mapping[Tuple[int, int], float],
    closed: Optional[Iterable[Edge]] = None,
) -> Dict[Edge, float]:
    """Assign each OD demand to deterministic shortest paths.

    OD pairs are grouped by origin so one shortest-path tree is computed per
    origin. This is mathematically identical to separate shortest-path calls
    at the same fixed link costs and only removes redundant computation.
    """
    flows: Dict[Edge, float] = {(link.u, link.v): 0.0 for link in links}
    grouped: Dict[int, List[Tuple[int, float]]] = {}
    for (origin, destination), demand in sorted(od.items()):
        if demand < 0.0:
            raise ValueError("OD demand must be nonnegative")
        if demand == 0.0 or origin == destination:
            continue
        grouped.setdefault(origin, []).append((destination, demand))

    for origin in sorted(grouped):
        dist, prev = _single_source_predecessors(links, costs, origin, closed)
        for destination, demand in grouped[origin]:
            _, path = _path_from_predecessors(origin, destination, dist, prev)
            if not path:
                raise ValueError("positive OD demand is disconnected")
            for edge in path:
                flows[edge] += demand
    return flows


def beckmann_objective(
    links: Sequence[RoadLink], flows: Mapping[Edge, float]
) -> float:
    total = 0.0
    for link in links:
        flow = flows[(link.u, link.v)]
        total += link.free_time * (
            flow
            + link.alpha
            * flow ** (link.beta + 1.0)
            / ((link.beta + 1.0) * link.capacity ** link.beta)
        )
    return total


def _golden_section(
    function, a: float = 0.0, b: float = 1.0, tol: float = 1e-13, max_iter: int = 200
) -> float:
    phi = (5.0 ** 0.5 - 1.0) / 2.0
    c = b - phi * (b - a)
    d = a + phi * (b - a)
    fc = function(c)
    fd = function(d)
    for _ in range(max_iter):
        if b - a <= tol:
            break
        if fc <= fd:
            b, d, fd = d, c, fc
            c = b - phi * (b - a)
            fc = function(c)
        else:
            a, c, fc = c, d, fd
            d = a + phi * (b - a)
            fd = function(d)
    return 0.5 * (a + b)


def _line_search_to_target(
    links: Sequence[RoadLink],
    flow: Mapping[Edge, float],
    target: Mapping[Edge, float],
) -> float:
    direction = {edge: target[edge] - flow[edge] for edge in flow}

    def objective(step: float) -> float:
        trial = {edge: flow[edge] + step * direction[edge] for edge in flow}
        return beckmann_objective(links, trial)

    return _golden_section(objective)


def relative_gap(
    links: Sequence[RoadLink],
    flows: Mapping[Edge, float],
    od: Mapping[Tuple[int, int], float],
) -> float:
    costs = {
        (link.u, link.v): bpr_time(link, flows[(link.u, link.v)])
        for link in links
    }
    aon = all_or_nothing(links, costs, od)
    current = sum(flows[edge] * costs[edge] for edge in flows)
    shortest = sum(aon[edge] * costs[edge] for edge in aon)
    if current <= 0.0:
        return 0.0
    return max(0.0, (current - shortest) / current)


def frank_wolfe_user_equilibrium(
    links: Sequence[RoadLink],
    od: Mapping[Tuple[int, int], float],
    gap_tol: float = 1e-8,
    max_iter: int = 5000,
) -> Tuple[Dict[Edge, float], int, float]:
    """Classical Frank-Wolfe retained as a diagnostic/reference solver."""
    free_costs = {(link.u, link.v): link.free_time for link in links}
    flow = all_or_nothing(links, free_costs, od)
    for iteration in range(1, max_iter + 1):
        gap = relative_gap(links, flow, od)
        if gap <= gap_tol:
            return flow, iteration, gap
        costs = {
            (link.u, link.v): bpr_time(link, flow[(link.u, link.v)])
            for link in links
        }
        aon = all_or_nothing(links, costs, od)
        step = _line_search_to_target(links, flow, aon)
        flow = {
            edge: flow[edge] + step * (aon[edge] - flow[edge])
            for edge in flow
        }
    return flow, max_iter, relative_gap(links, flow, od)


def _cfw_target(
    links: Sequence[RoadLink],
    flow: Mapping[Edge, float],
    fw_target: Mapping[Edge, float],
    previous_target: Mapping[Edge, float],
    conjugate_weight_max: float,
) -> Dict[Edge, float]:
    """Form the CFW sight point at the current iterate.

    ``previous_target - flow`` is exactly the residual prior conjugate
    direction ``(1-tau_prev)d_prev`` at the current iterate.  The coefficient
    is the diagonal-Hessian conjugacy coefficient of Mitradjieva-Lindberg,
    clipped to preserve a convex combination of feasible assignment points.
    """
    numerator = 0.0
    denominator = 0.0
    for link in links:
        edge = (link.u, link.v)
        h = bpr_derivative(link, flow[edge])
        bar = previous_target[edge] - flow[edge]
        d_fw = fw_target[edge] - flow[edge]
        numerator += bar * d_fw * h
        denominator += bar * (d_fw - bar) * h

    if abs(denominator) <= 1e-30:
        weight_previous = 0.0
    else:
        weight_previous = numerator / denominator
        if not isfinite(weight_previous):
            weight_previous = 0.0
        weight_previous = min(conjugate_weight_max, max(0.0, weight_previous))

    return {
        edge: weight_previous * previous_target[edge]
        + (1.0 - weight_previous) * fw_target[edge]
        for edge in flow
    }


def conjugate_frank_wolfe_user_equilibrium(
    links: Sequence[RoadLink],
    od: Mapping[Tuple[int, int], float],
    gap_tol: float = 1e-8,
    max_iter: int = 5000,
    conjugate_weight_max: float = 0.99999,
) -> Tuple[Dict[Edge, float], int, float]:
    """Conjugate-direction Frank-Wolfe (CFW) for separable traffic UE."""
    if not (0.0 < conjugate_weight_max < 1.0):
        raise ValueError("conjugate_weight_max must lie strictly between 0 and 1")

    free_costs = {(link.u, link.v): link.free_time for link in links}
    flow = all_or_nothing(links, free_costs, od)
    previous_target: Optional[Dict[Edge, float]] = None
    previous_step = 1.0
    restart_tol = max(gap_tol, 1e-12)

    for iteration in range(1, max_iter + 1):
        gap = relative_gap(links, flow, od)
        if gap <= gap_tol:
            return flow, iteration, gap

        costs = {
            (link.u, link.v): bpr_time(link, flow[(link.u, link.v)])
            for link in links
        }
        fw_target = all_or_nothing(links, costs, od)

        use_fw = previous_target is None or previous_step > 1.0 - restart_tol
        if use_fw:
            target = dict(fw_target)
        else:
            target = _cfw_target(
                links,
                flow,
                fw_target,
                previous_target,
                conjugate_weight_max,
            )

        step = _line_search_to_target(links, flow, target)
        flow = {
            edge: flow[edge] + step * (target[edge] - flow[edge])
            for edge in flow
        }
        previous_target = target
        previous_step = step

    return flow, max_iter, relative_gap(links, flow, od)


def biconjugate_frank_wolfe_user_equilibrium(
    links: Sequence[RoadLink],
    od: Mapping[Tuple[int, int], float],
    gap_tol: float = 1e-8,
    max_iter: int = 5000,
    conjugate_weight_max: float = 0.999999,
) -> Tuple[Dict[Edge, float], int, float]:
    """Biconjugate Frank-Wolfe (BFW) for separable traffic user equilibrium.

    This is a direct deterministic translation of the Mitradjieva-Lindberg
    biconjugate recurrence as independently implemented by TrafficAssign.jl.
    It solves the same frozen Beckmann problem, uses the same all-or-nothing
    oracle and exact Beckmann line search, and changes only the acceleration
    direction.  A nearly unit previous line step triggers an FW restart.
    """
    if not (0.0 < conjugate_weight_max < 1.0):
        raise ValueError("conjugate_weight_max must lie strictly between 0 and 1")

    free_costs = {(link.u, link.v): link.free_time for link in links}
    flow = all_or_nothing(links, free_costs, od)

    previous_target: Optional[Dict[Edge, float]] = None
    previous_previous_target: Optional[Dict[Edge, float]] = None
    previous_direction: Optional[Dict[Edge, float]] = None
    previous_previous_direction: Optional[Dict[Edge, float]] = None
    previous_step = 1.0
    previous_previous_step = 1.0
    stage = "FW"
    restart_tol = max(gap_tol, 1e-12)

    for iteration in range(1, max_iter + 1):
        gap = relative_gap(links, flow, od)
        if gap <= gap_tol:
            return flow, iteration, gap

        costs = {
            (link.u, link.v): bpr_time(link, flow[(link.u, link.v)])
            for link in links
        }
        fw_target = all_or_nothing(links, costs, od)
        fw_direction = {edge: fw_target[edge] - flow[edge] for edge in flow}

        if stage == "FW" or previous_target is None or previous_direction is None:
            target = dict(fw_target)
            direction = dict(fw_direction)
            next_stage = "CFW"
        elif stage == "CFW":
            old_target = previous_target
            old_direction = previous_direction
            target = _cfw_target(
                links,
                flow,
                fw_target,
                old_target,
                conjugate_weight_max,
            )
            direction = {edge: target[edge] - flow[edge] for edge in flow}
            previous_previous_target = old_target
            previous_previous_direction = old_direction
            next_stage = "BFW"
        else:
            if (
                previous_previous_target is None
                or previous_previous_direction is None
                or previous_target is None
                or previous_direction is None
                or previous_step >= 1.0 - restart_tol
                or previous_previous_step >= 1.0 - restart_tol
            ):
                target = dict(fw_target)
                direction = dict(fw_direction)
                next_stage = "CFW"
            else:
                hessian = {
                    (link.u, link.v): bpr_derivative(
                        link, flow[(link.u, link.v)]
                    )
                    for link in links
                }
                bar = {
                    edge: (1.0 - previous_step) * previous_direction[edge]
                    for edge in flow
                }
                bar_bar = {
                    edge: (1.0 - previous_step)
                    * (1.0 - previous_previous_step)
                    * previous_previous_direction[edge]
                    for edge in flow
                }

                mu_num = -sum(
                    bar_bar[edge] * hessian[edge] * fw_direction[edge]
                    for edge in flow
                )
                mu_den = sum(
                    bar_bar[edge]
                    * hessian[edge]
                    * (previous_previous_target[edge] - previous_target[edge])
                    for edge in flow
                )
                if abs(mu_den) <= 1e-30:
                    mu = 0.0
                else:
                    mu = mu_num / mu_den
                    if not isfinite(mu):
                        mu = 0.0
                mu = max(0.0, mu)

                nu_den = sum(
                    bar[edge] * hessian[edge] * bar[edge]
                    for edge in flow
                )
                if abs(nu_den) <= 1e-30:
                    nu = 0.0
                else:
                    nu = -sum(
                        bar[edge] * hessian[edge] * fw_direction[edge]
                        for edge in flow
                    ) / nu_den
                    nu += mu * previous_step / max(1.0 - previous_step, 1e-30)
                    if not isfinite(nu):
                        nu = 0.0
                nu = max(0.0, nu)

                beta_fw = 1.0 / (1.0 + mu + nu)
                beta_prev = nu * beta_fw
                beta_prevprev = mu * beta_fw
                target = {
                    edge: beta_fw * fw_target[edge]
                    + beta_prev * previous_target[edge]
                    + beta_prevprev * previous_previous_target[edge]
                    for edge in flow
                }
                direction = {edge: target[edge] - flow[edge] for edge in flow}
                next_stage = "BFW"

        step = _line_search_to_target(links, flow, target)
        new_flow = {
            edge: flow[edge] + step * direction[edge]
            for edge in flow
        }

        previous_previous_step = previous_step
        previous_step = step
        previous_target = target
        previous_direction = direction
        flow = new_flow

        if step > 1.0 - restart_tol:
            stage = "FW"
        else:
            stage = next_stage

    return flow, max_iter, relative_gap(links, flow, od)


def node_flow_residuals(
    links: Sequence[RoadLink],
    flows: Mapping[Edge, float],
    od: Mapping[Tuple[int, int], float],
) -> Dict[int, float]:
    nodes = sorted({node for link in links for node in (link.u, link.v)})
    residual = {node: 0.0 for node in nodes}
    for link in links:
        flow = flows[(link.u, link.v)]
        residual[link.u] -= flow
        residual[link.v] += flow
    for (origin, destination), demand in od.items():
        residual[origin] += demand
        residual[destination] -= demand
    return residual
