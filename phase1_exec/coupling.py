"""Explicit cross-domain maps frozen by the Phase-1 experiment specification."""
from typing import Dict, Mapping


def inject_charging_load(
    base_real_loads: Mapping[int, float],
    p_ch: float,
    bus: int = 24,
) -> Dict[int, float]:
    if p_ch < 0.0:
        raise ValueError("charging demand must be nonnegative in Phase-1 v1")
    result = dict(base_real_loads)
    result[bus] = result.get(bus, 0.0) + p_ch
    return result


def charging_availability(branch_energized: bool) -> int:
    return int(bool(branch_energized))
