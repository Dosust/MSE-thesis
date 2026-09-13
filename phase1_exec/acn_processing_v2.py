"""Prospective Phase-1 ACN v2 processing operators.

This module implements only the corrective mechanisms preregistered in
PHASE1_ACN_PROCESSING_AMENDMENT_V2.md. It does not inspect the fresh v2
holdout and does not execute H1/H2.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from typing import Mapping, Sequence, Tuple

import numpy as np

from .acn_processing import (
    ACNProcessingError,
    GRID_MINUTES,
    GRID_SECONDS,
    LOCAL_TZ,
    MAX_TRACE_GAP_SECONDS,
    SLOTS_PER_24H_DAY,
    TimeSeries,
    day_status,
    local_day_bounds,
    parse_aware_timestamp,
)


@dataclass(frozen=True)
class V2SessionTrace:
    session_id: str
    station_id: str
    connection: datetime
    disconnect: datetime
    active_end: datetime
    kwh_delivered: float
    current: TimeSeries
    pilot: TimeSeries


def _finite_nonnegative(value: object, name: str) -> float:
    try:
        out = float(value)
    except (TypeError, ValueError) as exc:
        raise ACNProcessingError(f"{name} must be numeric") from exc
    if not math.isfinite(out) or out < 0.0:
        raise ACNProcessingError(f"{name} must be finite and nonnegative")
    return out


def extract_timeseries_v2(
    obj: object, value_key: str, field_name: str
) -> TimeSeries:
    """Collapse equal timestamps by arithmetic mean; reject true reversal."""
    if not isinstance(obj, Mapping):
        raise ACNProcessingError(f"{field_name} must be an object")
    if "timestamps" not in obj or value_key not in obj:
        raise ACNProcessingError(
            f"{field_name} must contain 'timestamps' and {value_key!r}"
        )
    raw_ts = obj["timestamps"]
    raw_values = obj[value_key]
    if not isinstance(raw_ts, Sequence) or isinstance(raw_ts, (str, bytes)):
        raise ACNProcessingError(f"{field_name}.timestamps must be a sequence")
    if not isinstance(raw_values, Sequence) or isinstance(
        raw_values, (str, bytes)
    ):
        raise ACNProcessingError(f"{field_name}.{value_key} must be a sequence")
    if len(raw_ts) != len(raw_values):
        raise ACNProcessingError(f"{field_name} timestamp/value lengths differ")
    if len(raw_ts) < 2:
        raise ACNProcessingError(f"{field_name} needs at least two samples")

    timestamps = [parse_aware_timestamp(str(x)) for x in raw_ts]
    values = [
        _finite_nonnegative(x, f"{field_name}.{value_key}")
        for x in raw_values
    ]

    collapsed_t = []
    collapsed_v = []
    i = 0
    while i < len(timestamps):
        if i > 0 and timestamps[i] < timestamps[i - 1]:
            raise ACNProcessingError(
                f"{field_name} contains genuine backward time"
            )
        t = timestamps[i]
        group = [values[i]]
        j = i + 1
        while j < len(timestamps) and timestamps[j] == t:
            group.append(values[j])
            j += 1
        if j < len(timestamps) and timestamps[j] < t:
            raise ACNProcessingError(
                f"{field_name} contains genuine backward time"
            )
        collapsed_t.append(t)
        collapsed_v.append(float(np.mean(group)))
        i = j

    if len(collapsed_t) < 2:
        raise ACNProcessingError(
            f"{field_name} needs at least two unique timestamps"
        )

    for left, right in zip(collapsed_t, collapsed_t[1:]):
        dt = (right - left).total_seconds()
        if dt <= 0:
            raise ACNProcessingError(
                f"{field_name} timestamps must increase after duplicate collapse"
            )
        if dt > MAX_TRACE_GAP_SECONDS:
            raise ACNProcessingError(
                f"{field_name} contains gap {dt:.0f}s > {MAX_TRACE_GAP_SECONDS}s"
            )

    return TimeSeries(
        timestamps=tuple(collapsed_t), values=tuple(collapsed_v)
    )


def session_trace_v2(session: Mapping[str, object]) -> V2SessionTrace:
    required = (
        "sessionID",
        "spaceID",
        "connectionTime",
        "disconnectTime",
        "doneChargingTime",
        "kWhDelivered",
        "chargingCurrent",
        "pilotSignal",
    )
    missing = [key for key in required if key not in session]
    if missing:
        raise ACNProcessingError(f"missing required v2 session fields: {missing}")

    connection = parse_aware_timestamp(str(session["connectionTime"]))
    disconnect = parse_aware_timestamp(str(session["disconnectTime"]))
    done = parse_aware_timestamp(str(session["doneChargingTime"]))
    if not connection < disconnect:
        raise ACNProcessingError("connectionTime must precede disconnectTime")
    if done < connection:
        raise ACNProcessingError("doneChargingTime precedes connectionTime")
    active_end = min(done, disconnect)
    if active_end <= connection:
        raise ACNProcessingError("active charging interval is empty")

    if "timezone" in session and str(session["timezone"]) != "America/Los_Angeles":
        raise ACNProcessingError("unexpected ACN timezone for Caltech session")

    return V2SessionTrace(
        session_id=str(session["sessionID"]),
        station_id=str(session["spaceID"]),
        connection=connection,
        disconnect=disconnect,
        active_end=active_end,
        kwh_delivered=_finite_nonnegative(
            session["kWhDelivered"], "kWhDelivered"
        ),
        current=extract_timeseries_v2(
            session["chargingCurrent"], "current", "chargingCurrent"
        ),
        pilot=extract_timeseries_v2(
            session["pilotSignal"], "pilot", "pilotSignal"
        ),
    )


def _integral_linear(
    ts: TimeSeries, start: datetime, end: datetime
) -> float:
    if end <= start:
        return 0.0
    x = np.array([dt.timestamp() for dt in ts.timestamps], dtype=float)
    y = np.array(ts.values, dtype=float)
    lo = max(start.timestamp(), x[0])
    hi = min(end.timestamp(), x[-1])
    if hi <= lo:
        return 0.0
    interior = x[(x > lo) & (x < hi)]
    grid = np.concatenate(([lo], interior, [hi]))
    vals = np.interp(grid, x, y)
    return float(np.trapz(vals, grid))


def active_amp_seconds(trace: V2SessionTrace) -> float:
    return _integral_linear(
        trace.current, trace.connection, trace.active_end
    )


def implied_effective_voltage(trace: V2SessionTrace) -> float | None:
    amp_seconds = active_amp_seconds(trace)
    if trace.kwh_delivered == 0.0 and amp_seconds == 0.0:
        return None
    if trace.kwh_delivered > 0.0 and amp_seconds <= 0.0:
        raise ACNProcessingError(
            "positive delivered energy with zero reconstructed active current"
        )
    if trace.kwh_delivered == 0.0:
        return None
    return (
        1000.0 * 3600.0 * trace.kwh_delivered / amp_seconds
    )


def calibrate_global_effective_voltage(
    traces: Sequence[V2SessionTrace],
) -> Tuple[float, int]:
    values = []
    for trace in traces:
        value = implied_effective_voltage(trace)
        if value is not None:
            if not math.isfinite(value) or value <= 0.0:
                raise ACNProcessingError("invalid implied effective voltage")
            values.append(value)
    if not values:
        raise ACNProcessingError("no eligible session for effective-voltage calibration")
    return float(np.median(np.asarray(values, dtype=float))), len(values)


def reconstructed_active_energy_kwh(
    trace: V2SessionTrace, effective_voltage_v: float
) -> float:
    if not math.isfinite(effective_voltage_v) or effective_voltage_v <= 0.0:
        raise ACNProcessingError("effective voltage must be finite and positive")
    return (
        effective_voltage_v
        * active_amp_seconds(trace)
        / (1000.0 * 3600.0)
    )


def aggregate_day_power_kw_v2(
    day: date,
    traces: Sequence[V2SessionTrace],
    effective_voltage_v: float,
):
    """Return exactly 288 active-charging 5-min power values for a 24h day."""
    status = day_status(day)
    if not status.accepted:
        raise ACNProcessingError(status.reason)
    if not math.isfinite(effective_voltage_v) or effective_voltage_v <= 0.0:
        raise ACNProcessingError("effective voltage must be finite and positive")
    start_utc, end_utc = local_day_bounds(day)
    edges = [
        start_utc + timedelta(seconds=i * GRID_SECONDS)
        for i in range(SLOTS_PER_24H_DAY + 1)
    ]
    energy_kwh = np.zeros(SLOTS_PER_24H_DAY, dtype=float)
    for trace in traces:
        if trace.active_end <= start_utc or trace.connection >= end_utc:
            continue
        for k in range(SLOTS_PER_24H_DAY):
            amp_seconds = _integral_linear(
                trace.current, edges[k], min(edges[k + 1], trace.active_end)
            )
            if amp_seconds:
                energy_kwh[k] += (
                    effective_voltage_v
                    * amp_seconds
                    / (1000.0 * 3600.0)
                )
    power_kw = energy_kwh / (GRID_MINUTES / 60.0)
    return edges[:-1], power_kw
