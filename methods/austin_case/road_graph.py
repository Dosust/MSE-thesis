"""Road-graph and repair-access QA for the Austin case.

The default graph uses City centerline geometry and geodesic distance only.
Travel time is not fabricated from distance: a speed/travel-time field or a
separately calibrated traffic model must be supplied before time-based H1/H3 use.
"""
from __future__ import annotations

from math import isfinite
from typing import Any, Mapping, Sequence

import networkx as nx
from pyproj import Geod
from shapely.geometry import shape

WGS84 = Geod(ellps="WGS84")


class RoadGraphError(ValueError):
    pass


def _node(coord: Sequence[float]) -> tuple[float, float]:
    if len(coord) < 2:
        raise RoadGraphError("road coordinate requires lon/lat")
    lon, lat = float(coord[0]), float(coord[1])
    if not (-180 <= lon <= 180 and -90 <= lat <= 90):
        raise RoadGraphError("road coordinate outside WGS84 bounds")
    return (lon, lat)


def geodesic_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    _, _, distance = WGS84.inv(a[0], a[1], b[0], b[1])
    if not isfinite(distance) or distance < 0:
        raise RoadGraphError("invalid geodesic edge length")
    return float(distance)


def build_distance_graph(roads_fc: Mapping[str, Any]) -> nx.Graph:
    """Build exact-coordinate undirected graph for structural routing QA.

    A directed/one-way travel graph is a later model gate because the exact City
    attribute mapping must be inspected from raw source fields first.
    """
    features = roads_fc.get("features")
    if not isinstance(features, list):
        raise RoadGraphError("GeoJSON FeatureCollection required")
    graph = nx.Graph()
    rejected = 0
    for index, feature in enumerate(features):
        if not isinstance(feature, Mapping) or feature.get("geometry") is None:
            rejected += 1
            continue
        geom = shape(feature["geometry"])
        if geom.is_empty or not geom.is_valid:
            raise RoadGraphError(f"invalid road geometry at feature {index}")
        lines = [geom] if geom.geom_type == "LineString" else list(geom.geoms) if geom.geom_type == "MultiLineString" else []
        if not lines:
            raise RoadGraphError(f"non-line road geometry at feature {index}")
        for line in lines:
            coords = list(line.coords)
            for left, right in zip(coords, coords[1:]):
                u, v = _node(left), _node(right)
                if u == v:
                    continue
                length_m = geodesic_m(u, v)
                if length_m <= 0:
                    continue
                if graph.has_edge(u, v):
                    if length_m < graph[u][v]["length_m"]:
                        graph[u][v]["length_m"] = length_m
                else:
                    graph.add_edge(u, v, length_m=length_m, source_feature=index)
    if graph.number_of_edges() == 0:
        raise RoadGraphError("road graph contains no usable edge")
    graph.graph["rejected_null_features"] = rejected
    graph.graph["weight_semantics"] = "GEODESIC_DISTANCE_ONLY"
    return graph


def nearest_node(graph: nx.Graph, lon: float, lat: float, max_distance_m: float) -> tuple[tuple[float, float], float]:
    if max_distance_m <= 0 or not isfinite(float(max_distance_m)):
        raise RoadGraphError("max_distance_m must be positive and finite")
    query = _node((lon, lat))
    best = min(
        ((node, geodesic_m(query, node)) for node in graph.nodes),
        key=lambda item: item[1],
    )
    if best[1] > max_distance_m:
        raise RoadGraphError(
            f"nearest road node is {best[1]:.3f} m away, exceeding declared snap tolerance"
        )
    return best


def repair_route(
    graph: nx.Graph,
    origin_lonlat: tuple[float, float],
    target_lonlat: tuple[float, float],
    max_snap_distance_m: float,
) -> dict[str, Any]:
    origin, d_origin = nearest_node(graph, *origin_lonlat, max_snap_distance_m)
    target, d_target = nearest_node(graph, *target_lonlat, max_snap_distance_m)
    if not nx.has_path(graph, origin, target):
        raise RoadGraphError("no routable road path between repair origin and target")
    path = nx.shortest_path(graph, origin, target, weight="length_m")
    length_m = float(nx.shortest_path_length(graph, origin, target, weight="length_m"))
    return {
        "origin_node": origin,
        "target_node": target,
        "origin_snap_m": d_origin,
        "target_snap_m": d_target,
        "path": path,
        "road_distance_m": length_m,
        "travel_time": "NOT_COMPUTED_UNTIL_TRAFFIC_MODEL_QUALIFIED",
    }


def routing_gate(
    graph: nx.Graph,
    origins: Mapping[str, tuple[float, float]],
    targets: Mapping[str, tuple[float, float]],
    max_snap_distance_m: float,
) -> dict[str, Any]:
    if not origins or not targets:
        raise RoadGraphError("at least one repair origin and target are required")
    results: dict[str, Any] = {}
    failures: dict[str, str] = {}
    for target_id, target in targets.items():
        target_routes = []
        for origin_id, origin in origins.items():
            try:
                route = repair_route(graph, origin, target, max_snap_distance_m)
                target_routes.append((origin_id, route))
            except RoadGraphError as exc:
                failures[f"{origin_id}->{target_id}"] = str(exc)
        if not target_routes:
            raise RoadGraphError(f"repair target {target_id} has no feasible route from any declared origin")
        origin_id, route = min(target_routes, key=lambda item: item[1]["road_distance_m"])
        results[target_id] = {"selected_origin": origin_id, **route}
    return {
        "targets": results,
        "nonselected_or_failed_routes": failures,
        "all_targets_reachable": len(results) == len(targets),
        "scope": "STRUCTURAL_DISTANCE_ROUTING_ONLY_NOT_REPAIR_TIME_MODEL",
    }
