"""Structural/provenance QC for Austin raw-data manifests.

This module performs deterministic QA that is possible without interpreting
scientific outcomes. Spatial intersections and model physics are separate gates.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping


class AustinDataQCError(ValueError):
    """Raised when raw/provenance evidence violates the Austin QC contract."""


REQUIRED_OBJECTS = {
    "smartds_listing",
    "smartds_buscoords",
    "austin_full_purpose",
    "street_centerline",
    "traffic_signals",
    "fema_floodplain",
    "camera_detector_locations",
    "radar_sensor_locations",
}


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AustinDataQCError(message)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def _validate_record(name: str, record: Mapping[str, Any], root: Path | None) -> None:
    _require(isinstance(record.get("bytes"), int) and record["bytes"] > 0, f"{name}: positive byte count required")
    digest = record.get("sha256")
    _require(isinstance(digest, str) and len(digest) == 64, f"{name}: SHA-256 required")
    # Direct-download records use `source_url`; ArcGIS merged records preserve
    # the authoritative service endpoint under `layer`. Both are explicit
    # provenance URLs and neither may be absent.
    source = record.get("source_url") or record.get("layer")
    _require(isinstance(source, str) and source, f"{name}: source URL/layer endpoint required")

    if root is not None:
        path = Path(str(record.get("path", "")))
        candidate = path if path.is_absolute() else root / path
        _require(candidate.exists(), f"{name}: raw file missing: {candidate}")
        _require(candidate.stat().st_size == record["bytes"], f"{name}: byte-count mismatch")
        _require(sha256_file(candidate) == digest, f"{name}: SHA-256 mismatch")

    if "object_id_count" in record:
        count = record.get("object_id_count")
        features = record.get("feature_count")
        pages = record.get("pages")
        _require(isinstance(count, int) and count >= 0, f"{name}: invalid object-ID count")
        _require(features == count, f"{name}: merged feature count must equal object-ID count")
        _require(isinstance(pages, list), f"{name}: page manifest required")
        _require(record.get("page_count") == len(pages), f"{name}: page-count mismatch")
        page_features = 0
        requested_ids: list[int] = []
        for index, page in enumerate(pages):
            _require(isinstance(page, Mapping), f"{name}: page {index} must be object")
            ids = page.get("requested_ids")
            _require(isinstance(ids, list), f"{name}: page {index} requested IDs missing")
            _require(page.get("feature_count") == len(ids), f"{name}: page {index} count mismatch")
            _require(isinstance(page.get("sha256"), str) and len(page["sha256"]) == 64, f"{name}: page {index} hash missing")
            requested_ids.extend(ids)
            page_features += int(page.get("feature_count", 0))
        _require(page_features == count, f"{name}: sum of page features != object-ID count")
        _require(len(requested_ids) == len(set(requested_ids)), f"{name}: duplicate paginated object IDs")


def validate_raw_manifest(manifest: Mapping[str, Any], root: Path | None = None) -> dict[str, Any]:
    """Validate immutable acquisition/provenance structure and return QC summary."""
    _require(manifest.get("case_id") == "AUS-P5U-2018-V1", "unexpected Austin case ID")
    _require(manifest.get("status") == "RAW_MATERIALIZATION_ONLY", "raw manifest cannot claim downstream PASS")
    objects = manifest.get("objects")
    _require(isinstance(objects, Mapping), "manifest objects required")
    missing = REQUIRED_OBJECTS - set(objects)
    _require(not missing, f"missing required raw objects: {sorted(missing)}")

    for name in REQUIRED_OBJECTS:
        record = objects[name]
        _require(isinstance(record, Mapping), f"{name}: record must be object")
        _validate_record(name, record, root)

    bus = objects["smartds_buscoords"]
    rows = bus.get("plausible_lonlat_rows")
    bbox = bus.get("bbox_wgs84")
    _require(isinstance(rows, int) and rows > 0, "SMART-DS Buscoords must contain plausible rows")
    _require(isinstance(bbox, list) or isinstance(bbox, tuple), "SMART-DS bbox required")
    _require(len(bbox) == 4, "SMART-DS bbox must have four values")
    xmin, ymin, xmax, ymax = map(float, bbox)
    _require(-180 <= xmin < xmax <= 180 and -90 <= ymin < ymax <= 90, "SMART-DS bbox invalid")

    for name in ("austin_full_purpose", "street_centerline", "traffic_signals", "fema_floodplain"):
        _require(int(objects[name].get("feature_count", -1)) >= 0, f"{name}: feature count required")

    traffic_nonempty = any(int(objects[name].get("row_count", 0)) > 0 for name in ("camera_detector_locations", "radar_sensor_locations"))
    _require(traffic_nonempty, "at least one traffic-location table must be nonempty")

    return {
        "case_id": manifest["case_id"],
        "raw_integrity": "PASS",
        "provenance_structure": "PASS",
        "arcgis_pagination": "PASS",
        "bus_coordinate_structure": "PASS",
        "traffic_location_presence": "PASS",
        "scientific_scope": "RAW_QC_ONLY_NOT_CASE_ADMISSIBILITY",
    }


def load_and_validate(path: str | Path, root: str | Path | None = None) -> dict[str, Any]:
    p = Path(path)
    manifest = json.loads(p.read_text(encoding="utf-8"))
    return validate_raw_manifest(manifest, Path(root) if root is not None else None)
