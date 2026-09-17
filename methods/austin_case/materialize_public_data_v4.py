#!/usr/bin/env python3
"""Austin public-data materialization v4 with temporal-evidence controls.

V4 preserves all v3 raw evidence and adds derived/semantic objects only:
- current City signal layer remains immutable raw evidence;
- a separately hashed retrospective signal subset is derived from TURN_ON_DATE;
- flood polygons are tagged as static scenario support, never event-time truth;
- radar sensor locations are tagged as retrospective device metadata.

No parameter, threshold, probability law, travel time, or hypothesis result is
estimated by this step.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import methods.austin_case.materialize_public_data as v1
import methods.austin_case.materialize_public_data_v3 as v3
from methods.austin_case.temporal_evidence import (
    flood_semantics_summary,
    retrospective_signal_subset,
    validate_flood_summary,
    validate_signal_summary,
)

TEMPORAL_VERSION = "V1_RETROSPECTIVE_SIGNAL_STATIC_FLOOD"


def _resolve_record_path(root: Path, record: dict) -> Path:
    raw = Path(str(record.get("path", "")))
    if raw.is_absolute():
        return raw
    if raw.exists():
        return raw
    candidate = root / raw
    if candidate.exists():
        return candidate
    raise FileNotFoundError(f"materialized object path not found: {raw}")


def _read_geojson(root: Path, record: dict) -> dict:
    path = _resolve_record_path(root, record)
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict) or obj.get("type") != "FeatureCollection":
        raise ValueError(f"GeoJSON FeatureCollection required: {path}")
    return obj


def acquire(root: Path) -> dict:
    manifest = v3.acquire(root)
    objects = manifest["objects"]

    signals_fc = _read_geojson(root, objects["traffic_signals"])
    subset, signal_summary = retrospective_signal_subset(signals_fc)
    validate_signal_summary(signal_summary)
    signal_payload = (json.dumps(subset, separators=(",", ":"), sort_keys=True) + "\n").encode()
    signal_record = v1.write_immutable(
        root / "derived" / "temporal" / "traffic_signals_retrospective_2018.geojson",
        signal_payload,
    )
    signal_record.update(
        {
            "source_url": objects["traffic_signals"].get("layer")
            or objects["traffic_signals"].get("source_url"),
            "derived_from": "traffic_signals",
            **signal_summary,
        }
    )
    objects["traffic_signals_retrospective_2018"] = signal_record
    objects["traffic_signals"].update(
        {
            "temporal_role": "CURRENT_NONVERSIONED_SOURCE",
            "historical_2018_truth": False,
        }
    )

    flood_fc = _read_geojson(root, objects["fema_floodplain"])
    flood_summary = flood_semantics_summary(flood_fc)
    validate_flood_summary(flood_summary)
    objects["fema_floodplain"].update(flood_summary)

    objects["radar_sensor_locations"].update(
        {
            "temporal_role": "RETROSPECTIVE_LOCATION_METADATA",
            "exact_2018_snapshot": False,
            "required_join_key": "KITS_ID",
            "2018_observation_join_verified": False,
        }
    )

    manifest["temporal_version"] = TEMPORAL_VERSION
    manifest["temporal_gate"] = {
        "signal_source_semantics": "PASS",
        "signal_retrospective_extraction": (
            "PASS" if signal_summary["retained_feature_count"] > 0 else "FAIL_EMPTY"
        ),
        "radar_2018_observation_join": "OPEN",
        "flood_static_semantics": "PASS",
        "flood_asset_intersection": "OPEN",
        "G_time": "OPEN",
    }
    manifest.setdefault("scientific_prohibitions", []).extend(
        [
            "retrospective signal subset is not a complete 2018 signal inventory",
            "current signal status is not historical outage evidence",
            "radar sensor locations require a KITS-ID join to genuine 2018 observations",
            "FEMA floodplain polygons are static scenario support, not event-time flood depth",
        ]
    )

    path = root / "qa" / "raw_materialization_manifest_v4.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/AUS-P5U-2018-V1")
    args = parser.parse_args()
    acquire(Path(args.root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
