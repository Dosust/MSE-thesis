#!/usr/bin/env python3
"""Read-only every-row timestamp-grid QA for KIT OLTC Zenodo 22826984.

Local Mac input (user originals):
  ~/Downloads/KIT_OLTC_22826984/*.parquet

Scientific limitations:
  This checks the exact expected 100 ms UTC grid in all three files,
  not sensor calibration, true wall-clock accuracy, electrical topology,
  temperature observability, physical causality or resilience validation.
  It NEVER edits the original Parquet files.

Dependencies: Python 3.10+, numpy, pyarrow.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

FILES = [
    "oltc_fail_110kV_PMU04_TK1_100ms.parquet",
    "oltc_fail_20kV_PMU01_J01_100ms.parquet",
    "oltc_fail_400V_EV_SH.J.6_100ms.parquet",
]
EXPECTED_ROWS = 43_200_000
EPOCH_START = datetime(2026, 2, 3, 23, 0, 0, tzinfo=timezone.utc)
STEP_US = 100_000


def scan_file(path: Path, batch_size: int) -> dict:
    """Check each file row against the same unbroken nominal UTC grid."""
    import numpy as np
    import pyarrow as pa
    import pyarrow.compute as pc
    import pyarrow.parquet as pq

    result = {
        "file": path.name,
        "exists": path.is_file(),
        "expected_rows": EXPECTED_ROWS,
        "checked_rows": 0,
        "null_timestamps": 0,
        "grid_mismatches_including_nulls": 0,
        "first_mismatches": [],
        "status": "FAIL",
    }
    if not path.is_file():
        result["error"] = "Original Parquet file missing"
        return result

    pf = pq.ParquetFile(path)
    result["metadata_rows"] = pf.metadata.num_rows
    result["row_groups"] = pf.num_row_groups
    field = pf.schema_arrow.field("time[UTC]")
    if not pa.types.is_timestamp(field.type):
        result["error"] = "time[UTC] is not a timestamp field"
        return result
    if field.type.unit != "us" or field.type.tz != "UTC":
        result["error"] = f"Unexpected timestamp unit/tz: {field.type}"
        return result

    start_us = int(EPOCH_START.timestamp()) * 1_000_000
    row_offset = 0
    for batch in pf.iter_batches(
        batch_size=batch_size,
        columns=["time[UTC]"],
        use_threads=True,
    ):
        arr = batch.column(0)
        n = len(arr)
        result["null_timestamps"] += int(arr.null_count)

        # Timestamp[us, UTC] -> epoch microseconds; replace nulls
        # with a non-grid value, counted once in grid mismatches.
        integer_values = pc.cast(arr, pa.int64(), safe=False)
        integer_values = pc.fill_null(integer_values, -1)
        actual = integer_values.to_numpy(zero_copy_only=False)
        expected = start_us + STEP_US * np.arange(
            row_offset, row_offset + n, dtype=np.int64
        )
        wrong = actual != expected
        result["grid_mismatches_including_nulls"] += int(np.count_nonzero(wrong))

        remaining = 5 - len(result["first_mismatches"])
        if remaining > 0 and np.any(wrong):
            for idx in np.flatnonzero(wrong)[:remaining]:
                result["first_mismatches"].append(
                    {
                        "row_zero_based": int(row_offset + idx),
                        "expected_epoch_us": int(expected[idx]),
                        "actual_epoch_us": (
                            None if actual[idx] == -1 else int(actual[idx])
                        ),
                    }
                )
        row_offset += n
        result["checked_rows"] = row_offset

    result["status"] = (
        "PASS"
        if row_offset == EXPECTED_ROWS
        and pf.metadata.num_rows == EXPECTED_ROWS
        and result["null_timestamps"] == 0
        and result["grid_mismatches_including_nulls"] == 0
        else "FAIL"
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--folder",
        type=Path,
        default=Path.home() / "Downloads/KIT_OLTC_22826984",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.home()
        / "Downloads/KIT_OLTC_22826984/KIT_ROW_TIME_AUDIT.json",
    )
    parser.add_argument("--batch-size", type=int, default=250_000)
    args = parser.parse_args()
    if args.batch_size <= 0:
        parser.error("--batch-size must be > 0")

    report = {
        "dataset": "KIT OLTC 22826984, 110/20/0.4 kV",
        "source_url": "https://zenodo.org/records/22826984",
        "checked_utc_grid_start": EPOCH_START.isoformat(),
        "grid_step_microseconds": STEP_US,
        "checks": "Every row equals expected UTC 100 ms index; no nulls",
        "not_checked": [
            "independent time standard and sensor clock drift",
            "physical transformer-feeder-EVSE connectivity",
            "variable semantics, units beyond column labels, missing non-time data",
            "thermal fields, power derating, causality, SO1-SO3 validation",
        ],
        "files": [],
    }

    for filename in FILES:
        path = args.folder / filename
        print(f"\nInspecting: {path}", flush=True)
        try:
            result = scan_file(path, args.batch_size)
        except Exception as exc:
            result = {"file": filename, "status": "FAIL", "error": repr(exc)}
        report["files"].append(result)
        print(
            f"  {result['status']} | checked={result.get('checked_rows', 0)}"
            f" | mismatches={result.get('grid_mismatches_including_nulls', '?')}"
            f" | nulls={result.get('null_timestamps', '?')}",
            flush=True,
        )

    report["all_files_pass"] = (
        len(report["files"]) == 3
        and all(record["status"] == "PASS" for record in report["files"])
    )
    report["interpretation"] = (
        "All source files follow the exact same expected UTC time grid"
        if report["all_files_pass"]
        else "At least one source file failed strict row-level time QA"
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"\nReport: {args.output}")
    print(f"OVERALL: {'PASS' if report['all_files_pass'] else 'FAIL'}")
    return 0 if report["all_files_pass"] else 2


if __name__ == "__main__":
    sys.exit(main())
