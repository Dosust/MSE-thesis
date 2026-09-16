#!/usr/bin/env python3
"""Materialize City of Houston traffic-signal GIS data for H3.

Scientific authority:
  project/H3_HOUSTON_TRAFFIC_SIGNAL_SOURCE_AND_MATERIALIZATION_V1.md

The script preserves raw ArcGIS response pages, freezes hashes/provenance,
combines them only as a processed derivative, and does not perform Houston-core
clipping unless a separately validated boundary is supplied downstream.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

CASE_ID = "H3-HOU-FLOOD-V1"
LAYER_URL = (
    "https://geogimsms.houstontx.gov/arcgis/rest/services/"
    "TDO/Traffic_Management_gx/MapServer/26"
)


def fetch(url: str, params: dict[str, str] | None = None, timeout: int = 180) -> tuple[str, bytes]:
    full = url
    if params:
        full = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(full, headers={"User-Agent": "MSE-thesis-H3-signal-fetch/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", 200)
        if status != 200:
            raise RuntimeError(f"HTTP {status}: {full}")
        data = resp.read()
    if not data:
        raise RuntimeError(f"Empty response: {full}")
    return full, data


def parse_json(data: bytes, label: str):
    try:
        doc = json.loads(data.decode("utf-8"))
    except Exception as exc:
        raise RuntimeError(f"{label} is not valid UTF-8 JSON") from exc
    if isinstance(doc, dict) and "error" in doc:
        raise RuntimeError(f"ArcGIS error in {label}: {doc['error']}")
    return doc


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default="data/H3-HOU-FLOOD-V1")
    p.add_argument("--page-size", type=int, default=1000)
    args = p.parse_args()

    root = pathlib.Path(args.root)
    raw_dir = root / "raw" / "signals"
    proc_dir = root / "processed" / "signals"
    qa_dir = root / "qa" / "signals"
    manifest_dir = root / "qa" / "manifests"
    for d in (raw_dir, proc_dir, qa_dir, manifest_dir):
        d.mkdir(parents=True, exist_ok=True)

    accessed = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    meta_url, meta_bytes = fetch(LAYER_URL, {"f": "pjson"})
    meta = parse_json(meta_bytes, "signal layer metadata")
    if meta.get("geometryType") != "esriGeometryPoint":
        raise RuntimeError(f"Expected point layer, got {meta.get('geometryType')!r}")

    oid_field = meta.get("objectIdField") or meta.get("objectIdFieldName")
    if not oid_field:
        for fld in meta.get("fields") or []:
            if fld.get("type") == "esriFieldTypeOID":
                oid_field = fld.get("name")
                break
    if not oid_field:
        raise RuntimeError("No object ID field declared by signal layer")

    max_record_count = int(meta.get("maxRecordCount") or 2000)
    page_size = min(max(1, args.page_size), max_record_count)

    count_url, count_bytes = fetch(
        f"{LAYER_URL}/query",
        {"where": "1=1", "returnCountOnly": "true", "f": "json"},
    )
    count_doc = parse_json(count_bytes, "signal count query")
    expected_count = int(count_doc.get("count", -1))
    if expected_count < 0:
        raise RuntimeError("Signal count query did not return a nonnegative count")

    (raw_dir / "traffic_signal_layer_metadata.json").write_bytes(meta_bytes)
    (raw_dir / "traffic_signal_count.json").write_bytes(count_bytes)

    pages = []
    all_features = []
    seen_ids = set()
    duplicate_ids = []
    null_geometry = 0
    invalid_coordinate = 0
    offset = 0
    page_index = 0

    while offset < expected_count:
        query_params = {
            "where": "1=1",
            "outFields": "*",
            "returnGeometry": "true",
            "outSR": "4326",
            "orderByFields": f"{oid_field} ASC",
            "resultOffset": str(offset),
            "resultRecordCount": str(page_size),
            "f": "geojson",
        }
        page_url, page_bytes = fetch(f"{LAYER_URL}/query", query_params)
        page = parse_json(page_bytes, f"signal page {page_index}")
        features = page.get("features") or []
        if not features:
            raise RuntimeError(
                f"Empty page at offset {offset} before expected count {expected_count}"
            )

        page_path = raw_dir / f"traffic_signals_page_{page_index:04d}.geojson"
        page_path.write_bytes(page_bytes)
        pages.append({
            "page": page_index,
            "offset": offset,
            "records": len(features),
            "url": page_url,
            "bytes": len(page_bytes),
            "sha256": sha256(page_bytes),
            "file": str(page_path),
        })

        for feat in features:
            props = feat.get("properties") or {}
            oid = props.get(oid_field)
            if oid in seen_ids:
                duplicate_ids.append(oid)
            seen_ids.add(oid)
            geom = feat.get("geometry")
            if geom is None:
                null_geometry += 1
            else:
                coords = geom.get("coordinates") if isinstance(geom, dict) else None
                if not isinstance(coords, list) or len(coords) < 2:
                    invalid_coordinate += 1
                else:
                    try:
                        x, y = float(coords[0]), float(coords[1])
                        if not (math.isfinite(x) and math.isfinite(y) and -180 <= x <= 180 and -90 <= y <= 90):
                            invalid_coordinate += 1
                    except Exception:
                        invalid_coordinate += 1
            all_features.append(feat)

        offset += len(features)
        page_index += 1

    observed_count = len(all_features)
    complete = observed_count == expected_count
    if not complete:
        raise RuntimeError(f"Count mismatch: expected {expected_count}, observed {observed_count}")

    processed = {
        "type": "FeatureCollection",
        "name": "Houston Traffic Signal source-layer derivative",
        "features": all_features,
    }
    processed_path = proc_dir / "traffic_signals_wgs84.geojson"
    processed_bytes = (json.dumps(processed, separators=(",", ":")) + "\n").encode()
    processed_path.write_bytes(processed_bytes)

    qa_status = "PASS"
    if duplicate_ids or null_geometry or invalid_coordinate:
        qa_status = "REVIEW_REQUIRED"

    qa = {
        "case_id": CASE_ID,
        "access_utc": accessed,
        "source_layer": LAYER_URL,
        "source_metadata_url": meta_url,
        "count_query_url": count_url,
        "geometry_type": meta.get("geometryType"),
        "native_spatial_reference": meta.get("extent", {}).get("spatialReference"),
        "object_id_field": oid_field,
        "max_record_count": max_record_count,
        "page_size": page_size,
        "expected_feature_count": expected_count,
        "observed_feature_count": observed_count,
        "unique_object_ids": len(seen_ids),
        "duplicate_id_count": len(duplicate_ids),
        "null_geometry_count": null_geometry,
        "invalid_coordinate_count": invalid_coordinate,
        "page_count": len(pages),
        "status": qa_status,
        "limitations": [
            "No Houston-core clipping is performed in this materialization step.",
            "No signal-to-road or signal-to-power mapping is performed here.",
            "Signal locations do not reveal actual electric utility feeder assignments.",
            "Feature-level backup-power state is not inferred from this GIS layer.",
        ],
    }
    qa_path = qa_dir / "houston_traffic_signal_qa.json"
    qa_path.write_text(json.dumps(qa, indent=2, sort_keys=True) + "\n")

    manifest = {
        "dataset_id": "H3-HOU-SIGNALS-COH-V1",
        "case_id": CASE_ID,
        "authority": "City of Houston Public Works",
        "service": "TDO/Traffic_Management_gx",
        "layer": "Traffic Signal (26)",
        "layer_url": LAYER_URL,
        "access_utc": accessed,
        "metadata_sha256": sha256(meta_bytes),
        "count_sha256": sha256(count_bytes),
        "processed_file": str(processed_path),
        "processed_sha256": sha256(processed_bytes),
        "raw_pages": pages,
        "qa_file": str(qa_path),
        "status": "RAW_SIGNAL_BYTES_FROZEN" if complete else "INCOMPLETE",
    }
    manifest_path = manifest_dir / "houston_traffic_signal_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    print(json.dumps({"manifest": manifest, "qa": qa}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
