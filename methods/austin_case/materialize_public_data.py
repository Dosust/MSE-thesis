#!/usr/bin/env python3
"""Materialize public Austin case-study inputs with immutable provenance.

Scientific role
---------------
This instrument closes data-access/QC gates only. It does not estimate coupling
parameters, select thresholds, fit hypotheses, or execute H1--H5.

Order of operations
-------------------
1. acquire SMART-DS P5U Buscoords from public OEDI S3;
2. derive a query envelope from documented bus coordinates;
3. acquire City of Austin boundary/road/signal/flood features intersecting the
   envelope using ArcGIS REST;
4. acquire traffic-detector and travel-sensor location tables from Socrata;
5. freeze raw bytes + SHA-256 + source URLs + row/feature counts in a manifest.

The exact P5U asset footprint and final cross-layer admissibility are evaluated
by a separate QA step. A successful download is therefore never equivalent to
case admissibility.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping

CASE_ID = "AUS-P5U-2018-V1"
USER_AGENT = "MSE-thesis-Austin-admissibility/1.0"
OEDI_HTTPS = "https://oedi-data-lake.s3.amazonaws.com/"
SMARTDS_PREFIX = "SMART-DS/v1.0/2018/AUS/P5U/"
SMARTDS_SCENARIO = "base_timeseries"
SMARTDS_OPENDSS_PREFIX = (
    SMARTDS_PREFIX + f"scenarios/{SMARTDS_SCENARIO}/opendss/"
)

BOUNDARY_LAYER = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/"
    "City_of_Austin_WFL1/FeatureServer/0"
)
ROAD_LAYER = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/"
    "TRANSPORTATION_street_segment/FeatureServer/0"
)
SIGNAL_LAYER = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/"
    "TRANSPORTATION_signals2/FeatureServer/0"
)
FLOOD_LAYER = "https://maps.austintexas.gov/gis/rest/Shared/Floodplain/MapServer/1"

CAMERA_DETECTOR_LOCATIONS = "qpuw-8eeb"
RADAR_SENSOR_LOCATIONS = "6yd9-yz29"
SOCRATA_DOMAIN = "https://data.austintexas.gov"


class MaterializationError(RuntimeError):
    """Raised when immutable public-data acquisition cannot satisfy its contract."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def fetch(url: str, timeout: int = 180) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        status = getattr(response, "status", 200)
        if status != 200:
            raise MaterializationError(f"HTTP {status}: {url}")
        payload = response.read()
    if not payload:
        raise MaterializationError(f"empty response: {url}")
    return payload


def write_immutable(path: pathlib.Path, payload: bytes) -> dict[str, Any]:
    """Write one raw object without silently overwriting prior evidence."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_bytes()
        if existing != payload:
            raise MaterializationError(
                f"refusing to overwrite immutable raw object with changed bytes: {path}"
            )
        state = "EXISTS_IDENTICAL"
    else:
        path.write_bytes(payload)
        state = "WRITTEN"
    return {
        "path": str(path),
        "bytes": len(payload),
        "sha256": sha256_bytes(payload),
        "write_state": state,
    }


def object_url(key: str) -> str:
    return OEDI_HTTPS + urllib.parse.quote(key, safe="/")


def s3_list_url(prefix: str, delimiter: str | None = None) -> str:
    params = {"list-type": "2", "prefix": prefix}
    if delimiter is not None:
        params["delimiter"] = delimiter
    return OEDI_HTTPS + "?" + urllib.parse.urlencode(params)


def parse_s3_listing(payload: bytes) -> tuple[list[str], list[str]]:
    root = ET.fromstring(payload)
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    keys = [
        el.text
        for el in root.findall("s3:Contents/s3:Key", ns)
        if el.text is not None
    ]
    prefixes = [
        el.text
        for el in root.findall("s3:CommonPrefixes/s3:Prefix", ns)
        if el.text is not None
    ]
    return keys, prefixes


def parse_buscoords(payload: bytes) -> list[tuple[str, float, float]]:
    """Parse SMART-DS/OpenDSS Buscoords rows as bus, longitude, latitude."""
    text = payload.decode("utf-8", errors="replace")
    rows: list[tuple[str, float, float]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("!") or line.startswith("//"):
            continue
        parts = [part for part in re.split(r"[\s,]+", line) if part]
        if len(parts) < 3:
            continue
        try:
            x = float(parts[1])
            y = float(parts[2])
        except ValueError:
            continue
        if -180.0 <= x <= 180.0 and -90.0 <= y <= 90.0:
            rows.append((parts[0], x, y))
    if not rows:
        raise MaterializationError("Buscoords contains no plausible longitude/latitude rows")
    return rows


def bounds(coords: Iterable[tuple[str, float, float]]) -> tuple[float, float, float, float]:
    values = list(coords)
    if not values:
        raise MaterializationError("cannot compute bounds from empty coordinate set")
    xs = [row[1] for row in values]
    ys = [row[2] for row in values]
    return min(xs), min(ys), max(xs), max(ys)


def arcgis_query_url(
    layer: str,
    bbox: tuple[float, float, float, float] | None = None,
    *,
    where: str = "1=1",
) -> str:
    params: dict[str, str] = {
        "where": where,
        "outFields": "*",
        "returnGeometry": "true",
        "outSR": "4326",
        "f": "geojson",
    }
    if bbox is not None:
        xmin, ymin, xmax, ymax = bbox
        params.update(
            {
                "geometry": f"{xmin},{ymin},{xmax},{ymax}",
                "geometryType": "esriGeometryEnvelope",
                "inSR": "4326",
                "spatialRel": "esriSpatialRelIntersects",
            }
        )
    return layer.rstrip("/") + "/query?" + urllib.parse.urlencode(params)


def socrata_export_url(dataset_id: str) -> str:
    # v2 resource endpoint remains suitable for immutable read-only bulk JSON of
    # the small detector-location tables and does not require an app token.
    return f"{SOCRATA_DOMAIN}/resource/{dataset_id}.json?$limit=50000"


def json_count(payload: bytes) -> int:
    obj = json.loads(payload)
    if isinstance(obj, list):
        return len(obj)
    if isinstance(obj, Mapping) and isinstance(obj.get("features"), list):
        return len(obj["features"])
    raise MaterializationError("JSON object has no recognized row/feature collection")


def _find_buscoords_key(listing: bytes) -> str:
    keys, _ = parse_s3_listing(listing)
    exact = [key for key in keys if key.endswith("/Buscoords.dss")]
    if not exact:
        raise MaterializationError(
            f"no Buscoords.dss found under {SMARTDS_OPENDSS_PREFIX}"
        )
    # A subregion-level Buscoords file is expected directly below opendss/. If
    # multiple files are returned, choose the shallowest only; the full key is
    # frozen in the manifest and later QA rejects ambiguity if needed.
    exact.sort(key=lambda key: (key.count("/"), key))
    return exact[0]


def acquire(root: pathlib.Path) -> dict[str, Any]:
    raw = root / "raw"
    qa = root / "qa"
    qa.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, Any] = {
        "case_id": CASE_ID,
        "acquired_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": "RAW_MATERIALIZATION_ONLY",
        "objects": {},
        "scientific_prohibitions": [
            "download success is not case admissibility",
            "SMART-DS is synthetic and is not Austin Energy topology",
            "P5U query envelope is an acquisition filter, not a utility service boundary",
            "no coupling parameter, threshold, or probability law is estimated here",
        ],
    }

    listing_url = s3_list_url(SMARTDS_OPENDSS_PREFIX)
    listing = fetch(listing_url)
    record = write_immutable(raw / "power" / "opendss_listing.xml", listing)
    record["source_url"] = listing_url
    manifest["objects"]["smartds_listing"] = record

    buscoords_key = _find_buscoords_key(listing)
    buscoords_url = object_url(buscoords_key)
    buscoords_payload = fetch(buscoords_url)
    buscoords_record = write_immutable(raw / "power" / "Buscoords.dss", buscoords_payload)
    coords = parse_buscoords(buscoords_payload)
    query_bbox = bounds(coords)
    buscoords_record.update(
        {
            "source_url": buscoords_url,
            "source_key": buscoords_key,
            "plausible_lonlat_rows": len(coords),
            "bbox_wgs84": query_bbox,
        }
    )
    manifest["objects"]["smartds_buscoords"] = buscoords_record

    geo_sources = {
        "austin_full_purpose": (BOUNDARY_LAYER, None, "1=1"),
        "street_centerline": (ROAD_LAYER, query_bbox, "1=1"),
        "traffic_signals": (SIGNAL_LAYER, query_bbox, "1=1"),
        "fema_floodplain": (FLOOD_LAYER, query_bbox, "1=1"),
    }
    for name, (layer, bbox, where) in geo_sources.items():
        url = arcgis_query_url(layer, bbox, where=where)
        payload = fetch(url)
        record = write_immutable(raw / "gis" / f"{name}.geojson", payload)
        record.update({"source_url": url, "feature_count": json_count(payload)})
        manifest["objects"][name] = record

    traffic_sources = {
        "camera_detector_locations": CAMERA_DETECTOR_LOCATIONS,
        "radar_sensor_locations": RADAR_SENSOR_LOCATIONS,
    }
    for name, dataset_id in traffic_sources.items():
        url = socrata_export_url(dataset_id)
        payload = fetch(url)
        record = write_immutable(raw / "traffic" / f"{name}.json", payload)
        record.update(
            {
                "source_url": url,
                "dataset_id": dataset_id,
                "row_count": json_count(payload),
            }
        )
        manifest["objects"][name] = record

    manifest_path = qa / "raw_materialization_manifest.json"
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    manifest_path.write_bytes(manifest_bytes)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/AUS-P5U-2018-V1")
    args = parser.parse_args()
    acquire(pathlib.Path(args.root))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=__import__("sys").stderr)
        raise SystemExit(1)
