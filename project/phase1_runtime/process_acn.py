"""Deterministically process the frozen ACN raw JSONL into Phase-1 artifacts."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable, Mapping

import numpy as np
from acnportal.acnsim.network.sites.caltech_acn import caltech_acn

from phase1_exec.acn_processing import (
    ACNProcessingError,
    LOCAL_TZ,
    aggregate_day_power_kw,
    chronological_split,
    day_status,
    load_canonical_jsonl,
    parse_aware_timestamp,
    reconstructed_session_energy_kwh,
    session_trace,
    sha256_file,
)

START_DAY = date(2019, 10, 10)
END_DAY = date(2019, 12, 31)


def daterange(start: date, end: date) -> Iterable[date]:
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def session_span_days(session: Mapping[str, object]) -> set[date]:
    if "connectionTime" not in session or "disconnectTime" not in session:
        raise ACNProcessingError(
            "cannot localize rejected session without connection/disconnect timestamps"
        )
    c = (
        parse_aware_timestamp(str(session["connectionTime"]))
        .astimezone(LOCAL_TZ)
        .date()
    )
    d = (
        parse_aware_timestamp(str(session["disconnectTime"]))
        .astimezone(LOCAL_TZ)
        .date()
    )
    if d < c:
        raise ACNProcessingError("disconnect local date precedes connection local date")
    return set(daterange(c, d))


def write_day_list(path: Path, days: Iterable[date]) -> None:
    path.write_text(
        "".join(f"{d.isoformat()}\n" for d in days), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-jsonl", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    out = args.out
    if out.exists() and any(out.iterdir()):
        raise SystemExit(
            f"refusing to overwrite non-empty processed directory: {out}"
        )
    out.mkdir(parents=True, exist_ok=True)

    raw_sessions = load_canonical_jsonl(args.raw_jsonl)
    voltage_map = caltech_acn().voltages

    traces = []
    rejected_rows = []
    excluded_due_rejection: dict[date, list[str]] = {}
    for i, raw in enumerate(raw_sessions):
        sid = str(raw.get("sessionID", f"ROW_{i}"))
        try:
            traces.append(session_trace(raw, voltage_map))
        except ACNProcessingError as exc:
            try:
                span = session_span_days(raw)
            except ACNProcessingError as boundary_exc:
                raise SystemExit(
                    f"fatal QC: rejected session {sid} cannot be localized: "
                    f"{boundary_exc}"
                ) from boundary_exc
            rejected_rows.append((sid, str(exc)))
            for local_day in span:
                excluded_due_rejection.setdefault(local_day, []).append(sid)

    accepted_ids = {trace.session_id for trace in traces}
    with (out / "session_qc.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["session_id", "state", "reason"])
        for raw in raw_sessions:
            sid = str(raw.get("sessionID", "UNKNOWN"))
            if sid in accepted_ids:
                writer.writerow([sid, "ACCEPTED", "schema/time-series QC pass"])
        for sid, reason in rejected_rows:
            writer.writerow([sid, "REJECTED", reason])

    excluded_rows = [
        (START_DAY.isoformat(), "LEFT_CENSORED_QUERY_BOUNDARY")
    ]
    usable_days = []
    for local_day in daterange(START_DAY + timedelta(days=1), END_DAY):
        status = day_status(local_day)
        if not status.accepted:
            excluded_rows.append((local_day.isoformat(), status.reason))
            continue
        if local_day in excluded_due_rejection:
            excluded_rows.append(
                (
                    local_day.isoformat(),
                    "REJECTED_ACTIVE_SESSION:"
                    + ",".join(sorted(excluded_due_rejection[local_day])),
                )
            )
            continue
        usable_days.append(local_day)

    with (out / "excluded_days.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["local_date", "reason"])
        writer.writerows(excluded_rows)

    cal_days, val_days = chronological_split(usable_days)
    if not cal_days or not val_days:
        raise SystemExit(
            "chronological split produced empty calibration or validation subset"
        )
    cal_set = set(cal_days)
    write_day_list(out / "usable_days.txt", usable_days)
    write_day_list(out / "calibration_days.txt", cal_days)
    write_day_list(out / "validation_days.txt", val_days)

    with (out / "power_5min.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["timestamp_utc", "timestamp_local", "local_date", "slot", "p_kw"]
        )
        for local_day in usable_days:
            stamps, power_kw = aggregate_day_power_kw(local_day, traces)
            if len(stamps) != 288 or len(power_kw) != 288:
                raise SystemExit(
                    f"V-D05 failure on {local_day}: expected 288 slots"
                )
            for slot, (stamp, value) in enumerate(zip(stamps, power_kw)):
                writer.writerow(
                    [
                        stamp.isoformat(),
                        stamp.astimezone(LOCAL_TZ).isoformat(),
                        local_day.isoformat(),
                        slot,
                        format(float(value), ".17g"),
                    ]
                )

    # V-D06 consistency check. Group full-session reconstruction by local
    # connection date. Do not rescale reconstructed energy to kWhDelivered.
    energy_by_day: dict[date, list[float]] = {}
    for trace in traces:
        local_day = trace.connection.astimezone(LOCAL_TZ).date()
        rec = reconstructed_session_energy_kwh(trace)
        bucket = energy_by_day.setdefault(local_day, [0.0, 0.0, 0.0])
        bucket[0] += rec
        bucket[1] += trace.kwh_delivered
        bucket[2] += 1.0

    energy_rows = []
    for local_day in usable_days:
        rec, observed, count = energy_by_day.get(
            local_day, [0.0, 0.0, 0.0]
        )
        denom = max(observed, 1e-12)
        epsilon = abs(rec - observed) / denom if count > 0 else 0.0
        split = "calibration" if local_day in cal_set else "validation"
        energy_rows.append(
            (
                local_day.isoformat(),
                split,
                int(count),
                rec,
                observed,
                epsilon,
            )
        )

    with (out / "energy_reconstruction.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "local_date",
                "split",
                "sessions",
                "e_reconstructed_kwh",
                "e_data_kwh",
                "epsilon_E",
            ]
        )
        writer.writerows(energy_rows)

    val_eps = [
        row[-1]
        for row in energy_rows
        if row[1] == "validation" and row[2] > 0
    ]
    if val_eps:
        median_eps = float(np.median(val_eps))
        p95_eps = float(np.percentile(val_eps, 95))
        max_eps = float(max(val_eps))
        vd06_state = "PASS" if median_eps <= 0.01 else "FAIL"
    else:
        median_eps = None
        p95_eps = None
        max_eps = None
        vd06_state = "NOT_EVALUABLE"

    energy_summary = {
        "validation_days_with_sessions": len(val_eps),
        "median_epsilon_E": median_eps,
        "p95_epsilon_E": p95_eps,
        "max_epsilon_E": max_eps,
        "V_D06_threshold": 0.01,
        "V_D06_state": vd06_state,
    }

    output_names = [
        "session_qc.csv",
        "excluded_days.csv",
        "usable_days.txt",
        "calibration_days.txt",
        "validation_days.txt",
        "power_5min.csv",
        "energy_reconstruction.csv",
    ]
    hashes = {name: sha256_file(out / name) for name in output_names}
    manifest = {
        "raw_jsonl": str(args.raw_jsonl),
        "raw_sha256": sha256_file(args.raw_jsonl),
        "processing_rule": "PHASE1_ACN_PROCESSING_PROTOCOL_V1",
        "source_session_count": len(raw_sessions),
        "accepted_session_count": len(traces),
        "rejected_session_count": len(rejected_rows),
        "usable_day_count": len(usable_days),
        "calibration_day_count": len(cal_days),
        "validation_day_count": len(val_days),
        "grid_minutes": 5,
        "slots_per_accepted_day": 288,
        "energy_reconstruction": energy_summary,
        "outputs_sha256": hashes,
    }
    manifest_path = out / "processing_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                **energy_summary,
                "processing_manifest_sha256": sha256_file(manifest_path),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
