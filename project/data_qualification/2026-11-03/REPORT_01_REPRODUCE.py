#!/usr/bin/env python3
"""Reproduce selected Report 1 RQ1-RQ5 statistics from original source files.
No new numerical conclusions are generated for RQ6/RQ7 without raw inputs.
Requires pandas numpy scipy openpyxl; does not modify originals.
"""
import argparse, hashlib, io, json, zipfile
import numpy as np
import pandas as pd
from scipy.optimize import lsq_linear

HASH={'sintef':'5d81840a2f901f04fded98c3e1097b6e',
      'p':'6a7fce6170230bcc73b69ba745509dad',
      'q':'7b8a9a608b0489c6227ced8cceb08a59'}
def check(path,key):
    with open(path,'rb') as f: digest=hashlib.md5(f.read()).hexdigest()
    if digest!=HASH[key]:raise ValueError(f'{key}: publisher MD5 mismatch')
def metrics(y,p):
    e=np.asarray(y)-np.asarray(p)
    return {'n':len(e),'rmse':float(np.sqrt(np.mean(e*e))),
            'mae':float(np.mean(np.abs(e)))}
def main():
    ap=argparse.ArgumentParser()
    for x in ('sintef','p','q','evzip'):ap.add_argument('--'+x,required=True)
    a=ap.parse_args()
    for k in ('sintef','p','q'):check(getattr(a,k),k)
    d=pd.read_csv(a.sintef,parse_dates=['Timestamp'])
    T=d['Top oil [degC]'].to_numpy()
    Ta=d['Ambient [degC]'].to_numpy()
    I=d['Current [A]'].to_numpy()
    r1={'r_T_oil_ambient':float(np.corrcoef(T,Ta)[0,1]),
        'r_T_oil_current_squared':float(np.corrcoef(T,I**2)[0,1])}
    tm=d.Timestamp
    valid=((tm.shift(-1)-tm)==pd.Timedelta(hours=1)).to_numpy()
    train=valid & (tm<pd.Timestamp('2024-07-01')).to_numpy()
    cal=valid & (tm>=pd.Timestamp('2024-07-01')).to_numpy() & (tm<pd.Timestamp('2024-10-01')).to_numpy()
    test=valid & (tm>=pd.Timestamp('2024-10-01')).to_numpy()
    Iref=float(np.median(I[train]))
    X=np.column_stack((Ta-T,(I/Iref)**2,np.ones(len(d))))
    y=np.roll(T,-1)-T
    fit=lsq_linear(X[train],y[train],bounds=([0,0,0],[1,np.inf,np.inf]))
    pred=T+X@fit.x
    r2={'coefficients':fit.x.tolist(),'Iref_A':Iref,
        'holdout_model':metrics(np.roll(T,-1)[test],pred[test]),
        'holdout_persistence':metrics(np.roll(T,-1)[test],T[test]),
        'calibration_q95_abs_residual_C':float(np.quantile(np.abs(np.roll(T,-1)[cal]-pred[cal]),.95))}
    p=pd.read_csv(a.p,parse_dates=['timestamp'])
    q=pd.read_csv(a.q,parse_dates=['timestamp'])
    assert list(p.columns)==list(q.columns) and p.timestamp.equals(q.timestamp)
    cols=p.columns[1:]
    r3={'time_intervals':len(p),'stations':len(cols),'paired_station_intervals':len(p)*len(cols),
        'negative_P_fraction':float((p[cols]<0).to_numpy().mean()),
        'negative_Q_fraction':float((q[cols]<0).to_numpy().mean()),
        'maximum_signed_P_source_units':float(p[cols].max().max())}
    z=zipfile.ZipFile(a.evzip);tests={}
    for fn in ['Figure6_AC1.csv','Figure6_AC2.csv','Figure7_AC1.csv','Figure7_AC2.csv']:
        x=pd.read_csv(io.BytesIO(z.read(fn)))
        t=pd.to_datetime(x.timestamps,utc=True)
        tests[fn]={'rows':len(x),
                   'backward_time_steps':int((t.diff()<pd.Timedelta(0)).sum()),
                   'median_line_power_source':float(x.ChargeLinePower264.median()),
                   'median_batt_voltage_V':float(x.BattVoltage132.median()),
                   'soc_first120_pct':float(x.SOCave292.head(120).median()),
                   'soc_last120_pct':float(x.SOCave292.tail(120).median()),
                   'tmax_first120_C':float(x.BMSmaxPackTemperature.head(120).median()),
                   'tmax_last120_C':float(x.BMSmaxPackTemperature.tail(120).median())}
    dc={}
    for sh in ['EV1_DC1','EV1_DC2']:
        x=pd.read_excel(io.BytesIO(z.read('Figure10.xlsx')),sheet_name=sh)
        mask=(x['AC power']>30000)&(x['DC power']>20000)
        ac=x.loc[mask,'AC power'];out=x.loc[mask,'DC power']
        dc[sh]={'n':int(mask.sum()),'median_DC_AC_ratio':float((out/ac).median()),
                'median_AC_minus_DC_kW':float((ac-out).median()/1000)}
    print(json.dumps({'RQ1':r1,'RQ2':r2,'RQ3':r3,'RQ4':tests,'RQ5':dc,
                      'RQ6':'not independently run without raw OPSD rows',
                      'RQ7':'not independently run without raw OSF experiment files'},indent=2))
if __name__=='__main__':main()
