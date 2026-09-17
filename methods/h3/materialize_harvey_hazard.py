#!/usr/bin/env python3
"""Materialize Harvey hazard evidence for H3-HOU-FLOOD-V1.

Scientific authority:
  project/H3_HARVEY_HAZARD_SOURCE_QUALIFICATION_V1.md

This utility preserves raw bytes and provenance. It does not convert flood depth
into infrastructure damage or failure probability.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import shutil
import sys
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone

CASE_ID = "H3-HOU-FLOOD-V1"

USGS_CATALOG_ITEM = "USGS:5aa023ebe4b0b1c392e6881b"
USGS_METADATA_XML = (
    "https://data.usgs.gov/datacatalog/metadata/"
    "USGS.5aa023ebe4b0b1c392e6881b.xml"
)
USGS_SCIENCEBASE_JSON = (
    "https://www.sciencebase.gov/catalog/item/"
    "5aa023ebe4b0b1c392e6881b?format=json"
)

FEMA_HARRIS_AOI = (
    "https://data.femadata.com/FIMA/NHRAP/Harvey/"
    "Harris_AOIandBoundaries.zip"
)
FEMA_HARRIS_DEPTH = (
    "https://data.femadata.com/FIMA/NHRAP/Harvey/"
    "Harris_Mosaic_dgft.zip"
)
FEMA_3M_BACKUP = (
    "https://web.corral.tacc.utexas.edu/nfiedata/Harvey/flood_data/"
    "FEMA_Harvey_Depths_3m.gdb.zip"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: pathlib.Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def fetch_bytes(url: str, timeout: int = 180) -> tuple[bytes, dict]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MSE-thesis-H3-Harvey-hazard/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = resp.read()
        meta = {
            "requested_url": url,
            "final_url": resp.geturl(),
            "status": getattr(resp, "status", 200),
            "content_type": resp.headers.get("Content-Type"),
            "content_length_header": resp.headers.get("Content-Length"),
            "etag": resp.headers.get("ETag"),
            "last_modified": resp.headers.get("Last-Modified"),
        }
    if not payload:
        raise RuntimeError(f"Empty response from {url}")
    return payload, meta


def stream_download(
    url: str,
    out_path: pathlib.Path,
    timeout: int = 300,
    max_bytes: int | None = None,
) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MSE-thesis-H3-Harvey-hazard/1.0"},
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_suffix(out_path.suffix + ".partial")
    h = hashlib.sha256()
    total = 0
    with urllib.request.urlopen(req, timeout=timeout) as resp, tmp.open("wb") as f:
        while True:
            chunk = resp.read(8 * 1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if max_bytes is not None and total > max_bytes:
                raise RuntimeError(
                    f"Download exceeds safety limit ({max_bytes} bytes): {url}"
                )
            f.write(chunk)
            h.update(chunk)
        meta = {
            "requested_url": url,
            "final_url": resp.geturl(),
            "status": getattr(resp, "status", 200),
            "content_type": resp.headers.get("Content-Type"),
            "content_length_header": resp.headers.get("Content-Length"),
            "etag": resp.headers.get("ETag"),
            "last_modified": resp.headers.get("Last-Modified"),
        }
    tmp.replace(out_path)
    return {
        **meta,
        "path": str(out_path),
        "bytes": total,
        "sha256": h.hexdigest(),
    }


def safe_zip_inventory(path: pathlib.Path) -> list[dict]:
    if not zipfile.is_zipfile(path):
        return []
    rows = []
    with zipfile.ZipFile(path, "r") as zf:
        for info in zf.infolist():
            name = info.filename
            p = pathlib.PurePosixPath(name)
            unsafe = p.is_absolute() or ".." in p.parts
            rows.append(
                {
                    "name": name,
                    "compressed_size": info.compress_size,
                    "uncompressed_size": info.file_size,
                    "crc32": f"{info.CRC:08x}",
                    "is_dir": info.is_dir(),
                    "unsafe_path": unsafe,
                }
            )
    return rows


def safe_extract_zip(path: pathlib.Path, dest: pathlib.Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "r") as zf:
        for info in zf.infolist():
            p = pathlib.PurePosixPath(info.filename)
            if p.is_absolute() or ".." in p.parts:
                raise RuntimeError(f"Unsafe ZIP member: {info.filename}")
        zf.extractall(dest)


def write_json(path: pathlib.Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


def materialize_usgs(root: pathlib.Path, download_attachments: bool) -> dict:
    raw = root / "raw" / "hazard" / "usgs_san_jacinto"
    qa = root / "qa" / "hazard"
    raw.mkdir(parents=True, exist_ok=True)
    qa.mkdir(parents=True, exist_ok=True)

    xml_bytes, xml_meta = fetch_bytes(USGS_METADATA_XML)
    xml_path = raw / "USGS_5aa023ebe4b0b1c392e6881b_metadata.xml"
    xml_path.write_bytes(xml_bytes)
    xml_record = {
        **xml_meta,
        "path": str(xml_path),
        "bytes": len(xml_bytes),
        "sha256": hashlib.sha256(xml_bytes).hexdigest(),
    }

    sb_bytes, sb_meta = fetch_bytes(USGS_SCIENCEBASE_JSON)
    sb_path = raw / "sciencebase_item_5aa023ebe4b0b1c392e6881b.json"
    sb_path.write_bytes(sb_bytes)
    try:
        sb = json.loads(sb_bytes.decode("utf-8"))
    except Exception as exc:
        raise RuntimeError("ScienceBase item is not valid UTF-8 JSON") from exc

    file_rows = []
    for fobj in sb.get("files", []) or []:
        row = {
            "name": fobj.get("name"),
            "url": fobj.get("url"),
            "size": fobj.get("size"),
            "contentType": fobj.get("contentType"),
        }
        if download_attachments and row["url"]:
            name = pathlib.Path(str(row["name"] or "attachment.bin")).name
            target = raw / "attachments" / name
            rec = stream_download(str(row["url"]), target)
            row["download"] = rec
            if zipfile.is_zipfile(target):
                row["zip_members"] = safe_zip_inventory(target)
        file_rows.append(row)

    result = {
        "source": "USGS San Jacinto Harvey inundation layers",
        "catalog_item": USGS_CATALOG_ITEM,
        "metadata_xml": xml_record,
        "sciencebase": {
            **sb_meta,
            "path": str(sb_path),
            "bytes": len(sb_bytes),
            "sha256": hashlib.sha256(sb_bytes).hexdigest(),
        },
        "files": file_rows,
        "status": "USGS_METADATA_MATERIALIZED"
        if not download_attachments
        else "USGS_METADATA_AND_ATTACHMENTS_MATERIALIZED",
    }
    write_json(qa / "usgs_san_jacinto_materialization_manifest.json", result)
    return result


def materialize_fema_harris(root: pathlib.Path, extract: bool) -> dict:
    raw = root / "raw" / "hazard" / "fema_harris"
    interim = root / "interim" / "hazard" / "fema_harris"
    qa = root / "qa" / "hazard"
    raw.mkdir(parents=True, exist_ok=True)
    qa.mkdir(parents=True, exist_ok=True)

    records = []
    for label, url, filename in [
        ("Harris_AOIandBoundaries", FEMA_HARRIS_AOI, "Harris_AOIandBoundaries.zip"),
        ("Harris_Mosaic_dgft", FEMA_HARRIS_DEPTH, "Harris_Mosaic_dgft.zip"),
    ]:
        path = raw / filename
        rec = stream_download(url, path)
        rec["label"] = label
        rec["zip_members"] = safe_zip_inventory(path)
        if any(m["unsafe_path"] for m in rec["zip_members"]):
            raise RuntimeError(f"Unsafe ZIP member found in {path}")
        if extract:
            safe_extract_zip(path, interim / label)
            rec["extracted_to"] = str(interim / label)
        records.append(rec)

    result = {
        "source": "FEMA NHRAP Harvey Harris County",
        "records": records,
        "status": "FEMA_HARRIS_RAW_MATERIALIZED_NOT_YET_RASTER_QA",
    }
    write_json(qa / "fema_harris_materialization_manifest.json", result)
    return result


def materialize_large_backup(root: pathlib.Path, allow_large: bool) -> dict:
    if not allow_large:
        raise RuntimeError(
            "Large FEMA 3 m backup is intentionally disabled. Re-run with --allow-large-backup."
        )
    raw = root / "raw" / "hazard" / "fema_3m_backup"
    qa = root / "qa" / "hazard"
    raw.mkdir(parents=True, exist_ok=True)
    path = raw / "FEMA_Harvey_Depths_3m.gdb.zip"
    rec = stream_download(FEMA_3M_BACKUP, path, timeout=1800)
    rec["zip_members"] = safe_zip_inventory(path)
    result = {
        "source": "Archived FEMA Harvey 3 m composite",
        "record": rec,
        "status": "FEMA_3M_BACKUP_MATERIALIZED_NOT_YET_RASTER_QA",
    }
    write_json(qa / "fema_3m_backup_materialization_manifest.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/H3-HOU-FLOOD-V1")
    parser.add_argument(
        "--source",
        choices=["usgs", "fema-harris", "fema-3m-backup", "all-small"],
        default="all-small",
    )
    parser.add_argument("--download-usgs-attachments", action="store_true")
    parser.add_argument("--extract", action="store_true")
    parser.add_argument("--allow-large-backup", action="store_true")
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    manifest = {
        "case_id": CASE_ID,
        "access_utc": utc_now(),
        "source_request": args.source,
        "results": [],
        "limitations": [
            "Successful download does not imply CRS/raster/support QA.",
            "NoData/outside-support cells must not be interpreted as zero depth without source verification.",
            "Flood depth is exposure, not infrastructure damage/failure probability.",
        ],
    }

    if args.source in {"usgs", "all-small"}:
        manifest["results"].append(
            materialize_usgs(root, args.download_usgs_attachments)
        )
    if args.source in {"fema-harris", "all-small"}:
        manifest["results"].append(materialize_fema_harris(root, args.extract))
    if args.source == "fema-3m-backup":
        manifest["results"].append(
            materialize_large_backup(root, args.allow_large_backup)
        )

    manifest_path = root / "qa" / "hazard" / "harvey_hazard_materialization_manifest.json"
    write_json(manifest_path, manifest)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
