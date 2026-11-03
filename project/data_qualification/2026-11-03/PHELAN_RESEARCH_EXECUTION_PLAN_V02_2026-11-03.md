# Professor Phelan research execution plan — consolidated v2.0

**Thesis:** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Planning date:** 3 November 2026  
**Repository status:** Active *working* research plan, pending methodological review and protocol lock; **not a supervisor-approved protocol**, executed systematic review, or independently validated coupled model.  
**Branch:** `user-data-qualification-2026-11-03`, not merged to `main`.

**Supersedes as the primary *planning structure*:** [Detailed execution plan v1.0](./PHELAN_FEEDBACK_MASTER_RESEARCH_EXECUTION_PLAN_V01_2026-11-03.md). The original v1.0 and [44-task register v1.0](./PHELAN_FEEDBACK_TASK_REGISTER_V01_2026-11-03.csv) are retained unchanged as methodological and version-history records.

**Implementing register:** [Remapped 44-task register v2.0](./PHELAN_RESEARCH_TASK_REGISTER_V02_2026-11-03.csv). **Research-method authority:** [Systematic review protocol v0.2](./SYSTEMATIC_REVIEW_EXECUTION_PROTOCOL_V02_2026-11-03.md) until superseded by a dated, explicitly locked protocol.

## 1. Professor Phelan's two requests

1. **“What have other people done in this area? … have you conducted a thorough literature review?”** Execute a reproducible, sufficiently comprehensive examination of prior field, laboratory, theoretical, mathematical and computational work, explaining exactly what was *measured*, *derived*, *simulated* and *independently validated*.
2. **“If we're able to find some experimental data … [consider] a physics-informed neural network or some other kind of physics-informed machine learning … if we can't find the data … proceed with a pure physics model.”** First qualify measurements and physics; then compare candidate methods under matched independent tests where possible. Do not choose a PINN by preference alone or misrepresent unconnected data as one instrumented system.

**Immediate request boundary:** Produce the research evidence base, scientific gap and defensible methodology decision. **Full coupled physical field validation and completed SO1–SO3 resilience results are downstream thesis tasks, not preconditions for honestly answering these requests.**

## 2. General objective

Establish a comprehensive, reproducible scientific evidence base identifying what prior researchers have investigated, mathematically formulated, experimentally measured and independently validated concerning the time-dependent thermal, electrical and service interdependencies between power systems and electrified transportation under extreme heat. Use it to determine what physics and what data support pure physics, hybrid or physics-informed ML modeling, and to bound a defensible thesis contribution.

## 3. Six objectives and acceptance outcomes

| ID | Specific objective | Measurable outcome |
|---|---|---|
| **O1 — Scientific literature coverage** | Systematically discover and select relevant primary papers, standards, reports, data descriptors and reviews | All executed queries, exact timestamps/filter settings, raw exports/checksums, dedup logic, eligibility and exclusion reasons reproducible |
| **O2 — Critical scientific analysis** | Extract mathematical laws, constitutive assumptions, states, sensors, data ranges, parameter provenance, validation and uncertainty | Claim-by-claim equation/table/figure/page matrix tied to original primary sources; unknown items explicitly flagged |
| **O3 — Research gap identification** | Determine solved problems, close counterexamples, unsupported mechanisms, state–time and service gaps | Closest-paper and novelty-boundary matrix with contrary evidence sought, no unsupported global “first” claims |
| **O4 — Experimental-data qualification** | Audit transformer, EVSE, vehicle and connected-site sources for physical meaning, quality, observability, identifiability and validation | Dataset-to-equation matrix with explicit calibration/validation admission and exact blocked conditions |
| **O5 — Mathematical methodology selection** | Independently test a pure-physics baseline and conditionally gray-box/PINN/PIML where qualified measurements allow | Matched benchmark and VVUQ decision; or documented physics-only fallback when data/identifiability inadequate |
| **O6 — Supervisor-ready synthesis** | Produce a concise, reference-supported answer to Professor Phelan | Literature review, state-of-art/gap, data availability, methodological decision, limitations and next evidence requirements |

**Thesis connection:** SO1 = directional thermal/electrical physical interfaces; SO2 = coupled state–time equations, calibration and VVUQ; SO3 = service viability, criticality, propagation, recovery and interventions. O1–O6 establish their foundation but do not prove the coupled-system result.

## 4. Eight-package work-breakdown structure (official v2.0)

| WP | Scope and key activities | Deliverables | Exit gate |
|---|---|---|---|
| **WP1 — Research governance (T01–T04)** | Confirm frozen SO1–SO3 scope, review LQ1–LQ6, evidence units, eligibility, exclusion rules, reviewer availability, source access and protocol version. Translate thematic searches into executable database syntax | Dated version-locked protocol, true roles, exact query plan, archive naming and traceability standard | **G1**: methods/rules and allowable amendments recorded **before** systematic execution; supervisor approval recorded *only if received* |
| **WP2 — Literature discovery (T05–T09)** | Search six independent blocks A–F in accessible Scopus/WoS/IEEE/Compendex and supplementary sources; backward/forward citation tracing; seed-recall diagnostics | Authentic RIS/BibTeX/CSV corpus, per-platform complete query log, counts/export hashes, access limitations, citation-chase register | **G2**: real search exports and provenance support every reported count; inability to access database explicitly logged |
| **WP3 — Study selection (T10–T13)** | Normalize/merge metadata, DOI/title-year dedup, title/abstract and full-text screening, record reasons; transparent one/two-reviewer practice | Dedup and screening decisions, retrieval-failure records, reconciled actual PRISMA-ScR flow | **G3**: each excluded full-text report has recorded reason, every included study traceable, counts reconciled |
| **WP4 — Scientific extraction (T14–T19)** | Read primary papers, audit published equations, sensors, equipment topology, thermal losses, cooling, parameters, initial/boundary conditions, uncertainties, test splits and measured-vs-modeled claims | Source-linked physical/equation/field-evidence matrix and model/measurement quality appraisals | **G4**: each important claim references DOI and original page/equation/figure, with verification limits stated |
| **WP5 — Scientific synthesis (T20–T23)** | Compare direct closest prior art and counterexamples; map F1–F7 *per claim* and separate thermal constants, propagation delay and service onset; establish bounded novelty | SO1–SO3 evidence map, equations taxonomy, state-of-art chapter outline, defensible novelty/knowledge-gap table | **G5**: novelty claims tested against strongest predecessors (including Bragone 2022, RACE 2025, Cao 2026, Krama 2026, Li 2026, Wen 2025); no unsupported “first ever” |
| **WP6 — Experimental data (T24–T29)** | Audit SINTEF, STREAM Slovenia, TUM, Leuven, OSF, OPSD, Qatar, Li and any same-site field sources; original hashes, unit/clock/sensor semantics, limitations, physically connected topology, identifiability, relevant extreme heat | Dataset QA, data/experiment gaps, sensor-to-equation matrix, instrumented connected-site candidate/access log | **G6**: data quality/physical states/operating conditions qualified; source separation maintained; “unavailable” clearly distinguished from “not measured” |
| **WP7 — Model selection (T30–T37)** | Derive conservation-based ODE/PDE and calibrated pure-physics benchmark; matched holdouts, VVUQ. If physical/data prerequisites passed, test minimal gray-box/PIML/PINN against the same inputs, horizons and baselines | Reproducible physics benchmark + conditional model-comparison **or** justified physics-only decision | **G7**: selected approach has transparent evidence and limitation; same-site vs external generalization separated, no false coupled field validation |
| **WP8 — Research reporting (T38–T41)** | Write thesis review/mathematical background and gap; assemble source library, traceability/PRISMA appendix and 2-page supervisor brief; perform QA and record real feedback | Supervisor-ready technical research package, documented corrections and next experiment requests | **G8**: answers both questions from Professor Phelan with credible citations, explicit model decision, limitations and validation needs |

**Downstream, outside these eight:** legacy tasks **T42–T44** for complete physically connected SO1–SO3 thesis experiments remain in register under workstream **THESIS-DOWNSTREAM**, **not WP9** of the immediate professor-response plan. Do not lose them or count them as complete.

### Eight-week illustrative schedule (targets, NOT delivery promise)

| Proposed period | Main WPs | Exit target and caveat |
|---|---|---|
| **Week 1** | WP1; WP6 source audit begins | Dated scope, eligibility, database access, actual executable queries and source inventory. Review protocol is **not** approved until recorded. |
| **Week 2** | WP2; WP3 begins; WP6 parallel | Raw bibliographic exports with real logged counts and dedup initiation. Date may shift with paid database access. |
| **Weeks 3–4** | WP3 + WP4; WP6 parallel | Transparent screening and intensive source-page mathematical extraction. Full-text access is a critical risk. |
| **Week 5** | WP5; WP4 residual queries | Evidence-bounded prior-art and novelty synthesis; unresolved counterexample literature triggers additional search. |
| **Week 6** | WP6 + WP7 | Data/identifiability gate and pure-physics baseline results; physical-model calibration may require additional equipment details. |
| **Weeks 7–8 (conditional)** | WP7 + WP8 | Matched optional PINN/gray-box comparison only if data pass G6; otherwise rigorously justified physics-only route, reviewer QA and supervisor package. |

**Parallelism:** WP6 runs concurrently with WP1–WP4. Preliminary physical derivation may use verified primary standards while screening continues; final model references must be reconciled with the completed review. The eight-week sequence can lengthen or narrow based on genuine blockers. No asynchronous work or future delivery is being claimed.

## 5. Method: exact scientific sequence

\[
\boxed{\text{Define}\rightarrow\text{Search}\rightarrow\text{Screen}\rightarrow\text{Retrieve}\rightarrow\text{Extract}\rightarrow\text{Verify}\rightarrow\text{Compare}\rightarrow\text{Synthesize}\rightarrow\text{Identify gap}\rightarrow\text{Qualify data}\rightarrow\text{Select model}\rightarrow\text{Validate}\rightarrow\text{Report}}
\]

### Search/selection standards

- **Tier 1**: systematic scoping/evidence map, report with **PRISMA-ScR** and source-specific eligibility; use **PRISMA-S** for reporting actual search strategies.
- **Tier 2**: critical, focused engineering physics/mathematical-model synthesis; use the transparent systematic-review elements appropriate to the subset and **PRISMA 2020** only if claiming a completed formal systematic review. PRISMA is a reporting framework, not proof of a high-quality review by itself.
- **Six independent search themes**: (A) transformer/EV load thermal models, (B) EVSE thermal derating/weather, (C) measured transformer–charger connectivity, (D) P–T dynamics/resilience, (E) physics-informed thermal ML/PINN, (F) transformer loading guides and mathematical baselines.
- Record the literal database-native search string, date/time, coverage year, result total, exported count, export filename and digest; do not turn seed references, provider passages or targeted web searches into systematic counts.
- Screen in accordance with locked rules, explicitly record investigator/reviewer method; document actual full-text retrieval attempts and reasons for exclusion.
- Classify **individual claims**, not entire papers, by original mechanism: operational connected field F1/F2, measured component field F3, controlled lab F4, field-driven model F5, pure simulation F6, review/standard F7.
- Maintain *original sources and access rights*: cite papers and quote short passages rather than uploading copyrighted PDFs to public repository.

### Mathematical/measurement verification requirements

For each primary study: original DOI/page/equation/figure; hardware rated capacities, source sensor positions, measured/derived data and units; governing conservation plus loss/cooling constitutive laws; boundary/initial conditions and state operator \(y=h(x)+\epsilon\); independent parameter source, identifiability and state observability; ambient/charge/load confounders; dynamics/temporal resolution; calibration/holdout metrics and uncertainty; external-asset or high-heat validation; interface map and service consequence quality.

The physical first law is broadly applicable, but a simplified model, fitted coefficient, or specific thermal limit is **not** automatically transferable to other equipment. A single installation's valid coefficients do not establish a general law or extreme-heat validity.

### Experimental-data and model-choice decision

| Situation | Decision | Required evidence or caveat |
|---|---|---|
| **A — No qualified experimental thermal measurements for the target subsystem** | Develop conventional physics-based ODE/PDE, physical-parameter bounds and uncertainty/scenario analysis | Clearly distinguish mathematical verification and conditional simulation from empirical validation; get more measured data where needed |
| **B — Qualified component-level measurements** | Calibrate and independently test pure physics first; optionally compare parsimonious inverse/gray-box/PINN/PIML **for that component** | Identifiable physical states/inputs, sensor and environmental ranges, holdout independence, fair baselines; *no connected field claim* |
| **C — Qualified *same-installation* transformer–EVSE thermal/electrical/restriction/service records** | Consider connected-system physics and conditional physics-informed coupled modeling with actual interface validation | Physical feeder/asset topology, synchronized thermal/electrical observations, reason-code/controls, confounder checks, service requirements, external validation |

**No hard threshold of row count is a PINN eligibility rule.** Data richness must correspond to the *physics variables and experimental excitation*, not a large long-format observation count.

**Minimum fair comparison:** calibrated physical ODE/PDE/standard model, persistence and/or simple parametric baseline, optional gray-box/hybrid/PINN if admissible; same trained/not-trained splits, time/asset/temperature holdouts, available future forcings, per-horizon RMSE/MAE, physics residual/violations, uncertainty coverage, transfer sensitivity, data-efficiency and computational cost. Prevent leakage, spurious out-of-range codes, simulated-to-measured equivalence and unstated direct thermal measurements.

## 6. Specific source priorities and open evidence gates

| Comparator/data | Established initial relevance | What must be done |
|---|---|---|
| **Bragone et al. 2022** | Prior transformer thermal PINNs using real measurements | Verify full equations, actual thermal states and independent train/test or external asset behavior |
| **RACE / Fletcher–Khan 2025** | IEC-style transformer thermal inertia plus simulated charging-energy and aging examples | Extract pages/coefficients, re-derive conservation/constitutive assumptions; don't treat modeled aging as measured field degradation |
| **Krama et al. 2026, Qatar** | Published field charger heat-driven derating, charging time outcome | Obtain original EVSE thermal/electrical datasets if permitted; distinguish charger thermal derating from SOC taper and time/environment confounding |
| **Li, Chang & Lu 2026** | Operating bus-station transformer electrical interface measurements | Verify full instrumentation, measured-versus-calculated losses and whether actual same-site thermal sensors/raw data exist |
| **Cao et al. 2026** | Physics-informed *neural Transformer* EV thermal management (not electrical transformer) | Test originality, actual raw experimental channels, validation design and model sensitivity |
| **SINTEF** | Measured transformer top-oil and ambient plus tested phenomenological model | Independently verify physics parameters, observed operating regime (max ambient 25.97°C) and beyond-site transfer |
| **TUM** | Seven production EV field logs; potential vehicle battery heat | Resolve 1023°C-like invalid/sentinel codes, local original SHA-256, timing/charging-state alignment and vehicle-held-out tests |
| **STREAM Slovenia** | Authentic paired station P/Q operating records | Verify source units/sign/nameplates and topology; cannot infer transformer overload or EVSE heat from signed P/Q alone |

**Known blocked claims:** no verified one-site time-aligned transformer + EVSE internal thermal field data, no qualified extreme-heat *coupled* thermal field validation, no demonstrated field bidirectional propagation or quantified measured service-level resilience. Literature discovery may change the assessment; document and compare new evidence openly.

## 7. Execution controls and milestone proof

| Gate | Proof before marking completed |
|---|---|
| **G1 WP1 governance** | Protocol status explicitly versioned and method/rules fixed, reviewer and permission status recorded |
| **G2 WP2 search** | Exact platform queries + actual dated exports and checked counts, seed-recall check |
| **G3 WP3 screen** | Dedup trace, inclusion and primary full-text exclusion reasons, reconciled real PRISMA records |
| **G4 WP4 extraction** | Key peer-reviewed primary sources verified with equation/figure/page, actual source data/model boundary and appraisal |
| **G5 WP5 synthesis** | Closest counterexample per proposed novelty, clear source-scope limitations and SO1–SO3 map |
| **G6 WP6 data** | Authentic files/units/time/quality/observability/identifiability and explicit field component vs coupled admissibility |
| **G7 WP7 methods** | Matched validated pure-physics comparison plus optional PIML, or a documented no-go physics-only route; VVUQ and external-asset limits |
| **G8 WP8 reporting** | Traceable state-of-art, experimental-data decision, bibliography, reproducibility appendix, short supervisor brief; reviewer/approval not invented |

**Progress at plan adoption:** WP1 is **partial**; WP2/WP3 systematic execution **not started**; WP4 targeted initial reading only; WP5 preliminary comparisons; WP6 partial source qualification; WP7 initial SINTEF component model (not method selection); WP8 not ready. The prior **17 seed references** are *not* systematic included studies. Review corpus, full text screen, systematic PRISMA flow, coupled validation and full model comparison are **not complete**. The earlier provisional SO1 35%, SO2 20%, SO3 5% / equal-weight 20% overall remain *planning judgments*, not confirmed evaluation.

## 8. Version mapping and continuity (44 legacy tasks retained)

| New active WP | Source legacy WP and task IDs | Meaning |
|---|---|---|
| WP1 | legacy WP0: **T01–T04** | Governance |
| WP2 | legacy WP1: **T05–T09** | Literature discovery |
| WP3 | legacy WP2: **T10–T13** | Study selection |
| WP4 | legacy WP3: **T14–T19** | Scientific extraction |
| WP5 | legacy WP4: **T20–T23** | Scientific synthesis |
| WP6 | legacy WP5: **T24–T29** | Experimental data |
| WP7 | legacy WP6 + WP7: **T30–T37** | Physics benchmark and conditional PINN/PIML choice |
| WP8 | legacy WP8: **T38–T41** | Research reporting |
| THESIS-DOWNSTREAM | legacy WP9: **T42–T44** | Subsequent SO1–SO3 connected physical validation and resilience research |

Preserve **original** task IDs, priority, objective, activity, prerequisites, deliverable, test, status and role in [v2.0 register](./PHELAN_RESEARCH_TASK_REGISTER_V02_2026-11-03.csv), with a new `legacy_wp` and `scope` field. Do not silently mark planned tasks as completed or remove WP9 science from overall thesis scope.

**Planning targets and blockers:** register columns indicate target weeks, not strict deadlines. Replanning requires cause, date and no fabricated success. Store each genuine completed gate's artifact hyperlink and note in register before status is changed.

## 9. Next actions: first actual executed work

1. **WP1 (T01–T04):** lock v0.2 scoping-review protocol, validate bibliographic search syntax and note accessible platforms; record any external supervisor-method approval only when received.
2. **WP2 (T05–T09):** run search blocks A–F and citation chasing in available platforms; save literal query/filters/date/count/exports and seed-recall test.
3. **WP3/WP4 (T10–T19):** systematically screen studies; verify Bragone, RACE, Krama, Li and Cao equations against original full text.
4. **WP6 parallel (T24–T29):** continue original-source QA, prioritize Qatar EVSE raw thermal and TUM sensor decoding; do not wait for review completion to inspect measurements.
5. **WP5/WP7/WP8:** only then freeze novelty assessment, compare physics with eligible learning alternatives and report the evidence-based decision to Professor Phelan.

**Definition of done for Professor Phelan's immediate request:** a reproducible, source-grounded account of prior work and defensible research gap, plus an honest experimental-data-sufficiency assessment and justified decision between validated pure physics and optional PINN/PIML. It need not claim a successful PINN or finished coupled thesis.

**Source-control policy:** do not edit frozen thesis authority files or merge to `main` during this planning update; preserve raw data in authorized storage, original v1.0 plans, protocol v0.2 and empty logs until the relevant activity has actually executed.
