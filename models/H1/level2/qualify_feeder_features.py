#!/usr/bin/env python3
"""Qualify an extracted Level-2 feeder feature matrix for outcome-blind selection.

This step cryptographically binds the CSV produced by extract_feeder_features.py
to its extraction audit. It does not compute features and it does not select a
feeder. Its only role is to decide whether the frozen selection algorithm is
allowed to read the matrix.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

PREDICATES = ("C_geo", "C_road", "C_interface", "C_hazard", "C_computable")
FEATURES = ("N_P", "N_T", "N_I", "P_max", "L_T", "R_T", "E_H")
EXPECTED_SPEC = "FEEDER_FEATURE_SPECIFICATION_V1.md"
EXPECTED_COMMIT = "6aff1cac48869ccfa0183643979f5f04b04e1124"
EXPECTED_FEEDER_COUNT = 61


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def as_bool(x: object) -> bool:
    return str(x).strip().lower() in {"1", "true", "yes", "y", "pass"}


def finite(x: object) -> bool:
    try:
        return math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def main() -> None:
    ap = argparse.ArgumentParser(description="Authorize or block the frozen feeder selection matrix")
    ap.add_argument("--features", required=True)
    ap.add_argument("--extraction-audit", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    feature_path = Path(args.features)
    audit_path = Path(args.extraction_audit)
    with feature_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    extraction = json.loads(audit_path.read_text(encoding="utf-8"))

    reasons: list[str] = []
    ids = [str(r.get("feeder_id", "")).strip() for r in rows]
    required_cols = {"feeder_id", *PREDICATES, *FEATURES}
    cols = set(rows[0].keys()) if rows else set()

    if not rows:
        reasons.append("feature CSV is empty")
    if not required_cols.issubset(cols):
        reasons.append(f"feature CSV missing required columns: {sorted(required_cols - cols)}")
    if len(rows) != EXPECTED_FEEDER_COUNT:
        reasons.append(f"expected {EXPECTED_FEEDER_COUNT} feeder rows, found {len(rows)}")
    if any(not x for x in ids) or len(ids) != len(set(ids)):
        reasons.append("feeder IDs are empty or duplicated")

    if extraction.get("specification") != EXPECTED_SPEC:
        reasons.append("extraction audit does not cite the frozen feature specification")
    if extraction.get("upstream_commit") != EXPECTED_COMMIT:
        reasons.append("extraction audit does not use the frozen GreenEVT commit")
    if int(extraction.get("feeder_count", -1)) != len(rows):
        reasons.append("extraction audit feeder_count does not match the CSV")

    source = extraction.get("source_gates", {})
    if not bool(source.get("database", {}).get("ok")):
        reasons.append("frozen UDS database gate did not pass")
    if not bool(source.get("sumo", {}).get("ok")):
        reasons.append("frozen SUMO topology gate did not pass")
    if extraction.get("hazard_table_supplied") is not True:
        reasons.append("qualified FEMA-NFHL exposure table was not supplied")

    # Missing hazard rows cannot silently remove candidate feeders from the
    # selection population. All 61 source feeders need an explicit coverage
    # determination, even if some are subsequently declared C_hazard=FALSE.
    feeder_audits = extraction.get("feeders", {})
    if set(feeder_audits) != set(ids):
        reasons.append("extraction-audit feeder keys do not exactly match the feature CSV")
    missing_hazard_determinations = []
    for fid in ids:
        hz = feeder_audits.get(fid, {}).get("hazard_exposure", {})
        if not hz or hz.get("status") == "MISSING_NOT_ZERO":
            missing_hazard_determinations.append(fid)
    if missing_hazard_determinations:
        reasons.append(
            f"{len(missing_hazard_determinations)} feeder(s) lack an explicit FEMA-NFHL coverage determination"
        )

    evaluated_rows = 0
    eligible: list[str] = []
    row_errors: dict[str, list[str]] = {}
    for r in rows:
        fid = str(r.get("feeder_id", "")).strip() or "<missing>"
        errs: list[str] = []
        pred_raw = [str(r.get(p, "")).strip() for p in PREDICATES]
        if any(x == "" for x in pred_raw):
            errs.append("one or more eligibility predicates are unevaluated")
        else:
            evaluated_rows += 1
        if all(as_bool(r.get(p)) for p in PREDICATES):
            bad = [f for f in FEATURES if not finite(r.get(f))]
            if bad:
                errs.append(f"eligible row has missing/non-finite features: {bad}")
            else:
                eligible.append(fid)
        if errs:
            row_errors[fid] = errs

    if evaluated_rows != len(rows):
        reasons.append("not every feeder has an explicit eligibility determination")
    if row_errors:
        reasons.append("one or more feeder rows fail matrix consistency checks")
    if len(eligible) < 2:
        reasons.append("fewer than two fully eligible feeders remain for development/held-out selection")

    extraction_eligible = sorted(str(x) for x in extraction.get("eligible_feeders", []))
    if sorted(eligible) != extraction_eligible:
        reasons.append("eligible set in CSV differs from extraction audit")
    if int(extraction.get("eligible_count", -1)) != len(eligible):
        reasons.append("eligible count in CSV differs from extraction audit")

    authorized = len(reasons) == 0
    result = {
        "specification": EXPECTED_SPEC,
        "upstream_commit": EXPECTED_COMMIT,
        "feeder_count": len(rows),
        "eligible_count": len(eligible),
        "eligible_feeders": sorted(eligible),
        "feature_csv_sha256": sha256(feature_path),
        "extraction_audit_sha256": sha256(audit_path),
        "source_feature_csv": str(feature_path),
        "source_extraction_audit": str(audit_path),
        "selection_authorized": authorized,
        "status": "QUALIFIED_FOR_OUTCOME_BLIND_SELECTION" if authorized else "BLOCKED",
        "block_reasons": reasons,
        "row_errors": row_errors,
        "missing_hazard_determinations": missing_hazard_determinations,
        "claim_boundary": "Qualification authorizes only the preregistered feeder selector. It does not authorize M0/M1/M2 execution or H1 claims.",
    }
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if authorized else 2)


if __name__ == "__main__":
    main()
