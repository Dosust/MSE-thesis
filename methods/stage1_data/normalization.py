"""Case-independent Stage-1 normalization and QA primitives.

These helpers are deliberately small, deterministic, and auditable. They are
used by synthetic fixture tests to verify the generic Stage-1 data framework.
They do not contain Austin- or Greensboro-specific constants.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Optional, Tuple

import networkx as nx
from pyproj import Transformer
from shapely import make_valid
from shapely.geometry.base import BaseGeometry


MISSING_KINDS = {
    "unavailable",
    "not_applicable",
    "censored",
    "unknown",
    "parse_failure",
}


def stable_id(namespace: str, raw_id: str) -> str:
    """Return a deterministic canonical identifier."""
    payload = f"{namespace}::{raw_id}".encode("utf-8")
    return f"{namespace}:{hashlib.sha256(payload).hexdigest()[:20]}"


def sha256_bytes(data: bytes) -> str:
    """Return the SHA-256 digest of immutable RAW bytes."""
    return hashlib.sha256(data).hexdigest()


def normalize_missing(
    value: Any, *, missing_kind: Optional[str] = None
) -> Dict[str, Any]:
    """Preserve missingness semantics rather than silently imputing.

    Non-missing values are returned unchanged with missing_kind=None.
    Missing values require an explicit missing-kind classification.
    """
    if value is not None:
        return {"value": value, "missing_kind": None}
    if missing_kind not in MISSING_KINDS:
        raise ValueError(
            f"Missing value requires missing_kind in {sorted(MISSING_KINDS)}"
        )
    return {"value": None, "missing_kind": missing_kind}


_UNIT_FACTORS: Dict[Tuple[str, str], float] = {
    ("kV", "V"): 1000.0,
    ("MW", "W"): 1_000_000.0,
    ("kW", "W"): 1000.0,
    ("km", "m"): 1000.0,
    ("h", "s"): 3600.0,
    ("min", "s"): 60.0,
}


def convert_unit(value: float, raw_unit: str, canonical_unit: str) -> float:
    """Convert a limited fixture-level set of engineering units deterministically."""
    if raw_unit == canonical_unit:
        return float(value)
    key = (raw_unit, canonical_unit)
    if key not in _UNIT_FACTORS:
        raise ValueError(f"Unsupported deterministic conversion: {raw_unit}->{canonical_unit}")
    return float(value) * _UNIT_FACTORS[key]


def transform_xy(
    x: float, y: float, *, source_crs: str, target_crs: str
) -> Tuple[float, float]:
    """Transform a point while preserving explicit CRS provenance."""
    transformer = Transformer.from_crs(source_crs, target_crs, always_xy=True)
    return transformer.transform(x, y)


@dataclass(frozen=True)
class GeometryQA:
    original_valid: bool
    released_valid: bool
    repaired: bool
    repair_operation: Optional[str]


def validate_or_repair_geometry(
    geometry: BaseGeometry, *, allow_repair: bool = False
) -> Tuple[BaseGeometry, GeometryQA]:
    """Detect invalid geometry and repair only when explicitly configured."""
    original_valid = bool(geometry.is_valid)
    if original_valid:
        return geometry, GeometryQA(True, True, False, None)
    if not allow_repair:
        return geometry, GeometryQA(False, False, False, None)

    repaired_geometry = make_valid(geometry)
    return repaired_geometry, GeometryQA(
        original_valid=False,
        released_valid=bool(repaired_geometry.is_valid),
        repaired=True,
        repair_operation="shapely.make_valid",
    )


def directed_topology(
    edges: Iterable[Tuple[str, str]]
) -> nx.DiGraph:
    """Construct a directed reference topology without changing edge direction."""
    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    return graph


def resolve_authority_applicability(
    *,
    case_jurisdiction: str,
    authority_jurisdiction: str,
    technical_scope_match: bool,
    status: str,
) -> str:
    """Return a conservative applicability state for fixture verification.

    This is not a legal-reasoning engine. It enforces the Stage-1 rule that a
    requirement outside the declared jurisdiction or technical scope cannot
    silently become a model constraint.
    """
    if status not in {"current", "superseded", "draft", "historical", "unknown"}:
        raise ValueError(f"Unknown authority status: {status}")

    if case_jurisdiction != authority_jurisdiction:
        return "NOT_APPLICABLE"
    if not technical_scope_match:
        return "NOT_APPLICABLE"
    if status == "current":
        return "APPLICABLE"
    if status in {"superseded", "historical"}:
        return "CONDITIONAL"
    return "UNRESOLVED"


def authority_becomes_model_constraint(applicability: str) -> bool:
    """Only currently applicable/explicitly conditional authorities may constrain a case."""
    return applicability in {"APPLICABLE", "CONDITIONAL"}


def preserve_temporal_role(manifest: Mapping[str, Any]) -> str:
    """Return source temporal semantics unchanged."""
    role = manifest.get("temporal_semantics")
    allowed = {
        "contemporaneous",
        "retrospective",
        "persistent_static",
        "proxy",
        "synthetic",
        "mixed",
    }
    if role not in allowed:
        raise ValueError(f"Unknown temporal semantics: {role}")
    return str(role)
