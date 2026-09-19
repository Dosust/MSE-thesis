#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load(path: str) -> tuple[dict, bool, str | None]:
    p = Path(path)
    if not p.exists():
        return {}, False, "missing"
    try:
        return json.loads(p.read_text()), True, None
    except Exception as exc:
        return {}, False, f"unreadable: {exc}"


def main() -> None:
    ap = argparse.ArgumentParser()
    names = ["environment", "data", "dss", "sumo", "q05", "repro", "provenance"]
    for name in names:
        ap.add_argument("--" + name, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    reports: dict[str, dict] = {}
    input_status: dict[str, dict] = {}
    for name in names:
        payload, ok, error = load(getattr(a, name))
        reports[name] = payload
        input_status[name] = {
            "path": getattr(a, name),
            "readable": ok,
            "error": error,
        }

    gates = {
        "G_DATA": bool(reports["data"].get("G_DATA")),
        "G_ENV": bool(reports["environment"].get("G_ENV")),
        "G_DSS": bool(reports["dss"].get("G_DSS")),
        "G_SUMO": bool(reports["sumo"].get("G_SUMO")),
        "G_Q05": bool(reports["q05"].get("G_Q05")),
        "G_SENS": bool(reports["q05"].get("G_SENS")),
        "G_REPRO": bool(reports["repro"].get("G_REPRO")),
        "G_PROV": bool(reports["provenance"].get("G_PROV")),
    }
    overall = all(gates.values())

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "input_status": input_status,
        "gates": gates,
        "G_RUNTIME": overall,
        "G_impl_Q05_CDEV": "PASS" if overall else "NOT_QUALIFIED",
        "claim_boundary": (
            "Runtime/software implementation qualification only; "
            "not empirical infrastructure validation and not Stage-3 closure."
        ),
    }

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if overall else 2)


if __name__ == "__main__":
    main()
