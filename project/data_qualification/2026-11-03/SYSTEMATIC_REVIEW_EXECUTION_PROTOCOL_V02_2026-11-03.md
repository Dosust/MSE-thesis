# Systematic literature evidence map and focused mathematical-model review — executable protocol v0.2

**Created:** 2026-11-03. **Thesis:** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience under Extreme Heat.  
**Responds to:** Professor Pat Phelan's research feedback: rigorous review of prior work first; choose a physics-informed neural network / physics-informed ML only if relevant measured data are adequate, otherwise develop a pure-physics model.  
**Protocol state:** **PROPOSED, NOT FROZEN, SEARCHES NOT EXECUTED**. A preliminary targeted source scan exists; it is not a systematic review and cannot supply PRISMA denominator counts. Scope and queries must be locked and versioned *before* executing systematic database searches. Preserve amendments with dates.  
**Relationship to previous files:** [Targeted comparators v0.1](./TARGETED_LITERATURE_THERMAL_PT_SYSTEMATIC_PROTOCOL_V01.md); [literature-to-data physics crosswalk](./LITERATURE_TO_DATA_VALIDATION_CROSSWALK_V01.md); [RQ1–RQ11 findings](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md); [thesis checkpoint](./THESIS_RESEARCH_CHECKPOINT_2026-11-03.md).

## A. Review type and reporting standards

A single narrow PICO/meta-analysis cannot adequately cover thermal physics, real field mechanisms, experimental measurements, data-driven algorithms and network-service resilience. Implement a **two-tier structured evidence synthesis**:

- **Tier 1: systematic scoping/evidence map**, using JBI scoping-review conduct guidance and PRISMA-ScR reporting (20 essential + two optional items); include measured field, controlled lab, physics modeling, mathematical optimization, physics-informed ML, review and standards in disjoint *claim-specific* evidence strata. Purpose: map what has been studied, which variables are measured, and which interdependencies are genuinely validated.
- **Tier 2: focused critical systematic-style model synthesis** from the eligible primary papers: equation-by-equation comparisons, independent model-validation benchmarks, data requirements and residual research gaps. Use PRISMA 2020 reporting when making systematic-review claims; **PRISMA-S** for full reproducible database strategies (16 items); **PRISMA-P** to document prospective protocol methods (17 items). Report methodological adaptations to engineering literature transparently. Do not claim a clinical intervention risk-of-bias rubric applies directly to transformer models.

Verified methodology:
- PRISMA 2020: https://www.prisma-statement.org/prisma-2020 ; DOI 10.1186/s13643-021-01626-4.
- PRISMA-S: DOI 10.1186/s13643-020-01542-z (Rethlefsen et al., 2021).
- PRISMA-ScR: https://www.prisma-statement.org/scoping ; DOI 10.7326/M18-0850 (Tricco et al., 2018).
- JBI scoping-review conduct: https://doi.org/10.46658/JBIMES-24-09.
- PRISMA-P: DOI 10.1186/2046-4053-4-1 (Moher et al., 2015).

## B. Primary and secondary review questions

**Overarching:** What physical, mathematical, experimental and algorithmic evidence exists for the time-dependent environmental, electrical and thermal interdependencies of *connected* power and electrified-transportation infrastructure, and what is sufficiently validated to predict/maintain energy and mobility services under extreme heat?

- **SLR-Q1 (SO1):** Which thermal/electrical P→T_e and T_e→P pathways are described or *observed*, and do they include documented physical connectivity and intervention reason codes?
- **SLR-Q2 (SO2 physics):** Which energy-balance, circuit-thermal, diffusion-PDE, IEEE/IEC standard, battery/EVSE cooling and network state models are used? What are their state variables, constitutive relations, boundaries, time constants and parameter sources?
- **SLR-Q3 (SO2 data):** Which quantities are measured versus calculated/simulated? What sensors, equipment scales, times, extreme-heat exposure, data access, physical identifiability and within-/external-site validation exist?
- **SLR-Q4 (SO2 method):** When do physics ODE/PDE, reduced-order models, calibrated hybrid residual models, PINNs or other PIML improve matched independent prediction or inverse-parameter estimation? What comparisons and failure modes are reported?
- **SLR-Q5 (SO3):** Which measured or modeled performance outcomes (charging power, delivered/required energy, mobility deadlines, transformer limits, disruption propagation, recovery and service trade-offs) are distinguished from unobserved consequences?
- **SLR-Q6 (novelty):** Has *any* study already measured and validated thermal state-to-state coupled transformation of actual connected transformer and EVSE/transport service, including temporal directionality, parameter transfer or uncertainty? What closest studies could invalidate our novelty hypothesis?

Keep the **three core thesis objectives** (SO1 physical interface, SO2 state–time modeling, SO3 service resilience) separate from the previously reported supporting RQ1–RQ11 descriptive questions.

## C. Eligibility and search time horizon — specify before systematic execution

- **Population/contexts:** operating transformer/distribution network, EVSE fast/AC charging and associated vehicle battery/fleet; interdependent power-transport, EV smart charging, traffic/mobility services.
- **Phenomena:** heatwave/high ambient thermal dynamics, thermal ratings/inertia, rectifier/battery derating/cooling, observed/modeled bidirectional electrical coupling, physics-informed modeling, service response.
- **Evidence:** field observations and natural experiments, controlled laboratory studies, engineering standards, primary simulations with equations, reproducible algorithms, and syntheses (reviews tracked separately, *not* counted as primary experimental studies).
- **Records:** journal papers, relevant peer-reviewed conferences, technical reports, authoritative standards, data descriptors with instrument definitions, seminal mathematical methodology. Track preprints and theses as non-peer-reviewed strata.
- **Temporal plan:** default database query window 2000–2026-11-03; earlier foundational work recovered by citation chasing, documented separately. No arbitrary *heat-only* exclusion for important general governing equations.
- **Language plan:** search without language exclusion where possible; document language and translation restrictions rather than silently excluding.
- **Exclude/label:** untraceable claims and nontechnical publicity from primary evidence; studies with only an aggregate energy or traffic result may still be relevant as SO3 comparator, but are **not thermally validated**. Do not suppress non-supporting studies as irrelevant merely because they weaken a novelty claim.

## D. Search architecture (six independent blocks; do not AND all six)

To avoid missing thermal transformer physics and EVSE literature that do not explicitly mention 'resilience', run **separate searches** with discipline-appropriate indexing:

**A. Transformer thermal physics and charging load**
\`("power transformer" OR "distribution transformer") AND ("electric vehicle" OR "EV charging" OR EVSE OR "fast charging") AND (thermal OR temperature OR "hot spot" OR "top oil" OR "dynamic rating" OR aging)\`

**B. EVSE thermal derating under weather**
\`("fast charger" OR "DC charger" OR EVSE OR rectifier) AND ("ambient temperature" OR "high temperature" OR "extreme heat" OR "heatwave" OR cooling) AND (derating OR temperature OR "offered power" OR efficiency)\`

**C. Measured electrically connected transformer–charger site**
\`("charging station" OR "electric bus depot" OR EVSE) AND (transformer OR feeder OR substation) AND ("field measurement" OR monitoring OR experiment OR "metered")\`

**D. System-of-systems dynamics and resilience**
\`("power transportation" OR "power-transportation" OR "transportation power" OR "coupled electricity transportation") AND (resilience OR recovery OR service OR cascading OR dynamic OR thermal)\`

**E. Physics-informed thermals and inverse methods**
\`("physics-informed" OR PINN OR "neural operator" OR "hybrid physics") AND (transformer OR "EV battery" OR "battery thermal" OR "charger" OR "thermal management") AND (temperature OR "heat equation" OR "parameter identification")\`

**F. Standards and mathematical baselines**
\`("IEC 60076-7" OR "IEEE C57.91" OR "transformer loading guide" OR "dynamic thermal model" OR "battery thermal model") AND (validation OR measurement OR loss OR time OR cooling)\`

These are **conceptual master strings**, not copy-paste claims of database-valid syntax. Translate each to exact Scopus \`TITLE-ABS-KEY\`, Web of Science \`TS=\`, IEEE Xplore query builder and Engineering Village/Compendex before execution, recording exact syntax, field codes, date and filters. Run a **sensitivity check**: searches must retrieve known seed Bragone 2022; RACE 2025; Krama 2026; Li 2026; Cao 2026; Wen 2025 and relevant transformer standards (from their intended databases). Expand synonyms where seeds are not retrieved.

**Databases:** Scopus; Web of Science Core Collection; IEEE Xplore; Engineering Village/Compendex where available; ScienceDirect and Wiley publisher platforms for full-text followup; OpenAlex/Crossref for discovery, DOI resolution and citation chaining; institutional repositories and paper-specific datasets/standards. Use Google Scholar only as supplementary citation discovery with query, date and export limitations recorded, not the sole reproducible systematic source. Record database *plus host platform*, exact access date/time, total source hits, queries, all export files and inaccessible sources in [search log](./SYSTEMATIC_REVIEW_SEARCH_LOG_TEMPLATE_2026-11-03.csv).

**Backward/forward citation chasing:** RACE, Bragone, Krama, Li, Cao, Wen, Godina, PRISMA seed references; record which parent yielded each added citation. Search for follow-up RACE Part 2 and any post-2025 external field validations, but **do not infer absence from an indexed abstract**.

## E. Screening and complete, honest PRISMA accounting

1. Export raw metadata (RIS/BibTeX/CSV) from each database; record search date, exact query, platform and result counts. Never report demo search/widget counts as PRISMA-denominators.
2. Remove duplicates by DOI after DOI normalization; by normalized title/year/author where no DOI; retain all original provenance and paper/report/version IDs. Record duplicate count and reasons, don't mistakenly merge distinct reports on one project.
3. Apply predeclared **title/abstract eligibility** and note reason categories for exclusion. Do not infer a temperature measurement from phrases 'thermal stress' or 'real-world evaluation'.
4. Seek original full text for all eligible/uncertain studies; document sought/retrieved/not retrieved counts. Full-text screening exclusion requires **one primary recorded reason** (wrong domain, no mechanism/model/outcome, unavailable verification, duplicate published study, non-technical, other predeclared); retain all notes.
5. A second independent reviewer is preferred for screening and critical extractions. If the thesis has only one screener, document that explicitly, use a stratified verification subsample and adjudication record; **never fabricate inter-rater agreement or claim dual screening**.
6. Maintain audit trail in [screening log template](./SYSTEMATIC_REVIEW_SCREENING_TEMPLATE_2026-11-03.csv); freeze final counts and PRISMA/ScR flow *only after* an executed search/screen. Reviews are separate from primary studies; article-level and dataset-level duplicates must be identified.
7. Predeclare update date and rerun search close to supervisor review/defense to catch 2026 work.

## F. Claim-specific evidence classification

Classify individual **claims** (measured thermal, derived losses, network resilience), not merely whole papers. A single paper may have field electrical measurements but *modeled* heat and *simulated* service.

| Code | Meaning | Can prove |
|---|---|---|
| **F1** | Same-site physical topology and synchronized measured transformer + EVSE internal thermal, electrical controls, charging service, with supported causal transition tests | Strongest directly relevant integrated field evidence, with confounders checked |
| **F2** | Same-site field transformer + EVSE electrical/partial thermal observations but lacks a full synchronized and causal mechanism | Connected partial field interface only |
| **F3** | Genuine operational field component, transformer *or* charger *or* vehicle | Component behavior; cannot prove joint field coupling |
| **F4** | Controlled lab instrumented experiment | Component mechanism in tested setup, not routine field site |
| **F5** | Model calibrated or driven by field data and independently evaluated (specify which variables were actually measured) | Validates model *outputs* to the extent actually tested |
| **F6** | Pure analytical, synthetic simulation or optimization | Mathematical possibility and conditional predictions, not observed field causality |
| **F7** | Review or standard | Methodological synthesis or normative model, not primary validation |

## G. Equation-by-equation and observation extraction

For each eligible paper, record [extraction fields](./SYSTEMATIC_REVIEW_EXTRACTION_TEMPLATE_2026-11-03.csv):
- Precise citation, DOI, venue, original full-text PDF/location, page/equation/table/figure, review date; raw datasets, archive DOI/access/checksum and code location.
- Physical assets and *actual* interconnection diagram, site climate and operating envelope, equipment make/rating/cooling/age; sensors, physical positions, instrument bounds, timing resolution, time zones, measurement versus derived channels.
- States \`x\`, forcing \`d\`, controls \`u\`, time step; first law, state balance, constitutive terms, loss/cooling laws, battery pack/EVSE rectifier/transformer distinctions, signed P/Q meter boundaries, interface \`Phi\`, constraints and units.
- Parameter source: datasheet/standard, bench-identified/field fit, estimated, assumed; dimension/identifiability/conditioning; thermal time constants, direction-specific propagation delays and service delay must be separate fields.
- Report measured-vs-simulated/out-of-sample, chronological/asset/site splits, comparator baseline and whether future disturbances were **observed** (hindcast) versus predicted (real forecast); errors/uncertainty and extreme-heat range, ablation, robustness and model failures.
- Distinguish charger derating (charger's *offered* power) from vehicle SOC taper (accepted/delivered), electrical conversion loss from measured reject heat, modeled transformer aging from life loss, and unserved energy from missed mobility service.

**Independent full-text checks:** two readers for selected high-stakes claims or explicit one-reviewer limitations; extract exact equations and source print page. For PDFs used, inspect original page figures and labels; never rely on publisher abstract for a claim of observed thermal states. Record original edition of standards (do not publish proprietary text).

## H. Critical appraisal without an unjustified numeric meta-score

Judge each central claim on:
- **Physical directness**: same installation and connection? temperature measured or estimated? measured restrictions versus inferred cause?
- **Measurement quality**: calibrated sensors and known location, units, signs, clocks, sampling, missingness, invalid codes, meter boundary, independent error diagnostics.
- **Identification and confounding**: distinguishes ambient, background load, SOC and thermal protection logic; sufficient observed excitation; parameter structural/practical identifiability.
- **Validation design**: independent holdouts across *time and assets*, no temporal leakage; appropriate physics and data-driven baselines; genuine prediction vs conditional hindsight; extrapolation and sensitivity uncertainty.
- **Reproducibility**: source raw data, code, parameter and model assumptions available; figures/equations traceable; conflicts/limitations.
- **Relevance**: extreme heat, charging/transformer hardware class, time-scale, bidirectional interface and meaningful electricity/mobility service outcome.

Each domain rated \`adequate\`, \`partial\`, \`not documented\`, or \`not applicable\` **with exact source quotation/page**; avoid adding scores across fundamentally different study designs. Separate evidence confidence from topic relevance. A peer-reviewed publication is not necessarily physically identified.

## I. Planned synthesis (not yet executed)

1. **State-of-the-art matrix:** rows = individual paper/model and source; columns = physics, measured variables, coupled interface, validation, P/T directional inference, temporal delays, resilience/service, external transfer, data/software availability.
2. **Time/scale map:** \`thermal time constant\` vs \`propagation delay\` vs \`service time\`; record hardware scales and regimes.
3. **Equation taxonomy:** transformer IEC/equivalent-thermal/heat-diffusion; EVSE heat loss/cooling; battery thermal ODE/PDE; network power-flow/charging/transport service; PINN inverse/forward/surrogate/hybrid.
4. **Evidence/novelty table:** known solved problems, partial proofs and unverified links; cite at least one closest predecessor **for each claimed novelty**.
5. **Narrative critical synthesis by physical mechanism and model**, reporting contrasts/heterogeneity. Quantitative meta-analysis **only if** studies share comparable experimental units, hardware/meter boundaries, outcome definitions and uncertainties. Otherwise do not pool RMSE, thermal aging, or charging-energy percentages.
6. **Method-selection recommendation:** data suitability/equation identifiability → pure physics baseline → optional gray-box/PIML/PINN → asset/time/heat-stress transfer tests → service viability.

## J. PINN/PIML decision gate specific to Professor Phelan's instruction

**Landmark predecessor:** Bragone et al. (2022), DOI 10.1016/j.epsr.2022.108447, **already** applied heat-diffusion PINNs to transformer real field data and benchmarked against finite-volume solutions. **Another predecessor:** Cao et al. (2026), DOI 10.1016/j.applthermaleng.2026.130776, applied a physics-informed *neural Transformer architecture* to EV thermal management with real-vehicle experiment data. Do not claim originality for component PINN alone.

A physics-informed candidate for \`P\` thermal state:
\[
r_P(t)=C_P\frac{d\hat T_P}{dt}
       -P_{\mathrm{loss},P}(I_P,\hat T_P;\theta_P)
       +Q_{\mathrm{cool},P}(\hat T_P,T_a;\theta_P).
\]
A training objective *if parameters, units and observation operators make this meaningful*:
\[
\mathcal L=
w_{\mathrm{obs}}\|\hat y-y_{\mathrm{measured}}\|^2_{\Sigma^{-1}}+
w_{\mathrm{phys}}\|r_P\|^2+
w_{\mathrm{initial}}\|\hat x(0)-x_0\|^2+
w_{\mathrm{bc}}\|\text{boundary residuals}\|^2.
\]
Constraint-weight selection/normalization, noisy derivatives, structural identification, unknown losses, and cross-asset validation are experimental design issues; a small physical residual is **not proof of correct physics**.

**Preconditions (no invented universal minimum sample count):**
- Authenticated measured states/inputs **co-observed under the relevant regime** with physical units and clock; abnormal sensor codes resolved; event and boundary conditions verifiable.
- Physical states/parameters sufficiently identifiable or fixed from independent tests; data contain independent variation/excitation across ambient, current, cooling/control modes.
- Independent *chronological, session and equipment* holdouts, with some hot-condition data; separately quantify interpolation and extrapolation.
- Compare **(i)** calibrated pure physics ODE/PDE, **(ii)** persistence/standard physical engineering baseline, **(iii)** simple statistical/gray-box residual, **(iv)** PINN/hybrid if warranted. Same measured inputs and holdouts, per-horizon RMSE and MAE, constraint violations, uncertainty coverage, external transfer, computational cost and data efficiency.
- Do not train a coupled thermal PINN by aligning Norway, Slovenia, Qatar and German vehicle logs as though from one measured site. Without physically connected thermal observations, coupled PINN would at most be a **conditional simulation/surrogate**, not field-validated interdependency inference.
- **Decision:** Data QA invalid/thermal states unobserved → physics-only model with explicitly assumed parameters and parameter sensitivity. QA passed but limited paired observations → test *modest* gray-box/physics-regularized inverse parameter fit against physics baselines. Sufficient quality, identifiability and defensible validation design → **compare** PINN/PIML experimentally; choose only if it independently improves relevant metrics/uncertainty/physics feasibility. A large row count alone never establishes suitability.

## K. Deliverable inventory and stopping criteria

| Artifact | Required before calling review thorough/complete |
|---|---|
| Protocol v0.2 | Lock scope/eligibility/version; record date and deviations |
| Exact search log | One row per platform×query×date with retrieved counts, export filenames/hash; database/platform names |
| Raw bibliographic exports | Saved originals, dedup mapping and citation chasing provenance |
| Title/abstract + full-text screening log | Eligibility and one primary reason for exclusion, reviewer process, full-text retrieval attempted |
| Primary paper reference library | Complete source bibliographies and verified DOI/full text |
| Extraction matrix | Equation/figure pages, sensor/asset variables, measured-vs-model status, validation gates and source data links |
| Evidence and model comparison | Separate F1–F7, physics/PINN results, independent holdouts and confidence qualifiers |
| PRISMA-ScR or PRISMA 2020 flow | Real observed numbers that reconcile arithmetically |
| Novelty boundaries | Supported by comparisons to closest counterexamples, no unsupported 'first ever' |
| Decision memorandum to Prof. Phelan | Demonstrated prior-work mapping, available experimental data, choice of pure physics vs gray-box/PINN, unresolved needs |

**State as of creation:** The earlier **10-paper targeted scan** and this **new verified PINN/thermal review additions** are **seed citations**, *not a PRISMA database search*. No publication counts, screening decisions, excluded-source totals or claimed meta-analysis have been fabricated.

## L. Current verified high-priority references to scrutinize

- **Bragone et al. 2022**, *Physics-informed neural networks for modelling power transformer’s dynamic thermal behaviour*, DOI 10.1016/j.epsr.2022.108447 — real transformer field observations + heat diffusion PINN vs finite-volume reference; **direct prior art**.
- **Cao et al. 2026**, *Physics-informed Transformer for end-to-end energy prediction of integrated electric vehicle thermal management under extreme ambient temperature conditions*, DOI 10.1016/j.applthermaleng.2026.130776 — EV heat-pump vehicle test data and physics-informed neural Transformer; external equipment transfer and raw source still require checking.
- **Oladigbolu et al. 2025**, *A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources*, DOI 10.1016/j.est.2025.118419 — existing broad coupled power–transport review, check overlap and how it treats thermal interfaces.
- **Fletcher & Khan 2025**, *Maximising Electric Vehicle Fast Charging by Improved Thermal Management of Distribution Transformers*, RACE report https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf — installed 2025 Part 1 project modeling and heat-run context; **not** connected monitored field Part 2.
- **Krama et al. 2026**, *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*, DOI 10.1016/j.ecmx.2026.101960 — operating EVSE thermal derating; raw on request.
- **Li, Chang & Lu 2026**, *Field Measurement and Analysis of an Electric Bus Charging Station: A Case Study on Transformer Losses and Harmonic Impacts*, DOI 10.1109/PESGM58988.2026.11693150 — physical interface electrical field monitoring; transformer/EVSE internal temperature raw sensors not verified.
- **Wen et al. 2025**, *Robust Resilience Enhancement by EV Charging Infrastructure Planning in Coupled Power Distribution and Transportation Systems*, DOI 10.1109/TSG.2024.3390657 — numerical planning/optimization not joint thermal field sensing.
- **Raissi et al. 2019**, PINN foundational method, DOI 10.1016/j.jcp.2018.10.045.
- **Karniadakis et al. 2021**, *Physics-informed machine learning*, DOI 10.1038/s42254-021-00314-5.
- **IEC 60076-7:2018** loading guide for mineral-oil-immersed transformers https://webstore.iec.ch/en/publication/34351 ; an applicable model standard where hardware conditions match; **not** source validation.
- **TUM seven-EV operational UDS** original https://github.com/TUMFTM/electric-vehicle-uds-dataset and [ID1 thesis QA](https://github.com/Dossiya-SE/MSE-thesis/blob/main/data/field_candidates/2026-11-03/TUM_ID1_FIELD_THERMAL_QA_2026-11-03.md). Battery field source only; anomalous 1023°C-like codes require QA.

**Starting references (NOT systematic-screened):** [17-source verified seed bibliography, each with claim-level limitations](./SYSTEMATIC_REVIEW_VERIFIED_SEED_REFERENCES_V02.csv).

**Immediate next action:** Freeze/approve this protocol, execute platform-valid A–F searches with auditable counts, and independently extract full equations from Bragone, RACE, Cao, Krama and Li before selecting modeling complexity.
