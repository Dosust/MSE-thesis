#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

LOAD_RE = re.compile(r"kW=([0-9.]+)")


def make_fixture(root: Path, baseline: float = 100.0) -> None:
    od = root / "open_dss"
    feeder = od / "fixture"
    feeder.mkdir(parents=True)
    (od / "Master.dss").write_text(
        "\n".join(
            [
                "Clear",
                "New Circuit.Q05 bus1=source.1.2.3 phases=3 basekV=12.47 pu=1.0",
                "New Line.L1 bus1=source.1.2.3 bus2=testbus.1.2.3 phases=3 length=0.1 units=km r1=0.1 x1=0.2 r0=0.3 x0=0.6",
                "Redirect fixture/Loads.dss",
                "Set VoltageBases=[12.47]",
                "CalcVoltageBases",
                "Solve",
                "",
            ]
        )
    )
    line = (
        f"New Load.Q05 phases=3 bus1=testbus.1.2.3 conn=wye "
        f"kV=7.2 kW={baseline} kvar=20\n"
    )
    (feeder / "Loads_original.dss").write_text(line)
    (feeder / "Loads.dss").write_text(line)


def make_db(n_ev: int) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE vehicles("
        "vehicle_id INTEGER PRIMARY KEY,"
        "bus_name TEXT,"
        "charging_start INTEGER,"
        "charging_end INTEGER,"
        "ev INTEGER,"
        "scenario_id INTEGER)"
    )
    if n_ev == 0:
        conn.execute("INSERT INTO vehicles VALUES(1,'testbus',0,10,0,1)")
    else:
        for i in range(n_ev):
            conn.execute(
                "INSERT INTO vehicles VALUES(?,?,?,?,?,?)",
                (i + 1, "testbus", 0, 10, 1, 1),
            )
    conn.commit()
    return conn


def read_kw(path: Path) -> float:
    match = LOAD_RE.search(path.read_text())
    if not match:
        raise RuntimeError(f"No kW field in {path}")
    return float(match.group(1))


def run_case(greenevt: Path, n_ev: int, p_ev: float) -> dict:
    if str(greenevt) not in sys.path:
        sys.path.insert(0, str(greenevt))
    from scripts.solve_opendss import iteratively_solve_opendss

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        make_fixture(root)
        conn = make_db(n_ev)
        try:
            iteratively_solve_opendss(
                dst_path=str(root),
                db_conn=conn,
                step_size=5,
                scenario_id=1,
                load_per_charging_ev=p_ev,
                export_option="Powers",
            )
        finally:
            conn.close()

        final_kw = read_kw(root / "open_dss/fixture/Loads.dss")
        return {
            "n_ev": n_ev,
            "p_ev_kW": p_ev,
            "baseline_kW": 100.0,
            "final_kW": final_kw,
            "delta_kW": final_kw - 100.0,
        }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    ge = Path(a.greenevt).resolve()

    cases = {
        "zero_ev_7_2": run_case(ge, 0, 7.2),
        "one_ev_7_2": run_case(ge, 1, 7.2),
        "two_ev_7_2": run_case(ge, 2, 7.2),
        "one_ev_disabled": run_case(ge, 1, 0.0),
        "one_ev_7_5": run_case(ge, 1, 7.5),
    }
    expected = {
        "zero_ev_7_2": 0.0,
        "one_ev_7_2": 7.2,
        "two_ev_7_2": 14.4,
        "one_ev_disabled": 0.0,
        "one_ev_7_5": 7.5,
    }
    checks = {
        key: math.isclose(cases[key]["delta_kW"], value, rel_tol=0.0, abs_tol=1e-12)
        for key, value in expected.items()
    }
    checks["linear_scaling"] = math.isclose(
        cases["two_ev_7_2"]["delta_kW"],
        2.0 * cases["one_ev_7_2"]["delta_kW"],
        rel_tol=0.0,
        abs_tol=1e-12,
    )

    report = {
        "fixtures": cases,
        "expected_delta_kW": expected,
        "checks": checks,
        "G_Q05": all(checks.values()),
        "G_SENS": checks["one_ev_7_5"],
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["G_Q05"] and report["G_SENS"] else 2)


if __name__ == "__main__":
    main()
