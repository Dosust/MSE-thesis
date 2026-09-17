from __future__ import annotations

import pytest

from methods.austin_case.signal_power_mapping import (
    SignalMappingError,
    map_signals_to_power,
)


def signals(rows):
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"id": sid},
                "geometry": {"type": "Point", "coordinates": [lon, lat]},
            }
            for sid, lon, lat in rows
        ],
    }


def test_near_signal_maps_and_semantics_are_explicit():
    result = map_signals_to_power(
        signals([("s1", -97.7501, 30.25)]),
        [("p1", -97.75, 30.25)],
        max_distance_m=50.0,
        id_field="id",
    )
    assert result["mapped_count"] == 1
    assert result["rejected_count"] == 0
    assert result["mapped"][0]["observed_feeder_assignment"] is False
    assert "NOT_OBSERVED_UTILITY_FEEDER" in result["semantics"]


def test_far_signal_is_rejected_not_forced_to_power_node():
    result = map_signals_to_power(
        signals([("s1", -97.80, 30.25)]),
        [("p1", -97.75, 30.25)],
        max_distance_m=100.0,
        id_field="id",
    )
    assert result["mapped_count"] == 0
    assert result["rejected_count"] == 1


def test_duplicate_signal_ids_fail_closed():
    data = signals([
        ("s1", -97.7501, 30.25),
        ("s1", -97.7502, 30.25),
    ])
    with pytest.raises(SignalMappingError, match="duplicate signal"):
        map_signals_to_power(data, [("p1", -97.75, 30.25)], 100.0, id_field="id")


def test_duplicate_power_ids_fail_closed():
    with pytest.raises(SignalMappingError, match="duplicate power"):
        map_signals_to_power(
            signals([("s1", -97.7501, 30.25)]),
            [("p1", -97.75, 30.25), ("p1", -97.74, 30.25)],
            100.0,
            id_field="id",
        )


def test_mapping_tolerance_must_be_declared_positive():
    with pytest.raises(SignalMappingError, match="positive and finite"):
        map_signals_to_power(
            signals([("s1", -97.7501, 30.25)]),
            [("p1", -97.75, 30.25)],
            0.0,
            id_field="id",
        )
