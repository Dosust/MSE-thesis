# S0 integrated Scopus search and eligibility protocol — version 0.1

**Drafted:** 2026-11-05 | **Status:** **PROPOSED / retrospective local text check complete; native Scopus validation and protocol approval pending**. This is a dated amendment to the preexisting review protocol; it is not retrospective preregistration.  
**Thesis:** *Engineering of Power–Electrified Transportation Interdependencies for Resilience*.  
**Scientific boundary:** heat-conditioned dynamic interdependencies between electrical power and electrified road transportation, including transformer and EVSE/battery interfaces, physical state, time, resilience and electricity/mobility services.

## A. Why add integrated search S0?

Arizona State University Library recommends building a sensitive, multi-line primary-database search and translating it to other databases. **S0 is the direct coupled-system core search only; the existing twelve A0–F1 physics, method, standards and service searches remain unchanged as complementary sensitivity searches.** Do NOT combine all six thematic block requirements with AND. All raw original files and search provenance remain intact. The earlier 2026-11-03 v0.2 protocol's separate thematic searches are preserved; S0 is an explicitly dated addition pending supervisor approval.

## B. Review type, questions and PCC

**Conduct:** JBI-informed systematic scoping review/evidence map plus a more stringent equation- and validation-focused critical engineering synthesis, not a meta-analysis by default.  
**Population/participants (P):** power distribution networks/feeders/transformers, EVSE, electric vehicles and batteries, electric buses and charging depots; coupled and component-level thermal systems.  
**Concept (C):** thermal/electrical states, equipment capacity/temperature limits, directional EV charging ↔ electrical network mechanisms, physical ODE/PDE/heat balances, experimental observations, uncertainty and state estimation, transition and service effects.  
**Context (C):** extreme ambient heat is the focal stressor. Baseline and moderate-temperature physical validation studies stay eligible as comparators, coded accordingly, not falsely described as extreme-heat experiments.

**SLR-Q1 / SO1:** Which P→T and T→P physical mechanisms, electrical connections and thermal states are qualified?  
**SLR-Q2 / SO2:** Which governing equations, heat-transfer laws, constraints, numerical methods and parameters support dynamic time/state modeling?  
**SLR-Q3 / SO2:** Which thermal and electrical variables are actually measured and independently validated, at what sampling resolution/conditions?  
**SLR-Q4 / SO3:** Which predicted or measured critical times, delays, charging limitations, electricity and mobility service effects follow from thermal restrictions?  
**Novelty question:** What closest prior work and counterexamples limit any claimed novelty?

## C. Eligibility rules (do NOT finalize without human reviewer calibration)

A record is provisionally eligible for **CORE** when it studies the **real electrical power–electrified transportation connection** and provides an evidenced or clearly modeled physical heat-dependent mechanism, restriction, time behavior or consequence relevant to ≥1 SO.

A record is provisionally eligible for **SUPPORTING PHYSICS/METHOD/DATA** when it supplies transferable validated transformer or distribution heat-transfer laws; EVSE or battery electrothermal laws, loss and derating mechanisms; observable measurements, calibrated parameters; or a relevant physically constrained modeling method. **A study need not mention both P and T to be supporting**; it must explain its transfer to the coupled problem and not be confused with validated interface evidence.

A record may be **CONTEXT/SERVICE** when it establishes power–transport demand, connectivity, load profiles, deadlines/traffic or service constraints relevant to model forcing, but does **not** prove the thermal mechanism. Preserve context as such; avoid inflating the core direct-coupling evidence count.

Retain **REVIEWS/BOOKS/STANDARDS** as separately coded background, normative baseline and citation-chaining sources where relevant, not as independent primary observations unless original data are extractable and verified. Mark simulation, laboratory, field, open benchmark, technical standard, review and original report separately. Preprint vs published and report-version relation must be documented.

### Inclusion criteria

I1. Publication between 2000-01-01 and 2026-12-31 in planned primary database searches, subject to actual search date; older foundational studies may be added separately through citation chaining and reported outside S0 date-limited counts.  
I2. Any language at search stage; pursue reliable translation when feasible, and report full-text language limitations.  
I3. Relevant to **at least one** defined review objective or a transferable thermal physical/mathematical evidence role, with explicit relevance justification.  
I4. Obtainable title/abstract for first-pass screening, or uncertainty flagged; full-text confirmation needed for evidence extraction and final inclusion when possible.  
I5. Research studies may be analytical, simulation-based, numerical, experimental, field-observational, mixed, or original technical reports; assign evidence type and validation strength without assuming measurement.

### Exclusion criteria and codes (human-confirmed only)

E01 Wrong physical system: e.g. only fusion superconducting magnets with no defensible transferrable element.  
E02 No thermal physical, transfer-method, qualifying interface or service-context relevance to any SO.  
E03 Purely economic, cyber, pricing, siting or generic AI optimization without a defensible physical or service input to the thesis; *check full text if title/abstract ambiguous*.  
E04 Secondary/non-original source offered as field measurement; **reclassify as context/standard/citation source** rather than automatically discard if informative.  
E05 Insufficient methodological traceability/metadata to establish the claimed contribution after retrieval attempts; maintain reasons and limitations.  
E06 Out of approved temporal boundary in main search (foundational older references flagged separately).  
E07 Confirmed duplicate **bibliographic work** after identity review; preserve every alias EID, DOI and original search occurrence.

**Do not exclude solely because:** it covers only SO1, only SO2 or only SO3; it is a negative/counterexample result; it is not in English; it is a single-component comparator; it was returned by multiple searches; it lacks extreme-heat ambient forcing while giving transferrable measured physics. All require proper strata/labels.

## D. S0 query construction

S0 = P (grid/transformer) AND T (EV/charging/mobility) AND H (thermal mechanisms or operating limits); publication year 2000–2026. Search title, abstract and indexed/author keywords. Do not require the terms “extreme heat”, “resilience”, “PINN”, or “validation”: making them mandatory would make S0 miss physically important studies. Do not add subject/language/document type filters. See **S0_SCOPUS_ADVANCED_PROVISIONAL_QUERY.txt** for exact paste-ready string. Scopus syntax relies on field tags and explicitly parenthesized OR groups; however **Scopus has not executed or accepted this string yet**. Exact date, server-reported hit count and native result set are `PENDING`.

## E. Retrospective local validation (NOT a live Scopus search)

We checked literal phrase/single-word proxies on TITLE, ABSTRACT, AUTHOR KEYWORDS and INDEX KEYWORDS of the existing EID-deduplicated 23,862-record Scopus union. The proxy approximates Scopus field matching; it does **not** reproduce Scopus tokenization, lemmatization, hyphen parsing, indexing, or coverage outside the union. The calibration used known records while developing the query, so it is **not held-out external validation**.

- Five assistant-identified **core** pilot records: **5/5** matched the local S0 text proxy.
- Six assistant-identified **supporting** pilot records: **2/6** matched; missing cases are primarily single-component physics or service/context without explicit thermal vocabulary and remain reachable through A0–F1.
- 25-record pilot overall: **10/25** matched (the pilot includes deliberate irrelevant cases).
- **1,737 of 23,862** preexisting unique EIDs matched the local text proxy. This is **not** a native Scopus hit count, an external recall estimate, an inclusion count or a PRISMA denominator.
- The reference comparator audit includes Pan, Bragone, Krama, Hilshey, Soltani and pilot core papers; a component paper's S0 non-retrieval is not grounds for exclusion.

**Scientific interpretation:** This provides internal syntactic/sensitivity assurance on five known core titles/abstracts only. Real Scopus validation and calibration against independent benchmark studies still **PENDING**. No independent reviewers have approved the criteria.

## F. Native Scopus validation and completion gates

1. **Reviewer signoff:** supervisor/review team approve review type, PCC, inclusion/exclusion rules and use of an S0+complementary-block strategy, log version/date/signatories. If no signoff, mark explicitly PENDING.  
2. **Native execution:** paste the exact query in Scopus Advanced Search, confirm it parses; capture screenshot or native search history showing **database=Scopus, platform=Elsevier Scopus, search local date, full exact query, limits, hit count**, and record any Scopus-reported query modifications. Do not treat an offline proxy as native execution.  
3. **Seed recall check:** check each known core DOI/EID using native Scopus presence and S0 result membership, including Hilshey, Gong, Pan and pilot five. Distinguish **indexed but not retrieved by S0**, **not indexed**, and **search/syntax mismatch**. Test extra independent seed set, with held-out selection recorded before modifying the query. Revise only with versioned change log, explain misses, and rerun/retest.  
4. **Original export:** save untouched CSV/RIS (all available metadata), filename `SCOPUS_S0_YYYY-MM-DD_original.csv`, exact bytes/hash/size, date and native hit count; reconcile export rows to native hits including platform limits.  
5. **Multi-source translation:** translate concept logic, not verbatim Scopus syntax, to IEEE Xplore, Web of Science and Engineering Village where accessible. Record exact database/platform-specific queries, dates and hits. Grey literature, standards and backward/forward citation searches are separate and logged.  
6. **Consolidation and dedup:** merge S0 with all A0–F1 searches plus subsequent database records. Preserve source EIDs, aliases, full search provenance and DOI. **15 different-EID/shared-DOI groups and 104 same-title/year groups await identity checks.** A confirmed work counts once; one work may fulfill several SO roles.  
7. **Human screening:** two independent reviewers pilot the preselected 25 cases **without seeing assistant recommendations**; log decisions and reason codes, resolve disagreements, then screen whole consolidated corpus at title/abstract and full text. Keep `UNCLEAR` for missing evidence, not automatic exclusion. Define acceptable single-reviewer deviation transparently if independent reviewers unavailable.  
8. **Evidence synthesis:** for each eligible work extract equations, boundary conditions, physical network and causality, time constants, validated parameter sources, experimental context, instrument/sensor data, scenario temperature, cooling/derating, service metrics, uncertainty, simulation-vs-observation and evidence page. Full reported search and study flow follow PRISMA-ScR/PRISMA-S.

## G. Source records and authoritative methods

- [ASU Library — Planning a search strategy](https://libguides.asu.edu/evidence_synthesis/search-strategy) — single comprehensive multi-line primary strategy and database translation.  
- [ASU Library — Running/exporting searches](https://libguides.asu.edu/evidence_synthesis/exporting-citation-management) — record database/platform/date/exact string/filters/hits.  
- [JBI Manual — three-step search process](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/653099013/2.4.2%20The%20JBI%203-Step%20Search%20Process) — explore, expand, chain/check citations.  
- [Elsevier Scopus — Advanced search](https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search) — TITLE-ABS-KEY and Boolean syntax.  
- [PRISMA-S search reporting extension](https://doi.org/10.1186/s13643-020-01542-z) — exact executed query, database, platform, limits, dates and exported counts.  
- Existing ASU thesis SLR methodology audit 2026-11-05 (project-local) and 15 DOI multi-role decision; originals A0–F1 unchanged.

## H. Decision/status record

| Decision item | Status at 2026-11-05 | Reason |
|---|---|---|
| S0 integrated P∧T∧H query constructed | DRAFT COMPLETE | Transparent 3-block strategy |
| Five core pilot records in local text check | 5/5 INTERNAL PROXY | Not Scopus-native and not independently held out |
| ASU/JBI/PRISMA-S search reporting rules documented | DOCUMENTED | Method guidance, not ASU-specific compulsory S0 rule |
| 12 preexisting A0–F1 searches | RETAIN UNCHANGED | Component evidence and audit provenance |
| 15 DOI identity checks / 104 title/year groups | PENDING HUMAN REVIEW | Never silently merge/remove records |
| Native S0 Scopus execution / hit count | NOT EXECUTED / UNKNOWN | Needs institutional Scopus access |
| Human reviewer calibration/approval | PENDING | Prevent pseudo-eligibility decisions |
| S0 query as final frozen systematic search | NOT YET | Requires native seed recall and versioned refinement |
