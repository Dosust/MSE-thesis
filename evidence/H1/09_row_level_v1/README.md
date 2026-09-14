# EGMIV H1 Row-Level Data Qualification Executor v1.0

This package executes the frozen row-level data-quality gate for H1 before any calibration or confirmatory M0/M1/M2 experiment.

## Scientific status

- Acquisition windows: frozen.
- Candidate split: `E0,E2` training; `E1,E3,E4` held out — **candidate only, not frozen**.
- Audit code: verified offline (`4/4` tests passed).
- Raw event-window metrics: pending actual source retrieval.
- Confirmatory calibration/simulation: prohibited until the R1–R8 data gate passes.

## Install

```bash
python -m pip install -r requirements.txt
```

## Sources handled

- NYISO P-58B monthly Real-Time Actual Load archive.
- EAGLE-I yearly county outage CSV (supplied locally after download).
- NYC TLC High Volume FHV monthly Parquet.
- NYC DOT Traffic Speeds Socrata API.
- NYC 311 Socrata API.

## Example execution

```bash
python row_level_audit_runner.py \
  --event E1 \
  --outdir audit_outputs \
  --eaglei-dir /path/to/eaglei \
  --sources NYISO_P58B EAGLEI TLC_HVFHV NYC_DOT_SPEEDS NYC_311
```

Repeat for `E0` through `E4`.

## Mandatory interpretation rules

1. An absent EAGLE-I row is **not** interpreted as zero outage.
2. TLC completed trips are **not** treated as the complete requested-demand population.
3. Held-out events cannot be moved to training because of model performance.
4. Failed/missing source retrieval is recorded as failure/pending, never converted into PASS.
5. No H1 calibration or confirmatory run is authorized until required event/source roles pass the frozen R1–R8 audit.

## Outputs

For each event, the executor writes an `audit.json` containing row count, timestamp range, temporal-gap metrics, required-field null rates, duplicate rate, rule flags, provenance URL, and hashes for downloaded raw files where available. Event-window extracts are preserved as Parquet.
