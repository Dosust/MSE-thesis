from __future__ import annotations

import pytest

from methods.austin_case.spatial_qa import (
    SpatialQAError,
    boundary_symmetric_difference_ratio,
    spatial_case_summary,
)


def fc(geometries):
    return {
        "type": "FeatureCollection",
        "features": [
            {"type": "Feature", "properties": {}, "geometry": geom}
            for geom in geometries
        ],
    }


def polygon(x0, y0, x1, y1):
    return {
        "type": "Polygon",
        "coordinates": [[
            [x0, y0], [x1, y0], [x1, y1], [x0, y1], [x0, y0]
        ]],
    }


def line(points):
    return {"type": "LineString", "coordinates": points}


def point(x, y):
    return {"type": "Point", "coordinates": [x, y]}


def test_feature_level_summary_known_geometry():
    primary = fc([polygon(-97.8, 30.2, -97.7, 30.3)])
    current = fc([polygon(-97.81, 30.19, -97.69, 30.31)])
    service = fc([polygon(-97.82, 30.18, -97.68, 30.32)])
    roads = fc([line([[-97.79, 30.21], [-97.71, 30.29]])])
    signals = fc([point(-97.75, 30.25)])
    flood = fc([polygon(-97.76, 30.24, -97.74, 30.26)])
    buses = [("b1", -97.75, 30.25), ("b2", -97.78, 30.28)]
    result = spatial_case_summary(buses, primary, current, service, roads, signals, flood)
    assert result["bus_in_primary"] == 2
    assert result["bus_in_service_area"] == 2
    assert result["bus_in_flood"] == 1
    assert result["road_features_intersect_primary"] == 1
    assert result["road_features_intersect_flood"] == 1
    assert result["signal_features_intersect_primary"] == 1
    assert result["G2_common_spatial_support_candidate"] is True
    assert result["G7_coupled_flood_exposure_candidate"] is True
    assert result["scope"] == "SPATIAL_QA_ONLY_NOT_FINAL_CASE_PASS"


def test_bbox_like_proximity_without_feature_intersection_does_not_pass_flood():
    primary = fc([polygon(-97.8, 30.2, -97.7, 30.3)])
    roads = fc([line([[-97.79, 30.21], [-97.78, 30.22]])])
    signals = fc([point(-97.75, 30.25)])
    flood = fc([polygon(-97.705, 30.295, -97.7001, 30.2999)])
    result = spatial_case_summary(
        [("b1", -97.75, 30.25)], primary, primary, primary, roads, signals, flood
    )
    assert result["G2_common_spatial_support_candidate"] is True
    assert result["G7_coupled_flood_exposure_candidate"] is False


def test_identical_boundaries_have_zero_difference():
    primary = fc([polygon(-97.8, 30.2, -97.7, 30.3)])
    assert boundary_symmetric_difference_ratio(primary, primary) == pytest.approx(0.0, abs=1e-12)


def test_invalid_polygon_is_rejected_without_silent_repair():
    bowtie = {
        "type": "Polygon",
        "coordinates": [[
            [-97.8, 30.2], [-97.7, 30.3], [-97.8, 30.3], [-97.7, 30.2], [-97.8, 30.2]
        ]],
    }
    good = fc([polygon(-97.8, 30.2, -97.7, 30.3)])
    with pytest.raises(SpatialQAError, match="invalid geometry"):
        spatial_case_summary(
            [("b1", -97.75, 30.25)], fc([bowtie]), good, good, good, good, good
        )


def test_invalid_bus_coordinate_is_rejected():
    good = fc([polygon(-97.8, 30.2, -97.7, 30.3)])
    with pytest.raises(SpatialQAError, match="invalid WGS84"):
        spatial_case_summary(
            [("b1", 200.0, 30.25)], good, good, good, good, good, good
        )
