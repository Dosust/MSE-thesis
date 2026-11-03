# Field-only acquisition gate — 2026-11-03

**Canonical thesis title V3:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.

## Mandatory scientific rule
Only genuine *operational field measurements* qualify. Actual hardware tested solely in a laboratory/research center is NOT eligible; neither are simulated results, synthetic data, calculated thermal states or unconstrained merged multi-site time series.

An original online record of a file is evidence of **file existence and described field origin**, NOT proof that we downloaded and inspected its raw bytes.

## Priority dataset leads
**P1-A — SINTEF 2024, DOI 10.5281/zenodo.17223516:** the closest match for transformer thermal state-time calibration. The repository explicitly identifies `Barug2025_sensordata.csv` (873 kB; published MD5 `5d81840a2f901f04fded98c3e1097b6e`), with recorded current, voltage, ambient, top/bottom oil, HV/LV hotspot/mid-spot and clamping series, from a 40 MVA ONAN transformer **in operation** in Norway in 2024. It separately labels `Barug2025_calculated.csv`; computed results must NOT enter the observed measurement table. Original file bytes NOT accessed in this run. Original link: https://zenodo.org/records/17223516/files/Barug2025_sensordata.csv?download=1 . Source: https://zenodo.org/records/17223516 .
**P1-B — Qatar 2026, DOI 10.1016/j.ecmx.2026.101960:** real commercial 50 kW DC charger field study spanning extreme summer conditions; observed rectifier and ambient temperatures, offered and delivered power, SOC and power quality; temperature sensors reported 5 min, electrical telemetry 1 min. **DATA ON REQUEST; no released file located**. Corresponding author Abdelbasset Krama per HBKU institutional publication. Request original synchronized anonymized logs and instrument/quality metadata, without implying delivery.
**P1-C — Slovenia STREAM 2025:** primary real 20/0.4 kV transformer-station P and Q at 15 min, DOI 10.5281/zenodo.20927130; **pair with the independently released anonymized transformer technical parameters**, DOI 10.5281/zenodo.20927801. Candidate for measured electrical boundary conditions, **NOT thermal calibration**. Individual original CSV contents not inspected.
**P2 — Caltech ACN-Data:** genuine operating-site EVSE charging sessions/current and estimated/requested departure needs, but no measured EVSE internal or transformer temperature and no confirmed transformer network map. https://ev.caltech.edu/dataset
**P2 conditional — KIT:** instrumented campus EV charging and measured ambient temperature, DOI 10.5281/zenodo.17866847. Verify **real-world field status** (routine operational installation versus staged testing) prior to strict admission. No charger internal temperature.
**P2 restricted — Hydro-Québec 2026 paper:** authentic 2021–2025 substation data but author states **not publicly available**. DOI 10.3390/en19174224.
**Excluded:** controlled KU Leuven EnergyVille charging experiments (DOI 10.48804/C5PT0R) and TU Dortmund laboratory charging profiles (DOI 10.1038/s41597-025-05524-5) from strict field-only collection.

## Current evidence stage
- **FIELD ORIGIN established by source publisher:** SINTEF 2024 transformer, SINTEF DynaLoad, Slovenian transformer stations, Qatar commercial charger, Caltech operational EVSE.
- **Original raw data files obtained and locally audited in THIS acquisition pass:** 0. Download attempts were not successful; do not claim otherwise.
- **One shared instrumented transformer→EVSE installation with synchronized both-side thermal measurements:** 0 confirmed.
- **Field-calibrated unified SO2/SO3 model:** NOT ESTABLISHED.

## Acceptance gates (apply independently per candidate)
- G0 — Field-origin proof: operating site, original physical hardware and measurement method; exclude lab/simulation/synthetic.
- G1 — Original file acquisition: downloaded unmodified bytes, expected file inventory, SHA-256 and publisher checksum compared.
- G2 — Schema: physical variable definitions, units, observed versus computed flag, sensor position, sampling, time zone, QC.
- G3 — Source physical topology: true transformer, feeder, charger and vehicle identifiers + electrical connection.
- G4 — State/time adequacy: temperatures and power at sufficient temporal resolution; synchronize clocks, document missing data.
- G5 — Independent train/test split and physical validation with declared uncertainty, with field installation distinctions preserved.
- G6 — Directional dependence: common ambient heating alone not causal coupling; matched forcing and true interface effects needed.
- G7 — SO3: required/delivered electricity and charge-by-departure service plus justified thermal threshold crossing/propagation delays.

**Gate interpretations:** A transformer-only operating dataset can be admitted to thermal calibration (G0–G2 pass) while remaining INSUFFICIENT for a **coupled field** claim (G3–G7 not established). Field data from unrelated facilities must never be combined into fake joint observations.

## Next actions
1. Fetch `Barug2025_sensordata.csv` (not calculated file) and `README.txt` through authenticated/open Zenodo access; check publisher md5, preserve raw hash, inspect header/time gaps.
2. Fetch Slovenia 2025 `control_measurements_P_2025.csv`, `control_measurements_Q_2025.csv` and `transformer_parameters_anon.csv`; confirm shared station IDs, units and quality.
3. Request Qatar original commercial EVSE rectifier temperature, electrical power, ambient and charging session measurements, instrument accuracy and clocks.
4. Investigate whether **any** single operating site provides synchronized transformer and EVSE thermal observations. If not, keep SO2 model conclusions conditional and validate component models separately.
5. Record source-to-data traceability and split **observed / calculated / scenario inputs** in all analyses.

See `field_candidate_register.csv` for row-level records and direct source links.

The materials are **candidate registration only**: no original field-data measurement CSV has been copied into GitHub or Drive in this pass.
