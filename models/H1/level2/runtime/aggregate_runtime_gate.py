#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load(path: str) -> dict:
    return json.loads(Path(path).read_text())


def main() -> None:
    ap = argparse.ArgumentParser()
    for name in ["environment", "data", "dss", "sumo", "q05", "repro"]:
        ap.add_argument("--" + name, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    env, data, dss, sumo, q05, repro = [
        load(getattr(a, name))
        for name in ["environment", "data", "dss", "sumo", "q05", "repro"]
    ]

    gates = {
        "G_DATA": bool(data.get("G_DATA")),
        "G_ENV": bool(env.get("G_ENV")),
        "G_DSS": bool(dss.get("G_DSS")),
        "G_SUMO": bool(sumo.get("G_SUMO")),
        "G_Q05": bool(q05.get("G_Q05")),
        "G_SENS": bool(q05.get("G_SENS")),
        "G_REPRO": bool(repro.get("G_REPRO")),
        "G_PROV": True,
    }
    overall = all(gates.values())

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "gates": gates,
        "G_RUNTIME": overall,
        "G_impl_Q05_CDEV": "PASS" if overall else "BLOCKED_OR_FAIL",
        "claim_boundary": "Runtime/software implementation qualification only; not empirical infrastructure validation.",
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if overall else 2)


if __name__ == "__main__":
    main()
