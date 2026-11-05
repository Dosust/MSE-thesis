#!/usr/bin/env python3
"""Screen KIT one-second 20-kV voltage steps conditional on EV-point real-power activity.

Reads previously derived files from KIT OLTC data (Zenodo 22826984), NOT the
original 100-ms Parquet files. Only measured electrical co-responses are reported.
See repository evidence protocol and originals' source qualification before
interpreting output as charging states, feeder causation or thermal resilience.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

FIRST_UTC = datetime(2026, 2, 3, 23, 0, tzinfo=timezone.utc)
EXPECTED_SECONDS = 4_320_000


def median_finite(values: np.ndarray) -> float:
    values = values[np.isfinite(values)]
    return float(np.median(values)) if len(values) else float("nan")


def pct_change(before: float, after: float) -> float:
    return float(100 * (after / before - 1)) if np.isfinite(before) and before > 0 and np.isfinite(after) else float("nan")


def select_conditioned_events(
    u20: np.ndarray,
    ev_p: np.ndarray,
    voltage_step_threshold_pct: float = 0.15,
    ev_active_threshold_w: float = 500,
    min_gap_s: int = 45,
    max_events: int = 60,
) -> tuple[list[tuple[int, float, float]], dict]:
    """Return up to max_events independent 20kV step candidates with active pre-window P.

    The pre-window is [-20, -6] seconds inclusive. The voltage trigger is the
    positive or negative *one-second* step, not the post/pre window difference.
    """
    n = len(u20)
    if len(ev_p) != n or n < 61:
        raise ValueError("Voltage and EV power arrays must align and be at least 61 seconds long")
    if voltage_step_threshold_pct <= 0 or ev_active_threshold_w <= 0 or min_gap_s <= 0 or max_events <= 0:
        raise ValueError("Thresholds, min gap and max events must be positive")

    left = u20[:-1]
    right = u20[1:]
    valid_pair = np.isfinite(left) & np.isfinite(right) & (left > 0) & (right > 0)
    scores = np.zeros(n - 1, dtype=np.float64)
    np.divide(np.abs(right - left) * 100.0, left, out=scores, where=valid_pair)
    raw_idx = np.flatnonzero((scores >= voltage_step_threshold_pct) & valid_pair) + 1
    raw_idx = raw_idx[(raw_idx >= 30) & (raw_idx < n - 30)]

    qualified: list[tuple[int, float, float]] = []
    valid_pre_count = 0
    for i in raw_idx:
        pre = median_finite(ev_p[i - 20:i - 5])
        if np.isfinite(pre):
            valid_pre_count += 1
            if abs(pre) >= ev_active_threshold_w:
                qualified.append((int(i), float(scores[i - 1]), pre))

    # Rank only *power-conditioned* steps; unlike an earlier top-60 selection,
    # power conditioning takes place BEFORE applying the 60-event limit.
    qualified.sort(key=lambda x: (-x[1], x[0]))
    blocked = np.zeros(n, dtype=np.bool_)
    selected: list[tuple[int, float, float]] = []
    for i, score, pre in qualified:
        if blocked[i]:
            continue
        selected.append((i, score, pre))
        blocked[max(0, i - min_gap_s + 1):min(n, i + min_gap_s)] = True
        if len(selected) >= max_events:
            break
    selected.sort(key=lambda x: x[0])
    stats = {
        "one_second_voltage_steps_above_screening_threshold": int(len(raw_idx)),
        "steps_with_finite_ev_pre_median": int(valid_pre_count),
        "steps_with_ev_pre_median_abs_ge_power_threshold": int(len(qualified)),
        "selected_independent_power_conditioned_steps": int(len(selected)),
        "selected_events_capped_at": int(max_events),
        "selected_at_cap": bool(len(selected) == max_events),
    }
    return selected, stats


def load_source_signals(folder: Path):
    import pyarrow.parquet as pq

    def table(name, cols):
        p = folder / name
        if not p.is_file():
            raise FileNotFoundError(f"Missing existing derived dataset: {p}")
        t = pq.read_table(p, columns=cols)
        if t.num_rows != EXPECTED_SECONDS:
            raise ValueError(f"{p.name}: expected {EXPECTED_SECONDS:,} one-second rows, found {t.num_rows:,}")
        ids = np.asarray(t["second_index"].to_numpy(zero_copy_only=False))
        if not np.array_equal(ids, np.arange(EXPECTED_SECONDS, dtype=np.int32)):
            raise ValueError(f"{p.name}: second_index alignment mismatch")
        return t

    t20 = table("grid20_1s.parquet", ["second_index", "u_pos_V", "fault_phase_at_second_start"])
    u20 = np.asarray(t20["u_pos_V"].to_numpy(zero_copy_only=False), dtype=np.float64)
    phases = t20["fault_phase_at_second_start"]

    t110 = table("grid110_1s.parquet", ["second_index", "u_pos_V"])
    u110 = np.asarray(t110["u_pos_V"].to_numpy(zero_copy_only=False), dtype=np.float64)

    te = table("ev400_1s.parquet", ["second_index", "u_L1_V", "u_L2_V", "u_L3_V", "p_L1_W", "p_L2_W", "p_L3_W"])
    voltage = [np.asarray(te[f"u_L{k}_V"].to_numpy(zero_copy_only=False), dtype=np.float64) for k in (1, 2, 3)]
    all_u = np.logical_and.reduce([np.isfinite(v) for v in voltage])
    u400 = np.full(EXPECTED_SECONDS, np.nan)
    u400[all_u] = (voltage[0][all_u] + voltage[1][all_u] + voltage[2][all_u]) / 3
    del voltage

    power = [np.asarray(te[f"p_L{k}_W"].to_numpy(zero_copy_only=False), dtype=np.float64) for k in (1, 2, 3)]
    all_p = np.logical_and.reduce([np.isfinite(v) for v in power])
    ev_p = np.full(EXPECTED_SECONDS, np.nan)
    ev_p[all_p] = power[0][all_p] + power[1][all_p] + power[2][all_p]
    return u20, u110, u400, ev_p, phases


def make_result_row(i: int, score: float, pre_power: float, u20, u110, u400, ev_p, phases) -> dict:
    pre = slice(i - 20, i - 5)
    post = slice(i + 5, i + 20)
    u110_before, u110_after = median_finite(u110[pre]), median_finite(u110[post])
    u20_before, u20_after = median_finite(u20[pre]), median_finite(u20[post])
    u400_before, u400_after = median_finite(u400[pre]), median_finite(u400[post])
    post_power = median_finite(ev_p[post])
    return {
        "event_utc": (FIRST_UTC + timedelta(seconds=i)).isoformat(),
        "second_index": i,
        "fault_phase_at_event": phases[i].as_py(),
        "trigger_20kV_1s_step_abs_pct": score,
        "ev_pre_power_W_signed": pre_power,
        "ev_post_power_W_signed": post_power,
        "ev_delta_power_W_signed": post_power - pre_power,
        "u110_pre_post_delta_pct": pct_change(u110_before, u110_after),
        "u20_pre_post_delta_pct": pct_change(u20_before, u20_after),
        "u400_pre_post_delta_pct": pct_change(u400_before, u400_after),
        "full_three_voltage_pre_post_response_finite": bool(np.all(np.isfinite([u110_before, u110_after, u20_before, u20_after, u400_before, u400_after]))),
    }


def synthetic_self_test():
    n = 260
    u = np.full(n, 20_000., dtype=np.float64)
    u[100:180] = 19_700.
    p = np.full(n, 2., dtype=np.float64)
    p[65:120] = 7_000.
    selected, counts = select_conditioned_events(u, p, max_events=60)
    assert counts["one_second_voltage_steps_above_screening_threshold"] == 2
    assert counts["steps_with_finite_ev_pre_median"] == 2
    assert counts["steps_with_ev_pre_median_abs_ge_power_threshold"] == 1
    assert len(selected) == 1 and selected[0][0] == 100
    assert abs(pct_change(100., 101.) - 1.0) < 1e-8
    p[65:120] = np.nan
    selected, _ = select_conditioned_events(u, p)
    assert not selected
    print("PASS: power-conditioned 1s step selection synthetic self-test (NOT KIT measurement)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", type=Path, default=Path.home() / "Downloads/KIT_OLTC_Electrical_Results")
    parser.add_argument("--step-threshold-pct", type=float, default=0.15)
    parser.add_argument("--ev-power-threshold-w", type=float, default=500)
    parser.add_argument("--min-gap-s", type=int, default=45)
    parser.add_argument("--max-events", type=int, default=60)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        synthetic_self_test()
        return

    u20, u110, u400, ev_p, phases = load_source_signals(args.folder)
    picked, counts = select_conditioned_events(u20, ev_p, args.step_threshold_pct,
                                               args.ev_power_threshold_w, args.min_gap_s, args.max_events)
    rows = [make_result_row(i, score, power, u20, u110, u400, ev_p, phases) for i, score, power in picked]
    csv_path = args.folder / "power_conditioned_voltage_step_events.csv"
    fields = ["event_utc", "second_index", "fault_phase_at_event", "trigger_20kV_1s_step_abs_pct",
              "ev_pre_power_W_signed", "ev_post_power_W_signed", "ev_delta_power_W_signed",
              "u110_pre_post_delta_pct", "u20_pre_post_delta_pct", "u400_pre_post_delta_pct",
              "full_three_voltage_pre_post_response_finite"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "source": "https://doi.org/10.5281/zenodo.22826984",
        "input": "previously generated 1-second derived measured KIT records, not raw 100ms reread",
        "time_range_first_utc": FIRST_UTC.isoformat(),
        "source_one_second_count": EXPECTED_SECONDS,
        "screening_parameters": {"step_abs_pct_at_20kV": args.step_threshold_pct,
                                 "ev_pre_abs_power_w": args.ev_power_threshold_w,
                                 "minimum_gap_seconds": args.min_gap_s, "maximum_selected": args.max_events,
                                 "pre_window": "event-20 through event-6 inclusive",
                                 "post_window": "event+5 through event+19 inclusive"},
        **counts,
        "selected_events_with_finite_all_three_voltage_pre_post": sum(int(r["full_three_voltage_pre_post_response_finite"]) for r in rows),
        "csv_filename": csv_path.name,
        "limits": ["Power sign/charger state not independently verified",
                   "Event triggering is one-second 20kV steps, not measured OLTC tap telemetry",
                   "Coincident changes do not prove causal feeder parentage",
                   "No heat, EVSE internal temperature, derating or observed mobility-service impact",
                   "Power screening before cap avoids missing substantial EV operation when strongest steps happen at idle times"],
    }
    json_path = args.folder / "power_conditioned_voltage_step_summary.json"
    json_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("=== KIT POWER-CONDITIONED 20 kV VOLTAGE STEP CANDIDATES ===")
    print("One-second 20kV steps ≥ threshold, excluding edge windows:", counts["one_second_voltage_steps_above_screening_threshold"])
    print("Steps with finite pre-event EV power:", counts["steps_with_finite_ev_pre_median"])
    print("Steps where |pre-event EV-point real power| ≥", args.ev_power_threshold_w,
          "W:", counts["steps_with_ev_pre_median_abs_ge_power_threshold"])
    print("Independent selected power-conditioned event candidates:", len(picked))
    print("Full 110/20/400V pre/post finite coverage:", summary["selected_events_with_finite_all_three_voltage_pre_post"])
    print("First 5 conditional events:")
    for r in rows[:5]:
        print({k: r[k] for k in ("event_utc", "fault_phase_at_event", "trigger_20kV_1s_step_abs_pct",
                                 "ev_pre_power_W_signed", "ev_delta_power_W_signed",
                                 "u110_pre_post_delta_pct", "u20_pre_post_delta_pct", "u400_pre_post_delta_pct")})
    print("JSON:", json_path)
    print("CSV:", csv_path)
    print("LIMIT: describes synchronized electrical measurements, NOT thermal effects, verified charge state or causal feeder paths")


if __name__ == "__main__":
    main()