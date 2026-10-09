"""Original math reference for synthetic shader lessons, not a physical or empirical model.

Educational concepts attributed to Gonzalez Vivo & Lowe, The Book of Shaders,
Chapter 10, https://thebookofshaders.com/10/. No copied source code.
"""

from __future__ import annotations

import math

SEED = 20261009
TWO_TO_24 = 16777216


def fract(x: float) -> float:
    """Mathematical fractional part on finite real-valued input."""
    if not math.isfinite(x):
        raise ValueError("x must be finite")
    return x - math.floor(x)


def fractional_sine(x: float) -> float:
    """Deterministic discontinuous shader lesson; no IID/uniformity claim."""
    return fract(173.7 * math.sin(4.37 * x + 0.21))


def power_quantile(u: float, gamma: float) -> float:
    """Return u^gamma on [0,1], gamma>0; probability law assumes U uniform."""
    if not math.isfinite(u) or not math.isfinite(gamma):
        raise ValueError("u and gamma must be finite")
    if not (0 <= u <= 1) or gamma <= 0:
        raise ValueError("require 0 <= u <= 1 and gamma > 0")
    return u**gamma


def cell_position(x: float, y: float, scale: float) -> tuple[tuple[int, int], tuple[float, float]]:
    """Map dimensionless global coordinates to integer cell + local fractions."""
    if not all(math.isfinite(v) for v in (x, y, scale)) or scale <= 0:
        raise ValueError("coordinates must be finite and scale positive")
    scaled_x, scaled_y = x * scale, y * scale
    if not math.isfinite(scaled_x) or not math.isfinite(scaled_y):
        raise ValueError("coordinate scaling exceeds finite range")
    ix, iy = math.floor(scaled_x), math.floor(scaled_y)
    return (ix, iy), (scaled_x - ix, scaled_y - iy)


def hash_cell(col: int, row: int, seed: int = SEED) -> float:
    """Reproducible 24-bit coordinate hash; not a scientific RNG."""
    if any(type(v) is not int for v in (col, row, seed)):
        raise ValueError("cell coordinates/seed must be integers")
    if not (-2**31 <= col < 2**31 and -2**31 <= row < 2**31 and 0 <= seed < 2**32):
        raise ValueError("cell coordinates must be int32, seed must be uint32")

    h = ((col * 0x9E3779B1) ^ (row * 0x85EBCA77) ^ seed) & 0xFFFFFFFF
    h ^= h >> 16
    h = (h * 0x7FEB352D) & 0xFFFFFFFF
    h ^= h >> 15
    h = (h * 0x846CA68B) & 0xFFFFFFFF
    h ^= h >> 16
    return (h >> 8) / TWO_TO_24


def row_displacement(t: float, v0: float, amplitude: float, omega: float, phase: float) -> float:
    """Integrate synthetic velocity v0+a sin(omega*t+phase) from zero to t."""
    if not all(math.isfinite(v) for v in (t, v0, amplitude, omega, phase)):
        raise ValueError("parameters must be finite")
    if t < 0:
        raise ValueError("display time must be nonnegative")
    if omega == 0.0:
        return (v0 + amplitude * math.sin(phase)) * t
    return v0 * t + amplitude / omega * (math.cos(phase) - math.cos(omega * t + phase))
