# Master Data Inventory — Power–Electrified Transportation Interdependencies — 2026-11-03

**Research title:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Status:** WORKING EVIDENCE INVENTORY, not frozen thesis authority.  
**Scope:** Extreme-heat thermal interdependencies P ↔ T_e, state-time dynamics, electricity/mobility service consequences.  
**Method:** Consolidated from local original-file audits, source-linked evidence registers, first validation cycle, 77-lead screen, and latest user archives. This is **not** an assertion that every candidate source in all repositories has undergone full-text or full-file validation.

## Critical interpretation

- A **retrieved source**, a **quality-screened measurement**, a **verified physical model**, and a **validated cross-system thermal interdependency** are four distinct scientific milestones.
- **Current connected thermal field validation: BLOCKED.** No common physically mapped transformer–EVSE system with synchronized transformer/charger thermal states, electrical power and observed thermal operating restrictions has been verified.
- Separate-source timestamps must never be joined as though they represent the same measured installation.
- Do not add model-only or assumed reactive power to a measured-data count.

## Acquired and examined

| ID | Dataset | Observed contents / previously completed work | Status for thesis physics | What remains |
|---|---|---|---|---|
| D01 | SINTEF transformer, 40 MVA | 8,592 hourly 2024 records: electrical current, voltage, ambient, top/bottom oil, winding/hot-spot channels; official source hashes checked | **MEASURED P component — provisional model** | Improve independent winding/oil prediction and calibrated uncertainty; identify parameters; test limits of extreme heat extrapolation (measured maximum ambient 25.97 °C) |
| D02 | KU Leuven / EnergyVille BEV measurements | 134 original AC/DC charging sessions; 103 with >=100 complete plausible sample rows; independent 5/15-min session holdout tests | **MEASURED T_e component — model blocked** | Reconcile CAN semantics/current polarity, battery preconditioning, sensor staleness, DC thermal model/uncertainty; AC persistence sometimes outperforms physics model |
| D03 | EPFL level-3 charging | 1,878 sessions; original minute-level electrical measurements, session QA performed | **MEASURED charging component — provisional electrical boundary** | Explain published 64,277 vs audited 61,816 populated minutes; reconcile AC input/DC output, per-plug power, energy integrals, nine nominal-rating exceptions |
| D04 | OPSD household EV+grid | Official 60.5 MB source acquired, hashed; 116,355 qualified derived 15-min intervals at 2 same-premises sites; chronological electrical forecast benchmark | **MEASURED METER BASIS, DERIVED ELECTRICAL BENCHMARK** | Verify reporting interval/meter and other-load/PV boundaries; seek transformer/charger topology and thermal sensors; no causal effect established |
| D05 | Iowa 296-node smart-meter | Two workbooks: 8,760 hourly 2022 readings, 226 bus-load series across 3 feeders; P derived from 1-hour energy; Q based on randomly assumed PF 0.90–0.95 | **MEASURED/AGGREGATED ENERGY; ASSUMED Q — supporting grid model** | Obtain matching OpenDSS model, topology, clock/asset map, ratings and license; validate load/P/Q mapping and independent power-flow |
| D06 | OSF 94GKC Li et al. 2026 | 313 controlled AC EV charging disturbance CSVs, 4,061,379 rows; raw code+README; only 0.57% battery-temperature cells populated; four 1538.3 values | **CONTROLLED electrical lab, not heat coupling** | Establish sensor/DAQ and interpolation provenance, reconcile three schema variants; use for power-quality electrical response only |
| D07 | DOE/ORNL live archive V1 | 22 candidate original-file links found; 4 small MD5-verified downloads: two SINTEF CSVs already in D01, two TU Dortmund metadata indexes | **ACQUISITION METHOD, not four distinct new measured systems** | Access ORNL 35-file DOE EV collection (public API had 0 records/attachments), request original TU Dortmund time series, review oversized files/rights |
| D08 | FCP ChargePoint session CSV — new | 259,415 rows, 33 columns, 2011–2020 sessions, energy, duration, charger labels, geolocation and identifiers | **NEW / NOT YET SCIENTIFICALLY QUALIFIED** | Verify publisher/license, timestamps/duplicates, energy-duration power plausibility, charging boundary; contains location/driver/identifier fields — do not commit raw |
| D09 | FCP independent weather/PV/price CSVs — new | Singapore hourly temperature 52,584, Singapore price 52,560; Stanford PV 15,454 half-hour rows; 36-row forecast | **NEW / SEPARATE ORIGINS; NO CONNECTED MEASUREMENTS** | Verify source units, timezone, completeness and dates; do not join Singapore heat/price with California charging as same observed site |
| D10 | SPS Cyprus LV suburban network | 315-kVA 11/0.4-kV benchmark topology, 3 feeders; model in code/Drive research sheet | **BENCHMARK MODEL, NOT FIELD THERMAL** | Reproduce power flow; independently verify assumptions, do not infer EVSE thermal data |
| D11 | SPS PyEPlan five-bus | 5-bus code/test case, P/Q sample data byte-identical in existing audit | **SOFTWARE EXAMPLE ONLY** | Verify units, reason P and Q are identical, timestamp semantics and solver outputs |
| D12 | 500-row EV battery event file | 500 rows, 24 fields; average temperature equals midpoint in 500/500; power equals V×I within rounding | **QUARANTINE / unverified provenance** | Original experimental origin and independent sensor logs; unsuitable for physics calibration as-is |
| D13 | EV charging/routing archive | 64,945 hourly labels, 28 features, 31 abstract location nodes; major identity, calendar and conditional energy inconsistencies | **QUARANTINE / likely synthetic** | Origin/algorithm documentation; software QA only; original and reproducible audit safely saved |
| D14 | French charging-station `data.csv` | Single 39-field station-information record, including contact details | **METADATA ONLY / privacy-limited** | No time-series use; avoid raw publication |
| D15 | Kaggle grid–transport resilience table | 5,000 scenario/time-step rows; missing electrical connection/thermal state and charging measurements | **SYNTHETIC/SCENARIO-LIKE; no validation role** | Keep only for synthetic test scaffolding with source documentation |
| D16 | Physics-informed virtual coupling experiment | 36 virtual cases, 103,680 minute-resolution simulated rows, numerical/conservation checks completed | **SYNTHETIC MODEL TEST ONLY** | Replace illustrative coefficients with admitted laws/parameters; independent connected validation remains blocked |

| D17 | KU Leuven C5PT0R EV charge efficiency, EnergyVille | 40,873 measured/processed AC CSV records (4 files), five XLSX files including 258 DC converter samples with AC/DC input/output and battery temperature; publisher file checksums match | **MEASURED T_e ELECTRICAL + BATTERY THERMAL, CONDITIONAL COMPONENT ONLY** | Three AC files have backward timestamp steps; suspected swapped charger current/voltage labels in one DC test; validate meter boundaries/overlap with D02; no EVSE internal temp, derating, transformer link |
| D18 | Mendeley single-phase transformer thermal images V3 | 255 RGB 320x240 laboratory IR images of one healthy + 8 induced-fault configurations; 45 expert ROI masks plus 45 paired reference images | **LAB MEASURED FAULT IMAGING, AUXILIARY ONLY** | 1 kW dry-type 1-phase transformer, reported ambient 23°C; color images not calibrated heat time series; cannot validate oil/hotspot dynamics, severe heat, or P↔T_e coupling |

**New upload audit:** [Two uploaded archives — qualification and QA](./UPLOADED_ARCHIVES_QUALIFICATION_2026-11-03.md). Originals are in the existing Drive Data folder, documented by DOI, SHA-256 and Drive links in that audit; these are **D17/D18 additional sources**, not repairs to the existing D01–D16 data.

## High-value externally identified sources not yet qualified as full connected thermal datasets

| Lead | What public evidence supports | Blocker |
|---|---|---|
| KIT Campus North OLTC + low-voltage EV | 100-ms multivoltage electrical observations; source DOI https://doi.org/10.5281/zenodo.22826984 | ~20 GB original, branch map transformer→EV and synchronized equipment heat telemetry not shown |
| Electric-bus transformer installation | Primary/secondary electrical and harmonic measurements around 2,000-kVA transformer; DOI https://doi.org/10.1109/PESGM58988.2026.11693150 | Public raw series, oil/winding temperatures and derating records not verified |
| Qatar fast charger | Measured charger power/ambient/rectifier derating under up to 55°C; DOI https://doi.org/10.1016/j.ecmx.2026.101960 | Raw data on request; transformer-to-charger thermal linkage unknown |
| TU Dortmund Esser et al. laboratory | Grid/charger synchronized electrical tests; DOI https://doi.org/10.1038/s41597-025-05524-5 | Downloaded 2 index CSVs are NOT original experimental waveforms or transformer temperatures |
| UrbanEV occupancy and others | Station availability/event studies, source DOI https://doi.org/10.5061/dryad.np5hqc04z | Charging volume derived from duration/rating rather than necessarily metered, no thermal P↔T_e |

## Research completion gates

| Gate | Current status | Minimum for advancement |
|---|---|---|
| Source discovery and intake | **DONE initial 77 metadata/title leads (not unique datasets); 9 priority primary studies** | Continue targeted sources only for missing physical interface |
| Original data integrity/provenance | **PARTIAL** | Audit individual original files, instrument/clock/units, publisher license, source SHA/checksum |
| Electrical co-location benchmark | **COMPLETED supporting experiment** | Need actual feeder/transformer/EVSE IDs and measurements |
| Transformer model | **PROVISIONAL** | Winding/oil and temperature UQ, independent days, extreme heat transfer limitations |
| Vehicle battery model | **BLOCKED** | Independent holdout skill vs persistence, DC session coverage, cooling observability |
| EVSE physical derating model | **BLOCKED** | Charger temperatures, losses, cooling/derating flags and equipment limits |
| Network topology for selected application | **BLOCKED** | Single-line + asset mappings; simulate only after documented model available |
| P→T_e and T_e→P *observed* thermal effects | **BLOCKED** | Same-site synchronized power + thermal + restriction/response measurements |
| SO2 unified coupled model | **CONDITIONAL VIRTUAL ONLY** | Admit source-supported interface laws, parameter identifiability and independent validation |
| SO3 service resilience and sustainability | **CONDITIONAL VIRTUAL ONLY** | Measured/justified service requirements, horizon, thermal transitions, matching scenarios and bounded indicators |

## Execution queue (highest first)

1. **P0 — Connected field evidence:** KIT single-line/PMU-to-EV mapping, electric-bus depot owner, Qatar rectifier data; request original synchronized electrical & thermal traces, clocks, equipment and thermal protection data.
2. **P1 — Component model credibility:** SINTEF hot-spot/oil calibration, identifiability and proper predictive uncertainty; KU Leuven independently held-out thermal model; EPFL energy/charging boundaries.
3. **P1 — Electrical network baseline:** Obtain Iowa 296-bus OpenDSS topology and join only documented meter IDs; execute/verify load flow; use Cyprus/PyEPlan only as explicitly simulated test cases.
4. **P2 — Original EVSE and FCP:** Audit Qatar measured derating, TU Dortmund actual waveform files; for FCP ChargePoint sessions verify provenance, timestamps, privacy and energy plausibility.
5. **P2 — Conditional physics coupling:** Use separately validated component models, transparent hypothetical topology/constraints, paired thermal-mechanism ablations and full numerical/model uncertainty. Never claim this is field-validated coupling.
6. **P3 — SO3:** Predefine service energy-by-departure, critical electricity demand, transition/recovery timing and sustainability indicator boundaries before attributing resilience gains.

## Original-source and qualification links

- SINTEF: https://doi.org/10.5281/zenodo.17223516
- KU Leuven: https://doi.org/10.48804/8KPDTW
- EPFL: https://github.com/DESL-EPFL/Level-3-EV-charging-dataset
- OPSD: https://data.open-power-system-data.org/household_data/2020-04-15/
- Iowa original in Drive: https://drive.google.com/file/d/1Fk3jvLBGe_9vyVi1_AAdz8dvUJ753Foq/view
- OSF original in Drive: https://drive.google.com/file/d/1Sjdg5TaGWXybjO_8DOlnkzIeSHpVhR4x/view
- Quarantined routing archive: https://drive.google.com/file/d/1-XY4-xDP5sfpbv3gPzTyHhjJ0ZJR2nYj/view
- [Existing Data folder](https://drive.google.com/drive/folders/10vfbC7cNM4IjEIsKaM8d-V7U8HaCanb2) contains Iowa/OSF originals, quarantine/audit packages and a separate *SPS-specific* evidence spreadsheet, **not yet a consolidated master register**.
- [First-validation methodology](https://doi.org/10.5281/zenodo.17223516) and local supporting research artifacts are indexed in earlier research execution.
- FCP source original SHA-256: `416a619a829823bfc5cebdf7c193ada6d6807d0aeff734a05e4345c56a025095`. ZIP CRC check passed; the user-uploaded FCP source has **not** been uploaded to Drive or admitted as experimental evidence.

**No model parameters, thermal limits, causal links, or field measurements have been fabricated. No frozen scientific files have been modified.**
