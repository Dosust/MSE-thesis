#!/usr/bin/env python3
"""Materialize and QA the authoritative Houston H3 boundary.

Scientific authority:
  project/H3_HOUSTON_BOUNDARY_FREEZE_V1.md

Outputs are written under a case-data root and are intended to be uploaded as
GitHub Actions evidence artifacts. Raw bytes are preserved exactly as returned.
No geometry repair is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone

from pyproj import Transformer
from shapely.geometry import mapping, shape
from shapely.ops import transform, unary_union

CASE_ID = "H3-HOU-FLOOD-V1"
PRIMARY_LAYER = (
    "https://mycity2.houstontx.gov/pubgis02/rest/services/"
    "HoustonMap/Administrative_Boundary/MapServer/0"
)
SECONDARY_LAYER = (
    "https://geohwp.houstontx.gov/arcgis/rest/services/"
    "02_BaseData_Boundaries/COH/FeatureServer/7"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, params: dict[str, str] | None = None, timeout: int = 180) -> tuple[str, bytes]:
    full_url = url
    if params:
        full_url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        full_url,
        headers={"User-Agent": "MSE-thesis-H3-Houston-boundary/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", 200)
        if status != 200:
            raise RuntimeError(f"HTTP {status}: {full_url}")
        payload = resp.read()
    if not payload:
        raise RuntimeError(f"Empty response: {full_url}")
    return full_url, payload


def parse_json(payload: bytes, label: str) -> dict:
    try:
        doc = json.loads(payload.decode("utf-8"))
    except Exception as exc:
        raise RuntimeError(f"{label} is not valid UTF-8 JSON") from exc
    if isinstance(doc, dict) and "error" in doc:
        raise RuntimeError(f"ArcGIS error for {label}: {doc['error']}")
    return doc


def service_counts_geojson(doc: dict) -> Counter:
    c: Counter = Counter()
    for feat in doc.get("features", []):
        props = feat.get("properties") or {}
        val = props.get("SERVICE_TY")
        key = "<NULL>" if val is None else str(val).strip().upper()
        c[key] += 1
    return c


def geojson_geometries(doc: dict, service_type: str | None = None):
    out = []
    for feat in doc.get("features", []):
        props = feat.get("properties") or {}
        val = props.get("SERVICE_TY")
        key = "<NULL>" if val is None else str(val).strip().upper()
        if service_type is not None and key != service_type:
            continue
        geom = feat.get("geometry")
        if geom is None:
            out.append(None)
        else:
            out.append(shape(geom))
    return out


def write_feature(path: pathlib.Path, geom, properties: dict) -> None:
    fc = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": properties,
                "geometry": mapping(geom),
            }
        ],
    }
    path.write_text(json.dumps(fc, separators=(",", ":")) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/H3-HOU-FLOOD-V1")
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    raw_dir = root / "raw" / "boundary"
    processed_dir = root / "processed" / "boundary"
    qa_dir = root / "qa" / "boundary"
    manifest_dir = root / "qa" / "manifests"
    for d in (raw_dir, processed_dir, qa_dir, manifest_dir):
        d.mkdir(parents=True, exist_ok=True)

    access_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    # 1. Layer metadata from two independent City-hosted services.
    p_meta_url, p_meta_bytes = fetch(PRIMARY_LAYER, {"f": "pjson"})
    s_meta_url, s_meta_bytes = fetch(SECONDARY_LAYER, {"f": "pjson"})
    p_meta = parse_json(p_meta_bytes, "primary layer metadata")
    s_meta = parse_json(s_meta_bytes, "secondary layer metadata")

    # 2. Immutable primary raw FeatureSet JSON in native service CRS.
    raw_params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "returnTrueCurves": "false",
        "f": "json",
    }
    raw_url, raw_bytes = fetch(f"{PRIMARY_LAYER}/query", raw_params)
    raw_doc = parse_json(raw_bytes, "primary raw boundary")
    if raw_doc.get("geometryType") != "esriGeometryPolygon":
        raise RuntimeError(f"Unexpected primary geometry type: {raw_doc.get('geometryType')!r}")
    if raw_doc.get("exceededTransferLimit") is True:
        raise RuntimeError("Primary raw query exceeded transfer limit; pagination is required")
    raw_features = raw_doc.get("features") or []
    if not raw_features:
        raise RuntimeError("Primary raw query returned no features")

    field_names = {f.get("name") for f in (raw_doc.get("fields") or [])}
    if "SERVICE_TY" not in field_names:
        raise RuntimeError("SERVICE_TY missing from primary raw FeatureSet")

    raw_path = raw_dir / "coh_city_limits_primary_raw.json"
    raw_path.write_bytes(raw_bytes)
    (raw_dir / "coh_city_limits_primary_layer_metadata.json").write_bytes(p_meta_bytes)
    (raw_dir / "coh_city_limits_secondary_layer_metadata.json").write_bytes(s_meta_bytes)

    # 3. Derived WGS84 GeoJSON solely for geometry QA and reproducible processed domains.
    geo_params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "outSR": "4326",
        "f": "geojson",
    }
    p_geo_url, p_geo_bytes = fetch(f"{PRIMARY_LAYER}/query", geo_params)
    s_geo_url, s_geo_bytes = fetch(f"{SECONDARY_LAYER}/query", geo_params)
    p_geo = parse_json(p_geo_bytes, "primary WGS84 GeoJSON")
    s_geo = parse_json(s_geo_bytes, "secondary WGS84 GeoJSON")
    (raw_dir / "coh_city_limits_primary_wgs84.geojson").write_bytes(p_geo_bytes)
    (raw_dir / "coh_city_limits_secondary_wgs84.geojson").write_bytes(s_geo_bytes)

    p_counts = service_counts_geojson(p_geo)
    s_counts = service_counts_geojson(s_geo)
    if p_counts.get("FULL", 0) == 0:
        raise RuntimeError("Primary dataset has no SERVICE_TY=FULL features")

    p_geoms = geojson_geometries(p_geo)
    null_geom_count = sum(g is None for g in p_geoms)
    valid_geoms = [g for g in p_geoms if g is not None]
    invalid_indices = [i for i, g in enumerate(valid_geoms) if not g.is_valid]
    empty_indices = [i for i, g in enumerate(valid_geoms) if g.is_empty]

    # Hard gate: do not silently repair invalid or empty geometries.
    if null_geom_count or invalid_indices or empty_indices:
        status = "FAIL_GEOMETRY_VALIDITY"
    else:
        status = "PASS"

    full_geoms = [g for g in geojson_geometries(p_geo, "FULL") if g is not None]
    limited_geoms = [g for g in geojson_geometries(p_geo, "LIMITED") if g is not None]
    legal_geoms = full_geoms + limited_geoms
    if not full_geoms:
        raise RuntimeError("No valid FULL geometries available for core domain")

    core = unary_union(full_geoms)
    limited = unary_union(limited_geoms) if limited_geoms else None
    legal = unary_union(legal_geoms)

    to_2278 = Transformer.from_crs("EPSG:4326", "EPSG:2278", always_xy=True).transform
    core_2278 = transform(to_2278, core)
    legal_2278 = transform(to_2278, legal)
    limited_2278 = transform(to_2278, limited) if limited is not None else None
    sqft_to_km2 = 0.09290304 / 1_000_000.0

    core_area_km2 = core_2278.area * sqft_to_km2
    legal_area_km2 = legal_2278.area * sqft_to_km2
    limited_area_km2 = limited_2278.area * sqft_to_km2 if limited_2278 is not None else 0.0

    # Secondary-source cross-check: compare dissolved legal-envelope areas in one CRS.
    secondary_geoms = [g for g in geojson_geometries(s_geo) if g is not None]
    secondary_valid = [g for g in secondary_geoms if g.is_valid and not g.is_empty]
    secondary_legal = unary_union(secondary_valid) if secondary_valid else None
    secondary_area_km2 = None
    area_difference_fraction = None
    if secondary_legal is not None:
        secondary_2278 = transform(to_2278, secondary_legal)
        secondary_area_km2 = secondary_2278.area * sqft_to_km2
        if legal_area_km2 > 0:
            area_difference_fraction = abs(secondary_area_km2 - legal_area_km2) / legal_area_km2

    raw_sha = sha256_bytes(raw_bytes)
    p_geo_sha = sha256_bytes(p_geo_bytes)
    s_geo_sha = sha256_bytes(s_geo_bytes)

    common_props = {
        "case_id": CASE_ID,
        "primary_source_sha256": raw_sha,
        "derived_from": p_geo_url,
        "analysis_crs_for_area": "EPSG:2278",
        "geometry_storage_crs": "EPSG:4326",
    }
    write_feature(
        processed_dir / "houston_core_full_service.geojson",
        core,
        {**common_props, "domain": "Omega_core", "SERVICE_TY": "FULL"},
    )
    write_feature(
        processed_dir / "houston_legal_full_plus_limited.geojson",
        legal,
        {**common_props, "domain": "Omega_legal", "SERVICE_TY": "FULL+LIMITED"},
    )
    if limited is not None:
        write_feature(
            processed_dir / "houston_limited_service.geojson",
            limited,
            {**common_props, "domain": "Omega_limited", "SERVICE_TY": "LIMITED"},
        )

    qa = {
        "case_id": CASE_ID,
        "access_utc": access_utc,
        "status": status,
        "primary": {
            "layer_url": PRIMARY_LAYER,
            "metadata_url": p_meta_url,
            "raw_query_url": raw_url,
            "wgs84_geojson_query_url": p_geo_url,
            "raw_bytes": len(raw_bytes),
            "raw_sha256": raw_sha,
            "wgs84_geojson_bytes": len(p_geo_bytes),
            "wgs84_geojson_sha256": p_geo_sha,
            "layer_name": p_meta.get("name"),
            "layer_geometry_type": p_meta.get("geometryType"),
            "layer_extent": p_meta.get("extent"),
            "raw_feature_count": len(raw_features),
            "geojson_feature_count": len(p_geo.get("features") or []),
            "service_type_counts": dict(p_counts),
            "null_geometry_count": null_geom_count,
            "invalid_geometry_count": len(invalid_indices),
            "empty_geometry_count": len(empty_indices),
            "raw_spatial_reference": raw_doc.get("spatialReference"),
        },
        "secondary_crosscheck": {
            "layer_url": SECONDARY_LAYER,
            "metadata_url": s_meta_url,
            "wgs84_geojson_query_url": s_geo_url,
            "wgs84_geojson_bytes": len(s_geo_bytes),
            "wgs84_geojson_sha256": s_geo_sha,
            "layer_name": s_meta.get("name"),
            "layer_extent": s_meta.get("extent"),
            "service_type_counts": dict(s_counts),
            "feature_count": len(s_geo.get("features") or []),
            "legal_area_km2": secondary_area_km2,
            "primary_vs_secondary_legal_area_difference_fraction": area_difference_fraction,
            "note": "Difference is reported, not thresholded; sources represent different publication snapshots.",
        },
        "domains": {
            "Omega_core_area_km2": core_area_km2,
            "Omega_limited_area_km2": limited_area_km2,
            "Omega_legal_area_km2": legal_area_km2,
            "primary_domain": "Omega_core = dissolve(SERVICE_TY=FULL)",
        },
        "gates": {
            "G_Omega_source": 1,
            "G_Omega_bytes": 1,
            "G_Omega_parse": 1,
            "G_Omega_geom": int(raw_doc.get("geometryType") == "esriGeometryPolygon"),
            "G_Omega_class": int(p_counts.get("FULL", 0) > 0),
            "G_Omega_valid": int(status == "PASS"),
            "G_Omega_crosscheck": int(secondary_legal is not None),
            "G_Omega_QA": int(status == "PASS" and secondary_legal is not None),
        },
        "prohibitions": [
            "No geometry repair was performed.",
            "No limited-purpose polygon was merged into Omega_core.",
            "No exterior network connector is included in service denominators by this step.",
        ],
    }

    qa_path = qa_dir / "houston_boundary_qa.json"
    qa_path.write_text(json.dumps(qa, indent=2, sort_keys=True) + "\n")

    manifest = {
        "dataset_id": "H3-HOU-BOUNDARY-COH-V1",
        "case_id": CASE_ID,
        "source_authority": "City of Houston / COHGIS",
        "source_title": "Houston City Limit — Administrative Boundary",
        "source_layer_url": PRIMARY_LAYER,
        "source_query_url": raw_url,
        "secondary_verification_layer_url": SECONDARY_LAYER,
        "access_date_utc": access_utc,
        "raw_filename": str(raw_path),
        "bytes": len(raw_bytes),
        "sha256": raw_sha,
        "format": "ArcGIS FeatureSet JSON",
        "native_crs": raw_doc.get("spatialReference"),
        "transformations": "NONE",
        "status": "RAW_BYTES_FROZEN" if status == "PASS" else "RAW_BYTES_FROZEN_QA_FAIL",
    }
    (manifest_dir / "coh_city_limits_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )

    summary = qa_dir / "houston_boundary_summary.txt"
    summary.write_text(
        "\n".join(
            [
                f"CASE_ID={CASE_ID}",
                f"STATUS={status}",
                f"RAW_SHA256={raw_sha}",
                f"RAW_BYTES={len(raw_bytes)}",
                f"FEATURES={len(raw_features)}",
                f"FULL_FEATURES={p_counts.get('FULL', 0)}",
                f"LIMITED_FEATURES={p_counts.get('LIMITED', 0)}",
                f"INVALID_GEOMETRIES={len(invalid_indices)}",
                f"NULL_GEOMETRIES={null_geom_count}",
                f"OMEGA_CORE_AREA_KM2={core_area_km2:.6f}",
                f"OMEGA_LIMITED_AREA_KM2={limited_area_km2:.6f}",
                f"OMEGA_LEGAL_AREA_KM2={legal_area_km2:.6f}",
                f"SECONDARY_AREA_DIFF_FRACTION={area_difference_fraction}",
                f"G_OMEGA_QA={qa['gates']['G_Omega_QA']}",
                "",
            ]
        )
    )
    print(summary.read_text())

    if qa["gates"]["G_Omega_QA"] != 1:
        return 88
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)
