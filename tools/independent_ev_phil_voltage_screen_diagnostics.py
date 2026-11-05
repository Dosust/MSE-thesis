#!/usr/bin/env python3
"""Non-destructive KIT PHIL screening-sensitivity audit from locally verified 20ms CSVs.

This checks whether Nissan Leaf's zero 2V detected events reflects insufficient
voltage variation or a detector/window problem. Uses cached original files only.
Does not change the prior V1 result or merge separate experiments.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from independent_ev_lab_voltage_control_audit import PHIL, PHIL_COLS, read_csv, screen_voltage_events

THRESHOLDS_V = (0.5, 1.0, 1.5, 2.0, 3.0, 5.0)

def series_stats(t, u, i):
    if not (len(t) >= 100 and len(t) == len(u) == len(i)):
        raise ValueError('Insufficient/misaligned samples')
    if not np.all(np.isfinite(t)) or not np.all(np.diff(t)>0):
        raise ValueError('Nonmonotonic or missing sample times')
    v=u.mean(axis=1); amps=i.mean(axis=1)
    dt=float(np.median(np.diff(t)))
    lag=max(1,int(round(1.0/dt)))
    idx=int(np.argmax(np.abs(v[lag:]-v[:-lag])))+lag
    n={str(k):len(screen_voltage_events(t,v,threshold_v=k)) for k in THRESHOLDS_V}
    def med(a,lo,hi):
        x=a[(t>=lo)&(t<hi)];return float(np.median(x)) if len(x) else None
    pre_u,post_u=med(v,-3,-.5),med(v,.5,3)
    pre_i,post_i=med(amps,-3,-.5),med(amps,.5,3)
    range_u=float(np.max(v)-np.min(v))
    label=('NO_2V_EVENTS_DESPITE_GT_2V_RUN_RANGE_REQUIRES_SCREEN_QA'
           if n['2.0']==0 and range_u>=2 else
           'NO_2V_EVENTS_WITH_LT_2V_RUN_RANGE' if n['2.0']==0 else
           'TWO_VOLT_EVENT_SCREEN_RETURNED_CANDIDATES')
    return dict(n_samples=len(t),median_dt_s=round(dt,6),
                mean_phase_voltage_range_V=[round(float(np.min(v)),4),round(float(np.max(v)),4)],
                mean_phase_current_range_A=[round(float(np.min(amps)),4),round(float(np.max(amps)),4)],
                max_mean_phase_voltage_span_V=round(range_u,4),
                largest_1s_voltage_change_V=round(float(v[idx]-v[idx-lag]),4),
                largest_1s_voltage_change_target_time_s=round(float(t[idx]),3),
                screen_candidate_counts_at_V_thresholds=n,
                pre_near_t0_voltage_V=pre_u,post_near_t0_voltage_V=post_u,
                near_t0_voltage_delta_V=None if pre_u is None or post_u is None else round(post_u-pre_u,4),
                near_t0_current_delta_A=None if pre_i is None or post_i is None else round(post_i-pre_i,5),
                interpretation=label)

def test():
    t=np.arange(-6,12,.02)
    u=np.full((len(t),3),230.)
    i=np.full((len(t),3),15.)
    u[t>=0]-=5
    a=series_stats(t,u,i)
    assert a['screen_candidate_counts_at_V_thresholds']['2.0']>=1,a
    assert a['largest_1s_voltage_change_V'] <=-4.99,a
    b=series_stats(t,np.full_like(u,230.),i)
    assert b['screen_candidate_counts_at_V_thresholds']['2.0']==0,b
    print('PASS: independent PHIL voltage-screen diagnostic synthetic self-test (NOT measured KIT PHIL)')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--self-test',action='store_true')
    p.add_argument('--cache',type=Path,default=Path.home()/'Downloads/Independent_EV_Lab_2026/KIT_PHIL_22965111')
    p.add_argument('--out',type=Path,default=Path.home()/'Research/MSE-thesis/data/lab_candidates/2026-11-05')
    a=p.parse_args()
    if a.self_test:
        test();return
    out=[]
    for car,name,expected in PHIL:
        path=a.cache/name
        if not path.is_file():
            raise FileNotFoundError(f'Verified source cache not found: {path}')
        actual=hashlib.md5(path.read_bytes()).hexdigest()
        if actual!=expected:
            raise ValueError(f'Publisher checksum mismatch: {name}')
        rows=read_csv(path)
        if not rows or list(rows[0])!=PHIL_COLS:
            raise ValueError(f'Unexpected columns in {name}')
        t=np.array([float(r['time_s']) for r in rows])
        u=np.array([[float(r[f'U_L{k}_V']) for k in (1,2,3)] for r in rows])
        i=np.array([[float(r[f'I_L{k}_A']) for k in (1,2,3)] for r in rows])
        record=series_stats(t,u,i)
        record.update(vehicle=car,file=name,publisher_md5_verified=True)
        out.append(record)
        print(f"{car}: voltage span {record['max_mean_phase_voltage_span_V']} V; screen 0.5/1/1.5/2/3/5V -> "+
              '/'.join(str(v) for v in record['screen_candidate_counts_at_V_thresholds'].values())+
              f"; voltage at t=0 Δ {record['near_t0_voltage_delta_V']} V; {record['interpretation']}")
    result={'source':'https://doi.org/10.5281/zenodo.22965111',
            'status':'MEASURED_SCREEN_SENSITIVITY_ONLY_NOT_COMMAND_LOG_OR_CAUSAL_DELAY',
            'screens_in_volts':list(THRESHOLDS_V),
            'limits':['Original CSV contains phase RMS voltage/current but not measured active power, actual charger state or command time',
                      'A detector count is not a count of confirmed experimental commands',
                      'Separate laboratory from 50-day KIT field study'],
            'vehicles':out}
    a.out.mkdir(parents=True,exist_ok=True)
    jp=a.out/'INDEPENDENT_EV_PHIL_VOLTAGE_SCREEN_DIAGNOSTICS_V1.json'
    mp=a.out/'INDEPENDENT_EV_PHIL_VOLTAGE_SCREEN_DIAGNOSTICS_V1.md'
    jp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    lines=['# KIT independent PHIL voltage-screen sensitivity audit','','**Distinct from the 50-day KIT campus field data.**','',
           '| Vehicle | Whole-run mean voltage span (V) | Screened 2 V transitions | Pre/post near t=0 ΔU (V) | Qualification |',
           '|---|---:|---:|---:|---|']
    for r in out:
        lines.append(f"| {r['vehicle']} | {r['max_mean_phase_voltage_span_V']:.3f} | {r['screen_candidate_counts_at_V_thresholds']['2.0']} | {r['near_t0_voltage_delta_V']} | {r['interpretation']} |")
    lines.extend(['','See JSON for thresholds 0.5, 1.0, 1.5, 2.0, 3.0 and 5.0 V, per-vehicle sample coverage and largest 1 s voltage change.','',
                  'A zero at the 2 V screen is NOT by itself a finding of no voltage perturbation, charging interruption, or a particular car controller response.',''])
    mp.write_text('\n'.join(lines))
    print('JSON:',jp)
    print('Markdown:',mp)
if __name__=='__main__':main()