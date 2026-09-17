import pytest

from methods.austin_case.radar_2018 import (
    Radar2018Error,
    chronological_blocks,
    index_sensor_locations,
    join_inventory_to_locations,
    validate_inventory_rows,
)


def valid_inventory_rows():
    return [
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


def test_valid_inventory_is_strictly_calendar_2018():
    result = validate_inventory_rows(valid_inventory_rows())
    assert result["year"] == 2018
    assert result["sensor_ids"] == [7, 42]
    assert result["observation_count"] == 180
    assert result["temporal_role"] == "HISTORICAL_2018_OBSERVATION"


def test_inventory_rejects_duplicate_or_non2018_sensor_summary():
    rows = valid_inventory_rows()
    rows.append(dict(rows[0]))
    with pytest.raises(Radar2018Error, match="duplicate grouped KITS ID"):
        validate_inventory_rows(rows)

    rows = valid_inventory_rows()
    rows[0]["t_min"] = "2017-12-31T23:45:00Z"
    with pytest.raises(Radar2018Error, match="outside calendar-year 2018"):
        validate_inventory_rows(rows)


def test_location_schema_must_be_explicit_and_unique():
    rows = [
        {"kits": "7", "lat": "30.25", "lon": "-97.75"},
        {"kits": "42", "lat": "30.30", "lon": "-97.70"},
    ]
    locations = index_sensor_locations(
        rows,
        kits_id_key="kits",
        latitude_key="lat",
        longitude_key="lon",
    )
    assert locations[7] == (-97.75, 30.25)

    with pytest.raises(Radar2018Error, match="location schema"):
        index_sensor_locations(rows, kits_id_key="kits")

    duplicate = rows + [{"kits": "7", "lat": "30.26", "lon": "-97.76"}]
    with pytest.raises(Radar2018Error, match="duplicate Travel Sensors KITS ID"):
        index_sensor_locations(
            duplicate,
            kits_id_key="kits",
            latitude_key="lat",
            longitude_key="lon",
        )


def test_point_object_schema_is_supported_only_when_explicit():
    locations = index_sensor_locations(
        [{"kits": 7, "location": {"coordinates": [-97.75, 30.25]}}],
        kits_id_key="kits",
        point_key="location",
    )
    assert locations == {7: (-97.75, 30.25)}


def test_join_reports_missing_metadata_without_inventing_locations():
    inventory = validate_inventory_rows(valid_inventory_rows())
    result = join_inventory_to_locations(inventory, {7: (-97.75, 30.25)})
    assert result["matched_sensor_ids"] == [7]
    assert result["missing_location_sensor_ids"] == [42]
    assert result["join_fraction"] == 0.5
    assert result["exact_2018_location_snapshot"] is False
    assert result["spatial_overlap_verified"] is False

    with pytest.raises(Radar2018Error, match="no 2018 radar KITS ID joins"):
        join_inventory_to_locations(inventory, {999: (-97.7, 30.3)})


def test_chronological_split_prevents_random_row_leakage():
    rows = [
        {"curdatetime": "2018-01-01T00:00:00Z", "int_id": 7},
        {"curdatetime": "2018-06-30T23:45:00Z", "int_id": 7},
        {"curdatetime": "2018-07-01T00:00:00Z", "int_id": 7},
        {"curdatetime": "2018-12-31T23:45:00Z", "int_id": 42},
    ]
    split = chronological_blocks(rows, split_utc="2018-07-01T00:00:00Z")
    assert len(split["development"]) == 2
    assert len(split["validation"]) == 2
    assert split["random_row_split"] is False
    assert split["external_coupled_H1b_validation"] is False


def test_split_rejects_leakage_or_non2018_rows():
    with pytest.raises(Radar2018Error, match="strictly inside 2018"):
        chronological_blocks(
            [{"curdatetime": "2018-01-01T00:00:00Z"}],
            split_utc="2019-01-01T00:00:00Z",
        )

    with pytest.raises(Radar2018Error, match="non-2018 row"):
        chronological_blocks(
            [
                {"curdatetime": "2017-12-31T23:45:00Z"},
                {"curdatetime": "2018-08-01T00:00:00Z"},
            ],
            split_utc="2018-07-01T00:00:00Z",
        )
