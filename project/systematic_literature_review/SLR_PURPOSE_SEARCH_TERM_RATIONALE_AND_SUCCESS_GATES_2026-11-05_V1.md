# SLR Research Purpose, Search-Term Rationale, Expected Evidence and Measurable Acceptance Gates

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Controlled supplement:** SLR-PURPOSE-KEYWORDS-GATES-2026-11-05-V1 | **Date:** 5 November 2026  
**Status:** PROPOSED, source-grounded protocol supplement for researcher/supervisor/search-specialist approval. NOT a claim that native A–F searches have been executed, independently screened or preregistered.  
**Related controlled execution audit:** [SLR methods, execution history and completion protocol, V1](./SLR_METHODS_EXECUTION_AUDIT_AND_COMPLETION_PROTOCOL_2026-11-05_V1.md).  
**Scope authority:** Frozen thermal Power–Electrified Transportation physical state-time SO1–SO3 under extreme heat. Do not introduce a new objective or silently broaden to water or other network types. This document clarifies literature-search decisions; it does not replace or retroactively amend an executed query.

## 1. Why are we doing the review?

### 1.1 Scientific problem—not a paper-count target
Heat changes operating capabilities of both electrical supply and electrified transport. Electrical loading generates transformer heat; ambient conditions and cooling determine thermal state evolution; thermal limits can constrain supply or charging power. EVSE converter and battery temperatures also determine feasible charging. When equipment responds to a limit, energy delivered or vehicle departure readiness may change. However, **a component temperature, a component capacity, an implemented control restriction, a delivered-energy shortfall and a mobility-service failure are different things**. The review must discover which links have physical evidence and which are only modeled.

**Overarching review question:** Which physical thermal mechanisms, governing equations, state variables, parameter sources, characteristic timescales, operational restrictions, and electricity/mobility service consequences in coupled power–electrified transportation systems have been proposed, measured or validated under high ambient temperatures or related operating conditions?

**Purpose:** (i) map physical directional interfaces and qualification of measurement (SO1); (ii) identify defensible first-principles mathematical descriptions and empirical identifiability/validation (SO2); (iii) determine what is evidenced about thermal state-to-restriction-to-service delays and outcomes (SO3); (iv) search specifically for contrary prior art that could invalidate any novelty claim; (v) determine whether physics-only or physics-informed learning is justified by actual data.

**Not our purpose:** establish a predetermined global literature gap; declare novelty based on incomplete searches; use publication counts as a proxy for rigor; include an article because it supports a desired thesis narrative; infer missed trips from charging-energy shortfalls; equate numerical simulations with observed field service; or require PINNs merely because they are fashionable.

### 1.2 Why a two-tier design instead of one narrow meta-analysis?
- **Tier 1: systematic scoping/evidence map.** A broad, heterogeneous engineering evidence base includes standards, measured field/lab work, thermal ODE/PDE models, simulations, reviews and mathematical algorithms. We need to map concepts, evidence strata, methods, configurations and gaps, not pool incompatible effects.
- **Tier 2: focused mathematical and validation synthesis.** From eligible primary sources, we will compare dimensional equations, assumptions, temporal/spatial scales, boundary conditions, calibration, identifiability, baseline performance, uncertainty and service claims. It is more exacting than merely charting themes. The primary systematic scoping report follows JBI conduct and PRISMA-ScR; search reporting follows PRISMA-S. A separate conventional systematic-effect estimate/meta-analysis is NOT promised.
- ASU Library explains that scoping reviews are suited to mapping available evidence, clarifying concepts, identifying characteristics and gaps; protocols predefine methods and amendments must be documented.
  [ASU review type](https://libguides.asu.edu/evidence_synthesis/scoping-review) | [ASU protocol](https://libguides.asu.edu/evidence_synthesis/protocol) | [JBI review question alignment](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862687).

## 2. PCC and eligibility logic: why these boundaries?

| Element | Intended inclusion logic | Why essential | How coverage is checked |
|---|---|---|---|
| Population/system | Electrical distribution transformers/feeders and electrified road-transport charging equipment (EVSE), EV battery/vehicle/fleet. Some qualifying stand-alone component work belongs in a SUPPORTING stratum. | Captures both directions of the physical interface without requiring every paper to instrument the entire chain. | Every included source explicitly identifies an equipment scale and system role; "connected" claimed only if topology verified. |
| Concept | Temperature-dependent thermal dynamics, losses/heat transfer, thermal rating, cooling/derating, control, constraint propagation, time-resolved charging and service. | Physical **state, capacity, action and service** must be separated. | Every claim is tagged by mechanism and evidence level; thermal variables and boundaries recorded. |
| Context | Extreme heat/high ambient first; general-purpose seminal transformer/EVSE thermal laws retained as supporting physics even when experiments are not hot-weather. Field, lab and simulation are separate evidence strata. | A heat-only keyword requirement would miss necessary governing laws and earlier contrary inventions. | Each source records heat exposure and whether observed, imposed, simulated, or unreported. |
| Evidence design | Primary field/lab/validated simulations, methods and numerical papers; reviews/standards in contextual/methodological strata; grey literature with provenance. | No single research design answers all objectives. | Unique source/report/study-family IDs; no review counted as an independent field experiment. |

**Primary inclusion does not require the words "resilience", "extreme heat", "PINN", or "interdependency" in the title.** Concepts may be demonstrated without these labels. The strict connection status is an extraction variable, not a universal hard title/abstract exclusion.

## 3. Search design: why advanced, and how to test it

**JBI three-step reasoning**: Step 1, find and verify seed references and harvest actual author keywords/index terms; Step 2, build and peer-review the main source-specific query, iteratively confirm retrieval of *known indexed* seed papers, translate it to other platforms; Step 3, citation chasing, standards/grey literature and targeted handsearching. [JBI 3-step](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/653099013/2.4.2%20The%20JBI%203-Step%20Search%20Process).

- **OR** groups synonyms of one concept (avoids requiring an author's exact preferred term).
- **AND** intersects two/three meaningful concepts, increasing relevance but risking misses. Every highly intersected query needs a broader companion query.
- **Quoted phrases** preserve a phrase, but plurals/hyphens/word order may differ by database; pilot both phrase and alternate forms.
- **Truncation/proximity** is database-specific; only apply after testing it. For example, \`thermal rating\`, \`dynamic rating\`, \`DTR\` overlap but DTR is ambiguous.
- **Field-coded searches** (Scopus TITLE-ABS-KEY; Web of Science TS; IEEE/Compendex native fields) must be verified separately; do not claim one syntax works universally.
- **Never AND A through F together**: each block answers a different subquestion, and doing so could exclude most relevant component physics and field evidence.
- Do not use \`NOT thermal\` or \`NOT transportation\` to shrink hits. Review titles/abstracts against eligibility, and log test exclusions.
- **PRESS search peer review** checks question translation, Boolean operators, subject headings/text terms, syntax/line numbers and filters before execution: [PRESS 2015](https://pubmed.ncbi.nlm.nih.gov/27005575/).

### 3.1 Why each concept / keyword is used
The full one-term/one-decision machine-readable record is in the companion \`SLR_KEYWORD_DECISION_MATRIX_2026-11-05.csv\`. Terms below are proposed master concepts; the final verbatim database syntax requires index-term harvesting and specialist check.

| Concept family | Why these words | False-negative/false-positive issue |
|---|---|---|
| Electrical equipment: "distribution transformer", "power transformer", transformer, feeder, substation | Locate actual heat-generating assets, winding/oil states and loading constraints. | "Power transformer" may mean upstream transmission assets; feeder/substation alone can be electrical-only. Require equipment classification during screening. |
| Transport charging: "electric vehicle", EV, "EV charging", "charging station", EVSE, "electric bus depot", "fast charger", "DC charger" | Capture load direction T→P, supplied charging P→T, asset types and charging service. | EV can be ambiguous; charging station can be a fleet or generic facility; "DC charger" can include nontransport applications. |
| Thermal state: thermal, temperature, "hot spot", hotspot, "top oil", "winding temperature", rectifier, cooling, "heat equation" | Identify the state equations and physical heat pathway. | Temperature may denote only battery ambient or meteorological correlations. Extract which state and actual sensor. |
| Ambient hazard: "ambient temperature", "high temperature", "extreme heat", heatwave, "hot arid", cooling, climate | Test ambient-dependent derating and physically relevant hazard range. | "High temperature" may mean materials processing; heatwave-only filtering misses general model laws. |
| Rating and restriction: derating, "dynamic thermal rating", DTR, "thermal limit", offered power, delivered power, current limit, aging | Connect physical state to feasible power and implemented decisions. | "Aging" alone may capture accelerated life with no operational restriction; DTR sometimes cable-only. |
| Field credibility: "field measurement", monitoring, metered, experiment, instrumented, sensor, real-world | Prioritize topology and original measured observables, not assumed links. | Many empirical articles omit "field" in abstracts. Keep broader site searches. |
| Service and system-of-systems: "power-transportation", coupled, interdependent, resilience, recovery, cascading, service, arrival, departure, SOC, charging demand | Seek dynamic propagation and observed vehicle/service outcomes, not just kW. | "Resilience" captures storms/cyber papers that have no thermal pathway; departure timestamps may be simulated. |
| Numerical modeling: ODE, PDE, "heat transfer", "finite volume", FVM, "physics-informed", PINN, "neural operator", hybrid, "parameter identification" | Compare physics first-principles, discretization, inverse problems and data-driven alternatives. | General PINN articles may have no transformer/EVSE application; a physics loss alone is not an independent validation. |
| Standards: "IEC 60076-7", "IEEE C57.91", "transformer loading guide", "battery thermal model" | Trace accepted thermal baseline assumptions and rating calculations, independent of new techniques. | Standards are not field validations; versions, asset applicability and access rights must be documented. |

## 4. Search blocks A–F: explicit rationale, expected evidence, success test

### A — Transformer heat and charging loads (SO1, SO2, SO3)
**Question:** How does EV charging load alter transformer thermal state and potentially charging capacity or aging?
- **Why concepts:** transformer identifies oil/winding asset; EV/charging identifies electrical load interface; temperature/hotspot/dynamic rating identifies physics and possible operational response.
- **Focused core example:** \`("distribution transformer" OR "power transformer") AND ("electric vehicle" OR "EV charging" OR EVSE) AND (thermal OR temperature OR "hot spot" OR "top oil" OR "dynamic thermal rating" OR aging)\`.
- **Broad companion A0:** \`("transformer" AND ("top oil" OR "winding temperature" OR "hot spot" OR "thermal model" OR "heat run"))\`; exclude irrelevant transformers only during screening. This retains physically foundational papers with no EV term.
- **Seed tests:** Fletcher–Khan 2025 report (supplement/grey), Gong 2015 DOI 10.1109/TSG.2014.2365452, Hilshey 2013 DOI 10.1109/TSG.2012.2217385, Pan 2025 DOI 10.1049/hve2.70024.
- **Expected evidence (not guaranteed):** ODE/PDE or IEC/IEEE dynamic load/thermal relations, thermal time constants, measured-vs-simulated temperatures, charging control thresholds, energy delivered, independent load tests.
- **Pass:** search retrieves relevant *indexed* seed(s) or documents precisely why not; eligible included A studies have source pages, physical asset model and validation classification. No fabricated field connection.

### B — EVSE thermal derating and ambient (SO1, SO2, SO3)
**Question:** Do ambient and internal power-electronics temperatures cause offered charging power limits, distinct from EV battery acceptance?
- **Why concepts:** charger/rectifier locates charging device; heat/ambient locates thermal excitation; derating/offered power/efficiency captures operational consequence.
- **Focused B1:** \`("fast charger" OR "DC charger" OR EVSE OR rectifier) AND ("ambient temperature" OR "high temperature" OR "extreme heat" OR heatwave OR cooling) AND (derating OR temperature OR "offered power" OR efficiency)\`.
- **Broad B0:** \`("EVSE" OR "DC fast charging" OR "charging converter") AND (thermal OR cooling OR temperature)\`. Do not insist that every empirical study literally says "derating".
- **Seeds:** Krama et al. 2026 DOI 10.1016/j.ecmx.2026.101960 and potential Sezer/Bayhan 2025 Qatar conference predecessor (study family to be checked).
- **Expected:** ambient and rectifier sensor location/time series, thermal thresholds or internal derating commands, offered vs delivered output, SOC/vehicle BMS confounders, energy/service times, uncertainty.
- **Pass:** distinguish charger thermal control from battery taper and grid curtailment; raw/abstract/fulltext access status truthful.

### C — Physically connected transformer–charger field site (SO1–SO3)
**Question:** Has a single site measured enough synchronized variables to establish transformer→EVSE or EVSE→transformer causal thermal propagation?
- **Why concepts:** charging station/depot identifies mobility load; transformer/feeder identifies supply asset; measurement terms prioritize observed data; topology is a verification condition.
- **Focused C1:** \`("charging station" OR "electric bus depot" OR EVSE) AND (transformer OR feeder OR substation) AND ("field measurement" OR monitoring OR experiment OR metered)\`.
- **Broad C0:** \`("bus charging" OR "charging station" OR "charger") AND ("distribution transformer" OR "power quality" OR "electrical monitoring")\`; trace the full text regardless of missing "field".
- **Seed:** Li, Chang & Lu 2026 DOI 10.1109/PESGM58988.2026.11693150 (public electrical site abstract; full thermal channels not verified).
- **Expected:** a physically documented single-line diagram/site asset IDs, common clock, load/current, ambient, transformer top-oil/hotspot, EVSE rectifier temp, limit/intervention log, charger offered/delivered power and mobility deadlines.
- **Pass:** explicit matrix of each sensor present/absent, synchronization and measured-vs-inferred channels; results may legitimately reveal NO complete same-site data. Absence from a bounded search is **not** proof nobody has ever measured it.

### D — Coupled system dynamics and resilience (SO1 and SO3)
**Question:** What is known about bidirectional dependency, state transitions, restriction propagation, service consequences and recovery?
- **Why concepts:** power-transportation/coupled locates network interaction; resilience/recovery/cascading/service locates temporal performance; thermal/EV terms can be applied as a *second narrower search*, not as mandatory first-pass filters.
- **D1:** \`("power transportation" OR "power-transportation" OR "coupled electricity transportation" OR "electricity transport interdependency") AND (resilience OR recovery OR service OR cascading OR dynamic OR thermal)\`.
- **D0 companion:** \`("electric vehicle charging" OR "charging network") AND (delay OR curtailment OR "departure time" OR "unserved energy" OR service)\`; permits service models not labeled "resilience".
- **Expected:** dependency direction, transition onset and delay, SOC/demand/required vs delivered energy, exact definition of service loss/recovery, direct measurement versus optimized-scenario estimates.
- **Pass:** all modeled outages and service metrics labeled model vs field; cross-study SO3 inference cannot be presented as a site observation.

### E — Physics-informed thermals and identification (SO2)
**Question:** Under what data and comparison conditions do physics-informed learning methods improve or fail versus pure-physics ODE/PDE/FVM or persistence?
- **Why concepts:** PINN/physics-informed/hybrid identifies trained constrained algorithms, transformer/battery/charger defines application, heat equation/parameter identification identifies governing physics and inverse problem.
- **E1:** \`("physics-informed" OR PINN OR "neural operator" OR "hybrid physics") AND (transformer OR "EV battery" OR charger OR "battery thermal") AND (temperature OR "heat equation" OR "parameter identification")\`.
- **E0 companion:** \`(transformer OR charger OR "battery thermal") AND ("thermal model" OR "finite volume" OR "parameter identification" OR "heat transfer")\`. Include strong physics-only negative results.
- **Seed:** Bragone et al. 2022 DOI 10.1016/j.epsr.2022.108447; EV battery thermal measured-model reference Acker 2025/2026 DOI 10.1007/s41104-025-00157-7 (not PINN seed).
- **Expected:** state PDE/ODE, physical residual, measured boundary conditions, data volume, loss weights, parameter anchor/identifiability, baseline match, held-out asset/time regimes, UQ.
- **Pass:** no physics-informed recommendation without fair measured-data baseline and identification of leakage/confounding.

### F — Standards and validated physics baselines (SO2)
**Question:** Which accepted physical and measurement standards define permissible transformer thermal behavior and equations?
- **Why concepts:** IEC 60076-7 and IEEE C57.91 identify governing transformer thermal guide families; validation/measurement/loss/cooling identify parameter and empirical relevance.
- **F1:** \`("IEC 60076-7" OR "IEEE C57.91" OR "transformer loading guide" OR "dynamic thermal model" OR "battery thermal model") AND (validation OR measurement OR loss OR time OR cooling)\`.
- **F0 companion:** original standard documents and citations from validated primary papers (standards may not have titles indexed in bibliographic databases).
- **Expected:** edition-appropriate definitions for top-oil/hotspot, loss ratios, exponents and thermal constants; material/asset boundaries; laboratory/field measurement practices; allowable claims.
- **Pass:** standard year/edition, clause/page if accessible, asset applicability and assumed-vs-measured parameter list. Standards do NOT count as independent empirical validation.

## 5. What counts as review success? Predeclared, measurable checks

| Gate | Measure / formula | Acceptance rule (prospective, to approve) | Evidence |
|---|---|---|---|
| G0 Goal alignment | mapped review questions / total questions; every SO covered | 6/6 SLR questions mapped and SO1–SO3 fully traceable before execution | question→PCC→block→extraction crosswalk |
| G1 Keyword traceability | documented terms / terms in actual queries | 100% of executed significant terms have a scientific rationale, synonyms tested, and reason for inclusion/exclusion | versioned term dictionary |
| G2 Known-seed recall | retrieved *indexed and eligible* test seeds / eligible indexed seed total | Aim for 100% known-indexed seed capture over all applicable searches; record each failed seed, database coverage issue and amendment. Never claim population-wide recall. | seed DOI, source platform, query log, retrieval outcome |
| G3 Native provenance | executed database searches with exact fields/date/query/hits/raw export/hash / total executed | 100% of searches in claimed core databases documented; unavailable access labeled unavailable, NOT searched. No invented hit counts. | verbatim export manifest, SHA-256, platform screenshots if allowable |
| G4 Dedup correctness | unadjudicated duplicate-family groups; lost source IDs | zero unresolved families at PRISMA freeze; zero dropped provenance; confirm differing versions/experiments manually | duplicate decision audit and source crosswalk |
| G5 Screening completeness | records with final human eligibility / all screened records | 100% final decision and reason as applicable; genuinely independent reviewer where protocol requires; otherwise explicit single-reviewer deviation. | reviewer1/reviewer2 timestamps, reconciliation |
| G6 Screening calibration | pilot % agreement = agreements / total pilot; optionally Cohen's kappa | pilot 25 diverse records; report agreement and resolve definitions; JBI commonly references ≥75% calibration agreement, but not proof of scientific validity. No retroactive pass threshold. | initial independent ballots and discrepancy log |
| G7 Full-text eligibility | reports assessed or explicitly not retrieved / reports sought | Every eligible potential source has verified original access status, full-text decision and reason; no unknown status turned into an exclusion silently | source PDF/URL/access logs, reason codes |
| G8 Mathematical extraction | full extracted primary included studies / primary included studies | 100% charted with model equations, dimensions, assumptions, parameter origin, temporal scale and validation status, or explicit NOT_REPORTED | pages, equations, data sheets and double-check |
| G9 Claim quality | substantive claims with precise original evidence / substantive review claims | 100% source-backed; distinguish measured field, laboratory, numerical, abstract-only and inference. "UNKNOWN" where not established. | claim/figure/equation citation trace |
| G10 Thermal causal evidence | proportion of studies with independently verified full site chain | **Descriptive fraction, NOT target ≥1 study.** Zero is possible and cannot alone prove global novelty. Record sensor/topology/time/control/service completeness for each | connectivity × thermal sensors × intervention × service matrix |
| G11 Physics/PINN method | matched leakage-safe benchmark available and comparable | Conditional: recommend PIML only if original data and matched baselines permit; otherwise physics-first with limits. Never fabricate validation | source conditions, matched test metrics, UQ |
| G12 PRISMA accounting | source records→duplicates→screened→fulltext→included arithmetic reconciles | Every count auditable, no mixing historical Q0, preliminary V5 triage and formal current-protocol results | PRISMA-ScR + PRISMA-S appendix |
| G13 Independent QA | review of claims and searches by qualified other person | Actual reviewer identity and scope documented; if absent mark open, not "independently validated" | signed/dated adjudication or recorded exceptions |

### 5.1 Do not use these as success metrics
- **Number of found articles** (no scientifically required minimum such as 100).
- **Number of articles confirming novelty** (invites confirmation bias).
- **High percentage exclusion** (could mean a flawed query).
- **A perfect-looking PRISMA diagram** without the original logs.
- **A model's small RMSE in a leakage-prone time split** or low simulated service loss treated as validation.

### 5.2 Performance diagnostics for search tuning—not final review claims
1. **Seed recall:** \`R_seed = n_known_indexed_retrieved / n_known_indexed_eligible\`. Define inclusion of every seed *before* running the candidate query, record whether each database actually indexes it and its searchable metadata.
2. **Pilot precision:** \`P_pilot = n_relevant_in_handchecked_sample / n_handchecked_sample\`. Useful for workload only; any sampling method and denominator must be specified. It does not estimate full-population sensitivity.
3. **Incremental yield:** \`Y_block = n_new_eligible_from_block / n_records_screened_from_block\` after formal decisions. Compare broad/focused query pairs; don't drop low-yield blocks if they supply unique physics or contrary evidence.
4. **Reviewer agreement:** \`A = n_agreed / n_double_screened\`, alongside raw category table and optional chance-corrected kappa if suitable.
5. **Evidence-chain observability:** list the six critical site variables (topology; transformer thermal; EVSE thermal; ambient/forcing; logged control; electricity/mobility service), each present measured / estimated / absent. A low fraction is an outcome, not a failed review.

## 6. What exactly is expected from each paper?

For every formally eligible report, chart:
- Bibliography and immutable source: canonical record ID; study-family ID; DOI; title/year/venue; URL; original source path; pages/section/figure; report version.
- Equipment and scale: transformer type/nameplate/oil/winding, feeder connection, DC/AC EVSE topology, charger converter, vehicle/battery, cooling configuration.
- Directional interface: T_e→P current/load/heat and P→T_e available charging supply/thermal limit; direct physical link verified/assumed/absent.
- **Physical state:** \`T_o(t)\`, \`T_h(t)\`, \`T_rectifier(t)\`, \`T_battery(t)\`, SOC, current, and ambient. Note sensor-vs-derived-vs-synthetic values.
- **Equations and units:** balance law, time constants, boundary conditions, discretization, parameter identification, cooling controls, physical dimensionality and parameter confidence.
- **Events and times:** disturbance onset; thermal threshold crossing; command; power change; energy request/delivery; vehicle departure; recovery. Distinguish field-observed event times from model-generated ones.
- **Validation:** held-out times/equipment, persistence/physics/FVM comparisons; error and uncertainty; data leakage and calibration limits; sensitivity under extreme heat.
- **Consequences:** immediate power constraint vs energy shortfall vs true missed transport service (actual-trip data needed); status of sustainable electricity/mobility implications if evidence supports them.
- **Counterexamples:** closest paper that did this already; which part of the proposed contribution it invalidates; what remains open without overclaiming.

Do not convert an abstract claim into an exact physical equation until full original source is inspected. Positive and contradictory evidence receive identical evidence-grade treatment.

## 7. Pre-execution decision test for each proposed keyword

Log the following fields **before** final search execution for each keyword/synonym:
\`term_id, search_block, concept, exact_term, alternative_term, reason_inclusion, expected_relevant_sources, risk_false_negative, risk_false_positive, seed_support, pilot_hit_count, measured_seed_capture, proposed_disposition, approver, protocol_version\`.

Decision rule:
1. Does this term represent a *physical asset, state, forcing, method or service consequence* needed by an SO?
2. Which known seed report uses it in title, abstract, keywords or indexed subject field? If not in seeds, is theoretical/terminological justification explicit?
3. What becomes invisible if the term is removed? Run a search ablation or seed-retrieval test.
4. What unrelated papers does it create? Test precision on an independently reviewed sample.
5. Does a broader companion search protect relevant studies? If not, revise the query.
6. Record final decision, reasons, date and reviewer. **If changed after execution, log an amendment; never pretend it was prespecified.**

## 8. Traceable deliverables and current factual status

**Completed and verified in earlier project audit:** historical Q0 provenance 687 raw records (Scopus 253/IEEE 189/Compendex 245) and 404 historical deduplicated; 533 original GitHub master; Library V5 indexed 590 with 57 appended IDs; no DOI/title/relevance changes in 533 matched; 16 title-family duplication issues and 74 year discrepancies; 590 preliminary title/abstract labels (98 advance/126 background/259 preliminary exclude/107 uncertain); two source-reading batches and targeted public-search access log. None of these are formal final study-inclusion counts.

**Still NOT achieved:** original V5 XLSX byte-level hash; complete current-protocol native database A–F queries/exports; study-family verification; independently adjudicated screening; complete original full-text data extraction; PRISMA-ScR arithmetic; global prior-art novelty test; experimental end-to-end transformer/charger/service validation.

**Researcher action order:** approve objectives/PCC/eligibility/keywords and their nontrivial ambiguities → run small seed tests and independent PRESS review → execute original platform-native A–F broad/focused queries, preserve exports/checksums → reconcile full master and 16 duplicate families → independent human title/abstract decisions → full-text reading and reason-coded exclusions → claim-level mathematical synthesis → validated final PRISMA report and science-method decision.

### Source-and-authority trail (accessed 2026-11-05)
1. ASU Library, Scoping Reviews: https://libguides.asu.edu/evidence_synthesis/scoping-review
2. ASU Library, Protocol Development: https://libguides.asu.edu/evidence_synthesis/protocol
3. ASU Library, Search Documentation: https://libguides.asu.edu/evidence_synthesis/search-strategy
4. JBI Manual, 10.2.3 rationale for scoping review protocol: https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862687
5. JBI Manual, 2.4.2 three-step search: https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/653099013/2.4.2%20The%20JBI%203-Step%20Search%20Process
6. PRESS 2015 peer-review search strategy: https://pubmed.ncbi.nlm.nih.gov/27005575/
7. PRISMA-S 2021 (16 search-reporting items): https://doi.org/10.1186/s13643-020-01542-z
8. PRISMA-ScR: https://www.prisma-statement.org/scoping
9. Project: \`CURRENT_THESIS_AUTHORITY_INDEX_V1.md\`, current SLR methods audit V1, V5 crosswalk and paper reading batches 01–02 at branch \`user-data-qualification-2026-11-03\`.

**Provenance rule:** This is an explicitly proposed addition to an existing internally drafted protocol. It is NOT presented as preregistered, supervisor approved or executed. Final search acceptance thresholds and amendments require their own approval dates and identities.
