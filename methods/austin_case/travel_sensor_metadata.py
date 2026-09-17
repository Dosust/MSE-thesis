"""Resolve Travel Sensors API fields from official Socrata column metadata.

The resolver is intentionally conservative. It accepts only unique exact
semantic labels from the official `columns.json` metadata and then requires the
resulting API field names to be present in the raw observed row schema. If the
metadata is missing or ambiguous, the result remains OPEN rather than guessing.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from typing import Any, Mapping, Sequence

from methods.austin_case.radar_2018 import (
    Radar2018Error,
    index_sensor_locations,
    join_inventory_to_locations,
)
from methods.austin_case.travel_sensor_schema import observe_schema, validate_registry


class TravelSensorMetadataError(ValueError):
    pass


def _norm(value: Any) -> str:
    return " ".join(str(value or "").strip().casefold().split())


def parse_columns(payload: bytes) -> list[Mapping[str, Any]]:
    try:
        obj = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise TravelSensorMetadataError("official columns metadata is not valid JSON") from exc
    if isinstance(obj, Mapping):
        obj = obj.get("columns")
    if not isinstance(obj, list) or not obj:
        raise TravelSensorMetadataError("official columns metadata must contain a nonempty column list")
    columns: list[Mapping[str, Any]] = []
    for col in obj:
        if not isinstance(col, Mapping):
            raise TravelSensorMetadataError("column metadata entries must be objects")
        columns.append(col)
    return columns


def _unique_exact_name(columns: Sequence[Mapping[str, Any]], names: set[str]) -> Mapping[str, Any] | None:
    matches = [col for col in columns if _norm(col.get("name")) in names]
    if len(matches) == 1:
        return matches[0]
    return None


def _field_name(column: Mapping[str, Any] | None) -> str | None:
    if column is None:
        return None
    value = column.get("fieldName") or column.get("field_name")
    return value if isinstance(value, str) and value.strip() else None


def resolve_mapping_from_metadata(
    columns: Sequence[Mapping[str, Any]], observed_keys: Sequence[str]
) -> dict[str, Any]:
    """Return RESOLVED only for one unambiguous official metadata mapping."""
    observed = set(observed_keys)
    kits_col = _unique_exact_name(columns, {"kits id"})
    kits_key = _field_name(kits_col)
    if kits_key is None or kits_key not in observed:
        return {
            "status": "OPEN_UNRESOLVED",
            "reason": "unique official KITS ID field not found in observed raw keys",
            "field_mapping": None,
        }

    lat_col = _unique_exact_name(columns, {"latitude"})
    lon_col = _unique_exact_name(columns, {"longitude"})
    lat_key, lon_key = _field_name(lat_col), _field_name(lon_col)
    latlon_candidate = (
        lat_key is not None
        and lon_key is not None
        and lat_key in observed
        and lon_key in observed
    )

    point_matches = [
        col
        for col in columns
        if _norm(col.get("name")) in {"location", "sensor location"}
        and _norm(col.get("dataTypeName") or col.get("data_type_name"))
        in {"location", "point", "geospatial"}
    ]
    point_key = _field_name(point_matches[0]) if len(point_matches) == 1 else None
    point_candidate = point_key is not None and point_key in observed

    if int(latlon_candidate) + int(point_candidate) != 1:
        return {
            "status": "OPEN_UNRESOLVED",
            "reason": "coordinate mapping is missing or ambiguous in official metadata",
            "field_mapping": None,
        }

    mapping = {
        "kits_id_key": kits_key,
        "point_key": point_key if point_candidate else None,
        "latitude_key": lat_key if latlon_candidate else None,
        "longitude_key": lon_key if latlon_candidate else None,
    }
    return {
        "status": "RESOLVED_UNIQUE_OFFICIAL_METADATA",
        "reason": None,
        "field_mapping": mapping,
    }


def resolve_runtime_registry(
    template: Mapping[str, Any],
    *,
    columns_payload: bytes,
    sensor_rows: Sequence[Mapping[str, Any]],
    sensor_raw_sha256: str,
    inventory_summary: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """Create an OPEN or FROZEN runtime schema registry from immutable evidence."""
    columns = parse_columns(columns_payload)
    observation = observe_schema(sensor_rows)
    resolution = resolve_mapping_from_metadata(columns, observation["observed_keys"])

    registry = deepcopy(dict(template))
    registry["metadata_evidence"] = {
        "columns_metadata_sha256": hashlib.sha256(columns_payload).hexdigest(),
        "column_count": len(columns),
    }
    registry["raw_evidence"] = {
        "raw_data_sha256": sensor_raw_sha256,
        "raw_row_count": observation["row_count"],
        "observed_keys_sha256": observation["observed_keys_sha256"],
        "observed_keys": observation["observed_keys"],
    }

    if resolution["status"] != "RESOLVED_UNIQUE_OFFICIAL_METADATA":
        registry["status"] = "OPEN"
        registry["field_mapping"] = {
            "kits_id_key": None,
            "point_key": None,
            "latitude_key": None,
            "longitude_key": None,
        }
        registry["mapping_evidence_basis"] = None
        registry["runtime_resolution"] = resolution
        validate_registry(registry)
        return registry, None

    mapping = resolution["field_mapping"]
    try:
        locations = index_sensor_locations(
            sensor_rows,
            kits_id_key=mapping["kits_id_key"],
            latitude_key=mapping["latitude_key"],
            longitude_key=mapping["longitude_key"],
            point_key=mapping["point_key"],
        )
        join = join_inventory_to_locations(inventory_summary, locations)
    except Radar2018Error as exc:
        raise TravelSensorMetadataError(
            f"official metadata mapping failed raw-value/join verification: {exc}"
        ) from exc

    registry["status"] = "FROZEN"
    registry["field_mapping"] = mapping
    registry["mapping_evidence_basis"] = (
        "official City Socrata columns metadata (immutable SHA-256) + raw Travel Sensors "
        "observed schema (immutable SHA-256) + verified KITS-ID raw values/coordinates + "
        "verified join to genuine calendar-2018 radar inventory"
    )
    registry["verification"].update(
        {
            "official_metadata_mapping_unique": True,
            "selected_fields_observed": True,
            "kits_values_valid": True,
            "kits_unique_or_resolution_versioned": True,
            "coordinates_valid": True,
            "at_least_one_2018_radar_join": True,
            "missing_joins_reported": True,
            "road_overlap_verified": False,
        }
    )
    registry["runtime_resolution"] = resolution
    validate_registry(registry)
    return registry, join
