#!/usr/bin/env python3
"""Materialize Austin Energy service-area geometry for spatial cross-check only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from methods.austin_case.materialize_public_data import acquire_arcgis_layer, write_immutable

SERVICE_AREA_LAYER = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/"
    "UTILITIESCOMMUNICATION_austin_energy_service_area/FeatureServer/0"
)
ITEM_ID = "fda30e1a33af449fa9e75e28ad36643e"
CASE_ID = "AUS-P5U-2018-V1"


def materialize(root: Path) -> dict:
    raw_dir = root / "raw" / "gis" / "austin_energy_service_area"
    payload, metadata = acquire_arcgis_layer(
        SERVICE_AREA_LAYER,
        bbox=None,
        raw_dir=raw_dir,
        name="austin_energy_service_area",
        where="1=1",
    )
    merged = write_immutable(
        root / "raw" / "gis" / "austin_energy_service_area.geojson", payload
    )
    merged.update(metadata)
    result = {
        "case_id": CASE_ID,
        "item_id": ITEM_ID,
        "role": "GEOGRAPHIC_CROSSCHECK_ONLY",
        "claims_real_feeder_topology": False,
        "object": merged,
    }
    qa = root / "qa"
    qa.mkdir(parents=True, exist_ok=True)
    (qa / "austin_energy_service_area_manifest.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/AUS-P5U-2018-V1")
    args = parser.parse_args()
    print(json.dumps(materialize(Path(args.root)), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
