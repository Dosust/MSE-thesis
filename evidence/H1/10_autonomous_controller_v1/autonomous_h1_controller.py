#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "H1_RAW_DATA_v1"

EXPECTED = {
    "NYISO": [
        "20200701pal_csv.zip","20200801pal_csv.zip","20221201pal_csv.zip",
        "20231201pal_csv.zip","20240401pal_csv.zip"
    ],
    "EAGLEI": [
        "eaglei_outages_2020.csv","eaglei_outages_2022.csv",
        "eaglei_outages_2023.csv","eaglei_outages_2024.csv"
    ],
    "TLC": [
        "fhvhv_tripdata_2020-07.parquet","fhvhv_tripdata_2020-08.parquet",
        "fhvhv_tripdata_2022-12.parquet","fhvhv_tripdata_2023-12.parquet",
        "fhvhv_tripdata_2024-04.parquet"
    ],
}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()

def inventory():
    rows=[]
    for group,names in EXPECTED.items():
        for name in names:
            p=RAW/group/name
            rows.append({
                "group":group,
                "name":name,
                "exists":p.exists(),
                "size_bytes":p.stat().st_size if p.exists() else None,
                "sha256":sha256(p) if p.exists() else None,
            })
    return rows

def main():
    RAW.mkdir(exist_ok=True)
    for group in EXPECTED:
        (RAW/group).mkdir(exist_ok=True)
    inv=inventory()
    (ROOT/"raw_inventory_v1.json").write_text(json.dumps(inv,indent=2))
    missing=[r for r in inv if not r["exists"]]
    if missing:
        print("S08_BLOCKED_RAW_BYTES")
        for r in missing:
            print(f"MISSING {r['group']}/{r['name']}")
        print("STOP: state machine refuses to advance to R1-R8.")
        return 2
    print("S08_CORE_BINARY_SET_PRESENT")
    print("NEXT: execute the frozen R1-R8 row-level audit.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
