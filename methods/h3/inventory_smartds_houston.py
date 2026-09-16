#!/usr/bin/env python3
"""Inventory SMART-DS Full_Texas substations against the frozen Houston H3 domain.

This utility is deliberately gated. It may discover public S3 structure without the
Houston polygon, but it MUST NOT perform or claim Houston geographic selection until
project/H3_HOUSTON_BOUNDARY_FREEZE_V1.md has been executed successfully and the
boundary QA file reports PASS.

Scientific authority:
  project/H3_DEMONSTRATOR_FREEZE_V1.md
  project/H3_HOUSTON_BOUNDARY_FREEZE_V1.md
  project/H3_SMARTDS_HOUSTON_PREEXTRACTION_V1.md
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

from shapely.geometry import Point, shape
from shapely.ops import unary_union

BUCKET = "oedi-data-lake"
S3_HTTPS = "https://oedi-data-lake.s3.amazonaws.com/"
SMARTDS_ROOT = "SMART-DS/v0.9/"
CASE_ID = "H3-HOU-FLOOD-V1"


def fetch(url: str, timeout: int = 180) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MSE-thesis-H3-SMARTDS-inventory/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", 200)
        if status != 200:
            raise RuntimeError(f"HTTP {status}: {url}")
        data = resp.read()
    if not data:
        raise RuntimeError(f"Empty response: {url}")
    return data


def s3_list(prefix: str, delimiter: str | None = None) -> tuple[list[str], list[str]]:
    """Return (keys, common_prefixes) for the public OEDI S3 bucket."""
    keys: list[str] = []
    prefixes: list[str] = []
    token: str | None = None

    while True:
        params = {"list-type": "2", "prefix": prefix}
        if delimiter is not None:
            params["delimiter"] = delimiter
        if token:
            params["continuation-token"] = token
        url = f"{S3_HTTPS}?{urllib.parse.urlencode(params)}"
        root = ET.fromstring(fetch(url))
        ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}

        keys.extend(
            el.text for el in root.findall("s3:Contents/s3:Key", ns) if el.text
        )
        prefixes.extend(
            el.text
            for el in root.findall("s3:CommonPrefixes/s3:Prefix", ns)
            if el.text
        )

        truncated = (root.findtext("s3:IsTruncated", default="false", namespaces=ns) or "false").lower()
        if truncated != "true":
            break
        token = root.findtext("s3:NextContinuationToken", default=None, namespaces=ns)
        if not token:
            raise RuntimeError("S3 listing is truncated but no continuation token was returned")

    return keys, prefixes


def object_url(key: str) -> str:
    return f"{S3_HTTPS}{urllib.parse.quote(key, safe='/')}"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_buscoords(payload: bytes) -> list[tuple[str, float, float]]:
    """Parse OpenDSS Buscoords.dss rows as (bus, longitude/x, latitude/y)."""
    text = payload.decode("utf-8", errors="replace")
    out: list[tuple[str, float, float]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("!") or line.startswith("//"):
            continue
        parts = [p for p in re.split(r"[\s,]+", line) if p]
        if len(parts) < 3:
            continue
        try:
            x = float(parts[1])
            y = float(parts[2])
        except ValueError:
            continue
        out.append((parts[0], x, y))
    return out


def load_boundary(root: pathlib.Path):
    qa_path = root / "qa" / "boundary" / "houston_boundary_qa.json"
    core_path = root / "processed" / "boundary" / "houston_core_full_service.geojson"
    if not qa_path.exists() or not core_path.exists():
        raise RuntimeError(
            "Houston boundary QA/core geometry missing. G_Omega_QA must close before geographic SMART-DS selection."
        )
    qa = json.loads(qa_path.read_text())
    if str(qa.get("status", "")).upper() != "PASS":
        raise RuntimeError(f"Houston boundary QA status is not PASS: {qa.get('status')!r}")
    fc = json.loads(core_path.read_text())
    geoms = [shape(f["geometry"]) for f in fc.get("features", []) if f.get("geometry")]
    if not geoms:
        raise RuntimeError("Houston core boundary file contains no geometry")
    geom = unary_union(geoms)
    if geom.is_empty or not geom.is_valid:
        raise RuntimeError("Houston core boundary is empty or invalid")
    return geom, sha256(core_path.read_bytes()), qa_path, core_path


def discover_structure(out_dir: pathlib.Path) -> dict:
    _, year_prefixes = s3_list(SMARTDS_ROOT, delimiter="/")
    years: list[dict] = []
    for yp in sorted(year_prefixes):
        year_name = yp.rstrip("/").split("/")[-1]
        if not year_name.isdigit():
            continue
        _, dataset_prefixes = s3_list(yp, delimiter="/")
        dataset_names = [p.rstrip("/").split("/")[-1] for p in dataset_prefixes]
        years.append(
            {
                "year": year_name,
                "prefix": yp,
                "datasets": sorted(dataset_names),
                "has_Full_Texas": "Full_Texas" in dataset_names,
            }
        )

    result = {
        "case_id": CASE_ID,
        "access_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "bucket": BUCKET,
        "smartds_root": SMARTDS_ROOT,
        "years": years,
        "status": "STRUCTURE_DISCOVERED_NO_HOUSTON_SELECTION",
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "smartds_v09_structure.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    return result


def inventory_houston(root: pathlib.Path, year: str, scenario: str) -> dict:
    boundary, boundary_sha, qa_path, core_path = load_boundary(root)
    dataset_prefix = f"{SMARTDS_ROOT}{year}/Full_Texas/"
    _, subregion_prefixes = s3_list(dataset_prefix, delimiter="/")
    if not subregion_prefixes:
        raise RuntimeError(f"No Full_Texas subregions found under {dataset_prefix}")

    rows: list[dict] = []
    raw_coord_dir = root / "raw" / "power" / "smartds_buscoords"
    raw_coord_dir.mkdir(parents=True, exist_ok=True)

    for subregion_prefix in sorted(subregion_prefixes):
        subregion = subregion_prefix.rstrip("/").split("/")[-1]
        opendss_prefix = f"{subregion_prefix}scenarios/{scenario}/opendss/"
        _, station_prefixes = s3_list(opendss_prefix, delimiter="/")

        for station_prefix in sorted(station_prefixes):
            station = station_prefix.rstrip("/").split("/")[-1]
            if station.lower() in {"analysis", "subtransmission"}:
                continue

            station_keys, _ = s3_list(station_prefix, delimiter=None)
            coord_keys = sorted(k for k in station_keys if k.endswith("Buscoords.dss"))
            if not coord_keys:
                rows.append(
                    {
                        "year": year,
                        "subregion": subregion,
                        "substation": station,
                        "buscoords_files": 0,
                        "coordinate_rows": 0,
                        "plausible_lonlat_rows": 0,
                        "inside_core_rows": 0,
                        "intersects_houston_core": False,
                        "status": "NO_BUSCOORDS",
                    }
                )
                continue

            coordinate_rows = 0
            plausible_rows = 0
            inside_rows = 0
            hashes: list[str] = []
            for key in coord_keys:
                payload = fetch(object_url(key))
                digest = sha256(payload)
                hashes.append(digest)
                safe_name = key.replace("/", "__")
                (raw_coord_dir / safe_name).write_bytes(payload)
                coords = parse_buscoords(payload)
                coordinate_rows += len(coords)
                for _, x, y in coords:
                    # SMART-DS documentation defines Buscoords as longitude/latitude.
                    if not (-180.0 <= x <= 180.0 and -90.0 <= y <= 90.0):
                        continue
                    plausible_rows += 1
                    if boundary.covers(Point(x, y)):
                        inside_rows += 1

            rows.append(
                {
                    "year": year,
                    "subregion": subregion,
                    "substation": station,
                    "buscoords_files": len(coord_keys),
                    "coordinate_rows": coordinate_rows,
                    "plausible_lonlat_rows": plausible_rows,
                    "inside_core_rows": inside_rows,
                    "intersects_houston_core": inside_rows > 0,
                    "buscoords_sha256": ";".join(hashes),
                    "status": "CANDIDATE" if inside_rows > 0 else "OUTSIDE_CORE",
                }
            )

    qa_dir = root / "qa" / "power"
    qa_dir.mkdir(parents=True, exist_ok=True)
    csv_path = qa_dir / f"smartds_houston_inventory_{year}_{scenario}.csv"
    fields = [
        "year",
        "subregion",
        "substation",
        "buscoords_files",
        "coordinate_rows",
        "plausible_lonlat_rows",
        "inside_core_rows",
        "intersects_houston_core",
        "buscoords_sha256",
        "status",
    ]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    candidates = [r for r in rows if r["intersects_houston_core"]]
    manifest = {
        "case_id": CASE_ID,
        "access_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "smartds_version": "v0.9",
        "year": year,
        "scenario": scenario,
        "dataset_prefix": dataset_prefix,
        "boundary_core_file": str(core_path),
        "boundary_core_sha256": boundary_sha,
        "boundary_qa_file": str(qa_path),
        "substations_examined": len(rows),
        "candidate_substations": len(candidates),
        "candidate_ids": [f"{r['subregion']}/{r['substation']}" for r in candidates],
        "inventory_csv": str(csv_path),
        "status": "CANDIDATE_INVENTORY_ONLY",
        "limitations": [
            "Candidate status means at least one documented SMART-DS bus coordinate lies inside Omega_core.",
            "This step does not yet add electrical boundary circuits required for network closure.",
            "This step does not freeze the final H3 power graph, load denominator, or OpenDSS convergence state.",
        ],
    }
    manifest_path = qa_dir / f"smartds_houston_inventory_{year}_{scenario}_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/H3-HOU-FLOOD-V1")
    parser.add_argument(
        "--discover",
        action="store_true",
        help="Discover v0.9 year/dataset structure only; does not perform Houston selection.",
    )
    parser.add_argument("--year", help="SMART-DS year for Full_Texas inventory")
    parser.add_argument("--scenario", default="base_timeseries")
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    if args.discover:
        result = discover_structure(root / "qa" / "power")
    else:
        if not args.year:
            parser.error("--year is required unless --discover is used")
        result = inventory_houston(root, args.year, args.scenario)

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
