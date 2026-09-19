#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from pathlib import Path
from xml.etree import ElementTree as ET

EXPECTED = {
    "data/UDS.db": {"bytes": 107778048, "sha256": "74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724"},
    "data/sumo_network/greensboro.net.xml": {"bytes": 351967227, "sha256": "f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06"},
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root = Path(a.greenevt)

    objects = {}
    for rel, exp in EXPECTED.items():
        p = root / rel
        got = {"exists": p.exists(), "bytes": p.stat().st_size if p.exists() else None, "sha256": sha256(p) if p.exists() else None}
        got["pass"] = got["exists"] and got["bytes"] == exp["bytes"] and got["sha256"] == exp["sha256"]
        objects[rel] = got

    db_ok = False
    db_info = {}
    db = root / "data/UDS.db"
    if objects["data/UDS.db"]["pass"]:
        with sqlite3.connect(db) as conn:
            tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            db_info = {
                "bus_rows": conn.execute("SELECT COUNT(*) FROM buses").fetchone()[0],
                "parcel_rows": conn.execute("SELECT COUNT(*) FROM parcels").fetchone()[0],
                "active_load_sum_kW": conn.execute("SELECT SUM(active_load) FROM buses").fetchone()[0],
            }
            db_ok = {"buses", "parcels"}.issubset(tables)

    edges = 0
    tl_logic = 0
    xml_ok = False
    net = root / "data/sumo_network/greensboro.net.xml"
    if objects["data/sumo_network/greensboro.net.xml"]["pass"]:
        for _, elem in ET.iterparse(net, events=("end",)):
            if elem.tag == "edge" and not elem.attrib.get("id", "").startswith(":"):
                edges += 1
            elif elem.tag == "tlLogic":
                tl_logic += 1
            elem.clear()
        xml_ok = edges == 118289 and tl_logic == 914

    report = {
        "objects": objects,
        "database": {"pass": db_ok, **db_info},
        "sumo_xml": {"pass": xml_ok, "noninternal_edges": edges, "tlLogic_count": tl_logic},
    }
    report["G_DATA"] = all(x["pass"] for x in objects.values()) and db_ok and xml_ok

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["G_DATA"] else 2)


if __name__ == "__main__":
    main()
