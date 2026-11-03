# Professor Phelan feedback — Master research execution plan v1.0

**Created:** 3 November 2026  
**Thesis:** *Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience*  
**Branch:** \`user-data-qualification-2026-11-03\` (research working branch, not \`main\`)  
**Status:** **ACTIONABLE PLANNING DOCUMENT — NOT A COMPLETED SYSTEMATIC REVIEW, VALIDATED PINN, SUPERVISOR APPROVAL OR FINISHED THESIS.**  
**Research owner:** thesis researcher; supervisor: Professor Pat Phelan. An independent second reviewer, data owner, or engineer is included as a role **only if actually available**, never fabricated.

## 1. Supervisor request and interpretation

Professor Phelan's explicit two-part guidance:

1. **“What have other people done in this area? … have you conducted a thorough literature review? … as a next step.”** Required: an accountable answer about the state of the art, grounded in systematic search, primary sources, comparative equations, measured versus modeled claims and defensible novelty boundaries.
2. **“If we're able to find some experimental data … it might be better to develop a physics-informed neural network, or some other kind of physics-informed machine learning model … If we can't find the data then let's just proceed with a pure physics model.”** Required: independently verify experimental-data adequacy; develop a transparent pure-physics baseline; test physics-informed learning **conditionally**, not as an assumed superior method.

### Primary objectives

| ID | Objective | Concrete answer/evidence required | Mapped thesis work |
|---|---|---|---|
| **O1** | Provide a thorough reproducible account of prior studies | Systematic scoping search/screening; source-verified state-of-the-art evidence map; clear strengths/limits | SO1–SO3 |
| **O2** | Determine the defensible novelty of our thermal interdependency question | Closest-paper comparison, negative-evidence search, exact verified novelty boundaries and alternatives | SO1/SO2/SO3 |
| **O3** | Reconstruct the physically justified model foundation | Primary paper equation/page audit, conservation laws, state/inputs/parameters, boundary conditions and identification | SO1/SO2 |
| **O4** | Establish which experimental data genuinely support calibration/validation | Dataset provenance, physical apparatus, units, clocks, measured-vs-derived, QA, range, relevant states and inputs | SO2 |
| **O5** | Make an experimentally supported model-selection decision | Physics vs simple gray-box vs PINN/PIML on *same* splits/metrics where admissible, plus UQ/complexity; justified physics-only fallback | SO2 |
| **O6** | Communicate a concise defensible response to Prof. Phelan | Short literature synthesis, evidence table, experimental-data decision, exact modeling plan and outstanding needs | Advisor deliverable |

**Scope constraint:** Completing O1–O6 addresses the immediate supervisor request; it is **not** equivalent to completing SO1–SO3 or field-validating a thermally coupled transformer–EVSE system.

## 2. Confirmed starting point — no double counting

Already saved in thesis GitHub:
- [Targeted comparators v0.1](./TARGETED_LITERATURE_THERMAL_PT_SYSTEMATIC_PROTOCOL_V01.md): ten source candidates, RACE source-specific thermal simulations and validation caveats.
- [Systematic review execution protocol v0.2](./SYSTEMATIC_REVIEW_EXECUTION_PROTOCOL_V02_2026-11-03.md): review questions, six search blocks, eligibility, evidence strata, protocol reporting and conditional PINN gate.
- [17 initial reference seeds](./SYSTEMATIC_REVIEW_VERIFIED_SEED_REFERENCES_V02.csv): **not systematic-screening count**. Closest direct prior art includes Bragone 2022 transformer thermal PINN and Cao 2026 physics-informed EV thermal management.
- [Search log template](./SYSTEMATIC_REVIEW_SEARCH_LOG_TEMPLATE_2026-11-03.csv), [screening log template](./SYSTEMATIC_REVIEW_SCREENING_TEMPLATE_2026-11-03.csv), [equation/data extraction template](./SYSTEMATIC_REVIEW_EXTRACTION_TEMPLATE_2026-11-03.csv): **header-only; no database review execution recorded**.
- [Measured-data Report 1](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md) and [thesis continuation checkpoint](./THESIS_RESEARCH_CHECKPOINT_2026-11-03.md). Initial same-site SINTEF thermal model and component analytics exist, but coupled field and hot-extreme validations are **not established**.
- [Literature-to-measured-data crosswalk](./LITERATURE_TO_DATA_VALIDATION_CROSSWALK_V01.md) and [TUM original ID1 audit on main](https://github.com/Dossiya-SE/MSE-thesis/blob/main/data/field_candidates/2026-11-03/TUM_ID1_FIELD_THERMAL_QA_2026-11-03.md). TUM original seven Parquet files are user-local with anomalous temperature channels, not eligible as validated training data until QA.

**Result to date:** preliminary literature review and preliminary experimental-data audit, **not** completed systematic review, coupled causal physics validation, or empirically selected PINN.

## 3. Work packages, objectives, activities, deliverables and gates

The [machine-readable task register](./PHELAN_FEEDBACK_TASK_REGISTER_V01_2026-11-03.csv) is the authoritative activity-level checklist with IDs, dependencies and acceptance tests. Package-level plan:

### WP0 — Research governance and protocol lock (T01–T04)

**Objective:** prevent post-hoc eligibility, fabricated review counts or overwritten evidence.

**Activities:** lock exact core review questions LQ1–LQ6 and relationship to SO1–SO3; label current bibliography as pilot/seed; define review type as systematic **scoping evidence map** plus focused **critical primary mathematical synthesis**; confirm inclusion/exclusion and evidence codes; version all amendments; establish files/folders for citations, original bibliographic exports, raw permitted paper access, SHA-256 manifests and logs.

**Deliverables:** approved/dated protocol version; filled decision-rule appendix; immutable search/export naming convention; work register.

**Gate G0:** every database record can be traced to its source platform, exact query and date; no claim of completed PRISMA flow; supervisor approval where available is recorded, never presumed.

### WP1 — Systematic retrieval of the state of the art (T05–T09)

**Objective:** identify genuine prior art without only selecting supporting citations.

**Activities:** adapt six conceptually independent blocks A–F from protocol v0.2 to Scopus, Web of Science, IEEE Xplore and Engineering Village where accessible; also search Crossref/OpenAlex, publisher sites and repository/standard sources as supplementary strata; validate search sensitivity using the 17 seed records in their intended disciplines; run separate forward/backward citation chaining from Bragone, RACE, Krama, Li, Cao, Wen and relevant review articles; export all records without rewriting timestamps or DOI.

**Deliverables:** actual query-by-platform logs with date/time, total search result counts, exact filters and raw export names/sha256; DOI-normalized raw citation corpus; citation chasing log; documented access restrictions.

**Gate G1:** **no invented search totals**. Every executed search has an export or recorded tool limitation, and missing high-priority seeds trigger a search-sensitivity investigation.

### WP2 — Deduplication and eligibility screening (T10–T13)

**Objective:** turn raw search results into a transparent defensible pool of studies.

**Activities:** exact DOI and near-duplicate title/year disambiguation; separate multiple reports from same project; systematic title/abstract screening; attempt full-text retrieval for all include/uncertain records; use predeclared exclusion reasons; dual independent reviewer where truly available, otherwise explicitly single-reviewer protocol with verified subsample. Maintain clear counts for study vs report vs dataset vs source passage.

**Deliverables:** master bibliography, dedup map, screened title/abstract and full-text logs, retrieval failure list, PRISMA-ScR flow based on **actual** observed counts.

**Gate G2:** reconciled screening arithmetic; a documented exclusion reason for every excluded full text; no abstract-only claim promoted to field thermal validation.

### WP3 — Full-text physics, data and mathematics extraction (T14–T19)

**Objective:** answer “what have others actually done” at equation, apparatus and validation level.

**Activities:** detailed source-by-source extraction beginning with **Bragone 2022, RACE 2025, Krama 2026, Li et al. 2026, Cao 2026, Wen 2025**; page/eq/figure-level verification of original primary sources; extract thermal and electrical states, PDE/ODE/circuit/thermal-rating equations, constitutive loss/cooling terms, boundary and initial conditions, physical equipment identity, interconnection topology, sampling, sensor positions, environmental ranges, controls and model limitations. Record parameter measured/fitted/assumed, independent holdout, actual comparison baseline and whether a published “heat effect” is directly measured or simulated.

**Deliverables:** populated full-text extraction matrix; rigorous equation table; study quality appraisal (physical directness, sensing QA, identifiability, validation, reproducibility); original-data/code links; null/unknown labels instead of guesses.

**Gate G3:** each thesis-relevant numerical assertion has source/printed page/table/equation and evidence class. Key study claims verified against figures, not merely abstract; copyright respected (link to PDFs, no redistribution without rights).

### WP4 — Critical synthesis, closest prior art, and novelty boundary (T20–T23)

**Objective:** answer the supervisor's question with scientific precision.

**Activities:** summarize established versus provisional mechanisms by transformer, charger, vehicle, feeder interface and service; classify **by claim** as F1–F7 (field connected, partial connected, operational component, lab, field-driven model, simulation, review); distinguish (a) thermal time constant, (b) interface propagation delay and (c) service-onset time; search counterexamples to every proposed novelty claim; articulate alternatives if thermal coupling has already been studied. Compare with 2022 transformer PINN and 2026 EV thermal methods to avoid asserting “first PINN” novelty.

**Deliverables:** state-of-the-art narrative and source table; directional P→EVSE and EVSE→P interface evidence matrix; closest-predecessor and contradicted-claim matrix; explicit provisional thesis novelty and limits.

**Gate G4:** for each novelty claim, cite the closest counterexample and specify the *unproven* part; no “first ever,” global unstudied-topic or negative search conclusion without evidence coverage and date limits.

### WP5 — Experimental-data suitability / physics identifiability (T24–T29)

**Objective:** decide what actual observation quality permits, **before fitting PINNs**.

**Activities:** check original licensing/checksums and apparatus of SINTEF (transformer thermal), Slovenia (P/Q), KU Leuven (lab charging), OSF (lab PQ), OPSD (matched charging/grid demand), TUM (vehicle battery thermal) and targeted Qatar/Li datasets; validate raw measured-vs-derived channels, units and sensor location; audit physical interface connectivity, time-zone/sampling, gaps, anomalous codes and heat operating range; compare observation operator \(y=h(x)+\epsilon\) with theoretical states and available forcing; structurally/practically test identifiability of heat capacity, loss and cooling terms; explicitly verify real hot exposure co-occurs with charging/transformer loading.

**Deliverables:** versioned dataset-by-equation coverage matrix; source-backed admission decision per dataset/model state; open data requests to Qatar/Li/connected sites, source permissions and limitations; physical parameter-identification audit.

**Gate G5:** no temperature or “heat flux” is invented from electrical power gaps; TUM 1023°C-like codes excluded from physical inference *only after code/QA rationale*, preserving raw originals; unverified cross-country sources not joined as measured same-site data.

### WP6 — Reproducible pure-physics model and benchmark (T30–T33)

**Objective:** independently establish the physics-only option Professor Phelan explicitly permits.

**Activities:** derive first-law transformer thermal equations from study-specific appropriate standards and RACE, with all units, heat sources, cooling and boundary states; specify equipment-appropriate reduced order, measurement operator and parameter identification; test on same-site chronological holdout with *future inputs distinction*; add uncertainty/sensitivity, conservation residual, structural identifiability and no-leakage measured baselines. Use component-only model if connected interfaces not measured.

**Deliverables:** derivation with each assumption and citation, executed reproducible code and original-data checksums, holdout metrics and uncertainties, residual/identifiability report.

**Gate G6:** pure physics baseline independently tested with reproducible inputs and nontrivial baselines. Its failure modes explicitly stated; no long-horizon “forecast” when future forcing is known only retrospectively.

### WP7 — Conditional PINN/PIML experiment and model choice (T34–T37)

**Objective:** follow Professor Phelan's conditional suggestion, not presuppose use of AI.

**Activities:** gate data suitability. If enough authentic, co-observed, instrumented thermal states and physical source terms exist, formulate a physics-informed *component model* / inverse fit; compare against (1) physical engineering baseline, (2) persistence/appropriate statistical baseline, and (3) simple gray-box or residual hybrid. Use identical time/asset/heat-condition holdouts, metrics and physical-feasibility constraints. If data inadequate, do **not** substitute fabricated synchronized measurements or cherry-picked synthetic ground truth: choose physics-only and document why. Evaluate per-horizon RMSE/MAE, uncertainty/coverage, sensitivity, extrapolation, energy residuals, computational cost and transfer where data allow.

**Deliverables:** conditional model benchmark and transparent choice memo; or physics-only decision memo with precise experimental-data requirements.

**Gate G7:** PINN/PIML is justified **only when measurement and independent validation support it** and documented benefits/limitations are acceptable. A PINN with physics residuals is not proof of causal field coupling.

### WP8 — Synthesis and supervisor communication (T38–T41)

**Objective:** produce a short and defensible answer to Professor Phelan and a reproducible chapter-ready research record.

**Activities:** write the reviewed literature section with in-text citations, narrative comparative table, methods/gap and study limitations; summarize what experimental data actually exist/are missing; present model-choice logic and proposed experiments; draft a **concise** supervisor brief; pre-submission self-audit of originality, source traceability, citation validity, protocol version and unresolved limitations; record supervisor feedback and revisions.

**Deliverables:** literature review manuscript draft; reference library (BibTeX/RIS where lawful); source-to-claim table; 2-page advisor brief (goal, existing work, physical knowledge gap, data, method decision, next experiments); reproducibility appendix.

**Gate G8 / immediate supervisor request fulfilled:** researcher can clearly document (1) what previous studies did and did not show, (2) exactly where our work differs and with what confidence, and (3) **why** pure physics or PINN was chosen under data-quality and validation constraints. Missing evidence is clearly labeled rather than hidden.

### WP9 — Downstream full-thesis integration (T42–T44; **NOT a prerequisite to answering Phelan now**)

**Objective:** implement the SO1→SO3 thesis once the literature/model decision has been made.

**Activities:** identify measured transformer–EVSE network topology and thermal derating interfaces; compare uncoupled vs static- and dynamic-coupled models, uncertainty and external transfer; define charging availability, transformer health/limits, resilience, recovery and mobility-service constraints. Keep assumptions separate from field results.

**Deliverables:** SO1–SO3 validated coupled results **only if** adequate physical and empirical evidence exists; otherwise explicitly conditional simulation and validation plan.

**Gate G9:** never claim measured coupled severe-heat resilience or transferable verified service benefits from independent foreign-source components.

## 4. Decision logic and non-negotiable research controls

**Model decision matrix**

| Evidence condition | Permitted approach | Prohibited claim |
|---|---|---|
| Measured thermal states or forcing absent, unreliable or disconnected; fundamental physics available | Pure physics with explicit source parameters, sensitivity, assumptions and conditional validation | “Field-validated PINN” / identified heat flux |
| Limited reliable co-observations of single component, partially estimable dynamics | Calibrated thermal physics + perhaps parsimonious gray-box inverse/residual if justified | General coupled causal claim |
| Enough verified thermal/physical inputs and independent held-out observations to constrain physics residual and test prediction | Benchmark PINN/PIML **as an experiment** against pure physics and simpler models | PINN is automatically superior or universally transferable |
| Same physically mapped transformer–EVSE installation with synchronized measured power, thermal states and restriction/control events | Coupled dynamic field validation, temporal delays, viability/service consequences, candidate PIML | Full validation without topology, causal controls or service observations |

**Science rules:** original raw records are authoritative, local file origins and access must be explicitly logged; sensor errors and model assumptions are never replaced by convenient values; use conservation and dimensional consistency; prohibit observational correlations presented as causal; avoid parameter-transfer claims without hardware-specific testing; separate field, lab and numerical outcomes; document null results; retain IP/license limits; update research log each session.

## 5. Dependencies, priority and work order

\`\`\`text
NOW:  WP0 protocol/roles/log freeze
          |
          +--> WP1 search/export --> WP2 dedup/screen --> WP3 primary equation extraction
          |                                               |
          |                                               +--> WP4 prior art & novelty evidence
          |
          +--> WP5 source QA/experimental-data availability
                          |
                          +--> WP6 physical baseline & independent benchmark
                                                  |
                                                  +--> WP7 conditional PINN/gray-box trial or physics-only decision
                                                                        |
                  WP4 + WP5 + WP6 + WP7 -------------------------------+--> WP8 advisor package
                                                                               |
                                                                               v
                                                                  WP9 full thesis SO1–SO3
\`\`\`

**Critical path:** systematic search/screen → exact primary-source mathematics → evidence-based novelty boundary, conducted alongside dataset QA → baseline/model choice → supervisor briefing. WP6 can start before WP2 is complete using *already verified physical principles*, but final physics claims must reflect review findings. WP9 is a distinct continuation goal and should not delay answering the literature-review request.

**Immediate next actions, in order:**
1. Publish a dated review scope/eligibility/search-platform lock and exact database-valid A–F query set (WP0/WP1).
2. Run searches with genuine counts, exports and dedup; check the preidentified 17 seeds (WP1/WP2).
3. Read full source papers and extract equations/pages for Bragone, RACE, Cao, Krama, Li (WP3).
4. Parallel: dataset QA and raw measurements/Qatar-Li access requests (WP5).
5. Produce evidence/novelty matrix and baseline-vs-PIML decision (WP4/WP6/WP7).
6. Submit source-linked advisor report documenting decisions and open gaps (WP8).

## 6. Milestone evidence and acceptance ledger

| Milestone | Acceptance evidence | Status at plan creation |
|---|---|---|
| M0 Scope/protocol registered | Approved or version-locked dated search/screen rules + reviewer declaration | **DRAFT, not frozen** |
| M1 Systematic search complete | Each A–F query recorded by database, result count and exported bibliography with hash | **NOT STARTED** |
| M2 Screening complete | DOI/name dedup trace, included/excluded reasons and arithmetic PRISMA flow | **NOT STARTED** |
| M3 State-of-the-art extraction | Source PDF pages/equation details for included high-impact papers, claim-level evidence/quality | **PARTIAL target review only** |
| M4 Research gap qualified | Coverage-bound novelty table against close counterexamples | **PRELIMINARY** |
| M5 Experimental-data decision | Source-by-equation admission, physical identifiability and connected/topology gates | **PARTIAL** |
| M6 Physics baseline | Reproduced exact code/data inputs, chronological holdout, uncertainty, physics limits | **PRELIMINARY SINTEF component** |
| M7 PINN/physics selection | Prespecified matched benchmark OR explicitly justified physics-only | **NOT DECIDED** |
| M8 Advisor response ready | Accurate brief + review report + citations + method decision + remaining experiments | **NOT COMPLETE** |
| M9 Coupled system thesis validated | Observed interface and credible external coupled validation | **BLOCKED, outside immediate request** |

## 7. Repository organization and artifacts

All new files live in \`project/data_qualification/2026-11-03/\` on the existing review branch; avoid frozen-file edits:
- **This master plan:** \`PHELAN_FEEDBACK_MASTER_RESEARCH_EXECUTION_PLAN_V01_2026-11-03.md\`.
- **Task register:** \`PHELAN_FEEDBACK_TASK_REGISTER_V01_2026-11-03.csv\` (T01–T44 with owner role, predecessors, deliverable, acceptance test, current state).
- **Review method:** \`SYSTEMATIC_REVIEW_EXECUTION_PROTOCOL_V02_2026-11-03.md\`.
- **Starting bibliography:** \`SYSTEMATIC_REVIEW_VERIFIED_SEED_REFERENCES_V02.csv\`.
- **Search log:** \`SYSTEMATIC_REVIEW_SEARCH_LOG_TEMPLATE_2026-11-03.csv\` (no counts yet).
- **Screening log:** \`SYSTEMATIC_REVIEW_SCREENING_TEMPLATE_2026-11-03.csv\` (no screened studies yet).
- **Equation/data extraction:** \`SYSTEMATIC_REVIEW_EXTRACTION_TEMPLATE_2026-11-03.csv\` (no source-level reviewed entries yet).
- **Prior physical/data evidence:** Report 1 and source-specific audits indexed in existing README.

**Version-control instructions:** add new run-specific logs rather than modifying blank templates; preserve retrieved RIS/BibTeX exports locally or in approved private storage; do not upload copyrighted full texts to public GitHub; use fixed source DOI and retrieval dates, record exact reason for every assumption and every blocked task; amend checkpoint with actual progress but do not change percentage merely from tasks being listed.

## 8. Completion criteria in one sentence

We can tell Professor Phelan that his request has been met **only after** we can show a traceable, reproducible review of what others have done, an evidence-bounded novelty statement, and a defensible empirical-data-supported **physics versus PIML/PINN decision** with independent validation or a clearly justified physics-only fallback.

**Neither a longer reading list nor a large row count alone meets the request.**
