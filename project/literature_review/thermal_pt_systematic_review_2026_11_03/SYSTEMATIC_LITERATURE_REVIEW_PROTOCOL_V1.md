# Systematic review protocol V1 — extreme-heat Power–Electrified Transportation thermal interdependencies
**Status:** WORKING / PROTOCOL DRAFT — NOT YET PREREGISTERED; SEARCHES NOT YET RUN EXHAUSTIVELY; NO PRISMA COUNTS.  
**Date:** 2026-11-03. **Thesis:** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience.  
**Branch:** `user-data-qualification-2026-11-03`. No change to frozen authorities or objectives.
**Supervisory motivation:** Pat Phelan asks (i) what previous researchers have done and whether there has been a thorough literature review; (ii) conditional choice of physics-informed ML/PINN if experimental data can justify it, otherwise physics-based equations.

## A. Scope: canonical SO1–SO3 (never replace by historical H1–H5)
- **SO1:** Identify and qualify thermally sensitive physical states and *directional* thermal dependencies connecting Power System P and Electrified Transportation System T_e.
- **SO2:** Develop a physics-based state-time model of qualified thermal interdependencies and their propagation under extreme heat.
- **SO3:** Quantify critical transition times, propagation delays and electricity/mobility service consequences.
- Core studied application: grid-connected battery-electric road transport/EVSE (exact public DC vs depot context OPEN).
- Retain two pathways of sustainability only if data/functional unit justify them; not a generic sustainability review.
- EVSE belongs to T_e; power supply path/transformer to P; no third system invented.

## B. Review questions (all studies independently eligible across distinct strata)
1. **LRQ1 — Physics:** Which transformer, feeder, EVSE rectifier/cooling and battery heat-transfer laws, temperatures, loss mechanisms, thermal inertias, and thresholds are validated; where?
2. **LRQ2 — Directional interface:** Which articles show physically mapped transformer→EVSE and/or temperature-conditioned EVSE→transformer demand effects? Are causal thermal restrictions logged and alternative causes controlled?
3. **LRQ3 — State/time:** How are transient heat forcing, thermal state evolution, coupling, critical threshold time, delay and recovery modeled? Which quantities are observed vs modeled?
4. **LRQ4 — Service/resilience:** Which papers quantify **required vs delivered** electrical charging, SOC/departure or mobility operation under thermal constraints, with defensible time and service units?
5. **LRQ5 — Data/method:** What measured field/lab/synthetic inputs, instrumentation, data availability, validation splits, parameter identifiability, uncertainty and model comparisons support pure physics, PINNs, hybrid PIML or data-only ML?
6. **LRQ6 — Novelty:** Which precise results already exist, which fail the needed observational/physical gate, and what single falsifiable next test remains?

## C. Registration and applicable methodological guidance
- PRISMA-P 2015: DOI 10.1186/2046-4053-4-1 — protocol items; adapt to heterogeneous engineering evidence.
- PRISMA-S 2021: DOI 10.5195/jmla.2021.962 / 10.1186/s13643-020-01542-z — report every database, exact query, date, limit and export.
- PRISMA 2020: DOI 10.1136/bmj.n71 — report identification, deduplication, selection, exclusions, evidence appraisal and actual flow counts.
- PRESS 2015: DOI 10.1016/j.jclinepi.2016.01.021 — external/peer query review for search concepts, syntax, spelling and filters.
- Planned transparent repository protocol/OSF timestamp **if approved**; no registration claimed. No fictitious PROSPERO record.
- Search coverage, abstract screening and full-text decisions explicitly recorded as separate statuses.

## D. Retrieval — mechanism-first, not title-first
Search *independently* across these complementary families (see `SEARCH_QUERY_REGISTER_V1.csv`):
1. Transformer top-oil/hot-spot, life, ampacity, thermal rating with EV charging.
2. EVSE internal thermal physics, rectifier cooling/derating in high ambient temperatures.
3. Measured transformer–bus–EVSE electrical connectivity and monitored commercial charging stations.
4. Coupled power–transport dynamic propagation, resilience, electrical/mobility services.
5. PINNs, inverse physics, and physics-informed ML for transformer/EVSE/battery thermal systems.
6. Measured charging-session demand, fleet/depot service and departure-based outcomes.
7. Foundational transformer heat-transfer and validation papers without explicit EV wording (prevents search exclusion of core laws).

**Required target bibliographic collections:** Scopus, Web of Science Core Collection, IEEE Xplore, Engineering Village/Compendex, ScienceDirect and scholarly indexing of institutional/publisher literature (record inaccessible databases as *not searched*, never as searched). Supplement with Crossref/OpenAlex, publisher-site full text, Google Scholar documented citation chasing, technical project reports and standards.  
**Search date limit:** through 2026-11-03 inclusive in this first snapshot; no fixed earliest publication year in the initial comprehensive search. Record language, document type, date filters when actually applied; do not silently exclude non-English results.  
**No forced paper count:** earlier 325-paper corpus and 200-paper slots are *post-hoc coverage diagnostics*, not search universe or evidence of systematic completeness. Earlier 10 comparators are leads, NOT automatically eligible studies. FTEE v2 evidence-to-equation process should be adapted from superseded historical H1–H5 to frozen thermal SO1–SO3; preserve its evidence unit/traceability structure.

## E. Query quality and reproducibility
For every actual search store DB, platform, exact translated field-specific string, date/time (timezone), exact filters, retrieved count, file export (RIS/BibTeX/CSV), export SHA256, searcher and amendments. Use Boolean OR for synonyms within a concept, AND across independent concepts. Test a **pilot high-recall** query and a **precision** refinement; verify known strong primary papers appear as recall *diagnostic* after query design, not by inserting them into the results.
Apply PRESS peer review where available, and document if only self-audit performed. Save failed/limited database searches. Re-run/freeze the search near writing submission for recent papers; label initial and update cohorts separately.

## F. Eligibility — two different dimensions, not one arbitrary score
**Topical inclusion:** peer-reviewed studies and authenticated technical reports/standards with equations, field measurements, simulations, instrument data, charging services, coupled-system dynamics or method validation relevant to LRQ1–LRQ6. Reviews included as background/snowballing, but not counted as original field experiments.

**Topical exclusions:** unrelated charging marketing, general nonthermal congestion-only modeling, generic ML without thermal physics or relevant data; station-directory metadata with no relevant electrical/thermal result (except as traceable site leads). Explicitly record reason at full text.

**Evidence stratum (never merge):**
- F1: *single physically connected field site*, real transformer+EVSE thermal and grid-side electrical states, logged thermal causality and service timing; actual per-direction validation must be checked.
- F2: connected field site with partial electrical/thermal observations or only one direction; not a substitute for F1.
- F3: measured field transformer / EVSE / vehicle component from unrelated or standalone sites.
- F4: controlled laboratory experiment with measured equipment.
- F5: analytical/physics numerical/PINN/optimization modeling (may use some measured inputs, but field coupling not established).
- F6: review, technical guidance, standard or nonexperimental benchmark.
**Status:** at identification `CANDIDATE`; after decisions `INCLUDE`, `EXCLUDE`, `AWAITING_FULLTEXT`, `UNRESOLVED`. Papers may fit >1 stratum across different evidence units (e.g. component measured + modeled); classify each claim separately.

## G. Screening: no fabricated independence
1. Export and deduplicate by DOI first, then normalized exact title/year/authors; manually resolve ambiguous mergers. Preserve original identifiers and export provenance.
2. Title/abstract screening against explicit reasons; no full-text claim from abstracts.
3. Obtain primary full text, record page/section/equation/figure and exact date accessed. Missing papers classified `AWAITING_FULLTEXT`, not assumed negative.
4. Full-text inclusion and mechanism-specific admission, with reproducible exclusion codes (OUT_SCOPE, NO_THERMAL_MECHANISM, NO_POWER_TRANSPORT, NO_ORIGINAL_STUDY, DUPLICATE, INSUFFICIENT_PRIMARY_TEXT, OTHER).
5. Preferred: two independent human reviewers with conflict adjudication; if only one reviewer, use transparent single-reviewer status and independent spot-audit when possible. An AI-assisted screening opinion must never be reported as a second human reviewer.
6. Snowball forward/backward citations after database search; tag provenance so it is not miscounted as database retrieval.
7. Maintain unique **record** counts vs unique **study** counts; only generate PRISMA flow from actual run ledger. No invented denominator.

## H. Source-level evidence extraction (one claim/unit per row; CSV template supplied)
Fields: study DOI/title, publication/record version, work type, observation vs model, single-site physical topology (IDs and diagrams), asset rated/cooling type, heat forcing and duration, sensors/locations/units/sampling/timebase, electrical meter boundary and EVSE offered/request/delivered power, verified restriction/thermal reason, control/confounders, model equation + BC/IC + page, parameter and threshold source, physics conservation and dimensional verification, numerical method, independent train/validation/test/hardware split, baseline and error, uncertainty, data/file access, claim-to-SO, limitation, reproducibility/novelty.
For formula extraction record exact equation ID rather than inventing parameters. No universal temperature limits inferred from one charger.

## I. Quality appraisal: criterion-based, with evidence traceability
Six domains assessed independently (PASS/PARTIAL/FAIL/UNKNOWN; reason+primary text page):
1. Source and equipment authenticity: physical asset, measured vs inferred, data origin/license.
2. Mechanism/topology: same site, verified physical connection and P→T_e vs T_e→P distinction.
3. Confounding/reason codes: common ambient, SOC, background load, control/dispatch, battery taper.
4. Mathematical physics: mass/energy conservation, units, state definition, BC/IC, identifiable parameters.
5. Validation: field ground truth for claimed output; independent time/session/site holdout, no future input leakage; appropriate baseline; sensor uncertainty.
6. State-time/service: quantified thermal transition vs propagation lag vs service onset, requirements/delivered and recovery if claimed.
Do **not** sum these to fabricate one “quality percentage”; present evidence types and domain failures. Treat numerical/simulated results as numerical validation only.

## J. Synthesis and novelty audit
Deliver:
- Bibliographic corpus: DOI/resolved metadata, dedup, exact databases and search logs.
- PRISMA actual flow and full-text exclusion table (only when run).
- SO1–SO3 **mechanism × study × evidence stratum** matrix.
- Full-text evidence-to-equation extraction and comparison matrix (measured vs calculated vs modeled).
- Direct comparisons: transformer ODE/FVM/IEC model; EVSE thermal derating; coupling laws; temporal metrics; PINN/PIML vs ordinary physics and persistence; confidence limitations.
- Method-choice evidence matrix and dataset access checklist.
- Novelty sentence only with bounded corpus/date: “Within the searched/screened literature up to [date], [exact observed limitation] remains unverified.” Never claim global novelty solely because a search found no match.
- Narratively synthesize heterogeneity by equipment/cooling/ambient/measurement/validation. Quantitative pooling only if comparable definitions and sufficient studies.

## K. Supervisor-aligned physics versus data-informed ML decision gate
**Physics model is the base for all branches.** A PINN need not have experimental data to solve a forward PDE, but **an empirically supported physics-informed model** requires real measurements for calibration/independent validation and observable target states. No experiment => choose conventional numerical ODE/PDE with verification and parameter ranges; do not label PINN as field-validated. Cases:
- **A: no credible synchronized thermal/electrical measurements:** physics-based ODE/PDE and scenario/UQ only; no data-supported inverse/PINN claim.
- **B: valid component-level transformer or battery measurements:** separately test physics ODE/PDE, PINN inverse/hybrid residual and simple persistence on same held-out states; may validate component only.
- **C: valid connected, time-aligned transformer–EVSE field observations with restriction/service logs:** attempt joint physics-informed state/time coupling or PINN/hybrid and test P→T_e, T_e→P, service under matched conditions; compare with simpler physics baseline; accept ML only if it improves independent tests, has identifiable parameters, respects conservation, and UQ is adequate.
Baseline comparisons minimum: persistence; calibrated low-order thermal ODE; standard physics/FVM/IEC where appropriate; data-only regression where fair; PINN/PIML. Evaluate short- and multi-step forecasting vs **conditional hindcasts** with future observed covariates clearly labeled, time/site-separated splits and distribution shift. Beware that training collocation points are not physical observations. Standardized error, physical residual, threshold-event timing, calibration, sensitivity, computational cost, data-efficiency and uncertainty reported.
**Primary methodological readings:** Raissi et al. (2019), DOI 10.1016/j.jcp.2018.10.045; Karniadakis et al. (2021), DOI 10.1038/s42254-021-00314-5; Bragone et al. (2022), DOI 10.1016/j.epsr.2022.108447; Tang et al. (2024), DOI 10.1049/hve2.12435; other models require independently screened retrieval.

## L. Initial comparator list and fresh search separation
The 10 comparator leads in `project/data_qualification/2026-11-03/TARGETED_LITERATURE_THERMAL_PT_SYSTEMATIC_PROTOCOL_V01.md` are **leads** not already screened PRISMA inclusions. Additional close leads:
- Gong et al. (2015), DOI 10.1109/TSG.2014.2365452: 25-kVA transformer-life charging control and experimental thermal-model calibration; do not overstate field-connected EVSE temperatures.
- Bragone et al. (2022), DOI 10.1016/j.epsr.2022.108447: field ambient/top-oil/load factor as PINN thermal inputs and finite-volume comparison; not grid–EVSE coupled validation.
- Tang et al. (2024), DOI 10.1049/hve2.12435: transformer temperature-field PINN, determine actual measured vs modeled validation in full text.
- X. Xu et al. (2026), DOI 10.1016/j.segan.2026.102261: PINNs power-systems systematic review; background/method only.
- Fletcher & Khan 2025 RACE project: desktop Part 1, future instrumented Part 2 must be independently checked for updates.
**Avoid retrospective alteration** of the fresh query to force any named title into corpus. Use these as external recall diagnostics and additional snowball provenance only.

## M. Exit/acceptance criteria
- Reviewer-approved scope and searches, dated versioned query log, available database coverage and explicit coverage limitations.
- Exported primary records with dedup decision rules and reproducible nonzero counts, no invented PRISMA numbers.
- All highest-priority eligible close comparator full texts critically extracted with exact source locations; missing full text acknowledged.
- SO1–SO3 map and **what previous authors already did** statement; each mechanism's field/lab/simulation validity explicit.
- Decision document: conventional physics baseline required; PINN optional only after source-qualified real observation and honest heldout validation; refusal to upgrade unrelated component datasets to coupled field validation.
- Supervisor-ready 2–3 page evidence synthesis + full reference list (APA 7) once the screening actually completes.

**Related artifacts:** `SEARCH_QUERY_REGISTER_V1.csv`, `EVIDENCE_EXTRACTION_TEMPLATE_V1.csv`, `CLOSE_COMPARATORS_CANDIDATES_V1.csv`. No raw bibliographic records have been silently invented for PRISMA counts.
