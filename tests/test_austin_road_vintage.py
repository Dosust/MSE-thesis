from copy import deepcopy

import pytest

from methods.austin_case.road_vintage import (
    AUSTIN_CTN_LAYER,
    ROAD_VERSION,
    TXDOT_2018_LAYER,
    AustinRoadVintageError,
    validate_road_vintage_manifest,
)


def valid_manifest():
    primary = {
        "source_url": TXDOT_2018_LAYER,
        "inventory_year": 2018,
        "road_role": "PRIMARY_EXACT_2018_ANNUAL_INVENTORY",
        "strict_2018_snapshot": True,
        "feature_count": 2,
        "object_id_count": 2,
    }
    ctn = {
        "source_url": AUSTIN_CTN_LAYER,
        "road_role": "CURRENT_SEMANTIC_TOPOLOGY_SENSITIVITY",
        "strict_2018_snapshot": False,
    }
    current = {
        "road_role": "CURRENT_GEOMETRY_SENSITIVITY",
        "strict_2018_snapshot": False,
    }
    return {
        "case_id": "AUS-P5U-2018-V1",
        "road_version": ROAD_VERSION,
        "objects": {
            "txdot_roadway_inventory_2018": primary,
            "austin_ctn_current": ctn,
            "street_centerline": current,
        },
    }


def test_valid_2018_primary_and_current_sensitivity_pass():
    result = validate_road_vintage_manifest(valid_manifest())
    assert result["road_source_identity"] == "PASS"
    assert result["primary_inventory_year"] == 2018
    assert result["topology_qa"] == "NOT_EVALUATED_HERE"


def test_live_ctn_cannot_be_labeled_exact_2018():
    manifest = valid_manifest()
    manifest["objects"]["austin_ctn_current"]["strict_2018_snapshot"] = True
    with pytest.raises(AustinRoadVintageError):
        validate_road_vintage_manifest(manifest)


def test_primary_year_cannot_drift_from_2018():
    manifest = valid_manifest()
    manifest["objects"]["txdot_roadway_inventory_2018"]["inventory_year"] = 2019
    with pytest.raises(AustinRoadVintageError):
        validate_road_vintage_manifest(manifest)


def test_primary_source_identity_is_frozen():
    manifest = valid_manifest()
    manifest["objects"]["txdot_roadway_inventory_2018"]["source_url"] = "https://example.invalid/roads"
    with pytest.raises(AustinRoadVintageError):
        validate_road_vintage_manifest(manifest)


def test_nonempty_primary_is_required():
    manifest = deepcopy(valid_manifest())
    manifest["objects"]["txdot_roadway_inventory_2018"]["feature_count"] = 0
    manifest["objects"]["txdot_roadway_inventory_2018"]["object_id_count"] = 0
    with pytest.raises(AustinRoadVintageError):
        validate_road_vintage_manifest(manifest)
