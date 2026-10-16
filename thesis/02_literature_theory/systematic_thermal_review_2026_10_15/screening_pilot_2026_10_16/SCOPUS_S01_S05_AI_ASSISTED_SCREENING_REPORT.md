# Scopus 1–5: Initial systematic-screening work — 16 October 2026

**THESIS AUTHORITY:** `Engineering of Power–Electrified Transportation Interdependencies for Resilience`, extreme-heat thermal scope, frozen General Objective and SO1–SO3. This *literature-screening research artifact* does not change them.

**Status:** SEARCH RECORD DEDUPLICATION AND REPRODUCIBLE AI-ASSISTED FIRST-PASS PRIORITIZATION COMPLETED. **FORMAL INDEPENDENT TITLE/ABSTRACT SCREENING, FULL-TEXT SCREENING, PRISMA INCLUDED COUNT AND FINAL NOVELTY DECISION NOT COMPLETED.**

## 1. Corpus and exact stage accounting

Six original uploaded CSV files correspond to **five search strategies** (Search 5 required the additional 1970–2019 export). The repeat uploaded Search 2 CSV has the same SHA-256 and was not counted twice.

| Search corpus | Exported rows |
| --- | ---: |
| S01 Power–EV thermal interface | 3,009 |
| S02 Power-system thermal physics | 5,932 |
| S03 EV thermal behavior | 9,595 |
| S04 Mathematical and physical model methods | 5,108 |
| S05 original 20k CSV | 20,000 |
| S05 disjoint-year supplement, before within-S05 deduplication | 8,366 |
| Combined reconciled S05 EIDs | **23,054** |
| Total across **five concept searches**, counting S05 once | **46,698** |
| Duplicates **by Scopus EID across the five searches** | **9,322** |
| **Distinct Scopus EIDs** | **37,376** |

**Attention:** Two exports for S05 were not disjoint: 5,312 records overlap. That within-S05 overlap is removed *before* the 46,698 total above. An EID union does not resolve publication/preprint versions or missing/duplicate DOIs/near-duplicate titles; extra bibliographic identity QA remains.

No reported count above is a screened or included-study number.

## 2. AI-assisted high-recall triage, NOT eligibility decisions

All **37,376 distinct EIDs** were assigned automatically to one (mutually exclusive) *discovery* bin from title/abstract/keyword expressions. These bins do **not** establish inclusion or exclusion:

| Heuristic bin | Records |
| --- | ---: |
| A: high title-level Power+EV+heat co-occurrence | **71** |
| B: Power–EV+heat context in title/abstract | **1,573** |
| C: broader P–EV candidate / possible hidden interface | **1,233** |
| D: Power-system thermal components | **10,586** |
| E: Electrified transportation/EV thermal components | **10,775** |
| F: generic thermal methods/measurement | **4,614** |
| G: other or unresolved relevance | **8,524** |
| **Total** | **37,376** |

**The counts are a vocabulary-sensitivity diagnostic**, not a defensible tally of 2,877 eligible direct P–EV studies. Many keywords collide: `EV` in medicine, `transformer` as a neural model, `thermal power` as fossil generation, `transformer` inside EVSE (part of Tₑ not utility P). A source can have valid physics and still fall into a low bin; **do not automatically discard bins D–G before human verification**.

Scopus unique document types in input include **26 labeled Retracted**. Flag and verify retraction notices; no retracted paper should be counted as validated evidence.

## 3. Initial full-text request queue

[30 DOI-based candidates](PRIORITY_FULLTEXT_QUEUE_30.csv) with **15 P1 immediate**, 14 P2 next, and 1 P3 utility planning context. These are *selected reading priorities* based on available Scopus title/abstract evidence, not 30 fully read or formally included papers.

**High-impact counterexamples requiring earliest review:**

1. **2015 EV charging control + 25 kVA experimental transformer** — DOI `10.1109/TSG.2014.2365452`: experimentally calibrated transformer thermal control already exists. Audit whether actual P thermal limit actions and EV charging were jointly measured.
2. **2022 transformer monitoring + EV charging-current control** — DOI `10.1109/ECTI-CON54298.2022.9795360`: reports upstream oil/ambient state and EVSE commands. Check if limitation was temperature-activated or simply overload-related, and actual receiving observation.
3. **2023 EV-related transformer service disruption** — DOI `10.1016/j.segan.2023.101096`: assesses heat-related transformer operational failures. Test measured outage against modeled thermal consequence.
4. **2024 ambient-informed dynamic rating and EV demand** — DOI `10.1109/PESGM51994.2024.10688510`: prior dynamic transformer capacity with real EV charging profiles; assess physical validation.
5. **2023 ambient/charging distribution-network interaction** — DOI `10.1049/icp.2023.3126`: observed charging sessions and ambient exposure with grid consequences; test measured P state and EVSE derating.
6. **2026 Qatar fast charger experimental derating** — DOI `10.1016/j.ecmx.2026.101960`: prior Tₑ high-heat response, but P transformer receiver observations are unconfirmed.
7. **2017 genuine winding sensor validation** — DOI `10.1049/oap-cired.2017.1102`: valid P thermal-measurement baseline not a joint P–EV field test.
8. **2022 transformer PINN vs finite-volume** — DOI `10.1016/j.epsr.2022.108447`: PINN precedent with primarily numerical reference, not automatically field validation.
9. **2023 transformer grey-box based on actual lid-temperature sensors** — DOI `10.1016/j.segan.2023.101048`: P measurement/estimation model; distinguish lid from winding hotspot.

**Additional scientific novelty warning:** RACE for 2030 Fletcher & Khan 2025 (Project 23.ET8.R.0571, technical report) has already proposed a **temperature-driven transformer hot-spot charger-power constraint**. It is an important modeled P→Tₑ counterexample outside this 30-record Scopus EID queue and belongs in the cross-source synthesis.

## 4. Known-item sensitivity failures

Of 9 DOI-defined known relevant sentinels registered in [recall file](KNOWN_ITEM_RECALL_CHECK.csv), **7 appear**, **2 do not**:
- `10.1109/TSG.2023.3339374` — Balogun/EV-EcoSim (coupled grid/charging model).
- `10.3390/en11081937` — Trentadue charger temperature experiments.

Their absence from the five exported corpora is **NOT evidence they are outside Scopus or irrelevant**. It signals that this initial query set does not yet demonstrate sufficient coverage across key themes. Search new precise standalone concepts, adjust broad lanes and citation-chase; record why any recall miss persists. RACE is a separately indexed technical report and not expected to occur as an ordinary Scopus journal entry.

## 5. Physics/mathematics extraction contract for each P1 paper

Full-text reviewer must record page/equation-specific:

- **True physical boundary:** utility P transformer versus EVSE/BEV Tₑ, electrical/control interfaces and independent thermal source/receiver direction.
- **Governing laws:** Joule/core/switching heat losses; thermal resistances/capacitances or spatial conduction/convection/radiation; exact ODE/PDE/DAE, domains, units, initial and boundary conditions, energy conservation and parameters.
- **Evidence provenance:** direct temperature sensors (lid/oil/winding/rectifier), control/derating event flags, synchronized AC input, DC output, weather and actual service requirements.
- **Validation:** measured versus simulated targets, identification/calibration, independent heat/load holdout sessions, time lag vs causal identification, and quantified uncertainty/model domain.
- **SO3 services:** actual electricity delivery request or vehicle departure/trip obligation, not charging duration/power alone; time to physical thresholds, propagated limitations and recovery.
- **Novelty counterexample:** whether a given paper already models or measures the proposed mechanism. Unsupported direction must remain explicitly unsupported.
- **Method:** physics-only is baseline; PINN/grey box is conditional on actual observability and measured physical-target validation, not selected by name.

## 6. Integrity, licensing and next stage

Scopus CSVs contain original licensed abstracts and author/affiliation data. They were **analyzed locally**, not committed to this GitHub PR. The private repository stores only method, aggregate results and a **small 30-DOI prioritized bibliographic queue** without bulk abstracts. Original exports must remain under approved institutional storage until rights for third-party GitHub upload are established.

**Next actions:**
- Confirm exact executed query/search filters for S1–S4 and S5 year slice in Scopus Search History, before freezing PRISMA-S search log.
- Manually/in independently verify **all 71 high title co-occurrence records** and 30 P1/P2 candidates with documented eligibility judgments; resolve AI-related false positives and topic/physical boundary ambiguities.
- Obtain full texts for P1 studies and extract **physical equations, numerical/experimental targets and validation** using registered schema (see [rubric](SCREENING_DECISION_RUBRIC.md)).
- Repair sentinel misses with additional Scopus keyword lanes and backward/forward citation trails, especially full-text heat and EV-EcoSim.
- Continue systematic screening of the rest of 37,376 EIDs in batches, keeping each reviewer decision, exclusion reason and count. Do not fabricate completed PRISMA flow before this.

**Review status:** `DUPLICATE_EID_ACCOUNTING_DONE`, `HEURISTIC_TRIAGE_DONE`, `PRIORITY_QUEUE_CREATED`, `FORMAL_SCREENING_OPEN`, `FULLTEXT_VERIFICATION_OPEN`, `FINAL_NOVELTY_NOT_ESTABLISHED`.
