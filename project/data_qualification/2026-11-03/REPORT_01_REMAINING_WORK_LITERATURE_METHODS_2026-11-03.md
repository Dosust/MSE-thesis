# Report 1 companion — Advanced literature-method audit and systematic research protocol

**Effective research date:** 2026-11-03  
**Thesis (canonical):** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Frozen objectives:** SO1 identify and qualify thermal mechanisms; SO2 physics-based state-time model under extreme heat; SO3 critical transition time, propagation delay, electricity/mobility service consequences.  
**Status:** Targeted, source-audited **methodological evidence map and protocol**, **NOT a completed formal systematic review**. Does not supersede canonical frozen scope or claim that absent connected field data have been acquired. Integrates with [Report 1 RQ1–RQ11](./REPORT_01_EMPIRICAL_MATHEMATICAL_RQ1_RQ11_2026-11-03.md).

## 0. Critical scientific finding

The existing RQ1–RQ5 outcomes describe separate observed components (SINTEF, STREAM Slovenia, KU Leuven). New OSF RQ7 results are preliminary *within-test descriptive battery-terminal power responses* rather than causal or thermal effects. RQ8–RQ10 transformer investigations expose numerical but not physical identifiability, sensitivities but not predictive uncertainty, and within-site but not external validity. RQ6 lacks a freshly executed leakage-free forecasting comparison. RQ11 cannot be claimed as a measured coupled thermal/service result.

**No paper in the screened subset establishes that our independently recorded SINTEF, KU Leuven, Slovenian, EPFL, OSF, OPSD or KIT assets form one observed transformer–feeder–EVSE heatwave installation.** Generalizing from such a constructed combination must be labeled conditional/model-only.

## 1. Evidence-based methods from closely related papers

### A. Transformer heat equations, measurements and parameter identification

**T1 — Experimental study of dynamic thermal behaviour of an 11 kV distribution transformer** (2017). https://doi.org/10.1049/oap-cired.2017.1102.
- Verified publisher methods: 200 kVA 11/0.433 kV ONAN transformer; 16 internal fibre optic temperature sensors; multiple 0.7/1.0/1.25 pu heat-rise tests for parameter extraction; an additional transient up to 1.8 pu for 2 h tests the IEC thermal model.
- Adopt: discriminate parameter-estimation experiments from genuinely separate validation transients; evaluate oil AND hot-spot temperature responses; thermal parameters depend on actual sensor observability.
- Limit: lab test of one transformer, not an observed EVSE or extreme-heat coupled network; not a field transfer certificate.

**T2 — Dynamic thermal modeling of distribution transformers** (2005). https://doi.org/10.1109/TPWRD.2005.848675.
- Verified abstract: experimentally tests a 2500 kVA ONAN distribution transformer at varying currents with thermocouple responses and comparisons to IEEE loading-guide equations.
- Adopt: require winding-construction/cooling-mode qualification and external benchmark to challenge simplified top-oil/hot-spot models.
- Basis: abstract; full measurement files not inspected.

**T3 — Dynamic thermal model of liquid-immersed shell-type transformers** (2022). https://www.sciencedirect.com/science/article/pii/S0142061522003660.
- Verified abstract and section excerpts: IEC baseline upgraded with temperature-dependent losses and ambient/top-oil corrections; parameter estimation against fibre-optic and field operating temperature records of a 100 MVA ODAF transformer; one-year testing.
- Adopt: compare conventional IEC formulation with temperature-dependent loss and cooling variants, and report high-temperature signed bias rather than RMSE alone.
- Limit: shell-type ODAF differs from SINTEF ONAN and a future small distribution transformer; full experimental data availability unverified.

**T4 — Finite-time parameter estimation for online monitoring of transformer: a system identification perspective** (2023). https://doi.org/10.1016/j.ijepes.2022.108639.
- Verified publisher abstract/highlights: treats persistence of excitation, data richness and uncertainties in transformer top-oil temperature identification; compares estimation strategies.
- Adopt: before trusting parameter estimates, inspect regressor rank, excitation regime, season stratification, residual structure and whether different parameters produce indistinguishable predictions.
- Limit: abstract/overview screening; exact methods and conditions require full-text replication audit.

**T5 — Structural and practical identifiability by profile likelihood** (Raue et al., 2009). https://doi.org/10.1093/bioinformatics/btp358.
- Verified full accessible article/abstract. Profile likelihood separates structural and practical non-identifiability that local covariance estimates can miss.
- Adopt: constrained parameter profiles, bounded/unbounded likelihood intervals and parameter-correlation surfaces; distinguish numerical estimability of a,b,c from physical identifiability of thermal capacitance, heat loss and convection.
- Method paper is cross-domain: its theory transfers, not empirical thermal parameter values.

**T6 — A neural surrogate for practical identifiability and sensor placement in distributed battery thermal models** (2026). https://doi.org/10.1016/j.egyai.2026.100937.
- Verified open full-text. Tests profile likelihood against Fisher-matrix impressions, multi-condition inputs, sensor placement and synthetic-reference/independent numerical implementations. Reproducible Zenodo bundle: https://doi.org/10.5281/zenodo.23335953.
- Adopt: test what is actually observable from vehicle BMS temperatures and what remains unidentifiable; experiment conditions, not just sensor count, determine parameter recovery. Check inverse-crime safeguards when relying on simulated observations.
- **Critical limit:** synthetic benchmark results, not proof of physical EVSE internal thermal sensing or measured battery cross-site transfer.

### B. EVSE actual extreme-heat physics and coupled charging constraints

**E1 — Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar** (Krama et al., 2026). https://doi.org/10.1016/j.ecmx.2026.101960.
- Verified open full article: 50 kW CCS2 charger; actual ambient, rectifier/internal component temperature, AC-input/DC-output, input-current THD, offered/delivered DC charging power and vehicle SOC, under seasonal ambient roughly 15–55°C. Internal temperature monitoring sensors are specified ±1°C with 5-minute sampling; measurement clocks aligned to less than one sampling interval. Charger thermal derating begins around a rectifier temperature of 55°C in that *equipment-specific study*; data available **on request only**.
- Adopt: a charger-only mechanistic evidence template that explicitly separates **offered charger power** from **vehicle accepted power**, grid AC from charger DC boundaries, internal thermal and external ambient states, and temperature-dependent derating. Inspect coarseness of 5-min thermal sampling before inferring subminute transition times. Reproduce cross-session/temporal holdout only if actual original records are received.
- Limits: only the studied charging hardware/climate, and no source-confirmed same-site instrumented transformer in the described setup. 55°C is **not a universal EVSE temperature limit**.

**E2 — Analysis and mitigation of the impact of EV charging on service disruption of distribution transformers** (Visakh & Selvan, 2023). https://doi.org/10.1016/j.segan.2023.101096.
- Verified abstract/introduction excerpts: includes harmonic-related transformer heating and electrical/thermal restrictions, and examines scheduling EV charging to mitigate limits and meet user energy needs.
- Adopt: distinguish transformer top-oil, hot-spot, electrical protection thresholds and actual session energy obligations in optional coupled scenarios. Compare controlled and uncontrolled trajectories *as a model-only experiment* unless actual co-located data exist.
- Limit: study's transformer–EV relationship is modelling/simulation-oriented; do not treat it as a field-measured EVSE thermal coupling validation. Full paywalled methods not independently audited.

**E3 — Hosting capacity of distribution networks for residential EV charging with static and dynamic thermal ratings** (Zakaria et al., 2024). https://doi.org/10.1049/gtd2.13025.
- Verified publisher abstract: uses **actual UK charging data as inputs** with stochastic charging profiles, residential demand and local weather, then evaluates static/dynamic transformer and overhead-line thermal ratings on an IEEE 33-bus benchmark.
- Adopt: use measured inputs as **boundary conditions**, clearly label modeled network components, compare thermal constraints with uncontrolled vs conditional charging service.
- Limit: a modeled test network does not become a field-validated transformer–EVSE system merely because some inputs came from real chargers.

### C. RQ6 forecasting and RQ7 controlled response evaluation

**F1 — Leakage-aware benchmarking of temporal data preparation for hourly energy forecasting** (2026). https://doi.org/10.1016/j.ecmx.2026.101791.
- Verified open publisher methods: rolling-origin evaluation, chronological train/validation/test, train-only scaling, identical model and time splits across comparator branches, persistence/seasonal baselines, stress tests for missing blocks and spikes.
- Adopt for OPSD: past-only EV and grid features; identical test timestamps for baselines; variation by horizon; disclosure of interpolated observations, correct 15-minute kWh→kW transformation, and uncertainty for serial dependence.
- Limit: its case studies are not the same OPSD houses, and reported predictive improvements are not transferable to our dataset.

**F2 — Data leakage from full-series signal decomposition inflates accuracy** (2026). https://doi.org/10.1155/er/4433079.
- Verified open publisher paper: full-series pre-split decompositions can leak future data; splitting into train/test and separately decomposing the test block may still leak within the test segment.
- Adopt a strict **prediction-origin information set**. No future observed EV current, exogenous weather, test-block interpolation or targets at prediction time unless known in deployment.
- Limit: illustrates forecasting validity; not thermal physics.

**F3 — OSF: High-resolution Dataset of EV Charging Responses Under Varied Power Quality Disturbances** (Li et al., 2026). https://doi.org/10.1038/s41597-026-06768-5; originals https://doi.org/10.17605/OSF.IO/94GKC.
- Verified full Methods and Technical Validation: 220 V, single-phase AC charging, controlled PQ setpoints using programmable supply and a full vehicle. Instruments report synchronization residual below 5 ms. Data acquisition includes multiple measurement channels; publisher documents missing CAN frames repaired with adjacent-value interpolation. Event starts and durations are encoded in filenames, typically at t=20 s. Expanded voltage sag tests include alternate vehicles/chargers/initial SOC.
- Adopt: compare measured *grid disturbance waveform* onset/size, battery/charger electrical response and recovery with consistent units/clock. Use matched normal or repeated conditions, cluster/weight by experiment not millions of serial samples, and treat interpolation separately. Extended vehicle/EVSE groups allow **laboratory** hardware transfer checks.
- Our Report 1 61-experiment median change is a **preliminary battery-side power association**; not a complete OSF disturbance causal effect, EVSE thermal dynamics or connected transformer service effect.

**F4 — OPSD Household Data 2020-04-15** (primary data source, not a journal methods paper). https://data.open-power-system-data.org/household_data/2020-04-15/.
- Publisher explicitly describes cumulative meter energy, 1-min measurements and interpolation/fill to regular time grids, including 15-min series, and 11 German household/site sources.
- Adopt: per-site meter hierarchy, net-grid vs EV submeter accounting, energy increments and fill flags; never use row counts as an answer to RQ6.

### D. Verification, measurement conventions, and systematic research method

**M1 — ASME V&V 20**. https://www.asme.org/codes-standards/find-codes-standards/standard-for-verification-and-validation-in-computational-fluid-dynamics-and-heat-transfer
- Adopt the *principle* of separate numerical solution verification, experimental comparisons and explicit uncertainties at specified validation states/conditions. Does **not** give blanket proof of validity at untested high-temperature extrapolations or other installations.

**M2 — IEEE C57.91-2025**, active guide. https://standards.ieee.org/ieee/C57.91/7163/
- Scope covers mineral-oil transformer loading, oil/winding temperature and ambient/cooling limitations. Adopt current accepted transformer thermal-limit/insulation interpretation **after** obtaining applicable specification. No proprietary numeric threshold is asserted without the standard's text and the equipment rating.

**M3 — IEEE 1459-2025**, active power quantity definition standard. https://standards.ieee.org/ieee/1459/7578/
- Defines appropriate measured quantities under sinusoidal/non-sinusoidal and balanced/unbalanced operation. Adopt actual meter boundary, units, signed P,Q, harmonics and three-phase definitions. Do not apply simplistic S=sqrt(P²+Q²) across unverified unbalanced/non-sinusoidal station measurements.

**M4 — PRISMA-S** (2021), https://doi.org/10.1186/s13643-020-01542-z; **PRISMA 2020** https://www.prisma-statement.org/prisma-2020; **PRISMA-P** https://doi.org/10.1186/2046-4053-4-1.
- Adopt complete database/engine, search date, exact queries, deduplication, record-flow reporting, dual-reviewer information and logged exclusions for a future *formal* systematic evidence synthesis. **This targeted review is not a PRISMA-compliant completed review:** comprehensive multiple database queries, full record export, dedup count, full-text inclusion count, independent dual screening and risk-of-bias assessment are outstanding.

## 2. Exact research execution protocol — stage gates and outputs

| Stage | Research tasks | Required deliverable | Gate to advance |
|---|---|---|---|
| **G0 Search & critical appraisal** | Freeze review questions/subquestions, protocol and search strategy; collect DOI, full-text access state, experiment type, sample size, instruments and data/code access; classify genuine field vs lab vs simulation vs theory | Search log + screened evidence matrix + explicit exclusions and conflicts | No article treated as new observations; retrieved counts auditable |
| **G1 Source qualification** | Verify source file hashes, clocks, units, model ID and sensing boundary; label original vs author-calculated vs derived vs synthetic; audit gaps, time reversals, season and device/session dependence | Per-source signal dictionary, hash manifest, data-quality exceptions | Only physically qualified data reach estimation |
| **G2 Physics / identifiability (RQ8)** | Derive IEC/IEEE-consistent top-oil and winding model variants, convert to discrete time carefully, check structural parameter observability, excitation and profile likelihood; inspect split-season drift | Equations/units, identified parameter combinations, profiles and nuisance-parameter report | No ambiguous lumped coefficients advertised as material physical constants |
| **G3 Numerical verification + comparisons (RQ2/RQ9)** | Verify solver convergence/time step and energy balance; compare persistence, ambient-only, IEC/IEEE physical baseline and suitably simple alternatives using SAME chronological evaluation windows | Benchmark metric table, residual plots, solver convergence, unit tests | Do not select model from final test set |
| **G4 UQ and external domain (RQ9/RQ10)** | Separate measurement, parameters, initial state, forcing, numerical and structural uncertainty; use autocorrelation-aware block/bootstrap or appropriate likelihood; test periods, hardware and extreme temperature ranges actually observed; assess forecast/extrapolation separately | Interval calibration by temperature/load, domain diagram, sensitivity ranking, explicit extrapolation flags | Held-out high-temperature/external-site evidence required before actual transfer claims |
| **G5 OPSD demand forecasting (RQ6)** | Original row acquisition, meter hierarchy, 15-min kWh interval interpretation; fit past-only persistence/seasonal baseline then past-EV augmented model; rolling-origin holdout and interpolation-free sensitivity | Site-separated identical-test MAE/RMSE, paired uncertainty and data-leakage audit | No causality statement from forecasting gain; no claim if raw rows absent |
| **G6 OSF disturbance analysis (RQ7)** | Reconcile lab protocol/event times against grid-side waveform, battery CAN signals, pre/during/recovery windows, repeated experiments and SOC/charger groups; report experiment-level uncertainty | Disturbance severity versus response/recovery, robust sensitivity excluding interpolated samples | No thermal claim from electrical-only response; do not pool serial rows as independent tests |
| **G7 EVSE thermal mechanism** | Obtain Qatar or comparable raw internal charger temperatures, ambient, AC/DC and offered/accepted power plus charger control/derating events; map 5-min vs electrical sampling/clock | Equipment-specific calibrated thermal restriction law and temporal measurement-resolution limitations | Without original EVSE internal thermal signal, do not claim measured EVSE thermal law |
| **G8 Connected system and service (RQ11 / SO3)** | Verify same physical transformer-feeder-EVSE location, mapped site IDs, linked meter boundaries, synchronized thermal/electric state, actual operating restrictions and service requirements/departures. Otherwise run transparent hypothetical scenarios only | Measured vs simulated inference table, critical times/delays, energy/service trajectories and uncertainty | **COUPLED FIELD CLAIM BLOCKED** until topology/thermal/control and service measurements verified |

## 3. Analysis questions and acceptance logic

### RQ6, exact forecasting estimand
Let `y[t+h]` be true grid import on one metered premise (define kWh-interval or average kW unambiguously). Compare baseline `f0(history of grid, calendar)` with augmented `f1(history of grid, history of EV, calendar)`, same timestamps and train-only fit. Effect is `ΔMAE=MAE(f0)-MAE(f1)`; must provide blocked uncertainty or appropriate paired dependence-aware testing. **It is not a causal EV-load impact estimate.**

### RQ7, exact disturbance-response estimand
For each independent lab experiment e with verified PQ onset/offset, define within-test pre-event/active/recovery response on same battery terminal or charger AC boundary; report relative/absolute change, interruption or recovery time, severity and hardware/SOC. Paired controls strengthen causal interpretation but do not convert AC PQ perturbation into high-ambient DC charger thermal evidence.

### RQ8 thermal identifiability
For source-specific state-space/ODE `dot x=f(x,u;theta)`, establish observation map `y=h(x,theta)+epsilon`. Numerical regression/full rank is only local estimability; profile likelihood and physically differentiated sensor/forcing tests are needed to determine which individual parameters or parameter groups can be identified. Do not infer separately C, R, copper loss and unmeasured cooling flow from a three-coefficient phenomenological fit.

### RQ9, separate deterministic sensitivity from UQ
A calculated +5°C ambient input experiment indicates **conditional derivative/sensitivity**, not prediction uncertainty or measured extreme-heat performance. UQ must propagate defensible noise/parameter/structural/forcing distributions or bounds, evaluate out-of-sample interval coverage and evaluate near operating thresholds.

### RQ10 external transfer
Define deployment target and applicability domain BEFORE attempting source-to-target comparison: equipment transformer type/cooling/rating, ambient/loading ranges, charger rated power/cooling, control, metering topology, clocks and relevant service. Report either `WITHIN-SITE VALIDATION`, `EXTERNAL SITE VALIDATION`, or `EXTRAPOLATION / UNTESTED`, never a generic assertion of transfer.

### RQ11 thermal viability
Use explicit `C_T\dot T_T=P_loss(I,T_T)-Q_cool(T_T,T_a)`, `C_E\dot T_E=Q_gen(P_AC,P_DC,z)-Q_cool,E(T_E,T_a,z)`, admissible operating modes, protective restriction logs and harmonized AC/DC power boundaries. Define unmet delivered energy at verified charging DC boundary and required departure window. Quantify *only* model-conditional quantities until field observations close the topology and temperature/service gaps.

## 4. Search process transparency (this cycle)

**Search date:** 2026-11-03. Targeted web-index search and publisher full-text access for key records; sources include Springer/CIRED, Elsevier, Wiley, Oxford, IEEE Standards, ASME, OSF and official OPSD. Example executed search concepts: (transformer thermal identification / hot-spot / measured validation); (distribution transformer + EV charging + heatwave + dynamic thermal ratings); (DC EVSE rectifier internal temperature + extreme heat + field measurement); (practical identifiability/profile likelihood + thermal model); (energy forecasting + rolling origin + temporal leakage); (power-quality imposed EV charging + repeated experiment); (systematic review PRISMA-S reporting). Sources selected purposively for **method-to-gap match**, not for a pooled effect meta-analysis. **An Elicit API research search was attempted but unavailable under the connected account; no Elicit corpus screening was performed.**

**Not yet done:** exhaustive Scopus/Web of Science/IEEE Xplore automated retrieval, database-specific full Boolean query export, deduplication log, PRISMA flow totals, two-reviewer independent full-text decisions, all full-text access for paid studies, formal quality/risk-of-bias scoring. For that reason, cite this as an **advanced targeted literature-method audit** rather than a completed systematic review.

**Next formal review protocol**: pre-register the precise research questions, searchable bibliographic sources, Boolean strings and inclusion criteria; export RIS/BibTeX with query execution time, dedup DOI/title, store a reason code for each title/abstract/full-text exclusion, assess source type (field-same-site, lab component, modelling with measured inputs, simulation-only, theory), apparatus/sensors/timebase/units/uncertainty/independent holdout, and publish an auditable PRISMA-S-compatible search supplement and PRISMA-style flow chart once counts genuinely exist.

## 5. Most important research decision

**Highest-priority missing evidence: a real physically connected transformer→feeder→EVSE installation with both transformer and EVSE internal temperature, AC/DC electrical states, controlled or observed thermal restriction and actual electricity/mobility requirements, time-aligned at resolutions sufficient to see transitions.**

The Qatar study uniquely adds measured DC charger rectifier/derating observations under extreme heat **at its charger**; the SINTEF study adds transformer physics **at a different site**. Without a third dataset linking these, an integrated model can be explored **as conditional engineering simulation only**, not represented as validated real coupled dynamics.

## References / integrity

All titles and DOIs above were checked against the publisher/official archive at least at landing-page or abstracts; fully open text was examined for the Qatar and OSF articles and for selected accessible methodology papers. Paywalled full studies were not represented as fully audited. Record-level extraction is in [the adjacent evidence matrix](./REPORT_01_LITERATURE_METHOD_EVIDENCE_MATRIX_2026-11-03.csv). No original raw dataset is added to GitHub, and this report does not change any frozen research-scientific authorities.
