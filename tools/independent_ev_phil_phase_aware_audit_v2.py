#!/usr/bin/env python3
"""Phase-aware reanalysis of five separate KIT PHIL original EV U/I CSV experiments.

Corrects the all-3-phase arithmetic mean used in the frozen V1/V1 diagnostic.
The Nissan Leaf CSV shows one energized phase in inspected original rows; confirm
active phases over the full file before comparing its voltage steps to 3-phase EVs.

These are independent controlled laboratory data, NOT original KIT 50-day field
OLTC recordings, and contain neither real active power nor controller command logs.
Source DOI: https://doi.org/10.5281/zenodo.22965111
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np

PHIL = [
    ("Volkswagen ID.4", "01_voltages_current_iD4.csv", "4a985b5a7f1b14e92033aec421df949f"),
    ("Nissan Leaf", "02_voltages_current_Nissann_Leaf.csv", "b6c33f50cf13b42a2a70a2e040318872"),
    ("MG4", "03_voltages_current_MG4.csv", "ec879693acd6edb4a77fd3da69ed9af7"),
    ("Tesla Model 3", "04_voltages_current_Tesla_Model_3.csv", "144bbaaf604555b667a8cd38a6ef0d7c"),
    ("Renault Zoe", "05_voltages_current__Renault_Zoe.csv", "969c1c0203f86d0e1c338c517bd1a0c9"),
]
PHIL_COLS = ["time_s", "U_L1_V", "U_L2_V", "U_L3_V", "I_L1_A", "I_L2_A", "I_L3_A"]
SCREEN_THRESHOLD_V = 2.0


def read_csv(path: Path):
    s=path.read_text(encoding="utf-8-sig")
    return list(csv.DictReader(io.StringIO(s),delimiter=","))


def median_window(t: np.ndarray,y: np.ndarray,a: float,b: float):
    x=y[(t>=a)&(t<b)]
    x=x[np.isfinite(x)]
    return float(np.median(x)) if len(x) else float("nan")


def mad_scale(x: np.ndarray):
    x=x[np.isfinite(x)]
    if not len(x): return float("nan")
    m=np.median(x)
    return float(1.4826*np.median(np.abs(x-m)))


def screen_voltage_events(t: np.ndarray,v: np.ndarray,threshold_v=2.0,min_gap_s=3.0):
    """Legacy V1 detector replicated exactly, now fed ACTIVE-phase mean U."""
    if len(t)<100:return []
    median_dt=float(np.median(np.diff(t)))
    stride=max(1,int(round(.10/median_dt)))
    candidates=[]
    for j in range(0,len(t),stride):
        tj=float(t[j])
        a=median_window(t,v,tj-1.5,tj-.3)
        b=median_window(t,v,tj+.3,tj+1.5)
        if np.isfinite(a) and np.isfinite(b) and abs(b-a)>=threshold_v:
            candidates.append((tj,b-a))
    if not candidates:return []
    groups=[];cur=[candidates[0]]
    for row in candidates[1:]:
        if row[0]-cur[-1][0]>min_gap_s:
            groups.append(cur);cur=[row]
        else:cur.append(row)
    groups.append(cur)
    events=[]
    for group in groups:
        peak=max(abs(x[1]) for x in group)
        peakgroup=[x[0] for x in group if abs(x[1])>=.98*peak]
        events.append(float(np.median(peakgroup)))
    return events


def first_persistent_current_shift(t: np.ndarray,i_mean: np.ndarray,
                                   step_t: float,pre_med: float,
                                   pre_noise: float,dwell_s=.6):
    dt=float(np.median(np.diff(t)))
    n=max(1,int(math.ceil(dwell_s/dt)))
    tolerance=max(.5,5*pre_noise if np.isfinite(pre_noise) else .5)
    starts=np.flatnonzero((t>=step_t)&(t<=step_t+5.))
    for k in starts:
        chunk=i_mean[k:k+n]
        if len(chunk)<n:break
        if np.all(np.isfinite(chunk)) and np.all(np.abs(chunk-pre_med)>=tolerance):
            return round(float(t[k]-step_t),3)
    return None


def active_phase_mask(u: np.ndarray, i: np.ndarray) -> np.ndarray:
    """Flag phases with substantial measured voltage AND charging current.

    Source U and I are per-phase RMS magnitudes; thresholds are data-quality
    screening choices, not physical regulatory limits. Report phase counts.
    """
    if u.shape != i.shape or u.ndim != 2 or u.shape[1] != 3:
        raise ValueError("Expected aligned Nx3 phase signals")
    if not np.all(np.isfinite(u)) or not np.all(np.isfinite(i)):
        raise ValueError("Missing phase signal; manual qualification required")
    maxish_u = np.quantile(np.abs(u), 0.95, axis=0)
    maxish_i = np.quantile(np.abs(i), 0.95, axis=0)
    active = (maxish_u >= 50.0) & (maxish_i >= 0.5)
    if not active.any():
        raise ValueError("No phase simultaneously exhibits voltage and current")
    return active


def phase_aware_signals(u: np.ndarray, i: np.ndarray) -> tuple[np.ndarray,np.ndarray,np.ndarray,np.ndarray]:
    active = active_phase_mask(u, i)
    v = np.mean(u[:,active], axis=1)         # per energized phase [V]
    amps = np.mean(i[:,active], axis=1)      # per energized phase [A]
    va = np.sum(u[:,active]*i[:,active], axis=1)  # VA proxy, NOT real W
    return active, v, amps, va


def finite_summary(x: list[float]) -> float|None:
    return float(np.median(x)) if x else None


def metrics_from_series(name: str, t: np.ndarray, u: np.ndarray,
                        i: np.ndarray, screen_v: float=SCREEN_THRESHOLD_V) -> dict:
    if len(t) < 100 or len(t) != len(u) or len(t) != len(i):
        raise ValueError("Insufficient or misaligned source samples")
    if not np.all(np.isfinite(t)) or not np.all(np.diff(t)>0):
        raise ValueError("Source time must be strictly increasing")
    active,v,amps,va=phase_aware_signals(u,i)
    ignored_three_phase_mean = np.mean(u,axis=1)
    detected = screen_voltage_events(t,v,threshold_v=screen_v)
    legacy_detected = screen_voltage_events(t,ignored_three_phase_mean,threshold_v=screen_v)
    rows=[]
    for k,step in enumerate(detected,1):
        u0=median_window(t,v,step-3.,step-.5)
        u1=median_window(t,v,step+.5,step+3.)
        i0=median_window(t,amps,step-3.,step-.5)
        i1=median_window(t,amps,step+.5,step+3.)
        a0=median_window(t,va,step-3.,step-.5)
        a1=median_window(t,va,step+.5,step+3.)
        if not np.all(np.isfinite([u0,u1,i0,i1,a0,a1])) or u0<=0:
            continue
        presignal=amps[(t>=step-3.) & (t<step-.5)]
        noise=mad_scale(presignal)
        per_phase=[]
        for z in np.flatnonzero(active):
            per_phase.append({"phase":f"L{z+1}",
                "delta_voltage_V":round(median_window(t,u[:,z],step+.5,step+3.)-
                                         median_window(t,u[:,z],step-3.,step-.5),4),
                "delta_current_A":round(median_window(t,i[:,z],step+.5,step+3.)-
                                         median_window(t,i[:,z],step-3.,step-.5),4)})
        rows.append({
            "detected_index":k,
            "inferred_voltage_transition_time_s":round(float(step),4),
            "delta_active_phase_voltage_V":round(u1-u0,4),
            "delta_active_phase_voltage_pct":round((u1/u0-1)*100,4),
            "delta_mean_active_phase_current_A":round(i1-i0,4),
            "delta_active_phase_apparent_power_proxy_VA":round(a1-a0,2),
            "current_pre_MAD_scale_A":round(float(noise),5),
            "first_persistent_current_change_after_inferred_voltage_step_s":
                first_persistent_current_shift(t,amps,step,i0,noise),
            "per_active_phase_deltas":per_phase,
            "qualification":"measured phase U/I response; NOT logged voltage command, real P, or causal control latency",
        })
    near0pre=median_window(t,v,-3.,-.5)
    near0post=median_window(t,v,.5,3.)
    near0ipre=median_window(t,amps,-3.,-.5)
    near0ipost=median_window(t,amps,.5,3.)
    dv=[abs(x["delta_active_phase_voltage_pct"]) for x in rows]
    di=[abs(x["delta_mean_active_phase_current_A"]) for x in rows]
    return {
        "vehicle":name,"sample_count":len(t),"median_dt_s":round(float(np.median(np.diff(t))),5),
        "phase_activity":{"L1":bool(active[0]),"L2":bool(active[1]),"L3":bool(active[2])},
        "n_active_phases":int(active.sum()),
        "active_phase_voltage_range_V":[round(float(v.min()),3),round(float(v.max()),3)],
        "active_phase_current_range_A":[round(float(amps.min()),3),round(float(amps.max()),3)],
        "screen_threshold_V":screen_v,
        "original_V1_all_phase_mean_event_count":len(legacy_detected),
        "phase_aware_event_count":len(rows),
        "near_t0_active_phase_voltage_delta_V":round(float(near0post-near0pre),4)
            if np.isfinite(near0pre) and np.isfinite(near0post) else None,
        "near_t0_active_phase_current_delta_A":round(float(near0ipost-near0ipre),4)
            if np.isfinite(near0ipre) and np.isfinite(near0ipost) else None,
        "median_abs_voltage_change_pct":round(finite_summary(dv),4) if dv else None,
        "median_abs_mean_active_phase_current_change_A":round(finite_summary(di),4) if di else None,
        "number_abs_current_change_ge_0p5A":sum(x>=.5 for x in di),
        "events":rows,
    }


def self_test():
    t=np.round(np.arange(-8.,18.,.02),8)
    volt=np.zeros((len(t),3)); current=np.zeros_like(volt)
    volt[:,0]=230.;current[:,0]=16.
    volt[t>=0.,0]-=5
    r=metrics_from_series("synthetic single phase",t,volt,current)
    assert r["n_active_phases"]==1 and r["phase_activity"]=={"L1":True,"L2":False,"L3":False},r
    assert r["phase_aware_event_count"]>=1 and r["original_V1_all_phase_mean_event_count"]==0,r
    assert abs(r["near_t0_active_phase_voltage_delta_V"]+5.)<.01,r
    volt[:,1:]=volt[:,0,None];current[:,1:]=current[:,0,None]
    r3=metrics_from_series("synthetic three phase",t,volt,current)
    assert r3["n_active_phases"]==3 and r3["phase_aware_event_count"]>=1,r3
    print("PASS: single-phase/three-phase voltage screening and V1 averaging-bias synthetic QA")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache",type=Path,default=Path.home()/"Downloads/Independent_EV_Lab_2026/KIT_PHIL_22965111")
    parser.add_argument("--out",type=Path,default=Path.home()/"Research/MSE-thesis/data/lab_candidates/2026-11-05")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    if args.self_test:
        self_test();return
    trials=[]
    for car,file,md5 in PHIL:
        p=args.cache/file
        if not p.is_file():raise FileNotFoundError(p)
        if hashlib.md5(p.read_bytes()).hexdigest()!=md5:
            raise ValueError("Publisher checksum mismatch: "+file)
        rows=read_csv(p)
        if not rows or list(rows[0])!=PHIL_COLS:raise ValueError("Unexpected phase columns "+file)
        t=np.array([float(r["time_s"]) for r in rows])
        u=np.array([[float(r[f"U_L{k}_V"]) for k in (1,2,3)] for r in rows])
        i=np.array([[float(r[f"I_L{k}_A"]) for k in (1,2,3)] for r in rows])
        result=metrics_from_series(car,t,u,i)
        result["source_filename"]=file
        result["publisher_md5_pass"]=True
        trials.append(result)
        print(f"{car}: {result['n_active_phases']} active phase(s), "
              f"legacy {result['original_V1_all_phase_mean_event_count']} vs "
              f"phase-aware {result['phase_aware_event_count']} voltage candidates, "
              f"near-t0 ΔU {result['near_t0_active_phase_voltage_delta_V']} V, "
              f"near-t0 ΔI {result['near_t0_active_phase_current_delta_A']} A")
    obj={"source":"https://doi.org/10.5281/zenodo.22965111",
         "evidence":"original publisher-MD5-qualified phase U/I laboratory observations",
         "reason_for_v2":"V1 divided single-phase Nissan Leaf voltage step by three by averaging inactive zero channels",
         "claim_limit":"V2 measured change-screen candidates are not verified commands or charger controller logs; apparent-power proxy VA not real W",
         "phase_screen_rule":"95th percentile |U_phase| >= 50 V AND 95th percentile |I_phase| >= 0.5 A across a trial",
         "voltage_step_threshold_V":SCREEN_THRESHOLD_V,"trials":trials}
    args.out.mkdir(parents=True,exist_ok=True)
    pj=args.out/"INDEPENDENT_EV_PHIL_PHASE_AWARE_AUDIT_V2.json"
    pm=args.out/"INDEPENDENT_EV_PHIL_PHASE_AWARE_AUDIT_V2.md"
    pj.write_text(json.dumps(obj,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    lines=["# KIT PHIL five-EV phase-aware quantitative audit — V2", "",
           "**Correction:** Inactive zero phase channels must not dilute single-phase EV RMS voltage/current. V1 is retained unchanged for auditability.",
           "**Source:** https://doi.org/10.5281/zenodo.22965111; all files must pass source MD5.",
           "**Evidence boundary:** U and I measured; VA proxy is not real W; event time inferred, no command-state log; different source from KIT OLTC field.","",
           "| EV | Active phases | V1 mean-all-phase candidates | V2 phase-aware candidates | Near t=0 ΔU (V) | Near t=0 ΔI (A) |",
           "|---|---:|---:|---:|---:|---:|"]
    for row in trials:
        lines.append(f"| {row['vehicle']} | {row['n_active_phases']} | {row['original_V1_all_phase_mean_event_count']} | {row['phase_aware_event_count']} | {row['near_t0_active_phase_voltage_delta_V']} | {row['near_t0_active_phase_current_delta_A']} |")
    lines += ["", "**Event-wise measured voltage and current changes, detector timing and phase-specific changes:** see V2 JSON.",
              "**Causality status:** controlled voltage perturbation test context, but exact source commands and charger state not recorded in these CSVs. No field KIT OLTC event attribution or thermal inference.", ""]
    pm.write_text("\n".join(lines),encoding="utf-8")
    print("JSON:",pj)
    print("Markdown:",pm)

if __name__=="__main__":main()