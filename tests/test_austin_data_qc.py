from __future__ import annotations

import pytest

from methods.austin_case.data_qc import AustinDataQCError, validate_raw_manifest

SHA = "a" * 64


def arc_record(name: str):
    return {
        "path": "raw/" + name + ".geojson",
        "bytes": 100,
        "sha256": SHA,
        "source_url": "https://example.org/" + name,
        "object_id_count": 2,
        "feature_count": 2,
        "page_count": 1,
        "pages": [{"sha256": SHA, "requested_ids": [1, 2], "feature_count": 2}],
    }


def manifest():
    return {
        "case_id": "AUS-P5U-2018-V1",
        "status": "RAW_MATERIALIZATION_ONLY",
        "objects": {
            "smartds_listing": {"path": "raw/list.xml", "bytes": 20, "sha256": SHA, "source_url": "https://example.org/list"},
            "smartds_buscoords": {"path": "raw/Buscoords.dss", "bytes": 30, "sha256": SHA, "source_url": "https://example.org/bus", "plausible_lonlat_rows": 3, "bbox_wgs84": [-97.8, 30.2, -97.7, 30.3]},
            "austin_full_purpose": arc_record("boundary"),
            "street_centerline": arc_record("roads"),
            "traffic_signals": arc_record("signals"),
            "fema_floodplain": arc_record("flood"),
            "camera_detector_locations": {"path": "raw/camera.json", "bytes": 10, "sha256": SHA, "source_url": "https://example.org/camera", "row_count": 2},
            "radar_sensor_locations": {"path": "raw/radar.json", "bytes": 10, "sha256": SHA, "source_url": "https://example.org/radar", "row_count": 2},
        },
    }


def test_valid_manifest_passes_raw_qc_only():
    result = validate_raw_manifest(manifest())
    assert result["raw_integrity"] == "PASS"
    assert result["scientific_scope"] == "RAW_QC_ONLY_NOT_CASE_ADMISSIBILITY"


def test_missing_object_is_rejected():
    data = manifest()
    del data["objects"]["traffic_signals"]
    with pytest.raises(AustinDataQCError, match="missing required raw objects"):
        validate_raw_manifest(data)


def test_arcgis_truncation_is_rejected():
    data = manifest()
    data["objects"]["street_centerline"]["feature_count"] = 1
    with pytest.raises(AustinDataQCError, match="must equal object-ID count"):
        validate_raw_manifest(data)


def test_duplicate_paginated_ids_are_rejected():
    data = manifest()
    data["objects"]["street_centerline"]["pages"][0]["requested_ids"] = [1, 1]
    with pytest.raises(AustinDataQCError, match="duplicate paginated object IDs"):
        validate_raw_manifest(data)


def test_invalid_power_bbox_is_rejected():
    data = manifest()
    data["objects"]["smartds_buscoords"]["bbox_wgs84"] = [-97.7, 30.3, -97.8, 30.2]
    with pytest.raises(AustinDataQCError, match="bbox invalid"):
        validate_raw_manifest(data)


def test_empty_traffic_locations_are_rejected():
    data = manifest()
    data["objects"]["camera_detector_locations"]["row_count"] = 0
    data["objects"]["radar_sensor_locations"]["row_count"] = 0
    with pytest.raises(AustinDataQCError, match="traffic-location table"):
        validate_raw_manifest(data)
