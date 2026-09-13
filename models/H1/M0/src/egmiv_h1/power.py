from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import math
import numpy as np


@dataclass(frozen=True)
class Line:
    """One oriented branch of a radial distribution network in per-unit.

    Convention: positive p/q are loads. The branch is oriented from parent -> child.
    r_pu, x_pu are per-unit branch impedance on the same system base used by loads.
    smax_pu is the branch apparent-power limit in per-unit.
    """
    parent: int
    child: int
    r_pu: float
    x_pu: float
    smax_pu: float = math.inf

    def __post_init__(self) -> None:
        if self.parent == self.child:
            raise ValueError("A line cannot connect a bus to itself.")
        if self.r_pu < 0 or self.x_pu < 0:
            raise ValueError("Branch r/x must be nonnegative.")
        if self.smax_pu <= 0:
            raise ValueError("smax_pu must be positive.")


@dataclass(frozen=True)
class PowerResult:
    voltage_sq_pu: np.ndarray
    branch_p_pu: np.ndarray
    branch_q_pu: np.ndarray
    served_p_pu: np.ndarray
    served_q_pu: np.ndarray
    energized_bus: np.ndarray
    service: float
    max_power_balance_residual_pu: float
    min_voltage_pu: float
    max_voltage_pu: float
    max_thermal_loading: float
    voltage_violation_pu: float
    thermal_violation_pu: float


class RadialNetwork:
    """Lossless LinDistFlow baseline for a radial distribution feeder.

    This class is deliberately minimal for EGMIV H1 M0. It contains no transport
    variables and no coupling terms. Electrical service is disconnected only by
    exogenous branch availability. Voltage/thermal violations are *reported*, not
    silently corrected by an optimizer, so physical admissibility remains auditable.
    """

    def __init__(
        self,
        n_buses: int,
        slack_bus: int,
        lines: Iterable[Line],
        v_slack_pu: float = 1.0,
        v_min_pu: float = 0.95,
        v_max_pu: float = 1.05,
    ) -> None:
        self.n_buses = int(n_buses)
        self.slack_bus = int(slack_bus)
        self.lines = tuple(lines)
        self.v_slack_pu = float(v_slack_pu)
        self.v_min_pu = float(v_min_pu)
        self.v_max_pu = float(v_max_pu)
        self._validate_topology()

        self.parent_line = {ln.child: idx for idx, ln in enumerate(self.lines)}
        self.children: dict[int, list[tuple[int, int]]] = {i: [] for i in range(self.n_buses)}
        for idx, ln in enumerate(self.lines):
            self.children[ln.parent].append((ln.child, idx))
        self.topological_order = self._topological_order()

    def _validate_topology(self) -> None:
        if self.n_buses < 1:
            raise ValueError("n_buses must be positive.")
        if not (0 <= self.slack_bus < self.n_buses):
            raise ValueError("slack_bus is outside the bus set.")
        if len(self.lines) != self.n_buses - 1:
            raise ValueError("A radial connected network must have n_buses - 1 lines.")

        parent_count = [0] * self.n_buses
        adj = {i: [] for i in range(self.n_buses)}
        for ln in self.lines:
            if not (0 <= ln.parent < self.n_buses and 0 <= ln.child < self.n_buses):
                raise ValueError("Line endpoint outside bus set.")
            parent_count[ln.child] += 1
            adj[ln.parent].append(ln.child)
        if parent_count[self.slack_bus] != 0:
            raise ValueError("Slack bus cannot have a parent in the oriented tree.")
        for b in range(self.n_buses):
            if b != self.slack_bus and parent_count[b] != 1:
                raise ValueError("Every non-slack bus must have exactly one parent.")

        seen = set()
        stack = [self.slack_bus]
        while stack:
            u = stack.pop()
            if u in seen:
                raise ValueError("Cycle detected in radial network.")
            seen.add(u)
            stack.extend(adj[u])
        if len(seen) != self.n_buses:
            raise ValueError("Radial network must be connected from the slack bus.")

    def _topological_order(self) -> list[int]:
        out: list[int] = []
        q = [self.slack_bus]
        while q:
            u = q.pop(0)
            out.append(u)
            q.extend(child for child, _ in self.children[u])
        return out

    def solve(
        self,
        p_demand_pu: np.ndarray,
        q_demand_pu: np.ndarray | None = None,
        line_available: np.ndarray | None = None,
        service_weights: np.ndarray | None = None,
    ) -> PowerResult:
        p = np.asarray(p_demand_pu, dtype=float)
        q = np.zeros_like(p) if q_demand_pu is None else np.asarray(q_demand_pu, dtype=float)
        if p.shape != (self.n_buses,) or q.shape != (self.n_buses,):
            raise ValueError("Demand arrays must have shape (n_buses,).")
        if np.any(p < -1e-12) or np.any(q < -1e-12):
            raise ValueError("M0 baseline expects nonnegative load demand.")

        avail = np.ones(len(self.lines), dtype=bool) if line_available is None else np.asarray(line_available, dtype=bool)
        if avail.shape != (len(self.lines),):
            raise ValueError("line_available must have one entry per branch.")

        w = np.ones(self.n_buses, dtype=float) if service_weights is None else np.asarray(service_weights, dtype=float)
        if w.shape != (self.n_buses,) or np.any(w < 0):
            raise ValueError("service_weights must be nonnegative with shape (n_buses,).")

        energized = np.zeros(self.n_buses, dtype=bool)
        energized[self.slack_bus] = True
        for u in self.topological_order:
            if not energized[u]:
                continue
            for child, line_idx in self.children[u]:
                energized[child] = bool(avail[line_idx])

        served_p = p * energized
        served_q = q * energized

        branch_p = np.zeros(len(self.lines), dtype=float)
        branch_q = np.zeros(len(self.lines), dtype=float)
        subtree_p = served_p.copy()
        subtree_q = served_q.copy()
        for bus in reversed(self.topological_order):
            if bus == self.slack_bus:
                continue
            idx = self.parent_line[bus]
            ln = self.lines[idx]
            if energized[bus] and avail[idx]:
                branch_p[idx] = subtree_p[bus]
                branch_q[idx] = subtree_q[bus]
                subtree_p[ln.parent] += subtree_p[bus]
                subtree_q[ln.parent] += subtree_q[bus]

        v_sq = np.full(self.n_buses, np.nan, dtype=float)
        v_sq[self.slack_bus] = self.v_slack_pu ** 2
        for u in self.topological_order:
            if not energized[u]:
                continue
            for child, idx in self.children[u]:
                if not energized[child] or not avail[idx]:
                    continue
                ln = self.lines[idx]
                v_sq[child] = v_sq[u] - 2.0 * (ln.r_pu * branch_p[idx] + ln.x_pu * branch_q[idx])

        # Branch power balance: flow into child equals local served load + child branch flows.
        residuals = []
        for idx, ln in enumerate(self.lines):
            if not energized[ln.child] or not avail[idx]:
                continue
            child_out_p = sum(branch_p[j] for _, j in self.children[ln.child])
            residuals.append(abs(branch_p[idx] - served_p[ln.child] - child_out_p))
        max_res = max(residuals, default=0.0)

        finite_v = np.sqrt(v_sq[np.isfinite(v_sq)])
        min_v = float(finite_v.min()) if finite_v.size else float("nan")
        max_v = float(finite_v.max()) if finite_v.size else float("nan")
        voltage_violation = max(0.0, self.v_min_pu - min_v, max_v - self.v_max_pu)

        loadings = []
        thermal_violation = 0.0
        for idx, ln in enumerate(self.lines):
            if not energized[ln.child] or not avail[idx] or math.isinf(ln.smax_pu):
                continue
            s = math.hypot(branch_p[idx], branch_q[idx])
            loading = s / ln.smax_pu
            loadings.append(loading)
            thermal_violation = max(thermal_violation, max(0.0, loading - 1.0))
        max_loading = max(loadings, default=0.0)

        denom = float(np.dot(w, p))
        service = 1.0 if denom <= 1e-15 else float(np.dot(w, served_p) / denom)

        return PowerResult(
            voltage_sq_pu=v_sq,
            branch_p_pu=branch_p,
            branch_q_pu=branch_q,
            served_p_pu=served_p,
            served_q_pu=served_q,
            energized_bus=energized,
            service=service,
            max_power_balance_residual_pu=float(max_res),
            min_voltage_pu=min_v,
            max_voltage_pu=max_v,
            max_thermal_loading=float(max_loading),
            voltage_violation_pu=float(voltage_violation),
            thermal_violation_pu=float(thermal_violation),
        )