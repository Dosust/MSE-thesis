import copy
import hashlib
import json

import pytest

from methods.austin_case.travel_sensor_schema import (
    TravelSensorSchemaError,
    observe_schema,
    validate_registry,
)


def open_registry():
    return {
        "version": "1.0",
        "case_id": "AUS-P5U-2018-V1",
        "dataset": {
            "dataset_id": "6yd9-yz29",
            "temporal_role": "RETROSPECTIVE_LOCATION_METADATA",
            "exact_2018_snapshot": False,
        },
        "status": "OPEN",
        "raw_evidence": {
            "raw_data_sha256": None,
            "raw_row_count": None,
            "observed_keys_sha256": None,
            "observed_keys": [],
        },
        "field_mapping": {
            "kits_id_key": None,
            "point_key": None,
            "latitude_key": None,
            "longitude_key": None,
        },
        "mapping_evidence_basis": None,
        "verification": {
            "selected_fields_observed": False,
            "kits_values_valid": False,
            "kits_unique_or_resolution_versioned": False,
            "coordinates_valid": False,
            "at_least_one_2018_radar_join": False,
            "missing_joins_reported": False,
            "road_overlap_verified": False,
        },
    }


def test_schema_observation_is_descriptive_not_semantic():
    rows = [
        {"alpha": "7", "where": {"coordinates": [-97.7, 30.2]}},
        {"alpha": "42", "where": None, "status": "retired"},
    ]
    observed = observe_schema(rows)
    assert observed["observed_keys"] == ["alpha", "status", "where"]
    assert observed["semantic_field_selection"] == "NOT_PERFORMED"
    assert len(observed["observed_keys_sha256"]) == 64


def test_open_registry_is_valid_only_without_fake_verification():
    reg = open_registry()
    assert validate_registry(reg) == "OPEN"
    reg["verification"]["selected_fields_observed"] = True
    with pytest.raises(TravelSensorSchemaError, match="OPEN schema"):
        validate_registry(reg)


def frozen_registry():
    reg = open_registry()
    keys = ["kits", "lat", "lon", "status"]
    keys_digest = hashlib.sha256(
        json.dumps(keys, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    reg.update({"status": "FROZEN", "mapping_evidence_basis": "raw schema + City semantic relationship"})
    reg["raw_evidence"] = {
        "raw_data_sha256": "a" * 64,
        "raw_row_count": 2,
        "observed_keys_sha256": keys_digest,
        "observed_keys": keys,
    }
    reg["field_mapping"] = {
        "kits_id_key": "kits",
        "point_key": None,
        "latitude_key": "lat",
        "longitude_key": "lon",
    }
    for key in (
        "selected_fields_observed",
        "kits_values_valid",
        "kits_unique_or_resolution_versioned",
        "coordinates_valid",
        "at_least_one_2018_radar_join",
        "missing_joins_reported",
    ):
        reg["verification"][key] = True
    return reg


def test_complete_frozen_mapping_passes_without_requiring_road_overlap():
    reg = frozen_registry()
    assert reg["verification"]["road_overlap_verified"] is False
    assert validate_registry(reg) == "FROZEN"


def test_frozen_mapping_rejects_unobserved_field_name():
    reg = frozen_registry()
    reg["field_mapping"]["kits_id_key"] = "guessed_kits"
    with pytest.raises(TravelSensorSchemaError, match="KITS field must be observed"):
        validate_registry(reg)


def test_frozen_mapping_rejects_ambiguous_coordinate_modes():
    reg = frozen_registry()
    reg["raw_evidence"]["observed_keys"].append("location")
    reg["field_mapping"]["point_key"] = "location"
    with pytest.raises(TravelSensorSchemaError, match="exactly one coordinate mapping mode"):
        validate_registry(reg)


def test_frozen_mapping_rejects_missing_join_verification():
    reg = frozen_registry()
    reg["verification"]["at_least_one_2018_radar_join"] = False
    with pytest.raises(TravelSensorSchemaError, match="at_least_one_2018_radar_join"):
        validate_registry(reg)
