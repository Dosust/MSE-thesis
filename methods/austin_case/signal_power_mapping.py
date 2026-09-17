"""Synthetic P->T traffic-signal mapping for Austin case QA.

The result is explicitly a demonstrator crosswalk, never an observed Austin
Energy feeder assignment. A maximum mapping discrepancy must be supplied by a
pre-result spatial-QA decision before confirmatory use.
"""
from __future__ import annotations

from math import isfinite
from typing import Any, Mapping, Sequence

from pyproj import Geod
from shapely.geometry import shape

WGS84 = Geod(ellps="WGS84")


class SignalMappingError(ValueError):
    pass


def distance_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    _, _, d = WGS84.inv(a[0], a[1], b[0], b[1])
    return float(d)


def signal_points(signals_fc: Mapping[str, Any], id_field: str | None = None) -> list[tuple[str, float, float]]:
    features = signals_fc.get("features")
    if not isinstance(features, list):
        raise SignalMappingError("GeoJSON FeatureCollection required")
    rows = []
    seen = set()
    for index, feature in enumerate(features):
        if not isinstance(feature, Mapping) or feature.get("geometry") is None:
            continue
        geom = shape(feature["geometry"])
        if geom.geom_type != "Point" or geom.is_empty or not geom.is_valid:
            raise SignalMappingError(f"signal feature {index} must be one valid Point")
        props = feature.get("properties") or {}
        signal_id = str(props.get(id_field)) if id_field and props.get(id_field) is not None else f"feature_{index}"
        if signal_id in seen:
            raise SignalMappingError(f"duplicate signal identifier: {signal_id}")
        seen.add(signal_id)
        rows.append((signal_id, float(geom.x), float(geom.y)))
    if not rows:
        raise SignalMappingError("no usable traffic-signal points")
    return rows


def map_signals_to_power(
    signals_fc: Mapping[str, Any],
    eligible_power_points: Sequence[tuple[str, float, float]],
    max_distance_m: float,
    *,
    id_field: str | None = None,
) -> dict[str, Any]:
    if not isfinite(float(max_distance_m)) or max_distance_m <= 0:
        raise SignalMappingError("max_distance_m must be positive and finite")
    if not eligible_power_points:
        raise SignalMappingError("eligible power point set must be nonempty")
    power = []
    ids = set()
    for pid, lon, lat in eligible_power_points:
        pid = str(pid)
        if pid in ids:
            raise SignalMappingError(f"duplicate power identifier: {pid}")
        if not (-180 <= lon <= 180 and -90 <= lat <= 90):
            raise SignalMappingError(f"invalid power coordinate: {pid}")
        ids.add(pid)
        power.append((pid, float(lon), float(lat)))

    mappings = []
    rejected = []
    for sid, lon, lat in signal_points(signals_fc, id_field=id_field):
        nearest = min(
            ((pid, distance_m((lon, lat), (plon, plat))) for pid, plon, plat in power),
            key=lambda item: item[1],
        )
        if nearest[1] <= max_distance_m:
            mappings.append(
                {
                    "signal_id": sid,
                    "synthetic_power_id": nearest[0],
                    "mapping_distance_m": nearest[1],
                    "observed_feeder_assignment": False,
                }
            )
        else:
            rejected.append(
                {"signal_id": sid, "nearest_power_id": nearest[0], "distance_m": nearest[1]}
            )
    total = len(mappings) + len(rejected)
    return {
        "mapped": mappings,
        "rejected": rejected,
        "mapped_count": len(mappings),
        "rejected_count": len(rejected),
        "mapping_fraction": len(mappings) / total if total else 0.0,
        "max_distance_m": float(max_distance_m),
        "semantics": "SYNTHETIC_SPATIAL_CROSSWALK_NOT_OBSERVED_UTILITY_FEEDER",
    }
