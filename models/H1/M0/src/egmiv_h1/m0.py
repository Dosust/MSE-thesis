from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from .power import RadialNetwork, PowerResult
from .traffic import CTMNetwork, TrafficStepResult
from .metrics import cumulative_service_loss


@dataclass(frozen=True)
class M0Result:
    power_results: tuple[PowerResult, ...]
    traffic_results: tuple[TrafficStepResult, ...]
    power_service: np.ndarray
    transport_service: np.ndarray
    cumulative_power_service_loss_h: float
    cumulative_transport_service_loss_h: float
    completed_by_commodity: np.ndarray
    requested_by_commodity: np.ndarray


class M0Runner:
    """Independent H1 baseline.

    The API intentionally has no P↔T mapping. Power inputs and traffic inputs are
    accepted separately and passed to independent solvers. This structural choice
    is itself unit-tested as an EGMIV decoupling requirement.
    """

    def __init__(self, power: RadialNetwork, traffic: CTMNetwork) -> None:
        self.power = power
        self.traffic = traffic

    def run(
        self,
        p_demand_pu: np.ndarray,
        q_demand_pu: np.ndarray,
        power_line_available: np.ndarray,
        traffic_source_demand_vph: np.ndarray,
        initial_traffic_occupancy: np.ndarray,
        traffic_cell_available: np.ndarray,
        service_weights_power: np.ndarray | None = None,
        service_weights_transport: np.ndarray | None = None,
    ) -> M0Result:
        p = np.asarray(p_demand_pu, dtype=float)
        q = np.asarray(q_demand_pu, dtype=float)
        pa = np.asarray(power_line_available, dtype=bool)
        td = np.asarray(traffic_source_demand_vph, dtype=float)
        tc = np.asarray(traffic_cell_available, dtype=bool)
        occ = np.asarray(initial_traffic_occupancy, dtype=float).copy()

        K = p.shape[0]
        if q.shape != p.shape or p.shape[1] != self.power.n_buses:
            raise ValueError("Power demand arrays must be (K, n_buses).")
        if pa.shape != (K, len(self.power.lines)):
            raise ValueError("power_line_available must be (K, n_lines).")
        if td.shape != (K, self.traffic.n_cells, self.traffic.n_commodities):
            raise ValueError("traffic_source_demand_vph has incompatible shape.")
        if tc.shape != (K, self.traffic.n_cells):
            raise ValueError("traffic_cell_available must be (K, n_cells).")
        if occ.shape != (self.traffic.n_cells, self.traffic.n_commodities):
            raise ValueError("initial_traffic_occupancy has incompatible shape.")

        power_results = []
        traffic_results = []
        power_service = np.zeros(K)
        completed = np.zeros(self.traffic.n_commodities)
        requested = np.zeros(self.traffic.n_commodities)
        transport_service = np.zeros(K)
        wt = np.ones(self.traffic.n_commodities, dtype=float) if service_weights_transport is None else np.asarray(service_weights_transport, dtype=float)
        if wt.shape != (self.traffic.n_commodities,) or np.any(wt < 0):
            raise ValueError("service_weights_transport must be nonnegative with shape (n_commodities,).")

        for k in range(K):
            pr = self.power.solve(p[k], q[k], pa[k], service_weights_power)
            power_results.append(pr)
            power_service[k] = pr.service

            tr = self.traffic.step(occ, td[k], tc[k])
            traffic_results.append(tr)
            occ = tr.occupancy

            requested_flow_k = td[k].sum(axis=0)
            completed_flow_k = tr.completed_sink.sum(axis=0)
            requested += self.traffic.dt_h * requested_flow_k
            completed += self.traffic.dt_h * completed_flow_k
            requested_weighted = float(np.dot(wt, requested_flow_k))
            completed_weighted = float(np.dot(wt, completed_flow_k))
            transport_service[k] = 1.0 if requested_weighted <= 1e-15 else min(1.0, completed_weighted / requested_weighted)

        dt = self.traffic.dt_h
        return M0Result(
            power_results=tuple(power_results),
            traffic_results=tuple(traffic_results),
            power_service=power_service,
            transport_service=transport_service,
            cumulative_power_service_loss_h=cumulative_service_loss(power_service, dt),
            cumulative_transport_service_loss_h=cumulative_service_loss(transport_service, dt),
            completed_by_commodity=completed,
            requested_by_commodity=requested,
        )