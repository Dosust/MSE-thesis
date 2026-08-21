from __future__ import annotations
from typing import Dict, Iterable, List, Sequence

def evidence_weight(symbol: str) -> float:
    if symbol == "**":
        return 1.0
    if symbol == "*":
        return 0.5
    if symbol in ("", None):
        return 0.0
    raise ValueError(f"Unsupported evidence symbol {symbol!r}")

def category_coverage(symbols: Sequence[str]) -> float:
    if not symbols:
        return 0.0
    return sum(evidence_weight(x) for x in symbols) / len(symbols)

def group_coverage(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

def normalized_mapping_count(direct_flags: Sequence[bool], denominator: int) -> float:
    if denominator <= 0:
        raise ValueError("Denominator must be > 0.")
    value = sum(bool(x) for x in direct_flags) / denominator
    if not 0 <= value <= 1:
        raise ValueError("Normalized mapping must lie in [0,1].")
    return value
