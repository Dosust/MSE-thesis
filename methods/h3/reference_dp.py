"""Reference finite-state viability and reach-avoid dynamic programming.

Purpose
-------
This module is a verification instrument for H3, not the final infrastructure
solver. It implements exact finite-state dynamic programming on explicitly
declared transition probabilities so that structural H3 identities can be
unit-tested before a higher-dimensional method is selected.

Scientific role
---------------
- verifies probability bounds;
- verifies confidence-threshold nesting;
- verifies viability-horizon nesting;
- verifies recovery-horizon monotonicity;
- verifies increased control authority cannot reduce optimal probability;
- verifies deterministic limits as degenerate transition distributions.

No Houston-specific parameter, threshold, probability distribution, or
confirmatory result is encoded here.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from math import isclose
from typing import TypeVar

State = TypeVar("State", bound=Hashable)
Action = TypeVar("Action", bound=Hashable)

Transition = Callable[[State, Action], Mapping[State, float]]
ActionMap = Callable[[State], Iterable[Action]]


@dataclass(frozen=True)
class DPResult:
    """Finite-horizon value functions indexed by remaining steps.

    ``values[h][x]`` is the optimal probability for state ``x`` with exactly
    ``h`` future transitions available. ``values[0]`` is the terminal value.
    """

    values: tuple[dict[Hashable, float], ...]

    def at(self, horizon: int, state: Hashable) -> float:
        return self.values[horizon][state]


def _validated_distribution(dist: Mapping[State, float], *, tol: float = 1e-12) -> None:
    if not dist:
        raise ValueError("transition distribution must be non-empty")
    if any((p < -tol or p > 1.0 + tol) for p in dist.values()):
        raise ValueError("transition probabilities must lie in [0, 1]")
    total = sum(dist.values())
    if not isclose(total, 1.0, abs_tol=tol, rel_tol=0.0):
        raise ValueError(f"transition probabilities must sum to one, got {total!r}")


def _expectation(
    dist: Mapping[State, float],
    continuation: Mapping[State, float],
) -> float:
    _validated_distribution(dist)
    try:
        value = sum(float(p) * float(continuation[x_next]) for x_next, p in dist.items())
    except KeyError as exc:
        raise ValueError(f"transition reaches undeclared state {exc.args[0]!r}") from exc
    # Numerical guard only; exact finite-state recursions should already obey this.
    return min(1.0, max(0.0, value))


def finite_horizon_viability(
    states: Sequence[State],
    actions: ActionMap,
    transition: Transition,
    safe: Callable[[State], bool],
    max_horizon: int,
) -> DPResult:
    """Compute optimal probability of remaining in ``safe`` for h steps.

    A state outside the safe set has value zero. A safe state at horizon zero
    has value one. For h>0, the controller selects the admissible action that
    maximizes expected continuation probability.
    """

    if max_horizon < 0:
        raise ValueError("max_horizon must be non-negative")
    state_tuple = tuple(states)
    if len(set(state_tuple)) != len(state_tuple):
        raise ValueError("states must be unique")

    values: list[dict[Hashable, float]] = [
        {x: 1.0 if safe(x) else 0.0 for x in state_tuple}
    ]
    for _h in range(1, max_horizon + 1):
        prev = values[-1]
        current: dict[Hashable, float] = {}
        for x in state_tuple:
            if not safe(x):
                current[x] = 0.0
                continue
            feasible_actions = tuple(actions(x))
            if not feasible_actions:
                current[x] = 0.0
                continue
            current[x] = max(
                _expectation(transition(x, u), prev) for u in feasible_actions
            )
        values.append(current)
    return DPResult(tuple(values))


def finite_horizon_reach_avoid(
    states: Sequence[State],
    actions: ActionMap,
    transition: Transition,
    target: Callable[[State], bool],
    avoid: Callable[[State], bool],
    max_horizon: int,
) -> DPResult:
    """Compute optimal probability of hitting target within h steps, avoiding F.

    Target states are successful absorbing evaluation states with value one.
    Avoid states have value zero. Other states optimize the expected probability
    of future target entry.
    """

    if max_horizon < 0:
        raise ValueError("max_horizon must be non-negative")
    state_tuple = tuple(states)
    if len(set(state_tuple)) != len(state_tuple):
        raise ValueError("states must be unique")
    overlap = [x for x in state_tuple if target(x) and avoid(x)]
    if overlap:
        raise ValueError("target and avoid sets must be disjoint")

    values: list[dict[Hashable, float]] = [
        {x: 1.0 if target(x) else 0.0 for x in state_tuple}
    ]
    for _h in range(1, max_horizon + 1):
        prev = values[-1]
        current: dict[Hashable, float] = {}
        for x in state_tuple:
            if target(x):
                current[x] = 1.0
                continue
            if avoid(x):
                current[x] = 0.0
                continue
            feasible_actions = tuple(actions(x))
            if not feasible_actions:
                current[x] = 0.0
                continue
            current[x] = max(
                _expectation(transition(x, u), prev) for u in feasible_actions
            )
        values.append(current)
    return DPResult(tuple(values))


def confidence_set(
    result: DPResult,
    horizon: int,
    threshold: float,
) -> frozenset[Hashable]:
    """Return states whose value is at least the declared confidence threshold."""

    if threshold < 0.0 or threshold > 1.0:
        raise ValueError("threshold must lie in [0, 1]")
    values = result.values[horizon]
    return frozenset(x for x, p in values.items() if p >= threshold)
