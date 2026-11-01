# Executed dataset portfolio audit — 2026-11-01

**Status:** DOCUMENTATION AUDIT COMPLETE; RAW ACQUISITION/PHYSICAL VALIDATION OPEN.

**Governing thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience. Only directional **thermal** Power–Electrified Transportation effects under extreme heat are in active scope, and SO1–SO3 remain unchanged.

## Execution facts
- The source ontology was read directly from `project/data_ontology/power_electrified_transport_thermal_v1/data_dictionary.csv` at Git blob `62b041e5eb80e46448b3a39b74a098c42fe30240`.
- Exact dictionary rows: **301**. Distinct tables: **21**.
- Inventory: **15** distinct source/authority records; includes peer-reviewed **papers** and **synthetic network benchmarks** that must not be described as physical observational datasets.
- Preliminary explicitly mapped source-to-field candidates: **24 unique ontology field labels**, with one or more source descriptions supporting a related quantity. **This is not a validated field-coverage score.**
- Raw datasets acquired by this audit: **0** (external HTTP/DNS access blocked in the local execution environment; the GitHub connector provided repository ontology text and public metadata but not source workbook/ZIP bytes).
- Mechanism-ready coupled transformer–EVSE dataset: **0**.
- This new 15-entry portfolio is **reconstructed** from the earlier 14-entry working register and additional verified public sources; it is **not claimed to reproduce the absent earlier 15-source CSV**.

## Corrections to prior interpretation
1. ETT `OT` is oil temperature, **not verified top-oil sensor temperature**; its time zone is not established. Do not auto-admit `transformer_top_oil_temperature`.
2. Shenzhen `charging_gun_temperature*` measures a connector region, not verified internal rectifier/cabinet temperature; do not auto-admit `evse_temperature`.
3. EPFL `Pset` is a charging setpoint, **not verified thermal limiting capability or thermal reason**.
4. Weather temperature cannot be relabeled as the actual equipment temperature.
5. Transformer measurements from Norway cannot be joined to Swiss charging records as an observed physical transformer–EVSE installation.
6. Real topology/flow inputs and simulated scenarios are not independent coupled-thermal validation data.
7. `documentation_candidate=YES_DOC_ONLY` is an indexing aid, **not a scientific admission decision**.

## Four noncompensatory evidence gates
| Gate | State | Reason |
|---|---|---|
| G1 Raw source integrity | OPEN | No primary raw file bytes downloaded in this execution |
| G2 Physical-time and sensor semantics | OPEN | Documentation-only candidate names are insufficient |
| G3 Directional thermal mechanism | BLOCKED | No co-installed directional sensor and restriction dataset |
| G4 Independent VVUQ and service validation | BLOCKED | No admitted coupled-case service and hold-out records |

## Minimum next admissible operations
1. Acquire exact primary sensor CSVs `Barug2025_sensordata.csv` (SINTEF) and `measurements.csv` / `parameters.csv` (Esser); preserve file-specific hashes.
2. Audit EPFL original measurement and session workbooks, using measured AC P, charger Pset, Preq and SOC without inferring a thermal cause.
3. Request Qatar synchronized controller, rectifier temperature, AC power and operating-mode records; separately verify measured versus inferred quantities.
4. Seek a verified transformer–bus–EVSE map together with transformer thermal restriction events and charger derating causes. If unavailable, use explicit **separately validated components + declared simulation**, never label the composite as field validated.
5. Define required vs delivered electricity and mobility services and test independent holdouts before SO3 empirical claims.

## Primary source registry
- **S01 TU Wien LV Test Grids:** https://data.mendeley.com/datasets/hgh8c99tnx/1 — Documentation verified; original files not retrieved this execution
- **S02 Qatar Siemens CPC50 field experiment:** https://doi.org/10.1016/j.ecmx.2026.101960 — Study verified; synchronized original measurements not acquired
- **S03 Esser TU Dortmund AC/DC charging:** https://zenodo.org/records/14065331 — File list verified; raw ZIP not downloaded
- **S04 Najar et al. ONAN transformer thermal model:** https://doi.org/10.1016/j.applthermaleng.2017.03.061 — Publication confirmed; equipment transfer not established
- **S05 SINTEF Bærug 40 MVA transformer monitoring:** https://zenodo.org/records/17223516 — Measured-vs-calculated file distinction verified; raw CSV not retrieved
- **S06 EPFL Level-3 EV charging:** https://github.com/DESL-EPFL/Level-3-EV-charging-dataset — Official README and XLSX listings verified; raw workbook not retrieved
- **S07 KIT EV charging 2026:** https://zenodo.org/records/17866847 — Metadata fields verified; large waveform files not retrieved
- **S08 Shenzhen Autosun-PolyU charging:** https://data.mendeley.com/datasets/c7gg94tmvz/3 — Gun temperature is not rectifier temperature; raw data not retrieved
- **S09 KU Leuven EV charging measurements:** https://doi.org/10.48804/C5PT0R — Prior repository register; new primary-file verification not completed
- **S10 KU Leuven BEV energy dynamics:** https://doi.org/10.48804/8KPDTW — Prior repository register; new primary-file verification not completed
- **S11 NASA POWER hourly meteorology:** https://power.larc.nasa.gov/docs/services/api/temporal/hourly/ — API documentation reviewed; data request failed from this runtime
- **S12 ETT small transformer time series:** https://github.com/zhouhaoyi/ETDataset — README/headers confirmed; oil sensor location and time zone not established
- **S13 236-bus low-voltage network:** https://zenodo.org/records/8274780 — 34.6 MB workbook listed; file not retrieved
- **S14 SMART-DS NREL distribution networks:** https://data.openei.org/submissions/2981 — Official dataset description verified; no real transformer/charger physical join
- **S15 Synthetic grid in Pypower format:** https://zenodo.org/records/3603126 — Zenodo dataset and file listing verified; files not retrieved

## Trust and reproducibility note
This audit only tests source-documentation *candidates*. It does not test the raw file values or demonstrate a state-space equation, thermal restriction law, causal effect, or resilience outcome. The original files and measurements must be acquired before any new empirical model admission.
