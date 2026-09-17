"""Reference decision primitives for canonical H4/H5.

These functions are verification instruments. They do not select interventions,
weights, materiality thresholds, or provide H4/H5 results.
"""
from __future__ import annotations

from math import isfinite
from typing import Hashable, Mapping, Sequence


class DecisionMathError(ValueError):
    """Raised for malformed multi-objective decision inputs."""


def _vector(values: Sequence[float]) -> tuple[float, ...]:
    out = tuple(float(x) for x in values)
    if not out or not all(isfinite(x) for x in out):
        raise DecisionMathError("objective vectors must be nonempty and finite")
    return out


def dominates(loss_a: Sequence[float], loss_b: Sequence[float], tol: float = 0.0) -> bool:
    """Return True when minimization vector a Pareto-dominates b.

    Tolerance is numerical only and must not be confused with an engineering
    materiality threshold.
    """
    if tol < 0 or not isfinite(float(tol)):
        raise DecisionMathError("tol must be finite and nonnegative")
    a = _vector(loss_a)
    b = _vector(loss_b)
    if len(a) != len(b):
        raise DecisionMathError("objective vectors must have equal dimension")
    no_worse = all(x <= y + tol for x, y in zip(a, b))
    strictly_better = any(x < y - tol for x, y in zip(a, b))
    return no_worse and strictly_better


def nondominated(objectives: Mapping[Hashable, Sequence[float]]) -> frozenset[Hashable]:
    """Return IDs not Pareto-dominated by another candidate."""
    if not objectives:
        raise DecisionMathError("candidate objective mapping must be nonempty")
    vectors = {key: _vector(value) for key, value in objectives.items()}
    dims = {len(v) for v in vectors.values()}
    if len(dims) != 1:
        raise DecisionMathError("all objective vectors must share one dimension")
    keep = []
    for key, vector in vectors.items():
        if not any(
            other != key and dominates(other_vector, vector)
            for other, other_vector in vectors.items()
        ):
            keep.append(key)
    return frozenset(keep)


def set_change_distance(a: Sequence[Hashable] | set[Hashable] | frozenset[Hashable],
                        b: Sequence[Hashable] | set[Hashable] | frozenset[Hashable]) -> float:
    """Jaccard distance used as a transparent H5 set-change diagnostic."""
    aa, bb = frozenset(a), frozenset(b)
    union = aa | bb
    if not union:
        raise DecisionMathError("set-change distance is undefined for two empty sets")
    return 1.0 - len(aa & bb) / len(union)


def sustainability_loss(accessibility: float, energy: float, carbon: float, cost: float) -> tuple[float, float, float, float]:
    """Orient J_sus=[-A,E,G,C] so every component is minimized."""
    values = (-float(accessibility), float(energy), float(carbon), float(cost))
    if not all(isfinite(x) for x in values):
        raise DecisionMathError("sustainability values must be finite")
    return values


def consequence_sign(delta_resilience: float, delta_loss: float, delta_r_tol: float = 0.0, delta_j_tol: float = 0.0) -> str:
    """Classify one resilience/sustainability component consequence.

    Positive delta_resilience is better. Sustainability is represented as a
    loss, so negative delta_loss is better. Tolerances must be preregistered for
    confirmatory use; defaults are for software verification only.
    """
    dr, dj = float(delta_resilience), float(delta_loss)
    rtol, jtol = float(delta_r_tol), float(delta_j_tol)
    if not all(isfinite(x) for x in (dr, dj, rtol, jtol)) or rtol < 0 or jtol < 0:
        raise DecisionMathError("effects/tolerances must be finite and tolerances nonnegative")
    r_improves = dr > rtol
    j_improves = dj < -jtol
    j_worsens = dj > jtol
    if r_improves and j_improves:
        return "SYNERGY"
    if r_improves and j_worsens:
        return "TRADE_OFF"
    if r_improves:
        return "RESILIENCE_GAIN_SUSTAINABILITY_NEUTRAL_WITHIN_TOL"
    return "NO_QUALIFIED_RESILIENCE_GAIN"
