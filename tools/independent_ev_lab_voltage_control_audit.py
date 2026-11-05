#!/usr/bin/env python3
"""Audit independent KIT 20 ms PHIL voltage/current trials and Dortmund controller metadata.

Sources (different laboratories/experiments, NOT the KIT 50-day OLTC field):
  KIT PHIL: https://doi.org/10.5281/zenodo.22965111
  Dortmund: https://doi.org/10.5281/zenodo.14065331

Only measured phase voltage/current are present in the KIT PHIL CSVs.
Apparent-power proxy Σ(U_RMS * I_RMS) is VA, NOT real active power W.
All event times are inferred from measured U, not independently logged commands.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import statistics
import time
import urllib.request
import urllib.error
import subprocess
from pathlib import Path

import numpy as np

PHIL_RECORD = "https://zenodo.org/records/22965111/files/"
DORT_RECORD = "https://zenodo.org/records/14065331/files/"
PHIL = [
    ("Volkswagen ID.4", "01_voltages_current_iD4.csv", "4a985b5a7f1b14e92033aec421df949f"),
    ("Nissan Leaf", "02_voltages_current_Nissann_Leaf.csv", "b6c33f50cf13b42a2a70a2e040318872"),
    ("MG4", "03_voltages_current_MG4.csv", "ec879693acd6edb4a77fd3da69ed9af7"),
    ("Tesla Model 3", "04_voltages_current_Tesla_Model_3.csv", "144bbaaf604555b667a8cd38a6ef0d7c"),
    ("Renault Zoe", "05_voltages_current__Renault_Zoe.csv", "969c1c0203f86d0e1c338c517bd1a0c9"),
]
DORT_METADATA = [
    ("parameters.csv", "55a479a1a34114a81da6bbc233cda419"),
    ("measurements.csv", "332378d8e25b2edf808f3f05a610fdc1"),
]
PHIL_COLS = ["time_s", "U_L1_V", "U_L2_V", "U_L3_V",
             "I_L1_A", "I_L2_A", "I_L3_A"]


def fetch_https_bytes(url: str) -> bytes:
    """Secure HTTPS download with macOS trust-store fallback.

    Some python.org macOS Python builds lack a configured CA certificate
    bundle, although the operating system curl verifies TLS correctly.
    Never turn off certificate checks. Publisher MD5 is verified by caller.
    """
    request = urllib.request.Request(url, headers={
        "User-Agent": "ThesisMeasuredEvidenceAudit/1.0 (noncommercial academic research)",
    })
    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            return response.read()
    except urllib.error.URLError as exc:
        if "CERTIFICATE_VERIFY_FAILED" not in str(exc):
            raise
        print("Python CA bundle unavailable; retrying with macOS curl "
              "(TLS verification ENABLED).", flush=True)
        try:
            cmd = [
                "/usr/bin/curl", "--fail", "--location",
                "--silent", "--show-error", "--retry", "2",
                "--connect-timeout", "15", "--max-time", "120",
                "--proto", "=https", "--proto-redir", "=https", url,
            ]
            done = subprocess.run(cmd, capture_output=True, check=True, timeout=150)
            return done.stdout
        except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as curl_exc:
            raise RuntimeError(
                "Secure macOS curl also failed. Check internet access and "
                "macOS certificate settings; TLS verification remains enabled."
            ) from curl_exc


def download_verified(folder: Path, name: str, md5: str, base: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    if path.exists() and hashlib.md5(path.read_bytes()).hexdigest() == md5:
        return path
    url = base + name + "?download=1"
    last = None
    for attempt in range(3):
        try:
            payload = fetch_https_bytes(url)
            actual = hashlib.md5(payload).hexdigest()
            if actual != md5:
                raise ValueError(f"Source checksum mismatch for {name}: expected {md5}, got {actual}")
            path.write_bytes(payload)
            return path
        except Exception as exc:
            last = exc
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Cannot retrieve and verify {name} from {url}: {last}")


def read_csv(path: Path) -> list[dict]:
    s = path.read_text(encoding="utf-8-sig")
    sample = s[:4096]
    try:
        delim = csv.Sniffer().sniff(sample, delimiters=",;\t").delimiter
    except csv.Error:
        delim = ","
    return list(csv.DictReader(io.StringIO(s), delimiter=delim))


def median_window(t: np.ndarray, y: np.ndarray, a: float, b: float) -> float:
    segment = y[(t >= a) & (t < b)]
    segment = segment[np.isfinite(segment)]
    return float(np.median(segment)) if len(segment) else float("nan")


def mad_scale(x: np.ndarray) -> float:
    x = x[np.isfinite(x)]
    if not len(x):
        return float("nan")
    m = np.median(x)
    return float(1.4826 * np.median(np.abs(x - m)))


def screen_voltage_events(t: np.ndarray, v: np.ndarray, threshold_v: float = 2.0,
                          min_gap_s: float = 3.0) -> list[float]:
    """Screen multi-second plateau-level transitions, not commanded event timestamps.

    The relative time is a *measured-voltage* transition estimate; gradual ramps
    and overlapping short disturbances can shift/merge candidates. No causal lag.
    """
    if len(t) < 100:
        return []
    median_dt = float(np.median(np.diff(t)))
    stride = max(1, int(round(0.10 / median_dt)))
    candidates = []
    for j in range(0, len(t), stride):
        tj = float(t[j])
        a = median_window(t, v, tj-1.5, tj-0.3)
        b = median_window(t, v, tj+0.3, tj+1.5)
        if np.isfinite(a) and np.isfinite(b) and abs(b-a) >= threshold_v:
            candidates.append((tj, b-a))
    if not candidates:
        return []
    groups = []
    cur = [candidates[0]]
    for row in candidates[1:]:
        if row[0] - cur[-1][0] > min_gap_s:
            groups.append(cur)
            cur = [row]
        else:
            cur.append(row)
    groups.append(cur)
    events = []
    for group in groups:
        peak = max(abs(x[1]) for x in group)
        peakgroup = [x[0] for x in group if abs(x[1]) >= 0.98*peak]
        events.append(float(np.median(peakgroup)))
    return events


def first_persistent_current_shift(t: np.ndarray, i_mean: np.ndarray,
                                   step_t: float, pre_med: float,
                                   pre_noise: float, dwell_s: float = 0.6):
    dt = float(np.median(np.diff(t)))
    n = max(1, int(math.ceil(dwell_s / dt)))
    tolerance = max(0.5, 5.0 * pre_noise if np.isfinite(pre_noise) else 0.5)
    starts = np.flatnonzero((t >= step_t) & (t <= step_t+5.0))
    for k in starts:
        chunk = i_mean[k:k+n]
        if len(chunk) < n:
            break
        if np.all(np.isfinite(chunk)) and np.all(np.abs(chunk-pre_med) >= tolerance):
            return round(float(t[k]-step_t), 3)
    return None


def analyze_signals(name: str, t: np.ndarray, voltage: np.ndarray,
                    current: np.ndarray, threshold_v: float = 2.0) -> dict:
    """Each voltage/current array has three columns in L1/L2/L3 order."""
    if voltage.shape != current.shape or voltage.shape != (len(t), 3):
        raise ValueError("Expected aligned Nx3 phase arrays")
    if len(t) < 100 or not np.all(np.isfinite(t)) or not np.all(np.diff(t) > 0):
        raise ValueError("Expected monotonic finite time with >=100 rows")
    if not np.all(np.isfinite(voltage)) or not np.all(np.isfinite(current)):
        raise ValueError("Nonfinite voltage or current: qualify missingness before calculation")
    vmean = voltage.mean(axis=1)
    imean = current.mean(axis=1)
    apparent = np.sum(voltage * current, axis=1)  # VA, NOT true active power.
    events = []
    for k, step in enumerate(screen_voltage_events(t, vmean, threshold_v)):
        a = step-3.0
        b = step-0.5
        c = step+0.5
        d = step+3.0
        u_pre = median_window(t, vmean, a, b)
        u_post = median_window(t, vmean, c, d)
        i_pre = median_window(t, imean, a, b)
        i_post = median_window(t, imean, c, d)
        s_pre = median_window(t, apparent, a, b)
        s_post = median_window(t, apparent, c, d)
        if not np.all(np.isfinite([u_pre,u_post,i_pre,i_post,s_pre,s_post])) or u_pre<=0:
            continue
        baseline_segment = imean[(t >= a) & (t < b)]
        sigma = mad_scale(baseline_segment)
        onset = first_persistent_current_shift(t, imean, step, i_pre, sigma)
        phases = []
        for j in range(3):
            ub = median_window(t, voltage[:,j], a, b)
            ua = median_window(t, voltage[:,j], c, d)
            ib = median_window(t, current[:,j], a, b)
            ia = median_window(t, current[:,j], c, d)
            phases.append({
                "phase":f"L{j+1}","u_pre_V":round(ub,3),
                "delta_u_V":round(ua-ub,3),"i_pre_A":round(ib,3),
                "delta_i_A":round(ia-ib,3)})
        events.append({
            "index":k+1,
            "observed_voltage_transition_relative_s":round(step,3),
            "delta_mean_phase_voltage_V":round(u_post-u_pre,4),
            "delta_mean_phase_voltage_pct":round(100*(u_post/u_pre-1),4),
            "pre_mean_phase_current_A":round(i_pre,4),
            "delta_mean_phase_current_A":round(i_post-i_pre,4),
            "delta_three_phase_apparent_proxy_VA":round(s_post-s_pre,2),
            "pre_current_MAD_scale_A":round(sigma,4),
            "first_sustained_current_deviation_after_screen_time_s":onset,
            "phase_deltas":phases,
            "evidence":"MEASURED_VOLTAGE_CURRENT_ASSOCIATION_UNDER_CONTROLLED_PHIL_PROTOCOL; COMMAND_TIME_AND_STATUS_NOT_IN_CSV",
        })
    return {
        "vehicle":name,
        "n_rows":len(t),
        "time_range_s":[round(float(t[0]),3),round(float(t[-1]),3)],
        "median_sampling_period_s":round(float(np.median(np.diff(t))),5),
        "measured_columns":PHIL_COLS,
        "voltage_transition_screen_threshold_V":threshold_v,
        "n_candidate_voltage_transitions":len(events),
        "events":events
    }


def data_from_phil_csv(path: Path, name: str) -> dict:
    rows = read_csv(path)
    if not rows or list(rows[0].keys()) != PHIL_COLS:
        raise ValueError(f"Unexpected KIT PHIL schema {name}: {list(rows[0]) if rows else '<empty>'}")
    t = np.array([float(r["time_s"]) for r in rows])
    v = np.array([[float(r[f"U_L{k}_V"]) for k in (1,2,3)] for r in rows])
    i = np.array([[float(r[f"I_L{k}_A"]) for k in (1,2,3)] for r in rows])
    result = analyze_signals(name,t,v,i)
    result["file"] = path.name
    result["publisher_md5_verified"] = True
    return result


def metadata_audit(paths: list[Path]) -> dict:
    param = read_csv(paths[0])
    meas = read_csv(paths[1])
    if not param or not meas:
        raise ValueError("Publisher metadata are empty")
    relevant = [r for r in param if any(k in json.dumps(r,ensure_ascii=False).lower()
                    for k in ("setpoint","status","charging enabled","charging_enabled",
                              "power limit","state of charge"))]
    dynamic = [r for r in meas if any(k in json.dumps(r,ensure_ascii=False).lower()
                    for k in ("dynamic","ts_unidir","ts_bidir"))]
    return {
        "dataset":"TU Dortmund: 10.5281/zenodo.14065331",
        "publisher_md5_verified":True,
        "measurement_index_rows":len(meas),
        "measurement_index_columns":list(meas[0]),
        "parameters_rows":len(param),
        "parameters_columns":list(param[0]),
        "potential_dynamic_record_count":len(dynamic),
        "sample_dynamic_records":dynamic[:8],
        "potential_charger_status_setpoint_fields":relevant[:35],
        "limitation":"Metadata identify candidate experiments/columns only; controller-state values and command-to-power delay not yet extracted from selected 207.7MB merged-session archive.",
    }


def self_test():
    t=np.round(np.arange(-6.,8.,.02),8)
    v=np.full((len(t),3),230.)
    i=np.full((len(t),3),15.)
    v[t>=0.2,:]-=10.
    i[t>=2.0,:]-=2.
    r=analyze_signals("synthetic",t,v,i)
    assert r["n_candidate_voltage_transitions"]>=1,r
    best=min(r["events"],key=lambda x:abs(x["observed_voltage_transition_relative_s"]-0.2))
    assert abs(best["delta_mean_phase_voltage_V"]+10)<0.05,best
    assert abs(r["median_sampling_period_s"]-.02)<1e-9
    assert any(e["delta_mean_phase_voltage_pct"]<0 for e in r["events"])
    print("PASS: controlled-voltage transition / phase-current / VA-proxy synthetic test (NOT measured lab result)")


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test",action="store_true")
    ap.add_argument("--cache",type=Path,default=Path.home()/"Downloads/Independent_EV_Lab_2026")
    ap.add_argument("--out",type=Path,default=Path.home()/"Research/MSE-thesis/data/lab_candidates/2026-11-05")
    args=ap.parse_args()
    if args.self_test:
        self_test();return
    results=[]
    for car,filename,md5 in PHIL:
        path=download_verified(args.cache/"KIT_PHIL_22965111",filename,md5,PHIL_RECORD)
        result=data_from_phil_csv(path,car)
        results.append(result)
        print(f"{car}: {result['n_rows']} verified measured samples; "
              f"{result['n_candidate_voltage_transitions']} screened voltage transitions")
    other=[]
    for name,md5 in DORT_METADATA:
        other.append(download_verified(args.cache/"Dortmund_14065331",name,md5,DORT_RECORD))
    metadata=metadata_audit(other)
    out={
        "classification":"INDEPENDENT_LABORATORY_ELECTRICAL_MECHANISM_EVIDENCE_NOT_KIT_FIELD",
        "sources":[
            "https://doi.org/10.5281/zenodo.22965111",
            "https://doi.org/10.5281/zenodo.14065331"],
        "note":"Observed voltage change screening times are not experimental command timestamps.",
        "power_caution":"Sum of U_RMS*I_RMS per phase is apparent-power proxy VA, not measured real active power W.",
        "thermal_caution":"Does not establish device thermal derating or field resilience.",
        "KIT_PHIL_voltage_current":results,
        "TU_Dortmund_control_metadata":metadata,
    }
    args.out.mkdir(parents=True,exist_ok=True)
    j=args.out/"INDEPENDENT_EV_LAB_M2_M3_ELECTRICAL_AUDIT_V1.json"
    j.write_text(json.dumps(out,indent=2,ensure_ascii=False,allow_nan=False)+"\n")
    md=["# Independent controlled EV charging laboratory audit — measured output",
        "",
        "**Source separation:** neither dataset represents the 50-day KIT field deployment.",
        "**Electrical measurement limit:** the PHIL published CSV has U/I RMS per phase, not actual active-power or charger-command columns.",
        "",
        "| PHIL EV | Samples | Screened voltage transitions | Median sample time (s) |",
        "|---|---:|---:|---:|"]
    for x in results:
        md.append(f"| {x['vehicle']} | {x['n_rows']} | {x['n_candidate_voltage_transitions']} | {x['median_sampling_period_s']} |")
    md+=["",
         "**Exact per-event measured voltage/current changes:** see JSON. Change-point times are voltage-screen estimates and are not verified treatment commands.",
         f"**Dortmund measurements in metadata index:** {metadata['measurement_index_rows']}",
         f"**Dortmund candidate dynamic measurements:** {metadata['potential_dynamic_record_count']}",
         f"**Dortmund potentially relevant control parameter definitions:** {len(metadata['potential_charger_status_setpoint_fields'])} (sample capped at 35; see JSON).",
         "",
         "**Evidence verdict:** Controlled PHIL can test voltage/current response under laboratory conditions. Dortmund metadata identifies separate charger-status/setpoint evidence sources. Neither proves the March 2026 field power transitions were controlled by grid voltage. No thermal field validation.",
         ""]
    m=args.out/"INDEPENDENT_EV_LAB_M2_M3_ELECTRICAL_AUDIT_V1.md"
    m.write_text("\n".join(md),encoding="utf-8")
    print("JSON:",j)
    print("Markdown:",m)
    print("LIMIT: independent lab measurements, not field mechanism identification or measured thermal effects")


if __name__=="__main__":
    main()