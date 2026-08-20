"""Reference numerical utilities for thesis viability/recovery geometry.

This module is intentionally small and auditable. It does not claim to solve the
full thesis model. It provides reproducible primitives for toy/synthetic tests,
geometry QA, and figure generation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable
import math

Point = tuple[float, float]


@dataclass(frozen=True)
class Rectangle:
    """Axis-aligned admissible set used for deterministic smoke tests."""

    xmin: float
    xmax: float
    ymin: float
    ymax: float

    def contains(self, p: Point) -> bool:
        x, y = p
        return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax


def euler_step(
    x: Point,
    dt: float,
    field: Callable[[Point, float], Point],
    t: float,
) -> Point:
    """One explicit Euler step for a 2-D reference system."""
    fx, fy = field(x, t)
    return x[0] + dt * fx, x[1] + dt * fy


def trajectory_is_admissible(
    x0: Point,
    admissible: Rectangle,
    field: Callable[[Point, float], Point],
    horizon: float,
    dt: float,
) -> bool:
    """Return True if a deterministic reference trajectory stays admissible."""
    if dt <= 0 or horizon < 0:
        raise ValueError("Require dt > 0 and horizon >= 0")
    x = x0
    t = 0.0
    if not admissible.contains(x):
        return False
    while t < horizon - 1e-15:
        step = min(dt, horizon - t)
        x = euler_step(x, step, field, t)
        t += step
        if not admissible.contains(x):
            return False
    return True


def grid_points(rect: Rectangle, nx: int, ny: int) -> Iterable[Point]:
    """Generate a deterministic Cartesian grid including rectangle boundaries."""
    if nx < 2 or ny < 2:
        raise ValueError("nx and ny must be at least 2")
    for j in range(ny):
        y = rect.ymin + (rect.ymax - rect.ymin) * j / (ny - 1)
        for i in range(nx):
            x = rect.xmin + (rect.xmax - rect.xmin) * i / (nx - 1)
            yield (x, y)


def approximate_viable_grid(
    admissible: Rectangle,
    field: Callable[[Point, float], Point],
    horizon: float,
    dt: float,
    nx: int = 81,
    ny: int = 81,
) -> list[Point]:
    """Approximate finite-horizon viable points for a deterministic smoke test.

    The full thesis viability problem is controlled, uncertain, hybrid, and
    higher-dimensional. This finite-grid routine is only a transparent baseline.
    """
    return [
        p
        for p in grid_points(admissible, nx, ny)
        if trajectory_is_admissible(p, admissible, field, horizon, dt)
    ]


def directed_hausdorff(a: Iterable[Point], b: Iterable[Point]) -> float:
    """Compute directed Hausdorff distance between finite 2-D point clouds."""
    aa, bb = list(a), list(b)
    if not aa or not bb:
        raise ValueError("Point clouds must be non-empty")

    def dist(p: Point, q: Point) -> float:
        return math.hypot(p[0] - q[0], p[1] - q[1])

    return max(min(dist(p, q) for q in bb) for p in aa)


def hausdorff_distance(a: Iterable[Point], b: Iterable[Point]) -> float:
    """Symmetric Hausdorff distance for finite point clouds."""
    aa, bb = list(a), list(b)
    return max(directed_hausdorff(aa, bb), directed_hausdorff(bb, aa))


def static_interface_field(zbar: float) -> Callable[[Point, float], Point]:
    """Reference static-interface vector field with a nontrivial safe-set boundary.

    The weakly unstable x1 direction is deliberate: it ensures the finite-horizon
    admissible set is a proper subset of K, so dynamic/static interface changes can
    produce a measurable synthetic boundary deformation.
    """
    def field(x: Point, _t: float) -> Point:
        x1, x2 = x
        return (0.18 * x1 + zbar * x2, -0.12 * x2 + 0.18 * x1)
    return field


def dynamic_interface_field(
    z0: float = 0.25,
    amplitude: float = 0.18,
    omega: float = 1.0,
) -> Callable[[Point, float], Point]:
    """Reference time-varying interface field used only for P1 synthetic QA."""
    def field(x: Point, t: float) -> Point:
        x1, x2 = x
        z = z0 + amplitude * math.sin(omega * t)
        return (0.18 * x1 + z * x2, -0.12 * x2 + 0.18 * x1)
    return field


def demo_boundary_deformation() -> dict[str, float | int]:
    """Reproducible P1 smoke test: dynamic vs static finite-horizon viability.

    Expected reference behavior on the default 81x81 grid:
      * both viable sets are non-empty and proper subsets of K;
      * dynamic and static approximations are not identical;
      * the grid-based Hausdorff distance is positive.

    These are software/geometry checks, not empirical thesis results.
    """
    k = Rectangle(-1.0, 1.0, -1.0, 1.0)
    v_static = approximate_viable_grid(k, static_interface_field(0.25), 5.0, 0.02)
    v_dynamic = approximate_viable_grid(k, dynamic_interface_field(), 5.0, 0.02)
    return {
        "n_grid": 81 * 81,
        "n_static": len(v_static),
        "n_dynamic": len(v_dynamic),
        "hausdorff_grid_distance": hausdorff_distance(v_static, v_dynamic),
    }


if __name__ == "__main__":
    print(demo_boundary_deformation())
