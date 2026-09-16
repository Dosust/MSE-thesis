#!/usr/bin/env python3
"""Fetch and freeze the authoritative City of Houston city-limit layer.

H3-HOU-FLOOD-V1 acquisition utility.

This script downloads the raw ArcGIS JSON feature set without reprojection,
computes SHA-256, performs minimal schema checks, and writes a manifest.
It does not dissolve, reproject, repair, or otherwise mutate the raw geometry.

Scientific authority:
  project/H3_HOUSTON_BOUNDARY_FREEZE_V1.md

Usage:
  python methods/h3/fetch_houston_boundary.py \
      --root data/H3-HOU-FLOOD-V1
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE_URL = (
    "https://mycity2.houstontx.gov/gisweb01/rest/services/"
    "HoustonMap/Administrative_Boundary/MapServer/0/query"
)
LAYER_URL = (
    "https://mycity2.houstontx.gov/gisweb01/rest/services/"
    "HoustonMap/Administrative_Boundary/MapServer/0"
)
SECONDARY_LAYER_URL = (
    "https://geohwp.houstontx.gov/arcgis/rest/services/"
    "02_BaseData_Boundaries/COH/FeatureServer/7"
)

QUERY = {
    "where": "1=1",
    "outFields": "*",
    "returnGeometry": "true",
    "f": "json",
}


def sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def fetch(url: str, params: dict[str, str], timeout: int = 120) -> tuple[str, bytes]:
    query = urllib.parse.urlencode(params)
    full_url = f"{url}?{query}"
    request = urllib.request.Request(
        full_url,
        headers={"User-Agent": "MSE-thesis-H3-boundary-fetch/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        status = getattr(response, "status", 200)
        if status != 200:
            raise RuntimeError(f"HTTP status {status} for {full_url}")
        payload = response.read()
    if not payload:
        raise RuntimeError("Downloaded boundary payload is empty")
    return full_url, payload


def validate_arcgis_json(doc: dict) -> dict:
    if "error" in doc:
        raise RuntimeError(f"ArcGIS service error: {doc['error']}")

    geometry_type = doc.get("geometryType")
    if geometry_type != "esriGeometryPolygon":
        raise RuntimeError(
            f"Expected esriGeometryPolygon, received {geometry_type!r}"
        )

    fields = doc.get("fields") or []
    field_names = {f.get("name") for f in fields}
    if "SERVICE_TY" not in field_names:
        raise RuntimeError("Required SERVICE_TY field not found")

    features = doc.get("features")
    if not isinstance(features, list) or not features:
        raise RuntimeError("No boundary features returned")

    service_types: dict[str, int] = {}
    null_geometry_count = 0
    for feature in features:
        attrs = feature.get("attributes") or {}
        value = attrs.get("SERVICE_TY")
        key = "<NULL>" if value is None else str(value).strip().upper()
        service_types[key] = service_types.get(key, 0) + 1
        if feature.get("geometry") is None:
            null_geometry_count += 1

    if service_types.get("FULL", 0) == 0:
        raise RuntimeError("No SERVICE_TY=FULL features found")

    spatial_reference = doc.get("spatialReference") or {}

    return {
        "geometry_type": geometry_type,
        "feature_count": len(features),
        "service_type_counts": service_types,
        "null_geometry_count": null_geometry_count,
        "spatial_reference": spatial_reference,
        "field_names": sorted(x for x in field_names if x),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="data/H3-HOU-FLOOD-V1",
        help="Case data root",
    )
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    raw_dir = root / "raw" / "boundary"
    manifest_dir = root / "qa" / "manifests"
    raw_dir.mkdir(parents=True, exist_ok=True)
    manifest_dir.mkdir(parents=True, exist_ok=True)

    raw_path = raw_dir / "coh_city_limits_raw.json"
    manifest_path = manifest_dir / "coh_city_limits_manifest.json"

    access_time = datetime.now(timezone.utc).isoformat()
    full_url, payload = fetch(BASE_URL, QUERY)

    try:
        doc = json.loads(payload.decode("utf-8"))
    except Exception as exc:
        raise RuntimeError("Downloaded payload is not valid UTF-8 JSON") from exc

    qa = validate_arcgis_json(doc)
    digest = sha256_bytes(payload)

    # Raw bytes are written exactly as returned by the City-hosted service.
    raw_path.write_bytes(payload)

    manifest = {
        "dataset_id": "H3-HOU-BOUNDARY-COH-V1",
        "case_id": "H3-HOU-FLOOD-V1",
        "source_authority": "City of Houston / COHGIS / MyCity Houston",
        "source_title": "Houston City Limit — Administrative Boundary, Layer 0",
        "source_layer_url": LAYER_URL,
        "source_query_url": full_url,
        "secondary_verification_layer_url": SECONDARY_LAYER_URL,
        "access_date_utc": access_time,
        "raw_filename": str(raw_path),
        "bytes": len(payload),
        "sha256": digest,
        "format": "ArcGIS FeatureSet JSON",
        "transformations": "NONE",
        "qa": qa,
        "status": "RAW_BYTES_FROZEN_SCHEMA_PASS",
        "notes": [
            "No reprojection/dissolve/geometry repair performed by this script.",
            "SERVICE_TY=FULL is the primary H3 service domain after downstream QA.",
            "SERVICE_TY=LIMITED is retained as a separate contextual/sensitivity domain.",
            "Geometry validity, dissolve, area, and secondary-endpoint cross-check are downstream QA tasks.",
        ],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
