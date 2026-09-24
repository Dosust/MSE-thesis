"""Constraint geometry and sensitivity diagnostics for the demonstrator.

Important terminology:
- SustainableConstraints defines an admissible threshold set K_sus.
- constraint_margin is a signed distance-to-threshold proxy under a diagonal metric.
- This module does not compute a viability kernel. A viability kernel requires
  explicit control admissibility and reachability/invariance analysis.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from math import sqrt
from typing import Iterable

from .core import Parameters, Sample, State, simulate


@dataclass(frozen=True)
class SustainableConstraints:
    min_power: float = 0.62
    min_transport: float = 0.58
    min_interface: float = 0.55

    def validate(self) -> None:
        for name, value in self.__dict__.items():
            if not (0.0 <= value <= 1.0):
                raise ValueError(f"{name} must lie in [0, 1]")


@dataclass(frozen=True)
class DiagonalMetric:
    power_weight: float = 1.0
    transport_weight: float = 1.0
    interface_weight: float = 0.75

    def validate(self) -> None:
        for name, value in self.__dict__.items():
            if value <= 0.0:
                raise ValueError(f"{name} must be strictly positive")


@dataclass(frozen=True)
class CriticalityResult:
    parameter: str
    baseline_min_margin: float
    perturbed_min_margin: float
    delta: float
    sensitivity: float


def constraint_margin(
    state: State,
    constraints: SustainableConstraints = SustainableConstraints(),
    metric: DiagonalMetric = DiagonalMetric(),
) -> float:
    """Signed minimum distance to axis-aligned sustainability thresholds."""

    state.validate()
    constraints.validate()
    metric.validate()
    distances = (
        sqrt(metric.power_weight) * (state.power - constraints.min_power),
        sqrt(metric.transport_weight) * (state.transport - constraints.min_transport),
        sqrt(metric.interface_weight) * (state.interface - constraints.min_interface),
    )
    return min(distances)


def annotate_margins(
    samples: Iterable[Sample],
    constraints: SustainableConstraints = SustainableConstraints(),
    metric: DiagonalMetric = DiagonalMetric(),
) -> list[Sample]:
    return [
        Sample(
            time=s.time,
            hazard=s.hazard,
            state=s.state,
            margin=constraint_margin(s.state, constraints, metric),
        )
        for s in samples
    ]


def minimum_margin(samples: Iterable[Sample]) -> float:
    margins = [s.margin for s in samples]
    if not margins:
        raise ValueError("samples must not be empty")
    if any(m is None for m in margins):
        raise ValueError("all samples must be margin-annotated")
    return min(float(m) for m in margins)


def parameter_criticality(
    *,
    parameter: str,
    delta: float = 0.02,
    params: Parameters = Parameters(),
    constraints: SustainableConstraints = SustainableConstraints(),
    metric: DiagonalMetric = DiagonalMetric(),
    duration: float = 24.0,
    dt: float = 0.05,
) -> CriticalityResult:
    """Finite-difference sensitivity of minimum constraint margin to a parameter.

    This is a model diagnostic, not causal identification.
    """

    if parameter not in params.__dict__:
        raise ValueError(f"unknown parameter: {parameter}")
    if delta == 0.0:
        raise ValueError("delta must be non-zero")
    candidate = getattr(params, parameter) + delta
    if candidate < 0.0:
        raise ValueError("perturbation would make a non-negative rate negative")

    base = annotate_margins(simulate(params=params, duration=duration, dt=dt), constraints, metric)
    perturbed_params = replace(params, **{parameter: candidate})
    perturbed = annotate_margins(
        simulate(params=perturbed_params, duration=duration, dt=dt), constraints, metric
    )
    base_min = minimum_margin(base)
    pert_min = minimum_margin(perturbed)
    return CriticalityResult(
        parameter=parameter,
        baseline_min_margin=base_min,
        perturbed_min_margin=pert_min,
        delta=delta,
        sensitivity=(pert_min - base_min) / delta,
    )
