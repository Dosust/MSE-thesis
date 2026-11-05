#!/usr/bin/env python3
"""KIT measured P–EV interface: reproducible M2/M3 100ms metric audit.

Runs on the two small, pre-extracted ORIGINAL 100-ms KIT event CSVs only.
Does NOT inspect the multi-GB source Parquets or assert a causal dependency.
Source: https://doi.org/10.5281/zenodo.22826984
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

EVENTS = (
    ("2026-03-10T15:32:02+00:00", "KIT_100ms_20260310T153202Z.csv"),
    ("2026-03-10T15:55:02+00:00", "KIT_100ms_20260310T155502Z.csv"),
)
COLUMNS = ("relative_s", "u110_V", "u20_V", "u400_mean_phase_V", "ev_total_p_W",
           "ev_p_L1_W", "ev_p_L2_W", "ev_p_L3_W", "utc")
SAMPLE_INTERVAL = 0.1


def finite_median(x: np.ndarray) -> float:
    vals = x[np.isfinite(x)]
    return float(np.median(vals)) if vals.size else float("nan")


def finite_mad(x: np.ndarray) -> float:
    vals = x[np.isfinite(x)]
    return float(np.median(np.abs(vals - np.median(vals)))) if vals.size else float("nan")


def pct(pre: float, post: float) -> float:
    if not (np.isfinite(pre) and np.isfinite(post) and pre > 0):
        return float("nan")
    return 100.0 * (post / pre - 1.0)


def time_window(t: np.ndarray, low: float, high: float) -> np.ndarray:
    return (t >= low - 1e-8) & (t <= high + 1e-8)


def adjacent_jumps(t: np.ndarray, signal: np.ndarray, start: float, stop: float,
                   percentage: bool = False) -> dict:
    """Largest signed adjacent sample jump with target sample time in [start,stop]."""
    d = np.diff(signal, prepend=np.nan)
    if percentage:
        with np.errstate(divide="ignore", invalid="ignore"):
            d = np.divide(100 * d, np.roll(signal, 1))
        d[0] = np.nan
    allowed = time_window(t, start, stop) & np.isfinite(d)
    if not np.any(allowed):
        return {"time_relative_s": None, "signed_step": None}
    selected = np.flatnonzero(allowed)
    best = selected[np.argmax(np.abs(d[selected]))]
    return {"time_relative_s": round(float(t[best]), 3), "signed_step": float(d[best])}


def sustained_change(t: np.ndarray, p: np.ndarray, baseline: float,
                     threshold_w: float, dwell_s: float = 3.0) -> dict:
    """First >=dwell_s contiguous future samples >=threshold_W from pre baseline.

    This is an intentionally operational *change-state* definition, NOT a verified
    device-response latency or physical mechanism. Evaluate sensitivity.
    """
    n = int(round(dwell_s / SAMPLE_INTERVAL))
    if n < 1 or threshold_w <= 0:
        raise ValueError("Positive dwell and magnitude threshold required")
    for k in np.flatnonzero(t >= 0):
        if k + n > len(t):
            break
        z = p[k:k+n] - baseline
        if len(z) != n or not np.all(np.isfinite(z)):
            continue
        if np.all(z >= threshold_w):
            return {"time_relative_s": round(float(t[k]), 3), "direction": "up",
                    "threshold_W": threshold_w, "dwell_s": dwell_s}
        if np.all(z <= -threshold_w):
            return {"time_relative_s": round(float(t[k]), 3), "direction": "down",
                    "threshold_W": threshold_w, "dwell_s": dwell_s}
    return {"time_relative_s": None, "direction": None,
            "threshold_W": threshold_w, "dwell_s": dwell_s}


def build_metrics(event_utc: str, data: dict[str, np.ndarray]) -> dict:
    t = data["relative_s"]
    n = len(t)
    if n < 401 or not np.isclose(t[0], -25.0, atol=1e-7) or not np.isclose(t[-1], 30.0, atol=1e-7):
        raise ValueError("Expected default event window -25 to +30s with 551 samples")
    if n != 551 or not np.allclose(np.diff(t), SAMPLE_INTERVAL, atol=1e-6):
        raise ValueError("100ms continuity check failed: expected 551 samples with no gaps")
    if not np.any(np.isclose(t, 0, atol=1e-7)):
        raise ValueError("Event time t=0 missing")
    e = datetime.fromisoformat(event_utc)
    utc = data.get("utc")
    if utc is not None:
        for i, (s, offs) in enumerate(zip(utc, t)):
            actual = datetime.fromisoformat(str(s))
            expected = e + timedelta(seconds=float(offs))
            if abs((actual - expected).total_seconds()) > 1e-6:
                raise ValueError(f"Timestamp alignment incorrect at sample {i}: {actual} vs {expected}")

    # M2: robust local voltage levels around the selected voltage step.
    # A symmetric short window, separated by 0.5s from t=0, minimizes one-point noise
    # and avoids the earlier -18s voltage step seen in Event A.
    pre_v = time_window(t, -3, -0.5)
    post_v = time_window(t, +0.5, +3)
    ref_v = time_window(t, -8, -3.5)
    signals = {"u110": data["u110_V"], "u20": data["u20_V"],
               "u400": data["u400_mean_phase_V"]}
    voltages = {}
    for key, v in signals.items():
        before, after = finite_median(v[pre_v]), finite_median(v[post_v])
        peak = adjacent_jumps(t, v, -0.5, +1.0, percentage=True)
        differences = np.diff(v)
        noise = differences[time_window(t[1:], -8, -3.5)]
        noise_mad = 1.4826 * finite_mad(noise)
        voltages[key] = {
            "pre_median_V": before,
            "post_median_V": after,
            "pre_post_delta_pct": pct(before, after),
            "largest_100ms_step_within_minus0p5_to_plus1s_pct": peak["signed_step"],
            "peak_step_time_relative_s": peak["time_relative_s"],
            "pre_ref_difference_MAD_scale_V_per_100ms": noise_mad,
            "n_finite_pre": int(np.isfinite(v[pre_v]).sum()),
            "n_finite_post": int(np.isfinite(v[post_v]).sum()),
        }
    d20 = voltages["u20"]["pre_post_delta_pct"]
    d400 = voltages["u400"]["pre_post_delta_pct"]
    # This is an OBSERVED response ratio, never a calibrated circuit transfer gain.
    ratio = d400 / d20 if np.isfinite(d20) and abs(d20) > 0.15 and np.isfinite(d400) else None
    t20, t400 = voltages["u20"]["peak_step_time_relative_s"], voltages["u400"]["peak_step_time_relative_s"]
    delay = round(t400 - t20, 3) if t20 is not None and t400 is not None else None

    # Note earlier substantial 20kV steps and other event steps in the full 55s window.
    u20_d = 100 * np.diff(signals["u20"]) / signals["u20"][:-1]
    prior_20_steps = [{"relative_s": round(float(t[i+1]), 3), "signed_step_pct": float(v)}
                      for i, v in enumerate(u20_d)
                      if np.isfinite(v) and abs(v) >= 0.15 and t[i+1] < -0.5]

    # M3: independently measured EV point power, separate sustained state change
    # from the largest instantaneous jump and the median effect over a broad window.
    p = data["ev_total_p_W"]
    p_sum = data["ev_p_L1_W"] + data["ev_p_L2_W"] + data["ev_p_L3_W"]
    together = np.isfinite(p) & np.isfinite(p_sum)
    if np.any(np.abs(p[together] - p_sum[together]) > 1e-4):
        raise ValueError("EV summed power does not agree with phase power series")
    pre_p = time_window(t, -5, -0.5)
    post_p = time_window(t, 20, 30)
    mid_post_p = time_window(t, 5, 19)
    baseline = finite_median(p[pre_p])
    stable_post = finite_median(p[post_p])
    if not np.isfinite(baseline):
        raise ValueError("No valid pre-event EV-point power samples")
    event_index = int(np.flatnonzero(np.isclose(t, 0, atol=1e-7))[0])
    p0 = float(p[event_index])
    mad = 1.4826 * finite_mad(p[pre_p])
    n_pre = int(np.isfinite(p[pre_p]).sum())
    n_post = int(np.isfinite(p[post_p]).sum())
    first_stable = sustained_change(t, p, baseline, 100.0, 3.0)
    largest_before = adjacent_jumps(t, p, -20.0, -0.1)
    largest_after = adjacent_jumps(t, p, 0.0, 30.0)
    sensitivity = [sustained_change(t, p, baseline, th, dwell)
                   for th, dwell in ((100, 2), (100, 3), (150, 3), (200, 3), (300, 3))]
    phases = {}
    for k in (1, 2, 3):
        key = f"ev_p_L{k}_W"
        bp, ep = finite_median(data[key][pre_p]), finite_median(data[key][post_p])
        phases[f"L{k}"] = {"pre_median_W": bp, "post_median_W": ep,
                           "delta_W": ep - bp if np.isfinite(bp) and np.isfinite(ep) else None}
    lag = (round(first_stable["time_relative_s"] - t20, 3)
           if first_stable["time_relative_s"] is not None and t20 is not None else None)
    return {
        "event_utc": event_utc,
        "sample_count": n,
        "sample_interval_s": SAMPLE_INTERVAL,
        "M2_cross_voltage": {
            "measurement_definition": "Median voltage step comparing -3..-0.5 s to +0.5..+3 s around selected t=0 voltage event",
            "voltage_channels": voltages,
            "same_direction_20kV_and_400V_median_steps": bool(d20 * d400 > 0),
            "observed_relative_voltage_ratio_delta400_over_delta20": ratio,
            "max_step_timing_difference_400V_minus20kV_s": delay,
            "earlier_20kV_steps_above_0p15pct": prior_20_steps,
            "evidence_grade": "OBSERVED_CROSS_VOLTAGE_CO_RESPONSE_ONLY",
        },
        "M3_EV_point_power": {
            "measurement_definition": "Pre P -5..-0.5 s; post state +20..+30 s; first continuous >=100W baseline deviation lasting >=3 s",
            "pre_median_W": baseline,
            "p_at_selected_voltage_step_W": p0,
            "post_20_to_30s_median_W": stable_post,
            "state_pre_post_delta_W": stable_post-baseline,
            "state_pre_post_delta_percent_of_abs_baseline": (100*(stable_post-baseline)/abs(baseline)
                                                           if abs(baseline)>=50 else None),
            "original_5_to_19s_post_median_W": finite_median(p[mid_post_p]),
            "pre_robust_MAD_scale_W": mad,
            "pre_max_absolute_deviation_from_median_W": float(np.max(np.abs(p[pre_p][np.isfinite(p[pre_p])] - baseline))),
            "n_finite_pre": n_pre,
            "n_finite_post": n_post,
            "first_100W_3s_sustained_state_change": first_stable,
            "lag_sustained_change_minus_u20_largest_step_s": lag,
            "largest_100ms_power_jump_pre": largest_before,
            "largest_100ms_power_jump_at_or_after": largest_after,
            "threshold_and_dwell_sensitivity": sensitivity,
            "phase_median_changes": phases,
            "evidence_grade": "OBSERVED_TIME_ORDERED_POWER_STATE_TRANSITION_CAUSE_UNIDENTIFIED",
        },
        "interface_verdict": {
            "M1_structural_topology": "NOT_VERIFIED_FOR_SPECIFIC_20KV_TO_EV_POINT_PARENTAGE",
            "M2_electrical": "OBSERVED",
            "M3_power_to_transport_operational_interdependency": "NOT_ESTABLISHED_AS_CAUSAL_OR_DEVICE_DEPENDENCE",
            "M4_transport_to_power_loading": "NOT_IDENTIFIED_FROM_SOURCE_POWER_CHANNELS",
            "M5_heat_thermal": "NOT_MEASURED",
            "M6_mobility_service": "NOT_MEASURED",
            "reason": "No confirmed feeder connectivity, EV/EVSE controller state, causal test/control or measured thermal/service variables. Change-point timing alone cannot establish physical causal direction.",
        },
    }


def load_csv(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"Expected pre-extracted original 100ms event CSV: {path}")
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        if not set(COLUMNS).issubset(r.fieldnames or []):
            raise ValueError(f"Wrong CSV schema: {path.name}")
        rows = list(r)
    def parse_float(s: str) -> float:
        return float(s) if s is not None and s.strip() else float("nan")
    data = {k: np.array([parse_float(row[k]) for row in rows], dtype=np.float64)
            for k in COLUMNS if k != "utc"}
    data["utc"] = np.array([r["utc"] for r in rows], dtype=object)
    return data


def safe_json(value):
    """Avoid writing NaN / Inf as non-standard JSON literals."""
    if isinstance(value, dict):
        return {k: safe_json(v) for k, v in value.items()}
    if isinstance(value, list):
        return [safe_json(v) for v in value]
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, (np.integer,)):
        return int(value)
    return value


def report_markdown(results: list[dict]) -> str:
    lines = ["# KIT M2/M3 original 100 ms event metrics — measured output",
             "", "**Source:** https://doi.org/10.5281/zenodo.22826984",
             "**Provenance:** Derived from previously extracted original 100 ms KIT CSV windows. Do not infer heat or causality.",
             "**Definitions:** M2 local voltage median change: -3 to -0.5s versus +0.5 to +3s. M3 active-power pre baseline -5 to -0.5s, post settled-state +20 to +30s; sustained transition = >=100 W for >=3.0s uninterrupted. All windows relative to selected 20kV voltage-step time.",
             "", "| Event UTC | M2 U20 delta % | M2 U400 delta % | U400/20 ratio | M2 Δt peak 400-20 (s) | P at t=0 (W) | M3 settled ΔP (W) | First sustained shift t (s) |",
             "|---|---:|---:|---:|---:|---:|---:|---:|"]
    fmt = lambda x, n=3: "NA" if x is None or not np.isfinite(x) else f"{x:+.{n}f}"
    for r in results:
        a, b = r["M2_cross_voltage"], r["M3_EV_point_power"]
        u = a["voltage_channels"]
        t = b["first_100W_3s_sustained_state_change"]["time_relative_s"]
        lines.append("| " + " | ".join((r["event_utc"], fmt(u["u20"]["pre_post_delta_pct"]),
                    fmt(u["u400"]["pre_post_delta_pct"]),
                    fmt(a["observed_relative_voltage_ratio_delta400_over_delta20"]),
                    fmt(a["max_step_timing_difference_400V_minus20kV_s"], 1),
                    fmt(b["p_at_selected_voltage_step_W"], 2),
                    fmt(b["state_pre_post_delta_W"], 2),
                    "NA" if t is None else f"+{t:.1f}")) + " |")
    lines += ["", "## Per-event checks", ""]
    for r in results:
        a, b = r["M2_cross_voltage"], r["M3_EV_point_power"]
        lines += [f"### {r['event_utc']}",
                  f"- 20/400V M2 voltage step signs agree: **{a['same_direction_20kV_and_400V_median_steps']}**; voltage relative timing is observational at 100ms precision.",
                  f"- Earlier 20kV steps >=0.15% before selected event: **{len(a['earlier_20kV_steps_above_0p15pct'])}**; see JSON for offsets.",
                  f"- Event-time EV power: **{fmt(b['p_at_selected_voltage_step_W'],2)} W**; pre baseline {fmt(b['pre_median_W'],2)} W; settled post {fmt(b['post_20_to_30s_median_W'],2)} W.",
                  f"- Pre-window power 1.4826×MAD **{fmt(b['pre_robust_MAD_scale_W'],2)} W**, maximum absolute deviation **{fmt(b['pre_max_absolute_deviation_from_median_W'],2)} W**.",
                  f"- Largest raw prior 100ms ΔP: **{fmt(b['largest_100ms_power_jump_pre']['signed_step'],2)} W** at t={b['largest_100ms_power_jump_pre']['time_relative_s']} s; largest at/after ΔP: **{fmt(b['largest_100ms_power_jump_at_or_after']['signed_step'],2)} W** at t={b['largest_100ms_power_jump_at_or_after']['time_relative_s']} s.",
                  f"- Sensitivity (change-point onset at thresholds/dwell): " + ", ".join(f"{int(s['threshold_W'])}W/{int(s['dwell_s'])}s -> {s['time_relative_s']}s" for s in b["threshold_and_dwell_sensitivity"]),
                  ""]
    lines += ["## Scientific evidence decision", "",
              "**M2: OBSERVED synchronized electrical cross-voltage co-response.** Measured relative voltage changes at 20kV and the EV-meter 400V level; ratio and timing are *descriptive*, not a verified transfer factor or feeder cause.", "",
              "**M3: OBSERVED subsequent EV-meter electrical power-state transitions.** Changes in independently metered EV-point power must be distinguished from battery charging status and controller commands. A stable pre-window and later transition cannot demonstrate voltage-induced operational dependence by themselves.", "",
              "**Operational P↔T interdependency: NOT VERIFIED from this pair alone.** Specific feeder parentage, alternative controller states / matched controls, and corroborating mechanism remain missing. **Thermal and mobility-service metrics: NOT MEASURED.**", "",
              "**Data note:** Two events selected within the same labeled fault period are not independent trials. Local noise, thresholds and baseline/window choices are exploratory; evaluate sensitivity before inferential claims.", ""]
    return "\n".join(lines)


def synthetic_self_test() -> None:
    t = np.round(np.arange(-25, 30.01, 0.1), 1)
    assert len(t) == 551
    # Known 20kV +0.6% near event, 400V +0.7% 100ms later,
    # independently imposed EV power transition at +8s.
    v20 = np.full(len(t), 12000.0)
    v20[t >= 0] *= 1.006
    v400 = np.full(len(t), 237.0)
    v400[t >= 0.1] *= 1.007
    v110 = np.full(len(t), 64000.0)
    power = np.full(len(t), 1500.0)
    power[t >= 8.0] = 1200.0
    e = datetime.fromisoformat(EVENTS[0][0])
    data = {"relative_s": t, "u20_V": v20, "u400_mean_phase_V": v400,
            "u110_V": v110, "ev_total_p_W": power,
            "utc": np.array([(e + timedelta(seconds=float(v))).isoformat() for v in t])}
    for k in (1, 2, 3):
        data[f"ev_p_L{k}_W"] = power / 3.0
    m = build_metrics(EVENTS[0][0], data)
    assert abs(m["M2_cross_voltage"]["voltage_channels"]["u20"]["pre_post_delta_pct"] - 0.6) < 1e-6
    assert abs(m["M2_cross_voltage"]["voltage_channels"]["u400"]["pre_post_delta_pct"] - 0.7) < 1e-6
    assert abs(m["M2_cross_voltage"]["max_step_timing_difference_400V_minus20kV_s"] - 0.1) < 1e-6
    assert m["M3_EV_point_power"]["state_pre_post_delta_W"] == -300.0
    assert m["M3_EV_point_power"]["first_100W_3s_sustained_state_change"]["time_relative_s"] == 8.0
    assert m["interface_verdict"]["M5_heat_thermal"] == "NOT_MEASURED"
    assert json.loads(json.dumps(safe_json(m), allow_nan=False))["sample_count"] == 551
    print("PASS: M2/M3 synthetic metrics and timing self-test (NOT a KIT measured result)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-folder", type=Path,
                        default=Path.home() / "Downloads/KIT_OLTC_Electrical_Results/100ms_targeted_events")
    parser.add_argument("--out-folder", type=Path,
                        default=Path(__file__).resolve().parent.parent / "data/field_candidates/2026-11-05")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        synthetic_self_test()
        return
    findings = [build_metrics(stamp, load_csv(args.input_folder / name))
                for stamp, name in EVENTS]
    output = {
        "source": "https://doi.org/10.5281/zenodo.22826984",
        "source_kind": "measured original 100ms electrical observations in 551-row extracted event CSV windows",
        "metric_protocol": "POWER_TRANSPORT_INTERDEPENDENCY_METRICS_AND_EVIDENCE_QUALIFICATION_V1.md",
        "selection": "two hand-selected events from same March 10 fault episode; not independent experiments",
        "operational_dependency_causality": "NOT_ESTABLISHED",
        "thermal_or_mobility_field_measurement": "NOT_PRESENT",
        "results": findings,
    }
    args.out_folder.mkdir(parents=True, exist_ok=True)
    j = args.out_folder / "KIT_M2_M3_100MS_MEASUREMENTS_V1.json"
    m = args.out_folder / "KIT_M2_M3_100MS_MEASUREMENTS_V1.md"
    j.write_text(json.dumps(safe_json(output), indent=2, allow_nan=False) + "\n", encoding="utf-8")
    m.write_text(report_markdown(findings), encoding="utf-8")
    print("=== KIT MEASURED M2/M3 ORIGINAL 100MS ===")
    for r in findings:
        a, b = r["M2_cross_voltage"], r["M3_EV_point_power"]
        print("Event UTC:", r["event_utc"])
        print(" M2 20kV/400V delta %:", round(a["voltage_channels"]["u20"]["pre_post_delta_pct"], 4),
              round(a["voltage_channels"]["u400"]["pre_post_delta_pct"], 4))
        print(" M2 observed 400/20 relative-step ratio:",
              None if a["observed_relative_voltage_ratio_delta400_over_delta20"] is None else
              round(a["observed_relative_voltage_ratio_delta400_over_delta20"], 4))
        print(" M2 400V-minus-20kV strongest voltage-step timestamp difference (s):",
              a["max_step_timing_difference_400V_minus20kV_s"])
        print(" M2 earlier 20kV steps >=0.15%:",len(a["earlier_20kV_steps_above_0p15pct"]))
        print(" M3 EV pre / at event / late post (W):", *(round(b[z], 2) for z in
              ("pre_median_W", "p_at_selected_voltage_step_W", "post_20_to_30s_median_W")))
        print(" M3 settled post minus pre delta (W):",round(b["state_pre_post_delta_W"], 2))
        print(" M3 first >=100W for >=3s state change at (s):",
              b["first_100W_3s_sustained_state_change"]["time_relative_s"])
        print(" M3 pre baseline robust MAD scale (W):", round(b["pre_robust_MAD_scale_W"],2))
    print("EVIDENCE: M2 observed electrical co-response; M3 time-ordered association; operational dependency NOT verified; thermal/service NOT measured")
    print("JSON:", j)
    print("Markdown:", m)


if __name__ == "__main__":
    main()