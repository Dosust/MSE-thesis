"""Regression tests for the Austin case-study admissibility contract."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from methods.austin_case.admissibility import (
    AustinAdmissibilityError,
    REQUIRED_GATE_IDS,
    case_is_admissible,
    validate_contract,
)


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "austin_case_admissibility_v1.json"


def _contract():
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def test_repository_contract_is_valid_but_not_yet_admissible():
    data = _contract()
    validate_contract(data)
    assert case_is_admissible(data) is False
    assert data["gates"]["G0_canonical_consistency"] == "PASS"
    assert any(value != "PASS" for value in data["gates"].values())


def test_outcome_based_subregion_selection_is_rejected():
    data = _contract()
    data["selection"]["selection_uses_hypothesis_results"] = True
    with pytest.raises(AustinAdmissibilityError, match="must not use H1-H5 outcomes"):
        validate_contract(data)


def test_final_pass_with_open_gate_is_rejected():
    data = _contract()
    data["final_case_admissibility"] = True
    data["selection"]["candidate_is_frozen"] = True
    with pytest.raises(AustinAdmissibilityError, match="every G0--G8 gate"):
        validate_contract(data)


def test_missing_mandatory_source_is_rejected():
    data = _contract()
    data["required_data_families"] = [
        row for row in data["required_data_families"] if row["id"] != "signals"
    ]
    with pytest.raises(AustinAdmissibilityError, match="mandatory Austin data families"):
        validate_contract(data)


def test_final_pass_requires_full_spatial_network_and_interface_closure():
    data = _contract()
    for gate in REQUIRED_GATE_IDS:
        data["gates"][gate] = "PASS"
    data["selection"]["candidate_is_frozen"] = True
    data["status"] = "ADMISSIBLE_FROZEN"
    data["final_case_admissibility"] = True

    for row in data["required_data_families"]:
        if row["id"] in {"boundary", "power", "road", "signals", "flood"}:
            row["spatial_overlap_verified"] = True
        if row["id"] == "power":
            row["raw_materialized"] = True
        if row["id"] == "road":
            row["network_qa_pass"] = True
        if row["id"] == "signals":
            row["synthetic_power_mapping_verified"] = True

    with pytest.raises(AustinAdmissibilityError, match="traffic-observation"):
        validate_contract(data)

    next(row for row in data["required_data_families"] if row["id"] == "traffic_camera")[
        "spatial_overlap_verified"
    ] = True

    with pytest.raises(AustinAdmissibilityError, match="repair access"):
        validate_contract(data)

    next(row for row in data["derived_objects"] if row["id"] == "repair_access")[
        "computable"
    ] = True

    with pytest.raises(AustinAdmissibilityError, match="signal-power mapping"):
        validate_contract(data)

    next(
        row
        for row in data["derived_objects"]
        if row["id"] == "p_to_t_signal_power_mapping"
    )["computable"] = True

    validate_contract(data)
    assert case_is_admissible(data) is True
