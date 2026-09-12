"""Frozen information-processing operators for Phase-1 verification.

These functions implement only the preregistered low-dimensional information
model. They do not tune against holdout outcomes.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date
from typing import Dict, Iterable, Mapping, Sequence, Tuple

import numpy as np

SLOTS_PER_DAY = 288
SITE_CAP_KW = 150.0
LATENCY_STEPS = (0, 1, 3, 6)


class InformationProcessingError(ValueError):
    """Raised when the frozen information-processing contract cannot be applied."""


@dataclass(frozen=True)
class DailyPower:
    local_date: date
    power_kw: Tuple[float, ...]

    def __post_init__(self) -> None:
        if len(self.power_kw) != SLOTS_PER_DAY:
            raise InformationProcessingError(
                f"daily trajectory must have {SLOTS_PER_DAY} slots"
            )
        if not all(math.isfinite(float(x)) and float(x) >= 0.0 for x in self.power_kw):
            raise InformationProcessingError(
                "daily power must be finite and nonnegative"
            )


def day_type(day: date) -> str:
    return "weekday" if day.weekday() < 5 else "weekend"


def _by_date(days: Iterable[DailyPower]) -> Dict[date, DailyPower]:
    out: Dict[date, DailyPower] = {}
    for item in days:
        if item.local_date in out:
            raise InformationProcessingError(f"duplicate day {item.local_date}")
        out[item.local_date] = item
    return out


def seasonal_slot_means(
    calibration: Sequence[DailyPower],
) -> Mapping[str, np.ndarray]:
    groups: Dict[str, list[np.ndarray]] = {"weekday": [], "weekend": []}
    for item in calibration:
        groups[day_type(item.local_date)].append(np.asarray(item.power_kw, dtype=float))
    if not groups["weekday"] or not groups["weekend"]:
        raise InformationProcessingError(
            "both weekday and weekend classes require calibration days"
        )
    return {
        key: np.mean(np.stack(values, axis=0), axis=0)
        for key, values in groups.items()
    }


def forecast_day(
    item: DailyPower, means: Mapping[str, np.ndarray]
) -> np.ndarray:
    key = day_type(item.local_date)
    if key not in means:
        raise InformationProcessingError(f"missing slot mean for {key}")
    values = np.asarray(means[key], dtype=float)
    if values.shape != (SLOTS_PER_DAY,):
        raise InformationProcessingError("slot-mean vector has wrong shape")
    return values.copy()


def loo_calibration_residuals(
    calibration: Sequence[DailyPower],
) -> Tuple[np.ndarray, Tuple[Tuple[date, int], ...]]:
    grouped: Dict[str, list[DailyPower]] = {"weekday": [], "weekend": []}
    for item in calibration:
        grouped[day_type(item.local_date)].append(item)
    for key, values in grouped.items():
        if len(values) < 2:
            raise InformationProcessingError(
                f"{key} requires at least two calibration days for LOO residuals"
            )

    residuals = []
    index = []
    for key in ("weekday", "weekend"):
        values = grouped[key]
        matrix = np.stack(
            [np.asarray(item.power_kw, dtype=float) for item in values], axis=0
        )
        total = matrix.sum(axis=0)
        denom = len(values) - 1
        for row, item in zip(matrix, values):
            loo_mean = (total - row) / denom
            r = row - loo_mean
            residuals.extend(r.tolist())
            index.extend((item.local_date, slot) for slot in range(SLOTS_PER_DAY))
    return np.asarray(residuals, dtype=float), tuple(index)


def reference_power_kw(calibration: Sequence[DailyPower]) -> float:
    if not calibration:
        raise InformationProcessingError("empty calibration set")
    values = np.concatenate(
        [np.asarray(item.power_kw, dtype=float) for item in calibration]
    )
    return float(np.median(values))


def persistence_forecast(
    target: DailyPower, all_usable: Sequence[DailyPower]
) -> Tuple[date, np.ndarray]:
    lookup = _by_date(all_usable)
    earlier = [day for day in lookup if day < target.local_date]
    if not earlier:
        raise InformationProcessingError("no prior usable day for persistence")
    source_day = max(earlier)
    return source_day, np.asarray(lookup[source_day].power_kw, dtype=float).copy()


def rmse(observed: Sequence[float], predicted: Sequence[float]) -> float:
    y = np.asarray(observed, dtype=float)
    p = np.asarray(predicted, dtype=float)
    if y.shape != p.shape or y.size == 0:
        raise InformationProcessingError("RMSE arrays must be nonempty and equal shape")
    if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)):
        raise InformationProcessingError("RMSE inputs must be finite")
    return float(np.sqrt(np.mean((p - y) ** 2)))


def paired_validation_rmse(
    validation: Sequence[DailyPower],
    all_usable: Sequence[DailyPower],
    means: Mapping[str, np.ndarray],
) -> Tuple[float, float, int]:
    observed_parts = []
    slot_parts = []
    pers_parts = []
    used_days = 0
    for target in sorted(validation, key=lambda x: x.local_date):
        try:
            _, pers = persistence_forecast(target, all_usable)
        except InformationProcessingError:
            continue
        slot = forecast_day(target, means)
        observed = np.asarray(target.power_kw, dtype=float)
        observed_parts.append(observed)
        slot_parts.append(slot)
        pers_parts.append(pers)
        used_days += 1
    if used_days == 0:
        raise InformationProcessingError("no validation day has persistence prehistory")
    observed_all = np.concatenate(observed_parts)
    slot_all = np.concatenate(slot_parts)
    pers_all = np.concatenate(pers_parts)
    return rmse(observed_all, slot_all), rmse(observed_all, pers_all), used_days


def delay_with_na(values: Sequence[float], delay_steps: int) -> np.ndarray:
    if delay_steps not in LATENCY_STEPS:
        raise InformationProcessingError(
            f"delay_steps must be one of {LATENCY_STEPS}"
        )
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or not np.all(np.isfinite(x)):
        raise InformationProcessingError("delay input must be finite one-dimensional")
    if delay_steps == 0:
        return x.copy()
    result = np.full(x.shape, np.nan, dtype=float)
    if delay_steps < len(x):
        result[delay_steps:] = x[:-delay_steps]
    return result


def empirical_residual_sample(
    residuals: Sequence[float], rng: np.random.Generator, size: int
) -> np.ndarray:
    values = np.asarray(residuals, dtype=float)
    if values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values)):
        raise InformationProcessingError("residual population must be finite and nonempty")
    if size < 0:
        raise InformationProcessingError("sample size must be nonnegative")
    return rng.choice(values, size=size, replace=True)
