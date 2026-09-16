#!/usr/bin/env python3
"""Materialize candidate SMART-DS Houston substations after boundary/inventory gates close.

Scientific authority:
  project/H3_SMARTDS_HOUSTON_PREEXTRACTION_V1.md
  project/H3_SMARTDS_ELECTRICAL_CLOSURE_AND_OPENDSS_QA_V1.md

The utility is intentionally gated. It refuses to download/freeze final Houston power
objects unless the boundary QA status is PASS and a candidate inventory exists.
It preserves raw SMART-DS object bytes, paths, sizes and SHA-256 identities.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

BUCKET = "oedi-data-lake"
S3_HTTPS = "https://oedi-data-lake.s3.amazonaws.com/"
SMARTDS_ROOT = "SMART-DS/v0.9/"
CASE_ID = "H3-HOU-FLOOD-V1"


def fetch(url: str, timeout: int = 240) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MSE-thesis-H3-SMARTDS-materializer/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", 200)
        if status != 200:
            raise RuntimeError(f"HTTP {status}: {url}")
        data = resp.read()
    if not data:
        raise RuntimeError(f"Empty response: {url}")
    return data


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def object_url(key: str) -> str:
    return f"{S3_HTTPS}{urllib.parse.quote(key, safe='/')}"


def s3_list(prefix: str) -> list[dict]:
    objects: list[dict] = []
    token: str | None = None
    while True:
        params = {"list-type": "2", "prefix": prefix}
        if token:
            params["continuation-token"] = token
        url = f"{S3_HTTPS}?{urllib.parse.urlencode(params)}"
        root = ET.fromstring(fetch(url))
        ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
        for item in root.findall("s3:Contents", ns):
            key = item.findtext("s3:Key", default="", namespaces=ns)
            size_txt = item.findtext("s3:Size", default="0", namespaces=ns)
            etag = item.findtext("s3:ETag", default="", namespaces=ns).strip('"')
            modified = item.findtext("s3:LastModified", default="", namespaces=ns)
            if key:
                objects.append(
                    {
                        "key": key,
                        "listed_size": int(size_txt or 0),
                        "etag": etag,
                        "last_modified": modified,
                    }
                )
        truncated = (root.findtext("s3:IsTruncated", default="false", namespaces=ns) or "false").lower()
        if truncated != "true":
            break
        token = root.findtext("s3:NextContinuationToken", default=None, namespaces=ns)
        if not token:
            raise RuntimeError("S3 listing truncated without continuation token")
    return objects


def verify_boundary_gate(root: pathlib.Path) -> None:
    qa = root / "qa" / "boundary" / "houston_boundary_qa.json"
    if not qa.exists():
        raise RuntimeError("Boundary QA file missing; G_Omega_QA is not closed")
    doc = json.loads(qa.read_text())
    if str(doc.get("status", "")).upper() != "PASS":
        raise RuntimeError(f"Boundary QA is not PASS: {doc.get('status')!r}")


def read_candidates(csv_path: pathlib.Path) -> list[dict]:
    if not csv_path.exists():
        raise RuntimeError(f"Candidate inventory missing: {csv_path}")
    with csv_path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    candidates = [r for r in rows if str(r.get("intersects_houston_core", "")).lower() == "true"]
    if not candidates:
        raise RuntimeError("Candidate inventory contains no Houston-core candidate substations")
    return candidates


def safe_relative_key(key: str, prefix: str) -> pathlib.Path:
    if not key.startswith(prefix):
        raise RuntimeError(f"Object key is outside requested prefix: {key}")
    rel = key[len(prefix):]
    if not rel:
        raise RuntimeError(f"Empty object relative path for {key}")
    p = pathlib.PurePosixPath(rel)
    if any(part in {"", ".", ".."} for part in p.parts):
        raise RuntimeError(f"Unsafe relative object path: {rel}")
    return pathlib.Path(*p.parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/H3-HOU-FLOOD-V1")
    parser.add_argument("--year", default="2016")
    parser.add_argument("--scenario", default="base_timeseries")
    parser.add_argument("--inventory", default=None)
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    verify_boundary_gate(root)

    inventory_path = pathlib.Path(args.inventory) if args.inventory else (
        root / "qa" / "power" / f"smartds_houston_inventory_{args.year}_{args.scenario}.csv"
    )
    candidates = read_candidates(inventory_path)

    raw_root = root / "raw" / "power" / f"smartds_v09_{args.year}_Full_Texas"
    manifest_dir = root / "qa" / "manifests"
    qa_dir = root / "qa" / "power"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    qa_dir.mkdir(parents=True, exist_ok=True)

    object_rows: list[dict] = []
    station_rows: list[dict] = []

    for row in candidates:
        subregion = row["subregion"]
        station = row["substation"]
        station_prefix = (
            f"{SMARTDS_ROOT}{args.year}/Full_Texas/{subregion}/"
            f"scenarios/{args.scenario}/opendss/{station}/"
        )
        objects = s3_list(station_prefix)
        if not objects:
            raise RuntimeError(f"No SMART-DS objects found under {station_prefix}")

        station_dir = raw_root / subregion / station
        station_dir.mkdir(parents=True, exist_ok=True)
        master_count = 0
        total_bytes = 0

        for meta in objects:
            key = meta["key"]
            rel = safe_relative_key(key, station_prefix)
            target = station_dir / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            payload = fetch(object_url(key))
            if len(payload) != meta["listed_size"]:
                raise RuntimeError(
                    f"Size mismatch for {key}: listed={meta['listed_size']} downloaded={len(payload)}"
                )
            target.write_bytes(payload)
            digest = sha256(payload)
            total_bytes += len(payload)
            if rel.name.lower() == "master.dss":
                master_count += 1
            object_rows.append(
                {
                    "year": args.year,
                    "scenario": args.scenario,
                    "subregion": subregion,
                    "substation": station,
                    "s3_key": key,
                    "relative_path": rel.as_posix(),
                    "bytes": len(payload),
                    "sha256": digest,
                    "etag": meta["etag"],
                    "last_modified": meta["last_modified"],
                }
            )

        station_rows.append(
            {
                "subregion": subregion,
                "substation": station,
                "station_prefix": station_prefix,
                "object_count": len(objects),
                "downloaded_bytes": total_bytes,
                "master_dss_count": master_count,
                "status": "RAW_FROZEN" if master_count >= 1 else "RAW_FROZEN_NO_MASTER_DSS",
            }
        )

    manifest = {
        "case_id": CASE_ID,
        "access_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "smartds_version": "v0.9",
        "year": args.year,
        "dataset": "Full_Texas",
        "scenario": args.scenario,
        "inventory_file": str(inventory_path),
        "candidate_substations": len(candidates),
        "downloaded_objects": len(object_rows),
        "downloaded_bytes": sum(r["bytes"] for r in object_rows),
        "stations": station_rows,
        "status": "RAW_CANDIDATE_SUBSTATIONS_FROZEN",
        "limitations": [
            "Raw materialization does not itself establish OpenDSS compile or power-flow validity.",
            "Candidate substations are retained whole for electrical integrity; interior-service accounting is handled separately.",
            "No candidate is claimed to represent actual CenterPoint or historical Houston topology.",
        ],
    }

    obj_csv = qa_dir / f"smartds_materialized_objects_{args.year}_{args.scenario}.csv"
    if object_rows:
        with obj_csv.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(object_rows[0].keys()))
            writer.writeheader()
            writer.writerows(object_rows)

    manifest_path = manifest_dir / f"smartds_houston_power_raw_{args.year}_{args.scenario}_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
