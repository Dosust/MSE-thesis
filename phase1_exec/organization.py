"""Organizational/access restoration timing operators."""
from math import inf


def restoration_time(
    tau_decision: float,
    tau_mobilization: float,
    crew_travel: float,
    tau_repair: float,
) -> float:
    values = (tau_decision, tau_mobilization, crew_travel, tau_repair)
    if any(value < 0.0 for value in values):
        raise ValueError("restoration-time components must be nonnegative")
    if crew_travel == inf:
        return inf
    return sum(values)


def energization_guard(time_min: float, restoration_time_min: float) -> int:
    return int(time_min >= restoration_time_min)
