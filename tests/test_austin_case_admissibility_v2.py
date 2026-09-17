import json
from pathlib import Path

import pytest

from methods.austin_case.admissibility import AustinAdmissibilityError, validate_contract

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "austin_case_admissibility_v2.json"


def contract():
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def test_repository_v2_contract_is_valid_but_open():
    data = contract()
    validate_contract(data)
    assert data["version"] == "2.0"
    assert data["final_case_admissibility"] is False
    assert data["gates"]["G3_transport_topology"] != "PASS"


def test_v2_rejects_primary_road_source_drift():
    data = contract()
    road = next(row for row in data["required_data_families"] if row["id"] == "road")
    road["endpoint"] = "https://example.invalid/current-road"
    with pytest.raises(AustinAdmissibilityError, match="TxDOT Roadway Inventory 2018"):
        validate_contract(data)


def test_v2_rejects_wrong_primary_inventory_year():
    data = contract()
    road = next(row for row in data["required_data_families"] if row["id"] == "road")
    road["inventory_year"] = 2019
    with pytest.raises(AustinAdmissibilityError, match="year must remain 2018"):
        validate_contract(data)


def test_v2_rejects_live_ctn_labeled_as_2018_snapshot():
    data = contract()
    ctn = next(
        row for row in data["required_data_families"] if row["id"] == "road_ctn_sensitivity"
    )
    ctn["strict_2018_snapshot"] = True
    with pytest.raises(AustinAdmissibilityError, match="must not be labeled"):
        validate_contract(data)
