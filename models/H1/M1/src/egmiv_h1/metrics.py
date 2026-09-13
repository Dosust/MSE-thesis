from __future__ import annotations
import numpy as np


def cumulative_service_loss(service: np.ndarray, dt_h: float) -> float:
    s = np.asarray(service, dtype=float)
    if s.ndim != 1:
        raise ValueError("service must be one-dimensional.")
    if dt_h <= 0:
        raise ValueError("dt_h must be positive.")
    if np.any((s < -1e-12) | (s > 1.0 + 1e-12)):
        raise ValueError("service values must be in [0,1].")
    return float(np.sum(1.0 - np.clip(s, 0.0, 1.0)) * dt_h)