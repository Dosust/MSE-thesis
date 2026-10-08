"""Model-independent mathematical QA examples for state/time diagrams.

All examples are DIMENSIONLESS SYNTHETIC SOFTWARE TESTS.
This is NOT a transformer, EVSE, battery, service, or resilience model.
No equipment thresholds or case parameters are supplied.

Definitions require case-specific source/validation before thesis use.
"""
from __future__ import annotations

from math import isfinite
from typing import Sequence, Optional


def _check_time(time: Sequence[float]) -> None:
    if len(time) < 2:
        raise ValueError("time requires at least two samples")
    if any(not isfinite(float(x)) for x in time):
        raise ValueError("time contains a non-finite sample")
    if any(float(time[i + 1]) <= float(time[i]) for i in range(len(time) - 1)):
        raise ValueError("time must increase strictly")


def _check_series(time: Sequence[float], values: Sequence[float], label: str) -> None:
    if len(values) != len(time):
        raise ValueError(f"{label} length must equal time length")
    if any(not isfinite(float(x)) for x in values):
        raise ValueError(f"{label} contains a non-finite sample")


def first_downward_threshold_time(
    time: Sequence[float],
    state: Sequence[float],
    threshold: float,
) -> Optional[float]:
    """First x(t) <= threshold, using piecewise-linear interpolation.

    Returns None if the declared threshold is never reached on sampled horizon.
    Crossing uncertainty from sampling/measurement is not quantified here.
    Units of result equal the caller's documented time units.
    """
    _check_time(time)
    _check_series(time, state, "state")
    if not isfinite(float(threshold)):
        raise ValueError("threshold must be finite")
    if state[0] <= threshold:
        return float(time[0])
    for i in range(1, len(time)):
        a, b = float(state[i - 1]), float(state[i])
        if a > threshold >= b:
            # b < a by guard; denominator cannot be zero.
            alpha = (a - threshold) / (a - b)
            return float(time[i - 1]) + alpha * (float(time[i]) - float(time[i - 1]))
    return None


def propagation_delay(
    source_event_time: float,
    receiver_event_time: float,
    *,
    require_nonnegative: bool = True,
) -> float:
    """Event-time difference; **not** proof of a causal dependency.

    To interpret as propagation, separately qualify the source→receiver mechanism,
    event definitions, timing accuracy, and common time coordinate.
    """
    if not all(isfinite(float(t)) for t in (source_event_time, receiver_event_time)):
        raise ValueError("event times must be finite")
    delay = float(receiver_event_time) - float(source_event_time)
    if require_nonnegative and delay < 0:
        raise ValueError("receiver precedes source; review ordering/definitions")
    return delay


def positive_service_deficit_integral(
    time: Sequence[float],
    service: Sequence[float],
    requirement: Sequence[float],
    *,
    time_unit: str,
    service_unit: str,
) -> float:
    """Integrate positive (required-service) gap under linear segment assumptions.

    Output units are 'service_unit * time_unit'. The quantity is an integral of a
    defined service deficit, NOT by itself a validated resilience metric.
    Each sign-changing segment is split at its exact linear crossing point.
    """
    _check_time(time)
    _check_series(time, service, "service")
    _check_series(time, requirement, "requirement")
    if not time_unit.strip() or not service_unit.strip():
        raise ValueError("declare nonempty time and service units")
    total = 0.0
    for i in range(len(time) - 1):
        dt = float(time[i + 1]) - float(time[i])
        left = float(requirement[i]) - float(service[i])
        right = float(requirement[i + 1]) - float(service[i + 1])
        if left >= 0 and right >= 0:
            area = dt * (left + right) / 2
        elif left <= 0 and right <= 0:
            area = 0.0
        else:
            fraction = abs(left) / (abs(left) + abs(right))
            area = (dt * fraction * left / 2) if left > 0 else (dt * (1 - fraction) * right / 2)
        total += area
    return total


if __name__ == "__main__":
    # Explicitly dimensionless manufactured unit-test sequences; NOT physical data.
    t = [0.0, 1.0, 2.0]
    x = [0.9, 0.7, 0.4]
    tau = first_downward_threshold_time(t, x, 0.5)
    assert tau is not None and abs(tau - 5.0 / 3.0) < 1e-12
    deficit = positive_service_deficit_integral(
        t, [1.0, 0.4, 1.0], [0.8, 0.8, 0.8],
        time_unit="dimensionless-time", service_unit="dimensionless-service")
    assert abs(deficit - 4.0 / 15.0) < 1e-12
    print("PASS: synthetic first-passage and positive-gap integration tests")
    print("UNITS: dimensionless; NOT TRANSFORMER OR EVSE DATA; NOT PHYSICAL VALIDATION")
