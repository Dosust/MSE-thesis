import json

import pytest

from methods.austin_case.travel_sensor_metadata import (
    TravelSensorMetadataError,
    resolve_mapping_from_metadata,
    resolve_runtime_registry,
)
from methods.austin_case.travel_sensor_schema import SCHEMA_METADATA_ENDPOINT


def template():
    return {
        "version": "1.0",
        "case_id": "AUS-P5U-2018-V1",
        "dataset": {
            "dataset_id": "6yd9-yz29",
            "schema_metadata_endpoint": SCHEMA_METADATA_ENDPOINT,
            "temporal_role": "RETROSPECTIVE_LOCATION_METADATA",
            "exact_2018_snapshot": False,
        },
        "status": "OPEN",
        "metadata_evidence": {"columns_metadata_sha256": None, "column_count": None},
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
            "official_metadata_mapping_unique": False,
            "selected_fields_observed": False,
            "kits_values_valid": False,
            "kits_unique_or_resolution_versioned": False,
            "coordinates_valid": False,
            "at_least_one_2018_radar_join": False,
            "missing_joins_reported": False,
            "road_overlap_verified": False,
        },
    }


def inventory():
    return {
        "sensor_ids": [7, 42],
        "sensor_count": 2,
        "observation_count": 180,
        "temporal_role": "HISTORICAL_2018_OBSERVATION",
    }


def latlon_columns():
    return [
        {"name": "KITS ID", "fieldName": "kits_id", "dataTypeName": "number"},
        {"name": "Latitude", "fieldName": "latitude", "dataTypeName": "number"},
        {"name": "Longitude", "fieldName": "longitude", "dataTypeName": "number"},
        {"name": "Status", "fieldName": "status", "dataTypeName": "text"},
    ]


def test_unique_exact_metadata_mapping_resolves_latlon():
    result = resolve_mapping_from_metadata(
        latlon_columns(), ["kits_id", "latitude", "longitude", "status"]
    )
    assert result["status"] == "RESOLVED_UNIQUE_OFFICIAL_METADATA"
    assert result["field_mapping"]["kits_id_key"] == "kits_id"
    assert result["field_mapping"]["latitude_key"] == "latitude"
    assert result["field_mapping"]["point_key"] is None


def test_metadata_resolver_refuses_guessing_when_kits_label_missing():
    columns = [
        {"name": "Sensor Number", "fieldName": "sensor_number", "dataTypeName": "number"},
        {"name": "Latitude", "fieldName": "latitude", "dataTypeName": "number"},
        {"name": "Longitude", "fieldName": "longitude", "dataTypeName": "number"},
    ]
    result = resolve_mapping_from_metadata(
        columns, ["sensor_number", "latitude", "longitude"]
    )
    assert result["status"] == "OPEN_UNRESOLVED"
    assert result["field_mapping"] is None


def test_metadata_resolver_refuses_ambiguous_coordinate_modes():
    columns = latlon_columns() + [
        {"name": "Location", "fieldName": "location", "dataTypeName": "location"}
    ]
    result = resolve_mapping_from_metadata(
        columns, ["kits_id", "latitude", "longitude", "location", "status"]
    )
    assert result["status"] == "OPEN_UNRESOLVED"


def test_runtime_registry_freezes_only_after_raw_value_and_2018_join_verification():
    columns_payload = json.dumps(latlon_columns()).encode("utf-8")
    sensor_rows = [
        {"kits_id": "7", "latitude": "30.25", "longitude": "-97.75", "status": "retired"},
        {"kits_id": "42", "latitude": "30.30", "longitude": "-97.70", "status": "retired"},
    ]
    registry, join = resolve_runtime_registry(
        template(),
        columns_payload=columns_payload,
        sensor_rows=sensor_rows,
        sensor_raw_sha256="a" * 64,
        inventory_summary=inventory(),
    )
    assert registry["status"] == "FROZEN"
    assert registry["verification"]["official_metadata_mapping_unique"] is True
    assert registry["verification"]["at_least_one_2018_radar_join"] is True
    assert registry["verification"]["road_overlap_verified"] is False
    assert join["matched_sensor_ids"] == [7, 42]
    assert join["spatial_overlap_verified"] is False


def test_runtime_registry_stays_open_when_metadata_is_unresolved():
    columns_payload = json.dumps(
        [{"name": "Unknown ID", "fieldName": "unknown", "dataTypeName": "number"}]
    ).encode("utf-8")
    registry, join = resolve_runtime_registry(
        template(),
        columns_payload=columns_payload,
        sensor_rows=[{"unknown": 7}],
        sensor_raw_sha256="a" * 64,
        inventory_summary=inventory(),
    )
    assert registry["status"] == "OPEN"
    assert registry["runtime_resolution"]["status"] == "OPEN_UNRESOLVED"
    assert join is None


def test_runtime_registry_fails_when_official_mapping_points_to_invalid_raw_values():
    columns_payload = json.dumps(latlon_columns()).encode("utf-8")
    sensor_rows = [
        {"kits_id": "7", "latitude": "not-a-latitude", "longitude": "-97.75", "status": "retired"}
    ]
    with pytest.raises(TravelSensorMetadataError, match="failed raw-value/join verification"):
        resolve_runtime_registry(
            template(),
            columns_payload=columns_payload,
            sensor_rows=sensor_rows,
            sensor_raw_sha256="a" * 64,
            inventory_summary=inventory(),
        )
