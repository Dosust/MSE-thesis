#!/usr/bin/env python3
"""Austin public-data materialization v2 aligned with boundary-vintage freeze.

V2 changes only the boundary provenance contract:
- primary: explicit City full-purpose boundary last edited 2019-04-04;
- current BOUNDARIES_jurisdictions FULL class: sensitivity/cross-check.
All other immutable/paginated acquisition logic is inherited from v1.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import methods.austin_case.materialize_public_data as v1

PRIMARY_BOUNDARY_LAYER = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/"
    "City_of_Austin_full_purpose_boundary/FeatureServer/0"
)
CURRENT_JURISDICTION_LAYER = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/"
    "BOUNDARIES_jurisdictions/FeatureServer/0"
)
CURRENT_FULL_WHERE = "JURISDICTION_TYPE='FULL'"
PRIMARY_ITEM_ID = "46a37551e8b64f098f29a2f991df5e9d"


def acquire(root: Path) -> dict:
    # The v1 acquisition function reads its module-level boundary constant.
    # Override it explicitly here so v1 remains preserved for provenance.
    original = v1.BOUNDARY_LAYER
    v1.BOUNDARY_LAYER = PRIMARY_BOUNDARY_LAYER
    try:
        manifest = v1.acquire(root)
    finally:
        v1.BOUNDARY_LAYER = original

    primary = manifest["objects"]["austin_full_purpose"]
    primary.update(
        {
            "boundary_role": "PRIMARY_2018_ERA_SUPPORT",
            "arcgis_item_id": PRIMARY_ITEM_ID,
            "known_data_last_edit": "2019-04-04T03:13:39Z",
            "native_crs": "EPSG:3857",
        }
    )

    payload, meta = v1.acquire_arcgis_layer(
        CURRENT_JURISDICTION_LAYER,
        bbox=None,
        raw_dir=root / "raw" / "gis" / "austin_current_full_purpose",
        name="austin_current_full_purpose",
        where=CURRENT_FULL_WHERE,
    )
    record = v1.write_immutable(
        root / "raw" / "gis" / "austin_current_full_purpose.geojson", payload
    )
    record.update(meta)
    record.update(
        {
            "boundary_role": "CURRENT_BOUNDARY_SENSITIVITY_ONLY",
            "where": CURRENT_FULL_WHERE,
            "native_crs": "EPSG:2277",
        }
    )
    manifest["objects"]["austin_current_full_purpose"] = record
    manifest["boundary_version"] = "V2_2019_PRIMARY_CURRENT_SENSITIVITY"

    path = root / "qa" / "raw_materialization_manifest_v2.json"
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
