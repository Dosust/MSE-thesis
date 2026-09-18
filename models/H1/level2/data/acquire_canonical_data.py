#!/usr/bin/env python3
"""Acquire canonical H1 Level-2 public data for the frozen GreenEVT study region.

The script deliberately distinguishes:
  1. small study-area extracts that may be committed to Git;
  2. large authoritative archives that remain externally materialized and are
     represented in Git by exact provenance, query and checksum metadata.

It does not select feeders and does not inspect M0/M1/M2 outcomes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time
from typing import Any

import requests

ROI = {
    "west": -80.198958,
    "south": 35.894145,
    "east": -79.157255,
    "north": 36.410277,
    "crs": "EPSG:4326",
}

FEMA_NFHL = "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28"
GSO_EAM = "https://gis.greensboro-nc.gov/arcgis/rest/services/GISDivision/EAM_DEFAULT_FS/FeatureServer"
USGS_WATER_LOCATIONS = (
    "https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/items"
)
DOE_OUTAGE_ZIP = "https://data.openei.org/files/6458/Outage_Dataset_R1.zip"
TNM_PRODUCTS = "https://tnmaccess.nationalmap.gov/api/v1/products"

SESSION = requests.Session()
SESSION.headers.update(
    {
        "User-Agent": "Dossiya-SE-MSE-thesis/1.0 scientific-reproducibility",
        "Accept-Encoding": "gzip, deflate",
    }
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def get_json(url: str, params: dict[str, Any] | None = None, timeout: int = 120) -> dict:
    last = None
    for attempt in range(4):
        try:
            r = SESSION.get(url, params=params, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except Exception as exc:
            last = exc
            if attempt < 3:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"GET failed for {url}: {last}")


def download(url: str, dest: Path, timeout: int = 300) -> dict:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with SESSION.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        with tmp.open("wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
    tmp.replace(dest)
    return {
        "path": str(dest),
        "size_bytes": dest.stat().st_size,
        "sha256": sha256(dest),
        "source_url": url,
    }


def envelope_json() -> str:
    return json.dumps(
        {
            "xmin": ROI["west"],
            "ymin": ROI["south"],
            "xmax": ROI["east"],
            "ymax": ROI["north"],
            "spatialReference": {"wkid": 4326},
        },
        separators=(",", ":"),
    )


def arcgis_geojson(
    layer_url: str,
    out: Path,
    *,
    where: str = "1=1",
    out_fields: str = "*",
    chunk_size: int = 500,
) -> dict:
    """Retrieve every intersecting feature by OID chunks; never trust a single max-record response."""
    meta = get_json(layer_url, {"f": "pjson"})
    if "error" in meta:
        raise RuntimeError(meta["error"])
    oid_field = meta.get("objectIdField")
    if not oid_field:
        for fld in meta.get("fields", []):
            if fld.get("type") == "esriFieldTypeOID":
                oid_field = fld.get("name")
                break
    if not oid_field:
        raise RuntimeError(f"No object ID field discovered for {layer_url}")

    common = {
        "where": where,
        "geometry": envelope_json(),
        "geometryType": "esriGeometryEnvelope",
        "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects",
        "returnGeometry": "true",
        "outSR": "4326",
    }
    ids = get_json(
        layer_url + "/query",
        {
            **common,
            "returnIdsOnly": "true",
            "returnGeometry": "false",
            "f": "json",
        },
    ).get("objectIds", [])
    ids = sorted(set(int(x) for x in (ids or [])))

    features: list[dict] = []
    for i in range(0, len(ids), chunk_size):
        chunk = ids[i : i + chunk_size]
        r = SESSION.get(
            layer_url + "/query",
            params={
                "objectIds": ",".join(map(str, chunk)),
                "outFields": out_fields,
                "returnGeometry": "true",
                "outSR": "4326",
                "f": "geojson",
            },
            timeout=180,
        )
        r.raise_for_status()
        page = r.json()
        if page.get("type") != "FeatureCollection":
            raise RuntimeError(f"Non-GeoJSON response from {layer_url}: {page}")
        features.extend(page.get("features", []))

    fc = {
        "type": "FeatureCollection",
        "name": meta.get("name"),
        "crs": {"type": "name", "properties": {"name": "EPSG:4326"}},
        "features": features,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(fc, separators=(",", ":")), encoding="utf-8")
    return {
        "source": layer_url,
        "where": where,
        "feature_count": len(features),
        "oid_count": len(ids),
        "oid_field": oid_field,
        "size_bytes": out.stat().st_size,
        "sha256": sha256(out),
        "path": str(out),
    }


def gso_named_layers() -> list[dict]:
    meta = get_json(GSO_EAM, {"f": "pjson"})
    wanted = {
        "Traffic Signal Location",
        "SWS Channel",
        "SWS Culvert",
        "SWS Pipe",
        "SWS Swale",
        "SWS Combo Inlet",
        "SWS Curb Inlet",
        "SWS Grate Inlet",
        "SWS Yard Inlet",
        "SWS Storm Manhole",
    }
    return [x for x in meta.get("layers", []) if x.get("name") in wanted]


def usgs_water_locations(out: Path) -> dict:
    params = {
        "bbox": f'{ROI["west"]},{ROI["south"]},{ROI["east"]},{ROI["north"]}',
        "limit": 10000,
        "f": "json",
    }
    data = get_json(USGS_WATER_LOCATIONS, params)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    n = len(data.get("features", []))
    return {
        "source": USGS_WATER_LOCATIONS,
        "feature_count": n,
        "size_bytes": out.stat().st_size,
        "sha256": sha256(out),
        "path": str(out),
    }


def tnm_3dep_index(out: Path) -> dict:
    params = {
        "bbox": f'{ROI["west"]},{ROI["south"]},{ROI["east"]},{ROI["north"]}',
        "datasets": "Digital Elevation Model (DEM) 1 meter",
        "max": 1000,
        "outputFormat": "JSON",
    }
    data = get_json(TNM_PRODUCTS, params)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return {
        "source": TNM_PRODUCTS,
        "product_count": int(data.get("total", len(data.get("items", [])))),
        "size_bytes": out.stat().st_size,
        "sha256": sha256(out),
        "path": str(out),
        "note": "Index only. DEM tiles are intentionally not committed before feeder/catchment freeze.",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="models/H1/level2/data/materialized")
    ap.add_argument("--include-municipal", action="store_true")
    ap.add_argument("--download-large", action="store_true")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "architecture": "CANONICAL_DATA_ARCHITECTURE_V1.md",
        "roi": ROI,
        "generated_utc": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc
        ).isoformat(),
        "sources": {},
        "claim_boundary": (
            "Materialization does not qualify feeder selection, validate H1, or "
            "convert synthetic topology into observed infrastructure."
        ),
    }

    jobs = [
        (
            "FEMA_NFHL_SFHA",
            lambda: arcgis_geojson(
                FEMA_NFHL,
                outdir / "fema_nfhl_sfha_greenevt_roi.geojson",
                where="SFHA_TF='T'",
                out_fields="*",
            ),
        ),
        (
            "USGS_WATER_LOCATIONS",
            lambda: usgs_water_locations(
                outdir / "usgs_water_monitoring_locations_greenevt_roi.json"
            ),
        ),
        (
            "USGS_3DEP_INDEX",
            lambda: tnm_3dep_index(outdir / "usgs_3dep_1m_product_index.json"),
        ),
    ]

    if args.include_municipal:
        try:
            for layer in gso_named_layers():
                lid = int(layer["id"])
                name = str(layer["name"])
                safe = name.lower().replace(" ", "_").replace("/", "_")
                jobs.append(
                    (
                        "GSO_" + safe.upper(),
                        lambda lid=lid, safe=safe: arcgis_geojson(
                            f"{GSO_EAM}/{lid}",
                            outdir / f"gso_{safe}.geojson",
                        ),
                    )
                )
        except Exception as exc:
            report["sources"]["GSO_LAYER_DISCOVERY"] = {
                "status": "FAILED",
                "error": repr(exc),
                "note": "Municipal redistribution terms must be verified before committing extracts.",
            }

    for source_id, fn in jobs:
        try:
            report["sources"][source_id] = {"status": "PASS", **fn()}
        except Exception as exc:
            report["sources"][source_id] = {
                "status": "FAILED",
                "error": repr(exc),
            }

    if args.download_large:
        try:
            report["sources"]["DOE_EVENT_OUTAGE_ARCHIVE"] = {
                "status": "PASS",
                **download(DOE_OUTAGE_ZIP, outdir / "external" / "Outage_Dataset_R1.zip"),
                "storage_rule": "Do not push to ordinary Git if large; retain checksum and event-specific Guilford extract.",
            }
        except Exception as exc:
            report["sources"]["DOE_EVENT_OUTAGE_ARCHIVE"] = {
                "status": "FAILED",
                "error": repr(exc),
            }

    report_path = outdir / "acquisition_report_v1.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
