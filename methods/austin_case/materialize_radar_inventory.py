#!/usr/bin/env python3
"""Materialize Austin 2018 radar inventory and observe Travel Sensors schema.

This is a pre-join evidence step. It downloads only the grouped 2018 radar
sensor inventory, validates its time support, and records the exact keys present
in the already-materialized Travel Sensors rows. It deliberately does not guess
which Travel Sensors API fields represent KITS ID or coordinates.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import methods.austin_case.materialize_public_data as base
from methods.austin_case.radar_2018 import inventory_url, validate_inventory_rows
from methods.austin_case.travel_sensor_schema import observe_schema


class RadarInventoryMaterializationError(RuntimeError):
    pass


def _resolve(root: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute() and path.exists():
        return path
    if path.exists():
        return path
    candidate = root / path
    if candidate.exists():
        return candidate
    raise RadarInventoryMaterializationError(f"referenced materialized file not found: {value}")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def materialize(root: Path) -> dict[str, Any]:
    manifest_path = root / "qa" / "raw_materialization_manifest_v4.json"
    if not manifest_path.exists():
        raise RadarInventoryMaterializationError(
            "v4 core materialization manifest is required before radar inventory"
        )
    manifest = _read_json(manifest_path)
    if manifest.get("case_id") != "AUS-P5U-2018-V1":
        raise RadarInventoryMaterializationError("unexpected Austin case ID")
    objects = manifest.get("objects")
    if not isinstance(objects, dict) or "radar_sensor_locations" not in objects:
        raise RadarInventoryMaterializationError("radar_sensor_locations raw object is required")

    # Stage A: grouped 2018 sensor inventory only.
    url = inventory_url()
    payload = base.fetch(url)
    raw_record = base.write_immutable(
        root / "raw" / "traffic" / "radar_2018_sensor_inventory.json", payload
    )
    raw_record["source_url"] = url
    rows = json.loads(payload)
    if not isinstance(rows, list):
        raise RadarInventoryMaterializationError("radar inventory response must be a JSON list")
    inventory_summary = validate_inventory_rows(rows)
    inventory_record = {
        **raw_record,
        "source_dataset": "i626-g7ub",
        "query_role": "GROUPED_2018_KITS_SENSOR_INVENTORY",
        **inventory_summary,
    }

    # Stage B: observe Travel Sensors raw row schema without selecting semantics.
    sensor_record = objects["radar_sensor_locations"]
    if not isinstance(sensor_record, dict) or not isinstance(sensor_record.get("path"), str):
        raise RadarInventoryMaterializationError("invalid radar_sensor_locations manifest record")
    sensor_path = _resolve(root, sensor_record["path"])
    sensor_rows = _read_json(sensor_path)
    if not isinstance(sensor_rows, list):
        raise RadarInventoryMaterializationError("Travel Sensors raw object must be a JSON list")
    schema_observation = observe_schema(sensor_rows)
    schema_observation.update(
        {
            "dataset_id": "6yd9-yz29",
            "source_url": sensor_record.get("source_url"),
            "raw_data_sha256": sensor_record.get("sha256"),
            "temporal_role": "RETROSPECTIVE_LOCATION_METADATA",
            "field_mapping_status": "OPEN",
        }
    )

    qa_dir = root / "qa"
    qa_dir.mkdir(parents=True, exist_ok=True)
    inventory_summary_path = qa_dir / "radar_2018_inventory_summary.json"
    schema_path = qa_dir / "travel_sensor_schema_observation.json"
    inventory_summary_path.write_text(
        json.dumps(inventory_record, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    schema_path.write_text(
        json.dumps(schema_observation, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    result = {
        "case_id": "AUS-P5U-2018-V1",
        "radar_inventory": inventory_record,
        "travel_sensor_schema_observation": schema_observation,
        "gates": {
            "radar_2018_inventory": "PASS",
            "travel_sensor_raw_schema_observed": "PASS",
            "travel_sensor_field_mapping": "OPEN",
            "radar_2018_location_join": "OPEN",
            "road_spatial_overlap": "OPEN",
            "G4_traffic_observations": "OPEN",
        },
        "prohibitions": [
            "schema observation does not select KITS or coordinate API fields",
            "inventory materialization does not download all 15-minute observations",
            "G4 cannot pass before verified KITS join and road overlap",
        ],
    }
    result_path = qa_dir / "radar_2018_prejoin_manifest.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/AUS-P5U-2018-V1")
    args = parser.parse_args()
    materialize(Path(args.root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
