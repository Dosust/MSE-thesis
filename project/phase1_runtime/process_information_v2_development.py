"""Build Phase-1 v2 information development artifacts only.

Uses the corrected 2019 development charging trajectory. No fresh holdout is
read and no V-I04 decision is made here.
"""
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
    loo_calibration_residuals,
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
        raise SystemExit(f"empty development day list: {path}")
    return values


def read_power(path: Path) -> dict[date, DailyPower]:
    buckets: dict[date, list[tuple[int, float]]] = {}
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"local_date", "slot", "p_kw"}
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise SystemExit(f"v2 power CSV missing fields: {sorted(required)}")
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
    parser.add_argument("--development-acn", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    source = args.development_acn
    out = args.out
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty v2 information dir: {out}")
    out.mkdir(parents=True, exist_ok=True)

    power = read_power(source / "power_5min_v2.csv")
    development_dates = read_days(source / "development_days.txt")
    if not set(development_dates).issubset(power):
        raise SystemExit("one or more v2 development days are absent from power CSV")

    development = [power[d] for d in development_dates]
    means = seasonal_slot_means(development)
    residuals, residual_index = loo_calibration_residuals(development)
    p_ref = reference_power_kw(development)

    slot_means_path = out / "seasonal_slot_means_v2.csv"
    with slot_means_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["day_type", "slot", "mean_p_kw"])
        for key in ("weekday", "weekend"):
            for slot, value in enumerate(means[key]):
                writer.writerow([key, slot, format(float(value), ".17g")])

    residual_path = out / "development_loo_residuals_v2.csv"
    with residual_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["local_date", "slot", "residual_kw"])
        for (d, slot), value in zip(residual_index, residuals):
            writer.writerow([d.isoformat(), slot, format(float(value), ".17g")])

    params = {
        "development_only": True,
        "P_ref_kw": p_ref,
        "P_site_cap_kw": SITE_CAP_KW,
        "latency_minutes": [0, 5, 15, 30],
        "latency_steps": [0, 1, 3, 6],
        "development_days_sha256": sha256_file(source / "development_days.txt"),
        "source_development_manifest_sha256": sha256_file(
            source / "development_manifest_v2.json"
        ),
        "seasonal_slot_means_sha256": sha256_file(slot_means_path),
        "loo_residuals_sha256": sha256_file(residual_path),
        "residual_count": int(residuals.size),
        "residual_mean_kw": float(np.mean(residuals)),
        "residual_std_kw": float(np.std(residuals, ddof=1)),
    }
    params_path = out / "information_parameters_v2.json"
    params_path.write_text(
        json.dumps(params, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )

    output_names = [
        "seasonal_slot_means_v2.csv",
        "development_loo_residuals_v2.csv",
        "information_parameters_v2.json",
    ]
    manifest = {
        "processing_rule": "PHASE1_INFORMATION_V2_DEVELOPMENT",
        "development_only": True,
        "outputs_sha256": {name: sha256_file(out / name) for name in output_names},
    }
    manifest_path = out / "information_development_manifest_v2.json"
    manifest_path.write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "P_ref_kw": p_ref,
                "development_day_count": len(development_dates),
                "residual_count": int(residuals.size),
                "information_development_manifest_sha256": sha256_file(manifest_path),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
