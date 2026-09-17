from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREDICATES = ("C_geo", "C_road", "C_interface", "C_hazard", "C_computable")
FEATURES = ("N_P", "N_T", "N_I", "P_max", "L_T", "R_T", "E_H")
FIELDS = ("feeder_id",) + PREDICATES + FEATURES


def _write_matrix(path: Path, eligible: int = 2) -> list[str]:
    ids = [f"F{i:02d}" for i in range(61)]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for i, fid in enumerate(ids):
            ok = i < eligible
            row = {"feeder_id": fid}
            for p in PREDICATES:
                row[p] = "TRUE" if ok else "FALSE"
            for j, feature in enumerate(FEATURES):
                row[feature] = str(float(i + j + 1)) if ok else ""
            w.writerow(row)
    return ids


def _write_extraction_audit(path: Path, ids: list[str], eligible: int = 2, missing_hazard: str | None = None) -> None:
    eligible_ids = ids[:eligible]
    feeders = {}
    for fid in ids:
        feeders[fid] = {
            "hazard_exposure": (
                {"status": "MISSING_NOT_ZERO"}
                if fid == missing_hazard
                else {
                    "e_P": "0.1",
                    "e_T": "0.2",
                    "E_H": "0.15",
                    "coverage_status": "EVALUATED",
                    "source_ref": "synthetic-test-fixture",
                }
            )
        }
    doc = {
        "specification": "FEEDER_FEATURE_SPECIFICATION_V1.md",
        "upstream_commit": "6aff1cac48869ccfa0183643979f5f04b04e1124",
        "source_gates": {"database": {"ok": True}, "sumo": {"ok": True}},
        "feeder_count": 61,
        "hazard_table_supplied": True,
        "eligible_count": eligible,
        "eligible_feeders": eligible_ids,
        "feeders": feeders,
    }
    path.write_text(json.dumps(doc), encoding="utf-8")


def test_qualification_blocks_missing_hazard_determination(tmp_path: Path):
    matrix = tmp_path / "features.csv"
    ids = _write_matrix(matrix)
    extraction = tmp_path / "extraction.json"
    _write_extraction_audit(extraction, ids, missing_hazard=ids[-1])
    out = tmp_path / "qualification.json"

    p = subprocess.run(
        [sys.executable, str(ROOT / "qualify_feeder_features.py"), "--features", str(matrix), "--extraction-audit", str(extraction), "--out", str(out)],
        check=False,
    )
    assert p.returncode == 2
    result = json.loads(out.read_text())
    assert result["selection_authorized"] is False
    assert ids[-1] in result["missing_hazard_determinations"]


def test_qualified_hash_chain_and_tamper_rejection(tmp_path: Path):
    matrix = tmp_path / "features.csv"
    ids = _write_matrix(matrix)
    extraction = tmp_path / "extraction.json"
    _write_extraction_audit(extraction, ids)
    qualification = tmp_path / "qualification.json"

    subprocess.run(
        [sys.executable, str(ROOT / "qualify_feeder_features.py"), "--features", str(matrix), "--extraction-audit", str(extraction), "--out", str(qualification)],
        check=True,
    )
    q = json.loads(qualification.read_text())
    assert q["selection_authorized"] is True
    expected_sha = hashlib.sha256(matrix.read_bytes()).hexdigest()
    assert q["feature_csv_sha256"] == expected_sha

    selection = tmp_path / "selection.json"
    subprocess.run(
        [sys.executable, str(ROOT / "select_feeders.py"), "--features", str(matrix), "--feature-audit", str(qualification), "--out", str(selection)],
        check=True,
    )
    s = json.loads(selection.read_text())
    assert s["outcome_blind"] is True
    assert s["development_feeder_id"] != s["heldout_feeder_id"]

    # Any post-qualification edit must invalidate the authorized matrix.
    matrix.write_text(matrix.read_text() + "\n", encoding="utf-8")
    p = subprocess.run(
        [sys.executable, str(ROOT / "select_feeders.py"), "--features", str(matrix), "--feature-audit", str(qualification), "--out", str(tmp_path / "tampered.json")],
        check=False,
    )
    assert p.returncode != 0
