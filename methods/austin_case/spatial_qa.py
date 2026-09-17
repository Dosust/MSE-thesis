"""Feature-level spatial QA for the Austin candidate case.

All input GeoJSON is expected in WGS84 because acquisition requests outSR=4326.
Native CRS identities remain in the acquisition manifests. Area calculations are
performed only after projection to EPSG:2277 (Texas Central, US survey feet).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Sequence

from pyproj import Transformer
from shapely.geometry import Point, shape
from shapely.geometry.base import BaseGeometry
from shapely.ops import transform, unary_union


class SpatialQAError(ValueError):
    pass


@dataclass(frozen=True)
class GeometryAudit:
    feature_count: int
    null_count: int
    invalid_count: int
    empty_count: int


def _geometries(fc: Mapping[str, Any]) -> tuple[list[BaseGeometry], GeometryAudit]:
    features = fc.get("features")
    if not isinstance(features, list):
        raise SpatialQAError("GeoJSON FeatureCollection with features list required")
    geoms: list[BaseGeometry] = []
    null_count = invalid_count = empty_count = 0
    for feature in features:
        if not isinstance(feature, Mapping) or feature.get("geometry") is None:
            null_count += 1
            continue
        geom = shape(feature["geometry"])
        if geom.is_empty:
            empty_count += 1
            continue
        if not geom.is_valid:
            invalid_count += 1
        geoms.append(geom)
    return geoms, GeometryAudit(len(features), null_count, invalid_count, empty_count)


def audited_union(fc: Mapping[str, Any], *, require_valid: bool = True) -> tuple[BaseGeometry, GeometryAudit]:
    geoms, audit = _geometries(fc)
    if not geoms:
        raise SpatialQAError("no usable geometry")
    if require_valid and audit.invalid_count:
        raise SpatialQAError(f"invalid geometry present: {audit.invalid_count}")
    merged = unary_union(geoms)
    if merged.is_empty:
        raise SpatialQAError("union geometry is empty")
    if require_valid and not merged.is_valid:
        raise SpatialQAError("union geometry is invalid")
    return merged, audit


def point_membership(coords: Iterable[tuple[str, float, float]], domain: BaseGeometry) -> tuple[int, tuple[str, ...]]:
    inside: list[str] = []
    for name, lon, lat in coords:
        if not (-180 <= float(lon) <= 180 and -90 <= float(lat) <= 90):
            raise SpatialQAError(f"invalid WGS84 point: {name}")
        if domain.covers(Point(float(lon), float(lat))):
            inside.append(str(name))
    return len(inside), tuple(sorted(inside))


def feature_intersection_count(fc: Mapping[str, Any], domain: BaseGeometry) -> int:
    geoms, audit = _geometries(fc)
    if audit.invalid_count:
        raise SpatialQAError("cannot intersect invalid feature geometry without logged repair")
    return sum(1 for geom in geoms if geom.intersects(domain))


def point_hazard_exposure(coords: Iterable[tuple[str, float, float]], hazard_fc: Mapping[str, Any]) -> tuple[int, tuple[str, ...]]:
    hazard, _ = audited_union(hazard_fc)
    return point_membership(coords, hazard)


def _project_2277(geom: BaseGeometry) -> BaseGeometry:
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:2277", always_xy=True)
    return transform(transformer.transform, geom)


def boundary_symmetric_difference_ratio(primary_fc: Mapping[str, Any], current_fc: Mapping[str, Any]) -> float:
    primary, _ = audited_union(primary_fc)
    current, _ = audited_union(current_fc)
    p = _project_2277(primary)
    c = _project_2277(current)
    if p.area <= 0:
        raise SpatialQAError("primary projected area must be positive")
    return float(p.symmetric_difference(c).area / p.area)


def spatial_case_summary(
    buscoords: Sequence[tuple[str, float, float]],
    primary_boundary_fc: Mapping[str, Any],
    current_boundary_fc: Mapping[str, Any],
    service_area_fc: Mapping[str, Any],
    roads_fc: Mapping[str, Any],
    signals_fc: Mapping[str, Any],
    flood_fc: Mapping[str, Any],
) -> dict[str, Any]:
    primary, primary_audit = audited_union(primary_boundary_fc)
    current, current_audit = audited_union(current_boundary_fc)
    service, service_audit = audited_union(service_area_fc)
    flood, flood_audit = audited_union(flood_fc)

    bus_primary_n, bus_primary_ids = point_membership(buscoords, primary)
    bus_service_n, bus_service_ids = point_membership(buscoords, service)
    bus_flood_n, bus_flood_ids = point_membership(buscoords, flood)
    road_primary = feature_intersection_count(roads_fc, primary)
    road_flood = feature_intersection_count(roads_fc, flood)
    signal_primary = feature_intersection_count(signals_fc, primary)

    return {
        "bus_total": len(buscoords),
        "bus_in_primary": bus_primary_n,
        "bus_in_primary_ids": bus_primary_ids,
        "bus_in_service_area": bus_service_n,
        "bus_in_service_area_ids": bus_service_ids,
        "bus_in_flood": bus_flood_n,
        "bus_in_flood_ids": bus_flood_ids,
        "road_features_intersect_primary": road_primary,
        "road_features_intersect_flood": road_flood,
        "signal_features_intersect_primary": signal_primary,
        "boundary_symmetric_difference_ratio": boundary_symmetric_difference_ratio(primary_boundary_fc, current_boundary_fc),
        "geometry_audits": {
            "primary": primary_audit.__dict__,
            "current": current_audit.__dict__,
            "service_area": service_audit.__dict__,
            "flood": flood_audit.__dict__,
        },
        "G2_common_spatial_support_candidate": (
            bus_primary_n > 0 and bus_service_n > 0 and road_primary > 0 and signal_primary > 0
        ),
        "G7_coupled_flood_exposure_candidate": (bus_flood_n > 0 and road_flood > 0),
        "scope": "SPATIAL_QA_ONLY_NOT_FINAL_CASE_PASS",
    }
