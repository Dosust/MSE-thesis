# MacBook ↔ GitHub KIT research: reproducible execution runbook V1

**Date:** 2026-11-05
**Repository:** https://github.com/Dossiya-SE/MSE-thesis (private; default branch `main`)
**Current task:** Execute the measured 110 kV, 20 kV, and 400 V EV charging-point electrical-response analysis of source-verified KIT OLTC 100 ms observations.
**Source code:** [tools/kit_oltc_electrical_response_analysis.py](../../../tools/kit_oltc_electrical_response_analysis.py)
**Scientific protocol:** [KIT_OLTC_ELECTRICAL_RESPONSE_ANALYSIS_PROTOCOL_V1.md](KIT_OLTC_ELECTRICAL_RESPONSE_ANALYSIS_PROTOCOL_V1.md)

## A. Permanent division of responsibilities

- **MacBook:** stores original large KIT Parquet files and executes numerical analysis, produces intermediate one-second files, JSON, CSV and figures. Never edit the three originals.
- **GitHub `main`:** versioned executable Python script, evidence reports, analysis protocol and subsequent verified findings. Do not imply original multi-GB Parquet files live in GitHub.
- **ChatGPT:** reviews actual pasted Terminal logs and small outcome files, distinguishes measured results from assumptions, and documents the verified checkpoint in GitHub.
- **Private repository:** direct unauthenticated curl to raw.githubusercontent.com may return 404/403; download the script from the chat attachment or the GitHub page while logged in, or use an authenticated local Git clone. The supplied profile overview URL is **not** the thesis repository itself.

## B. Already complete; do not repeat

| Work | Status |
|---|---|
| Three KIT Parquet original downloads onto Mac | COMPLETE |
| Original publisher MD5 on all 3 | PASS, from user Terminal |
| All source schemas and 50-day metadata windows | COMPLETE |
| All 129,600,000 recorded 100 ms UTC timestamps | PASS, zero mismatches, from user Terminal |
| Source-level campus power-network context | Documented |
| Exact parent-child feeder map | Unknown but not blocking **system-level descriptive** electrical comparisons |
| Raw KIT electrical event and charging-power numerical results | **NOT RUN YET in evidence currently available** |

See [prior acquisition and QA](KIT_OLTC_22826984_ACQUISITION_AUDIT.md). No extra original download, checksum scan, or timestamp scan is required unless the original bytes change.

## C. One Mac Terminal command per step

**Rule:** paste only the command text inside a code block. Review the command result before moving to the next step. If a step fails, record that output and stop instead of pretending later work completed.

### Step 1: Verify original file presence (no expensive rehash)

```bash
ls -lh "$HOME/Downloads/KIT_OLTC_22826984/"*.parquet
```

**Expected:** exactly the three known original `oltc_fail_110kV_PMU04_TK1_100ms.parquet`, `oltc_fail_20kV_PMU01_J01_100ms.parquet`, and `oltc_fail_400V_EV_SH.J.6_100ms.parquet`. If a fourth relevant Parquet appears, record it; do not automatically include it in this run.

### Step 2: Save the Python program to Downloads

Use the downloadable `kit_oltc_electrical_response_analysis.py` Python file from the relevant ChatGPT message, or open the [GitHub code page](../../../tools/kit_oltc_electrical_response_analysis.py) in the browser **while signed in**, use **Raw → Save As**, and save the file under `~/Downloads/kit_oltc_electrical_response_analysis.py`.

Check that it exists:

```bash
ls -lh "$HOME/Downloads/kit_oltc_electrical_response_analysis.py"
```

**Expected:** one `.py` file (roughly 22 KB). If missing, do not run Step 4. If saved with a `.txt` extension accidentally, correct the filename only after verifying actual Python source.

### Step 3: Check Python dependencies

```bash
python3 -c 'import sys,numpy,pyarrow,matplotlib;print(sys.version);print("numpy",numpy.__version__,"pyarrow",pyarrow.__version__,"matplotlib",matplotlib.__version__)'
```

If `ModuleNotFoundError` is printed, install the missing packages using:

```bash
python3 -m pip install numpy pyarrow matplotlib
```

Then repeat only the failed dependency check. Avoid making system Python modifications beyond normal Python package installation.

### Step 4: Validate local script before processing large data

```bash
python3 -m py_compile "$HOME/Downloads/kit_oltc_electrical_response_analysis.py" &&
python3 "$HOME/Downloads/kit_oltc_electrical_response_analysis.py" --self-test
```

**Expected:** syntax success (no traceback) and the script's printed self-test success. This tests only algorithm logic against small synthetic examples, **not** any KIT measured result.

### Step 5: Run measured electrical analysis (three originals)

```bash
python3 "$HOME/Downloads/kit_oltc_electrical_response_analysis.py" \
  --folder "$HOME/Downloads/KIT_OLTC_22826984" \
  --out "$HOME/Downloads/KIT_OLTC_Electrical_Results" \
  --step-threshold-pct 0.15 \
  --max-events 60
```

The script reads 100 ms original data in batches and creates one-second summaries before analyzing candidate 20 kV voltage steps and the associated measured 110 kV/400 V voltage and EV-point power responses. **0.15% is an exploratory event-screening setting, not a physical threshold.** A long run or memory use depends on the user's Mac; do not infer results from silence. Do not execute two copies concurrently.

### Step 6: Confirm output artifacts

```bash
ls -lh "$HOME/Downloads/KIT_OLTC_Electrical_Results/"
```

When successful, expect derived `grid110_1s.parquet`, `grid20_1s.parquet`, `ev400_1s.parquet`, `event_metrics.csv`, `analysis_summary.json`, a 50-day `01_voltage_power_50days.png` plot, and `02_largest_event_comparison.png` only if any event passed screening.

Print the non-sensitive compact summary:

```bash
python3 -m json.tool "$HOME/Downloads/KIT_OLTC_Electrical_Results/analysis_summary.json"
```

### Step 7: Evidence handoff (do not upload GB-scale originals)

Upload to the same ChatGPT thesis conversation:
1. `analysis_summary.json`;
2. `event_metrics.csv`;
3. `01_voltage_power_50days.png`;
4. `02_largest_event_comparison.png`, if produced.

These are suitable for reviewing measured signal changes and qualifying scientific claims. Leave the three original publisher files and the large one-second Parquet derivatives on the MacBook unless there is a documented and authorized storage need.

### Step 8: Record scientifically qualified results in GitHub

After reviewing original measured outputs and checking source variables, sign conventions, event definitions and limitations, add a dated research finding to `data/field_candidates/2026-11-05/` with exact input identities, execution parameters, summary statistics, event counts, plots if suitable, limitations and source citations. Do not modify the canonical SO1–SO3 or invent thermal states.

## D. Stop and recovery rules

- `No such file`: inspect `~/Downloads` and confirm precise spellings; do not fabricate an alternative data source.
- `ModuleNotFoundError`: use the Step 3 installation command, then rerun the relevant check.
- Python `Traceback`: copy complete terminal error; do not label the run a success.
- Partial results folder: keep and inspect; do not assume all outputs were completed merely because derived Parquets exist.
- Re-running after failure can overwrite derived products in the results folder. Preserve outputs that were already reviewed and versioned if traceability requires it.
- The private GitHub URL may require sign-in; *GitHub overview contribution calendar* is not a raw source-file or execution log.

## E. Scientific boundary

Measured same-system electrical responses can be analyzed without the exact feeder map, as the user explicitly decided. **Do not infer exact upstream branch causality from synchrony alone.** KIT lacks measured transformer/EVSE temperatures, cooling actuation and recorded thermal derating in the inspected files. Therefore this run is **electrical supporting evidence**, not direct SO1–SO3 thermal field validation.

**Governing thesis authority:** [Current thermal-only scope](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md) and [evidence standard](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md).
