"""Build frozen Phase-1 information artifacts from processed ACN power data."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

import numpy as np

from phase1_exec.acn_processing import sha256_file
from phase1_exec.information_processing import (
    DailyPower,
    SITE_CAP_KW,
    forecast_day,
    loo_calibration_residuals,
    paired_validation_rmse,
    persistence_forecast,
    reference_power_kw,
    seasonal_slot_means,
)


def read_days(path: Path) -> tuple[date, ...]:
    values = tuple(
        date.fromisoformat(line.strip())
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )
    if not values:
        raise SystemExit(f"empty day list: {path}")
    return values


def read_power(path: Path) -> dict[date, DailyPower]:
    buckets: dict[date, list[tuple[int, float]]] = {}
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"local_date", "slot", "p_kw"}
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise SystemExit(f"power CSV missing fields: {sorted(required)}")
        for row in reader:
            d = date.fromisoformat(row["local_date"])
            buckets.setdefault(d, []).append((int(row["slot"]), float(row["p_kw"])))

    out: dict[date, DailyPower] = {}
    for d, rows in buckets.items():
        rows.sort(key=lambda x: x[0])
        slots = [slot for slot, _ in rows]
        if slots != list(range(288)):
            raise SystemExit(f"{d} does not contain slots 0..287 exactly once")
        out[d] = DailyPower(d, tuple(value for _, value in rows))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--processed-acn", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    source = args.processed_acn
    out = args.out
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty information dir: {out}")
    out.mkdir(parents=True, exist_ok=True)

    power = read_power(source / "power_5min.csv")
    usable_dates = read_days(source / "usable_days.txt")
    cal_dates = read_days(source / "calibration_days.txt")
    val_dates = read_days(source / "validation_days.txt")

    if set(cal_dates) & set(val_dates):
        raise SystemExit("calibration and validation day lists overlap")
    if tuple(sorted(cal_dates + val_dates)) != tuple(sorted(usable_dates)):
        raise SystemExit("calibration + validation dates do not equal usable-day set")
    if not set(usable_dates).issubset(power):
        raise SystemExit("one or more usable days are absent from power_5min.csv")

    calibration = [power[d] for d in cal_dates]
    validation = [power[d] for d in val_dates]
    all_usable = [power[d] for d in usable_dates]

    means = seasonal_slot_means(calibration)
    residuals, residual_index = loo_calibration_residuals(calibration)
    p_ref = reference_power_kw(calibration)

    slot_means_path = out / "seasonal_slot_means.csv"
    with slot_means_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["day_type", "slot", "mean_p_kw"])
        for key in ("weekday", "weekend"):
            for slot, value in enumerate(means[key]):
                writer.writerow([key, slot, format(float(value), ".17g")])

    residual_path = out / "calibration_loo_residuals.csv"
    with residual_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["local_date", "slot", "residual_kw"])
        for (d, slot), value in zip(residual_index, residuals):
            writer.writerow([d.isoformat(), slot, format(float(value), ".17g")])

    forecast_path = out / "validation_forecasts.csv"
    with forecast_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "local_date",
                "slot",
                "observed_kw",
                "seasonal_slot_kw",
                "persistence_source_date",
                "persistence_kw",
            ]
        )
        for target in sorted(validation, key=lambda x: x.local_date):
            seasonal = forecast_day(target, means)
            source_day, persistence = persistence_forecast(target, all_usable)
            for slot in range(288):
                writer.writerow(
                    [
                        target.local_date.isoformat(),
                        slot,
                        format(float(target.power_kw[slot]), ".17g"),
                        format(float(seasonal[slot]), ".17g"),
                        source_day.isoformat(),
                        format(float(persistence[slot]), ".17g"),
                    ]
                )

    rmse_slot, rmse_persistence, used_days = paired_validation_rmse(
        validation, all_usable, means
    )
    vi04_state = "PASS" if rmse_slot <= rmse_persistence else "FAIL"

    params = {
        "P_ref_kw": p_ref,
        "P_site_cap_kw": SITE_CAP_KW,
        "latency_minutes": [0, 5, 15, 30],
        "latency_steps": [0, 1, 3, 6],
        "calibration_days_sha256": sha256_file(source / "calibration_days.txt"),
        "validation_days_sha256": sha256_file(source / "validation_days.txt"),
        "seasonal_slot_means_sha256": sha256_file(slot_means_path),
        "loo_residuals_sha256": sha256_file(residual_path),
        "residual_count": int(residuals.size),
        "residual_mean_kw": float(np.mean(residuals)),
        "residual_std_kw": float(np.std(residuals, ddof=1)),
    }
    params_path = out / "information_parameters.json"
    params_path.write_text(
        json.dumps(params, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )

    verification = {
        "paired_validation_days": used_days,
        "RMSE_seasonal_slot_kw": rmse_slot,
        "RMSE_persistence_kw": rmse_persistence,
        "V_I04_rule": "RMSE_seasonal_slot <= RMSE_persistence",
        "V_I04_state": vi04_state,
    }
    verification_path = out / "information_verification.json"
    verification_path.write_text(
        json.dumps(verification, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    output_names = [
        "seasonal_slot_means.csv",
        "calibration_loo_residuals.csv",
        "validation_forecasts.csv",
        "information_parameters.json",
        "information_verification.json",
    ]
    manifest = {
        "processing_rule": "PHASE1_INFORMATION_PROCESSING_PROTOCOL_V1",
        "source_processing_manifest_sha256": sha256_file(
            source / "processing_manifest.json"
        ),
        "outputs_sha256": {name: sha256_file(out / name) for name in output_names},
        "V_I04_state": vi04_state,
    }
    manifest_path = out / "information_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                **verification,
                "information_manifest_sha256": sha256_file(manifest_path),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
