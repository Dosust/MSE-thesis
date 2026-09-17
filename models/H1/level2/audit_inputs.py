#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path
from xml.etree import ElementTree as ET

REQUIRED = [
    "data/open_dss/Master.dss",
    "data/open_dss/bus_info.csv",
    "data/open_dss/Long_lat_buscoords.txt",
    "data/sumo_network/greensboro.net.xml",
    "data/sumo_network/greensboro.sumocfg",
    "data/UDS.db",
]


def is_lfs_pointer(path: Path) -> bool:
    try:
        head = path.read_bytes()[:256]
    except OSError:
        return False
    return b"git-lfs.github.com/spec/v1" in head


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def table_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}


def audit_db(path: Path) -> dict:
    out = {"path": str(path), "ok": False}
    if not path.exists() or is_lfs_pointer(path):
        out["error"] = "missing or unresolved Git-LFS pointer"
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
    try:
        edge_count = 0
        junction_count = 0
        signalized = 0
        for event, elem in ET.iterparse(path, events=("end",)):
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
    files = []
    for rel in REQUIRED:
        p = root / rel
        files.append({
            "relative_path": rel,
            "exists": p.exists(),
            "size_bytes": p.stat().st_size if p.exists() else None,
            "git_lfs_pointer": is_lfs_pointer(p) if p.exists() else None,
            "sha256": sha256(p) if p.exists() and not is_lfs_pointer(p) else None,
        })
    db = audit_db(root / "data/UDS.db")
    sumo = audit_sumo(root / "data/sumo_network/greensboro.net.xml")
    all_materialized = all(x["exists"] and not x["git_lfs_pointer"] for x in files)
    report = {
        "level": 2,
        "mode": "realistic",
        "root": str(root),
        "required_files": files,
        "database": db,
        "sumo": sumo,
        "gates": {
            "G1_files_materialized": all_materialized,
            "G2_db_schema": bool(db.get("ok")),
            "G3_sumo_parse": bool(sumo.get("ok")),
        },
    }
    report["pass"] = all(report["gates"].values())
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["pass"] else 2)


if __name__ == "__main__":
    main()
