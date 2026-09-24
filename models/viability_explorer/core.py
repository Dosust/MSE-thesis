"""Reduced coupled power--transport dynamics for visualization experiments.

This module is deliberately small and dependency-free. It is a *research
prototype*, not a calibrated infrastructure model. States are normalized to
[0, 1] and the vector field is constructed so the continuous-time dynamics
point inward at the unit-cube boundary for non-negative parameters.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from math import exp
from typing import Iterable, Iterator


@dataclass(frozen=True)
class State:
    """Normalized reduced state: power service, transport service, interface health."""

    power: float
    transport: float
    interface: float

    def validate(self, *, tol: float = 1e-12) -> None:
        for name, value in asdict(self).items():
            if not (-tol <= value <= 1.0 + tol):
                raise ValueError(f"{name}={value!r} lies outside normalized state domain [0, 1]")


@dataclass(frozen=True)
class Parameters:
    """Parameters for the reduced demonstrator.

    All rates are non-negative and expressed in inverse model-time units.
    Coupling terms represent loss amplification when the other service is low.
    """

    power_recovery: float = 0.16
    transport_recovery: float = 0.12
    interface_recovery: float = 0.10
    power_hazard: float = 0.36
    transport_hazard: float = 0.46
    interface_hazard: float = 0.40
    transport_to_power: float = 0.24
    power_to_transport: float = 0.32
    mismatch_to_interface: float = 0.20

    def validate(self) -> None:
        for name, value in asdict(self).items():
            if value < 0.0:
                raise ValueError(f"{name} must be non-negative, got {value!r}")


@dataclass(frozen=True)
class Derivative:
    power: float
    transport: float
    interface: float


@dataclass(frozen=True)
class Sample:
    time: float
    hazard: float
    state: State
    margin: float | None = None


def gaussian_flood(time: float, *, peak_time: float = 8.0, width: float = 2.4, amplitude: float = 0.92) -> float:
    """Deterministic smooth flood-intensity pulse bounded to [0, 1]."""

    if width <= 0.0:
        raise ValueError("width must be positive")
    if not (0.0 <= amplitude <= 1.0):
        raise ValueError("amplitude must lie in [0, 1]")
    z = (time - peak_time) / width
    return amplitude * exp(-0.5 * z * z)


def vector_field(state: State, hazard: float, params: Parameters) -> Derivative:
    """Evaluate the reduced coupled vector field.

    Model form::

        dP/dt = rP(1-P) - hP*eta*P - kTP(1-T)P
        dT/dt = rT(1-T) - hT*eta*T - kPT(1-P)T
        dC/dt = rC(1-C) - hC*eta*C - kM*|P-T|C

    The structure is intentionally interpretable. It encodes recovery toward
    service=1, direct hazard loss, and directional cross-sector degradation.
    """

    state.validate()
    params.validate()
    if not (0.0 <= hazard <= 1.0):
        raise ValueError(f"hazard must lie in [0, 1], got {hazard!r}")

    p, t, c = state.power, state.transport, state.interface
    dp = (
        params.power_recovery * (1.0 - p)
        - params.power_hazard * hazard * p
        - params.transport_to_power * (1.0 - t) * p
    )
    dt = (
        params.transport_recovery * (1.0 - t)
        - params.transport_hazard * hazard * t
        - params.power_to_transport * (1.0 - p) * t
    )
    dc = (
        params.interface_recovery * (1.0 - c)
        - params.interface_hazard * hazard * c
        - params.mismatch_to_interface * abs(p - t) * c
    )
    return Derivative(dp, dt, dc)


def _advance_rk4(state: State, time: float, dt: float, params: Parameters, hazard_fn) -> State:
    """One classical RK4 step with stage-wise hazard evaluation."""

    def add(s: State, k: Derivative, scale: float) -> State:
        return State(
            s.power + scale * k.power,
            s.transport + scale * k.transport,
            s.interface + scale * k.interface,
        )

    h1 = hazard_fn(time)
    k1 = vector_field(state, h1, params)
    s2 = add(state, k1, 0.5 * dt)
    s2 = State(*(min(1.0, max(0.0, x)) for x in (s2.power, s2.transport, s2.interface)))
    k2 = vector_field(s2, hazard_fn(time + 0.5 * dt), params)
    s3 = add(state, k2, 0.5 * dt)
    s3 = State(*(min(1.0, max(0.0, x)) for x in (s3.power, s3.transport, s3.interface)))
    k3 = vector_field(s3, hazard_fn(time + 0.5 * dt), params)
    s4 = add(state, k3, dt)
    s4 = State(*(min(1.0, max(0.0, x)) for x in (s4.power, s4.transport, s4.interface)))
    k4 = vector_field(s4, hazard_fn(time + dt), params)

    nxt = State(
        state.power + dt * (k1.power + 2 * k2.power + 2 * k3.power + k4.power) / 6.0,
        state.transport + dt * (k1.transport + 2 * k2.transport + 2 * k3.transport + k4.transport) / 6.0,
        state.interface + dt * (k1.interface + 2 * k2.interface + 2 * k3.interface + k4.interface) / 6.0,
    )
    bounded = State(*(min(1.0, max(0.0, x)) for x in (nxt.power, nxt.transport, nxt.interface)))
    bounded.validate()
    return bounded


def simulate(
    *,
    initial: State = State(0.96, 0.95, 0.93),
    params: Parameters = Parameters(),
    duration: float = 24.0,
    dt: float = 0.05,
    hazard_fn=gaussian_flood,
) -> list[Sample]:
    """Integrate the demonstrator using fixed-step RK4."""

    initial.validate()
    params.validate()
    if duration <= 0.0:
        raise ValueError("duration must be positive")
    if not (0.0 < dt <= 0.25):
        raise ValueError("dt must lie in (0, 0.25] for this demonstrator")

    n_steps = int(round(duration / dt))
    if abs(n_steps * dt - duration) > 1e-10:
        raise ValueError("duration must be an integer multiple of dt")

    out: list[Sample] = []
    state = initial
    for i in range(n_steps + 1):
        time = i * dt
        hazard = float(hazard_fn(time))
        if not (0.0 <= hazard <= 1.0):
            raise ValueError("hazard_fn must return values in [0, 1]")
        out.append(Sample(time=time, hazard=hazard, state=state))
        if i < n_steps:
            state = _advance_rk4(state, time, dt, params, hazard_fn)
    return out


def thin(samples: Iterable[Sample], every: int) -> Iterator[Sample]:
    """Yield every Nth sample while always retaining the last sample."""

    if every < 1:
        raise ValueError("every must be >= 1")
    seq = list(samples)
    if not seq:
        return iter(())
    selected = seq[::every]
    if selected[-1] is not seq[-1]:
        selected.append(seq[-1])
    return iter(selected)
