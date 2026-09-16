#!/usr/bin/env python3
"""Compile and QA materialized SMART-DS Houston candidate substations.

This is a DATA/MODEL QA utility, not the H3 reachability solver. It uses
OpenDSSDirect.py only to verify that the retained SMART-DS OpenDSS models compile,
solve a baseline snapshot, and expose reproducible network dimensions/topology.

Scientific authority:
  project/H3_SMARTDS_ELECTRICAL_CLOSURE_AND_OPENDSS_QA_V1.md
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys
from datetime import datetime, timezone

CASE_ID = "H3-HOU-FLOOD-V1"


def finite_summary(values):
    vals = [float(x) for x in values]
    finite = [x for x in vals if math.isfinite(x)]
    return {
        "count": len(vals),
        "finite_count": len(finite),
        "nonfinite_count": len(vals) - len(finite),
        "min": min(finite) if finite else None,
        "max": max(finite) if finite else None,
    }


def load_manifest(root: pathlib.Path, year: str, scenario: str) -> dict:
    path = root / "qa" / "manifests" / f"smartds_houston_power_raw_{year}_{scenario}_manifest.json"
    if not path.exists():
        raise RuntimeError(f"Materialization manifest missing: {path}")
    doc = json.loads(path.read_text())
    if doc.get("status") != "RAW_CANDIDATE_SUBSTATIONS_FROZEN":
        raise RuntimeError(f"Unexpected materialization status: {doc.get('status')!r}")
    return doc


def find_station_master(station_dir: pathlib.Path) -> pathlib.Path:
    direct = station_dir / "Master.dss"
    if direct.exists():
        return direct
    masters = sorted(p for p in station_dir.rglob("Master.dss") if p.is_file())
    if len(masters) == 1:
        return masters[0]
    if not masters:
        raise RuntimeError(f"No Master.dss found under {station_dir}")
    raise RuntimeError(
        f"Ambiguous station-level Master.dss under {station_dir}: {len(masters)} candidates"
    )


def qa_station(dss, station_dir: pathlib.Path, subregion: str, substation: str) -> dict:
    master = find_station_master(station_dir)
    dss("clear")
    dss(f'redirect "{master.as_posix()}"')
    dss("solve")

    converged = bool(dss.Solution.Converged())
    bus_count = int(dss.Circuit.NumBuses())
    node_count = int(dss.Circuit.NumNodes())
    circuit_element_count = int(dss.Circuit.NumCktElements())
    pd_element_count = int(dss.PDElements.Count())
    line_count = int(dss.Lines.Count())
    transformer_count = int(dss.Transformers.Count())
    load_count = int(dss.Loads.Count())

    try:
        isolated_branches = int(dss.Topology.NumIsolatedBranches())
    except Exception:
        isolated_branches = None
    try:
        isolated_loads = int(dss.Topology.NumIsolatedLoads())
    except Exception:
        isolated_loads = None
    try:
        loops = int(dss.Topology.NumLoops())
    except Exception:
        loops = None

    try:
        vpu = finite_summary(dss.Circuit.AllBusMagPu())
    except Exception:
        vpu = None

    try:
        total_power = [float(x) for x in dss.Circuit.TotalPower()]
    except Exception:
        total_power = None

    hard_pass = (
        converged
        and bus_count > 0
        and pd_element_count > 0
        and load_count >= 0
        and (vpu is None or vpu["nonfinite_count"] == 0)
    )

    return {
        "subregion": subregion,
        "substation": substation,
        "station_dir": str(station_dir),
        "master_dss": str(master),
        "converged": converged,
        "bus_count": bus_count,
        "node_count": node_count,
        "circuit_element_count": circuit_element_count,
        "pd_element_count": pd_element_count,
        "line_count": line_count,
        "transformer_count": transformer_count,
        "load_count": load_count,
        "isolated_branches": isolated_branches,
        "isolated_loads": isolated_loads,
        "loops": loops,
        "bus_voltage_pu_summary": vpu,
        "total_power_kw_kvar_sign_convention_native": total_power,
        "status": "PASS_BASELINE_COMPILE_SOLVE" if hard_pass else "FAIL_BASELINE_QA",
        "note": (
            "Voltage extrema are reported descriptively only. No thesis voltage-limit pass/fail threshold "
            "is imposed here without an independently qualified engineering criterion."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/H3-HOU-FLOOD-V1")
    parser.add_argument("--year", default="2016")
    parser.add_argument("--scenario", default="base_timeseries")
    args = parser.parse_args()

    try:
        from opendssdirect import dss
        import opendssdirect
    except Exception as exc:
        raise RuntimeError(
            "OpenDSSDirect.py is required for the baseline compile/solve gate"
        ) from exc

    root = pathlib.Path(args.root)
    manifest = load_manifest(root, args.year, args.scenario)
    raw_root = root / "raw" / "power" / f"smartds_v09_{args.year}_Full_Texas"
    if not raw_root.exists():
        raise RuntimeError(f"Materialized power root missing: {raw_root}")

    rows = []
    for station in manifest.get("stations", []):
        subregion = station["subregion"]
        substation = station["substation"]
        station_dir = raw_root / subregion / substation
        rows.append(qa_station(dss, station_dir, subregion, substation))

    if not rows:
        raise RuntimeError("No materialized candidate substations found for QA")

    aggregate = {
        "N_P_sim_buses": sum(r["bus_count"] for r in rows),
        "N_P_sim_nodes": sum(r["node_count"] for r in rows),
        "M_P_sim_power_delivery_elements": sum(r["pd_element_count"] for r in rows),
        "line_count": sum(r["line_count"] for r in rows),
        "transformer_count": sum(r["transformer_count"] for r in rows),
        "load_count": sum(r["load_count"] for r in rows),
        "candidate_substations": len(rows),
        "stations_passed": sum(r["status"] == "PASS_BASELINE_COMPILE_SOLVE" for r in rows),
        "stations_failed": sum(r["status"] != "PASS_BASELINE_COMPILE_SOLVE" for r in rows),
    }

    all_pass = aggregate["stations_failed"] == 0
    result = {
        "case_id": CASE_ID,
        "execution_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "smartds_version": "v0.9",
        "year": args.year,
        "scenario": args.scenario,
        "opendssdirect_version": getattr(opendssdirect, "__version__", "UNKNOWN"),
        "engine_version": dss.Basic.Version(),
        "stations": rows,
        "aggregate": aggregate,
        "status": "PASS_POWER_BASELINE_QA" if all_pass else "FAIL_POWER_BASELINE_QA",
        "scope": (
            "This gate verifies materialized SMART-DS model compile/solve integrity and reports network dimensions. "
            "It does not validate historical Houston topology, H3 service thresholds, hazard response, or reachability."
        ),
    }

    out_dir = root / "qa" / "power"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"smartds_power_baseline_qa_{args.year}_{args.scenario}.json"
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))

    return 0 if all_pass else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
