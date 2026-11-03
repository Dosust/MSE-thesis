# TUM production-EV UDS field dataset — source, local acquisition, ID1 thermal QA and open gates
**Audit date:** 2026-11-03  
**Registry:** FD-013 (field candidate register); D20 (master inventory)  
**Assessment:** **RELEVANT: REAL VEHICLE-SIDE OPERATIONAL FIELD DATA; LOCAL COPY ACQUIRED; THERMAL CHANNELS QA PENDING.** It is not measured EVSE-internal thermal data and is not a physically connected power–transport field dataset.

## 1. Source and eligibility

- Original repository: https://github.com/TUMFTM/electric-vehicle-uds-dataset
- README: https://github.com/TUMFTM/electric-vehicle-uds-dataset/blob/main/README.MD
- Signal dictionary: https://github.com/TUMFTM/electric-vehicle-uds-dataset/blob/main/data/value_overview.csv
- Original Parquet directory: https://github.com/TUMFTM/electric-vehicle-uds-dataset/tree/main/data/uds_data
- Citation: Schreiber et al. (2026), *Lab-to-field gap in battery aging studies: Mismatch of operating conditions between laboratory environments and real-world automotive applications*, eTransportation 27, 100518. DOI https://doi.org/10.1016/j.etran.2025.100518
- License per repository: CC BY-NC 4.0 (attribution required; noncommercial restriction).
- Source describes actual UDS/OBD-II logging from seven unmodified production EVs in German public-road operation: two VW ID.3 Pro Performance, five CUPRA Born, >72,000 km fleet total. Includes driving, parking and charging observations. The raw per-vehicle logs are stored as Git LFS Parquet; derived session/trip histogram JSONs are NOT the source logs.
- **Evidence classification:** verified source-described real-world EV field data, not laboratory/synthetic. Individual thermal signals and intervals still require independent validity/QA.

## 2. User-local acquisition and readback (reported in terminal, not independently downloaded here)

Environment: Apple Silicon macOS; DuckDB v2.0.0; Git LFS v3.8.1. Git LFS pull completed **7/7** objects, reporting **805.49 MiB** transferred. The user listed these original local files under `~/Downloads/electric-vehicle-uds-dataset/data/uds_data/`:

| File | User-terminal file size |
|---|---:|
| CUP1.parquet | 74M |
| CUP2.parquet | 32M |
| CUP3.parquet | 8.4M |
| CUP4.parquet | 42M |
| CUP5.parquet | 28M |
| ID1.parquet | 323M |
| ID2.parquet | 297M |

**Important:** These bytes exist on the user's Mac; not asserted uploaded to GitHub or Drive. Original SHA-256 hashes have NOT yet been captured in a persistent registry. File size/7 of 7 alone is not full hash verification.

DuckDB read `data/uds_data/ID1.parquet` successfully and counted **40,401,700 long-format rows**. Schema: `vehicle_id VARCHAR`, `time TIMESTAMP_NS`, `value_id BIGINT`, `value DOUBLE`. SQL count of `value IS NULL`: **0** (not proof of valid data). Reported latest ID1 timestamp: **2023-06-13 07:50:10.952**. Earliest timestamp and count of distinct `value_id` were truncated from the console and remain **unknown**. Source clock timezone has NOT been verified. `ID1.csv` export completed without reported error; its row-count and fidelity to the original Parquet still require checking. **Do not conflate CSV export with new independent empirical data.**

## 3. Documented signal dictionary (source metadata)

| ID | Source variable | Unit | Source listed valid min/max | Nominal source sampling |
|---|---|---|---|---|
| 15 | `ambient_air_temp` | °C | -40 to 215 | 10,000 ms |
| 1208 | `hv_temp_min` | °C | -40 to 100 | 10,000 ms |
| 1209 | `hv_temp_max` | °C | -40 to 100 | 10,000 ms |
| 1272 | `hv_battery_temp_inlet` (battery-pack inlet) | °C | **-40 to 200** | 5,000 ms |
| 1273 | `hv_battery_temp_outlet` (battery-pack outlet) | °C | **-40 to 200** | 5,000 ms |
| 1200 | `hv_battery_voltage` | V | 0 to 1000 | 200 ms |
| 900 | `hv_soc` | % | 0 to 100 | 5,000 ms |

The source calls IDs 1272/1273 **battery pack inlet/outlet temperatures**, NOT verified internal EVSE charger/rectifier or necessarily dedicated coolant thermometers. Prior discussion used "coolant inlet/outlet" as a working description; confirm whether they specifically measure coolant before applying coolant heat-balance equations. Sampling listed is nominal, not a guarantee of complete synchronized sample records.

## 4. ID1 measured temperature summaries from DuckDB

| ID | N | Minimum °C | Maximum °C | Mean °C | Median °C | p01 °C | p99 °C |
|---|---:|---:|---:|---:|---:|---:|---:|
| 15 ambient | 283,059 | -9.5 | 39.5 | 10.2823 | 8.5 | -5.0 | 30.0 |
| 1208 pack min | 25,450 | 0 | 44.0 | 17.2675 | 19.8 | 0.0 | 33.2 |
| 1209 pack max | 21,908 | 0 | 75.2 | 18.5341 | 17.9 | 6.1 | 35.79 |
| 1272 pack inlet | 376,303 | 0 | 1023.98 | 21.3695 | 12.0 | 0.0 | **127.09** |
| 1273 pack outlet | 372,630 | 0 | 1023.98 | 21.0657 | 12.0 | 0.0 | **79.9** |

The ambient maximum of 39.5°C makes hot-weather exposure **possible**, but ambient co-occurrence with charging/battery load and sustained heat periods is unverified. The pack-max 75.2°C single-channel maximum and zero-coded pack minimum values warrant independent checking, not automatic removal.

## 5. ID1 threshold QA (measured record counts; flag threshold only, not confirmed invalid-code semantics)

| ID | n zero | n >=60 °C | n >=80 °C | n >=100 °C | n >=200 °C |
|---|---:|---:|---:|---:|---:|
| 1208 pack min | 2,890 | 0 | 0 | 0 | 0 |
| 1209 pack max | 17 | 1 | 0 | 0 | 0 |
| 1272 pack inlet | 19,797 | 4,356 | 3,794 | **3,772 (1.002%)** | **3,718** |
| 1273 pack outlet | 20,839 | 4,313 | 3,726 | **3,693 (0.991%)** | **3,644** |

Values **greater than 200°C** are outside the published dictionary bound for IDs 1272/1273 (counts are for >=200, so check equality to separate strict violations). Examples of recurring likely invalid/decoded codes:
- `1023.0`: ID1272 **2,400** rows; ID1273 **2,188** rows.
- `1023.98`: **1** row in each channel.
- Also `1022`, `1019`, and clusters around `271.5`, `528`, `588`, `592` °C.
- `1023` equals 2^10-1; `1023.984375` equals 65535/64. These arithmetic resemblances are **hypotheses for diagnostic/saturation encoding only**. No authoritative decoding scheme has been confirmed for these exact channels.
- Zero values, 50.13°C outlet on a cold night, and 75.2°C battery-max readings require contextual tests; do not classify solely by intuition.

## 6. Within-second co-occurrence (avoid mislabeling as simultaneously sampled)

From **225,906 one-second bins where both channels were observed**:
- Both >=100°C: **960 seconds** (0.425%).
- Inlet only >=100°C: **1,498** (0.663%).
- Outlet only >=100°C: **1,563** (0.692%).
- Neither >=100°C: **221,885** (98.220%).

The conditional rate `P(outlet_flag | inlet_flag)` is **960/(960+1498)=39.06%**, compared with `P(outlet_flag | inlet_not_flag)=1563/(1563+221885)=0.70%`. This establishes strong pooled temporal association; **does not prove a shared fault** due to temporal clustering, asynchronous measurement and correlated operating conditions. These second-level figures differ from raw flagged row counts.

Temporal excerpt **2021-12-22**:
- 00:37:24.733 ambient **-5.5°C**; 00:37:24.916 pack-min **0.0°C**.
- 00:37:30.008 outlet **1023.0°C** and 00:37:30.009 inlet **1023.0°C**, just **1 ms** apart.
- 00:38:00.115 inlet **1023.0°C**; 00:38:00.116 outlet **50.13°C**, illustrating disagreement.
- 00:38:05.044 pack-max **6.1°C**; later both inlet/outlet again 1023.0.
- First 30 joint flagged seconds returned 1023.0°C in both channels over 00:37:30–00:47:47 on 2021-12-22.

## 7. Suitability for thesis and admission gate

**Status label: `USER_LOCAL_ACQUIRED_ID1_PROFILED_THERMAL_QA_PENDING`.**
- **Eligible empirically:** actual vehicle-side field battery thermal/voltage/SOC and operational environmental observations, after channel-specific QA.
- **Potential use:** standalone battery thermal state response and charging-event context; compare with separately verified transformer and EVSE datasets with explicit non-co-location assumptions; stress-testing component models or inference methodology.
- **NOT observed/qualified:** transformer hot-spot/top-oil of same installation, charging-station internal rectifier/cooling/derating, distribution feeder topology to this vehicle's charging event, synchronized P↔T coupling or intervention/recovery evidence. Cannot empirically validate the joint coupled thermal SoS model or claim causal heat derating from these readings alone.
- **G0/G1:** original documented field provenance and local acquisition supported by source and user's readback. **Original-file checksums and third-party access verification pending.**
- **G2:** schema confirmed for ID1; thermal validity/clock/metadata/coverage incomplete. **Not passed for thermal calibration.**
- **Further gates:** synchronized electrical and charging state, causal inputs, model identifiability, data split and uncertainty quantification open; physically connected power–EVSE field gate absent.

## 8. Ordered next actions (requirements and acceptance criteria)

1. **Freeze source provenance:** capture `git rev-parse HEAD`, `git lfs ls-files`, SHA-256/byte sizes for all seven original Parquet files, license and paper DOI; keep immutable originals separate from derived CSV/QA files. No claim of Drive backup until uploaded and verified.
2. **Full seven-vehicle inventory:** DuckDB per-file record counts, distinct `value_id`, `MIN/MAX(time)`, units/source dictionary mapping, non-null and `NaN/Inf` tests, duplicates, negative/forward gaps, actual per-channel sampling and missingness. Complete unknown ID1 `MIN(time)` and distinct value IDs.
3. **Signal/decoding validation:** confirm whether 1272/1273 are coolant temperature vs general pack inlet/outlet sensors; ask dataset authors for UDS raw decoding, out-of-range codes, sentinel values, scaling and any original error flags. Compare anomalous 1023/271/528/592 clusters with source bounds. Preserve an explicit `qa_flag` and reason for every filtered observation; never overwrite original value.
4. **Independent thermal coherence:** inspect rare battery max at 75.2°C, zero-coded minimum temperature, abrupt derivatives, inlet/outlet differences, near-synchronous cross-channel matches and changes across diagnostic episodes. Stratify by vehicle, date, charging vs driving/parking; avoid global threshold cleaning without evidence.
5. **Real charging exposure:** use `data/value_overview.csv` to discover *verified* HV current/power and charging-state signal IDs, alongside SOC ID900, battery V ID1200, temperature IDs15/1208/1209/1272/1273. Verify electrical sign conventions, observed continuity and distinct physical current paths; do not invent missing EVSE power.
6. **Synchronization and event segmentation:** preserve nanosecond timestamps; verify timezone, sample rates, charging periods and actual sensor overlap, then use as-of joins with measured tolerances and explicit gap limits. Never treat nearest sensor observation as truly simultaneous or fill gaps without provenance.
7. **Physics and statistics:** only after 1–6, establish thermodynamic state definitions, model inputs, leakage-free time/vehicle holdouts, sensitivity, UQ, parameter identifiability and external comparison. Do not fit to flagged values or report joint power–transport validation.
8. **Evidence transfer:** create immutable analysis outputs + QA report per vehicle; optionally upload properly hashed source files to authorized storage (not yet done). Record which SO1–SO3 component claims are supportable. Keep source datasets from different installations separated.

## 9. Reproducible read-only local commands

From `~/Downloads/electric-vehicle-uds-dataset`:
```bash
git rev-parse HEAD
git lfs ls-files
shasum -a 256 data/uds_data/*.parquet
du -h data/uds_data/*.parquet
duckdb -csv -c "SELECT COUNT(*) AS n, COUNT(DISTINCT value_id) AS channels, MIN(time) AS t0, MAX(time) AS t1, COUNT(*) FILTER (WHERE value IS NULL OR isnan(value) OR isinf(value)) AS null_nan_inf FROM read_parquet('data/uds_data/ID1.parquet');"
duckdb -csv -c "SELECT value_id, COUNT(*) AS n, COUNT(*) FILTER (WHERE value > 200) AS above_source_max FROM read_parquet('data/uds_data/ID1.parquet') WHERE value_id IN (1272,1273) GROUP BY 1 ORDER BY 1;"
duckdb -csv -c "SELECT (SELECT COUNT(*) FROM read_parquet('data/uds_data/ID1.parquet')) AS parquet_rows, (SELECT COUNT(*) FROM read_csv_auto('ID1.csv')) AS csv_rows;"
```
**Do not erase or mutate original Parquet files.** The CSV row-count command requires `ID1.csv` already exported; it is not a file-integrity hash comparison.

## 10. Pending external evidence for full coupled model

Separate verified datasets (e.g. SINTEF transformer field thermal records; Qatar charger thermal measurements, raw not yet acquired; Slovenian transformer P/Q data) cannot be represented as a single field-installed coupled system without documented physical connectivity and synchronized observations. TUM is relevant **component-level vehicle evidence** only. Continue searching actual transformer–EVSE–vehicle installation records with operational temperatures, electrical/charging states, time bases and topology.
