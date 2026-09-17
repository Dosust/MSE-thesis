"""Feeder-level SMART-DS Austin inventory before spatial case selection.

The inventory is intentionally metadata/coordinate-only. It discovers the
substation/feeder hierarchy and feeder Buscoords without choosing a feeder from
H1-H5 results. Complete circuit/profile materialization is a later gate.
"""
from __future__ import annotations

import json
import urllib.parse
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Callable

from methods.austin_case.materialize_public_data import (
    OEDI_HTTPS,
    SMARTDS_OPENDSS_PREFIX,
    fetch,
    object_url,
    parse_buscoords,
)

Fetch = Callable[[str], bytes]


@dataclass(frozen=True)
class S3Page:
    keys: tuple[str, ...]
    prefixes: tuple[str, ...]
    truncated: bool
    next_token: str | None


def list_url(prefix: str, delimiter: str | None = None, token: str | None = None) -> str:
    params = {"list-type": "2", "prefix": prefix}
    if delimiter is not None:
        params["delimiter"] = delimiter
    if token:
        params["continuation-token"] = token
    return OEDI_HTTPS + "?" + urllib.parse.urlencode(params)


def parse_page(payload: bytes) -> S3Page:
    root = ET.fromstring(payload)
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    keys = tuple(
        el.text for el in root.findall("s3:Contents/s3:Key", ns) if el.text
    )
    prefixes = tuple(
        el.text
        for el in root.findall("s3:CommonPrefixes/s3:Prefix", ns)
        if el.text
    )
    truncated = (root.findtext("s3:IsTruncated", "false", ns) or "false").lower() == "true"
    token = root.findtext("s3:NextContinuationToken", None, ns)
    if truncated and not token:
        raise ValueError("truncated S3 page missing continuation token")
    return S3Page(keys, prefixes, truncated, token)


def list_all(prefix: str, delimiter: str | None = None, fetcher: Fetch = fetch) -> tuple[tuple[str, ...], tuple[str, ...]]:
    keys: list[str] = []
    prefixes: list[str] = []
    token: str | None = None
    while True:
        page = parse_page(fetcher(list_url(prefix, delimiter, token)))
        keys.extend(page.keys)
        prefixes.extend(page.prefixes)
        if not page.truncated:
            break
        token = page.next_token
    return tuple(sorted(set(keys))), tuple(sorted(set(prefixes)))


def basename(prefix: str) -> str:
    return prefix.rstrip("/").split("/")[-1]


def discover_feeders(fetcher: Fetch = fetch) -> dict:
    root_keys, substation_prefixes = list_all(SMARTDS_OPENDSS_PREFIX, delimiter="/", fetcher=fetcher)
    root_names = {key.rsplit("/", 1)[-1] for key in root_keys}
    required_root = {"Buscoords.dss", "LoadShapes.dss", "Master.dss", "SMART-DS_version.txt"}
    missing_root = sorted(required_root - root_names)
    if missing_root:
        raise ValueError(f"SMART-DS regional root missing required files: {missing_root}")

    substations = []
    for station_prefix in substation_prefixes:
        station = basename(station_prefix)
        if station.lower() in {"analysis", "subtransmission"}:
            continue
        station_keys, feeder_prefixes = list_all(station_prefix, delimiter="/", fetcher=fetcher)
        feeders = []
        for feeder_prefix in feeder_prefixes:
            feeder = basename(feeder_prefix)
            if feeder.lower() == "analysis":
                continue
            feeder_keys, _ = list_all(feeder_prefix, delimiter="/", fetcher=fetcher)
            by_name = {key.rsplit("/", 1)[-1]: key for key in feeder_keys}
            required = {"Buscoords.dss", "Lines.dss", "Loads.dss", "Master.dss", "Transformers.dss"}
            missing = sorted(required - set(by_name))
            coords = []
            if "Buscoords.dss" in by_name:
                coords = parse_buscoords(fetcher(object_url(by_name["Buscoords.dss"])))
            feeders.append(
                {
                    "substation": station,
                    "feeder": feeder,
                    "prefix": feeder_prefix,
                    "buscoord_rows": len(coords),
                    "bbox_wgs84": (
                        [min(x for _, x, _ in coords), min(y for _, _, y in coords),
                         max(x for _, x, _ in coords), max(y for _, _, y in coords)]
                        if coords else None
                    ),
                    "missing_required_circuit_files": missing,
                    "structurally_complete": not missing,
                }
            )
        substations.append(
            {
                "substation": station,
                "prefix": station_prefix,
                "direct_file_count": len(station_keys),
                "feeders": feeders,
            }
        )

    feeder_count = sum(len(s["feeders"]) for s in substations)
    complete_count = sum(
        1 for s in substations for f in s["feeders"] if f["structurally_complete"] and f["buscoord_rows"] > 0
    )
    return {
        "opendss_root": SMARTDS_OPENDSS_PREFIX,
        "root_required_files_present": True,
        "substation_count": len(substations),
        "feeder_count": feeder_count,
        "complete_geocoded_feeder_count": complete_count,
        "substations": substations,
        "status": "INVENTORY_ONLY_NO_FEEDER_SELECTED",
        "selection_uses_hypothesis_results": False,
    }


def main() -> int:
    print(json.dumps(discover_feeders(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
