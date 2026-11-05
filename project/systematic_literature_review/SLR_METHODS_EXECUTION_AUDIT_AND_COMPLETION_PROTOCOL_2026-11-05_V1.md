# SYSTEMATIC LITERATURE REVIEW
## Methodology, execution history, provenance audit, and completion protocol

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Research focus:** Thermal interdependencies under extreme heat; physical state and time; electricity and mobility services  
**Document ID:** SLR-METHODS-AUDIT-2026-11-05-V1  
**Issue date:** 5 November 2026  
**Status:** **Controlled working record — retrospective audit plus prospective completion plan. NOT a completed systematic review, preregistered protocol, externally approved method, or final PRISMA report.**  
**Authority:** Current thesis title/scope/GO/SO1–SO3 are governed by the project’s existing canonical authority files. This document records review execution only; it does not amend the thesis objectives.  
**Repository working branch:** `user-data-qualification-2026-11-03`, `Dossiya-SE/MSE-thesis`  
**Proposed custodian:** Thesis researcher; supervisor and reviewers to be identified and recorded, not inferred.

---

## EXECUTIVE RECORD: WHAT THIS DOCUMENT IS

This document combines **(A) a retrospective, provenance-bound record of work already performed** with **(B) an executable protocol for work not yet performed**. Those sections must remain distinct. Historic retrieval, AI-assisted triage, content-level workbook reconciliation, public web discovery, primary-source reading, final eligibility decisions, and independently validated experimental evidence have different evidentiary meanings. The review must not be presented as complete until all defined gates have evidence of closure.

The planned review has two linked tiers, following the existing proposed review protocol. **Tier 1** is a systematic scoping review/evidence map of physical, mathematical, numerical, field and laboratory evidence for the power–electrified transportation interface. **Tier 2** is an equation- and validation-focused critical synthesis of eligible primary studies. Conduct guidance is adapted from JBI's scoping-review manual, reporting is mapped to PRISMA-ScR and PRISMA-S, and relevant prospective protocol items are checked against PRISMA-P. The adaptations to engineering evidence—multiple model families, standards, simulation studies, experimental platforms and measured versus modeled service—must be stated transparently (JBI, 2024/2026; Tricco et al., 2018; Rethlefsen et al., 2021).

**ASU-specific verification.** ASU Library emphasizes protocol planning, explicit and translatable searches, retention of database/platform/search-date/search-string/filters/results, complete original exports, deduplication audit, independent screening and documented amendments. ASU Library also states that PRISMA checklists guide **reporting**, rather than serving as the review's conduct methodology (Arizona State University Library [ASU Library], n.d.-a–d). ASU Graduate College provides separate formatting requirements for eligible theses/dissertations; an **applied project or other non-thesis culminating event does not automatically require Graduate College format approval**. The researcher should verify the actual MSE culminating-event classification with the advisor; do not assume every engineering research report is an ETD (ASU Graduate College, n.d.).

## 1. SCIENTIFIC PURPOSE AND RESEARCH BOUNDARY

### 1.1 Fixed research purpose

**General objective (GO).** Characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat; quantify how their consequences evolve through physical state and time.

**SO1 — mechanism and evidence:** identify and qualify thermally sensitive physical states and directional thermal interdependency mechanisms connecting the two systems.  
**SO2 — mathematical dynamics:** develop a physics-based state–time model of qualified thermal interdependencies and propagation under extreme heat.  
**SO3 — consequences:** quantify critical transition times, interdependency propagation delays and resulting electricity and mobility service consequences.

Power and electrified road transportation are the physical core; information, price, organization and control may be documented as supporting mechanisms but are not permission to expand to new core systems. Heat is the active disturbance. Distinguish **state** (measured/modelled physical variables), **capability** (possible performance under limits), **service** (delivered electricity/mobility), and **resilience** (service behaviour through disruption and recovery). Do not label a simulated energy curtailment as a measured missed trip.

### 1.2 Review questions, inherited rather than redefined

- **SLR-Q1 / SO1:** Which direction-specific thermal/electrical pathways P→Tₑ and Tₑ→P are described versus physically observed? Is electrical connectivity established?
- **SLR-Q2 / SO2 physics:** Which transformer, EVSE, battery and feeder heat/electrical equations, constitutive relations, boundary conditions, thermal time constants and parameter sources are used?
- **SLR-Q3 / SO2 data:** Which state variables and forcing terms are actually measured, under what sensors, sampling periods, sites and ambient conditions; what is identifiable or validated?
- **SLR-Q4 / SO2 methods:** Under what independently tested conditions does a physics-based ODE/PDE/FVM baseline perform differently from a gray-box, PINN or other physics-informed model?
- **SLR-Q5 / SO3:** Which charging-power, delivered-energy, thermal-limit, departure/deadline, transition, delay and recovery consequences are measured rather than simulated?
- **SLR-Q6 / novelty challenge:** Which closest original studies already demonstrate these connections? What alternative studies falsify a proposed novelty statement?

No pre-emptive “first-ever” claim is permitted. The review asks what is established or missing, not how to prove a preferred thesis novelty.

### 1.3 Proposed eligibility boundary requiring documented approval

**Population/context:** distribution transformers/feeders, electrically connected EV charging stations (EVSE), electric-bus depots, EV/battery systems, and associated mobility/energy service where relevant.  
**Concepts:** thermal state/time, dynamic thermal rating, hotspot/top-oil, charger rectifier cooling/derating, battery thermal acceptance, thermal-induced power restrictions, interdependency propagation, physical mathematical models and their validation.  
**Context:** extreme heat as focal hazard; standard or moderate-temperature studies remain eligible as physical/methodological comparators, labelled by applicability.  
**Evidence sources:** primary journal and conference papers, original technical reports, measured field/lab studies, modeling studies with equations and explicit validation, authoritative standards and data descriptors; preprints/theses/reviews retained in separate evidence strata.  
**Temporal plan:** search 2000 through the fixed protocol cutoff, with earlier foundational studies through citation chaining; update searches on a separately logged date.  
**Language:** no automatic exclusion where translation is feasible; document restrictions.  
**Exclusion principle:** wrong physical system, no defensible thermal/method/service relevance for any review question, nontraceable secondary assertion. A study that challenges novelty is not excluded merely because its result is inconvenient.

The current project protocol is an **internal proposed protocol**, not externally registered, approved, or retrospectively pre-registered. The review team must record whether the original 2026-11-03 cutoff is retained or amended when formally initiating native searches.

## 2. METHODOLOGICAL AUTHORITIES AND ASU COMPLIANCE CROSSWALK

| Authority | What it governs in this project | Documentation/acceptance rule |
|---|---|---|
| ASU Library — protocol | Written plan, transparent amendments, selection of review type | Date/version each protocol; disclose that initial research predates formal prospective lock |
| ASU Library — search strategy | Sensitive, reproducible search; seed recall; platform translation | Preserve a multi-line concept build and the verbatim final database query for each A–F block |
| ASU Library — exporting and citation management | Original raw exports, RIS/CSV, import count and de-duplication trail | File counts/hashes and provenance survive de-duplication; verify true duplicate study families |
| ASU Library — appraisal | Trained, independent title/abstract/full-text decisions and reconciled disagreements | Separate human reviewer logs, pilot, adjudication and reason-coded exclusions |
| JBI Manual, scoping review | PCC and transparent conduct of searching, selecting, extracting and presenting | Follow a prespecified method; log all changes and actual reviewer configuration |
| PRISMA-ScR (Tricco et al., 2018) | Final scoping review reporting items | Fill checklist with exact manuscript section/page and supporting artifact |
| PRISMA-S (Rethlefsen et al., 2021) | Reproducible literature search reporting | Database/platform, full search, limits, dates, peer review of search, source counts and updates |
| ASU Graduate College | Thesis/dissertation *formatting* only when applicable to program and culminating event | Confirm MSE route; use ASU Format Wizard and manual only if actual format review applies |

**Do not mislabel:** a PRISMA checklist is not a replacement for a review protocol; an internally dated protocol created after preliminary screening is not a prospectively registered protocol; a paper's claim of experimental validation is not automatically experimental validation of the full connected P–T system.

## 3. EVIDENCE STATUS VOCABULARY AND CONTROL RULES

Use **VERIFIED / PARTIAL / PROVISIONAL / NOT STARTED / BLOCKED / NOT APPLICABLE**. Status must attach to a named artifact and the specific operation; never to a whole review by implication.

- **VERIFIED:** original artifact or authorized content read, operation checked, reproducible results recorded; caveat exact access (raw binary versus indexed text).
- **PARTIAL:** some original methods/results checked but equations, figures, independent data or full set unavailable.
- **PROVISIONAL:** inferred relevance, AI-assisted screening, preliminary numerical output or undecided eligibility.
- **NOT STARTED:** explicitly no executed action under the current protocol.
- **BLOCKED:** action attempted but unavailable; store cause, owner and possible workaround.
- **NOT APPLICABLE:** justified reason and reviewer, never use to hide missing data.

For each quantitative number label **unit of analysis**: exported hit, bibliographic record, linked source report, independent study, laboratory experiment, simulation scenario or measured site. No count can be substituted for another.

## 4. RETROSPECTIVE EXECUTION HISTORY — DONE VERSUS NOT DONE

### H0 — Original literature acquisition and Q0 provenance (historical; partially reconstructed)

**Previously recorded:** 687 raw provenance entries collected in three historical database streams: Scopus 253, IEEE 189 and Compendex 245; a historical deduplication yielded 404 records. A 200→26 prioritization exercise was recorded. The earlier exports and historical logs are referenced by the November 5 inventory. **Not established for the present review:** native, complete, precisely translated A–F queries; original current search dates/hit limits/hashes and a formal PRISMA denominator. Treat the 687 as a historical inventory, not additive to the 590.

**Sources:** `project/THESIS_RESEARCH_FULL_INVENTORY_AND_ROADMAP_2026-11-05.md`; Q0 provenance files cited therein.

### H1 — Research scope and conceptual/methods development (historical → 2026-11-03)

**Done:** frozen thesis title and scope authority, GO/SO1–SO3, LQ1–LQ6 review questions, literature-to-physics crosswalk, JBI/PCC-derived internal screening plan. An executable systematic review protocol v0.2 was dated 2026-11-03.

**Still open:** reviewer/supervisor approval, prospective amendment record, full platform-native implementation, public protocol registration if chosen. It would be scientifically inaccurate to backdate public registration to before pilot triage.

**Source:** `project/data_qualification/2026-11-03/SYSTEMATIC_REVIEW_EXECUTION_PROTOCOL_V02_2026-11-03.md` (**PROPOSED, NOT FROZEN**).

### H2 — GitHub bibliographic master and V5 enrichment

**Verified master on GitHub:** 533 canonical IDs `LIT-0001` through `LIT-0533` at `project/systematic_literature_review/MASTER_SYSTEMATIC_LITERATURE_REGISTER_V01.csv`. 498 populated distinct DOI strings, 35 blanks.

**Located V5:** the Library entry `/My thesis/Unified_Thesis_Research_Master_V5_Reconciled_2026-11-04.xlsx` has a 554,533-byte source file, version 2, with 31 indexed tabs. The Master Literature tab was parsed from **indexed text**; original `.xlsx` binary materialization failed. The content-level audit found 590 canonical records, 555 distinct populated DOI strings, 35 blank DOI fields. The 533 prior IDs match on title, DOI and relevance class; 57 newer IDs `LIT-0534` through `LIT-0590` have been separately preserved in a crosswalk. These extra bibliographic rows do **not** establish 57 new independent studies.

**Additional unresolved checks:** 16 pairs with identical normalized titles (different/missing DOIs, including preprint/conference/journal versions) and 74 year-field differences (73 blank→`TO VERIFY`, one `LIT-0003` 2024→`TO VERIFY`). No automatic merge or source-year overwrite was performed.

**Source:** `project/data_qualification/2026-11-03/V5_RECONCILIATION_AUDIT_2026-11-05_V2.md` and the three companion CSV audit files. **Binary SHA-256 for V5 is NOT verified.**

### H3 — Initial relevance and title/abstract triage (single AI-assisted preliminary pass)

The recorded V5 preliminary triage spans 590 rows: 98 `ADVANCE_FULLTEXT`, 126 `SECONDARY_BACKGROUND`, 259 `EXCLUDE_TA_PROVISIONAL`, and 107 `UNCERTAIN_TA`. Relevance classes separately comprise 76 CORE, 73 SUPPORTING, 27 HISTORICAL, 233 UNRESOLVED_RELEVANCE and 181 UNRESOLVED_OR_OUT_OF_SCOPE. The 25-record reviewer pilot sample exists but has not been independently adjudicated. At least 366 records (259+107) need explicit human eligibility review, and the protocol also requires verification of the remaining records. **No 590-record formal human screening or PRISMA inclusion count exists.**

**Source:** project November 5 inventory and indexed V5 screening sheet.

### H4 — Source reading and equation audits (PARTIAL, original-depth qualified)

Selected original literature has been read at different depths; this is research extraction, **not** formal eligibility assignment. Batch 01 includes Fletcher & Khan (2025) RACE, Bragone et al. (2022), Acker et al. (2025/26), Pan et al. (2025), Krama et al. (2026) and Li, Chang & Lu (2026); detailed notes also treat Gong (2015) and Hilshey (2013). Batch 02 deepened Pan's time-scale simplification, Krama's rectifier derating, Gong's experimental predecessor and Soltani's temperature-aware planning counterexample. In some cases only publisher HTML excerpts, an abstract or indexed passages were available; precise equations, figures and raw data remain unverified where stated.

The scientifically relevant **observed/modelled distinction** is:

| Prior work | Qualified source-supported contribution | What it does NOT yet establish for this thesis |
|---|---|---|
| Fletcher & Khan (2025), RACE | Transformer oil/winding thermal transients, modeled thermal charging controls and simulated requested/delivered energy | Completed same-site long-term connected field validation or measured missed mobility trips |
| Bragone et al. (2022) | 1D thermal PDE and numerical PINN–FVM comparison using measured boundary inputs | PINN advantage over FVM or independently observed spatial/hotspot ground truth |
| Pan et al. (2025) | Dynamic thermal ratings with active EV response in numerical planning; hourly winding quasi-steady simplification | A justified minute-scale hotspot approximation for abrupt fast-charging peaks |
| Krama et al. (2026) | Measured hot-climate 50 kW EVSE rectifier temperature, derating, charging power and time | Measured thermal state from the site's supplying transformer or fully linked power-to-mobility causal chain |
| Gong et al. (2015) | Public abstract reports 25 kVA transformer experimental calibration and EV charging control | Independently verified article-level sensor placement, field deployment and actual joint service outcomes until full text read |
| Li et al. (2026) | Public abstract of metering at electric-bus/transformer connection | Full thermal sensors, service outcome timing, causal restrictions or complete full text |

**Sources:** two Batch 01/02 GitHub notes; primary paper DOI links within those notes. These statements are evidence-depth labels, not formal risk-of-bias scores.

### H5 — Public supplementary search and connection outcomes (2026-11-05)

Six A–F thematic **public index discovery searches** were executed and documented; Wiley Scholar Gateway retrieved limited ranked passages in two topic searches; six Elicit A–F API requests failed with an account-plan access denial. These are **not** the native platform A–F protocol searches. No authenticated 2026 Scopus, IEEE Xplore, Web of Science or Compendex native export and complete query log was created in that pass. Neither ranked passage hits nor API-denied requests are assigned PRISMA records.

**Source:** `project/data_qualification/2026-11-03/SLR_PUBLIC_SEARCH_ACCESS_LOG_2026-11-05.md`.

### H6 — Existing experimental/data investigation (supporting thesis evidence; not SLR inclusions)

Recorded data investigations include SINTEF measured transformer (8,592 hourly samples; no ambient extreme heat), Slovenia STREAM power datasets (34,932 time points per source CSV ×12 stations, equipment meaning unresolved), KU Leuven EV charging with timestamp/meter boundaries unresolved, OSF power-quality logs, and other sources. Their existence cannot substitute for a literature-search PRISMA count or a physically connected same-site transformer/EVSE rectifier temperature series. A fully synchronized extreme-heat site with control restrictions and mobility outcomes has not been demonstrated by existing inventory. The mathematical model/experiments therefore remain separate downstream validation tasks.

**Source:** November 5 full work inventory, dataset audit and research checklists.

## 5. CURRENT CONTROL MATRIX — EXACTLY WHAT REMAINS

| Gate / stage | Verified status at 2026-11-05 | Exit evidence required |
|---|---|---|
| G1. Protocol and review type | Internal version, proposed | Dated scope, inclusion/exclusion rules, approved reviewer workflow and amendments |
| G2. Original platform-native search | NOT COMPLETED for A–F | Native search A–F in licensed databases, verbatim queries, hit counts, exports, checksums |
| G3. Bibliographic source control | V5 content crosswalk VERIFIED; binary blocked | Source XLSX binary SHA; true study-family decisions; source-derived years verified |
| G4. Title/abstract eligibility | 590 preliminary AI/rule triage | Human pilot, independent decisions/adjudication or explicit single-reviewer limitation |
| G5. Full-text eligibility | Selective reading; formal screening NOT COMPLETED | Full reports for all still-eligible records, full-text decision per report, explicit exclusions |
| G6. Equation/experimental extraction | Mixed depth on priority papers | Original page/equation-verified physical, sensor, model, validation and service fields |
| G7. Quality and critical synthesis | Preliminary comparative notes | Structured engineering appraisal, adverse studies and source-backed SO1–SO3 evidence map |
| G8. Review reporting and PRISMA | NOT READY | Audited PRISMA-ScR flow counts, checklists, methods, limitations and chapters |
| G9. Thesis model validation (separate) | Component-level preliminary | Qualified joint topology/thermal data, matched physics baselines, propagation and service validation |

**No evidence justifies labeling G1–G8 “complete” as a whole.**

## 6. PROSPECTIVE STANDARD OPERATING PROCEDURE — RUN IN THIS ORDER

### P1 — Freeze a versioned protocol and document retrospective departures

**Action:** retain the 2026-11-03 v0.2 original unchanged; create an approved `v1.0` protocol with reviewer names/roles, PCC, research questions, field/time/language/source restrictions, six search blocks, inclusion criteria, planned critical appraisal, data extraction, synthesis and disagreement handling. Record dates of protocol drafting, preliminary work, any prospective registry filing, and any changes between them. Obtain advisor sign-off if available; if not, write `APPROVAL NOT YET OBTAINED`.

**Records:** `PROTOCOL_V1_0.md`, `PROTOCOL_CHANGELOG.csv` fields `change_id, date_utc, original_text, revised_text, reason, before_or_after_search, authorized_by, supporting_link`.

**Acceptance:** protocol and amendments date-stamped, transparent and consistent with frozen thesis; no invented registration.

### P2 — Prepare reproducible searches and test recall against seed papers

**Design:** run six **separate** thematic blocks; never combine A∧B∧C∧D∧E∧F into an impossibly restrictive single query. Within **each** thematic block create an explicitly structured multi-line search in a primary database and translate the syntax into each target platform (ASU Library, n.d.-b). Select a primary database suitable for engineering—**propose Scopus, subject to library access**—and validate retrieval against at least five known papers (Fletcher–Khan 2025 RACE report as supplemental grey literature, Bragone 2022, Gong 2015, Pan 2025, Krama 2026; Li 2026 as additional target). Missing seeds require a logged synonym/field revision rather than quiet exceptions.

**A — transformer thermal physics + charging:** transformer AND EV charging AND thermal/top-oil/hotspot/aging/dynamic ratings.  
**B — EVSE thermal derating:** DC fast charger/rectifier/EVSE AND ambient/cooling/high heat AND power derating/temperature.  
**C — physically connected field site:** charger/bus depot AND transformer/feeder/substation AND measured/field monitoring.  
**D — coupled service and resilience:** power–transport network AND cascading/dynamic/thermal/recovery/service.  
**E — physics-informed mathematics:** PINN/hybrid physics/neural operator AND transformer/EVSE/battery AND thermal/temperature/inverse parameter.  
**F — standards and baseline physics:** IEC 60076-7/IEEE C57.91/transformer loading guide and validation/cooling/heat balance.

For each platform document the actual field expressions: e.g., Scopus `TITLE-ABS-KEY(...)` and Web of Science `TS=(...)` where supported; **do not assume** verbatim portable syntax for IEEE or Engineering Village. Keep full tested and final queries with set numbers as available.

**Acceptance:** every protocol search translated, reproducible, seed recall tested, exclusions reasoned.

### P3 — Execute and archive native database searches

**Operator:** researcher/librarian with appropriate ASU institutional database access. **Databases:** Scopus, IEEE Xplore, Engineering Village/Compendex, Web of Science Core Collection where licensed; publisher/institutional repositories and OpenAlex/Crossref can augment discovery but cannot silently replace the intended native search.

For each A–F × platform search save: `search_run_id`, database and host, access route, UTC timestamp, last searched date, complete search line history, final string, date range and language/type filters, result count shown, exact exported count, all export filenames/formats (RIS preferred where supported; CSV supplementary), raw byte SHA-256, operator and limitations. Save exported files as immutable raw snapshots and compare reported hit count against exported count; if a provider export cap truncates, save **all numbered batches**.

Suggested path: `project/systematic_literature_review/evidence/01_raw_database_exports/<YYYY-MM-DD>/<platform>/<search_id>.*` for authorized files; if copyrighted metadata redistribution is restricted, store private controlled copies and publicly share only permitted methods/logs and manifest.

**Acceptance:** search counts and exported records reconcile per query, re-running possible, provenance for all records preserved. **Current status: blocked pending institutional access; cannot replace with web index searches.**

### P4 — Import, normalize and deduplicate WITHOUT destroying provenance

**Action:** snapshot imported records; normalize DOI, title, year, journal and source IDs, preserving originals; match DOI/PMID/IEEE accession as strong keys; manually review title/author/year fuzzy matches; compare preprint, proceedings, journal versions and identical experiments. Maintain one record-to-source many-to-many provenance table and a separate `study_family_id` where justified. Do not overwrite original LIT IDs.

**Priority audit:** 16 identical normalized-title groups; 74 year differences, including the `LIT-0003` regression; remaining 35 blank DOI slots are not automatically errors. Resolve all against original publication metadata.

**Acceptance:** counts of identified records, all duplicate decisions, retained records and source-family groups are auditable; original untouched.

### P5 — Pilot screening and independently apply eligibility

**Procedure:** choose and document 25 diverse pilot records, not artificially easy examples, from the 590 and any newly imported relevant records. Train reviewer 1 and reviewer 2 on short, low-inference questions for title/abstract screening. Screen independently (including `INCLUDE`, `EXCLUDE_WITH_REASON`, `UNCERTAIN/SEEK_FULLTEXT`), record both timestamps and page/abstract evidence, calculate agreement, and adjudicate disagreements with a third reviewer or signed consensus. Revise the rubric only through versioned amendment. Then screen all records once deduplicated, with any single-reviewer deviations explicitly disclosed rather than fabricated.

**Decisions:** (i) Is the engineering asset/context within scope? (ii) Is there thermal/dynamic/connected-service/methodological relevance to at least one review question? (iii) Is an acceptable source type and original traceable reference present? (iv) Is the record a primary source, review, standard, preprint or thesis stratum? (v) Is full text necessary to resolve ambiguity? Explicit reason-code hierarchy is essential: wrong system, wrong phenomenon, wrong source type, duplicate report, no traceable scientific content, insufficient information; a relevant *non-heat* baseline is a comparator, not an automatic exclusion.

**Important:** 98 ADVANCE, 126 BACKGROUND, 259 PROVISIONAL EXCLUDE and 107 UNCERTAIN are **triage labels only**. An AI-assisted evaluation is not a second independent human screening decision.

**Acceptance:** complete human decision log, disagreements resolved and eligible report retrieval queue grounded.

### P6 — Retrieve and assess the full text of every eligible report

**Action:** retrieve source-accessible full journal/proceeding/report PDFs or HTML; record source URL and date, rights/access limitations, original or secondary text depth, DOI, version and file hash where lawful. Record *each* full-text exclusion with one primary reason and optional secondary note; review study family independently from report count. Pursue institutional library access or author requests when appropriate, log every failed acquisition and attempt. A missing PDF is **not** evidence the study is irrelevant; classify as `REPORT_NOT_RETRIEVED` and separately record a retrieval attempt.

**Priority original papers:** Gong (2015) 25-kVA transformer experiment; Fletcher–Khan (2025) RACE report and Part 2 follow-up; Bragone (2022) PINN/FVM PDE; Pan (2025) transformer dynamic ratings; Krama (2026) Qatar EVSE derating; Li et al. (2026) electric-bus transformer site; Acker (2025/26) battery/coolant experimental model. The final eligible corpus is **not limited** to this list or to 98.

**Acceptance:** each sought report classified retrieved/not retrieved/assessed/excluded/included; no phantom full-text read.

### P7 — Extract original physics, measurements and validation into a claim-level matrix

**For every included study:** record study family, reference, page/table/figure/equation number, physical asset, topology, inputs and measured outputs, units and clock resolution, heat/electrical conservation equations, forcing, initial and boundary conditions, control policy, calibration versus validation dataset, independent holdout and uncertainty, direct extreme-heat exposure, energy/service metric and exactly what can/cannot be inferred.

**Source-depth labels:** F1 = theoretical/physical principle, F2 = peer-reviewed model description or abstract with limited validation, F3 = directly measured field/lab observation, F4 = measured parameter/calibration, F5 = numerical simulation outcome, F6 = matched independent validation, F7 = physically connected end-to-end directional field evidence; **these names are a proposed extraction guide, not an established universal appraisal scale**. Confirm consistency with the existing project's `F1–F7` taxonomy before freezing a new codebook. Do not infer F7 from a charger paper plus an unrelated transformer paper.

**Acceptance:** every consequential assertion points to the original page/equation and is distinguishable as observed, calculated, simulated or unverified.

### P8 — Critical appraisal and novelty falsification

**Appraise by design and claim, not journal impact:** validation independence, sensor calibration, electrical topology, sample/temporal coverage, thermal forcing and confounders, parameter identifiability, dimensional consistency, benchmark comparability, UQ and raw-data reproducibility. Record PASS/PARTIAL/FAIL/UNKNOWN *per domain*, plus explanation; no unfounded composite "scientific quality" score. For simulation-only papers, appraise mathematical verification and real-world transfer claims separately. For multi-paper families, avoid counting one experiment repeatedly.

**Required counterexamples:** Gong 2015/2012, Hilshey 2013, Fletcher–Khan 2025, Pan 2025, Bragone 2022, Krama 2026, Acker and Soltani 2026. Temperature-aware charging, transformer DTR, PINN transformer heat, and target SOC at departure already appear in prior art; therefore a proposed novelty cannot be **merely** their coexistence. A possible contribution would require testing an observed connected thermal state→constraint→propagation-delay→service chain, if data allow. That novelty remains a **hypothesis**, not a verified literature absence.

### P9 — Reconcile PRISMA-ScR quantities from auditable counts only

Use disjoint flow units and compute after the completed screening export. Suggested ledger:

| Reporting quantity | Present verified value | Future source |
|---|---|---|
| Records identified from native 2026 A–F database searches | UNKNOWN | Final search log/export manifests |
| Additional records from registers/repositories/citation chaining | UNKNOWN | Source discovery ledger |
| Duplicate records removed before screening | UNKNOWN | Signed dedup decisions |
| Records screened | UNKNOWN | Human title/abstract decision register |
| Records excluded at title/abstract | UNKNOWN | Reason-coded human decisions |
| Full-text reports sought | UNKNOWN | Retrieval queue |
| Reports not retrieved | UNKNOWN | Failed access attempts |
| Full-text reports assessed | UNKNOWN | Original full-text screening |
| Full-text reports excluded with reasons | UNKNOWN | Full-text exclusion register |
| Independent studies included | UNKNOWN | Included-study family register |

**Prohibited shortcuts:** do not treat 687, 404, 533, 590, 98 or 13 as final PRISMA included-study counts; do not add historical 687 raw provenance rows to 590 master records; do not count repeated reports as independent studies; do not declare an incomplete screen “completed” by leaving unknown cells blank.

### P10 — Produce reproducible synthesis and insert it into the thesis

**Final reporting package:** (1) locked method with amendments; (2) exact A–F native search appendix and immutable manifest; (3) normalized references and ID crosswalk; (4) dedup/study-family decisions; (5) human screening logs/adjudication; (6) retrieval and full-text exclusion log; (7) primary equation/sensor/validation evidence matrix; (8) SO1/SO2/SO3 synthesis with contradictory prior art; (9) PRISMA-ScR flow/checklist and PRISMA-S search checklist; (10) limitations and reproducibility statement; (11) reader-ready thesis Chapter 2 and its own citations.

Suggested writing structure in **Chapter 2**:
1. Research motivation, eligibility and state–time framing.
2. Methods (review type, protocol, exact searched sources, record management, selection, extraction and synthesis).
3. Thermal coupling evidence (P→Tₑ, Tₑ→P, and controls).
4. Transformer/charger/battery conservation models and timescales.
5. Field and laboratory validation, and observed versus simulated service.
6. Method comparisons (physical models, inverse/gray-box, PINN) under matched evidence.
7. Evidence gaps, falsified novelty claims, and exact model/data decisions.
8. SLR limitations and transparent PRISMA reporting; appendixes for large logs.

**Format warning:** if the ASU program calls the culminating work an applied project rather than a Graduate College-reviewed thesis, do not assert ETD-format approval or the Format Wizard as obligatory. For an actual ASU thesis/dissertation subject to Graduate College review, follow the current ASU format manual and wizard, which supersede a generic document style (ASU Graduate College, n.d.).

## 7. CONTROLLED FORMS AND FIELD DEFINITIONS

### Form S — database search execution record

```
search_run_id | protocol_version | concept_block_A_to_F | database
platform_vendor | subscription/access_method | operator_actual
search_date_UTC | search_date_local | coverage_start | coverage_end
verbatim_multiline_query | exact_final_string | field_tags
controlled_vocabulary | all_filters | hit_count_visible
exported_record_count | batch_count | raw_filename | file_format
sha256_raw_bytes | seed_papers_retrieved | reason_for_revision
limitations | reviewer_of_search | amendment_link
```

### Form D — bibliographic record and duplicate decision

```
canonical_LIT_ID | original_source_record_IDs | original_title
original_DOI | normalized_DOI | original_year | verified_year
all_database_provenance | source_export_file_hash | study_family_ID
duplicate_candidate_ids | merge_keep_separate | evidence_for_decision
record_versions_link | decision_maker | timestamp_UTC
```

### Form R — independent reviewer eligibility and adjudication

```
canonical_LIT_ID | protocol_version | screening_stage
reviewer1_actual_ID | reviewer1_decision | reviewer1_reason
reviewer1_evidence | reviewer1_timestamp_UTC
reviewer2_actual_ID | reviewer2_decision | reviewer2_reason
reviewer2_evidence | reviewer2_timestamp_UTC
adjudication_method | adjudicator_actual_ID | final_decision
final_reason_code | page_or_abstract_locator | disagreement_note
```

### Form E — original scientific extraction (one claim per row where needed)

```
study_family_ID | canonical_LIT_ID | original_paper_doi
fulltext_version_and_url | access_level | source_page_equation
asset_and_actual_topology | measured_vs_modelled_state
sensor_location_and_units | sample_interval_and_clock
ambient_and_heat_exposure | heating_cooling_boundary
first_law_equation | electrical_interface_equation
parameter_value_units_provenance | identifiability
calibration_design | validation_design_and_holdout
baseline_comparator | uncertainty_and_residuals
operational_restriction_reason_code | source_vs_EV_BMS_taper
requested_power | offered_power | actual_delivered_power
service_deadline_and_outcome | propagation_timestamp_chain
SO1_SO2_SO3_relevance | claim_grade_with_evidence | limitations
reviewer | extraction_date_UTC | verification_status
```

### Form A — versioned protocol amendment

```
amendment_ID | previous_version | new_version
recorded_at_UTC | original_rule | revised_rule | rationale
search_or_screening_stage_when_changed | possible_selection_bias
approved_by_actual_person | affected_LIT_IDs | linked_commit
```

### Form P — PRISMA reconciliation log

```
flow_stage | count | unit_record_report_or_study
input_artifact_sha256 | formula_or_query | responsible_reviewer
independent_verification_status | date_UTC | comment
```

## 8. IMMEDIATE OPERATIONAL QUEUE AND RESPONSIBILITY

| Order | Operator | Concrete action | Stop/pass gate |
|---|---|---|---|
| 1 | Researcher + supervisor | Review and approve the protocol/eligibility and reviewer configuration; record amendments | G1 passes only with actual sign-off or documented limitation |
| 2 | Researcher | Obtain original Library V5 `.xlsx` bytes for SHA-256, inspect all tabs and preserve original | Raw-file authenticity restored; no overwrite |
| 3 | Researcher + librarian | Obtain institutional Scopus, IEEE, Compendex and WoS access and exact A–F native exports | G2 with query+manifest+export count for each source |
| 4 | Researcher | Verify 16 same-title groups, 74 year cases; reconcile new exports into stable IDs | G3 with study families and source provenance |
| 5 | Two actual independent readers when available | Pilot a mixed 25-record subset, revise signed rubric, screen all candidate records | G4 with real decisions and adjudication |
| 6 | Reader(s) + library | Retrieve all eligible full texts, especially Gong, Krama, Pan and connected field studies | G5 complete retrieval/eligibility log |
| 7 | Researcher + technical verifier | Extract original equations, measurements, model validation and contradictions | G6/G7 evidence matrix complete |
| 8 | Researcher + independent QA/supervisor | Reconcile PRISMA counts, reporting checklists, scientific synthesis | G8 defensible manuscript and appendixes |

**Division of responsibility:** an AI tool may parse, normalize, generate candidate search strings, compare metadata, flag conflicts, draft code, extract source passages and build provisional matrices. It does **not** replace the person who accessed subscription databases, the independent second human reviewer, the advisor's approval, original field measurements or source verification. When not available, these actors/actions must be recorded as missing, not assigned fictitious identities.

## 9. EXPLICIT OPEN RISKS AND MITIGATIONS

1. **Retrospective protocol risk:** triage preceded complete protocol lock. Preserve actual chronology, disclose it and preregister only prospectively if desired.
2. **Data completeness risk:** accessible Library V5 indexed text differs from having original binary. Obtain raw XLSX and verify checksum, formulas and 31 tabs.
3. **Search sensitivity risk:** six blocks and primary database fields may miss literature if terms not translated. Pilot at least five known studies, revise synonym choices transparently and seek librarian peer review of exact strings.
4. **Selective-exclusion risk:** 259 provisional excludes/107 uncertainties are unadjudicated; screen them independently and preserve contrary studies.
5. **Duplicate/independence risk:** 16 same-title pairs may duplicate versions of one study. Separate record, report, study and experiment IDs; document every grouping.
6. **Source-depth risk:** Pan publisher 403, Krama abstract-only, Gong full IEEE access unresolved. Mark exact primary equation/experiment claims pending original full-text checks.
7. **Connected physical evidence risk:** existing transformer and charger data often come from unrelated installations. Never infer same-site thermal cause or field-observed mobility consequences from their combination.
8. **Model-method overclaim risk:** literature already contains transformer thermal controls and PINNs. Retain physics-first baseline; only test PINNs under matched leakage-safe validated splits and adequate measurements.
9. **Administrative format risk:** MSE applied projects and theses differ. Confirm actual ASU culmination/departmental style requirements with advisor.

## 10. REPRODUCIBILITY AND RELEASE CONDITIONS

Each released report or revision must state: version/date, source paths and GitHub commit(s), raw-export hashes and access rights, exact methods, numbers by unit, unresolved blockers, reviewer identities/roles (only actual), conflicts and amendments, validation checks, and version history. GitHub text commits may cite private raw-data manifests without redistributing licensed documents. A final results chapter must link every literature-derived substantive claim to an adjacent verified paper citation and source locator, following the project's canonical APA 7 in-text citation rule.

**RELEASE CONDITION — systematic scoping review ready:** G1–G8 evidence complete or every unavoidable deviation explicitly disclosed, actual PRISMA counts independently checked, original full texts of included studies qualified, search strings/public methods archived, and manuscript limitations written. A blocked database or missing second reviewer should not be silently converted into a completed standard review. If constraints force a rapid or partial review, rename and report the method accurately, with approved protocol amendments, instead of continuing to claim a full review.

**RELEASE CONDITION — thesis engineering model ready (separate):** validated physics equation set with measured parameters/uncertainty, verified electrical connection where claimed, extreme-heat applicability boundaries, independent benchmarks and physically meaningful service dynamics. A finished literature review is not a proxy for a validated connected system model.

## 11. EVIDENCE FILE MANIFEST — REFERENCED, NOT MODIFIED

- **Governing project authority:** `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md` and linked frozen title/scope/GO/SO files.
- **Historical and current inventory:** `project/THESIS_RESEARCH_FULL_INVENTORY_AND_ROADMAP_2026-11-05.md`.
- **Proposed existing review protocol:** `project/data_qualification/2026-11-03/SYSTEMATIC_REVIEW_EXECUTION_PROTOCOL_V02_2026-11-03.md`.
- **Original 533-register:** `project/systematic_literature_review/MASTER_SYSTEMATIC_LITERATURE_REGISTER_V01.csv`.
- **Library V5 workbook:** `/My thesis/Unified_Thesis_Research_Master_V5_Reconciled_2026-11-04.xlsx` (version 2 indexed; raw binary not materialized).
- **V5 audit report:** `project/data_qualification/2026-11-03/V5_RECONCILIATION_AUDIT_2026-11-05_V2.md`.
- **590-record ID crosswalk:** `project/data_qualification/2026-11-03/V5_GITHUB_RECORD_CROSSWALK_2026-11-05.csv`.
- **16 duplicate-title groups:** `project/data_qualification/2026-11-03/V5_POTENTIAL_STUDY_FAMILY_DUPLICATES_2026-11-05.csv`.
- **74 year checks:** `project/data_qualification/2026-11-03/V5_YEAR_FIELD_REVIEW_QUEUE_2026-11-05.csv`.
- **Primary reading batch 01:** `project/data_qualification/2026-11-03/PRIMARY_SOURCE_READING_BATCH01_2026-11-05.md`.
- **Primary reading batch 02:** `project/data_qualification/2026-11-03/PRIMARY_SOURCE_READING_BATCH02_PAN_KRAMA_GONG_2026-11-05.md`.
- **Public search access log:** `project/data_qualification/2026-11-03/SLR_PUBLIC_SEARCH_ACCESS_LOG_2026-11-05.md`.

All GitHub paths refer to `Dossiya-SE/MSE-thesis` branch `user-data-qualification-2026-11-03` unless otherwise noted. Referenced earlier Q0/V5 analysis files can have separate storage status, which must be stated rather than assumed.

## 12. OFFICIAL GUIDANCE AND METHODOLOGY REFERENCES

### ASU official sources — verified online 5 November 2026

- ASU Library. (n.d.-a). *Protocol development and registration*. https://libguides.asu.edu/evidence_synthesis/protocol
- ASU Library. (n.d.-b). *Write a search strategy*. https://libguides.asu.edu/evidence_synthesis/search-strategy
- ASU Library. (n.d.-c). *Running/exporting searches and citation management*. https://libguides.asu.edu/evidence_synthesis/exporting-citation-management
- ASU Library. (n.d.-d). *Critical appraisal/risk of bias assessment*. https://libguides.asu.edu/evidence_synthesis/critical-appraisal
- ASU Library. (n.d.-e). *Scoping review*. https://libguides.asu.edu/evidence_synthesis/scoping-review
- ASU Library. (n.d.-f). *Translating searches*. https://libguides.asu.edu/evidence_synthesis/translating
- ASU Graduate College. (n.d.). *Formatting your thesis or dissertation*. https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation

### Evidence synthesis scientific standards

- JBI. (2024/2026 current online guidance). *Manual for Evidence Synthesis: Scoping reviews, protocol and selection*. https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862729/10.2.5%2BSearch%2BStrategy ; https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862769/10.2.7%20Data%20extraction
- Tricco, A. C., et al. (2018). *PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation*. *Annals of Internal Medicine, 169*, 467–473. https://doi.org/10.7326/M18-0850
- Rethlefsen, M. L., et al. (2021). *PRISMA-S: An extension to the PRISMA statement for reporting literature searches in systematic reviews*. *Systematic Reviews*. https://doi.org/10.1186/s13643-020-01542-z
- Moher, D., et al. (2015). *PRISMA-P 2015 statement*. *Systematic Reviews*. https://doi.org/10.1186/2046-4053-4-1

### Key prior original research cited in the audit

- Fletcher & Khan (2025). RACE for 2030 Part 1 final technical report. https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf
- Bragone et al. (2022). Transformer heat/PINN comparison. https://doi.org/10.1016/j.epsr.2022.108447
- Gong et al. (2015). Transformer thermal control and 25 kVA experimental validation. https://doi.org/10.1109/TSG.2014.2365452
- Pan et al. (2025). Distribution planning with EV response and transformer/cable DTR. https://doi.org/10.1049/hve2.70024
- Krama et al. (2026). Qatar 50 kW EV charger extreme-climate field evidence. https://doi.org/10.1016/j.ecmx.2026.101960
- Acker et al. (2025/2026). EV battery/coolant physical thermal model. https://doi.org/10.1007/s41104-025-00157-7

---

**End of controlled document.** Update by new version and dated amendment. Do not retrospectively edit completed search, reviewer or provenance records to appear prospective.