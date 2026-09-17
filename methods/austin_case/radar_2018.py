"""Austin 2018 radar-traffic acquisition and qualification controls.

Scientific role
---------------
Stage A inventories genuine 2018 KITS sensor IDs without downloading millions
of rows. Stage B builds paginated queries only for sensor IDs already qualified
spatially. Stage C validates the KITS-ID join to retrospective Travel Sensors
metadata using an explicitly frozen location schema; field names are never
guessed by this module.

This qualifies transportation observations for subsystem calibration/validation.
It does not by itself provide independent external validation of the coupled H1
model and does not authorize random splitting of correlated 15-minute rows.
"""
from __future__ import annotations

from datetime import datetime, timezone
from math import isfinite
import urllib.parse
from typing import Any, Iterable, Mapping, Sequence

DOMAIN = "https://data.austintexas.gov"
DATASET = "i626-g7ub"
YEAR = 2018
PAGE_SIZE = 50000
START_2018 = datetime(2018, 1, 1, tzinfo=timezone.utc)
END_2018 = datetime(2019, 1, 1, tzinfo=timezone.utc)


class Radar2018Error(ValueError):
    """Raised when the 2018 radar evidence violates the frozen contract."""


def inventory_url() -> str:
    select = "int_id, count(*) as n, min(curdatetime) as t_min, max(curdatetime) as t_max"
    params = {
        "$select": select,
        "$where": f"year={YEAR}",
        "$group": "int_id",
        "$order": "int_id",
        "$limit": "50000",
    }
    return f"{DOMAIN}/resource/{DATASET}.json?{urllib.parse.urlencode(params)}"


def _sensor_clause(sensor_ids: Iterable[int]) -> str:
    ids = sorted({int(x) for x in sensor_ids})
    if not ids:
        raise ValueError("at least one spatially qualified KITS sensor ID is required")
    if any(x < 0 for x in ids):
        raise ValueError("sensor IDs must be nonnegative integers")
    return "int_id in (" + ",".join(str(x) for x in ids) + ")"


def data_page_url(sensor_ids: Iterable[int], offset: int = 0, limit: int = PAGE_SIZE) -> str:
    if offset < 0 or limit <= 0 or limit > PAGE_SIZE:
        raise ValueError("invalid Socrata page controls")
    where = f"year={YEAR} AND {_sensor_clause(sensor_ids)}"
    params = {
        "$select": "row_id,detid,int_id,curdatetime,intname,detname,volume,occupancy,speed,direction",
        "$where": where,
        "$order": "curdatetime,int_id,detid,row_id",
        "$limit": str(limit),
        "$offset": str(offset),
    }
    return f"{DOMAIN}/resource/{DATASET}.json?{urllib.parse.urlencode(params)}"


def calibration_validation_rule() -> str:
    return (
        "Freeze a chronological or independent event-block development/test split after data QC, "
        "before H1-H5 confirmatory outcomes; do not randomly split correlated 15-minute rows. "
        "This subsystem split is not automatically H1b external coupled-system validation."
    )


def _parse_timestamp(value: Any) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise Radar2018Error("radar timestamp must be a non-empty ISO string")
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError as exc:
        raise Radar2018Error(f"unparseable radar timestamp: {value!r}") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _kits_id(value: Any) -> int:
    try:
        sensor_id = int(value)
    except (TypeError, ValueError) as exc:
        raise Radar2018Error(f"invalid KITS ID: {value!r}") from exc
    if sensor_id < 0:
        raise Radar2018Error("KITS ID must be nonnegative")
    return sensor_id


def validate_inventory_rows(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Validate grouped 2018 sensor inventory returned by :func:`inventory_url`."""
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)) or not rows:
        raise Radar2018Error("nonempty 2018 radar inventory is required")
    seen: set[int] = set()
    counts: dict[int, int] = {}
    spans: dict[int, tuple[str, str]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise Radar2018Error("radar inventory rows must be objects")
        sensor_id = _kits_id(row.get("int_id"))
        if sensor_id in seen:
            raise Radar2018Error(f"duplicate grouped KITS ID: {sensor_id}")
        seen.add(sensor_id)
        try:
            n = int(row.get("n"))
        except (TypeError, ValueError) as exc:
            raise Radar2018Error(f"invalid observation count for KITS {sensor_id}") from exc
        if n <= 0:
            raise Radar2018Error(f"KITS {sensor_id} has no 2018 observations")
        t_min = _parse_timestamp(row.get("t_min"))
        t_max = _parse_timestamp(row.get("t_max"))
        if not (START_2018 <= t_min <= t_max < END_2018):
            raise Radar2018Error(f"KITS {sensor_id} inventory span is outside calendar-year 2018")
        counts[sensor_id] = n
        spans[sensor_id] = (t_min.isoformat(), t_max.isoformat())
    return {
        "year": YEAR,
        "sensor_ids": sorted(seen),
        "sensor_count": len(seen),
        "observation_count": sum(counts.values()),
        "counts_by_sensor": counts,
        "spans_by_sensor": spans,
        "temporal_role": "HISTORICAL_2018_OBSERVATION",
    }


def _point_from_row(
    row: Mapping[str, Any],
    *,
    latitude_key: str | None,
    longitude_key: str | None,
    point_key: str | None,
) -> tuple[float, float]:
    """Extract lon/lat only from an explicitly frozen schema mapping."""
    if point_key is not None:
        point = row.get(point_key)
        if not isinstance(point, Mapping):
            raise Radar2018Error(f"missing point object in field {point_key!r}")
        if isinstance(point.get("coordinates"), Sequence) and len(point["coordinates"]) >= 2:
            lon, lat = point["coordinates"][0], point["coordinates"][1]
        elif "longitude" in point and "latitude" in point:
            lon, lat = point["longitude"], point["latitude"]
        else:
            raise Radar2018Error(f"point field {point_key!r} lacks recognized coordinates")
    else:
        if latitude_key is None or longitude_key is None:
            raise Radar2018Error(
                "location schema must explicitly provide point_key or both latitude_key and longitude_key"
            )
        lat, lon = row.get(latitude_key), row.get(longitude_key)
    try:
        lat_f, lon_f = float(lat), float(lon)
    except (TypeError, ValueError) as exc:
        raise Radar2018Error("sensor location must contain numeric latitude/longitude") from exc
    if not (isfinite(lat_f) and isfinite(lon_f)):
        raise Radar2018Error("sensor location coordinates must be finite")
    if not (-90 <= lat_f <= 90 and -180 <= lon_f <= 180):
        raise Radar2018Error("sensor location is outside WGS84 bounds")
    return lon_f, lat_f


def index_sensor_locations(
    rows: Sequence[Mapping[str, Any]],
    *,
    kits_id_key: str,
    latitude_key: str | None = None,
    longitude_key: str | None = None,
    point_key: str | None = None,
) -> dict[int, tuple[float, float]]:
    """Build a unique KITS-ID location index from an explicitly mapped schema."""
    if not kits_id_key:
        raise Radar2018Error("kits_id_key must be frozen explicitly")
    out: dict[int, tuple[float, float]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise Radar2018Error("sensor-location rows must be objects")
        sensor_id = _kits_id(row.get(kits_id_key))
        point = _point_from_row(
            row,
            latitude_key=latitude_key,
            longitude_key=longitude_key,
            point_key=point_key,
        )
        if sensor_id in out:
            raise Radar2018Error(f"duplicate Travel Sensors KITS ID: {sensor_id}")
        out[sensor_id] = point
    if not out:
        raise Radar2018Error("no valid Travel Sensors locations were indexed")
    return out


def join_inventory_to_locations(
    inventory: Mapping[str, Any],
    locations: Mapping[int, tuple[float, float]],
) -> dict[str, Any]:
    """Join genuine 2018 radar KITS IDs to retrospective location metadata."""
    raw_ids = inventory.get("sensor_ids")
    if not isinstance(raw_ids, list) or not raw_ids:
        raise Radar2018Error("validated radar inventory with sensor_ids is required")
    sensor_ids = [_kits_id(x) for x in raw_ids]
    matched = {sensor_id: locations[sensor_id] for sensor_id in sensor_ids if sensor_id in locations}
    missing = sorted(sensor_id for sensor_id in sensor_ids if sensor_id not in locations)
    if not matched:
        raise Radar2018Error("no 2018 radar KITS ID joins to Travel Sensors location metadata")
    return {
        "year": YEAR,
        "matched_locations": matched,
        "matched_sensor_ids": sorted(matched),
        "missing_location_sensor_ids": missing,
        "inventory_sensor_count": len(sensor_ids),
        "matched_sensor_count": len(matched),
        "join_fraction": len(matched) / len(sensor_ids),
        "location_temporal_role": "RETROSPECTIVE_LOCATION_METADATA",
        "exact_2018_location_snapshot": False,
        "spatial_overlap_verified": False,
    }


def chronological_blocks(
    rows: Sequence[Mapping[str, Any]],
    *,
    timestamp_key: str = "curdatetime",
    split_utc: str,
) -> dict[str, list[Mapping[str, Any]]]:
    """Create deterministic non-random chronological development/validation blocks.

    This does not establish statistical independence of physical events; it only
    prevents leakage caused by random splitting of adjacent 15-minute rows.
    """
    split = _parse_timestamp(split_utc)
    if not (START_2018 < split < END_2018):
        raise Radar2018Error("chronological split must lie strictly inside 2018")
    development: list[Mapping[str, Any]] = []
    validation: list[Mapping[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping):
            raise Radar2018Error("radar data rows must be objects")
        ts = _parse_timestamp(row.get(timestamp_key))
        if not (START_2018 <= ts < END_2018):
            raise Radar2018Error("non-2018 row entered the frozen radar split")
        (development if ts < split else validation).append(row)
    if not development or not validation:
        raise Radar2018Error("chronological split must produce nonempty development and validation blocks")
    return {
        "development": development,
        "validation": validation,
        "split_utc": split.isoformat(),
        "random_row_split": False,
        "external_coupled_H1b_validation": False,
    }
