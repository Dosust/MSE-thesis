#!/usr/bin/env python3
"""Resolve the Travel Sensors schema from official metadata and raw evidence.

This step may freeze the API field mapping and verify the 2018 radar KITS join.
It never closes road-overlap or final G4 traffic admissibility.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import methods.austin_case.materialize_public_data as base
from methods.austin_case.travel_sensor_metadata import resolve_runtime_registry
from methods.austin_case.travel_sensor_schema import SCHEMA_METADATA_ENDPOINT


class TravelSensorResolutionError(RuntimeError):
    pass


def _read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_path(root: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute() and path.exists():
        return path
    if path.exists():
        return path
    candidate = root / path
    if candidate.exists():
        return candidate
    raise TravelSensorResolutionError(f"referenced evidence file not found: {value}")


def resolve(root: Path, template_path: Path) -> dict[str, Any]:
    core_path = root / "qa" / "raw_materialization_manifest_v4.json"
    prejoin_path = root / "qa" / "radar_2018_prejoin_manifest.json"
    if not core_path.exists() or not prejoin_path.exists():
        raise TravelSensorResolutionError("v4 core and radar prejoin manifests are required")

    core = _read(core_path)
    prejoin = _read(prejoin_path)
    template = _read(template_path)
    if core.get("case_id") != "AUS-P5U-2018-V1" or prejoin.get("case_id") != "AUS-P5U-2018-V1":
        raise TravelSensorResolutionError("unexpected Austin case ID")

    sensor_record = core.get("objects", {}).get("radar_sensor_locations")
    if not isinstance(sensor_record, dict):
        raise TravelSensorResolutionError("radar_sensor_locations raw record is required")
    sensor_path = _resolve_path(root, str(sensor_record.get("path", "")))
    sensor_rows = _read(sensor_path)
    if not isinstance(sensor_rows, list):
        raise TravelSensorResolutionError("Travel Sensors raw rows must be a JSON list")
    sensor_sha = sensor_record.get("sha256")
    if not isinstance(sensor_sha, str) or len(sensor_sha) != 64:
        raise TravelSensorResolutionError("Travel Sensors raw SHA-256 is required")

    inventory_summary = prejoin.get("radar_inventory")
    if not isinstance(inventory_summary, dict):
        raise TravelSensorResolutionError("validated radar inventory summary is required")

    metadata_payload = base.fetch(SCHEMA_METADATA_ENDPOINT)
    metadata_record = base.write_immutable(
        root / "raw" / "traffic" / "travel_sensor_columns.json", metadata_payload
    )
    metadata_record["source_url"] = SCHEMA_METADATA_ENDPOINT

    runtime_registry, join = resolve_runtime_registry(
        template,
        columns_payload=metadata_payload,
        sensor_rows=sensor_rows,
        sensor_raw_sha256=sensor_sha,
        inventory_summary=inventory_summary,
    )
    runtime_registry["metadata_evidence"]["columns_metadata_raw_record"] = metadata_record

    qa = root / "qa"
    runtime_path = qa / "austin_travel_sensor_schema_runtime.json"
    runtime_path.write_text(
        json.dumps(runtime_registry, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    if runtime_registry["status"] == "FROZEN":
        join_path = qa / "radar_2018_location_join.json"
        join_path.write_text(json.dumps(join, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        state = "SCHEMA_FROZEN_2018_JOIN_PASS_ROAD_OVERLAP_OPEN"
    else:
        state = "SCHEMA_OPEN_UNRESOLVED_G4_OPEN"

    result = {
        "case_id": "AUS-P5U-2018-V1",
        "state": state,
        "schema_status": runtime_registry["status"],
        "runtime_schema_path": str(runtime_path),
        "radar_location_join_path": (
            str(qa / "radar_2018_location_join.json") if join is not None else None
        ),
        "road_overlap_verified": False,
        "G4_traffic_observations": "OPEN",
        "scientific_scope": "SCHEMA_AND_KITS_JOIN_ONLY_NOT_SPATIAL_TRAFFIC_ADMISSIBILITY",
    }
    result_path = qa / "travel_sensor_schema_resolution_manifest.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/AUS-P5U-2018-V1")
    parser.add_argument(
        "--template", default="config/austin_travel_sensor_schema_v1.json"
    )
    args = parser.parse_args()
    resolve(Path(args.root), Path(args.template))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
