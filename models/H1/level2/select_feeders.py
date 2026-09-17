#!/usr/bin/env python3
from __future__ import annotations
import argparse
import csv
import json
import math
import statistics
from pathlib import Path

PREDICATES = ("C_geo", "C_road", "C_interface", "C_hazard", "C_computable")
FEATURES = ("N_P", "N_T", "N_I", "P_max", "L_T", "R_T", "E_H")


def as_bool(x: str) -> bool:
    return str(x).strip().lower() in {"1", "true", "yes", "y", "pass"}


def robust_scale(rows: list[dict[str, str]]) -> dict[str, list[float]]:
    cols = {f: [float(r[f]) for r in rows] for f in FEATURES}
    centers = {f: statistics.median(vals) for f, vals in cols.items()}
    scales = {}
    for f, vals in cols.items():
        med = centers[f]
        mad = statistics.median(abs(x - med) for x in vals)
        scale = 1.4826 * mad
        if scale <= 1e-15:
            scale = statistics.pstdev(vals) if len(vals) > 1 else 0.0
        scales[f] = scale if scale > 1e-15 else 1.0
    return {r["feeder_id"]: [(float(r[f]) - centers[f]) / scales[f] for f in FEATURES] for r in rows}


def dist(a: list[float], b: list[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def select(rows: list[dict[str, str]]) -> dict:
    eligible = [r for r in rows if all(as_bool(r[p]) for p in PREDICATES)]
    if len(eligible) < 2:
        raise ValueError("At least two feeders must satisfy every predeclared eligibility predicate")
    for r in eligible:
        for f in FEATURES:
            if r.get(f, "") == "":
                raise ValueError(f"missing {f} for eligible feeder {r.get('feeder_id')}")
    z = robust_scale(eligible)
    ids = sorted(z)
    D = {(i, j): dist(z[i], z[j]) for i in ids for j in ids}

    # Development case: global medoid, selected only from pre-simulation features.
    dev = min(ids, key=lambda i: (sum(D[i, j] for j in ids), i))

    # Held-out case: second representative medoid that improves feature-space
    # coverage conditional on the frozen development medoid. No model outcomes enter.
    candidates = [i for i in ids if i != dev]
    hold = min(
        candidates,
        key=lambda h: (sum(min(D[j, dev], D[j, h]) for j in ids), h),
    )

    return {
        "selection_status": "FROZEN_FROM_PRESIMULATION_FEATURES",
        "development_feeder_id": dev,
        "heldout_feeder_id": hold,
        "n_eligible": len(ids),
        "eligible_feeders": ids,
        "predicates": list(PREDICATES),
        "features": list(FEATURES),
        "standardization": "median / 1.4826*MAD; fallback population SD; zero-variance features contribute zero",
        "development_rule": "global medoid minimizing total standardized Euclidean distance",
        "heldout_rule": "conditional second medoid minimizing total distance to nearest of development/heldout medoid",
        "outcome_blind": True,
        "audit": {
            "development_total_distance": sum(D[dev, j] for j in ids),
            "two_medoid_coverage_objective": sum(min(D[j, dev], D[j, hold]) for j in ids),
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", required=True, help="CSV matching registries/feeder_features_template.csv")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    with Path(args.features).open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    result = select(rows)
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
