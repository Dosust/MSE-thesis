#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("run1")
    ap.add_argument("run2")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tol", type=float, default=1e-12)
    a = ap.parse_args()

    r1 = json.loads(Path(a.run1).read_text())
    r2 = json.loads(Path(a.run2).read_text())
    names = sorted(set(r1["fixtures"]) & set(r2["fixtures"]))

    diffs = {}
    passed = True
    for name in names:
        x = float(r1["fixtures"][name]["delta_kW"])
        y = float(r2["fixtures"][name]["delta_kW"])
        diff = abs(x - y)
        ok = diff <= a.tol
        diffs[name] = {
            "run1_delta_kW": x,
            "run2_delta_kW": y,
            "abs_diff_kW": diff,
            "pass": ok,
        }
        passed = passed and ok

    report = {
        "tolerance_kW": a.tol,
        "fixtures": diffs,
        "G_REPRO": passed and bool(names),
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["G_REPRO"] else 2)


if __name__ == "__main__":
    main()
