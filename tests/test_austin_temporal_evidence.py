from datetime import datetime, timezone

import pytest

from methods.austin_case.temporal_evidence import (
    AustinTemporalEvidenceError,
    flood_semantics_summary,
    retrospective_signal_subset,
    validate_flood_summary,
    validate_signal_summary,
)


def feature(turn_on_date=None, *, flood_zone=None, effective_date=None):
    props = {}
    if turn_on_date is not None:
        props["TURN_ON_DATE"] = turn_on_date
    if flood_zone is not None:
        props["FLOOD_ZONE"] = flood_zone
    if effective_date is not None:
        props["EFFECTIVE_DATE"] = effective_date
    return {"type": "Feature", "properties": props, "geometry": None}


def test_signal_subset_accepts_pre2019_epoch_and_iso_dates():
    fc = {
        "type": "FeatureCollection",
        "features": [
            feature(1546214400000),  # 2018-12-31 UTC
            feature("2018-01-15T12:00:00Z"),
            feature("2020-01-01T00:00:00Z"),
        ],
    }
    subset, summary = retrospective_signal_subset(fc)
    assert len(subset["features"]) == 2
    assert summary["retained_feature_count"] == 2
    assert summary["post_2018_turn_on_date"] == 1
    validate_signal_summary(summary)


def test_signal_subset_excludes_missing_and_invalid_dates_fail_closed():
    fc = {
        "type": "FeatureCollection",
        "features": [feature(), feature("not-a-date"), feature("2017-06-01")],
    }
    subset, summary = retrospective_signal_subset(fc)
    assert len(subset["features"]) == 1
    assert summary["missing_turn_on_date"] == 1
    assert summary["invalid_turn_on_date"] == 1


def test_signal_summary_cannot_claim_complete_2018_inventory():
    _, summary = retrospective_signal_subset(
        {"type": "FeatureCollection", "features": [feature("2018-01-01")]}
    )
    summary["complete_2018_inventory"] = True
    with pytest.raises(AustinTemporalEvidenceError):
        validate_signal_summary(summary)


def test_flood_layer_is_static_scenario_support_only():
    fc = {
        "type": "FeatureCollection",
        "features": [
            feature(flood_zone="AE", effective_date=1514764800000),
            feature(flood_zone="X"),
        ],
    }
    summary = flood_semantics_summary(fc)
    assert summary["temporal_role"] == "STATIC_SCENARIO_SUPPORT"
    assert summary["event_time_depth_available"] is False
    assert summary["missing_effective_date"] == 1
    validate_flood_summary(summary)


def test_flood_summary_cannot_be_reinterpreted_as_dynamic_event_truth():
    summary = flood_semantics_summary(
        {"type": "FeatureCollection", "features": [feature(flood_zone="AE")]}
    )
    summary["historical_2018_event_truth"] = True
    with pytest.raises(AustinTemporalEvidenceError):
        validate_flood_summary(summary)
