import json
from pathlib import Path

import pytest

from methods.austin_case.admissibility import AustinAdmissibilityError, validate_contract

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "austin_case_admissibility_v3.json"


def contract():
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def family(data, item_id):
    return next(row for row in data["required_data_families"] if row["id"] == item_id)


def derived(data, item_id):
    return next(row for row in data["derived_objects"] if row["id"] == item_id)


def test_repository_v3_contract_is_valid_but_open():
    data = contract()
    validate_contract(data)
    assert data["version"] == "3.0"
    assert data["final_case_admissibility"] is False
    assert data["temporal_evidence"]["G_time"] == "OPEN"


def test_v3_rejects_current_signal_layer_as_historical_truth():
    data = contract()
    family(data, "signals")["temporal_role"] = "EXACT_2018"
    with pytest.raises(AustinAdmissibilityError, match="current non-versioned"):
        validate_contract(data)


def test_v3_rejects_complete_2018_signal_inventory_claim():
    data = contract()
    derived(data, "traffic_signals_retrospective_2018")["complete_2018_inventory"] = True
    with pytest.raises(AustinAdmissibilityError, match="cannot claim complete 2018 inventory"):
        validate_contract(data)


def test_v3_rejects_dynamic_event_truth_from_static_floodplain():
    data = contract()
    family(data, "flood")["historical_2018_event_truth"] = True
    with pytest.raises(AustinAdmissibilityError, match="cannot claim historical 2018 event truth"):
        validate_contract(data)


def test_v3_rejects_radar_window_drift():
    data = contract()
    family(data, "traffic_radar")["confirmatory_candidate_window"] = "2020"
    with pytest.raises(AustinAdmissibilityError, match="calendar-year 2018"):
        validate_contract(data)


def test_v3_final_admissibility_rejects_open_temporal_gate():
    data = contract()
    data["final_case_admissibility"] = True
    data["status"] = "ADMISSIBLE_FROZEN"
    data["selection"]["candidate_is_frozen"] = True
    for gate in data["gates"]:
        data["gates"][gate] = "PASS"

    for item_id in ("boundary", "power", "road", "signals", "flood"):
        family(data, item_id)["spatial_overlap_verified"] = True
    family(data, "power")["raw_materialized"] = True
    family(data, "road")["network_qa_pass"] = True
    family(data, "signals")["synthetic_power_mapping_verified"] = True
    family(data, "traffic_radar")["spatial_overlap_verified"] = True
    family(data, "traffic_radar")["chronological_or_event_split_frozen"] = True
    family(data, "radar_sensor_locations")["2018_observation_join_verified"] = True

    derived(data, "traffic_signals_retrospective_2018")["computable"] = True
    derived(data, "repair_access")["computable"] = True
    derived(data, "p_to_t_signal_power_mapping")["computable"] = True

    data["temporal_evidence"]["signal_retrospective_extraction"] = "PASS"
    data["temporal_evidence"]["radar_2018_observation_join"] = "PASS"
    data["temporal_evidence"]["flood_asset_intersection"] = "PASS"
    data["temporal_evidence"]["G_time"] = "OPEN"

    with pytest.raises(AustinAdmissibilityError, match="G_time PASS"):
        validate_contract(data)
