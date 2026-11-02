---
name: thesis-python-data-engineering
description: Evidence-controlled python data engineering for the active extreme-heat Power System–Electrified Transportation thermal-interdependency thesis; follow the orchestrator and repository canonical governance.
---

# Python data engineering

**Prerequisite:** Load `.github/skills/power-ev-thermal-research/SKILL.md` and its current authority/gates before using this module.

## Trigger and objective
Activate for measured CSV/Parquet/XLSX/CAN data processing, timestamps, units, interpolation flags, battery sessions, EV energy-meters and thermal sensors.

## Steps
1. Copy originals to read-only storage; hash each raw file; record source version, Excel sheet name/CSV delimiter and a transformation script revision.
2. Parse acquisition clocks and timezone reliably into UTC while preserving original timestamp and timezone string. Report clock offset, drift, sampling gaps, DST ambiguity, duplicates, measurement latency and synchronization tolerance.
3. Attach mandatory `site_id`, `asset_id`, sensor location, measurement boundary, `unit`, `origin_kind` (`DIRECT_MEASURED`, `OBSERVED_AGGREGATE`, `IMPUTED`, `MODEL_CALCULATED`, `SYNTHETIC`), QC flags and original hash. Preserve raw source columns.
4. Check units/dimensions and physical ranges. Verify EV current charging sign, SOC range, `T_min <= T_max`, transformer oil vs hot spot channels and whether charger input power is per-connector, AC station-total or feeder-level.
5. If cumulative energy meters are verified, calculate interval-average power only for consecutive, valid intervals and account for timestamp gaps, resets, negative deltas, interpolation flags and DST. Distinguish kW and kWh. Save explicit derived-variable provenance; **do not** infer energy loss from unmatched accounting boundaries.
6. Synchronize streams only when an evidenced physical connection and clock policy permit joint analysis. Otherwise export separate partitioned components, never a fake coupled time series.

## Outputs and gate
`observations.csv`, `data_dictionary.csv`, `transform_ledger.csv`, `qa_report.json`. PASS for processing integrity only if rerun matches checksum/content and all transformations are documented. Original counts, complete-case counts and post-QC counts remain separate.

### ECE6378 / RPG Lab overlay (S3)
Practice L5–8: provenance of grid meters, input time resolution, missingness and interpolation, train-only scaler/PCA, physical units/signs and clock alignment. On OPSD keep `DE_KN_industrial3` and `DE_KN_residential4` distinct; cumulative kWh delta is a derived interval-average kW under verified meter conventions, not an input power measured directly. Save channel-level interpolation and transformation flags, feature extraction code, and `feature_provenance.csv`. Never run PCA on the whole dataset before chronological/asset splits.
