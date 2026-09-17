#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from xml.etree import ElementTree as ET

FROZEN_UPSTREAM_COMMIT = "6aff1cac48869ccfa0183643979f5f04b04e1124"

REQUIRED = [
    "data/open_dss/Master.dss",
    "data/open_dss/bus_info.csv",
    "data/open_dss/Long_lat_buscoords.txt",
    "data/sumo_network/greensboro.net.xml",
    "data/sumo_network/greensboro.sumocfg",
    "data/UDS.db",
]

# Exact Git-LFS identities observed at the frozen GreenEVT commit. These are
# content SHA-256 OIDs from the LFS pointers, not Git blob SHAs.
EXPECTED_LFS = {
    "data/UDS.db": {
        "oid_sha256": "74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724",
        "size_bytes": 107778048,
    },
    "data/sumo_network/greensboro.net.xml": {
        "oid_sha256": "f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06",
        "size_bytes": 351967227,
    },
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_lfs_pointer(path: Path) -> dict | None:
    try:
        raw = path.read_text(errors="replace")
    except OSError:
        return None
    if "git-lfs.github.com/spec/v1" not in raw:
        return None
    oid = re.search(r"^oid sha256:([0-9a-f]{64})$", raw, re.MULTILINE)
    size = re.search(r"^size ([0-9]+)$", raw, re.MULTILINE)
    return {
        "oid_sha256": oid.group(1) if oid else None,
        "size_bytes": int(size.group(1)) if size else None,
    }


def is_lfs_pointer(path: Path) -> bool:
    return parse_lfs_pointer(path) is not None


def inspect_required_file(root: Path, rel: str) -> dict:
    p = root / rel
    out = {
        "relative_path": rel,
        "exists": p.exists(),
        "storage_expected": "git-lfs" if rel in EXPECTED_LFS else "git",
        "size_bytes_on_disk": p.stat().st_size if p.exists() else None,
        "git_lfs_pointer": None,
        "materialized_sha256": None,
        "source_identity_ok": None,
    }
    if not p.exists():
        out["source_identity_ok"] = False
        return out

    pointer = parse_lfs_pointer(p)
    out["git_lfs_pointer"] = pointer
    expected = EXPECTED_LFS.get(rel)

    if pointer is not None:
        if expected is None:
            out["source_identity_ok"] = False
            out["identity_error"] = "unexpected Git-LFS pointer for a file not frozen as LFS"
        else:
            out["source_identity_ok"] = (
                pointer.get("oid_sha256") == expected["oid_sha256"]
                and pointer.get("size_bytes") == expected["size_bytes"]
            )
            if not out["source_identity_ok"]:
                out["identity_error"] = "LFS pointer does not match frozen OID/size"
        out["materialized"] = False
        return out

    out["materialized"] = True
    out["materialized_sha256"] = sha256(p)
    if expected is not None:
        out["source_identity_ok"] = (
            out["materialized_sha256"] == expected["oid_sha256"]
            and p.stat().st_size == expected["size_bytes"]
        )
        if not out["source_identity_ok"]:
            out["identity_error"] = "materialized LFS object does not match frozen SHA-256/size"
    else:
        # For ordinary Git files, existence plus hashing is sufficient here;
        # Git-commit identity is frozen by the acquisition step.
        out["source_identity_ok"] = True
    return out


def table_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}


def audit_db(path: Path) -> dict:
    out = {"path": str(path), "ok": False}
    if not path.exists() or is_lfs_pointer(path):
        out["error"] = "missing or unresolved Git-LFS pointer"
        return out
    expected = EXPECTED_LFS["data/UDS.db"]
    if path.stat().st_size != expected["size_bytes"] or sha256(path) != expected["oid_sha256"]:
        out["error"] = "UDS.db does not match frozen LFS SHA-256/size"
        return out
    try:
        with sqlite3.connect(path) as conn:
            tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            out["tables"] = sorted(tables)
            needed = {"buses", "parcels"}
            if not needed.issubset(tables):
                out["error"] = f"missing tables: {sorted(needed - tables)}"
                return out
            bc = table_columns(conn, "buses")
            pc = table_columns(conn, "parcels")
            out["bus_columns"] = sorted(bc)
            out["parcel_columns"] = sorted(pc)
            req_b = {"id", "long", "lat", "sumo_edge"}
            req_p = {"bus_id", "sumo_edge"}
            if not req_b.issubset(bc) or not req_p.issubset(pc):
                out["error"] = "required GreenEVT crosswalk columns are absent"
                return out
            out["bus_count"] = conn.execute("SELECT COUNT(*) FROM buses").fetchone()[0]
            out["parcel_count"] = conn.execute("SELECT COUNT(*) FROM parcels").fetchone()[0]
            out["bus_missing_edge"] = conn.execute("SELECT COUNT(*) FROM buses WHERE sumo_edge IS NULL OR CAST(sumo_edge AS TEXT) IN ('0','-2','')").fetchone()[0]
            out["parcel_missing_bus"] = conn.execute("SELECT COUNT(*) FROM parcels WHERE bus_id IS NULL OR bus_id < 0").fetchone()[0]
            out["parcel_missing_edge"] = conn.execute("SELECT COUNT(*) FROM parcels WHERE sumo_edge IS NULL OR CAST(sumo_edge AS TEXT) IN ('0','-2','')").fetchone()[0]
            out["ok"] = True
    except sqlite3.DatabaseError as e:
        out["error"] = f"sqlite error: {e}"
    return out


def audit_sumo(path: Path) -> dict:
    out = {"path": str(path), "ok": False}
    if not path.exists() or is_lfs_pointer(path):
        out["error"] = "missing or unresolved Git-LFS pointer"
        return out
    expected = EXPECTED_LFS["data/sumo_network/greensboro.net.xml"]
    if path.stat().st_size != expected["size_bytes"] or sha256(path) != expected["oid_sha256"]:
        out["error"] = "greensboro.net.xml does not match frozen LFS SHA-256/size"
        return out
    try:
        edge_count = 0
        junction_count = 0
        signalized = 0
        for _, elem in ET.iterparse(path, events=("end",)):
            if elem.tag == "edge" and not elem.attrib.get("id", "").startswith(":"):
                edge_count += 1
            elif elem.tag == "junction":
                junction_count += 1
                if elem.attrib.get("type") == "traffic_light":
                    signalized += 1
            elem.clear()
        out.update(edge_count=edge_count, junction_count=junction_count, signalized_junction_count=signalized, ok=edge_count > 0)
    except ET.ParseError as e:
        out["error"] = f"xml parse error: {e}"
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", default="input_audit.json")
    args = ap.parse_args()

    root = Path(args.greenevt)
    files = [inspect_required_file(root, rel) for rel in REQUIRED]
    db = audit_db(root / "data/UDS.db")
    sumo = audit_sumo(root / "data/sumo_network/greensboro.net.xml")

    source_identity_ok = all(bool(x.get("source_identity_ok")) for x in files)
    all_materialized = all(x["exists"] and x.get("materialized") is True for x in files)

    report = {
        "level": 2,
        "mode": "realistic",
        "upstream_commit_expected": FROZEN_UPSTREAM_COMMIT,
        "root": str(root),
        "required_files": files,
        "database": db,
        "sumo": sumo,
        "gates": {
            "G0_frozen_source_identity": source_identity_ok,
            "G1_files_materialized": all_materialized,
            "G2_db_schema": bool(db.get("ok")),
            "G3_sumo_parse": bool(sumo.get("ok")),
        },
    }
    report["pass"] = all(report["gates"].values())
    report["status"] = "PASS" if report["pass"] else "BLOCKED_PENDING_SOURCE_QUALIFICATION_OR_LFS_MATERIALIZATION"
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["pass"] else 2)


if __name__ == "__main__":
    main()
