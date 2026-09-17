from __future__ import annotations

import pytest

from methods.austin_case.road_graph import (
    RoadGraphError,
    build_distance_graph,
    repair_route,
    routing_gate,
)


def fc(lines):
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {"type": "LineString", "coordinates": coords},
            }
            for coords in lines
        ],
    }


def test_connected_road_graph_routes_repair_target():
    roads = fc([
        [[-97.75, 30.25], [-97.74, 30.25]],
        [[-97.74, 30.25], [-97.73, 30.25]],
    ])
    graph = build_distance_graph(roads)
    result = repair_route(
        graph,
        (-97.75001, 30.25),
        (-97.72999, 30.25),
        max_snap_distance_m=10.0,
    )
    assert result["road_distance_m"] > 0
    assert result["travel_time"] == "NOT_COMPUTED_UNTIL_TRAFFIC_MODEL_QUALIFIED"


def test_snap_tolerance_fails_closed():
    graph = build_distance_graph(fc([[[-97.75, 30.25], [-97.74, 30.25]]]))
    with pytest.raises(RoadGraphError, match="exceeding declared snap tolerance"):
        repair_route(graph, (-97.80, 30.25), (-97.74, 30.25), 5.0)


def test_disconnected_repair_target_is_rejected():
    graph = build_distance_graph(fc([
        [[-97.75, 30.25], [-97.74, 30.25]],
        [[-97.70, 30.25], [-97.69, 30.25]],
    ]))
    with pytest.raises(RoadGraphError, match="no routable road path"):
        repair_route(graph, (-97.75, 30.25), (-97.69, 30.25), 10.0)


def test_routing_gate_selects_shorter_declared_origin():
    graph = build_distance_graph(fc([
        [[-97.75, 30.25], [-97.74, 30.25]],
        [[-97.74, 30.25], [-97.73, 30.25]],
    ]))
    result = routing_gate(
        graph,
        {"far": (-97.75, 30.25), "near": (-97.74, 30.25)},
        {"asset": (-97.73, 30.25)},
        10.0,
    )
    assert result["targets"]["asset"]["selected_origin"] == "near"
    assert result["all_targets_reachable"] is True


def test_invalid_non_line_geometry_is_rejected():
    data = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature", "properties": {},
            "geometry": {"type": "Point", "coordinates": [-97.75, 30.25]},
        }],
    }
    with pytest.raises(RoadGraphError, match="non-line"):
        build_distance_graph(data)
