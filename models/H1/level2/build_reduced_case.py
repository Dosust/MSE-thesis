#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import sqlite3
from pathlib import Path
from xml.etree import ElementTree as ET


def preview_case() -> dict:
    # Deterministic plumbing fixture. Coordinates lie inside the GreenEVT published bounding box,
    # but nodes/edges below are synthetic and MUST NOT be interpreted as Greensboro assets.
    buses = [
        {"id": "P0", "lon": -79.90, "lat": 36.08, "base_load_pu": 0.18},
        {"id": "P1", "lon": -79.86, "lat": 36.07, "base_load_pu": 0.16},
        {"id": "P2", "lon": -79.82, "lat": 36.05, "base_load_pu": 0.14},
        {"id": "P3", "lon": -79.78, "lat": 36.03, "base_load_pu": 0.12},
    ]
    roads = [
        {"id": "R0", "from": "T0", "to": "T1", "length_km": 2.0, "free_speed_kph": 50.0},
        {"id": "R1", "from": "T1", "to": "T2", "length_km": 2.2, "free_speed_kph": 45.0},
        {"id": "R2", "from": "T2", "to": "T3", "length_km": 2.4, "free_speed_kph": 40.0},
    ]
    return {
        "level": 2,
        "mode": "preview",
        "admissible_for_thesis_results": False,
        "lineage": "deterministic software fixture only",
        "dt_h": 1/12,
        "horizon_steps": 24,
        "power_buses": buses,
        "road_edges": roads,
        "chargers": [
            {"id": "C0", "bus_id": "P2", "road_edge_id": "R1", "arrival_vph": 600.0, "capacity_vph": 720.0},
        ],
        "repair_jobs": [
            {"id": "J0", "bus_id": "P3", "road_path": ["R0", "R1", "R2"], "repair_time_h": 0.25},
        ],
        "disturbance": {"failed_bus_id": "P3", "start_step": 5, "charger_outage_steps": 3, "road_congestion_factor": 1.35},
        "provenance": {"all_values_below": "synthetic software verification fixture"},
    }


def sumo_edges(net_path: Path) -> dict[str, dict]:
    out = {}
    for event, elem in ET.iterparse(net_path, events=("end",)):
        if elem.tag == "edge":
            eid = elem.attrib.get("id", "")
            if eid and not eid.startswith(":"):
                lanes = elem.findall("lane")
                if lanes:
                    length = sum(float(x.attrib.get("length", 0.0)) for x in lanes) / len(lanes)
                    speed = max(float(x.attrib.get("speed", 0.0)) for x in lanes)
                    out[eid] = {
                        "id": eid,
                        "from": elem.attrib.get("from"),
                        "to": elem.attrib.get("to"),
                        "length_km": length / 1000.0,
                        "free_speed_kph": speed * 3.6,
                    }
            elem.clear()
    return out


def realistic_case(root: Path, max_buses: int, max_edges: int) -> dict:
    db_path = root / "data/UDS.db"
    net_path = root / "data/sumo_network/greensboro.net.xml"
    if not db_path.exists() or not net_path.exists():
        raise SystemExit("Required GreenEVT files are missing; run audit_inputs.py first")
    edges = sumo_edges(net_path)
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        bus_cols = {r[1] for r in conn.execute("PRAGMA table_info(buses)")}
        active_expr = "active_load" if "active_load" in bus_cols else "0.0"
        rows = conn.execute(
            f"SELECT id,long,lat,sumo_edge,{active_expr} AS active_load FROM buses "
            "WHERE sumo_edge IS NOT NULL AND CAST(sumo_edge AS TEXT) NOT IN ('0','-2','') "
            "ORDER BY active_load DESC LIMIT ?",
            (max_buses,),
        ).fetchall()
        buses = []
        selected_edges = []
        for r in rows:
            sid = str(r["sumo_edge"])
            if sid not in edges:
                continue
            buses.append({
                "id": str(r["id"]),
                "lon": float(r["long"]),
                "lat": float(r["lat"]),
                "base_load_native": float(r["active_load"] or 0.0),
                "sumo_edge_id": sid,
            })
            selected_edges.append(sid)
        # Expand one-hop topological neighborhood without inventing geometry.
        selected = set(selected_edges)
        endpoint_nodes = set()
        for eid in list(selected):
            e = edges[eid]
            endpoint_nodes.update([e.get("from"), e.get("to")])
        for eid, e in edges.items():
            if len(selected) >= max_edges:
                break
            if e.get("from") in endpoint_nodes or e.get("to") in endpoint_nodes:
                selected.add(eid)
        ordered = list(dict.fromkeys(selected_edges + sorted(selected - set(selected_edges))))
        roads = [edges[eid] for eid in ordered[:max_edges]]
        placeholders = ",".join("?" for _ in [b["id"] for b in buses])
        parcel_count = 0
        valid_crosswalks = 0
        if buses:
            q = f"SELECT bus_id,sumo_edge FROM parcels WHERE CAST(bus_id AS TEXT) IN ({placeholders})"
            for pr in conn.execute(q, [b["id"] for b in buses]):
                parcel_count += 1
                if pr[1] is not None and str(pr[1]) in edges:
                    valid_crosswalks += 1
    if not buses:
        raise SystemExit("No valid bus↔SUMO-edge crosswalks found in the selected GreenEVT subset")
    return {
        "level": 2,
        "mode": "realistic",
        "admissible_for_thesis_results": False,
        "admissibility_status": "BLOCKED_PENDING_FROZEN_EXPERIMENT_INPUTS",
        "lineage": "GreenEVT/SMART-DS Greensboro + OSM/SUMO",
        "power_buses": buses,
        "road_edges": roads,
        "crosswalk_audit": {
            "selected_bus_count": len(buses),
            "selected_road_edge_count": len(roads),
            "selected_parcel_rows": parcel_count,
            "parcel_rows_with_valid_road_edge": valid_crosswalks,
        },
        "synthetic_inputs_required_before_run": [
            "disturbance realization",
            "charger placement/capacity unless directly sourced",
            "repair jobs/crew productivity",
            "uncertainty distributions",
        ],
        "claim_boundary": "realistic synthetic spatial mechanism test; not observed-event prediction",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--max-buses", type=int, default=50)
    ap.add_argument("--max-edges", type=int, default=300)
    ap.add_argument("--out", default="case_bundle.json")
    args = ap.parse_args()
    if args.preview:
        case = preview_case()
    else:
        if not args.greenevt:
            raise SystemExit("--greenevt is required unless --preview is used")
        case = realistic_case(Path(args.greenevt), args.max_buses, args.max_edges)
    Path(args.out).write_text(json.dumps(case, indent=2) + "\n")
    print(json.dumps({"written": args.out, "mode": case["mode"], "power_buses": len(case["power_buses"]), "road_edges": len(case["road_edges"])}, indent=2))


if __name__ == "__main__":
    main()
