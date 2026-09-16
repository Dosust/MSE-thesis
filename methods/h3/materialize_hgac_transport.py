#!/usr/bin/env python3
"""Materialize and inventory H-GAC transportation source files for H3-HOU-FLOOD-V1.

Scientific authority:
  project/H3_HGAC_TRANSPORT_SOURCE_AND_BASEYEAR_QUALIFICATION_V1.md

This script preserves authoritative H-GAC source bytes, computes SHA-256,
records HTTP metadata, and safely inventories/extracts ZIP archives when the
returned payload is a ZIP. It does not clip to Houston, construct the final
transport graph, or infer service thresholds.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import pathlib
import shutil
import sys
import urllib.request
import zipfile
from datetime import datetime, timezone

CASE_ID = "H3-HOU-FLOOD-V1"
SOURCE_PAGE = "https://www.h-gac.com/transportation-conformity/2025"
SOURCES = {
    "C1_travel_model_validation": {
        "url": "https://www.h-gac.com/getmedia/26d3529a-3e1b-4211-83b5-a55515a06589/C1_Travel_Model_Variation",
        "role": "travel-model validation support",
        "posted_or_updated": "2025-08-29",
    },
    "C3_link_listing_capacity": {
        "url": "https://www.h-gac.com/getmedia/6faf4b9d-d6e7-4c7c-830b-7110663b0e52/C3_Link_Listing_and_Capacity_Staging",
        "role": "link listing and capacity staging",
        "posted_or_updated": "2025-10-22",
    },
    "C4_roadway_network_files": {
        "url": "https://www.h-gac.com/getmedia/e1498b1d-470d-4df9-92bb-2d55b749f524/C4_Roadway-Network-Files",
        "role": "roadway network files",
        "posted_or_updated": "2025-10-22",
    },
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_name(text: str) -> str:
    keep = []
    for ch in text:
        keep.append(ch if ch.isalnum() or ch in "-_." else "_")
    return "".join(keep).strip("_") or "source"


def fetch(url: str, timeout: int = 240) -> tuple[bytes, dict[str, str], str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MSE-thesis-H3-HGAC-transport/1.0",
            "Accept": "*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", 200)
        if status != 200:
            raise RuntimeError(f"HTTP {status}: {url}")
        data = resp.read()
        headers = {k.lower(): v for k, v in resp.headers.items()}
        final_url = resp.geturl()
    if not data:
        raise RuntimeError(f"Empty response: {url}")
    return data, headers, final_url


def looks_like_html(data: bytes, content_type: str) -> bool:
    head = data[:512].lstrip().lower()
    return "text/html" in content_type.lower() or head.startswith(b"<!doctype html") or head.startswith(b"<html")


def extension_from_headers(headers: dict[str, str], data: bytes) -> str:
    if data[:4] == b"PK\x03\x04":
        return ".zip"
    content_type = headers.get("content-type", "").split(";", 1)[0].strip()
    ext = mimetypes.guess_extension(content_type) if content_type else None
    return ext or ".bin"


def safe_extract_zip(zip_path: pathlib.Path, dest: pathlib.Path) -> list[dict]:
    dest.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            rel = pathlib.PurePosixPath(info.filename)
            if rel.is_absolute() or ".." in rel.parts:
                raise RuntimeError(f"Unsafe ZIP path: {info.filename}")
            target = dest.joinpath(*rel.parts)
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(info) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            payload = target.read_bytes()
            rows.append(
                {
                    "relative_path": rel.as_posix(),
                    "bytes": len(payload),
                    "sha256": sha256_bytes(payload),
                    "zip_crc32": f"{info.CRC:08x}",
                }
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/H3-HOU-FLOOD-V1")
    parser.add_argument(
        "--source",
        choices=["all", *SOURCES.keys()],
        default="all",
        help="Source object(s) to materialize",
    )
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    raw_dir = root / "raw" / "transport" / "hgac_2025_conformity"
    interim_dir = root / "interim" / "transport" / "hgac_2025_conformity"
    qa_dir = root / "qa" / "transport"
    manifest_dir = root / "qa" / "manifests"
    for d in (raw_dir, interim_dir, qa_dir, manifest_dir):
        d.mkdir(parents=True, exist_ok=True)

    selected = SOURCES if args.source == "all" else {args.source: SOURCES[args.source]}
    accessed = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    records: list[dict] = []

    for source_id, meta in selected.items():
        data, headers, final_url = fetch(meta["url"])
        content_type = headers.get("content-type", "")
        if looks_like_html(data, content_type):
            raise RuntimeError(
                f"{source_id} returned HTML rather than an expected downloadable source object; preserve blocker, do not treat as data"
            )

        ext = extension_from_headers(headers, data)
        filename = safe_name(source_id) + ext
        raw_path = raw_dir / filename
        raw_path.write_bytes(data)

        record = {
            "dataset_id": f"H3-HOU-HGAC-{source_id}",
            "case_id": CASE_ID,
            "source_authority": "Houston-Galveston Area Council (H-GAC)",
            "source_page": SOURCE_PAGE,
            "source_url": meta["url"],
            "resolved_url": final_url,
            "role": meta["role"],
            "posted_or_updated": meta["posted_or_updated"],
            "access_utc": accessed,
            "content_type": content_type,
            "content_disposition": headers.get("content-disposition"),
            "etag": headers.get("etag"),
            "last_modified": headers.get("last-modified"),
            "raw_file": str(raw_path),
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "zip": zipfile.is_zipfile(raw_path),
            "status": "RAW_BYTES_FROZEN",
        }

        if record["zip"]:
            extracted = safe_extract_zip(raw_path, interim_dir / source_id)
            record["archive_members"] = extracted
            record["archive_member_count"] = len(extracted)
        else:
            record["archive_members"] = []
            record["archive_member_count"] = 0

        records.append(record)

    manifest = {
        "case_id": CASE_ID,
        "source_family": "H-GAC 2025 Transportation Conformity",
        "transport_model_base_year": 2023,
        "claim_scope": "raw source materialization and archive inventory only",
        "boundary_qa_required_for_houston_clip": True,
        "records": records,
        "status": "RAW_SOURCE_MATERIALIZED_NOT_YET_HOUSTON_CLIPPED",
        "prohibitions": [
            "Do not infer final Houston graph dimensions from archive presence alone",
            "Do not clip or label links as Houston before G_Omega_QA=1",
            "Do not infer S_T thresholds from conformity network files",
            "Do not treat the 2023 transport model as a historical 2017 Harvey reconstruction",
        ],
    }
    manifest_path = manifest_dir / "hgac_transport_2025_conformity_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    inventory_path = qa_dir / "hgac_transport_archive_inventory.json"
    inventory_path.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
