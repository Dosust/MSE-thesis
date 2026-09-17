"""Fail-closed Travel Sensors schema observation and freeze controls."""
from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping, Sequence


class TravelSensorSchemaError(ValueError):
    """Raised when Travel Sensors schema provenance is incomplete or contradictory."""


SCHEMA_METADATA_ENDPOINT = "https://data.austintexas.gov/api/views/6yd9-yz29/columns.json"


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise TravelSensorSchemaError(message)


def observe_schema(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Describe observed row keys/types without selecting semantic fields."""
    _require(
        isinstance(rows, Sequence) and not isinstance(rows, (str, bytes)) and len(rows) > 0,
        "nonempty Travel Sensors rows are required",
    )
    occurrence: dict[str, int] = {}
    non_null: dict[str, int] = {}
    value_types: dict[str, set[str]] = {}
    for row in rows:
        _require(isinstance(row, Mapping), "Travel Sensors rows must be objects")
        for key, value in row.items():
            _require(isinstance(key, str) and key, "Travel Sensors keys must be nonempty strings")
            occurrence[key] = occurrence.get(key, 0) + 1
            if value is not None and value != "":
                non_null[key] = non_null.get(key, 0) + 1
                value_types.setdefault(key, set()).add(type(value).__name__)
            else:
                value_types.setdefault(key, set())
    observed_keys = sorted(occurrence)
    canonical = json.dumps(observed_keys, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return {
        "row_count": len(rows),
        "observed_keys": observed_keys,
        "observed_keys_sha256": hashlib.sha256(canonical).hexdigest(),
        "occurrence_count": {key: occurrence[key] for key in observed_keys},
        "non_null_count": {key: non_null.get(key, 0) for key in observed_keys},
        "value_types": {key: sorted(value_types[key]) for key in observed_keys},
        "semantic_field_selection": "NOT_PERFORMED",
    }


def validate_registry(registry: Mapping[str, Any]) -> str:
    """Validate OPEN or FROZEN registry state without inferring field names."""
    _require(registry.get("version") == "1.0", "unexpected Travel Sensors schema version")
    _require(registry.get("case_id") == "AUS-P5U-2018-V1", "unexpected Austin case ID")
    dataset = registry.get("dataset")
    _require(isinstance(dataset, Mapping), "dataset object required")
    _require(dataset.get("dataset_id") == "6yd9-yz29", "Travel Sensors dataset ID drift")
    _require(
        dataset.get("schema_metadata_endpoint") == SCHEMA_METADATA_ENDPOINT,
        "Travel Sensors official schema metadata endpoint drift",
    )
    _require(
        dataset.get("temporal_role") == "RETROSPECTIVE_LOCATION_METADATA",
        "Travel Sensors temporal role drift",
    )
    _require(dataset.get("exact_2018_snapshot") is False, "Travel Sensors cannot claim exact 2018 snapshot")

    status = registry.get("status")
    _require(status in {"OPEN", "FROZEN"}, "schema status must be OPEN or FROZEN")
    metadata = registry.get("metadata_evidence")
    raw = registry.get("raw_evidence")
    mapping = registry.get("field_mapping")
    verification = registry.get("verification")
    _require(isinstance(metadata, Mapping), "metadata_evidence object required")
    _require(isinstance(raw, Mapping), "raw_evidence object required")
    _require(isinstance(mapping, Mapping), "field_mapping object required")
    _require(isinstance(verification, Mapping), "verification object required")

    observed_keys = raw.get("observed_keys")
    _require(isinstance(observed_keys, list), "observed_keys must be a list")

    if status == "OPEN":
        _require(
            verification.get("selected_fields_observed") is False,
            "OPEN schema cannot claim selected fields observed",
        )
        return "OPEN"

    metadata_digest = metadata.get("columns_metadata_sha256")
    column_count = metadata.get("column_count")
    _require(
        isinstance(metadata_digest, str) and len(metadata_digest) == 64,
        "FROZEN schema requires official column-metadata SHA-256",
    )
    _require(isinstance(column_count, int) and column_count > 0, "FROZEN schema requires positive metadata column count")

    digest = raw.get("raw_data_sha256")
    keys_digest = raw.get("observed_keys_sha256")
    row_count = raw.get("raw_row_count")
    _require(isinstance(digest, str) and len(digest) == 64, "FROZEN schema requires raw-data SHA-256")
    _require(isinstance(keys_digest, str) and len(keys_digest) == 64, "FROZEN schema requires observed-keys SHA-256")
    _require(isinstance(row_count, int) and row_count > 0, "FROZEN schema requires positive raw row count")
    _require(bool(observed_keys), "FROZEN schema requires observed keys")

    kits_key = mapping.get("kits_id_key")
    point_key = mapping.get("point_key")
    lat_key = mapping.get("latitude_key")
    lon_key = mapping.get("longitude_key")
    _require(isinstance(kits_key, str) and kits_key in observed_keys, "FROZEN KITS field must be observed")
    point_mode = isinstance(point_key, str) and point_key in observed_keys
    latlon_mode = (
        isinstance(lat_key, str)
        and lat_key in observed_keys
        and isinstance(lon_key, str)
        and lon_key in observed_keys
    )
    _require(point_mode ^ latlon_mode, "FROZEN schema requires exactly one coordinate mapping mode")
    _require(
        isinstance(registry.get("mapping_evidence_basis"), str)
        and bool(registry["mapping_evidence_basis"].strip()),
        "FROZEN schema requires mapping evidence basis",
    )

    required_checks = (
        "official_metadata_mapping_unique",
        "selected_fields_observed",
        "kits_values_valid",
        "kits_unique_or_resolution_versioned",
        "coordinates_valid",
        "at_least_one_2018_radar_join",
        "missing_joins_reported",
    )
    for check in required_checks:
        _require(verification.get(check) is True, f"FROZEN schema requires verification PASS: {check}")
    # Road overlap remains a downstream G4 spatial gate and is intentionally not
    # required to freeze the API schema itself.
    return "FROZEN"
