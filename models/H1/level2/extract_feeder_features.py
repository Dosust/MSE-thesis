#!/usr/bin/env python3
"""Extract preregistered Level-2 feeder-selection features.

This script implements FEEDER_FEATURE_SPECIFICATION_V1.md.  It deliberately
separates source-derived power/transport/interface features from the static
hazard-exposure descriptor E_H.  It never chooses a feeder and it never fills
missing values with defaults.

Selection output produced here is admissible only after:
  * frozen GreenEVT LFS bytes pass audit_inputs.py;
  * every feeder row has complete source-qualified features;
  * a separately qualified static FEMA-NFHL exposure table supplies E_H.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator

try:
    from shapely.geometry import LineString, MultiPoint
except ImportError as exc:  # pragma: no cover - environment dependency
    raise SystemExit("shapely is required; install the frozen GreenEVT requirements") from exc

try:
    import sumolib
except ImportError as exc:  # pragma: no cover - environment dependency
    raise SystemExit("sumolib is required; install the frozen GreenEVT requirements") from exc

import audit_inputs

FEATURE_COLUMNS = [
    "feeder_id",
    "C_geo",
    "C_road",
    "C_interface",
    "C_hazard",
    "C_computable",
    "N_P",
    "N_T",
    "N_I",
    "P_max",
    "L_T",
    "R_T",
    "E_H",
]

HAZARD_REQUIRED_COLUMNS = {
    "feeder_id",
    "e_P",
    "e_T",
    "E_H",
    "C_hazard",
    "coverage_status",
    "source_ref",
}


@dataclass(frozen=True)
class FeederCoordinates:
    feeder_id: str
    substation_id: str
    source_path: str
    coords: dict[str, tuple[float, float]]  # bus_id -> (lon, lat)


@dataclass(frozen=True)
class RoadRecord:
    edge_id: str
    from_node: str
    to_node: str
    length_m: float
    line: LineString
    bounds: tuple[float, float, float, float]


def finite(x: object) -> bool:
    try:
        return math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def bool_text(v: bool) -> str:
    return "TRUE" if v else "FALSE"


def chunks(items: list[str], n: int = 400) -> Iterator[list[str]]:
    for i in range(0, len(items), n):
        yield items[i : i + n]


def parse_feeder_coordinates(path: Path) -> dict[str, tuple[float, float]]:
    """Parse a feeder-level Long_lat_buscoords.txt without silent row loss."""
    coords: dict[str, tuple[float, float]] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("!") or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) != 3:
            raise ValueError(f"{path}:{lineno}: expected 'bus lon lat', got {raw!r}")
        bus, lon_s, lat_s = parts
        try:
            lon = float(lon_s)
            lat = float(lat_s)
        except ValueError as exc:
            raise ValueError(f"{path}:{lineno}: invalid longitude/latitude") from exc
        if not (math.isfinite(lon) and math.isfinite(lat)):
            raise ValueError(f"{path}:{lineno}: non-finite longitude/latitude")
        old = coords.get(bus)
        if old is not None and old != (lon, lat):
            raise ValueError(f"{path}:{lineno}: conflicting coordinates for bus {bus}")
        coords[bus] = (lon, lat)
    if not coords:
        raise ValueError(f"{path}: no valid bus coordinates")
    return coords


def enumerate_feeders(root: Path) -> list[FeederCoordinates]:
    open_dss = root / "data" / "open_dss"
    feeders: list[FeederCoordinates] = []
    for sub in sorted(open_dss.glob("uhs*_1247"), key=lambda p: p.name):
        if not sub.is_dir():
            continue
        for feeder in sorted(sub.glob(f"{sub.name}--*"), key=lambda p: p.name):
            coord_path = feeder / "Long_lat_buscoords.txt"
            if not feeder.is_dir() or not coord_path.exists():
                continue
            feeders.append(
                FeederCoordinates(
                    feeder_id=feeder.name,
                    substation_id=sub.name,
                    source_path=str(feeder.relative_to(root)),
                    coords=parse_feeder_coordinates(coord_path),
                )
            )
    return feeders


def bbox_intersects(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])


def road_inventory(net) -> list[RoadRecord]:
    """Freeze the road universe to non-internal edges allowing passenger class."""
    roads: list[RoadRecord] = []
    for edge in net.getEdges():
        eid = str(edge.getID())
        if eid.startswith(":"):
            continue
        try:
            if str(edge.getFunction()) == "internal":
                continue
        except Exception:
            pass
        if not edge.allows("passenger"):
            continue
        shape = [(float(x), float(y)) for x, y in edge.getShape()]
        if len(shape) < 2:
            continue
        line = LineString(shape)
        length_m = float(edge.getLength())
        if not (line.is_valid and finite(length_m) and length_m > 0):
            continue
        roads.append(
            RoadRecord(
                edge_id=eid,
                from_node=str(edge.getFromNode().getID()),
                to_node=str(edge.getToNode().getID()),
                length_m=length_m,
                line=line,
                bounds=tuple(float(v) for v in line.bounds),
            )
        )
    return roads


def feeder_hull(net, feeder: FeederCoordinates):
    xy = [tuple(map(float, net.convertLonLat2XY(lon, lat))) for lon, lat in feeder.coords.values()]
    distinct = sorted(set(xy))
    if len(distinct) < 3:
        return None, {"distinct_xy_points": len(distinct), "hull_area_m2": None}
    hull = MultiPoint(distinct).convex_hull
    area = float(hull.area)
    if hull.geom_type != "Polygon" or not finite(area) or area <= 0:
        return None, {"distinct_xy_points": len(distinct), "hull_area_m2": area}
    return hull, {"distinct_xy_points": len(distinct), "hull_area_m2": area}


def selected_roads(hull, roads: list[RoadRecord]) -> list[RoadRecord]:
    hb = tuple(float(v) for v in hull.bounds)
    return [r for r in roads if bbox_intersects(hb, r.bounds) and r.line.intersects(hull)]


def normalized_cycle_rank(roads: Iterable[RoadRecord]) -> tuple[float | None, dict]:
    """Normalized cycle rank of the simple undirected projection."""
    edges: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    for r in roads:
        u, v = r.from_node, r.to_node
        if not u or not v or u == v:
            continue  # simple graph projection excludes self loops
        a, b = (u, v) if u < v else (v, u)
        edges.add((a, b))
        nodes.update((a, b))
    if not edges:
        return None, {"undirected_nodes": len(nodes), "undirected_edges": 0, "components": 0, "cycle_rank": None}

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
    components = len({find(n) for n in nodes})
    rank = len(edges) - len(nodes) + components
    if rank < 0:
        raise ValueError("negative cycle rank indicates an implementation error")
    value = rank / len(edges)
    return value, {
        "undirected_nodes": len(nodes),
        "undirected_edges": len(edges),
        "components": components,
        "cycle_rank": rank,
    }


def table_columns(conn: sqlite3.Connection, table: str) -> set[str]:
    return {str(r[1]) for r in conn.execute(f"PRAGMA table_info({table})")}


def fetch_bus_records(conn: sqlite3.Connection, bus_ids: list[str]) -> dict[str, dict]:
    cols = table_columns(conn, "buses")
    required = {"id", "sumo_edge", "max_real_power"}
    missing = required - cols
    if missing:
        raise ValueError(f"UDS buses table lacks feature-required columns: {sorted(missing)}")
    result: dict[str, dict] = {}
    for group in chunks(bus_ids):
        placeholders = ",".join("?" for _ in group)
        sql = (
            "SELECT CAST(id AS TEXT), CAST(sumo_edge AS TEXT), max_real_power "
            f"FROM buses WHERE CAST(id AS TEXT) IN ({placeholders})"
        )
        for bus_id, sumo_edge, max_real_power in conn.execute(sql, group):
            key = str(bus_id)
            if key in result:
                raise ValueError(f"UDS contains duplicate bus id {key}")
            result[key] = {"sumo_edge": None if sumo_edge is None else str(sumo_edge), "max_real_power": max_real_power}
    return result


def fetch_parcel_pairs(conn: sqlite3.Connection, bus_ids: list[str]) -> list[tuple[str, str]]:
    cols = table_columns(conn, "parcels")
    required = {"bus_id", "sumo_edge"}
    missing = required - cols
    if missing:
        raise ValueError(f"UDS parcels table lacks feature-required columns: {sorted(missing)}")
    pairs: list[tuple[str, str]] = []
    for group in chunks(bus_ids):
        placeholders = ",".join("?" for _ in group)
        sql = (
            "SELECT CAST(bus_id AS TEXT), CAST(sumo_edge AS TEXT) FROM parcels "
            f"WHERE CAST(bus_id AS TEXT) IN ({placeholders})"
        )
        for bus_id, edge_id in conn.execute(sql, group):
            if bus_id is not None and edge_id is not None:
                pairs.append((str(bus_id), str(edge_id)))
    return pairs


def interface_and_power_features(
    conn: sqlite3.Connection, feeder: FeederCoordinates, selected_edge_ids: set[str]
) -> tuple[float | None, int, dict]:
    bus_ids = sorted(feeder.coords)
    records = fetch_bus_records(conn, bus_ids)
    missing_bus_ids = sorted(set(bus_ids) - set(records))

    direct_pairs: set[tuple[str, str]] = set()
    direct_missing_edge = 0
    powers: list[float] = []
    invalid_power: list[str] = []

    for bus_id in bus_ids:
        rec = records.get(bus_id)
        if rec is None:
            invalid_power.append(bus_id)
            continue
        edge = rec["sumo_edge"]
        if edge in selected_edge_ids:
            direct_pairs.add((bus_id, edge))
        else:
            direct_missing_edge += 1
        p = rec["max_real_power"]
        if not finite(p):
            invalid_power.append(bus_id)
        else:
            powers.append(float(p))

    parcel_raw = fetch_parcel_pairs(conn, bus_ids)
    parcel_pairs = {(b, e) for b, e in parcel_raw if e in selected_edge_ids}
    interface_pairs = direct_pairs | parcel_pairs

    p_max = sum(powers) if not missing_bus_ids and not invalid_power and len(powers) == len(bus_ids) else None
    audit = {
        "feeder_bus_count": len(bus_ids),
        "uds_bus_match_count": len(records),
        "uds_bus_match_fraction": len(records) / len(bus_ids) if bus_ids else 0.0,
        "missing_uds_bus_ids": missing_bus_ids,
        "invalid_or_missing_max_real_power_bus_ids": sorted(set(invalid_power)),
        "P_max_native_unit": "UDS_NATIVE_UNVERIFIED",
        "direct_bus_edge_valid_pairs": len(direct_pairs),
        "direct_bus_edge_missing_or_outside_roi": direct_missing_edge,
        "parcel_rows_for_feeder_buses": len(parcel_raw),
        "parcel_valid_pairs_in_roi": len(parcel_pairs),
        "distinct_interface_opportunity_pairs": len(interface_pairs),
    }
    return p_max, len(interface_pairs), audit


def load_hazard_table(path: Path | None) -> dict[str, dict]:
    if path is None:
        return {}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or not HAZARD_REQUIRED_COLUMNS.issubset(set(reader.fieldnames)):
            raise ValueError(f"hazard table must contain {sorted(HAZARD_REQUIRED_COLUMNS)}")
        result: dict[str, dict] = {}
        for row in reader:
            fid = row["feeder_id"].strip()
            if not fid or fid in result:
                raise ValueError(f"empty or duplicate feeder_id in hazard table: {fid!r}")
            ep, et, eh = row["e_P"], row["e_T"], row["E_H"]
            c_h = str(row["C_hazard"]).strip().lower() in {"true", "1", "pass", "yes"}
            if c_h:
                if not all(finite(x) for x in (ep, et, eh)):
                    raise ValueError(f"hazard-complete row {fid} has non-finite exposure value")
                epf, etf, ehf = float(ep), float(et), float(eh)
                if not all(0.0 <= x <= 1.0 for x in (epf, etf, ehf)):
                    raise ValueError(f"hazard exposure outside [0,1] for {fid}")
                expected = 0.5 * (epf + etf)
                if abs(ehf - expected) > 1e-10:
                    raise ValueError(f"E_H != 0.5*(e_P+e_T) for {fid}")
            result[fid] = dict(row)
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract frozen pre-simulation feeder-selection features")
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--hazard-exposure", help="Qualified feeder-level FEMA-NFHL exposure CSV; omit to leave E_H blocked")
    ap.add_argument("--out", default="feeder_features_v1.csv")
    ap.add_argument("--audit-out", default="feeder_feature_audit_v1.json")
    ap.add_argument("--require-count", type=int, default=61)
    args = ap.parse_args()

    root = Path(args.greenevt)
    db_path = root / "data" / "UDS.db"
    net_path = root / "data" / "sumo_network" / "greensboro.net.xml"

    # Hard source gate before any feature values are trusted.
    db_audit = audit_inputs.audit_db(db_path)
    sumo_audit = audit_inputs.audit_sumo(net_path)
    if not db_audit.get("ok") or not sumo_audit.get("ok"):
        raise SystemExit(
            "Frozen source audit failed; materialize exact LFS objects and pass audit_inputs.py before feature extraction"
        )

    feeders = enumerate_feeders(root)
    if len(feeders) != args.require_count:
        raise SystemExit(f"Expected {args.require_count} feeder directories, found {len(feeders)}")
    ids = [f.feeder_id for f in feeders]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate feeder IDs discovered")

    net = sumolib.net.readNet(str(net_path), withInternal=True)
    roads = road_inventory(net)
    if not roads:
        raise SystemExit("No passenger-road inventory was constructed from the frozen SUMO network")
    hazard = load_hazard_table(Path(args.hazard_exposure) if args.hazard_exposure else None)

    rows: list[dict[str, object]] = []
    audits: dict[str, dict] = {}

    with sqlite3.connect(db_path) as conn:
        for feeder in feeders:
            row: dict[str, object] = {k: "" for k in FEATURE_COLUMNS}
            row["feeder_id"] = feeder.feeder_id
            feeder_audit = {
                "substation_id": feeder.substation_id,
                "source_path": feeder.source_path,
                "N_P_source_count": len(feeder.coords),
            }

            hull, geo_audit = feeder_hull(net, feeder)
            feeder_audit.update(geo_audit)
            c_geo = hull is not None
            row["C_geo"] = bool_text(c_geo)
            row["N_P"] = len(feeder.coords)

            c_road = False
            c_interface = False
            p_max = None
            n_i = None
            if c_geo:
                local_roads = selected_roads(hull, roads)
                n_t = len(local_roads)
                l_t = sum(r.length_m for r in local_roads) / 1000.0
                r_t, cycle_audit = normalized_cycle_rank(local_roads)
                c_road = n_t > 0 and l_t > 0 and r_t is not None and finite(r_t)
                row["N_T"] = n_t
                row["L_T"] = f"{l_t:.12g}" if finite(l_t) else ""
                row["R_T"] = f"{r_t:.12g}" if r_t is not None and finite(r_t) else ""
                feeder_audit.update(cycle_audit)
                feeder_audit["directed_passenger_edges_in_hull"] = n_t
                feeder_audit["directed_road_length_km"] = l_t

                edge_ids = {r.edge_id for r in local_roads}
                p_max, n_i, cross_audit = interface_and_power_features(conn, feeder, edge_ids)
                feeder_audit.update(cross_audit)
                row["N_I"] = n_i
                row["P_max"] = f"{p_max:.12g}" if p_max is not None and finite(p_max) else ""
                c_interface = bool(n_i and n_i > 0 and cross_audit["uds_bus_match_fraction"] == 1.0)

            row["C_road"] = bool_text(c_road)
            row["C_interface"] = bool_text(c_interface)

            hrow = hazard.get(feeder.feeder_id)
            c_hazard = False
            if hrow is not None:
                c_hazard = str(hrow["C_hazard"]).strip().lower() in {"true", "1", "pass", "yes"}
                if c_hazard:
                    row["E_H"] = f"{float(hrow['E_H']):.12g}"
                feeder_audit["hazard_exposure"] = {
                    "e_P": hrow["e_P"],
                    "e_T": hrow["e_T"],
                    "E_H": hrow["E_H"],
                    "coverage_status": hrow["coverage_status"],
                    "source_ref": hrow["source_ref"],
                }
            else:
                feeder_audit["hazard_exposure"] = {"status": "MISSING_NOT_ZERO"}
            row["C_hazard"] = bool_text(c_hazard)

            feature_values = [row[k] for k in ("N_P", "N_T", "N_I", "P_max", "L_T", "R_T", "E_H")]
            c_computable = c_geo and c_road and c_interface and c_hazard and all(finite(v) for v in feature_values)
            row["C_computable"] = bool_text(c_computable)

            rows.append(row)
            audits[feeder.feeder_id] = feeder_audit

    with Path(args.out).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FEATURE_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    eligible = [r["feeder_id"] for r in rows if all(r[p] == "TRUE" for p in ("C_geo", "C_road", "C_interface", "C_hazard", "C_computable"))]
    audit_doc = {
        "specification": "FEEDER_FEATURE_SPECIFICATION_V1.md",
        "upstream_commit": audit_inputs.FROZEN_UPSTREAM_COMMIT,
        "source_gates": {"database": db_audit, "sumo": sumo_audit},
        "road_inventory": {"passenger_noninternal_edges": len(roads)},
        "feeder_count": len(feeders),
        "hazard_table_supplied": bool(args.hazard_exposure),
        "eligible_count": len(eligible),
        "eligible_feeders": eligible,
        "selection_authorized": len(eligible) >= 2 and len(eligible) == len(rows),
        "selection_rule_note": "Current policy requires a complete qualified 61-row matrix before executing outcome-blind selection; partial eligible subsets are not silently substituted.",
        "feeders": audits,
    }
    Path(args.audit_out).write_text(json.dumps(audit_doc, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "written": args.out,
                "audit_written": args.audit_out,
                "feeders": len(rows),
                "eligible": len(eligible),
                "selection_authorized": audit_doc["selection_authorized"],
            },
            indent=2,
        )
    )

    # Feature extraction itself may legitimately produce a blocked table. It
    # returns success only if source extraction completed; selection remains a
    # separate guarded step.


if __name__ == "__main__":
    main()
