import hashlib
import json
from pathlib import Path

import methods.austin_case.resolve_travel_sensor_schema as resolver
from methods.austin_case.travel_sensor_schema import SCHEMA_METADATA_ENDPOINT


def _template(path: Path):
    data = {
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
    path.write_text(json.dumps(data), encoding="utf-8")


def _case(root: Path, sensor_rows):
    sensor_path = root / "raw" / "traffic" / "radar_sensor_locations.json"
    sensor_path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(sensor_rows).encode("utf-8")
    sensor_path.write_bytes(payload)
    qa = root / "qa"
    qa.mkdir(parents=True, exist_ok=True)
    core = {
        "case_id": "AUS-P5U-2018-V1",
        "objects": {
            "radar_sensor_locations": {
                "path": str(sensor_path),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "source_url": "https://data.austintexas.gov/resource/6yd9-yz29.json",
            }
        },
    }
    prejoin = {
        "case_id": "AUS-P5U-2018-V1",
        "radar_inventory": {
            "sensor_ids": [7, 42],
            "sensor_count": 2,
            "observation_count": 180,
            "temporal_role": "HISTORICAL_2018_OBSERVATION",
        },
    }
    (qa / "raw_materialization_manifest_v4.json").write_text(json.dumps(core), encoding="utf-8")
    (qa / "radar_2018_prejoin_manifest.json").write_text(json.dumps(prejoin), encoding="utf-8")


def metadata_payload():
    return json.dumps(
        [
            {"name": "KITS ID", "fieldName": "kits_id", "dataTypeName": "number"},
            {"name": "Latitude", "fieldName": "latitude", "dataTypeName": "number"},
            {"name": "Longitude", "fieldName": "longitude", "dataTypeName": "number"},
        ]
    ).encode("utf-8")


def test_runtime_resolution_freezes_schema_and_join_but_not_g4(monkeypatch, tmp_path):
    _case(
        tmp_path,
        [
            {"kits_id": "7", "latitude": "30.25", "longitude": "-97.75"},
            {"kits_id": "42", "latitude": "30.30", "longitude": "-97.70"},
        ],
    )
    template_path = tmp_path / "template.json"
    _template(template_path)
    monkeypatch.setattr(resolver.base, "fetch", lambda url: metadata_payload())

    result = resolver.resolve(tmp_path, template_path)
    assert result["schema_status"] == "FROZEN"
    assert result["state"] == "SCHEMA_FROZEN_2018_JOIN_PASS_ROAD_OVERLAP_OPEN"
    assert result["road_overlap_verified"] is False
    assert result["G4_traffic_observations"] == "OPEN"
    runtime = json.loads(Path(result["runtime_schema_path"]).read_text())
    assert runtime["field_mapping"]["kits_id_key"] == "kits_id"
    assert runtime["verification"]["at_least_one_2018_radar_join"] is True
    assert Path(result["radar_location_join_path"]).exists()


def test_runtime_resolution_remains_open_on_unresolved_official_metadata(monkeypatch, tmp_path):
    _case(tmp_path, [{"unknown": "7"}])
    template_path = tmp_path / "template.json"
    _template(template_path)
    payload = json.dumps(
        [{"name": "Unknown ID", "fieldName": "unknown", "dataTypeName": "number"}]
    ).encode("utf-8")
    monkeypatch.setattr(resolver.base, "fetch", lambda url: payload)

    result = resolver.resolve(tmp_path, template_path)
    assert result["schema_status"] == "OPEN"
    assert result["state"] == "SCHEMA_OPEN_UNRESOLVED_G4_OPEN"
    assert result["radar_location_join_path"] is None
    assert result["G4_traffic_observations"] == "OPEN"
