#!/usr/bin/env python3
"""KIT OLTC 110/20/0.4 kV electrical responses: source-grounded, read-only.

Original data: https://doi.org/10.5281/zenodo.22826984

The original three Parquet files must already be on the user's Mac and must have
passed their publisher MD5 and 100 ms UTC-grid checks. This script DOES NOT
prove circuit topology, electrical causation, extreme-heat effects, or service
resilience; only measured electrical contrasts are reported.

Requires: Python 3.10+, numpy, pyarrow, matplotlib.
Run: python3 kit_oltc_electrical_response_analysis.py
See --help for output and event sensitivity options.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

DATASET = "https://doi.org/10.5281/zenodo.22826984"
FIRST_UTC = datetime(2026, 2, 3, 23, 0, tzinfo=timezone.utc)
EXPECTED_SAMPLES = 43_200_000
EXPECTED_SECONDS = EXPECTED_SAMPLES // 10
SAMPLE_PER_SECOND = 10

SOURCES = {
    "grid110": {
        "name": "oltc_fail_110kV_PMU04_TK1_100ms.parquet",
        "signals": {"u_pos_V": "u_pos[V]", "p_MW": "p[MW]", "q_MVAr": "q[MVAr]", "f_Hz": "f[Hz]"},
    },
    "grid20": {
        "name": "oltc_fail_20kV_PMU01_J01_100ms.parquet",
        "signals": {"u_pos_V": "u_pos[V]", "i_pos_A": "i_pos[A]"},
    },
    "ev400": {
        "name": "oltc_fail_400V_EV_SH.J.6_100ms.parquet",
        "signals": {
            "u_L1_V": "u_L1[V]", "u_L2_V": "u_L2[V]", "u_L3_V": "u_L3[V]",
            "p_L1_W": "p_L1[W]", "p_L2_W": "p_L2[W]", "p_L3_W": "p_L3[W]",
            "q_L1_var": "q_L1[var]", "q_L2_var": "q_L2[var]", "q_L3_var": "q_L3[var]",
        },
    },
}


def finite_mean_groups(v: np.ndarray, group: int = SAMPLE_PER_SECOND) -> tuple[np.ndarray, int]:
    v = np.asarray(v, dtype=np.float64)
    if len(v) % group:
        raise ValueError("The provided buffer is not second-aligned")
    ok = np.isfinite(v)
    count = ok.reshape(-1, group).sum(axis=1)
    sums = np.where(ok, v, 0.0).reshape(-1, group).sum(axis=1)
    means = np.full(len(count), np.nan, dtype=np.float64)
    np.divide(sums, count, out=means, where=count > 0)
    return means, int((~ok).sum())


def source_aggregate(source_key: str, folder: Path, out: Path, batch_size: int) -> dict:
    import pyarrow as pa
    import pyarrow.compute as pc
    import pyarrow.parquet as pq

    spec = SOURCES[source_key]
    original = folder / spec["name"]
    if not original.is_file():
        raise FileNotFoundError(f"Missing original: {original}")
    raw = pq.ParquetFile(original)
    if raw.metadata.num_rows != EXPECTED_SAMPLES:
        raise ValueError(f"{original.name}: expected {EXPECTED_SAMPLES} rows; got {raw.metadata.num_rows}")

    selected = ["fault_phase", *spec["signals"].values()]
    available = set(raw.schema_arrow.names)
    for col in selected:
        if col not in available:
            raise ValueError(f"{original.name}: missing column {col!r}")

    out.parent.mkdir(parents=True, exist_ok=True)
    writer = None
    phase_carry = None
    carry: dict[str, np.ndarray] = {k: np.empty(0, dtype=np.float64) for k in spec["signals"]}
    second = 0
    quality = Counter()
    total_rows = 0

    try:
        for batch in raw.iter_batches(batch_size=batch_size, columns=selected, use_threads=True):
            raw_n = batch.num_rows
            total_rows += raw_n
            phases = batch.column(0)
            if phase_carry is not None and len(phase_carry):
                phases = pa.concat_arrays([phase_carry, phases])
            numeric = {}
            for k, original_col in spec["signals"].items():
                idx = selected.index(original_col)
                arr = batch.column(idx).to_numpy(zero_copy_only=False)
                numeric[k] = np.concatenate((carry[k], np.asarray(arr, dtype=np.float64)))

            n_full = len(phases) // SAMPLE_PER_SECOND
            used = n_full * SAMPLE_PER_SECOND
            if not n_full:
                phase_carry = phases
                carry = numeric
                continue

            offsets = pa.array(np.arange(0, used, SAMPLE_PER_SECOND, dtype=np.int32))
            sampled_phase = pc.take(phases.slice(0, used), offsets)
            out_cols: dict[str, object] = {
                "second_index": pa.array(np.arange(second, second + n_full, dtype=np.int32)),
                "fault_phase_at_second_start": sampled_phase,
            }
            for k, arr in numeric.items():
                avg, nonfinite = finite_mean_groups(arr[:used])
                quality[k + "_nonfinite_original_samples"] += nonfinite
                quality[k + "_valid_second_means"] += int(np.isfinite(avg).sum())
                out_cols[k] = pa.array(avg)
                carry[k] = arr[used:]
            phase_carry = phases.slice(used)
            second += n_full
            table = pa.table(out_cols)
            if writer is None:
                writer = pq.ParquetWriter(str(out), table.schema, compression="zstd")
            writer.write_table(table)
            if second % 500_000 < n_full:
                print(f"  {source_key}: {second:,} one-second means computed", flush=True)
        if second != EXPECTED_SECONDS or total_rows != EXPECTED_SAMPLES or len(phase_carry):
            raise RuntimeError(
                f"Unexpected aggregation final size: original={total_rows}, "
                f"seconds={second}, remaining={len(phase_carry) if phase_carry is not None else -1}"
            )
    finally:
        if writer is not None:
            writer.close()

    return {
        "original_filename": original.name,
        "original_bytes_local": original.stat().st_size,
        "original_rows": total_rows,
        "computed_one_second_bins": second,
        "source_fields": selected,
        "nonfinite_measurement_statistics": dict(quality),
        "note": "One-second averages of finite 100 ms observations; not original measurements at 1 Hz; fault labels sampled at first 100 ms instant",
    }


def read_col(table, name: str) -> np.ndarray:
    return np.asarray(table[name].to_numpy(zero_copy_only=False), dtype=np.float64)


def median_or_nan(arr: np.ndarray) -> float:
    a = arr[np.isfinite(arr)]
    return float(np.median(a)) if len(a) else float("nan")


def make_ev_voltage(ev) -> np.ndarray:
    phase = np.column_stack([read_col(ev, f"u_L{i}_V") for i in (1, 2, 3)])
    okay = np.all(np.isfinite(phase), axis=1)
    values = np.full(len(phase), np.nan)
    values[okay] = phase[okay].mean(axis=1)
    return values


def make_ev_power(ev) -> np.ndarray:
    phase = np.column_stack([read_col(ev, f"p_L{i}_W") for i in (1, 2, 3)])
    okay = np.all(np.isfinite(phase), axis=1)
    values = np.full(len(phase), np.nan)
    values[okay] = phase[okay].sum(axis=1)
    return values


def pct_change(before: float, after: float) -> float:
    if not np.isfinite(before) or not np.isfinite(after) or before <= 0:
        return float("nan")
    return 100.0 * (after / before - 1.0)


def event_candidates(u20: np.ndarray, threshold_pct: float, minimum_gap: int, maximum: int,
                     phase_labels: np.ndarray | None = None,
                     phase_filter: str = "") -> list[tuple[int, float]]:
    """Largest one-second 20 kV voltage steps, separated by minimum_gap seconds."""
    denom = u20[:-1]
    right = u20[1:]
    valid = (np.isfinite(denom) & np.isfinite(right) & (denom > 0) & (right > 0))
    score = np.zeros(len(denom), dtype=np.float32)
    np.divide(np.abs(right - denom) * 100.0, denom, out=score, where=valid)
    eligible = (score >= threshold_pct)
    if phase_filter and phase_labels is not None:
        eligible &= np.char.find(phase_labels[1:].astype(str), phase_filter) >= 0
    idx = np.flatnonzero(eligible)
    if len(idx) == 0:
        return []
    scores = score[idx]
    order = np.argsort(-scores, kind="stable")
    picked: list[tuple[int, float]] = []
    for pos in order:
        instant = int(idx[pos] + 1)
        if instant < 30 or instant >= len(u20) - 30:
            continue
        if all(abs(instant - past) >= minimum_gap for past, _ in picked):
            picked.append((instant, float(score[instant - 1])))
        if len(picked) >= maximum:
            break
    return sorted(picked)


def utc_label(seconds_from_start: int) -> str:
    return (FIRST_UTC + timedelta(seconds=int(seconds_from_start))).isoformat()


def event_metrics(events: list[tuple[int, float]],
                  signals: dict[str, np.ndarray],
                  phases: np.ndarray,
                  exchange_threshold_w: float) -> list[dict]:
    rows: list[dict] = []
    for i, raw_jump in events:
        before = slice(i - 20, i - 5)
        after = slice(i + 5, i + 20)
        vals = {k: (median_or_nan(arr[before]), median_or_nan(arr[after]))
                for k, arr in signals.items()}
        pb, pa = vals["ev_p_W"]
        row = {
            "event_utc": utc_label(i), "second_index": i,
            "source_trigger_20kV_1s_step_abs_pct": raw_jump,
            "fault_phase_label_at_event": str(phases[i]),
            "pre_window_seconds": "-20..-6", "post_window_seconds": "+5..+19",
            "ev_significant_exchange_pre": bool(np.isfinite(pb) and abs(pb) >= exchange_threshold_w),
            "ev_power_pre_kW": pb / 1000.0,
            "ev_power_post_kW": pa / 1000.0,
            "ev_power_delta_kW": (pa - pb) / 1000.0,
            "ev_power_sign_convention_verified": False,
            "u110_change_pct": pct_change(*vals["u110_V"]),
            "u20_change_pct": pct_change(*vals["u20_V"]),
            "u400_change_pct": pct_change(*vals["ev_u_V"]),
            "i20_change_A": vals["i20_A"][1] - vals["i20_A"][0],
            "p110_change_MW": vals["p110_MW"][1] - vals["p110_MW"][0],
        }
        rows.append(row)
    return rows


def safe_hourly_median(a: np.ndarray) -> np.ndarray:
    n = (len(a) // 3600) * 3600
    result = []
    # hourly loop avoids large temporary buffers or warnings from entirely missing groups
    for i in range(0, n, 3600):
        result.append(median_or_nan(a[i:i + 3600]))
    return np.asarray(result)


def save_figures(output: Path, signals: dict[str, np.ndarray],
                 events: list[tuple[int, float]]) -> list[str]:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    produced = []
    hours = np.arange(EXPECTED_SECONDS // 3600)
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(12, 6), constrained_layout=True)
    # A separate median reference for each voltage avoids invalid comparison of nominal levels.
    for key, label in [("u110_V", "110 kV positive-sequence"), ("u20_V", "20 kV positive-sequence"),
                       ("ev_u_V", "400 V mean of three measured phases")]:
        v = safe_hourly_median(signals[key])
        baseline = median_or_nan(v)
        if np.isfinite(baseline) and baseline > 0:
            ax[0].plot(hours[:len(v)] / 24.0, 100.0 * (v / baseline - 1.0), label=label, linewidth=0.8)
    ax[0].set_ylabel("Voltage deviation from own median (%)")
    ax[0].legend(fontsize=8)
    ax[0].grid(alpha=0.3)
    power = safe_hourly_median(signals["ev_p_W"]) / 1000.0
    ax[1].plot(hours[:len(power)] / 24.0, power, linewidth=0.8)
    ax[1].set_xlabel("Days since 2026-02-03 23:00 UTC")
    ax[1].set_ylabel("400 V EV measured three-phase P (kW)")
    ax[1].grid(alpha=0.3)
    fig.suptitle("KIT measured electrical levels: hourly medians (NOT temperature)")
    p = output / "01_voltage_power_50days.png"
    fig.savefig(p, dpi=180)
    plt.close(fig)
    produced.append(p.name)

    if events:
        # Strongest 20-kV event, not necessarily a confirmed tap-position change.
        i, size = max(events, key=lambda x: x[1])
        t = np.arange(-30, 31)
        idx = np.arange(i - 30, i + 31)
        fig, ax = plt.subplots(2, 1, figsize=(12, 7), sharex=True, constrained_layout=True)
        pre = slice(i - 20, i - 5)
        for key, label in [("u110_V", "110 kV"), ("u20_V", "20 kV"), ("ev_u_V", "400 V EV")]:
            basis = median_or_nan(signals[key][pre])
            if np.isfinite(basis) and basis > 0:
                ax[0].plot(t, 100.0 * (signals[key][idx] / basis - 1.0), label=label)
        ax[0].axvline(0, linestyle="--", alpha=0.7)
        ax[0].set_ylabel("Voltage change vs pre-event (%)")
        ax[0].legend()
        ax[0].grid(alpha=0.3)
        ax[1].plot(t, signals["ev_p_W"][idx] / 1000.0)
        ax[1].axvline(0, linestyle="--", alpha=0.7)
        ax[1].set_ylabel("EV point active P (kW)")
        ax[1].set_xlabel("Seconds relative to 20 kV voltage-step candidate")
        ax[1].grid(alpha=0.3)
        fig.suptitle(f"Observed response near {utc_label(i)} (20 kV 1s step = {size:.3f}%)")
        p = output / "02_largest_event_comparison.png"
        fig.savefig(p, dpi=180)
        plt.close(fig)
        produced.append(p.name)
    return produced


def jsonable(x):
    if isinstance(x, (np.bool_,)): return bool(x)
    if isinstance(x, (np.integer,)): return int(x)
    if isinstance(x, (np.floating,)): return float(x)
    return str(x)


def self_test():
    assert np.allclose(finite_mean_groups(np.arange(20, dtype=float))[0], [4.5, 14.5])
    assert finite_mean_groups(np.array([np.nan] * 10))[1] == 10
    n = 140
    s = np.full(n, 20000., dtype=float)
    s[60:90] = 20100.
    s[90:] = 20000.
    events = event_candidates(s, threshold_pct=0.2, minimum_gap=20, maximum=5)
    assert any(i == 60 for i, _ in events) and any(i == 90 for i, _ in events)
    evp = np.full(n, 3500., dtype=float)
    result = event_metrics(events, {"u110_V": s * 5, "u20_V": s, "ev_u_V": s / 87, "ev_p_W": evp,
                                    "i20_A": s / 2000, "p110_MW": s / 10000},
                           np.full(n, "synthetic"), 500)
    assert len(result) == len(events)
    print("PASS: pure-function synthetic tests only. These are NOT measured KIT findings.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", type=Path, default=Path.home() / "Downloads/KIT_OLTC_22826984")
    parser.add_argument("--out", type=Path, default=Path.home() / "Downloads/KIT_OLTC_Electrical_Results")
    parser.add_argument("--batch-size", type=int, default=100_000)
    parser.add_argument("--step-threshold-pct", type=float, default=0.15,
                        help="Absolute 1-second 20 kV voltage change in percent, candidate screening only")
    parser.add_argument("--min-event-gap-s", type=int, default=45)
    parser.add_argument("--max-events", type=int, default=60)
    parser.add_argument("--exchange-threshold-w", type=float, default=500.0,
                        help="Absolute EV point P threshold for significant exchange, NOT verified charging activity")
    parser.add_argument("--phase-filter", default="", help="Optional substring of source fault_phase label")
    parser.add_argument("--reuse-summaries", action="store_true", help="Reuse prior 1s Parquet files, if they have expected row counts")
    parser.add_argument("--self-test", action="store_true", help="Run synthetic algorithm tests without reading raw files")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.batch_size <= 0 or args.min_event_gap_s <= 0 or args.max_events <= 0 or args.step_threshold_pct <= 0:
        parser.error("batch size, event gap, max events, and threshold must be positive")

    import pyarrow.parquet as pq
    args.out.mkdir(parents=True, exist_ok=True)
    stats = {}
    for key, spec in SOURCES.items():
        path = args.out / f"{key}_1s.parquet"
        if args.reuse_summaries and path.is_file() and pq.ParquetFile(path).metadata.num_rows == EXPECTED_SECONDS:
            stats[key] = {"source_filename": spec["name"], "reused_summary": True, "bins": EXPECTED_SECONDS}
            print(f"Reusing: {path}")
            continue
        print(f"Original -> 1-second streaming mean: {spec['name']}", flush=True)
        stats[key] = source_aggregate(key, args.folder, path, args.batch_size)

    # Exactly one-second aligned bins: 4,320,000 per component (verified in local QA).
    grid110 = pq.read_table(args.out / "grid110_1s.parquet",
                            columns=["second_index", "u_pos_V", "p_MW"])
    grid20 = pq.read_table(args.out / "grid20_1s.parquet",
                           columns=["second_index", "fault_phase_at_second_start", "u_pos_V", "i_pos_A"])
    ev400 = pq.read_table(args.out / "ev400_1s.parquet",
                           columns=["second_index", "u_L1_V", "u_L2_V", "u_L3_V",
                                    "p_L1_W", "p_L2_W", "p_L3_W"])
    for label, table in [("110", grid110), ("20", grid20), ("EV", ev400)]:
        if table.num_rows != EXPECTED_SECONDS:
            raise RuntimeError(f"Unexpected one-second row count for {label}: {table.num_rows}")
    signals = {
        "u110_V": read_col(grid110, "u_pos_V"),
        "u20_V": read_col(grid20, "u_pos_V"),
        "ev_u_V": make_ev_voltage(ev400),
        "ev_p_W": make_ev_power(ev400),
        "i20_A": read_col(grid20, "i_pos_A"),
        "p110_MW": read_col(grid110, "p_MW"),
    }
    # Compare second_index rather than blindly concatenating source files.
    import pyarrow as pa
    for tbl in (grid110, grid20, ev400):
        second_index = np.asarray(tbl["second_index"].to_numpy(zero_copy_only=False))
        if not np.array_equal(second_index, np.arange(EXPECTED_SECONDS, dtype=np.int32)):
            raise RuntimeError("one-second index mismatch")

    phases = np.asarray(grid20["fault_phase_at_second_start"].to_pylist(), dtype=object)
    counts = Counter(str(x) for x in phases)
    events = event_candidates(signals["u20_V"], args.step_threshold_pct,
                              args.min_event_gap_s, args.max_events, phases, args.phase_filter)
    rows = event_metrics(events, signals, phases, args.exchange_threshold_w)
    event_csv = args.out / "event_metrics.csv"
    if rows:
        with event_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    else:
        event_csv.write_text("No candidates met threshold; adjust --step-threshold-pct after inspecting signals.\n", encoding="utf-8")

    figures = save_figures(args.out, signals, events)
    summary = {
        "source": DATASET,
        "time_range_first_utc": FIRST_UTC.isoformat(),
        "time_grid_ms": 100,
        "aggregation": "finite-valued arithmetic mean for each ten 100ms samples into 1s means",
        "raw_timeseries_not_modified": True,
        "original_time_test": "user-terminal original files passed exact 100ms grid 129600000/129600000 earlier; not rerun here",
        "source_qualification": "Multivoltage electrical measurements; exact feeder parentage unverified; no observed thermal channels",
        "files": stats,
        "measured_signal_valid_1s_counts": {k: int(np.isfinite(v).sum()) for k, v in signals.items()},
        "fault_phase_20kV_seconds": dict(counts),
        "event_selection": {"trigger": "abs(20kV u_pos 1-second percent step)",
                            "threshold_pct": args.step_threshold_pct,
                            "min_event_gap_s": args.min_event_gap_s,
                            "max_events": args.max_events,
                            "source_label_filter": args.phase_filter,
                            "pre_median_seconds": "event-20 through event-6",
                            "post_median_seconds": "event+5 through event+19",
                            "ev_power_exchange_threshold_W": args.exchange_threshold_w},
        "event_count": len(events),
        "events_with_significant_ev_real_power_pre": sum(int(r["ev_significant_exchange_pre"]) for r in rows),
        "event_metrics_csv": event_csv.name,
        "figures": figures,
        "scientific_limitations": [
            "The 20kV file lacks a measured active-power column; i_pos_A is not active power.",
            "No verified transformer->EV point feeder/asset path, CT/PT sign and phase conventions, or external clock calibration.",
            "The fault_phase label is source metadata; its control-state meaning must be checked against publisher documentation.",
            "Averaging 100ms measurements into 1s attenuates sub-second events; figures and metrics use 1s, not raw 100ms dynamic responses.",
            "Charging point three-phase P is the sum of three measured phase P values only if all phase readings are finite.",
            "Power sign convention and whether EV draw is positive are not independently qualified.",
            "Identical timestamps/correlated events are not a proof of a unique circuit path or of directional causality.",
            "The OLTC anomaly is electrical regulation, not an extreme-heat thermal disturbance.",
            "No measured transformer temperatures, EVSE internal temperature, thermal derating, battery SOC, or mobility-service demands.",
            "Selected high-amplitude 20kV steps are an exploratory selection, not an unbiased causal effect or system-wide estimate.",
        ],
    }
    (args.out / "analysis_summary.json").write_text(json.dumps(summary, indent=2, default=jsonable) + "\n", encoding="utf-8")
    print("\n--- SOURCE-GROUNDED KIT ELECTRICAL RESPONSE ---")
    print(f"Original: {DATASET}")
    print(f"Candidate 20 kV voltage steps: {len(events)}")
    print(f"Events with substantial pre-event EV real-power exchange: {summary['events_with_significant_ev_real_power_pre']}")
    print(f"Source fault-phase labels (seconds): {dict(counts)}")
    print(f"Results: {args.out}")
    print("CONSTRAINT: electrical response only; NO inference of heat-induced derating or exact feeder causality")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())