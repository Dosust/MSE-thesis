#!/usr/bin/env python3
"""KIT EV-point M3: pre-specified matched QUIET periods from existing one-second summaries.

Never treats a matched, observational comparison as causal identification.
No re-reading the multi-GB source measurements. Reference M2/M3 at original
100 ms remains separately preserved in KIT_M2_M3_100MS_MEASUREMENTS_V1.json.
Source: https://doi.org/10.5281/zenodo.22826984
"""
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

import numpy as np

from kit_ev_power_conditioned_voltage_events import FIRST_UTC, load_source_signals

EVENTS = ("2026-03-10T15:32:02+00:00", "2026-03-10T15:55:02+00:00")
WINDOW_BEFORE_S = 20
WINDOW_AFTER_S = 30


def median_valid(x):
    x = np.asarray(x, dtype=float)
    good = x[np.isfinite(x)]
    return float(np.median(good)) if len(good) else float('nan')


def mad_sigma(x):
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    return float(1.4826*np.median(np.abs(x - np.median(x)))) if x.size else float('nan')


def timestamp_index(stamp):
    return int((datetime.fromisoformat(stamp) - FIRST_UTC).total_seconds())


def utc_at(index):
    return (FIRST_UTC + timedelta(seconds=int(index))).isoformat()


def record(i, u20, u400, p):
    """Comparable 1-second M2/M3 metrics on identical pre/post windows in cases/controls."""
    pre_p = p[i-5:i]    # -5,-4,-3,-2,-1
    post_p = p[i+20:i+31] # +20 through +30
    pre_u20 = u20[i-3:i] # -3,-2,-1
    post_u20 = u20[i+1:i+4] # +1,+2,+3
    pre_u400 = u400[i-3:i]
    post_u400 = u400[i+1:i+4]
    base = median_valid(pre_p)
    late = median_valid(post_p)
    ub = median_valid(pre_u20)
    ua = median_valid(post_u20)
    vb = median_valid(pre_u400)
    va = median_valid(post_u400)
    r = {
        'utc': utc_at(i), 'second_index': int(i),
        'p_pre_W': base, 'p_at_W': float(p[i]), 'p_late_W': late,
        'delta_p_W': late-base, 'pre_p_MAD_scale_W': mad_sigma(p[i-20:i]),
        'max_pre_p_deviation_W': float(np.nanmax(np.abs(p[i-20:i]-base))),
        'u20_pre_V': ub, 'u20_post_V': ua,
        'delta_u20_pct': 100*(ua/ub-1),
        'u400_pre_V': vb, 'u400_post_V': va,
        'delta_u400_pct': 100*(va/vb-1),
    }
    return r


def prefix_counters(u20,u400,p,voltage_step_pct):
    """O(N) consecutive-step and finite coverage rejection, reusable for many windows."""
    valid = np.isfinite(u20) & np.isfinite(u400) & np.isfinite(p) & (u20>0) & (u400>0)
    step = np.full(len(u20), np.inf, dtype=float)
    both = np.isfinite(u20[1:]) & np.isfinite(u20[:-1]) & (u20[1:]>0) & (u20[:-1]>0)
    step[1:][both] = 100*np.abs(u20[1:][both]/u20[:-1][both] - 1)
    bad_step = ~np.isfinite(step) | (step>=voltage_step_pct)
    bad_step[0] = True
    bad_valid = ~valid
    return step, np.r_[0,np.cumsum(bad_step,dtype=np.int32)], np.r_[0,np.cumsum(bad_valid,dtype=np.int32)]


def window_count(prefix, idx, left=-WINDOW_BEFORE_S, right=WINDOW_AFTER_S):
    """Inclusive time-of-step indices [i+left, i+right]."""
    return prefix[idx+right+1] - prefix[idx+left]


def base_eligible(i, u20,u400,p,step_prefix,valid_prefix, voltage_step_pct):
    if window_count(valid_prefix, np.array([i]))[0]:
        return False
    if window_count(step_prefix, np.array([i]))[0]:
        return False
    return True


def match_one(event_i, other_events, u20,u400,p,phases, step_prefix, valid_prefix,
              max_controls, step_threshold_pct, control_stride_s):
    event = record(event_i,u20,u400,p)
    phase = phases[event_i].as_py()
    day = (FIRST_UTC+timedelta(seconds=event_i)).date()
    n = len(p)
    candidates = np.arange(WINDOW_BEFORE_S+1,n-WINDOW_AFTER_S-1,control_stride_s,dtype=np.int32)
    # User's case date *and* fault-phase matching are mandatory for primary comparison.
    # Avoid over-calling statistical independence: sample windows separated by at least 60 s.
    datesec0 = int((datetime.combine(day,datetime.min.time(),timezone.utc)-FIRST_UTC).total_seconds())
    datesec1 = datesec0+86400
    candidates = candidates[(candidates>=datesec0+WINDOW_BEFORE_S)&(candidates<datesec1-WINDOW_AFTER_S)]
    n_day = int(len(candidates))
    # Exclude ±180 s around all original hand-selected cases.
    for t in other_events:
        candidates = candidates[np.abs(candidates-int(t))>=180]
    n_far = int(len(candidates))
    if not len(candidates):
        return event,[], {'candidate_strided_same_day':n_day,'after_event_exclusion':0,'quiet_voltage_windows':0,
                           'all_signals_finite_windows':0,'same_source_fault_phase':0,'load_and_voltage_matched':0,
                           'pre_power_stable':0,'selected':0}
    quiet = (window_count(step_prefix,candidates) ==0)
    n_quiet = int(np.sum(quiet))
    candidates = candidates[quiet]
    finite = (window_count(valid_prefix,candidates)==0)
    n_finite = int(np.sum(finite))
    candidates = candidates[finite]
    # Phase check only after bounded voltage and coverage filters.
    candidates=np.array([j for j in candidates if phases[int(j)].as_py()==phase],dtype=np.int32)
    n_phase=int(len(candidates))
    if not len(candidates):
        return event,[],{'candidate_strided_same_day':n_day,'after_event_exclusion':n_far,
                         'quiet_voltage_windows':n_quiet,'all_signals_finite_windows':n_finite,
                         'same_source_fault_phase':n_phase,'load_and_voltage_matched':0,'pre_power_stable':0,'selected':0}
    # Similar reference voltage and nominal EV point loading, both measured in case and controls.
    exposure = event['p_pre_W']
    base_u20=event['u20_pre_V']
    matched=[]
    n_matched=0
    n_stable=0
    for i in candidates:
        cp=median_valid(p[i-5:i]); cv=median_valid(u20[i-3:i])
        if not (np.isfinite(cp) and np.isfinite(cv)):
            continue
        if abs(cp-exposure) > max(100,0.20*abs(exposure)):
            continue
        if abs(cv-base_u20) > 0.02*abs(base_u20):
            continue
        n_matched+=1
        pre=p[i-20:i]
        sigma=mad_sigma(pre)
        if (sigma>max(30,0.05*abs(cp)) or np.max(np.abs(pre-cp))>max(70,0.10*abs(cp))):
            continue
        n_stable+=1
        # Rank by proximity of pre-loading, voltage and time. Never force matches.
        ranking=(abs(cp-exposure)/max(100,abs(exposure)) +
                 0.5*abs(cv-base_u20)/max(1,abs(base_u20)) +
                 0.05*abs(int(i)-event_i)/(4*3600))
        matched.append((ranking,int(i)))
    matched.sort(key=lambda x:(x[0],x[1]))
    chosen=[]
    for _,i in matched:
        if any(abs(i-x)<60 for x in chosen):
            continue
        chosen.append(i)
        if len(chosen)>=max_controls:
            break
    records=[record(i,u20,u400,p) for i in chosen]
    stats={'candidate_strided_same_day':n_day,'after_event_exclusion':n_far,
           'quiet_voltage_windows':n_quiet,'all_signals_finite_windows':n_finite,
           'same_source_fault_phase':n_phase,'load_and_voltage_matched':n_matched,
           'pre_power_stable':n_stable,'selected':len(chosen),
           'matched_case_fault_phase':phase, 'matched_case_date_utc':day.isoformat()}
    return event,records,stats


def contrast(values, actual):
    x=np.asarray(values,dtype=float)
    x=x[np.isfinite(x)]
    if not len(x):
        return {'valid_matched_controls':0,'control_median_delta_W':None,
                'event_minus_control_median_delta_W':None,'fraction_control_abs_delta_ge_event':None}
    return {'valid_matched_controls':int(len(x)),
            'control_median_delta_W':float(np.median(x)),
            'control_delta_q25_q75_W':[float(np.quantile(x,.25)),float(np.quantile(x,.75))],
            'event_minus_control_median_delta_W':float(actual-np.median(x)),
            'fraction_control_abs_delta_ge_event':float(np.mean(np.abs(x)>=abs(actual)))}


def run(u20,u400,p,phases,args):
    step,badstep,badvalid=prefix_counters(u20,u400,p,args.voltage_step_pct)
    results=[]
    known=[timestamp_index(t) for t in EVENTS]
    for t,i in zip(EVENTS,known):
        event,controls,stats=match_one(i,known,u20,u400,p,phases,badstep,badvalid,
                                       args.max_controls,args.voltage_step_pct,args.stride_s)
        comp=contrast([c['delta_p_W'] for c in controls],event['delta_p_W'])
        results.append({'event_utc':t,'event_metrics_1s':event,'matching_audit':stats,
                        'controls_1s':controls, 'matched_comparison':comp,
                        'admissibility':('DESCRIPTIVE_WITHIN_PHASE_AND_DATE_COMPARISON_ONLY' if len(controls)>0 else
                                          'NO_CLEAN_MATCHED_CONTROLS_AVAILABLE')})
    return {
        'source':'https://doi.org/10.5281/zenodo.22826984',
        'analysis_type':'descriptive observational matching; NOT a causal experiment',
        'case_times':list(EVENTS),
        'sampling':'derived measured 1-second averages at BOTH events and controls; NOT comparable as if 100ms',
        'matching_policy':{'same_utc_date':True,'same_source_fault_phase':True,
                           'no_abs_20kV_one_second_step_at_or_above_pct_anywhere_in_window':args.voltage_step_pct,
                           'quiet_window':[-20,30], 'exclude_within_s_of_known_events':180,
                           'power_pre_baseline_window_s':[-5,-1], 'late_post_window_s':[20,30],
                           'voltage_pre_s':[-3,-1], 'voltage_post_s':[1,3],
                           'pre_power_tolerance':'max(100 W, 20% of case pre-power)',
                           'pre_voltage_tolerance_pct':2.0,
                           'control_pre_stability':'MAD scale <= max(30 W, 5% of control pre power); max abs deviation <= max(70 W,10%)',
                           'control_grid_stride_s':args.stride_s,'minimum_selected_control_spacing_s':60,
                           'maximum_controls_per_case':args.max_controls},
        'results':results,
        'limits':['Source 20kV/EV-point direct feeder parentage and charger control logs unverified',
                  'Conventional observed controls cannot identify causal EV power response',
                  'Two selected cases belong to one fault episode and are not independent replications',
                  'Zero selected quiet same-phase same-day controls is a legitimate evidence limitation',
                  'Electrical OLTC anomaly, not an extreme-heat thermal dataset']}


def write_outputs(folder, analysis):
    folder.mkdir(parents=True,exist_ok=True)
    path_json=folder/'KIT_M3_MATCHED_QUIET_CONTROLS_V1.json'
    path_md=folder/'KIT_M3_MATCHED_QUIET_CONTROLS_V1.md'
    path_json.write_text(json.dumps(analysis,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    lines=['# KIT EV-point matched quiet-window comparison (derived 1-second means)',
           '', '**Status:** observed descriptive comparison; NOT evidence of causal voltage-induced change.',
           '**Source:** https://doi.org/10.5281/zenodo.22826984',
           '**Matching:** same source phase, same UTC date and similar pre-event EV load / 20kV voltage; no one-second voltage steps ≥0.15% anywhere from −20 to +30 seconds around the control.',
           '**Consistency:** case metrics recalculated on SAME 1-second grid as controls; original 100-ms M2/M3 metrics remain separately preserved.',
           '', '| Case UTC | Case ΔP (W) | Case ΔU20 (%) | Clean controls (n) | Control median ΔP (W) | Case minus control median (W) |',
           '|---|---:|---:|---:|---:|---:|']
    def fmt(x): return 'n/a' if x is None else f'{x:+.3f}'
    for r in analysis['results']:
        e=r['event_metrics_1s']; c=r['matched_comparison'];n=c['valid_matched_controls']
        lines.append(f"| {r['event_utc']} | {e['delta_p_W']:+.3f} | {e['delta_u20_pct']:+.3f} | {n} | {fmt(c['control_median_delta_W'])} | {fmt(c['event_minus_control_median_delta_W'])} |")
        lines.extend(['',f"## Event {r['event_utc']}",
                      f"- Phase: {r['matching_audit'].get('matched_case_fault_phase','not evaluated')}",
                      f"- Availability/rejections: {json.dumps(r['matching_audit'])}",
                      f"- Status: **{r['admissibility']}**",''])
    lines.extend(['**Scientific limit:** Co-variation is not physical feeder verification or an identified voltage effect. This dataset lacks verified EVSE commands/charge status and thermal/service measurements.',
                  '**Decision:** if clean matches do not exist during the OLTC recurring-steps episode, report the absence rather than relax criteria after seeing outcomes. A separate controlled PHIL dataset can test voltage-driven device behavior, but cannot be merged as same feeder.', ''])
    path_md.write_text('\n'.join(lines),encoding='utf-8')
    return path_json,path_md


def self_test():
    n=1000
    u20=np.full(n,12000.,dtype=float)
    u400=np.full(n,237.,dtype=float)
    p=np.full(n,1000.,dtype=float)
    u20[500:550]=11900.
    p[510:]=1300.
    step,bad,badv=prefix_counters(u20,u400,p,.15)
    assert step[500]>=.15
    assert window_count(bad,np.array([500]))[0]>0
    assert window_count(bad,np.array([200]))[0]==0
    assert base_eligible(200,u20,u400,p,bad,badv,.15)
    assert not base_eligible(500,u20,u400,p,bad,badv,.15)
    r=record(500,u20,u400,p)
    assert abs(r['p_pre_W']-1000.)<1e-9 and abs(r['p_late_W']-1300.)<1e-9
    assert abs(r['delta_p_W']-300.)<1e-9
    assert contrast([0.,10.,-10.],300.)['valid_matched_controls']==3
    print('PASS: synthetic quiet-control/exposure exclusions and same-grid M2/M3 metrics (NOT measured KIT outcome)')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--folder',type=Path,default=Path.home()/'Downloads/KIT_OLTC_Electrical_Results')
    ap.add_argument('--out',type=Path,default=Path.home()/'Research/MSE-thesis/data/field_candidates/2026-11-05')
    ap.add_argument('--voltage-step-pct',type=float,default=.15)
    ap.add_argument('--stride-s',type=int,default=5)
    ap.add_argument('--max-controls',type=int,default=30)
    ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args()
    if args.self_test:
        self_test();return
    if args.voltage_step_pct<=0 or args.stride_s<1 or args.max_controls<1:
        ap.error('Threshold, stride and cap must be positive')
    u20,_,u400,p,phases=load_source_signals(args.folder)
    result=run(u20,u400,p,phases,args)
    pj,pm=write_outputs(args.out,result)
    print('=== KIT MATCHED QUIET PERIODS (1s measured source) ===')
    for r in result['results']:
        e=r['event_metrics_1s']; stat=r['matching_audit'];c=r['matched_comparison']
        print('Event:',r['event_utc'])
        print('  Case ΔP (W):',round(e['delta_p_W'],3),'case ΔU20 (%):',round(e['delta_u20_pct'],3))
        print('  Same-day quiet windows:',stat['quiet_voltage_windows'])
        print('  Same-source-phase quiet windows:',stat['same_source_fault_phase'])
        print('  Stable load/voltage matched windows:',stat['pre_power_stable'])
        print('  Selected controls:',stat['selected'])
        print('  Control median ΔP (W):',c['control_median_delta_W'])
        print('  Case minus control median ΔP (W):',c['event_minus_control_median_delta_W'])
        print('  Evidence:',r['admissibility'])
    print('JSON:',pj)
    print('Markdown:',pm)
    print('LIMIT: descriptive matched comparison; neither a feeder-specific causal effect nor thermal validation')

if __name__=='__main__':
    main()