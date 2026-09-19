import csv
from pathlib import Path

REGISTRY = (
    Path(__file__).resolve().parents[1]
    / "models"
    / "H1"
    / "level2"
    / "registries"
    / "dependency_registry_v2.csv"
)


def _rows():
    with REGISTRY.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_dependency_ids_are_unique():
    rows = _rows()
    ids = [r["dependency_id"] for r in rows]
    assert len(ids) == len(set(ids))


def test_accepted_m2_requires_both_causal_and_stage23_pass():
    for row in _rows():
        if row["execution_authority"] == "ACCEPTED_M2":
            assert row["g2_status"] == "PASS"
            assert row["stage23_status"] == "PASS"


def test_blocked_dependencies_cannot_be_accepted_m2():
    for row in _rows():
        if row["g2_status"] != "PASS" or row["stage23_status"] != "PASS":
            assert row["execution_authority"] != "ACCEPTED_M2"


def test_role_and_effect_metadata_are_not_blank():
    for row in _rows():
        assert row["role_class"] in {"OPERATION", "RECOVERY", "PLANNING"}
        assert row["effect_class"].strip()
