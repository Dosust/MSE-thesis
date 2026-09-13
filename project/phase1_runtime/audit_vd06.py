#!/usr/bin/env python3
"""Post-failure forensic audit for Phase-1 ACN V-D06.

Diagnostic only. This script does not alter raw data, thresholds, v1 processing,
or H1/H2. It quantifies candidate mechanisms after the preserved v1 failure.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

RFC1123 = "%a, %d %b %Y %H:%M:%S GMT"
NOMINAL_VOLTAGE_V = 208.0


def parse_ts(values):
    """Parse ACN RFC-1123 timestamps with one explicit ISO fallback."""
    try:
        return pd.to_datetime(values, format=RFC1123, utc=True)
    except Exception:
        return pd.to_datetime(values, utc=True)


def integrate_piecewise_linear(ts, values, start, end):
    """Integrate a single-valued piecewise-linear current trace."""
    x = np.asarray(ts.astype("int64"), dtype=float) / 1e9
    y = np.asarray(values, dtype=float)
    lo = max(float(start.timestamp()), float(x[0]))
    hi = min(float(end.timestamp()), float(x[-1]))
    if hi <= lo:
        return 0.0
    interior = x[(x > lo) & (x < hi)]
    grid = np.concatenate(([lo], interior, [hi]))
    vals = np.interp(grid, x, y)
    return float(np.trapezoid(vals, grid))


def read_days(path: Path):
    return {
        date.fromisoformat(x.strip())
        for x in path.read_text(encoding="utf-8").splitlines()
        if x.strip()
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-jsonl", type=Path, required=True)
    parser.add_argument("--processed-dir", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, required=True)
    args = parser.parse_args()

    proc = args.processed_dir
    qc = pd.read_csv(proc / "session_qc.csv")
    accepted = set(qc.loc[qc["state"] == "ACCEPTED", "session_id"].astype(str))
    rejected_current_dup = set(
        qc.loc[
            (qc["state"] == "REJECTED")
            & (
                qc["reason"]
                == "chargingCurrent timestamps must be strictly increasing"
            ),
            "session_id",
        ].astype(str)
    )
    cal_days = read_days(proc / "calibration_days.txt")
    val_days = read_days(proc / "validation_days.txt")

    rows = []
    dup_pairs = 0
    dup_pairs_same = 0
    dup_pairs_diff = 0
    dup_sessions_diff = 0
    duplicate_only_sessions = 0

    with args.raw_jsonl.open("r", encoding="utf-8") as handle:
        for line in handle:
            obj = json.loads(line)
            sid = str(obj.get("sessionID"))

            if sid in rejected_current_dup:
                current_obj = obj.get("chargingCurrent")
                if (
                    isinstance(current_obj, dict)
                    and "timestamps" in current_obj
                    and "current" in current_obj
                ):
                    raw_ts = current_obj["timestamps"]
                    cur = np.asarray(current_obj["current"], dtype=float)
                    ts = parse_ts(raw_ts)
                    ns = np.asarray(ts.astype("int64"))
                    delta = np.diff(ns)
                    duplicates = np.where(delta == 0)[0]
                    decreases = np.where(delta < 0)[0]
                    if len(decreases) == 0:
                        duplicate_only_sessions += 1
                    dup_pairs += len(duplicates)
                    same = sum(
                        float(cur[i]) == float(cur[i + 1]) for i in duplicates
                    )
                    different = len(duplicates) - same
                    dup_pairs_same += same
                    dup_pairs_diff += different
                    if different:
                        dup_sessions_diff += 1

            if sid not in accepted:
                continue

            current_obj = obj["chargingCurrent"]
            ts = parse_ts(current_obj["timestamps"])
            current = np.asarray(current_obj["current"], dtype=float)
            connection = parse_ts([obj["connectionTime"]])[0]
            disconnect = parse_ts([obj["disconnectTime"]])[0]
            done = (
                parse_ts([obj["doneChargingTime"]])[0]
                if obj.get("doneChargingTime")
                else disconnect
            )
            done_end = min(done, disconnect)

            amp_s_disconnect = integrate_piecewise_linear(
                ts, current, connection, disconnect
            )
            amp_s_done = integrate_piecewise_linear(
                ts, current, connection, done_end
            )
            e_disconnect = (
                NOMINAL_VOLTAGE_V
                * amp_s_disconnect
                / (1000.0 * 3600.0)
            )
            e_done = (
                NOMINAL_VOLTAGE_V * amp_s_done / (1000.0 * 3600.0)
            )
            e_data = float(obj["kWhDelivered"])
            local_day = connection.tz_convert("America/Los_Angeles").date()
            split = (
                "calibration"
                if local_day in cal_days
                else ("validation" if local_day in val_days else "other")
            )

            rows.append(
                {
                    "sid": sid,
                    "station": str(obj.get("spaceID")),
                    "local_date": local_day,
                    "split": split,
                    "e_data": e_data,
                    "e_disconnect": e_disconnect,
                    "e_done": e_done,
                    "gap_start_s": float((ts[0] - connection).total_seconds()),
                    "gap_end_s": float((disconnect - ts[-1]).total_seconds()),
                    "duration_h": float(
                        (disconnect - connection).total_seconds() / 3600.0
                    ),
                }
            )

    df = pd.DataFrame(rows)
    df_nonzero = df[df["e_data"] > 0].copy()
    df_nonzero["ratio_disconnect"] = (
        df_nonzero["e_disconnect"] / df_nonzero["e_data"]
    )
    df_nonzero["ratio_done"] = df_nonzero["e_done"] / df_nonzero["e_data"]
    df_nonzero["v_implied_done"] = NOMINAL_VOLTAGE_V / df_nonzero[
        "ratio_done"
    ].replace(0, np.nan)

    coverage_late_start = int((df["gap_start_s"] > 300).sum())
    coverage_early_end = int((df["gap_end_s"] > 300).sum())

    cal = df_nonzero[
        (df_nonzero["split"] == "calibration")
        & np.isfinite(df_nonzero["v_implied_done"])
    ].copy()
    val = df_nonzero[df_nonzero["split"] == "validation"].copy()
    v_eff_cal = float(np.median(cal["v_implied_done"]))
    val["e_diag_calibrated"] = (
        val["e_done"] * v_eff_cal / NOMINAL_VOLTAGE_V
    )

    day_diag = (
        val.groupby("local_date", as_index=False)
        .agg(
            sessions=("sid", "size"),
            e_diag=("e_diag_calibrated", "sum"),
            e_data=("e_data", "sum"),
        )
    )
    day_diag["epsilon"] = np.abs(
        day_diag["e_diag"] - day_diag["e_data"]
    ) / np.maximum(day_diag["e_data"], 1e-12)

    val["abs_rel_error_disconnect"] = np.abs(
        val["e_disconnect"] - val["e_data"]
    ) / np.maximum(val["e_data"], 1e-12)
    top_outliers = (
        val.sort_values("abs_rel_error_disconnect", ascending=False)
        .head(10)[
            [
                "sid",
                "station",
                "local_date",
                "e_data",
                "e_disconnect",
                "e_done",
                "duration_h",
                "abs_rel_error_disconnect",
            ]
        ]
        .copy()
    )
    top_outliers["local_date"] = top_outliers["local_date"].astype(str)

    power = pd.read_csv(proc / "power_5min.csv")
    cal_power = power[
        power["local_date"].astype(str).isin(
            {d.isoformat() for d in cal_days}
        )
    ]

    energy = pd.read_csv(proc / "energy_reconstruction.csv")
    val_energy = energy[
        (energy["split"] == "validation") & (energy["sessions"] > 0)
    ]

    report = {
        "status": "POST_FAILURE_DIAGNOSTIC_ONLY",
        "v1_preserved": True,
        "nominal_voltage_v": NOMINAL_VOLTAGE_V,
        "source_sessions": int(len(qc)),
        "accepted_sessions_v1": int((qc["state"] == "ACCEPTED").sum()),
        "rejected_sessions_v1": int((qc["state"] == "REJECTED").sum()),
        "v1_usable_days": int(
            sum(
                1
                for line in (proc / "usable_days.txt").read_text().splitlines()
                if line.strip()
            )
        ),
        "v1_calibration_days": int(len(cal_days)),
        "v1_validation_days": int(len(val_days)),
        "v1_V_D06_validation_median_epsilon": float(
            val_energy["epsilon_E"].median()
        ),
        "v1_V_D06_threshold": 0.01,
        "v1_V_D06_state": "FAIL",
        "time_support": {
            "accepted_sessions_with_first_sample_more_than_5min_after_connection": coverage_late_start,
            "accepted_sessions_with_last_sample_more_than_5min_before_disconnect": coverage_early_end,
        },
        "duplicate_timestamp_diagnostics": {
            "strict_current_nonincreasing_rejections": int(
                len(rejected_current_dup)
            ),
            "duplicate_only_no_backward_time_sessions": int(
                duplicate_only_sessions
            ),
            "duplicate_pairs_total": int(dup_pairs),
            "duplicate_pairs_same_value": int(dup_pairs_same),
            "duplicate_pairs_different_value": int(dup_pairs_diff),
            "sessions_with_at_least_one_different_value_duplicate": int(
                dup_sessions_diff
            ),
        },
        "nominal_voltage_disconnect_ratio": {
            "session_median_Erecon_over_Edata": float(
                df_nonzero["ratio_disconnect"].median()
            ),
            "session_median_abs_relative_error": float(
                np.median(
                    np.abs(
                        df_nonzero["e_disconnect"] - df_nonzero["e_data"]
                    )
                    / df_nonzero["e_data"]
                )
            ),
        },
        "doneChargingTime_diagnostic": {
            "session_median_Erecon_over_Edata": float(
                df_nonzero["ratio_done"].median()
            ),
            "session_median_abs_relative_error": float(
                np.median(
                    np.abs(df_nonzero["e_done"] - df_nonzero["e_data"])
                    / df_nonzero["e_data"]
                )
            ),
        },
        "calibration_only_global_effective_voltage_diagnostic": {
            "V_eff_calibration_median_v": v_eff_cal,
            "validation_day_median_epsilon_after_done_cutoff_and_global_calibration": float(
                day_diag["epsilon"].median()
            ),
            "validation_day_max_epsilon_after_done_cutoff_and_global_calibration": float(
                day_diag["epsilon"].max()
            ),
            "note": (
                "diagnostic only; designed after v1 failure and therefore not "
                "confirmatory on the exposed v1 validation set"
            ),
        },
        "calibration_power_reference": {
            "P_ref_median_kw": float(cal_power["p_kw"].median()),
            "zero_slot_fraction": float((cal_power["p_kw"] == 0).mean()),
            "mean_kw": float(cal_power["p_kw"].mean()),
        },
        "top_validation_session_outliers": top_outliers.to_dict(
            orient="records"
        ),
        "diagnostic_validation_days": [
            {
                "local_date": str(row.local_date),
                "sessions": int(row.sessions),
                "epsilon_after_done_cutoff_and_global_calibration": float(
                    row.epsilon
                ),
            }
            for row in day_diag.itertuples(index=False)
        ],
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
