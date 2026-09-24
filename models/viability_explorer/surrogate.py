"""Small deterministic ML surrogate for the synthetic reduced vector field."""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from .core import Derivative, Parameters, State, vector_field


def features(state: State, hazard: float) -> tuple[float, ...]:
    p, t, c = state.power, state.transport, state.interface
    return (
        1.0, p, t, c, hazard, hazard * p, hazard * t, hazard * c,
        (1.0 - t) * p, (1.0 - p) * t, abs(p - t) * c,
        1.0 - p, 1.0 - t, 1.0 - c,
    )


def _solve_linear(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    aug = [row[:] + [rhs] for row, rhs in zip(a, b)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-14:
            raise ValueError("singular regression system")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v / scale for v in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def _ridge_fit(x: list[tuple[float, ...]], y: list[float], ridge: float) -> tuple[float, ...]:
    if ridge < 0.0:
        raise ValueError("ridge must be non-negative")
    d = len(x[0])
    gram = [[0.0] * d for _ in range(d)]
    rhs = [0.0] * d
    for row, target in zip(x, y):
        for i in range(d):
            rhs[i] += row[i] * target
            for j in range(d):
                gram[i][j] += row[i] * row[j]
    for i in range(d):
        gram[i][i] += ridge
    return tuple(_solve_linear(gram, rhs))


@dataclass(frozen=True)
class LinearVectorFieldSurrogate:
    power_coefficients: tuple[float, ...]
    transport_coefficients: tuple[float, ...]
    interface_coefficients: tuple[float, ...]

    def predict(self, state: State, hazard: float) -> Derivative:
        phi = features(state, hazard)

        def dot(coefs: tuple[float, ...]) -> float:
            return sum(a * b for a, b in zip(coefs, phi))

        return Derivative(
            dot(self.power_coefficients),
            dot(self.transport_coefficients),
            dot(self.interface_coefficients),
        )


def synthetic_training_data(params: Parameters = Parameters()) -> tuple[list[tuple[float, ...]], list[Derivative]]:
    levels = (0.15, 0.35, 0.55, 0.75, 0.95)
    hazards = (0.0, 0.2, 0.5, 0.8, 1.0)
    x: list[tuple[float, ...]] = []
    y: list[Derivative] = []
    for p in levels:
        for t in levels:
            for c in (0.2, 0.5, 0.8):
                for h in hazards:
                    state = State(p, t, c)
                    x.append(features(state, h))
                    y.append(vector_field(state, h, params))
    return x, y


def train_surrogate(params: Parameters = Parameters(), *, ridge: float = 1e-9) -> LinearVectorFieldSurrogate:
    x, targets = synthetic_training_data(params)
    return LinearVectorFieldSurrogate(
        _ridge_fit(x, [d.power for d in targets], ridge),
        _ridge_fit(x, [d.transport for d in targets], ridge),
        _ridge_fit(x, [d.interface for d in targets], ridge),
    )


def validation_rmse(model: LinearVectorFieldSurrogate, params: Parameters = Parameters()) -> dict[str, float]:
    points = (
        (0.22, 0.44, 0.66, 0.11),
        (0.41, 0.63, 0.37, 0.33),
        (0.68, 0.27, 0.72, 0.57),
        (0.83, 0.61, 0.29, 0.74),
        (0.91, 0.86, 0.81, 0.93),
    )
    errors = {"power": [], "transport": [], "interface": []}
    for p, t, c, h in points:
        s = State(p, t, c)
        truth = vector_field(s, h, params)
        pred = model.predict(s, h)
        errors["power"].append((pred.power - truth.power) ** 2)
        errors["transport"].append((pred.transport - truth.transport) ** 2)
        errors["interface"].append((pred.interface - truth.interface) ** 2)
    return {name: sqrt(sum(vals) / len(vals)) for name, vals in errors.items()}
