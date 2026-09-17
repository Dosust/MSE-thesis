#!/usr/bin/env python3
"""Austin public-data materialization v3 with exact 2018 road provenance.

V3 preserves v2 boundary-vintage controls and adds:
- primary road evidence: TxDOT Roadway Inventory 2018;
- current City CTN: semantic/topology sensitivity only;
- current City street centerline from v2: geometry sensitivity only.

Successful acquisition remains raw-evidence materialization, not final case
admissibility.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import methods.austin_case.materialize_public_data as v1
import methods.austin_case.materialize_public_data_v2 as v2
from methods.austin_case.road_vintage import (
    AUSTIN_CTN_LAYER,
    ROAD_VERSION,
    TXDOT_2018_LAYER,
)

CTN_EXISTING_ROADWAY_WHERE = "FACILITY_TYPE='Roadway' AND BUILT_STATUS='Existing'"


def _acquire_extra_arcgis(
    root: Path,
    *,
    name: str,
    layer: str,
    bbox: tuple[float, float, float, float],
    where: str = "1=1",
) -> dict:
    payload, metadata = v1.acquire_arcgis_layer(
        layer,
        bbox=bbox,
        raw_dir=root / "raw" / "gis" / name,
        name=name,
        where=where,
    )
    record = v1.write_immutable(root / "raw" / "gis" / f"{name}.geojson", payload)
    record.update(metadata)
    record["source_url"] = layer
    return record


def acquire(root: Path) -> dict:
    manifest = v2.acquire(root)
    objects = manifest["objects"]
    bbox = tuple(float(x) for x in objects["smartds_buscoords"]["bbox_wgs84"])

    # Preserve the live City street source already materialized by v2, but
    # explicitly demote it from temporal truth to current-geometry sensitivity.
    objects["street_centerline"].update(
        {
            "road_role": "CURRENT_GEOMETRY_SENSITIVITY",
            "strict_2018_snapshot": False,
        }
    )

    primary = _acquire_extra_arcgis(
        root,
        name="txdot_roadway_inventory_2018",
        layer=TXDOT_2018_LAYER,
        bbox=bbox,
    )
    primary.update(
        {
            "inventory_year": 2018,
            "native_crs": "EPSG:4269",
            "source_family": "TxDOT Geospatial Roadway Inventory Database (GRID)",
            "road_role": "PRIMARY_EXACT_2018_ANNUAL_INVENTORY",
            "strict_2018_snapshot": True,
        }
    )
    objects["txdot_roadway_inventory_2018"] = primary

    ctn = _acquire_extra_arcgis(
        root,
        name="austin_ctn_current",
        layer=AUSTIN_CTN_LAYER,
        bbox=bbox,
        where=CTN_EXISTING_ROADWAY_WHERE,
    )
    ctn.update(
        {
            "native_crs": "EPSG:2277",
            "source_origin": "created by City staff between 2017 and 2018",
            "live_update_state": "UPDATED_REGULARLY_CURRENT_SERVICE",
            "road_role": "CURRENT_SEMANTIC_TOPOLOGY_SENSITIVITY",
            "strict_2018_snapshot": False,
            "where": CTN_EXISTING_ROADWAY_WHERE,
        }
    )
    objects["austin_ctn_current"] = ctn

    manifest["road_version"] = ROAD_VERSION
    manifest.setdefault("scientific_prohibitions", []).extend(
        [
            "live City CTN is not a frozen 2018 snapshot",
            "current City street centerline is sensitivity evidence only",
            "road geometry alone does not establish travel time, capacity, or passability",
        ]
    )

    path = root / "qa" / "raw_materialization_manifest_v3.json"
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
