# Thesis research checkpoint — 3 November 2026

**Project:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Scope:** Physics-based mathematical engineering of thermal/electrical power–electrified-transport interactions under extreme heat, with resilience and service outcomes.  
**State:** WORKING SCIENTIFIC CHECKPOINT, NOT A FROZEN RESULT OR SUPERVISOR-ASSESSMENT.  
**Working branch:** \`user-data-qualification-2026-11-03\`; **main has not been changed**.  
**Purpose:** Preserve complete continuity for the next session without repeating source acquisition or overstating validation.

## A. Thesis objectives: planning progress (not an objective measurement)

The following **subjective milestone estimates** were discussed on 3 November 2026; they are useful for prioritization, **not verified fractions of the thesis accepted by a supervisor**.

| Original core thesis objective | Provisional completed | Provisional remaining | Evidence supporting progress | Critical missing result |
|---|---:|---:|---|---|
| **SO1: Physical directional interdependencies** — identify and qualify transformer–EVSE mechanisms and observed states/interfaces | **35%** | **65%** | Architecture and candidate interface hypotheses; field-origin transformer thermals and P/Q loading; laboratory charging and PQ behavior; evidence/provenance register | Verified site-specific Power↔EVSE feeder connection, temperature-dependent interface restrictions and extreme-heat evidence |
| **SO2: Coupled physics-based state–time dynamics** — derive, parameterize and validate dynamic equations and uncertainty | **20%** | **80%** | SINTEF one-step/6-h/24-h conditional transformer hindcasts; component model coefficient fit; bootstrap and local sensitivity; laboratory EV electrical/pack observations | Independently validated EVSE thermal mechanisms, full coupled state equation, parameter identifiability and external thermal validation; coupled-vs-uncoupled VVUQ |
| **SO3: Criticality, viability, resilience and service consequences** — quantify service impacts and useful interventions | **5%** | **95%** | Mathematical viable-set/control formulation; component-level load/charge measurements | Quantified critical transition times, validated service thresholds, curtailment/recovery paths, matched controls, service trade-offs and connected physical evidence |
| **Equal-weight illustrative overall** | **20%** | **80%** | Simple mean of 35%, 20%, 5% | **Not a demonstrated scientific completion percentage** |

**Never conflate:** (i) 9 of 11 supporting questions having some analysis ≈82% *coverage*, with (ii) 20% provisional *core-thesis evidence progress*. Several supporting questions are provisional and do not validate any Power↔EVSE coupled thermal installation.

## B. Supporting RQ1–RQ11 status at this checkpoint

| RQ | Scientific question | Status | Most defensible finding / limit |
|---|---|---|---|
| **RQ1** | Relationship of transformer thermal states to ambient and electrical loading | **Measured descriptive result** | SINTEF 8,592 hourly samples, ambient/top-oil \(r≈0.9658\); raw top-oil/squared-current \(r≈−0.8007\) is **confounded**, not a cooling law |
| **RQ2** | Physics-constrained transformer temperature prediction | **Provisional same-site test** | Holdout 1-h RMSE 0.2147°C vs persistence 0.2480°C; model MAE 0.1469°C **worse** than persistence 0.1409°C; 6/24-h are conditional hindcasts with **observed future forcing** |
| **RQ3** | Variation of transformer station P/Q | **Measured descriptive result** | Slovenia 34,932×12=419,184 paired station-times; 6.392% signed P negative; original header has **unresolved units/sign** and nameplate companion not qualified |
| **RQ4** | Evolution of EV charging power, voltage/current, SOC and battery temperature | **Laboratory component result, provisional** | KU Leuven 40,873 AC row records; example SOC 39→90.3% with pack max temp 30.25→28.75°C; three AC files include clock reversal problems |
| **RQ5** | Charging electrical input/output differences | **Provisional conversion-boundary result** | Two DC tests median P_DC/P_AC 0.92635, 0.92691; respective power differences 3.589/3.549 kW; these are **not directly measured heat rejection**; EPFL energy reconciliation open |
| **RQ6** | EV charging contribution to net electricity demand/predictability | **NOT quantitatively completed** | OPSD earlier audit mentions 116,355 15-min intervals; need original matched site-level rows and leakage-safe chronological forecasting benchmarks |
| **RQ7** | Charging response to power-quality disturbances | **Exploratory laboratory result** | Original OSF source recovered, 250 main + 63 supplementary CSVs, 18 supplementary empty; eligible interruption experiments median Δ absolute battery current −6.1 A (n=19) and sags −3.5 A (n=20); no causal inference/sham test |
| **RQ8** | Identifiability of physics parameters | **Effective-coefficient result only** | SINTEF fitted three-coefficient model is rank 3; statistical coefficients identifiable under this structure; heat capacity, copper/core losses, cooling and battery physical parameters **not uniquely identified** |
| **RQ9** | Sensitivity and uncertainty | **Local model sensitivity and exploratory block bootstrap** | Analytic 1-h ambient derivative 0.0807461; site-specific normalized sensitivities; not external or physical parameter uncertainty |
| **RQ10** | Domains of validity/transferability | **Same-transformer range test** | Oct–Dec holdout inside separate training ranges; model beats persistence in monthly 1-h RMSE; **no independent equipment/site validation**, ambient observed max 25.97°C |
| **RQ11** | Service viability under thermal/electrical constraints | **Conditional formulation only** | Differential constraint and unmet-charge optimization possible; numerical coupled-service and extreme-heat field effects not yet established |

**Full scientific detail, sample definitions, methods, caveats:** [Report 1 — eleven questions](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md).

## C. Files and provenance — already acquired

### Original measurements stored in Google Drive (not duplicated as GitHub raw archives)

- [Data folder](https://drive.google.com/drive/folders/10vfbC7cNM4IjEIsKaM8d-V7U8HaCanb2).
- [SINTEF 2024 original measured sensors](https://drive.google.com/file/d/1sOEtx-Nlr00n_pLqTdWb4BZI6O35m8Nu/view) — 8,592 real transformer observations, original publisher MD5 verified; **source-sensor CSV is authoritative**, not the locale-coerced unified Google Sheet.
- [Slovenia 2025 measured P](https://drive.google.com/file/d/1hZ7pCydBAkfnLf4RU2lTu3LozNvuQ4tO/view) and [measured Q](https://drive.google.com/file/d/1SQ0ONhiCXK3_Ax--q9j0lUQV7IDACL5I/view) — 34,932 15-minute UTC stamps each and 12 matching station IDs.
- [KU Leuven C5PT0R source experiment archive](https://drive.google.com/file/d/1zYktMEjoqXu-ZheGW8HGATwx23_lAcjH/view) — lab AC/DC charging; original file provenance documented.
- [OSF 94GKC original power-quality laboratory archive](https://drive.google.com/file/d/1Sjdg5TaGWXybjO_8DOlnkzIeSHpVhR4x/view); 313 experiment CSV file entries including 18 empty supplemental CSVs.
- [Master evidence Google Sheet](https://docs.google.com/spreadsheets/d/1zsiI8TPJeI2jKiZqlGj1okBrD6kuBVpw7xHzOxJcV6A/edit) and [Field Candidates Sheet](https://docs.google.com/spreadsheets/d/1FgsfDBsCP43L6GyRbJ8v0NmUxseL4aJPeRnHBIHJqzk/edit).

### GitHub branch deliverables

- [Report 1 RQ1–RQ11](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md) — source-grounded answers and limits.
- [Original CSV provenance audit](./SLOVENIA_STREAM_SINTEF_RAW_AUDIT_2026-11-03.md) and [master dataset inventory](./MASTER_DATA_INVENTORY_2026-11-03.csv).
- [RQ1–RQ5 compact Python](./REPORT_01_REPRODUCE.py), [RQ7–RQ10 extended Python](./REPORT_01_EXTENDED_RQ7_RQ10.py).
- [RQ7–RQ11 results JSON](./REPORT_01_EXTENSION_RQ7_RQ11_RESULTS.json), [RQ7 grouped CSV](./REPORT_01_RQ7_OSF_BY_CATEGORY.csv), [RQ8 bootstrap CSV](./REPORT_01_RQ8_BLOCK_BOOTSTRAP.csv), and [RQ10 monthly holdout CSV](./REPORT_01_RQ10_MONTHLY_HOLDOUT.csv).
- **Known reporting gap at this checkpoint:** the Report 1 narrative links a per-experiment RQ7 QA CSV but \`REPORT_01_RQ7_OSF_BY_EXPERIMENT.csv\` is *not present in the current GitHub branch*. It exists inside the validated Report 1 ZIP package, which was saved in the user's persistent Library at `/Thesis Research Archive/Report_01_RQ1_RQ11_Research_Analysis_2026-11-03.zip` (SHA-256 `ca763a518b6cd668a90bd4c9b84f3acf45269a427fd76d609f4c5b09313da6c7`; ZIP CRC check PASS; **20 archive members**). It is preserved across sessions but the per-experiment CSV has not yet been individually committed to GitHub.
- **Reproduction gate:** the extended GitHub Python script has not been independently shown to byte-for-byte regenerate all files in the full local analysis package. Treat as reproducibility implementation pending independent run comparison, not as certified reproducibility.

## D. Physics/transferability rule to retain

We aim to transfer **validated governing physics and model structure**, not fitted parameters from an unrelated installation. Example:
\[
C_{\mathrm{th}}\dot{T}=P_{\mathrm{loss}}(I,T;\theta)-Q_{\mathrm{cool}}(T,T_a;\theta).
\]

This physical conservation statement is general. Specific model reductions, constitutive equations, boundaries, operating regimes and parameters require their own evidence and verification. Real original data prove **observed component conditions**, not universal portability, causality, severe-heat validation or coupling of Norwegian/Slovenian/Belgian installations. **Never join separate datasets into a fictitious synchronized field site.**

## E. Next-session task queue — in scientific priority order

1. **Archive reconciliation:** **full local RQ1–RQ11 package now preserved in persistent personal Library** (original ZIP, CRC valid). If full version-controlled replication is needed, commit the RQ7 per-experiment QA CSV separately to GitHub; confirm script/metric reproduction, check GitHub links and source hashes, and resolve the 313 vs 295 nonempty file and prior row-count discrepancy.
2. **RQ6 completion:** retrieve authentic original OPSD paired site-load/EV charging data and conduct no-leakage matched forecasts; record metering boundary, imputation and uncertainty.
3. **Transformer equipment parameters:** obtain and checksum the [STREAM transformer nameplate/impedance/loss file](https://doi.org/10.5281/zenodo.20927801); verify all 12 TR-ID joins and kW/kvar/sign conventions before computing rated utilization or thermal overload.
4. **SO1 physical-interface evidence:** prove or explicitly bound P→EVSE grid supply, EVSE→transformer demand, thermal restriction/derating, and EVSE battery/cooling paths; prioritize same-site instrumented extreme-heat evidence.
5. **SO2 mathematical physics:** derive minimum-sufficient coupled state-space/ODE representation consistent with source sensors and conservation; constrain parameter identifiability; compare uncoupled/static/dynamic coupling with matched inputs and controls; complete VVUQ and external transfer tests.
6. **SO3 viability and resilience:** specify service thresholds, criticality, delay/recovery and uncertainty; conduct conditional control experiments and clearly separate them from verified field outcomes.
7. **Writing/traceability:** update report and project status for every completed scientific gate; preserve original measured bytes, explicit source/units/assumptions, and do not change frozen authorities without approval.

### Research handoff

**Next working starting point:** [Report 1](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md) + [This checkpoint](./THESIS_RESEARCH_CHECKPOINT_2026-11-03.md) + [master inventory](./MASTER_DATA_INVENTORY_2026-11-03.csv). Begin at task **E.1**, then E.2. Use review branch; do not imply \`main\` contains these outputs until a deliberate merge is verified.
