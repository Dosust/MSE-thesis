import json
from pathlib import Path

import methods.austin_case.materialize_public_data_v4 as v4


def _write_fc(path: Path, features):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"type": "FeatureCollection", "features": features}), encoding="utf-8")


def _feature(properties):
    return {"type": "Feature", "properties": properties, "geometry": None}


def test_v4_derives_retrospective_signal_subset_and_preserves_open_temporal_gate(monkeypatch, tmp_path):
    signals_path = tmp_path / "raw" / "gis" / "traffic_signals.geojson"
    flood_path = tmp_path / "raw" / "gis" / "fema_floodplain.geojson"
    radar_path = tmp_path / "raw" / "traffic" / "radar_sensor_locations.json"

    _write_fc(
        signals_path,
        [
            _feature({"TURN_ON_DATE": 1514764800000}),  # 2018-01-01
            _feature({"TURN_ON_DATE": "2020-01-01T00:00:00Z"}),
            _feature({}),
        ],
    )
    _write_fc(
        flood_path,
        [
            _feature({"FLOOD_ZONE": "AE", "EFFECTIVE_DATE": 1514764800000}),
            _feature({"FLOOD_ZONE": "X"}),
        ],
    )
    radar_path.parent.mkdir(parents=True, exist_ok=True)
    radar_path.write_text("[]", encoding="utf-8")

    def fake_v3(root):
        (root / "qa").mkdir(parents=True, exist_ok=True)
        return {
            "case_id": "AUS-P5U-2018-V1",
            "status": "RAW_MATERIALIZATION_ONLY",
            "objects": {
                "traffic_signals": {
                    "path": str(signals_path),
                    "layer": "https://example.test/signals/FeatureServer/0",
                },
                "fema_floodplain": {
                    "path": str(flood_path),
                    "layer": "https://example.test/flood/MapServer/1",
                },
                "radar_sensor_locations": {
                    "path": str(radar_path),
                    "source_url": "https://example.test/radar-locations",
                },
            },
            "scientific_prohibitions": [],
        }

    monkeypatch.setattr(v4.v3, "acquire", fake_v3)
    manifest = v4.acquire(tmp_path)

    derived = manifest["objects"]["traffic_signals_retrospective_2018"]
    derived_path = Path(derived["path"])
    derived_fc = json.loads(derived_path.read_text(encoding="utf-8"))

    assert derived["temporal_role"] == "RETROSPECTIVE_2018_SUBSET"
    assert derived["retained_feature_count"] == 1
    assert len(derived_fc["features"]) == 1
    assert derived["complete_2018_inventory"] is False
    assert derived["survivorship_bias"] is True

    current_signals = manifest["objects"]["traffic_signals"]
    assert current_signals["temporal_role"] == "CURRENT_NONVERSIONED_SOURCE"
    assert current_signals["historical_2018_truth"] is False

    flood = manifest["objects"]["fema_floodplain"]
    assert flood["temporal_role"] == "STATIC_SCENARIO_SUPPORT"
    assert flood["event_time_depth_available"] is False
    assert flood["historical_2018_event_truth"] is False

    radar = manifest["objects"]["radar_sensor_locations"]
    assert radar["temporal_role"] == "RETROSPECTIVE_LOCATION_METADATA"
    assert radar["2018_observation_join_verified"] is False

    assert manifest["temporal_gate"]["signal_retrospective_extraction"] == "PASS"
    assert manifest["temporal_gate"]["radar_2018_observation_join"] == "OPEN"
    assert manifest["temporal_gate"]["flood_asset_intersection"] == "OPEN"
    assert manifest["temporal_gate"]["G_time"] == "OPEN"


def test_v4_fails_signal_temporal_extraction_when_no_pre2019_signal_survives(monkeypatch, tmp_path):
    signals_path = tmp_path / "raw" / "gis" / "traffic_signals.geojson"
    flood_path = tmp_path / "raw" / "gis" / "fema_floodplain.geojson"
    radar_path = tmp_path / "raw" / "traffic" / "radar_sensor_locations.json"

    _write_fc(signals_path, [_feature({"TURN_ON_DATE": "2020-01-01T00:00:00Z"})])
    _write_fc(flood_path, [_feature({"FLOOD_ZONE": "AE"})])
    radar_path.parent.mkdir(parents=True, exist_ok=True)
    radar_path.write_text("[]", encoding="utf-8")

    def fake_v3(root):
        (root / "qa").mkdir(parents=True, exist_ok=True)
        return {
            "case_id": "AUS-P5U-2018-V1",
            "status": "RAW_MATERIALIZATION_ONLY",
            "objects": {
                "traffic_signals": {"path": str(signals_path), "layer": "https://example.test/signals"},
                "fema_floodplain": {"path": str(flood_path), "layer": "https://example.test/flood"},
                "radar_sensor_locations": {"path": str(radar_path), "source_url": "https://example.test/radar"},
            },
            "scientific_prohibitions": [],
        }

    monkeypatch.setattr(v4.v3, "acquire", fake_v3)
    manifest = v4.acquire(tmp_path)
    assert manifest["temporal_gate"]["signal_retrospective_extraction"] == "FAIL_EMPTY"
    assert manifest["temporal_gate"]["G_time"] == "OPEN"
