#!/usr/bin/env python3
"""
EGMIV H1 row-level audit executor v1.0.

This program is intentionally separated into:
1) acquisition, which requires external internet access;
2) deterministic audit metrics, which can be unit-tested offline.

It never treats absent EAGLE-I rows as zero outage and never treats TLC completed
trips as the full requested-demand population.
"""
from __future__ import annotations
import argparse, hashlib, io, json, math, os, sys, zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlencode
import pandas as pd
import requests

NYC_FIPS = {"36005","36047","36061","36081","36085"}

EVENTS = {
"E0": dict(name="Tropical Storm Fay", start="2020-07-09T00:00:00", end="2020-07-12T23:59:59", year=2020, month=7),
"E1": dict(name="Tropical Storm Isaias", start="2020-08-03T00:00:00", end="2020-08-13T23:59:59", year=2020, month=8),
"E2": dict(name="December 2022 wind/rain storm", start="2022-12-22T00:00:00", end="2022-12-26T23:59:59", year=2022, month=12),
"E3": dict(name="December 2023 wind/rain storm", start="2023-12-17T00:00:00", end="2023-12-20T23:59:59", year=2023, month=12),
"E4": dict(name="April 2024 coastal wind/rain storm", start="2024-04-02T00:00:00", end="2024-04-06T23:59:59", year=2024, month=4),
}

REQUIRED = {
    "NYISO_P58B": ["Time Stamp","Time Zone","Name","PTID","Load"],
    "EAGLEI": ["fips_code","county","state","sum","run_start_time"],
    "TLC_HVFHV": ["request_datetime","pickup_datetime","dropoff_datetime","PULocationID","DOLocationID"],
    "NYC_DOT_SPEEDS": ["data_as_of","link_id","speed","travel_time","status","borough","link_name"],
    "NYC_311": ["unique_key","created_date","agency","complaint_type","descriptor","status","borough","latitude","longitude"],
}
TIME_FIELD = {
    "NYISO_P58B":"Time Stamp",
    "EAGLEI":"run_start_time",
    "TLC_HVFHV":"pickup_datetime",
    "NYC_DOT_SPEEDS":"data_as_of",
    "NYC_311":"created_date",
}
ID_FIELDS = {
    "NYISO_P58B":["Time Stamp","Name"],
    "EAGLEI":["fips_code","run_start_time"],
    "TLC_HVFHV":["hvfhs_license_num","dispatching_base_num","pickup_datetime","dropoff_datetime","PULocationID","DOLocationID"],
    "NYC_DOT_SPEEDS":["link_id","data_as_of"],
    "NYC_311":["unique_key"],
}

def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def parse_time(series, utc=False):
    return pd.to_datetime(series, errors="coerce", utc=utc)

def audit_frame(df: pd.DataFrame, source: str, event_start: str, event_end: str) -> dict:
    req = REQUIRED[source]
    missing_fields = [c for c in req if c not in df.columns]
    if missing_fields:
        return {"source":source,"n_rows":len(df),"R1":False,"R5":False,
                "error":"missing_required_fields:"+",".join(missing_fields)}
    tf = TIME_FIELD[source]
    ts = parse_time(df[tf], utc=(source=="EAGLEI"))
    valid = ts.dropna().sort_values()
    null_rates = {c: float(df[c].isna().mean()) for c in req}
    ids = [c for c in ID_FIELDS[source] if c in df.columns]
    dup_rate = float(df.duplicated(subset=ids).mean()) if ids else float(df.duplicated().mean())
    gaps = valid.diff().dt.total_seconds().dropna()
    out = {
        "source":source,
        "n_rows":int(len(df)),
        "t_min": valid.min().isoformat() if len(valid) else None,
        "t_max": valid.max().isoformat() if len(valid) else None,
        "median_dt_s": float(gaps.median()) if len(gaps) else None,
        "p95_dt_s": float(gaps.quantile(.95)) if len(gaps) else None,
        "max_gap_s": float(gaps.max()) if len(gaps) else None,
        "required_field_null_rate_max": max(null_rates.values()) if null_rates else None,
        "required_field_null_rates": null_rates,
        "duplicate_rate": dup_rate,
        "R1": bool(len(valid) == len(df)),
        "R5": True,
    }
    if len(valid):
        if source == "EAGLEI":
            out["R2"] = None
        else:
            es = pd.Timestamp(event_start)
            ee = pd.Timestamp(event_end)
            vmin = valid.min().tz_localize(None) if getattr(valid.min(),"tzinfo",None) else valid.min()
            vmax = valid.max().tz_localize(None) if getattr(valid.max(),"tzinfo",None) else valid.max()
            out["R2"] = bool(vmin <= es and vmax >= ee)
    else:
        out["R2"] = False
    out["R3"] = False if source == "EAGLEI" else None
    return out

def socrata_url(dataset: str, time_field: str, start: str, end: str, fields: list[str], limit=50000, offset=0):
    where = f"{time_field} >= '{start}' AND {time_field} <= '{end}'"
    q = {"$select": ",".join(fields), "$where": where, "$limit": str(limit), "$offset": str(offset), "$order": time_field}
    return f"https://data.cityofnewyork.us/resource/{dataset}.json?{urlencode(q)}"

def fetch_json_pages(dataset, time_field, start, end, fields, session=None):
    session = session or requests.Session()
    rows=[]; offset=0; limit=50000
    while True:
        url=socrata_url(dataset,time_field,start,end,fields,limit,offset)
        r=session.get(url,timeout=120); r.raise_for_status()
        chunk=r.json()
        if not chunk: break
        rows.extend(chunk)
        if len(chunk)<limit: break
        offset += limit
    return pd.DataFrame(rows)

def fetch_nyiso(event, outdir: Path):
    y,m=event["year"],event["month"]
    url=f"https://mis.nyiso.com/public/csv/pal/{y:04d}{m:02d}01pal_csv.zip"
    p=outdir/f"{y:04d}{m:02d}01pal_csv.zip"
    r=requests.get(url,timeout=180); r.raise_for_status(); p.write_bytes(r.content)
    frames=[]
    with zipfile.ZipFile(p) as z:
        for name in sorted(z.namelist()):
            if name.lower().endswith(".csv"):
                frames.append(pd.read_csv(z.open(name)))
    df=pd.concat(frames,ignore_index=True)
    return df[df["Name"].astype(str).str.strip().eq("N.Y.C.")].copy(), p, url

def fetch_tlc(event, outdir: Path):
    y,m=event["year"],event["month"]
    url=f"https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_{y:04d}-{m:02d}.parquet"
    p=outdir/f"fhvhv_tripdata_{y:04d}-{m:02d}.parquet"
    r=requests.get(url,timeout=300); r.raise_for_status(); p.write_bytes(r.content)
    df=pd.read_parquet(p)
    s=pd.Timestamp(event["start"]); e=pd.Timestamp(event["end"])
    t=pd.to_datetime(df["pickup_datetime"],errors="coerce")
    return df[(t>=s)&(t<=e)].copy(), p, url

def load_eaglei(event, eaglei_dir: Path):
    p=eaglei_dir/f"eaglei_outages_{event['year']}.csv"
    df=pd.read_csv(p, dtype={"fips_code":str})
    df["fips_code"]=df["fips_code"].str.zfill(5)
    df=df[df["fips_code"].isin(NYC_FIPS)].copy()
    t=pd.to_datetime(df["run_start_time"],errors="coerce",utc=True)
    s=pd.Timestamp(event["start"],tz="America/New_York").tz_convert("UTC")
    e=pd.Timestamp(event["end"],tz="America/New_York").tz_convert("UTC")
    return df[(t>=s)&(t<=e)].copy(), p

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--event",choices=EVENTS,required=True)
    ap.add_argument("--outdir",default="audit_outputs")
    ap.add_argument("--eaglei-dir",default=None)
    ap.add_argument("--sources",nargs="*",default=["NYISO_P58B","TLC_HVFHV","NYC_DOT_SPEEDS","NYC_311"])
    args=ap.parse_args()
    ev=EVENTS[args.event]; outdir=Path(args.outdir)/args.event; outdir.mkdir(parents=True,exist_ok=True)
    report=[]
    for src in args.sources:
        try:
            local_path=None; source_url=None
            if src=="NYISO_P58B":
                df,local_path,source_url=fetch_nyiso(ev,outdir)
            elif src=="TLC_HVFHV":
                df,local_path,source_url=fetch_tlc(ev,outdir)
            elif src=="NYC_DOT_SPEEDS":
                fields=REQUIRED[src]+["link_points"]
                df=fetch_json_pages("i4gi-tjb9","data_as_of",ev["start"],ev["end"],fields)
                source_url="https://data.cityofnewyork.us/resource/i4gi-tjb9.json"
            elif src=="NYC_311":
                df=fetch_json_pages("erm2-nwe9","created_date",ev["start"],ev["end"],REQUIRED[src])
                source_url="https://data.cityofnewyork.us/resource/erm2-nwe9.json"
            elif src=="EAGLEI":
                if not args.eaglei_dir: raise RuntimeError("--eaglei-dir required for EAGLEI")
                df,local_path=load_eaglei(ev,Path(args.eaglei_dir))
                source_url="doi:10.6084/m9.figshare.24237376"
            else:
                raise ValueError(src)
            metrics=audit_frame(df,src,ev["start"],ev["end"])
            metrics.update({"event_id":args.event,"event_name":ev["name"],"source_url":source_url})
            if local_path:
                metrics["local_file"]=str(local_path)
                metrics["sha256"]=sha256_file(local_path)
            report.append(metrics)
            pd.DataFrame(df).to_parquet(outdir/f"{src}_{args.event}_window.parquet",index=False)
        except Exception as exc:
            report.append({"event_id":args.event,"source":src,"status":"RETRIEVAL_OR_AUDIT_FAILED","error":repr(exc)})
    (outdir/"audit.json").write_text(json.dumps(report,indent=2,default=str))
    print(json.dumps(report,indent=2,default=str))

if __name__=="__main__":
    main()
