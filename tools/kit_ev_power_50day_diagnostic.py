#!/usr/bin/env python3
"""Read-only KIT EV-point 50-day active-power diagnostic from a prior 1 s Parquet.

Uses measured per-phase derived 1 s average powers, reported in W. Does not
establish EV battery charging, verified meter sign or extreme-heat derating.
Source original: https://doi.org/10.5281/zenodo.22826984
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

START_UTC = datetime(2026, 2, 3, 23, tzinfo=timezone.utc)
EXPECTED_SECONDS = 4_320_000
THRESHOLDS_W = (100, 500, 1000, 3000)
COLUMNS = (
    "second_index", "p_L1_W", "p_L2_W", "p_L3_W",
    "fault_phase_at_second_start",
)


def read_batch_arrays(batch):
    times = batch.column(0).to_numpy(zero_copy_only=False)
    phases = [
        np.asarray(batch.column(i).to_numpy(zero_copy_only=False), dtype=np.float64)
        for i in (1, 2, 3)
    ]
    labels = np.asarray(batch.column(4).to_pylist(), dtype=object)
    return times, phases, labels


def summarize_batches(batches, expected_seconds=None):
    valid_count = 0
    rows_seen = 0
    minimum = float("inf")
    maximum = float("-inf")
    peak = float("-inf")
    peak_second = None
    peak_signed = None
    threshold_counts = Counter({int(t): 0 for t in THRESHOLDS_W})
    labels_at_500W = Counter()
    examples = []
    next_second = 0

    for times, phases, labels in batches:
        if len(times) != len(labels) or any(len(p) != len(times) for p in phases):
            raise ValueError("Mismatched derived input columns")
        if len(times) and not np.array_equal(times, np.arange(next_second, next_second + len(times))):
            raise ValueError("Derived one-second index is incomplete or out of order")
        next_second += len(times)
        rows_seen += len(times)
        valid = np.logical_and.reduce([np.isfinite(x) for x in phases])
        if not np.any(valid):
            continue
        power = sum(phase[valid] for phase in phases)
        seconds = times[valid]
        phase_names = labels[valid]
        absolute = np.abs(power)
        valid_count += len(power)
        minimum = min(minimum, float(power.min()))
        maximum = max(maximum, float(power.max()))
        i = int(absolute.argmax())
        if absolute[i] > peak:
            peak = float(absolute[i])
            peak_second = int(seconds[i])
            peak_signed = float(power[i])
        for threshold in THRESHOLDS_W:
            matches = absolute >= threshold
            threshold_counts[threshold] += int(matches.sum())
            if threshold == 500 and np.any(matches):
                labels_at_500W.update(str(label) for label in phase_names[matches])
                if len(examples) < 5:
                    for j in np.flatnonzero(matches)[:5 - len(examples)]:
                        examples.append({
                            "utc": (START_UTC + timedelta(seconds=int(seconds[j]))).isoformat(),
                            "signed_power_W": float(power[j]),
                            "source_fault_phase_label": str(phase_names[j]),
                        })

    if expected_seconds is not None and rows_seen != expected_seconds:
        raise ValueError(f"Expected {expected_seconds} derived seconds; found {rows_seen}")

    return {
        "dataset": "https://doi.org/10.5281/zenodo.22826984",
        "input_data_type": "derived 1 s means of measured EV-point three-phase active powers",
        "period_start_utc": START_UTC.isoformat(),
        "total_one_second_rows": rows_seen,
        "valid_three_phase_power_seconds": valid_count,
        "invalid_three_phase_power_seconds": rows_seen - valid_count,
        "valid_fraction_pct": round(100 * valid_count / rows_seen, 6) if rows_seen else None,
        "minimum_signed_power_W": minimum if valid_count else None,
        "maximum_signed_power_W": maximum if valid_count else None,
        "maximum_absolute_power_W": peak if valid_count else None,
        "maximum_absolute_power_signed_W": peak_signed,
        "maximum_absolute_power_utc": (
            (START_UTC + timedelta(seconds=peak_second)).isoformat()
            if peak_second is not None else None
        ),
        "valid_seconds_by_absolute_power_threshold": {
            str(t): {"seconds": threshold_counts[t],
                     "fraction_of_valid_pct": round(100 * threshold_counts[t] / valid_count, 6)
                     if valid_count else None}
            for t in THRESHOLDS_W
        },
        "source_fault_phase_labels_for_abs_power_at_least_500W": dict(labels_at_500W),
        "first_five_seconds_with_abs_power_at_least_500W": examples,
        "limitations": [
            "This is the distribution of 1-second aggregate meter P; the charging/discharging sign convention is not independently verified.",
            "The 1-second average can hide 100 ms excursions and cannot prove EV battery charge status or service delivered.",
            "No measured ambient, EVSE internal temperature, thermal derating or mobility service outcome is evaluated.",
        ],
    }


def synthetic_self_test():
    p1 = np.array([1.0, 100.0, 1000.0, np.nan])
    p2 = np.array([2.0, 200.0, 2000.0, 1.0])
    p3 = np.array([3.0, 300.0, 3000.0, 2.0])
    labels = np.array(["pre_fault", "fault", "fault", "post_fault"])
    s = summarize_batches([(np.arange(4), (p1, p2, p3), labels)], expected_seconds=4)
    assert s["valid_three_phase_power_seconds"] == 3
    assert s["minimum_signed_power_W"] == 6.0
    assert s["maximum_absolute_power_W"] == 6000.0
    assert s["valid_seconds_by_absolute_power_threshold"]["500"]["seconds"] == 2
    assert s["source_fault_phase_labels_for_abs_power_at_least_500W"] == {"fault": 2}
    assert s["first_five_seconds_with_abs_power_at_least_500W"][0]["signed_power_W"] == 600.0
    print("PASS: synthetic self-test; not a measured KIT finding")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path,
                    default=Path.home() / "Downloads/KIT_OLTC_Electrical_Results/ev400_1s.parquet")
    ap.add_argument("--out", type=Path,
                    default=Path.home() / "Downloads/KIT_OLTC_Electrical_Results/ev_power_50day_diagnostic.json")
    ap.add_argument("--batch-size", type=int, default=100_000)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        synthetic_self_test()
        return
    if args.batch_size <= 0:
        ap.error("--batch-size must be positive")
    if not args.input.is_file():
        ap.error(f"Input missing: {args.input}")

    import pyarrow.parquet as pq
    pf = pq.ParquetFile(args.input)
    if pf.metadata.num_rows != EXPECTED_SECONDS:
        ap.error(f"Expected {EXPECTED_SECONDS} one-second records, got {pf.metadata.num_rows}")
    missing = [name for name in COLUMNS if name not in pf.schema_arrow.names]
    if missing:
        ap.error(f"Missing columns: {missing}")

    batches = (read_batch_arrays(batch) for batch in pf.iter_batches(
        batch_size=args.batch_size, columns=list(COLUMNS)))
    report = summarize_batches(batches, expected_seconds=EXPECTED_SECONDS)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print("=== KIT FULL 50-DAY EV-POINT POWER (1 s means) ===")
    print("Valid seconds:", report["valid_three_phase_power_seconds"])
    print("Min signed power (W):", report["minimum_signed_power_W"])
    print("Max signed power (W):", report["maximum_signed_power_W"])
    print("Max absolute power (W):", report["maximum_absolute_power_W"])
    print("Peak time UTC:", report["maximum_absolute_power_utc"])
    for threshold, data in report["valid_seconds_by_absolute_power_threshold"].items():
        print(f"Seconds |P| >= {threshold} W: {data['seconds']} ({data['fraction_of_valid_pct']}% of valid)")
    print("First >= 500 W examples:", report["first_five_seconds_with_abs_power_at_least_500W"])
    print("JSON saved:", args.out)
    print("LIMIT: source meter power, not verified battery charging or thermal derating")


if __name__ == "__main__":
    main()