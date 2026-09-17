import json
from pathlib import Path

import pytest

import methods.austin_case.materialize_radar_inventory as mri


def _write_v4_manifest(root: Path, sensor_rows):
    sensor_path = root / "raw" / "traffic" / "radar_sensor_locations.json"
    sensor_path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(sensor_rows).encode("utf-8")
    sensor_path.write_bytes(payload)
    import hashlib

    manifest = {
        "case_id": "AUS-P5U-2018-V1",
        "objects": {
            "radar_sensor_locations": {
                "path": str(sensor_path),
                "source_url": "https://data.austintexas.gov/resource/6yd9-yz29.json",
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        },
    }
    qa = root / "qa"
    qa.mkdir(parents=True, exist_ok=True)
    (qa / "raw_materialization_manifest_v4.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )


def inventory_payload():
    return json.dumps(
        [
            {
                "int_id": "7",
                "n": "100",
                "t_min": "2018-01-02T00:00:00.000",
                "t_max": "2018-12-30T23:45:00.000",
            },
            {
                "int_id": "42",
                "n": "80",
                "t_min": "2018-03-01T00:00:00Z",
                "t_max": "2018-10-01T00:00:00Z",
            },
        ]
    ).encode("utf-8")


def test_prejoin_materializer_observes_schema_but_does_not_choose_fields(monkeypatch, tmp_path):
    _write_v4_manifest(
        tmp_path,
        [
            {"mystery_id": "7", "geom": {"coordinates": [-97.75, 30.25]}},
            {"mystery_id": "42", "geom": {"coordinates": [-97.70, 30.30]}},
        ],
    )
    monkeypatch.setattr(mri.base, "fetch", lambda url: inventory_payload())

    result = mri.materialize(tmp_path)
    assert result["gates"]["radar_2018_inventory"] == "PASS"
    assert result["gates"]["travel_sensor_raw_schema_observed"] == "PASS"
    assert result["gates"]["travel_sensor_field_mapping"] == "OPEN"
    assert result["gates"]["radar_2018_location_join"] == "OPEN"
    observation = result["travel_sensor_schema_observation"]
    assert observation["observed_keys"] == ["geom", "mystery_id"]
    assert observation["semantic_field_selection"] == "NOT_PERFORMED"
    assert observation["field_mapping_status"] == "OPEN"
    assert (tmp_path / "qa" / "radar_2018_prejoin_manifest.json").exists()


def test_prejoin_requires_v4_core_manifest(tmp_path):
    with pytest.raises(mri.RadarInventoryMaterializationError, match="v4 core"):
        mri.materialize(tmp_path)


def test_prejoin_rejects_nonlist_radar_response(monkeypatch, tmp_path):
    _write_v4_manifest(tmp_path, [{"a": 1}])
    monkeypatch.setattr(mri.base, "fetch", lambda url: b'{"error":"bad"}')
    with pytest.raises(mri.RadarInventoryMaterializationError, match="JSON list"):
        mri.materialize(tmp_path)
