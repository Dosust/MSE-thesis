#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import sqlite3
from pathlib import Path

import opendssdirect as dss

EXPECTED_ACTIVE_LOAD_KW = 627267.32913


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--greenevt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    root = Path(a.greenevt)
    master = (root / "data/open_dss/Master.dss").resolve()
    db = root / "data/UDS.db"

    dss.Basic.ClearAll()
    compile_result = dss.run_command(f'compile "{master}"')
    solve_result = dss.run_command("Solve")

    converged = bool(dss.Solution.Converged())
    volts = [float(v) for v in dss.Circuit.AllBusMagPu() if float(v) > 0]
    total_power = [float(x) for x in dss.Circuit.TotalPower()]
    losses = [float(x) for x in dss.Circuit.Losses()]

    with sqlite3.connect(db) as conn:
        active_load = float(conn.execute("SELECT SUM(active_load) FROM buses").fetchone()[0])

    checks = {
        "master_exists": master.exists(),
        "converged": converged,
        "nonempty_voltage_solution": len(volts) > 0,
        "active_load_invariant": math.isclose(active_load, EXPECTED_ACTIVE_LOAD_KW, rel_tol=0.0, abs_tol=1e-6),
    }

    report = {
        "compile_result": str(compile_result),
        "solve_result": str(solve_result),
        "converged": converged,
        "voltage_count": len(volts),
        "voltage_min_pu": min(volts) if volts else None,
        "voltage_max_pu": max(volts) if volts else None,
        "total_power": total_power,
        "losses_W_var": losses,
        "source_active_load_sum_kW": active_load,
        "checks": checks,
        "G_DSS": all(checks.values()),
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["G_DSS"] else 2)


if __name__ == "__main__":
    main()
