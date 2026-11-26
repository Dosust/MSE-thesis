#!/usr/bin/env python3
"""Descriptive KU Leuven charging thermal diagnosis; never infer cooling state from correlations."""
import argparse,collections,csv,hashlib,io,json,zipfile
from pathlib import Path
import numpy as np
import pandas as pd

KEEP=['Timestamp','RawBattCurrent132','BattVoltage132','SOCave292','BMSminPackTemperature','BMSmaxPackTemperature','VCFRONT_tempAmbient', 'BMS_preconditionAllowed','UI_batteryPreconditioningRequest','ChargeLinePower264','FC_dcCurrent','FC_dcVoltage']

def run(archive,out):
 out=Path(out);out.mkdir(exist_ok=True,parents=True); rows=[]
 with zipfile.ZipFile(archive) as outer:
  with outer.open('BEV energy dynamic data_V2.zip') as fh:
   with zipfile.ZipFile(fh) as inner:
    files=sorted([n for n in inner.namelist() if '/fast charging sessions/' in n and n.endswith('.csv')])
    for fn in files:
     b=inner.read(fn)
     raw=pd.read_csv(io.BytesIO(b),low_memory=False)
     cols=[x for x in KEEP if x in raw.columns]
     d=raw[cols].copy();n=len(d)
     d['Timestamp']=pd.to_datetime(d['Timestamp'],utc=True,errors='coerce')
     for col in cols:
      if col!='Timestamp':d[col]=pd.to_numeric(d[col],errors='coerce')
     essential=['Timestamp','RawBattCurrent132','BMSminPackTemperature','BMSmaxPackTemperature','VCFRONT_tempAmbient','SOCave292']
     d=d.dropna(subset=essential).sort_values('Timestamp').drop_duplicates('Timestamp')
     t=d['Timestamp'].astype('int64').to_numpy()/1e9
     gaps=np.diff(t) if len(t)>1 else np.array([])
     gap_episodes=int(np.sum(gaps>2)+1) if len(t) else 0
     if len(d):
      span=d['BMSmaxPackTemperature']-d['BMSminPackTemperature']
      corr=[]
      for key in ['RawBattCurrent132','VCFRONT_tempAmbient','SOCave292']:
       cc=d[key].corr(d['BMSmaxPackTemperature']);corr.append(float(cc) if pd.notna(cc) else None)
      pre=[]
      for key in ['BMS_preconditionAllowed','UI_batteryPreconditioningRequest']:
       if key in d.columns:
        v=d[key].dropna();pre.append({'name':key,'present_rows':int(len(v)),'unique_values':sorted(set(map(float,v.unique())))[:12]})
      rec={'file':Path(fn).name,'vehicle':Path(fn).name.split('_')[0], 'sha256':hashlib.sha256(b).hexdigest(),
        'raw_rows':n,'complete_rows':len(d),'gap_intervals_gt_2sec':int(np.sum(gaps>2)), 'episodes':gap_episodes,
        'min_max_sensor_spread_median_C':float(span.median()), 'min_max_sensor_spread_max_C':float(span.max()),
        'max_sensor_min_C':float(d['BMSmaxPackTemperature'].min()),'max_sensor_max_C':float(d['BMSmaxPackTemperature'].max()),
        'max_sensor_delta_end_minus_start_C':float(d['BMSmaxPackTemperature'].iloc[-1]-d['BMSmaxPackTemperature'].iloc[0]),
        'I_min':float(d['RawBattCurrent132'].min()),'I_max':float(d['RawBattCurrent132'].max()),
        'SOC_start_pct':float(d['SOCave292'].iloc[0]),'SOC_end_pct':float(d['SOCave292'].iloc[-1]),
        'ambient_min_C':float(d['VCFRONT_tempAmbient'].min()),'ambient_max_C':float(d['VCFRONT_tempAmbient'].max()),
        'corr_Tmax_I':corr[0],'corr_Tmax_ambient':corr[1],'corr_Tmax_SOC':corr[2],
        'preconditioning_fields':json.dumps(pre),
        'power_note':'FC_dcCurrent*FC_dcVoltage candidate electrical product; original scale, sign and measurement boundary unverified'}
      rows.append(rec)
 outcsv=out/'dc_session_diagnostics.csv'
 with outcsv.open('w',newline='') as fp:
  w=csv.DictWriter(fp,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summary={'dc_sessions':len(rows),'complete_rows_total':sum(r['complete_rows'] for r in rows),
   'median_pack_sensor_spread_C':float(np.median([r['min_max_sensor_spread_median_C'] for r in rows])),
   'sessions_with_multiple_contiguous_episodes':sum(r['episodes']>1 for r in rows),
   'note':'Descriptive exploratory associations are not proof of cooling, causation, sensor identity or battery physical parameters.'}
 (out/'dc_diagnostic_summary.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps(summary,indent=2));return summary

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--archive',required=True);a.add_argument('--out',required=True);args=a.parse_args();run(args.archive,args.out)
