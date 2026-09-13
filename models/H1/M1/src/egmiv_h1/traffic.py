from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping
import numpy as np


@dataclass(frozen=True)
class Cell:
    length_km: float
    free_speed_kmh: float
    wave_speed_kmh: float
    jam_density_veh_per_km: float
    capacity_veh_per_h: float
    sink_capacity_veh_per_h: float = 0.0

    def __post_init__(self) -> None:
        vals = [self.length_km, self.free_speed_kmh, self.wave_speed_kmh,
                self.jam_density_veh_per_km, self.capacity_veh_per_h]
        if any(v <= 0 for v in vals):
            raise ValueError("Cell length, speeds, jam density and capacity must be positive.")
        if self.sink_capacity_veh_per_h < 0:
            raise ValueError("sink_capacity_veh_per_h must be nonnegative.")

    @property
    def jam_vehicles(self) -> float:
        return self.jam_density_veh_per_km * self.length_km


@dataclass(frozen=True)
class Turn:
    upstream: int
    downstream: int
    commodity: int
    fraction: float

    def __post_init__(self) -> None:
        if not 0.0 <= self.fraction <= 1.0:
            raise ValueError("Turn fraction must be in [0,1].")


@dataclass(frozen=True)
class TrafficStepResult:
    occupancy: np.ndarray
    internal_flow: np.ndarray
    admitted_source: np.ndarray
    completed_sink: np.ndarray
    conservation_residual_by_commodity_veh: np.ndarray
    max_conservation_residual_veh: float
    min_occupancy_veh: float
    max_jam_excess_veh: float


class CTMNetwork:
    """Multi-commodity Cell Transmission Model with fixed routing.

    State occupancy has shape (n_cells, n_commodities) in vehicles. All flows are
    vehicles/hour. Source demand is offered at network boundaries and is admitted
    only up to downstream receiving capacity. Sink discharge is explicit and
    contributes to completed trips by commodity.

    M0 contains no power variables and no charger-state dependence.
    """

    def __init__(
        self,
        cells: Iterable[Cell],
        n_commodities: int,
        turns: Iterable[Turn],
        dt_h: float,
    ) -> None:
        self.cells = tuple(cells)
        self.n_cells = len(self.cells)
        self.n_commodities = int(n_commodities)
        self.turns = tuple(turns)
        self.dt_h = float(dt_h)
        if self.n_cells < 1 or self.n_commodities < 1:
            raise ValueError("Need at least one cell and one commodity.")
        if self.dt_h <= 0:
            raise ValueError("dt_h must be positive.")
        self._validate_turns()
        self._validate_cfl()
        self.turn_fraction = np.zeros((self.n_cells, self.n_cells, self.n_commodities), dtype=float)
        for t in self.turns:
            self.turn_fraction[t.upstream, t.downstream, t.commodity] += t.fraction

    def _validate_turns(self) -> None:
        sums: dict[tuple[int, int], float] = {}
        for t in self.turns:
            if not (0 <= t.upstream < self.n_cells and 0 <= t.downstream < self.n_cells):
                raise ValueError("Turn endpoint outside cell set.")
            if not (0 <= t.commodity < self.n_commodities):
                raise ValueError("Turn commodity outside commodity set.")
            key = (t.upstream, t.commodity)
            sums[key] = sums.get(key, 0.0) + t.fraction
        if any(v > 1.0 + 1e-12 for v in sums.values()):
            raise ValueError("Outgoing turn fractions for a cell/commodity cannot exceed 1.")

    def _validate_cfl(self) -> None:
        for idx, c in enumerate(self.cells):
            # Explicit CTM requires a vehicle not to traverse more than one cell per step.
            dt_max = c.length_km / max(c.free_speed_kmh, c.wave_speed_kmh)
            if self.dt_h > dt_max + 1e-12:
                raise ValueError(
                    f"CFL violation in cell {idx}: dt_h={self.dt_h:g} > {dt_max:g} h."
                )

    def sending(self, occupancy: np.ndarray) -> np.ndarray:
        total = occupancy.sum(axis=1)
        return np.array([
            min(c.free_speed_kmh / c.length_km * total[i], c.capacity_veh_per_h)
            for i, c in enumerate(self.cells)
        ], dtype=float)

    def receiving(self, occupancy: np.ndarray) -> np.ndarray:
        total = occupancy.sum(axis=1)
        return np.array([
            max(0.0, min(c.capacity_veh_per_h,
                         c.wave_speed_kmh / c.length_km * (c.jam_vehicles - total[i])))
            for i, c in enumerate(self.cells)
        ], dtype=float)

    def step(
        self,
        occupancy: np.ndarray,
        source_demand_vph: np.ndarray | None = None,
        cell_available: np.ndarray | None = None,
    ) -> TrafficStepResult:
        n = np.asarray(occupancy, dtype=float)
        if n.shape != (self.n_cells, self.n_commodities):
            raise ValueError("occupancy shape must be (n_cells, n_commodities).")
        if np.any(n < -1e-12):
            raise ValueError("Occupancy cannot be negative.")

        source = np.zeros_like(n) if source_demand_vph is None else np.asarray(source_demand_vph, dtype=float)
        if source.shape != n.shape or np.any(source < -1e-12):
            raise ValueError("source_demand_vph must be nonnegative with occupancy shape.")

        avail = np.ones(self.n_cells, dtype=bool) if cell_available is None else np.asarray(cell_available, dtype=bool)
        if avail.shape != (self.n_cells,):
            raise ValueError("cell_available must have shape (n_cells,).")

        S = self.sending(n) * avail
        R = self.receiving(n) * avail
        total_n = n.sum(axis=1)
        composition = np.divide(n, total_n[:, None], out=np.zeros_like(n), where=total_n[:, None] > 1e-15)

        # Desired turn flows before downstream receiving constraint.
        desired = np.zeros((self.n_cells, self.n_cells, self.n_commodities), dtype=float)
        for i in range(self.n_cells):
            for k in range(self.n_commodities):
                if composition[i, k] <= 0:
                    continue
                desired[i, :, k] = S[i] * composition[i, k] * self.turn_fraction[i, :, k]

        # Each downstream cell shares its receiving capacity proportionally among internal and external demand.
        internal_flow = np.zeros_like(desired)
        admitted_source = np.zeros_like(source)
        for j in range(self.n_cells):
            incoming_internal = float(desired[:, j, :].sum())
            incoming_source = float(source[j, :].sum())
            total_desired = incoming_internal + incoming_source
            scale = 1.0 if total_desired <= R[j] + 1e-15 else (R[j] / total_desired if total_desired > 0 else 0.0)
            internal_flow[:, j, :] = desired[:, j, :] * scale
            admitted_source[j, :] = source[j, :] * scale

        # Sink completion. Residual sending not assigned to turns can leave through an explicit sink.
        completed_sink = np.zeros((self.n_cells, self.n_commodities), dtype=float)
        for i, c in enumerate(self.cells):
            if not avail[i] or c.sink_capacity_veh_per_h <= 0 or total_n[i] <= 1e-15:
                continue
            used_sending = float(internal_flow[i, :, :].sum())
            residual_send = max(0.0, S[i] - used_sending)
            sink_total = min(c.sink_capacity_veh_per_h, residual_send)
            completed_sink[i, :] = sink_total * composition[i, :]

        inflow = internal_flow.sum(axis=0)  # (cell, commodity)
        outflow = internal_flow.sum(axis=1) # (cell, commodity)
        rhs = inflow + admitted_source - outflow - completed_sink
        n_next = n + self.dt_h * rhs

        # Floating-point guard only; meaningful negative states are errors.
        if n_next.min(initial=0.0) < -1e-9:
            raise RuntimeError("CTM produced negative occupancy; check CFL/node model.")
        n_next = np.maximum(n_next, 0.0)

        # Commodity-wise conservation: internal flows cancel within each commodity.
        lhs_by_k = n_next.sum(axis=0)
        rhs_by_k = n.sum(axis=0) + self.dt_h * (admitted_source.sum(axis=0) - completed_sink.sum(axis=0))
        residual_by_k = np.abs(lhs_by_k - rhs_by_k)
        residual = float(residual_by_k.max(initial=0.0))

        jam_excess = max(
            [max(0.0, n_next[i].sum() - c.jam_vehicles) for i, c in enumerate(self.cells)],
            default=0.0,
        )

        return TrafficStepResult(
            occupancy=n_next,
            internal_flow=internal_flow,
            admitted_source=admitted_source,
            completed_sink=completed_sink,
            conservation_residual_by_commodity_veh=residual_by_k,
            max_conservation_residual_veh=float(residual),
            min_occupancy_veh=float(n_next.min(initial=0.0)),
            max_jam_excess_veh=float(jam_excess),
        )