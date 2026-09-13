"""Build the prospective Phase-1 ACN v2 development object.

This script may use only the already-exposed 2019 raw ACN object. It freezes the
corrected development parameters before any fresh v2 holdout is acquired.
"""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable, Mapping

import numpy as np

from phase1_exec.acn_processing import (
    ACNProcessingError,
    LOCAL_TZ,
    day_status,
    load_canonical_jsonl,
    parse_aware_timestamp,
    sha256_file,
)
from phase1_exec.acn_processing_v2 import (
    aggregate_day_power_kw_v2,
    calibrate_global_effective_voltage,
    reconstructed_active_energy_kwh,
    session_trace_v2,
)

START_DAY = date(2019, 10, 10)
END_DAY = date(2019, 12, 31)
EXPECTED_RAW_SHA256 = (
    "ac6d9b237d4e6752dd990f42b569f0de90af125455a8ffdff20b53a7f30e35fd"
)


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
    c = parse_aware_timestamp(str(session["connectionTime"])).astimezone(LOCAL_TZ).date()
    d = parse_aware_timestamp(str(session["disconnectTime"])).astimezone(LOCAL_TZ).date()
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

    if sha256_file(args.raw_jsonl) != EXPECTED_RAW_SHA256:
        raise SystemExit("v2 development raw SHA does not match frozen v1 raw identity")

    out = args.out
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty v2 development directory: {out}")
    out.mkdir(parents=True, exist_ok=True)

    raw_sessions = load_canonical_jsonl(args.raw_jsonl)
    traces = []
    rejected_rows = []
    excluded_due_rejection: dict[date, list[str]] = {}

    for i, raw in enumerate(raw_sessions):
        sid = str(raw.get("sessionID", f"ROW_{i}"))
        try:
            traces.append(session_trace_v2(raw))
        except ACNProcessingError as exc:
            try:
                span = session_span_days(raw)
            except ACNProcessingError as boundary_exc:
                raise SystemExit(
                    f"fatal v2 QC: rejected session {sid} cannot be localized: {boundary_exc}"
                ) from boundary_exc
            rejected_rows.append((sid, str(exc)))
            for local_day in span:
                excluded_due_rejection.setdefault(local_day, []).append(sid)

    v_eff, v_eff_n = calibrate_global_effective_voltage(traces)

    accepted_ids = {trace.session_id for trace in traces}
    with (out / "session_qc_v2.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["session_id", "state", "reason"])
        for raw in raw_sessions:
            sid = str(raw.get("sessionID", "UNKNOWN"))
            if sid in accepted_ids:
                writer.writerow([sid, "ACCEPTED", "v2 duplicate-collapse/active-boundary QC pass"])
        for sid, reason in rejected_rows:
            writer.writerow([sid, "REJECTED", reason])

    excluded_rows = [(START_DAY.isoformat(), "LEFT_CENSORED_QUERY_BOUNDARY")]
    development_days = []
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
        development_days.append(local_day)

    if not development_days:
        raise SystemExit("v2 development QC produced no usable days")

    with (out / "excluded_days_v2.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["local_date", "reason"])
        writer.writerows(excluded_rows)

    write_day_list(out / "development_days.txt", development_days)

    with (out / "power_5min_v2.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["timestamp_utc", "timestamp_local", "local_date", "slot", "p_kw"])
        for local_day in development_days:
            stamps, power_kw = aggregate_day_power_kw_v2(local_day, traces, v_eff)
            if len(stamps) != 288 or len(power_kw) != 288:
                raise SystemExit(f"v2 development day {local_day} does not have 288 slots")
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

    energy_rows = []
    for trace in traces:
        rec = reconstructed_active_energy_kwh(trace, v_eff)
        denom = max(trace.kwh_delivered, 1e-12)
        epsilon = abs(rec - trace.kwh_delivered) / denom if trace.kwh_delivered > 0 else 0.0
        local_day = trace.connection.astimezone(LOCAL_TZ).date()
        energy_rows.append(
            (
                trace.session_id,
                trace.station_id,
                local_day.isoformat(),
                trace.kwh_delivered,
                rec,
                epsilon,
            )
        )

    with (out / "development_energy_diagnostic.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "session_id",
                "station_id",
                "local_date",
                "e_data_kwh",
                "e_reconstructed_kwh",
                "epsilon_E",
            ]
        )
        writer.writerows(energy_rows)

    eps = np.asarray([row[-1] for row in energy_rows if row[3] > 0], dtype=float)
    calibration = {
        "processing_rule": "PHASE1_ACN_PROCESSING_AMENDMENT_V2",
        "V_eff_hat_v": v_eff,
        "V_eff_eligible_session_count": v_eff_n,
        "development_only": True,
        "not_independent_validation": True,
        "development_session_median_epsilon_E": float(np.median(eps)),
        "development_session_p95_epsilon_E": float(np.percentile(eps, 95)),
    }
    calibration_path = out / "v2_calibration.json"
    calibration_path.write_text(
        json.dumps(calibration, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    output_names = [
        "session_qc_v2.csv",
        "excluded_days_v2.csv",
        "development_days.txt",
        "power_5min_v2.csv",
        "development_energy_diagnostic.csv",
        "v2_calibration.json",
    ]
    manifest = {
        "raw_jsonl": str(args.raw_jsonl),
        "raw_sha256": sha256_file(args.raw_jsonl),
        "processing_rule": "PHASE1_ACN_PROCESSING_AMENDMENT_V2",
        "source_session_count": len(raw_sessions),
        "accepted_session_count": len(traces),
        "rejected_session_count": len(rejected_rows),
        "development_day_count": len(development_days),
        "V_eff_hat_v": v_eff,
        "V_eff_eligible_session_count": v_eff_n,
        "grid_minutes": 5,
        "slots_per_accepted_day": 288,
        "outputs_sha256": {name: sha256_file(out / name) for name in output_names},
    }
    manifest_path = out / "development_manifest_v2.json"
    manifest_path.write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "V_eff_hat_v": v_eff,
                "accepted_session_count": len(traces),
                "rejected_session_count": len(rejected_rows),
                "development_day_count": len(development_days),
                "development_manifest_sha256": sha256_file(manifest_path),
                "v2_calibration_sha256": sha256_file(calibration_path),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
