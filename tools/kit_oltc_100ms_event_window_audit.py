#!/usr/bin/env python3
"""Extract original KIT 100-ms electrical event windows without rescanning full Parquets.

Source: https://doi.org/10.5281/zenodo.22826984
For the two 2026-03-10 candidate voltage events: 15:32:02 and 15:55:02 UTC.

This script is observational: synchronized measured voltage and EV-point power
are NOT evidence of causal feeder propagation, charging state, or thermal effects.
The original three source datasets must have passed their MD5/timestamp QA.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

UTC = timezone.utc
SOURCE_START = datetime(2026, 2, 3, 23, 0, tzinfo=UTC)
ORIGINAL_N = 43_200_000
PER_SECOND = 10
EVENT_TIMES = (
    datetime(2026, 3, 10, 15, 32, 2, tzinfo=UTC),
    datetime(2026, 3, 10, 15, 55, 2, tzinfo=UTC),
)
SOURCES = {
    "grid110": (
        "oltc_fail_110kV_PMU04_TK1_100ms.parquet",
        ["time[UTC]", "u_pos[V]"],
    ),
    "grid20": (
        "oltc_fail_20kV_PMU01_J01_100ms.parquet",
        ["time[UTC]", "u_pos[V]", "fault_phase"],
    ),
    "ev400": (
        "oltc_fail_400V_EV_SH.J.6_100ms.parquet",
        ["time[UTC]", "u_L1[V]", "u_L2[V]", "u_L3[V]",
         "p_L1[W]", "p_L2[W]", "p_L3[W]", "fault_phase"],
    ),
}


def sample_index(when: datetime) -> int:
    if when.tzinfo is None:
        raise ValueError("An offset-aware UTC time is required")
    microseconds = int(round((when - SOURCE_START).total_seconds() * 1_000_000))
    if microseconds % 100_000:
        raise ValueError("Timestamp is not on a 100 ms sample boundary")
    index = microseconds // 100_000
    if not 0 <= index < ORIGINAL_N:
        raise ValueError("Event is outside the original measurement interval")
    return index


def read_row_range(parquet_path: Path, columns: list[str], left: int, right: int):
    """Read only row groups touched by [left,right) using original global row indices."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    if left < 0 or right < left:
        raise ValueError("Invalid index interval")
    pf = pq.ParquetFile(parquet_path)
    if right > pf.metadata.num_rows:
        raise ValueError("Requested source interval exceeds Parquet rows")
    if not set(columns).issubset(pf.schema_arrow.names):
        raise ValueError(f"Expected columns absent in {parquet_path.name}")

    chunks = []
    cursor = 0
    selected_groups = []
    for rg in range(pf.metadata.num_row_groups):
        n = pf.metadata.row_group(rg).num_rows
        if cursor + n <= left:
            cursor += n
            continue
        if cursor >= right:
            break
        block = pf.read_row_group(rg, columns=columns, use_threads=True)
        local_start = max(0, left - cursor)
        local_end = min(n, right - cursor)
        chunks.append(block.slice(local_start, local_end - local_start))
        selected_groups.append(rg)
        cursor += n
    if not chunks and left < right:
        raise ValueError("No matching Parquet row groups")
    out = pa.concat_tables(chunks) if chunks else pa.table({col: [] for col in columns})
    if out.num_rows != right - left:
        raise RuntimeError("Incomplete Parquet row-range extraction")
    return out, selected_groups


def values(table, col: str) -> np.ndarray:
    return np.asarray(table[col].to_numpy(zero_copy_only=False), dtype=np.float64)


def masked_three_phase(table, prefix: str, unit: str, operation: str) -> np.ndarray:
    a, b, c = (values(table, f"{prefix}_L{k}[{unit}]") for k in (1, 2, 3))
    valid = np.isfinite(a) & np.isfinite(b) & np.isfinite(c)
    out = np.full(len(a), np.nan, dtype=np.float64)
    if operation == "sum":
        out[valid] = a[valid] + b[valid] + c[valid]
    elif operation == "mean":
        out[valid] = (a[valid] + b[valid] + c[valid]) / 3
    else:
        raise ValueError("Invalid phase operation")
    return out


def check_source_time(table, left_index: int) -> None:
    actual = table["time[UTC]"].to_pylist()
    for offset, dt in enumerate(actual):
        expected = SOURCE_START + timedelta(microseconds=(left_index + offset) * 100_000)
        if dt != expected:
            raise RuntimeError(
                f"Source 100ms timestamps mismatch at local offset {offset}: {dt} != {expected}"
            )


def describe_peak_change(power: np.ndarray, rel: np.ndarray, side: str):
    change = np.diff(power, prepend=np.nan)
    if side == "pre":
        valid = (rel < 0) & (rel >= -20)
    elif side == "post":
        valid = (rel >= 0) & (rel <= 30)
    else:
        raise ValueError("Unknown side")
    valid &= np.isfinite(change)
    if not valid.any():
        return {"time_relative_s": None, "delta_power_W": None}
    ind = np.flatnonzero(valid)[np.argmax(np.abs(change[valid]))]
    return {"time_relative_s": float(rel[ind]), "delta_power_W": float(change[ind])}


def save_plot(rows: list[dict], output: Path, event: datetime) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    t = np.array([r["relative_s"] for r in rows])
    u110 = np.array([r["u110_V"] for r in rows], dtype=float)
    u20 = np.array([r["u20_V"] for r in rows], dtype=float)
    u400 = np.array([r["u400_mean_phase_V"] for r in rows], dtype=float)
    p = np.array([r["ev_total_p_W"] for r in rows], dtype=float)
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(12, 8), constrained_layout=True)
    for u, label in ((u110, "110 kV positive-sequence"), (u20, "20 kV positive-sequence"),
                     (u400, "400 V phase arithmetic mean")):
        pre = u[(t >= -20) & (t <= -6) & np.isfinite(u)]
        if len(pre) and np.median(pre) > 0:
            axes[0].plot(t, (u / np.median(pre) - 1) * 100, lw=.9, label=label)
    axes[0].set_ylabel("Voltage vs own pre-median (%)")
    axes[0].legend(fontsize=8)
    axes[1].plot(t, p, lw=1)
    axes[1].set_ylabel("EV point real power sum (W)")
    for phase in (1, 2, 3):
        axes[2].plot(t, [r[f"ev_p_L{phase}_W"] for r in rows], label=f"Phase L{phase}", lw=.8)
    axes[2].set_ylabel("Per-phase EV point P (W)")
    axes[2].set_xlabel("Seconds relative to selected 20 kV step (100 ms samples)")
    axes[2].legend(fontsize=8)
    for ax in axes:
        ax.axvline(0, lw=1, color="gray", ls="--")
        ax.grid(alpha=.2)
    fig.suptitle(f"KIT measured electrical event {event.isoformat()} — NOT thermal / causal evidence")
    fig.savefig(output, dpi=180)
    plt.close(fig)


def analyze_event(folder: Path, output: Path, event: datetime, before_s: int, after_s: int) -> dict:
    center = sample_index(event)
    lo = center - before_s * PER_SECOND
    hi = center + after_s * PER_SECOND + 1
    if lo < 0 or hi > ORIGINAL_N:
        raise ValueError("Window outside 50-day source interval")
    tables = {}
    row_groups = {}
    for key, (filename, columns) in SOURCES.items():
        table, groups = read_row_range(folder / filename, columns, lo, hi)
        check_source_time(table, lo)
        tables[key] = table
        row_groups[key] = groups

    relative = np.arange(lo - center, hi - center, dtype=np.int32) / PER_SECOND
    p = masked_three_phase(tables["ev400"], "p", "W", "sum")
    u400 = masked_three_phase(tables["ev400"], "u", "V", "mean")
    u20 = values(tables["grid20"], "u_pos[V]")
    u110 = values(tables["grid110"], "u_pos[V]")
    p_individual = {k: values(tables["ev400"], f"p_L{k}[W]") for k in (1, 2, 3)}
    fault = tables["grid20"]["fault_phase"].to_pylist()

    rows = []
    for j, r in enumerate(relative):
        row = {
            "utc": (SOURCE_START + timedelta(microseconds=(lo + j) * 100_000)).isoformat(),
            "relative_s": float(r),
            "u110_V": float(u110[j]),
            "u20_V": float(u20[j]),
            "u400_mean_phase_V": float(u400[j]),
            "ev_total_p_W": float(p[j]),
            "ev_p_L1_W": float(p_individual[1][j]),
            "ev_p_L2_W": float(p_individual[2][j]),
            "ev_p_L3_W": float(p_individual[3][j]),
            "fault_phase_20kV": fault[j],
        }
        rows.append(row)
    stem = event.strftime("%Y%m%dT%H%M%SZ")
    csv_path = output / f"KIT_100ms_{stem}.csv"
    png_path = output / f"KIT_100ms_{stem}.png"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    save_plot(rows, png_path, event)
    return {
        "event_utc": event.isoformat(),
        "first_sample": rows[0]["utc"],
        "last_sample": rows[-1]["utc"],
        "sample_count": len(rows),
        "selected_original_row_groups": row_groups,
        "finite_u20_samples": int(np.isfinite(u20).sum()),
        "finite_u400_samples": int(np.isfinite(u400).sum()),
        "finite_ev_p_samples": int(np.isfinite(p).sum()),
        "ev_p_at_event_W": float(p[before_s * PER_SECOND]),
        "largest_100ms_ev_power_jump_pre": describe_peak_change(p, relative, "pre"),
        "largest_100ms_ev_power_jump_post": describe_peak_change(p, relative, "post"),
        "csv_filename": csv_path.name,
        "figure_filename": png_path.name,
    }


def self_test() -> None:
    import pyarrow as pa
    import pyarrow.parquet as pq

    assert sample_index(SOURCE_START) == 0
    assert sample_index(SOURCE_START + timedelta(seconds=2.5)) == 25
    assert sample_index(EVENT_TIMES[0]) < sample_index(EVENT_TIMES[1])
    assert abs(float(np.nanmedian(np.array([1.0, np.nan, 2.0]))) - 1.5) < 1e-12
    assert describe_peak_change(np.array([100., 60., 5., 1., 1.]),
                                np.array([-2., -1., 0., 1., 2.]), "pre")["delta_power_W"] == -40.0
    with TemporaryDirectory() as d:
        p = Path(d) / "groups.parquet"
        expected = [SOURCE_START + timedelta(milliseconds=100 * k) for k in range(11)]
        pq.write_table(pa.table({"time[UTC]": pa.array(expected, type=pa.timestamp("us", tz="UTC")),
                                 "u_pos[V]": np.arange(11, dtype=np.float64)}), p, row_group_size=4)
        tbl, groups = read_row_range(p, ["time[UTC]", "u_pos[V]"], 3, 10)
        assert groups == [0, 1, 2]
        assert tbl.num_rows == 7
        check_source_time(tbl, 3)
        assert values(tbl, "u_pos[V]").tolist() == list(np.arange(3, 10, dtype=float))
    print("PASS: 100ms row-group-only extraction synthetic self-tests (NOT measured KIT output)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", type=Path, default=Path.home() / "Downloads/KIT_OLTC_22826984")
    parser.add_argument("--out", type=Path, default=Path.home() / "Downloads/KIT_OLTC_Electrical_Results/100ms_targeted_events")
    parser.add_argument("--before-s", type=int, default=25)
    parser.add_argument("--after-s", type=int, default=30)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.before_s < 20 or args.after_s < 20:
        parser.error("Window must include at least 20 seconds before and after event")
    args.out.mkdir(parents=True, exist_ok=True)
    findings = []
    for event in EVENT_TIMES:
        print(f"Reading original 100ms source window: {event.isoformat()}", flush=True)
        result = analyze_event(args.folder, args.out, event, args.before_s, args.after_s)
        findings.append(result)
        print(f"  {result['sample_count']} verified original 100ms samples per voltage level")
        print(f"  Largest preceding EV point 100ms power jump: {result['largest_100ms_ev_power_jump_pre']}")
        print(f"  Largest same/post-event EV point 100ms power jump: {result['largest_100ms_ev_power_jump_post']}")
        print(f"  CSV: {result['csv_filename']}")
        print(f"  Plot: {result['figure_filename']}")
    summary = {
        "source": "https://doi.org/10.5281/zenodo.22826984",
        "time_granularity_seconds": 0.1,
        "source_description": "original measured KIT 100ms sensor values from indexed row-group extraction",
        "does_not_reread_all_original_source_rows": True,
        "window_before_seconds": args.before_s,
        "window_after_seconds": args.after_s,
        "events": findings,
        "limit": "Observational voltage/power comparison, not a causal voltage-to-EV link, verified EV charging state or thermal field validation",
    }
    name = args.out / "KIT_100ms_event_window_summary.json"
    name.write_text(json.dumps(summary, indent=2, allow_nan=True) + "\n", encoding="utf-8")
    print(f"Summary: {name}")


if __name__ == "__main__":
    main()