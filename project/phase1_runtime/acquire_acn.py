"""Acquire the preregistered Caltech ACN window without exposing credentials.

This script is intentionally data-acquisition only. It preserves every HTTP
page byte-for-byte, writes a canonical session export, and records SHA-256
integrity metadata. It does not perform calibration or validation.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from urllib.parse import urljoin

import pytz
import requests
from acnportal.acndata.utils import http_date


BASE_URL = "https://ev.caltech.edu/api/v1/"
SITE = "caltech"
LOCAL_TZ = pytz.timezone("America/Los_Angeles")
START = LOCAL_TZ.localize(__import__("datetime").datetime(2019, 10, 10, 0, 0, 0))
END = LOCAL_TZ.localize(__import__("datetime").datetime(2019, 12, 31, 23, 59, 59))
OUT_ROOT = Path("data/raw/acn_caltech_20191010_20191231_ts")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def write_atomic(path: Path, payload: bytes) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(payload)
    tmp.replace(path)


def main() -> None:
    token = os.environ.get("ACN_API_TOKEN")
    if not token:
        raise SystemExit("ACN_API_TOKEN is required and must not be committed or logged.")

    if OUT_ROOT.exists() and any(OUT_ROOT.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty immutable raw directory: {OUT_ROOT}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    pages_dir = OUT_ROOT / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    condition = (
        f'connectionTime >= "{http_date(START)}" and '
        f'connectionTime <= "{http_date(END)}"'
    )
    endpoint = urljoin(BASE_URL, f"sessions/{SITE}/ts/")
    params = {"where": condition, "sort": "connectionTime", "max_results": "1"}

    page_records = []
    sessions = []
    next_url = endpoint
    next_params = params
    page_index = 0

    while next_url:
        response = requests.get(
            next_url,
            params=next_params,
            auth=(token, ""),
            timeout=120,
        )
        response.raise_for_status()
        raw = response.content
        page_path = pages_dir / f"page_{page_index:06d}.json"
        write_atomic(page_path, raw)
        page_records.append(
            {
                "index": page_index,
                "file": str(page_path.relative_to(OUT_ROOT)),
                "bytes": len(raw),
                "sha256": sha256_bytes(raw),
                "url_without_credentials": response.url,
            }
        )

        payload = response.json()
        sessions.extend(payload.get("_items", []))
        next_ref = payload.get("_links", {}).get("next", {}).get("href")
        if next_ref:
            next_url = urljoin(BASE_URL, next_ref)
            next_params = None
        else:
            next_url = ""
        page_index += 1

    canonical_path = OUT_ROOT / "sessions_canonical.jsonl"
    with canonical_path.open("wb") as handle:
        for session in sessions:
            line = json.dumps(
                session,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode("utf-8") + b"\n"
            handle.write(line)

    canonical_sha = sha256_bytes(canonical_path.read_bytes())
    manifest = {
        "source": "ACN-Data Caltech",
        "api_base_url": BASE_URL,
        "site": SITE,
        "start_local": START.isoformat(),
        "end_local": END.isoformat(),
        "timeseries": True,
        "record_count": len(sessions),
        "page_count": len(page_records),
        "canonical_export": canonical_path.name,
        "canonical_sha256": canonical_sha,
        "pages": page_records,
    }
    manifest_bytes = json.dumps(
        manifest,
        sort_keys=True,
        indent=2,
        ensure_ascii=False,
    ).encode("utf-8") + b"\n"
    manifest_path = OUT_ROOT / "acquisition_manifest.json"
    write_atomic(manifest_path, manifest_bytes)
    manifest_sha = sha256_bytes(manifest_bytes)

    print(f"records={len(sessions)}")
    print(f"pages={len(page_records)}")
    print(f"canonical_sha256={canonical_sha}")
    print(f"manifest_sha256={manifest_sha}")
    print("credential_logged=false")


if __name__ == "__main__":
    main()
