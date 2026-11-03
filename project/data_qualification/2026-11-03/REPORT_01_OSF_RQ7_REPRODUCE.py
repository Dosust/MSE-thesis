#!/usr/bin/env python3
"""Exploratory OSF 94GKC battery-terminal response screen, Report 1 RQ7.
Reads ORIGINAL outer ZIP with an embedded original research ZIP.
Do NOT interpret results as charger AC power, causality, rectifier heat or field resilience.
Usage: python REPORT_01_OSF_RQ7_REPRODUCE.py --source OSF_original_outer.zip
Requires: pandas numpy.
"""
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
import argparse, hashlib, json, re
import numpy as np
import pandas as pd

COLUMNS=["Time [s]","HV_Battery_Current [A]","HV_Battery_Voltage [V]"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--output_prefix",default="REPORT_01_OSF_RQ7")
    a=ap.parse_args()
    data=Path(a.source).read_bytes()
    sha=hashlib.sha256(data).hexdigest()
    rows=[]
    counts={"all_csv":0,"name_duration_and_start20_2to30s":0,
            "missing_columns":0,"no_valid_rows":0,
            "inadequate_pre_or_event_points":0,"inactive_precharge":0}
    with ZipFile(BytesIO(data)) as outer:
        inner_name=next(x for x in outer.namelist()
                        if x.startswith("High-resolution") and x.endswith(".zip"))
        with ZipFile(BytesIO(outer.read(inner_name))) as z:
            files=[f for f in z.namelist() if f.endswith(".csv")]
            counts["all_csv"]=len(files)
            for name in files:
                match=re.search(r"duration[_ ]?([0-9.]+)s",name,re.I)
                if not match or not re.search("_start_20",name,re.I):continue
                duration=float(match.group(1))
                if duration<2 or duration>30:continue
                counts["name_duration_and_start20_2to30s"]+=1
                d=pd.read_csv(BytesIO(z.read(name)),usecols=lambda col:col in COLUMNS)
                if len(d.columns)<3:
                    counts["missing_columns"]+=1;continue
                t=pd.to_numeric(d["Time [s]"],errors="coerce").to_numpy()
                current=pd.to_numeric(d["HV_Battery_Current [A]"],errors="coerce").to_numpy()
                voltage=pd.to_numeric(d["HV_Battery_Voltage [V]"],errors="coerce").to_numpy()
                good=(np.isfinite(t)&np.isfinite(current)&np.isfinite(voltage)&
                      (voltage>200)&(voltage<1000)&(np.abs(current)<600))
                if not good.any():
                    counts["no_valid_rows"]+=1;continue
                pre=good&(t>=10)&(t<20)
                during=good&(t>=20)&(t<20+duration)
                if pre.sum()<30 or during.sum()<20:
                    counts["inadequate_pre_or_event_points"]+=1;continue
                power=np.abs(current*voltage)/1000
                pre_p=float(np.median(power[pre]))
                event_p=float(np.median(power[during]))
                pre_current=float(np.median(np.abs(current[pre])))
                event_current=float(np.median(np.abs(current[during])))
                if pre_p<0.5 or pre_current<1:
                    counts["inactive_precharge"]+=1;continue
                rows.append({"file":name,"class":name.split("/")[0],
                   "duration_s":duration,
                   "n_pre":int(pre.sum()),"n_event":int(during.sum()),
                   "pre_median_batt_kW":pre_p,
                   "event_median_batt_kW":event_p,
                   "delta_batt_kW":event_p-pre_p,
                   "percent_delta_batt_power":100*(event_p-pre_p)/pre_p,
                   "delta_current_A":event_current-pre_current,
                   "pre_median_current_A":pre_current,
                   "event_median_current_A":event_current})
    counts["accepted_windows"]=len(rows)
    d=pd.DataFrame(rows)
    if d.empty:raise ValueError("No qualified event windows")
    csv_out=a.output_prefix+"_event_responses.csv"
    d.to_csv(csv_out,index=False)
    table=[]
    for klass,x in d.groupby("class"):
        y=x["percent_delta_batt_power"]
        table.append({"class":klass,"n_experiments":int(len(x)),
                      "median_pct_change":float(y.median()),
                      "q25":float(y.quantile(.25)),
                      "q75":float(y.quantile(.75))})
    table.sort(key=lambda x:x["n_experiments"],reverse=True)
    y=d["percent_delta_batt_power"]
    results={"source_SHA256":sha,"counts":counts,
        "overall":{"median_pct_change":float(y.median()),
          "q25":float(y.quantile(.25)),"q75":float(y.quantile(.75)),
          "decrease_ge_5_pct_count":int((y<=-5).sum())},
        "by_class":table,
        "method":"Event starts at 20s inferred from name; duration 2-30s; pre [10,20); during [20,20+duration); simultaneous valid V/I; per-file median |VI| change.",
        "critical_limitations":[
         "Filename time is not author-verified synchronized disturbance timestamp.",
         "Not a causal effect or independently matched control-group contrast.",
         "Absolute battery terminal power is not AC charger input power.",
         "No measured EVSE internal temperature, transformer thermal series, extreme heat or coupled mobility service.",
         "Short events and nonstandard schemas are intentionally excluded."]}
    with open(a.output_prefix+"_summary.json","w") as f:json.dump(results,f,indent=2)
    print(json.dumps(results,indent=2))

if __name__=="__main__":main()
