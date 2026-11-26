# Systematic Scoping Review Protocol V2 — Thermal Power–Electrified Transportation (for review)

**Working review title:** *Extreme-Heat-Induced Thermal Interdependencies Between Electrical Power and Electrified Transportation Systems: A Systematic Scoping Review*  
**Version/date:** V2, 2026-10-16. **Status: REVIEW-READY PROTOCOL DRAFT; NOT PREREGISTERED; FORMAL ACADEMIC SEARCHES NOT EXECUTED.**  
**Thesis authority preserved:** `project/CANONICAL_THESIS_TITLE_V3.md`, thermal scope, Extreme Heat V4 and frozen General Objective/SO1–SO3; this review protocol does not amend them.
**Method guidance:** [JBI scoping reviews chapter](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862497); [JBI search-method chapter](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355827873/2.4%2BSearching%2BCOMING%2BSOON); [PRISMA-ScR](https://www.prisma-statement.org/scoping); [PRISMA-S](https://www.prisma-statement.org/prisma-search).
**Review team:** Reviewer 1 identified; second reviewer/librarian PRESS review and independent screening availability UNCONFIRMED. Do not describe dual independent screening when not performed.

## 1. Review purpose and question (PCC)

**Population/physical objects:** distribution transformers, Power network equipment/circuit limits, EV supply equipment (EVSE), battery-electric road vehicles and relevant charging/service operations. EVSE remains inside Tₑ; the P transformer is outside the EVSE.
**Concept:** heat- or temperature-conditioned physical states, heat transfer, thermal inertia/capability/derating; time-dependent dynamics, physically qualified P→Tₑ or Tₑ→P propagation and electricity/mobility service.
**Context:** external extreme heat, heatwaves and related temperature-exposure regimes; studies without extreme heat may enter as **foundational mechanisms/methods**, clearly separated from directly heat-exposed empirical systems.

**Central review question:** *How does extreme heat change thermal states, operating constraints, and electricity–mobility services across coupled Power–Electrified Transportation systems?*

**Four review dimensions:**  
**A Physics:** heat generation, transport, temperature, state evolution, thermal inertia, operating temperature constraints and thresholds.  
**B Coupling:** EV charging loads, grid thermal rating/constraints, EVSE charging derating, actual carrying ports/variables, independent P→Tₑ and Tₑ→P mechanisms.  
**C Evidence:** sensors, raw data, identifiability/calibration, simulated vs measured, uncertainty and held-out physical validation.  
**D Resilience:** measured/predicted service deficits, required electricity and mobility, thermal transition/propagation times, adaptation and recovery only when explicitly modeled.

## 2. Review architecture and eligibility

**Four interlinked bibliographic retrieval streams, no single overrestrictive AND:**
- **A Power thermal dynamics:** transformer/feeder/conductor thermal ODE/PDE, heat balance, thermal inertia, oil/lid/hotspot state, dynamic rating under load and ambient heat. A study may lack EV terminology.
- **B Electrified transportation thermal performance:** EVSE/charger/converter/charging connection/cooling and battery/vehicle as needed for actual heat-conditioned service; high ambient temperature, charger capability, measured power/time. A study may lack power-system terminology.
- **C Direct and adjacent coupled P–Tₑ:** transformer↔EV charging load/control/capability, physical heat-conditioned interface, EV power/traffic interdependency, measured or simulation-only propagation; direct thermal and contextual nonthermal studies get **different tags**.
- **D Evidence/methods:** analytical/RC/ODE/PDE thermal solvers and first-principles baselines, grey-box and PINNs/other physics-informed ML, measured/simulated benchmarks, data papers and measurement metadata. A study may lack heatwave in title/abstract.

**Main directly relevant evidence:** primary physical, experimental, computational or formal mathematical work with identifiable Power or Tₑ physical equipment, temperature/heat-dependent mechanism and relevant state-time or operational consequence. **Direct P–Tₑ** papers require actual cross-system physical/electrical operating connection or defensible modeled coupling; actual field coupling and simulated coupling must be tagged separately.

**Foundational eligible papers:** high-relevance single-asset thermal physics, established thermal control and measurements, general P–Tₑ service/coupling methods, non-heat-specific EV loading studies, physics-informed method/baseline articles. These support modules or comparators **but cannot establish complete extreme-heat coupled field causality**.

**Include:** original peer-reviewed research and substantive experimental technical reports with source/date/equipment/method metadata; public datasets with a corresponding data descriptor; key review papers for reference-chasing, tagged `SECONDARY`; meaningful preprints separately tagged `NON_PEER_REVIEWED`; English/French if accessible, no retrospective arbitrary year cutoff (search from database inception to executed date).
**Exclude from counted primary synthesis:** pure generic resilience/network theory with no physically relevant component/interface/thermal evidence; only marketing statements or unrelated infrastructure; non-verifiable summaries without a source primary artifact (retain in leads); duplicates and superseded versions after DOI/document identity resolution; battery-only aging/chemistry not required by minimum thermal interdependency model. Record full-text exclusions with explicit one primary reason and keep relevant context references outside main denominator.

**Scoping-review boundary:** We map studies and methods rather than pool incompatible temperature, transformer, grid and mobility outcomes into a meta-analysis. Critical evidence appraisal will be charted for physics/validation strength; do not imply PRISMA-ScR automatically performs causal appraisal.

## 3. JBI three-step search and reproducibility

**Step 1 — preliminary term inventory:** title/abstract/keywords of confirmed sentinel papers: Trentadue 2018 extreme charger efficiency, Krama 2026, Fletcher & Khan RACE 2025, Lim & Bae 2018, Godina 2016, Blomgren 2023, Bragone 2022, EV-EcoSim 2024, Wu 2022, Cui 2025, Villarroel 2017. Document exact title, DOI, indexed terms and paper version.
**Step 2 — translate to databases:** four independent conceptual lanes using native Scopus `TITLE-ABS-KEY`, Web of Science `TS`, IEEE Xplore supported fielded interface, and Compendex (if accessible) with syntax and record export per query. **These databases are not currently authenticated here.** Run known-item recall on the full broad-lane returned record sets, not DOI-only lookup, adjust synonyms and confirm retrieval. Translate to OpenAlex, when a real API/access tool is available, and log host/syntax/hits; do not claim OpenAlex API search on public web queries.
**Step 3 — reference/citation chasing:** reference and forward citation papers of included primary articles using logged source/date and iterative saturation, supplemented with journal publisher indexes and grey sources from identifiable organizations.
**PRISMA-ScR/PRISMA-S:** Retain exact executed query, engine/platform, original timezone/date, limits, actual hit count (UNKNOWN until engine reports), RIS/BibTeX/CSV export location, checksums, dedup/selection software, exclusions and denominators. **Never treat web-ranked search snippets as complete database exports, and never fill PRISMA counts with provisional estimates.**

## 4. Candidate search strategy (NOT YET EXECUTED IN SCOPUS/WOS/IEEE)

The following eight **Scopus conceptual translations** use separate broad/sensitivity lanes; each must be syntax-tested and checked for actual sentinel DOI retrieval. Quotes are part of syntax; adjust capitalization/stems by database.

```text
A1 — TITLE-ABS-KEY((transformer OR "distribution network" OR "power distribution" OR "transmission line") AND (thermal OR temperature OR "hot spot" OR "hotspot" OR "dynamic rating" OR "heat transfer"))
A2 — TITLE-ABS-KEY((transformer OR "power system" OR "distribution grid") AND (heatwave* OR "extreme heat" OR "ambient temperature" OR "high temperature" OR cooling) AND (thermal OR rating OR derat*))
B1 — TITLE-ABS-KEY(("electric vehicle" OR EVSE OR "charging station" OR "fast charger" OR "DC charging") AND (temperature OR thermal OR heat OR derat* OR "charging efficiency"))
B2 — TITLE-ABS-KEY(("fast charging" OR charger OR EVSE) AND ("ambient temperature" OR "extreme temperature" OR "hot climate" OR heatwave* OR rectifier))
C1 — TITLE-ABS-KEY(("electric vehicle" OR "EV charging" OR "charging station") AND (transformer OR "power distribution" OR "power grid") AND (thermal OR temperature OR "hot spot" OR aging OR ageing OR "thermal limit"))
C2 — TITLE-ABS-KEY(("power transportation" OR "power and transportation" OR "coupled power" OR "electric vehicle" OR "charging infrastructure") AND (interdependen* OR "co-simulation" OR resilience OR "charging demand") AND (grid OR electricity OR power))
D1 — TITLE-ABS-KEY((transformer OR EVSE OR charger OR battery) AND (thermal OR temperature OR "heat equation") AND (experiment* OR measur* OR calibrat* OR validat* OR dataset OR "grey box"))
D2 — TITLE-ABS-KEY((transformer OR charger OR EVSE OR "electric vehicle" OR battery) AND (thermal OR temperature OR "heat equation") AND ("physics-informed" OR PINN OR "hybrid model" OR "grey-box" OR "gray-box" OR "finite volume"))
```

**Known-item QA before search freeze:**
A1 should find Blomgren, Villarroel; A2 probes heat-rated P studies; B1/B2 should find Trentadue and Krama; C1 should find Godina and Lim & Bae and RACE **if indexed** (RACE technical reports may NOT be indexed in Scopus); C2 should find Wu/Cui/Balogun where indexed; D1 should find Blomgren/field measurements; D2 should find Bragone. If indexed item recall fails, repair query and log version instead of silently selecting familiar papers. Cite papers found outside indexed databases as separate sources rather than denominator hits.

## 5. Screening, extraction, evidence grading and discrepancy tracking

- Assign one identifier per DOI/source-version, store original native retrieved IDs and query provenance; normalize DOI, then deduplicate, distinguishing a technical report from a later peer-reviewed journal paper.
- Title/abstract decision: `core_direct`, `component`, `methods`, `context`, `exclude`, `uncertain`; full-text eligibility separately with explicit exclusion reasons.
- Extraction: full title, authors, publication year/venue/DOI/license/source version/locator; physical systems and equipment (P vs Tₑ), ambient forcing, states/measurements (oil/lid/winding/EVSE/vehicle), heat generation/transfer laws, equations **with exact page/equation numbers**; units, initial/boundary conditions, mechanism & direction; control/derating; charging port/electrical quantities; critical times, propagation delay, services and recovery; methods, solver reference and hardware, baselines; calibration/holdout/uncertainty/independent observation; source PDF/access tier; raw data availability; transferability and author limitation.
- **Evidence labels are non-mutually-exclusive flags**, not a false guaranteed quality ladder: `ILLUSTRATIVE` = synthetic/hypothetical inputs; `EVIDENCE_BOUNDED` = stated sourced parameters/assumptions and domain; `CALIBRATED` = at least one parameter from measured data; `INDEPENDENTLY_VALIDATED` = predictions tested on relevant holdout **physical measurements**; plus `SIMULATED_REFERENCE` where validation target is only numerical. Calibrated ≠ field validated, and measured inputs ≠ measured outputs.
- **Directed mechanism flag for each direction**: `PHYSICS_PROPOSED`, `COMPONENT_MEASURED`, `INTERFACE_SIMULATED`, `INTERFACE_FIELD_IDENTIFIED`, `SERVICE_MEASURED`, `NOT_ESTABLISHED`; none of these are automatic from seeing EV/transformer in same paper.
- Chart actual electricity service vs rated available electrical power vs charging-energy proxies vs independent mobility requirement/fulfillment. State `UNKNOWN` where not reported.
- Source-level abstraction and gap synthesis must compare **counterexamples**. A novelty claim needs comprehensively checked prior art, not absence within current six-paper pilot.

## 6. Model and dataset decision, subordinate to Pat Phelan's feedback

**Data-suitability gate** first: lawful original temperature/thermal-state observations with known equipment/sensor location, timestamps and sync; boundaries/controls, power/energy flow and sufficient heat/load variation, usable holdouts and observable targets.
**If adequate data exists**: compare physics/RC/PDE baseline to conditional PINN/physics-informed ML on the **same physically measured target** with physical residuals, uncertainty, event timing, compute cost and independent extreme-heat or held-out equipment tests. A PINN is an *evaluated option*, not automatically beneficial.
**If data inadequate**: use verified pure physics, numerical analysis, limiting-case/standard comparisons and model-form uncertainty, explicitly **no empirical full-interface claim**. Discuss with supervisor whether resulting scope meets SO3.
**Separate feasibility paths:** same-site field-qualified P↔Tₑ versus component-measured + simulated cross-interface. These are not evidence-equivalent and require advisor feasibility decision.

## 7. Execution and current status

**Executed to date:** targeted publisher/source lookups, six-paper interim original-source audit, additional targeted web searches 2026-10-16 and a full-text PDF-text check of the 2025 RACE 32-page report (not figures or original raw transformer logs). These are *search discovery and source verification*, **not formal scoping-review record retrieval/screening**.
**Unexecuted:** Scopus, Web of Science, IEEE Xplore, Compendex authenticated collection queries/exports; OpenAlex API (direct request inaccessible through current web tool); formal known-item recall using live broad-lane database returns, duplicate-counted screening, PRISMA denominator, study-level eligibility completion, full raw-data physical validation.
**External blocker:** Elicit API denied by account plan, formal academic database access unavailable. Librarian/supervisor search QA and licensed native queries/exports required before asserting review comprehensive.

## Sources consulted for protocol method

- JBI Manual for Evidence Synthesis, scoping review chapter 2026: https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862497
- JBI comprehensive reproducible search and three-step process: https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355827873/2.4%2BSearching%2BCOMING%2BSOON
- PRISMA-ScR (2018) checklist: https://www.prisma-statement.org/scoping
- PRISMA-S (2021) checklist: https://www.prisma-statement.org/prisma-search

**Research decision:** `PROTOCOL_READY_FOR_ADVISOR/LIBRARIAN REVIEW`, not `SYSTEMATIC_REVIEW_COMPLETED` and not `PINN_SELECTED`.
