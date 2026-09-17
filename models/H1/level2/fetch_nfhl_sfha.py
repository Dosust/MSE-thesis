#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

SERVICE = "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28"
BOUNDS = {
    "south": 35.894145,
    "west": -80.198958,
    "north": 36.410277,
    "east": -79.157255,
}


def get_json(url: str, timeout: int = 60) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "MSE-thesis-H1-Level2/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def query_url(params: dict[str, object]) -> str:
    return SERVICE + "/query?" + urllib.parse.urlencode(params)


def main() -> None:
    p = argparse.ArgumentParser(description="Freeze effective FEMA NFHL SFHA polygons for the GreenEVT Level-2 selection rectangle")
    p.add_argument("--out", required=True, help="output GeoJSON FeatureCollection")
    p.add_argument("--metadata-out", required=True)
    p.add_argument("--page-size", type=int, default=1000)
    args = p.parse_args()

    layer = get_json(SERVICE + "?f=pjson")
    if "error" in layer:
        raise SystemExit(f"FEMA layer metadata error: {layer['error']}")

    oid_field = layer.get("objectIdField") or layer.get("objectIdFieldName") or "OBJECTID"
    fields = {f.get("name") for f in layer.get("fields", [])}
    required = {"SFHA_TF", "FLD_ZONE", "ZONE_SUBTY"}
    missing = required - fields
    if missing:
        raise SystemExit(f"NFHL layer lacks required fields: {sorted(missing)}")

    envelope = ",".join(str(x) for x in (BOUNDS["west"], BOUNDS["south"], BOUNDS["east"], BOUNDS["north"]))

    count_params = {
        "f": "json",
        "where": "SFHA_TF='T'",
        "geometry": envelope,
        "geometryType": "esriGeometryEnvelope",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "returnCountOnly": "true",
    }
    count_response = get_json(query_url(count_params))
    if "error" in count_response:
        raise SystemExit(f"NFHL count query error: {count_response['error']}")
    expected_count = int(count_response.get("count", -1))

    features: list[dict] = []
    offset = 0
    while True:
        params = {
            "f": "geojson",
            "where": "SFHA_TF='T'",
            "geometry": envelope,
            "geometryType": "esriGeometryEnvelope",
            "inSR": 4326,
            "outSR": 4326,
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": f"{oid_field},SFHA_TF,FLD_ZONE,ZONE_SUBTY,FLD_AR_ID,DFIRM_ID,VERSION_ID,SOURCE_CIT",
            "returnGeometry": "true",
            "resultOffset": offset,
            "resultRecordCount": args.page_size,
            "orderByFields": oid_field,
        }
        page = get_json(query_url(params))
        if "error" in page:
            raise SystemExit(f"NFHL feature query error at offset {offset}: {page['error']}")
        batch = page.get("features", [])
        if not batch:
            break
        features.extend(batch)
        offset += len(batch)
        if len(batch) < args.page_size:
            break
        time.sleep(0.1)

    if expected_count >= 0 and len(features) != expected_count:
        raise SystemExit(f"NFHL pagination mismatch: count query={expected_count}, downloaded={len(features)}")

    fc = {
        "type": "FeatureCollection",
        "name": "FEMA_NFHL_SFHA_GreenEVT_selection_AOI",
        "crs": {"type": "name", "properties": {"name": "EPSG:4326"}},
        "features": features,
    }
    raw = (json.dumps(fc, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    Path(args.out).write_bytes(raw)

    metadata = {
        "source_service": SERVICE,
        "source_role": "effective FEMA NFHL; feeder-selection exposure only",
        "retrieval_bounds_wgs84": BOUNDS,
        "query_filter": "SFHA_TF='T'",
        "object_id_field": oid_field,
        "feature_count": len(features),
        "geojson_sha256": sha256_bytes(raw),
        "layer_current_version": layer.get("currentVersion"),
        "layer_name": layer.get("name"),
        "spatial_reference": 4326,
        "selection_authorized": False,
        "claim_boundary": "This snapshot supports only static outcome-blind feeder exposure E_H; it is not the dynamic HEC-RAS hazard eta(x,t).",
    }
    Path(args.metadata_out).write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
