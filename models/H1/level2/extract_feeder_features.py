#!/usr/bin/env python3
"""Extract Level-2 feeder-selection features under specification v1.1.

Outcome-blind source processing only. This script never selects a feeder.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sqlite3
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from pyproj import CRS, Transformer
from shapely.geometry import LineString, MultiPoint
from shapely.strtree import STRtree

import audit_inputs

SPECIFICATION = "FEEDER_FEATURE_SPECIFICATION_V1_1.md"
UPSTREAM_COMMIT = "6aff1cac48869ccfa0183643979f5f04b04e1124"
FEATURE_COLUMNS = [
    "feeder_id", "C_geo", "C_road", "C_interface", "C_hazard", "C_computable",
    "N_P", "N_T", "N_I", "P_0", "L_T", "R_T", "E_H",
]
HAZARD_REQUIRED_COLUMNS = {
    "feeder_id", "e_P", "e_T", "E_H", "C_hazard", "coverage_status", "source_ref",
}


@dataclass(frozen=True)
class Feeder:
    feeder_id: str
    substation_id: str
    directory: Path
    coords: dict[str, tuple[float, float]]


@dataclass(frozen=True)
class Road:
    edge_id: str
    from_node: str
    to_node: str
    length_m: float
    line: LineString


def finite(x: object) -> bool:
    try:
        return math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def bool_text(v: bool) -> str:
    return "TRUE" if v else "FALSE"


def as_bool(v: object) -> bool:
    return str(v).strip().lower() in {"1", "true", "yes", "pass", "y"}


def chunks(xs: list[str], n: int = 400) -> Iterator[list[str]]:
    for i in range(0, len(xs), n):
        yield xs[i:i+n]


def parse_coords(path: Path) -> dict[str, tuple[float, float]]:
    out: dict[str, tuple[float, float]] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        s = raw.strip()
        if not s or s.startswith(("#", "!")):
            continue
        parts = s.split()
        if len(parts) != 3:
            raise ValueError(f"{path}:{lineno}: expected 'bus lon lat'")
        bus, lo, la = parts
        lon, lat = float(lo), float(la)
        if not finite(lon) or not finite(lat):
            raise ValueError(f"{path}:{lineno}: non-finite coordinate")
        old = out.get(bus)
        if old is not None and old != (lon, lat):
            raise ValueError(f"{path}:{lineno}: conflicting coordinate for {bus}")
        out[bus] = (lon, lat)
    if not out:
        raise ValueError(f"{path}: no coordinates")
    return out


def enumerate_feeders(root: Path) -> list[Feeder]:
    open_dss = root / "data" / "open_dss"
    out: list[Feeder] = []
    for sub in sorted(open_dss.glob("uhs*_1247"), key=lambda p: p.name):
        if not sub.is_dir():
            continue
        for d in sorted(sub.glob(f"{sub.name}--*"), key=lambda p: p.name):
            c = d / "Long_lat_buscoords.txt"
            if d.is_dir() and c.exists():
                out.append(Feeder(d.name, sub.name, d, parse_coords(c)))
    return out


def sumo_transform_and_roads(net_path: Path) -> tuple[Transformer, float, float, list[Road]]:
    location = None
    for _, e in ET.iterparse(net_path, events=("start",)):
        if e.tag == "location":
            location = dict(e.attrib)
            break
    if not location:
        raise ValueError("SUMO network lacks <location>")
    offx, offy = map(float, location["netOffset"].split(","))
    transformer = Transformer.from_crs(
        "EPSG:4326", CRS.from_proj4(location["projParameter"]), always_xy=True
    )

    def lane_allows(attrs: dict[str, str]) -> bool:
        allow = (attrs.get("allow") or "").split()
        disallow = (attrs.get("disallow") or "").split()
        if allow:
            return "passenger" in allow or "all" in allow
        return not ("passenger" in disallow or "all" in disallow)

    roads: list[Road] = []
    cur = None
    for ev, e in ET.iterparse(net_path, events=("start", "end")):
        if ev == "start" and e.tag == "edge":
            eid = e.get("id", "")
            cur = {
                "id": eid,
                "from": e.get("from", ""),
                "to": e.get("to", ""),
                "internal": e.get("function") == "internal" or eid.startswith(":"),
                "shape": e.get("shape"),
                "lane_shape": None,
                "lane_length": None,
                "passenger": False,
            }
        elif ev == "start" and e.tag == "lane" and cur is not None:
            if cur["lane_shape"] is None:
                cur["lane_shape"] = e.get("shape")
            if cur["lane_length"] is None and finite(e.get("length")):
                cur["lane_length"] = float(e.get("length"))
            if lane_allows(e.attrib):
                cur["passenger"] = True
        elif ev == "end" and e.tag == "edge":
            if cur and not cur["internal"] and cur["passenger"]:
                shape = cur["shape"] or cur["lane_shape"]
                if shape and cur["lane_length"] and cur["lane_length"] > 0:
                    pts = [tuple(map(float, pair.split(","))) for pair in shape.split()]
                    if len(pts) >= 2:
                        roads.append(
                            Road(
                                cur["id"],
                                cur["from"],
                                cur["to"],
                                cur["lane_length"],
                                LineString(pts),
                            )
                        )
            cur = None
            e.clear()
        elif ev == "end":
            e.clear()
    return transformer, offx, offy, roads


def load_hazard_table(path: Path | None) -> dict[str, dict]:
    if path is None:
        return {}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or not HAZARD_REQUIRED_COLUMNS.issubset(reader.fieldnames):
            raise ValueError(f"hazard table must contain {sorted(HAZARD_REQUIRED_COLUMNS)}")
        out: dict[str, dict] = {}
        for r in reader:
            fid = r["feeder_id"].strip()
            if not fid or fid in out:
                raise ValueError(f"empty/duplicate hazard feeder_id {fid!r}")
            if as_bool(r["C_hazard"]):
                vals = [float(r[k]) for k in ("e_P", "e_T", "E_H")]
                if not all(math.isfinite(x) and 0 <= x <= 1 for x in vals):
                    raise ValueError(f"invalid hazard values for {fid}")
                if abs(vals[2] - 0.5 * (vals[0] + vals[1])) > 1e-10:
                    raise ValueError(f"E_H mismatch for {fid}")
            out[fid] = dict(r)
    return out


def baseline_kw_from_dss(path: Path) -> float:
    total = 0.0
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = re.search(r"\bkW=([0-9.+\-Ee]+)", line, re.I)
        if m:
            total += float(m.group(1))
    return total


def cycle_rank(roads: list[Road]) -> tuple[float | None, dict]:
    edges: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    for r in roads:
        if not r.from_node or not r.to_node or r.from_node == r.to_node:
            continue
        a, b = sorted((r.from_node, r.to_node))
        edges.add((a, b))
        nodes.update((a, b))
    if not edges:
        return None, {
            "undirected_nodes": len(nodes),
            "undirected_edges": 0,
            "components": 0,
            "cycle_rank": None,
        }
    parent = {n: n for n in nodes}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in edges:
        union(a, b)
    comps = len({find(n) for n in nodes})
    rank = len(edges) - len(nodes) + comps
    if rank < 0:
        raise ValueError("negative cycle rank")
    return rank / len(edges), {
        "undirected_nodes": len(nodes),
        "undirected_edges": len(edges),
        "components": comps,
        "cycle_rank": rank,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--hazard-exposure")
    ap.add_argument("--out", required=True)
    ap.add_argument("--audit-out", required=True)
    ap.add_argument("--require-count", type=int, default=61)
    args = ap.parse_args()

    root = Path(args.greenevt)
    db_path = root / "data" / "UDS.db"
    net_path = root / "data" / "sumo_network" / "greensboro.net.xml"
    db_audit = audit_inputs.audit_db(db_path)
    sumo_audit = audit_inputs.audit_sumo(net_path)
    if not db_audit.get("ok") or not sumo_audit.get("ok"):
        raise SystemExit("exact GreenEVT source audit failed")

    feeders = enumerate_feeders(root)
    if len(feeders) != args.require_count:
        raise SystemExit(f"expected {args.require_count} feeders, found {len(feeders)}")

    transformer, offx, offy, roads = sumo_transform_and_roads(net_path)
    if len(roads) != 118289:
        raise SystemExit(f"unexpected passenger/noninternal road count: {len(roads)}")
    geoms = [r.line for r in roads]
    tree = STRtree(geoms)

    conn = sqlite3.connect(db_path)
    cols = {str(r[1]) for r in conn.execute("pragma table_info(buses)")}
    required = {"id", "bus", "sumo_edge", "active_load"}
    if not required.issubset(cols):
        raise SystemExit(f"UDS buses missing v1.1 columns: {sorted(required-cols)}")
    dup = conn.execute(
        "select count(*) from (select bus,count(*) n from buses group by bus having n>1)"
    ).fetchone()[0]
    if dup:
        raise SystemExit(f"UDS has {dup} duplicate bus names; v1.1 exact bus-name join invalid")

    hazard = load_hazard_table(Path(args.hazard_exposure) if args.hazard_exposure else None)
    feature_rows: list[dict] = []
    audits: dict[str, dict] = {}
    eligible: list[str] = []

    for feeder in feeders:
        names = sorted(feeder.coords)
        records: dict[str, dict] = {}
        for group in chunks(names):
            qs = ",".join("?" for _ in group)
            sql = f"select id,bus,cast(sumo_edge as text),active_load from buses where bus in ({qs})"
            for rid, bus, edge, p0 in conn.execute(sql, group):
                records[str(bus)] = {"id": int(rid), "edge": str(edge), "p0": float(p0)}
        missing = sorted(set(names) - set(records))
        if missing:
            raise SystemExit(f"{feeder.feeder_id}: {len(missing)} feeder buses missing in UDS")

        xy = []
        for lon, lat in feeder.coords.values():
            x, y = transformer.transform(lon, lat)
            xy.append((x + offx, y + offy))
        hull = MultiPoint(xy).convex_hull
        c_geo = hull.geom_type == "Polygon" and hull.area > 0
        selected = [roads[int(i)] for i in tree.query(hull, predicate="intersects")] if c_geo else []
        selected_ids = {r.edge_id for r in selected}
        n_t = len(selected)
        l_t = sum(r.length_m for r in selected) / 1000.0
        r_t, rank_meta = cycle_rank(selected)
        c_road = n_t > 0 and l_t > 0 and r_t is not None and finite(r_t)

        p0 = sum(records[b]["p0"] for b in names)
        dss_p0 = baseline_kw_from_dss(feeder.directory / "Loads_original.dss")
        if abs(p0 - dss_p0) > 1e-6:
            raise SystemExit(f"{feeder.feeder_id}: UDS active_load != Loads_original kW")

        direct = {(b, records[b]["edge"]) for b in names if records[b]["edge"] in selected_ids}
        id_to_name = {records[b]["id"]: b for b in names}
        parcel: set[tuple[str, str]] = set()
        ids = list(id_to_name)
        for group in [ids[i:i+400] for i in range(0, len(ids), 400)]:
            qs = ",".join("?" for _ in group)
            sql = f"select bus_id,cast(sumo_edge as text) from parcels where bus_id in ({qs})"
            for bid, edge in conn.execute(sql, group):
                e = str(edge)
                if e in selected_ids:
                    parcel.add((id_to_name[int(bid)], e))
        interfaces = direct | parcel
        n_i = len(interfaces)
        c_interface = n_i > 0

        hz = hazard.get(feeder.feeder_id)
        if hz is None:
            c_hazard = False
            e_h = ""
            hz_audit = {"status": "MISSING_NOT_ZERO"}
        else:
            c_hazard = as_bool(hz["C_hazard"])
            e_h = float(hz["E_H"]) if c_hazard else ""
            hz_audit = dict(hz)

        numeric_source = all(finite(v) for v in (len(names), n_t, n_i, p0, l_t, r_t))
        c_computable = bool(c_geo and c_road and c_hazard and numeric_source and finite(e_h))
        row = {
            "feeder_id": feeder.feeder_id,
            "C_geo": bool_text(c_geo),
            "C_road": bool_text(c_road),
            "C_interface": bool_text(c_interface),
            "C_hazard": bool_text(c_hazard),
            "C_computable": bool_text(c_computable),
            "N_P": len(names),
            "N_T": n_t,
            "N_I": n_i,
            "P_0": f"{p0:.12g}",
            "L_T": f"{l_t:.12g}",
            "R_T": "" if r_t is None else f"{r_t:.12g}",
            "E_H": "" if e_h == "" else f"{float(e_h):.12g}",
        }
        feature_rows.append(row)
        if all(as_bool(row[p]) for p in ("C_geo", "C_road", "C_interface", "C_hazard", "C_computable")):
            eligible.append(feeder.feeder_id)
        audits[feeder.feeder_id] = {
            "feeder_directory": str(feeder.directory.relative_to(root)),
            "N_P": len(names),
            "hull_area_m2": float(hull.area) if c_geo else None,
            "N_T": n_t,
            "L_T_km": l_t,
            **rank_meta,
            "uds_bus_match_count": len(records),
            "uds_bus_match_fraction": 1.0,
            "P_0_kW": p0,
            "Loads_original_kW": dss_p0,
            "P_0_abs_difference_kW": abs(p0 - dss_p0),
            "direct_bus_edge_pairs": len(direct),
            "parcel_bus_edge_pairs": len(parcel),
            "N_I": n_i,
            "hazard_exposure": hz_audit,
        }

    conn.close()
    with Path(args.out).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FEATURE_COLUMNS)
        w.writeheader()
        w.writerows(feature_rows)

    audit = {
        "specification": SPECIFICATION,
        "upstream_commit": UPSTREAM_COMMIT,
        "feeder_count": len(feature_rows),
        "source_gates": {"database": db_audit, "sumo": sumo_audit},
        "hazard_table_supplied": args.hazard_exposure is not None,
        "eligible_count": len(eligible),
        "eligible_feeders": sorted(eligible),
        "feeders": audits,
        "selection_authorized": False,
        "claim_boundary": "Extraction computes pre-simulation selection descriptors only; qualification and selection are separate gates.",
    }
    Path(args.audit_out).write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in audit.items() if k not in {"feeders", "source_gates"}}, indent=2))


if __name__ == "__main__":
    main()
