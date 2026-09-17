"""Austin 2018 radar-traffic acquisition controls.

Stage A inventories 2018 KITS sensor IDs without downloading millions of rows.
Stage B builds paginated queries only for sensor IDs already qualified spatially.
No traffic data are used to select the hypothesis outcome or effect threshold.
"""
from __future__ import annotations

import urllib.parse
from typing import Iterable

DOMAIN = "https://data.austintexas.gov"
DATASET = "i626-g7ub"
YEAR = 2018
PAGE_SIZE = 50000


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
        "Freeze a chronological or event-block development/test split after data QC, "
        "before H1-H5 confirmatory outcomes; do not randomly split correlated 15-minute rows."
    )
