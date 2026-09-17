#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

SOURCES = {
    "fema_national": {
        "service": "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28",
        "source_role": "FEMA_NATIONAL_PROVENANCE_AND_EFFECTIVE_NFHL",
        "expected_layer_hint": "Flood Hazard Zones",
    },
    "guilford_effective_2026": {
        "service": "https://gcgis.guilfordcountync.gov/arcgis/rest/services/GISDV/Watershed_Management/MapServer/12",
        "source_role": "FEMA_PROVENANCE_GUILFORD_OPERATIONAL_IMPLEMENTATION",
        "expected_layer_hint": "Flood Zones Effective 06-10-2026",
    },
}

BOUNDS = {
    "south": 35.894145,
    "west": -80.198958,
    "north": 36.410277,
    "east": -79.157255,
}


def get_json(url: str, timeout: int = 60) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "MSE-thesis-H1-Level2/1.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def query_url(service: str, params: dict[str, object]) -> str:
    return service + "/query?" + urllib.parse.urlencode(params)


def classify_sfha_field(layer: dict) -> tuple[str, str]:
    fields = {f.get("name"): f for f in layer.get("fields", [])}
    if "SFHA_TF" not in fields:
        raise SystemExit("Flood-hazard layer lacks required SFHA_TF field")
    ftype = str(fields["SFHA_TF"].get("type", ""))
    if ftype == "esriFieldTypeString":
        return ftype, "SFHA_TF='T'"
    if ftype in {"esriFieldTypeSmallInteger", "esriFieldTypeInteger"}:
        return ftype, "SFHA_TF=1"
    raise SystemExit(f"Unsupported SFHA_TF field type: {ftype!r}")


def main() -> None:
    p = argparse.ArgumentParser(description="Freeze effective SFHA polygons for the GreenEVT Level-2 selection rectangle")
    p.add_argument("--source", choices=sorted(SOURCES), default="guilford_effective_2026")
    p.add_argument("--out", required=True, help="output GeoJSON FeatureCollection")
    p.add_argument("--metadata-out", required=True)
    p.add_argument("--page-size", type=int, default=1000)
    args = p.parse_args()

    source = SOURCES[args.source]
    service = source["service"]
    layer = get_json(service + "?f=pjson")
    if "error" in layer:
        raise SystemExit(f"flood-hazard layer metadata error: {layer['error']}")

    oid_field = layer.get("objectIdField") or layer.get("objectIdFieldName") or "OBJECTID"
    sfha_field_type, where_sfha = classify_sfha_field(layer)
    fields = {f.get("name") for f in layer.get("fields", [])}

    audit_fields = [oid_field, "SFHA_TF"]
    for name in ("FLD_ZONE", "ZONE_SUBTY", "ZONE_LID", "FLD_AR_ID", "DFIRM_ID", "VERSION_ID", "SOURCE_CIT"):
        if name in fields and name not in audit_fields:
            audit_fields.append(name)

    envelope = ",".join(str(x) for x in (BOUNDS["west"], BOUNDS["south"], BOUNDS["east"], BOUNDS["north"]))
    count_params = {
        "f": "json",
        "where": where_sfha,
        "geometry": envelope,
        "geometryType": "esriGeometryEnvelope",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "returnCountOnly": "true",
    }
    count_response = get_json(query_url(service, count_params))
    if "error" in count_response:
        raise SystemExit(f"SFHA count query error: {count_response['error']}")
    expected_count = int(count_response.get("count", -1))

    features: list[dict] = []
    offset = 0
    while True:
        params = {
            "f": "geojson",
            "where": where_sfha,
            "geometry": envelope,
            "geometryType": "esriGeometryEnvelope",
            "inSR": 4326,
            "outSR": 4326,
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": ",".join(audit_fields),
            "returnGeometry": "true",
            "resultOffset": offset,
            "resultRecordCount": args.page_size,
            "orderByFields": oid_field,
        }
        page = get_json(query_url(service, params))
        if "error" in page:
            raise SystemExit(f"SFHA feature query error at offset {offset}: {page['error']}")
        batch = page.get("features", [])
        if not batch:
            break
        features.extend(batch)
        offset += len(batch)
        if len(batch) < args.page_size:
            break
        time.sleep(0.1)

    if expected_count >= 0 and len(features) != expected_count:
        raise SystemExit(f"SFHA pagination mismatch: count query={expected_count}, downloaded={len(features)}")

    fc = {
        "type": "FeatureCollection",
        "name": f"SFHA_GreenEVT_selection_AOI_{args.source}",
        "crs": {"type": "name", "properties": {"name": "EPSG:4326"}},
        "features": features,
    }
    raw = (json.dumps(fc, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    Path(args.out).write_bytes(raw)

    metadata = {
        "protocol": "NFHL_SELECTION_EXPOSURE_V1_1.md",
        "source_key": args.source,
        "source_service": service,
        "source_role": source["source_role"],
        "expected_layer_hint": source["expected_layer_hint"],
        "retrieval_bounds_wgs84": BOUNDS,
        "query_filter": where_sfha,
        "sfha_field_type": sfha_field_type,
        "object_id_field": oid_field,
        "audit_fields": audit_fields,
        "feature_count": len(features),
        "geojson_sha256": sha256_bytes(raw),
        "layer_current_version": layer.get("currentVersion"),
        "layer_name": layer.get("name"),
        "layer_extent": layer.get("extent"),
        "selection_authorized": False,
        "coverage_rule": "Every feeder ROI requires explicit coverage determination; missing/noncoverage is never E_H=0.",
        "claim_boundary": "Snapshot supports only static outcome-blind feeder exposure E_H; it is not the dynamic HEC-RAS hazard eta(x,t).",
    }
    Path(args.metadata_out).write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
