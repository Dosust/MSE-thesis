"""Deterministic ACN raw-to-5-minute processing for Phase-1 verification.

This module performs data QC and deterministic transformation only. It does not
fit models, inspect validation outcomes, or execute H1/H2.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Iterable, List, Mapping, Sequence, Tuple
from zoneinfo import ZoneInfo

import numpy as np

LOCAL_TZ = ZoneInfo("America/Los_Angeles")
GRID_MINUTES = 5
GRID_SECONDS = GRID_MINUTES * 60
SLOTS_PER_24H_DAY = 24 * 60 // GRID_MINUTES
MAX_TRACE_GAP_SECONDS = 5 * 60


class ACNProcessingError(ValueError):
    """Raised when a raw ACN object violates the frozen processing contract."""


@dataclass(frozen=True)
class TimeSeries:
    timestamps: Tuple[datetime, ...]
    values: Tuple[float, ...]


@dataclass(frozen=True)
class SessionTrace:
    session_id: str
    station_id: str
    connection: datetime
    disconnect: datetime
    kwh_delivered: float
    current: TimeSeries
    pilot: TimeSeries
    voltage_v: float


@dataclass(frozen=True)
class DayStatus:
    local_date: date
    accepted: bool
    reason: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def parse_aware_timestamp(value: str) -> datetime:
    """Parse RFC1123 or ISO-8601 timestamp and normalize it to UTC."""
    if not isinstance(value, str) or not value.strip():
        raise ACNProcessingError("timestamp must be a non-empty string")
    try:
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ACNProcessingError(f"unparseable timestamp: {value!r}") from exc
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ACNProcessingError(f"naive timestamp is forbidden: {value!r}")
    return dt.astimezone(timezone.utc)


def _finite_nonnegative(value: object, name: str) -> float:
    try:
        out = float(value)
    except (TypeError, ValueError) as exc:
        raise ACNProcessingError(f"{name} must be numeric") from exc
    if not math.isfinite(out) or out < 0.0:
        raise ACNProcessingError(f"{name} must be finite and nonnegative")
    return out


def extract_timeseries(obj: object, value_key: str, field_name: str) -> TimeSeries:
    """Extract the documented ACN {timestamps, current/pilot} time-series form."""
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
    if not isinstance(raw_values, Sequence) or isinstance(raw_values, (str, bytes)):
        raise ACNProcessingError(f"{field_name}.{value_key} must be a sequence")
    if len(raw_ts) != len(raw_values):
        raise ACNProcessingError(f"{field_name} timestamp/value lengths differ")
    if len(raw_ts) < 2:
        raise ACNProcessingError(f"{field_name} needs at least two samples")

    timestamps = tuple(parse_aware_timestamp(str(x)) for x in raw_ts)
    values = tuple(
        _finite_nonnegative(x, f"{field_name}.{value_key}") for x in raw_values
    )
    for left, right in zip(timestamps, timestamps[1:]):
        dt = (right - left).total_seconds()
        if dt <= 0:
            raise ACNProcessingError(
                f"{field_name} timestamps must be strictly increasing"
            )
        if dt > MAX_TRACE_GAP_SECONDS:
            raise ACNProcessingError(
                f"{field_name} contains gap {dt:.0f}s > {MAX_TRACE_GAP_SECONDS}s"
            )
    return TimeSeries(timestamps=timestamps, values=values)


def session_trace(
    session: Mapping[str, object], voltage_map: Mapping[str, float]
) -> SessionTrace:
    required = (
        "sessionID",
        "spaceID",
        "connectionTime",
        "disconnectTime",
        "kWhDelivered",
        "chargingCurrent",
        "pilotSignal",
    )
    missing = [key for key in required if key not in session]
    if missing:
        raise ACNProcessingError(f"missing required session fields: {missing}")

    session_id = str(session["sessionID"])
    station_id = str(session["spaceID"])
    if station_id not in voltage_map:
        raise ACNProcessingError(
            f"station {station_id!r} is absent from frozen Caltech ACN"
        )
    voltage_v = _finite_nonnegative(voltage_map[station_id], "station voltage")
    if voltage_v <= 0.0:
        raise ACNProcessingError("station voltage must be positive")

    connection = parse_aware_timestamp(str(session["connectionTime"]))
    disconnect = parse_aware_timestamp(str(session["disconnectTime"]))
    if not connection < disconnect:
        raise ACNProcessingError("connectionTime must precede disconnectTime")

    if "timezone" in session and str(session["timezone"]) != "America/Los_Angeles":
        raise ACNProcessingError("unexpected ACN timezone for Caltech session")

    return SessionTrace(
        session_id=session_id,
        station_id=station_id,
        connection=connection,
        disconnect=disconnect,
        kwh_delivered=_finite_nonnegative(
            session["kWhDelivered"], "kWhDelivered"
        ),
        current=extract_timeseries(
            session["chargingCurrent"], "current", "chargingCurrent"
        ),
        pilot=extract_timeseries(session["pilotSignal"], "pilot", "pilotSignal"),
        voltage_v=voltage_v,
    )


def _integral_linear(ts: TimeSeries, start: datetime, end: datetime) -> float:
    """Integrate a piecewise-linear signal over [start,end] in value-seconds."""
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


def reconstructed_session_energy_kwh(trace: SessionTrace) -> float:
    amp_seconds = _integral_linear(trace.current, trace.connection, trace.disconnect)
    return trace.voltage_v * amp_seconds / (1000.0 * 3600.0)


def local_day_bounds(day: date) -> Tuple[datetime, datetime]:
    start_local = datetime.combine(day, time.min, LOCAL_TZ)
    next_local = datetime.combine(day + timedelta(days=1), time.min, LOCAL_TZ)
    return start_local.astimezone(timezone.utc), next_local.astimezone(timezone.utc)


def day_status(day: date) -> DayStatus:
    start_utc, end_utc = local_day_bounds(day)
    duration = int((end_utc - start_utc).total_seconds())
    if duration != 24 * 3600:
        return DayStatus(day, False, f"DST_NON_24H_DAY:{duration // 3600}h")
    return DayStatus(day, True, "ACCEPTED_24H_DAY")


def aggregate_day_power_kw(
    day: date, traces: Sequence[SessionTrace]
) -> Tuple[List[datetime], np.ndarray]:
    """Return exactly 288 local-day five-minute average site-power values."""
    status = day_status(day)
    if not status.accepted:
        raise ACNProcessingError(status.reason)
    start_utc, end_utc = local_day_bounds(day)
    edges = [
        start_utc + timedelta(seconds=i * GRID_SECONDS)
        for i in range(SLOTS_PER_24H_DAY + 1)
    ]
    energy_kwh = np.zeros(SLOTS_PER_24H_DAY, dtype=float)
    for trace in traces:
        if trace.disconnect <= start_utc or trace.connection >= end_utc:
            continue
        for k in range(SLOTS_PER_24H_DAY):
            amp_seconds = _integral_linear(trace.current, edges[k], edges[k + 1])
            if amp_seconds:
                energy_kwh[k] += (
                    trace.voltage_v * amp_seconds / (1000.0 * 3600.0)
                )
    power_kw = energy_kwh / (GRID_MINUTES / 60.0)
    return edges[:-1], power_kw


def chronological_split(
    days: Sequence[date],
) -> Tuple[Tuple[date, ...], Tuple[date, ...]]:
    ordered = tuple(sorted(set(days)))
    n_cal = math.floor(0.70 * len(ordered))
    return ordered[:n_cal], ordered[n_cal:]


def load_canonical_jsonl(path: Path) -> List[Mapping[str, object]]:
    sessions: List[Mapping[str, object]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ACNProcessingError(
                    f"invalid JSONL at line {line_number}"
                ) from exc
            if not isinstance(obj, Mapping):
                raise ACNProcessingError(
                    f"line {line_number} is not a session object"
                )
            sessions.append(obj)
    if not sessions:
        raise ACNProcessingError("canonical ACN export is empty")
    return sessions


def connection_days(traces: Iterable[SessionTrace]) -> Tuple[date, ...]:
    return tuple(
        sorted({t.connection.astimezone(LOCAL_TZ).date() for t in traces})
    )
