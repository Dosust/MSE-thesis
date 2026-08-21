from __future__ import annotations
from typing import Dict, List, Tuple

PERFORMANCE_CLASSES = [
    "Structural/seismic",
    "Mechanical/material",
    "Durability/service life",
    "Thermal/energy",
    "Acoustic/fire",
    "Geotechnical",
    "Pavement",
    "Optimization/surrogate",
]

INTEGRATION_MECHANISMS = [
    "Causal loss chain",
    "Weighted formula",
    "MIVES/value-function",
    "LCSA + outranking",
    "Hybrid MCDM",
    "Consolidated index",
    "Hierarchical index",
    "Simulation + regression",
    "Robust optimization",
]

SUSTAINABILITY_OUTCOMES = [
    "Economic cost / lifecycle cost",
    "Environmental impact / GWP",
    "Energy / emergy / resource demand",
    "Social / downtime / safety",
    "Integrated sustainability score",
    "Trade-off ranking",
    "Service-life / resilience consequence",
    "Optimized design decision",
]

def empty_matrix(rows: List[str], cols: List[str]) -> Dict[str, Dict[str, int]]:
    return {r: {c: 0 for c in cols} for r in rows}
