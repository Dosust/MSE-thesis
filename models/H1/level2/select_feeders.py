#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path

PREDICATES = ("C_geo", "C_road", "C_interface", "C_hazard", "C_computable")
FEATURES = ("N_P", "N_T", "N_I", "P_max", "L_T", "R_T", "E_H")
REQUIRED_COLUMNS = ("feeder_id",) + PREDICATES + FEATURES
EXPECTED_SPEC = "FEEDER_FEATURE_SPECIFICATION_V1.md"
EXPECTED_COMMIT = "6aff1cac48869ccfa0183643979f5f04b04e1124"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


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


def validate_rows(rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("feature table is empty")
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in rows[0]]
    if missing_cols:
        raise ValueError(f"feature table missing required columns: {missing_cols}")
    ids = [str(r.get("feeder_id", "")).strip() for r in rows]
    if any(not x for x in ids):
        raise ValueError("feature table contains an empty feeder_id")
    if len(ids) != len(set(ids)):
        raise ValueError("feature table contains duplicate feeder_id values")


def validate_feature_audit(rows: list[dict[str, str]], audit: dict, feature_path: Path) -> None:
    """Hard guard against manually edited/unqualified selection matrices."""
    if audit.get("specification") != EXPECTED_SPEC:
        raise ValueError("feature audit does not identify the frozen feature specification")
    if audit.get("upstream_commit") != EXPECTED_COMMIT:
        raise ValueError("feature audit upstream commit does not match the frozen GreenEVT commit")
    if int(audit.get("feeder_count", -1)) != len(rows):
        raise ValueError("feature audit feeder count does not match feature CSV")
    if audit.get("selection_authorized") is not True:
        raise ValueError("feature audit has not authorized outcome-blind feeder selection")
    recorded_sha = audit.get("feature_csv_sha256")
    if not recorded_sha:
        raise ValueError("feature audit lacks feature_csv_sha256")
    actual_sha = sha256(feature_path)
    if recorded_sha != actual_sha:
        raise ValueError("feature CSV hash differs from the file authorized by the feature audit")

    eligible_csv = sorted(
        r["feeder_id"] for r in rows if all(as_bool(r[p]) for p in PREDICATES)
    )
    eligible_audit = sorted(str(x) for x in audit.get("eligible_feeders", []))
    if eligible_csv != eligible_audit:
        raise ValueError("eligible feeder set differs between feature CSV and audit")
    if int(audit.get("eligible_count", -1)) != len(eligible_csv):
        raise ValueError("eligible feeder count differs between feature CSV and audit")


def select(rows: list[dict[str, str]]) -> dict:
    validate_rows(rows)
    eligible = [r for r in rows if all(as_bool(r[p]) for p in PREDICATES)]
    if len(eligible) < 2:
        raise ValueError("At least two feeders must satisfy every predeclared eligibility predicate")
    for r in eligible:
        for f in FEATURES:
            if r.get(f, "") == "":
                raise ValueError(f"missing {f} for eligible feeder {r.get('feeder_id')}")
            value = float(r[f])
            if not math.isfinite(value):
                raise ValueError(f"non-finite {f} for eligible feeder {r.get('feeder_id')}")

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
    ap.add_argument("--features", required=True, help="CSV generated by extract_feeder_features.py")
    ap.add_argument("--feature-audit", required=True, help="matching audit JSON generated with the feature CSV")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    feature_path = Path(args.features)
    with feature_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    audit = json.loads(Path(args.feature_audit).read_text(encoding="utf-8"))

    validate_rows(rows)
    validate_feature_audit(rows, audit, feature_path)
    result = select(rows)
    result["feature_csv_sha256"] = sha256(feature_path)
    result["feature_audit_path"] = str(args.feature_audit)
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
