"""Information-pathway operators for Phase-1 verification."""
from typing import List, Optional, Sequence


def delay_series(
    values: Sequence[float], delay_steps: int, fill: Optional[float] = None
) -> List[Optional[float]]:
    if delay_steps < 0:
        raise ValueError("delay_steps must be nonnegative")
    if delay_steps == 0:
        return list(values)
    return [fill] * delay_steps + list(
        values[:-delay_steps] if delay_steps < len(values) else []
    )


def controller_limit(
    p_margin: float,
    forecast: float,
    p_ref: float,
    site_cap: float,
    k_i: float = 1.0,
) -> float:
    if site_cap < 0.0:
        raise ValueError("site_cap must be nonnegative")
    penalty = k_i * max(forecast - p_ref, 0.0)
    raw = p_margin - penalty
    return min(max(raw, 0.0), site_cap)
