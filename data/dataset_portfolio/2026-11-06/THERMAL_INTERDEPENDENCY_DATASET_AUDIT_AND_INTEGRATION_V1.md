# Thermal Power–Electrified Transportation Dataset Audit and Integration V1

**Date:** 2026-11-06  
**Status:** WORKING RESEARCH EVIDENCE REGISTER — NOT CANONICAL, NOT A VALIDATED COUPLED FIELD EXPERIMENT  
**Repository:** Dossiya-SE/MSE-thesis  
**Scope:** Extreme-heat-conditioned thermal interdependencies between the **Power System (P)** and the **Electrified Transportation System (T_e)**, respecting the full canonical T_e system boundary.  
**Authorities:** AI_RESEARCH_INSTRUCTIONS.md; project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md; project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md; project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md; project/EGMIV_METHOD_V1.md. This working document does not amend frozen text, models, or scientific status.

## 0. Governing research objectives — reproduce exactly

- **SO1 — Identify and qualify:** Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.
- **SO2 — Model state-time evolution:** Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.
- **SO3 — Quantify consequences:** Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

**Research principle:** Combine independently established work according to clearly identified roles. A dataset does not have to provide every variable; however, joining unrelated installations creates a transparent **composite simulation** and not empirical observation of a single coupled plant. Transferability and uncertainties must be demonstrated.

## 1. Screening and evidence-status protocol

For each candidate distinguish:
1. **R — Primary record / publication checked:** official metadata/source and published variable descriptions; does not prove numerical file quality.
2. **F — Files inventoried / schemas inspected:** original file listing or direct source file schema; not full row-wise QA.
3. **Q — Numerical QA actually performed:** downloaded data interrogated; name exact partition and tests.
4. **M — Local user-held measured data:** prior Mac-run hashes/measurements recorded in this repo; not a new run on this date.
5. **A — Author-request only:** paper available, but required original time series not downloaded.
6. **S — Simulator/method, not field data:** useful for model implementation and verification but not independent empirical validation.
7. **OPEN:** not independently established.

Audit fields: site/instrument, topology, equipment class, sensor identity, unit, measured/estimated/reconstructed/model-simulated provenance, timebase, clock accuracy, heat exposure, disturbance mechanism, control actions, thermal threshold, power-flow sign, service commitment, access/license, source file hash, QA, and transfer domain. Treat evidence for P→T_e and T_e→P **independently**. Common heat exposure alone is **not** directional thermal dependence. Bidirectionality does **not** require V2G.

An **electrical P→T_e** dataset or a **thermal component** dataset is supporting evidence until a heat-conditioned restriction is independently qualified. Do not silently relabel these as observed thermal interdependencies.

## 2. Prioritized portfolio — sources and bounded research roles

### A. Primary experimental component, interface and mobility evidence

| ID | Candidate and source | Data granularity / observed contents | Relevant role | Status; main blocker |
|---|---|---|---|---|
| D01 | **SINTEF Bærug et al. transformer field sensors** — [Zenodo 17223516](https://doi.org/10.5281/zenodo.17223516) | 2024 monitored 40 MVA ONAN transformer; measured voltage, current, ambient, top/bottom oil, HV/LV winding mid-/hot-spot temperature, clamping; sensor CSV separate from calculated-model CSV; time frequency needs source-file QA | **SO1/2 P thermal states; independent component validation**, parameter/observability tests | **R; raw CSV published**. Site has no demonstrated corresponding EVSE. Distinguish observed and calculated columns; address gaps, sensor location, instrument uncertainties and equipment transfer. |
| D02 | **KIT campus OLTC 110/20/0.4-kV including EV point** — [Zenodo 22826984](https://doi.org/10.5281/zenodo.22826984) | 100 ms synchronized-range electrical voltage/current; LV three-phase P/Q and EV-related measurement location; approx. 50 days | **SO1 directional electrical observation and supporting T_e→P / P→T_e response tests** | **M; three Parquet files user-local checksum-verified; repo logs 129.6M timestamp-grid PASS**. No temperature, exact feeder parentage/control-state proof or charge-by-departure observation. Association ≠ causal effect. Preserve existing M1–M3 and unmatched control findings. |
| D03 | **KIT 20-ms voltage-step PHIL EV charging trials** — [Zenodo 22965111](https://doi.org/10.5281/zenodo.22965111) | Controlled 230 V AC voltage perturbations, five EV types, 11-kW setup, per-phase RMS V/I in original CSVs, relative time | **SO1 controlled *electrical* P→T_e mechanism, model structure / falsification** | **R/F; CSV listing verified; rows not audited here**. Different site/trial from D02; no asserted internal charger temperature, transformer thermal sensor or mobility deadlines. |
| D04 | **EPFL Level-3 DC charging** — [Original repository](https://github.com/DESL-EPFL/Level-3-EV-charging-dataset) | 64,277 one-minute measurements; 1,878 sessions; P (AC W), Pset, Preq, energy Wh, SOC, charging capacity/controls, two CCS outlets | **SO1/2 EVSE power constraint and charging-service consequence proxies** | **R/F official source description**. No reported measured EVSE rectifier/core temperature, measured transformer thermal trajectory or verified mobility commitment. Pset<Preq is observed restriction but thermal *cause* is not established. |
| D05 | **TU Dortmund Esser et al. laboratory charging** — [paper DOI](https://doi.org/10.1038/s41597-025-05524-5); [data DOI](https://doi.org/10.5281/zenodo.14065331) | 142 EV charging profiles, eight EVs, sub-second grid/vehicle observations; some equipment logs charging status, setpoints, P/Q, SoC, ambient, DC states | **SO1 controls / operational coupling and SO2 EV charging dynamics** | **R; device/mode-dependent fields**. Read parameters.csv, measurements.csv and chosen session files; no single uniform schema or co-site transformer thermals. |
| D06 | **KIT EV charging characterization** — [Zenodo 17866847](https://doi.org/10.5281/zenodo.17866847) | 18 datasets, 16 EVs; low/high-frequency time series, three-phase V/I/P, setpoint and SOC; environmental temperature is documented | **SO1/2 charger/vehicle electrical response, ambient context** | **R; original large files available, not row-QA here**. Ambient temperature ≠ EVSE internal temperature; no measured connected transformer temperature. |
| D07 | **Qatar commercial DC fast charger under extreme heat** — [Krama et al., 2026](https://doi.org/10.1016/j.ecmx.2026.101960) | Field study reports ambient temperature, rectifier temperature, offered/delivered power, efficiency, harmonic distortion and SOC trajectories | **SO1/2 primary *thermal* T_e component mechanism / derating and service-time evidence** | **A; original synchronized raw measurements available on request, NOT acquired**. Strong thermal-field lead; no demonstrated same-site transformer winding/oil observations. No parameter calibration from paper-level descriptions alone. |
| D08 | **US DOE EVs@Scale NextGen EVSE characterization** — [official technical report](https://www.nrel.gov/docs/fy25osti/93967.pdf) | Controlled hot/cold ambient tests, connector/cable power limiting, charger electrical characteristics and control response (report-level results) | **SO1/2 independent EVSE thermal-protection mechanism; different component validity domain from rectifier** | **R; standalone machine-readable temperature/power files NOT verified**. Connector temperature ≠ rectifier temperature; use plots/report as qualitative/test-protocol evidence unless raw measurements acquired. |
| D09 | **Caltech ACN-Data** — [official dataset and API](https://ev.caltech.edu/dataset) | Per charging session: connection/disconnect/doneCharging times, delivered kWh, station/site, measured current series, pilot signal series, sometimes user requested kWh and departure | **SO3 service-target/proxy definition, delivered-energy and deadline feasibility** | **R; API access and selected raw-session QA pending**. User-requested energy/departure is self-reported, not independently verified trip failure. Historical web-interface timezone issue before 2019-10-10. |
| D10 | **KU Leuven BEV energy dynamics v2** — [RDR DOI](https://doi.org/10.48804/8KPDTW) | 1-s EV/charger/battery/auxiliary energy observations for charging, driving and parking; original public ZIP 154.8 MB | **SO1/2 energy-state / component loss and service modelling** | **R; latest original rows not re-audited here**. Verify battery versus EVSE temperature identity; do not assert internal EVSE thermals without schema. |
| D11 | **Farasis battery-cell experiments** — [Original archive](https://doi.org/10.5281/zenodo.17654407); [HF processed index](https://huggingface.co/datasets/Battery-Life/BatteryLife_Farasis) | 123 pouch cells; upstream original Parquet with ~1-s current, voltage, temperature; HF repository comprises 123 large pickle objects (~120.8 GB) | **SO2 battery-cell electrothermal component evidence** | **R/F repository inventory; original waveform QA OPEN**. Cell is not pack/EVSE; avoid deserializing untrusted pickle files; use upstream original Parquet with documented units/protocols. |
| D12 | **Li et al. 2026 vehicle charging under power-quality disturbances** — [Scientific Data](https://doi.org/10.1038/s41597-026-06768-5); [OSF original files](https://doi.org/10.17605/OSF.IO/94GKC) | 250 controlled experiments, approx. 21,539 s; voltage/current, CAN-FD battery SOC/current/voltage/temperature/charging power-limit/charging state | **SO1/2 controlled electrical P→T_e / battery response; constrained mechanism checks** | **R; open OSF original CSV numerics untested here**. Not direct transformer thermals, not an extreme-heat EVSE derating campaign. |

### B. Supporting environmental, regional load and forecasting datasets

| ID | Candidate and source | What it contributes | Status / exclusions |
|---|---|---|---|
| D13 | **Liander 2024** — [OpenSTEF HF](https://huggingface.co/datasets/OpenSTEF/liander2024-energy-forecasting-benchmark) | 15-min signed transformer/feeder active power (W), weather measurements and time-versioned forecast availability; real time-variable boundary loading | **R/F; earlier numerical inspection of OS Apeldoorn documented 35,136 load rows, three missing and mostly negative signed power; corresponding weather file 35,229 rows**. Check sign convention, matched timestamp coverage and forecast leakage. **NOT** winding/oil thermal validation. |
| D14 | **ETT** — [original CSV source](https://github.com/zhouhaoyi/ETDataset); [HF TsFile mirror](https://huggingface.co/datasets/THULab/ETDataset-ett) | Oil-temperature forecasting benchmark; load-related features; ETTh1 17,420 hourly rows | **R; prior direct ETTh1 original CSV QA found continuous 17,420 timestamps, no missing OT and 154 negative OT values**. Benchmark only; insufficient ambient/loss/cooling measurements for identified equipment-specific thermal physics. Hourly/15-min same-region files are not independent experimental sites. |
| D15 | **GridCharge** — [HF original connector files](https://huggingface.co/datasets/djordjebatic/GridCharge) | Charging occupancy/session timing and reconstructed energy; carbon mix metadata | **R; earlier raw connector 50376_2.csv QA: 1,294 30-min rows, 63 occupied, 25 occupied with zero reconstructed energy; fuel mix shares sum ~1**. No EVSE thermal cause or measured missed trips. Dataset viewer heterogeneous schema; do not load as a single uniform CSV. |
| D16 | **PJM demand+weather** — [HF Parquet](https://huggingface.co/datasets/Arimancy/pjm-demand-weather) | Regional hourly energy demand (MWh) and weather stress context; flags for imputation and preliminary weather | **R; earlier full 99,232-row Parquet QA: 279 imputed demand flags, 141 missing weather flags**. Regional energy ≠ local transformer W; optional scenario context only. |

### C. Modeling assets, explicitly *not observational datasets*

| ID | Resource | Appropriate use | Not established |
|---|---|---|---|
| M01 | [Stanford EV-EcoSim](https://s3l.stanford.edu/ev-ecosim) | Existing baseline co-simulator of EV charging, distribution grid, transformers, batteries, PV and controls; examine source equations/tests before selecting any extension | Public software ≠ independently calibrated full extreme-heat field site |
| M02 | [NLR/NREL EVI-Pro, EVI-X](https://www.nlr.gov/transportation/evi-x) | Model mobility charging requirements, demand scenarios; harmonize service assumptions | Modeled needs ≠ observed missed trips |
| M03 | [IEEE C57.91-2025](https://standards.ieee.org/ieee/C57.91/7163/) | Applicable oil-immersed transformer loading/thermal assessment guidance, subject to equipment applicability and actual standard access | Does not prescribe EVSE thermal derating or constitute field data |

## 3. Physical interdependency matrix — test direction separately

| Mechanism | Required observation | Best independent sources | Current proof boundary |
|---|---|---|---|
| **T_e→P, charging-caused transformer heating** | Actual EVSE input/current load mapped to exact transformer, transformer losses plus ambient and thermal state; aligned time and controls | D01 (transformer physics) + D02 (EV-point/grid electrical) + D04/D05 (charging load) | **Mechanistic composite possible; connected-site measured thermal causal path NOT VERIFIED** |
| **P→T_e, transformer thermal restriction on charging** | Measured/estimated transformer thermal state and equipment-valid temperature-dependent available capacity, actual charger controller limit, input/output power, delivered energy | D01 + D04 + D09 + M01/M03 | **Composite simulation only; no measured same-site heat-conditioned P→T_e restriction** |
| **T_e equipment thermal derating** | Ambient, **internal rectifier or explicit cable/connector sensor**, cooling status, allowed and delivered charge power, vehicle demand, time | D07 author raw target; D08 distinct connector mechanism; D10/D11 supporting battery | **Published mechanism, no qualifying downloaded raw D07 logs** |
| **Bidirectional thermal feedback** | Both prior directions demonstrated through same mapped electrical interface and timebase, and the heat dependence tested | Need connected-site primary campaign or qualified joint logs | **OPEN**; cannot be established by merging timestamps from different sites |
| **SO3 mobility consequence** | Battery energy at deadline, documented physical vehicle/route requirement, actual trip or explicitly modeled trip demand | D09, D04, D10, M02 | **Measured energy service proxy feasible; actual trip failure NOT VERIFIED** |

## 4. Constructive portfolio integration without false site joins

**Chain C1 — measured component validation:** Use D01 to fit/hold out a **transformer-only** thermal model with sensor provenance. Independently use D07 (if data acquired) for EVSE derating, D11 for battery-cell behavior, D04/D05/D06 for charging power/controller dynamics. Do not pool equipment-specific coefficients or thermal limits across technologies without an explicit transfer study.

**Chain C2 — electrical interface tests:** Use D02 observational KIT campus voltage/power series and D03 controlled PHIL voltage perturbations to compare alternative electrical response hypotheses. These are different trials; do not attach PHIL control states to campus timestamps. Existing D02 matched-controls report is descriptive only; no field causal identification is claimed.

**Chain C3 — service consequences:** Use D09 user targets and D04 charging request/setpoint/energy traces to define clearly labeled service proxies. Define required energy at departure as a **thesis-derived service metric**, not published measured mobility loss unless actual trip performance is independently observed.

**Chain C4 — synthetic coupled scenario, conditional:** Feed separately calibrated components into M01 or a reproducibly checked custom coupling. Inputs may use D13 ambient/load time histories or a declared heatwave scenario; the original climates/installations differ. Represent model input via a reproducible scenario manifest, *not a fabricated same-site dataset*. Propagate parameter uncertainty and separate model-form from data uncertainty.

**Chain C5 — falsification models (EGMIV):**
- M0: independent components / no cross-interface influence.
- M1: static or algebraic interface constraints with no thermal memory.
- M2: dynamic electrothermal coupling with valid thermal inertia, heat-conditioned capability and vehicle service states.
Check nested limits (coupling→0, thermal timescale→0 where mathematically well-posed), mass/energy/power balance, sign conventions, clock offsets, observation operators, and out-of-sample component predictions. A lower forecast error is not itself validation of thermally causal coupling.

## 5. Noncompensatory acquisition and validation gates

G0 **Original source**: DOI, primary URL, original filenames, version, license and hash.  
G1 **Reality**: equipment model/rating/condition, ambient exposure, sensor position, status of measured versus calculated channels.  
G2 **Chronology**: clocks, UTC/time zones, resolution, missingness, timestamp monotonicity, acquisition availability and leakage.  
G3 **Interface**: exact electrical parent-child map, currents/power conventions, EVSE input versus output, SOC/energy dynamics, control/status.  
G4 **Thermal mechanism**: observed local thermal state *and* admissible heat-conditioned capability/control mechanism; exclude common-cause heat alone.  
G5 **Identifiability**: parameters identifiable under available excitation, uncertainty and confounding; no arbitrary fixed threshold.  
G6 **VVUQ**: physical unit checks, numerical verification, chronological/site/device holdout where possible, sensitivity, uncertainty and competing-model falsification.  
G7 **Service evidence**: measured energy/availability versus requested mobility outcome clearly distinguished; recovery only if actually modeled/observed.

**No compensatory scoring**: a million records cannot substitute for an unverified sensor, missing topology, absent internal temperature, or unobservable mobility need.

## 6. Work queue — priority-ranked by scientific information gain

1. **D01 SINTEF**: inspect/download measured and calculated CSVs separately; inspect headers, timestamp/clock, units, gaps, sensors, range, thermal excitation, independence of validation window. Preserve original hashes. No claim of calibrated transformer parameters until fitted, challenged and validated.
2. **D07 Qatar**: request original synchronized time/ambient/rectifier temperature, offered/delivered power, input power, cooling/derating event/status, battery SOC, metadata and publication-permitted anonymization. Status **DATA NOT IN HAND**.
3. **D04 EPFL + D09 Caltech**: perform original session QA, verify measured/reconstructed fields and control-versus-demand separation; derive only source-qualified service proxies.
4. **D02 KIT**: do not repeat verified Mac MD5/129.6M-row time-grid audit. Use existing per-event M1–M3 results, seek feeder parent map and charger logs, then test electrical response with independent D03 trials. No thermal field claim.
5. **D05 TU Dortmund + D06 KIT vehicle profiles**: small reproducible sample, document which trial contains requested status, setpoint, SOC, ambient sensor; do not assume homogeneity across EVs.
6. **D11 Farasis**: request or access small upstream Parquet subset; inspect measured vs inferred SOC and raw temperature channels; avoid loading untrusted .pkl objects.
7. **D12 Li/OSF**: inspect published CSV and code for controlled electrical boundary tests, distinguish battery thermal telemetry from EVSE internal sensors.
8. **D13 Liander**: signed-power QA plus timestamp-and-availability-safe weather join; only as boundary-condition scenarios, NOT transformer temperature validation.
9. **D08 DOE**: request raw hot-condition connector/cable power/temperature trials and instrument metadata; distinguish physically from D07 rectifier mechanism.
10. D14–D16: use only for forecast benchmarks, occupancy scenarios, or regional-demand sensitivity when a frozen SO1–SO3 need actually arises.

## 7. What is established vs open

**Established at source/working level:** There exist public primary files for measured SINTEF transformer temperatures; KIT multivoltage electrical response (previous user-local verification); EPFL and several controlled charging trials; publicly described ACN service-request and charging observations; time-conditioned transformer inputs from Liander; and published Qatar measured charger derating evidence.

**Not established:** A connected same-site dataset measuring the full chain EVSE demand → transformer thermal state → equipment-valid power restriction → EVSE thermal/electrical state → achieved mobility service, with actual extreme-heat forcing and usable causal/temporal metadata. No retrieved work is allowed to fill this gap through an invented join.

**Important novelty caution:** Existing Stanford EV-EcoSim already co-simulates chargers, transformers, storage and control. The novelty claim must be established by closest-literature audit and empirical tests; merely placing separately known components into a simulation is **not** new by itself.

## 8. Machine-readable register and traceability

See [DATASET_CANDIDATE_REGISTER_V1.csv](DATASET_CANDIDATE_REGISTER_V1.csv) for source URLs, roles, access/QA depth, missing variables and next verification action. Every eventual source dataset entering a model must also have an immutable raw file hash and derived-data transformation log; neither is fabricated here.

### Key supporting sources (primary evidence; also linked inline)

- Bærug, H., Madshaven, I., & Espedal, C. (2025). Supporting data for thermomechanical modelling of clamping force in power transformer in operation. Zenodo. https://doi.org/10.5281/zenodo.17223516
- Moster, P., et al. (2026). 100 ms-resolution electrical measurement dataset of an OLTC-induced voltage fluctuation anomaly. Zenodo. https://doi.org/10.5281/zenodo.22826984
- Beichter, S., et al. (2026). High-frequency 20 ms PHIL measurements of electric vehicle charging control under voltage step perturbations. Zenodo. https://doi.org/10.5281/zenodo.22965111
- Krama, A., Kamal, N., Sezer, N., & Bayhan, S. (2026). Impact of extreme climatic conditions on fast EV charger performance: Field experimental insights from Qatar. Energy Conversion and Management: X, 31, 101960. https://doi.org/10.1016/j.ecmx.2026.101960
- Li, H., Zhang, Y., Yang, S., & Liu, X. (2026). High-resolution dataset of electric vehicle charging responses under varied power quality disturbances. Scientific Data, 13, 403. https://doi.org/10.1038/s41597-026-06768-5
- EPFL-DESL. Level 3 EV charging dataset and primary README. https://github.com/DESL-EPFL/Level-3-EV-charging-dataset
- California Institute of Technology. ACN-Data field descriptions and API. https://ev.caltech.edu/dataset
- OpenSTEF. Liander 2024 energy forecasting benchmark, dataset documentation. https://huggingface.co/datasets/OpenSTEF/liander2024-energy-forecasting-benchmark
- SINTEF/KIT previous actual local analysis provenance: data/field_candidates/2026-11-05/README.md and linked research logs in this repository.

**Final gate:** This is an evidence-qualified **dataset integration research plan**, not a validated SO1–SO3 empirical result, a validated new coupled physical law, or a freeze of final novelty/RQs/hypotheses.
