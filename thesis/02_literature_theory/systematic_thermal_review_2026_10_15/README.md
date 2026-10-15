# Thermal Power–Electrified Transportation systematic review — execution workspace

**Repository:** `Dossiya-SE/MSE-thesis`  
**Snapshot:** 2026-10-15  
**Research status:** **PROPOSED / NOT REGISTERED / DATABASE SEARCHES NOT RUN / NO MODEL SELECTED**  
**Branch status:** noncanonical research review materials; main-branch thesis authorities must not be silently rewritten.

## Why this exists

Professor Pat Phelan asked:
1. What have other researchers done, and has the literature been thoroughly reviewed?
2. Are suitable **experimental measurements** available to support physics-informed ML (including PINNs), or should the investigation remain physics-only?

This repository workspace documents a planned systematic evidence map, a focused critical synthesis of physical thermal mechanisms and candidate modeling methods, and an experimental-data feasibility audit. Its existence is **not** evidence that a systematic review has been completed.

## Current controlling thesis sources

- [Exact official title](../../../project/CANONICAL_THESIS_TITLE_V1.md).
- [Thermal-only Power–Electrified Transportation scope](../../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md).
- [Extreme-heat state-time amendment V4](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md).
- [SO1–SO3 frozen objectives](../../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md).
- [Electrified Transportation system boundary](../../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md).
- [State/time definitions](../../../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md).
- [Resilience definition](../../../project/CANONICAL_RESILIENCE_DEFINITION_V1.md).
- [Existing accepted core evidence](../02_00c_accepted_core_evidence.md), [Chapter 2 ontology](../02_00_literature_classification_ontology_register.md), [unresolved reading queue](../02_00d_deeper_research_and_reading_queue.md).

Active chain: **extreme heat → thermal state → thermally conditioned capability → qualified directional interdependency → state-time transition/propagation → electricity/mobility service consequence**.

EVSE is part of the **Electrified Transportation System**, not a third infrastructure system. Exogenous heat is not an internal state; correlation or shared weather exposure is not direct P→T or T→P causality. Sustainability is bounded downstream context and does not create extra primary objectives.

The older seven-stage framework is preserved as contextual/legacy methodology wherever superseded by current 2026-10-07/08 thermal scope authorities. The older Austin/flood case is not silently replaced.

## Contents

- [PROTOCOL_V1_PROPOSED.md](PROTOCOL_V1_PROPOSED.md) — full draft protocol: scope, questions, search streams, screening, extraction, data-readiness and model-selection gates.
- [REVIEW_EXECUTION_GUIDE_SOURCE_2026_10_15.md](REVIEW_EXECUTION_GUIDE_SOURCE_2026_10_15.md) — saved source of the companion step-by-step guidance (including original source-paste formatting).
- [trackers/README.md](trackers/README.md) — audit constraints and eight CSV worksheet projections.
- [trackers/](trackers/) — search log, screening decisions, original-PDF evidence register, dataset audit, model comparison, PRISMA counts and search sentinel bibliography.

**Binary workbook:** `Thermal_PT_Systematic_Review_Execution_Tracker_2026-10-15.xlsx` was checked locally (valid 8-sheet ZIP/XLSX, SHA-256 in tracker README). The connected GitHub writer in this workflow cannot upload the binary from the local environment; the CSV files are a text projection, not an .xlsx copy.

## High-rigor gates

| Phase | Evidence required for passing |
| --- | --- |
| Protocol | Scope, RQs, criteria, searches, exclusion rule, planned independent screening and version changes documented |
| Retrieval | Exact database/interface/query/filter/run-date; exported RIS/BibTeX/CSV; measured result counts |
| Screening | Deduplog, eligibility decisions and reasons, full-text access failures |
| Primary PDF | Opened original/version; page/section/equation/figure/table-anchored support and limitations |
| Raw data | Real files opened; units, timestamps, sensors, temperature coverage, equipment keys, licenses, missingness |
| Identification | Observable states and parameters, excitation/identifiability checks, heat-event/session/site holdout |
| Modeling | Baseline physical model; conditional grey-box; conditional PI-ML/PINN; matched task/splits/uncertainty |
| Synthesis | Explicit boundary between published evidence, inferences, simulations and qualified empirical claims |

**No evidence gates have been marked passed by this commit.** Current `NOT RUN` and `SEED ONLY` markers must remain until actual work is logged.

## Decision rule

- Missing/inadequate measured trajectories: **physics-only with bounded parameters and simulation claims**.
- Sufficiently informative measured inputs and states/outputs: **calibrated grey-box** as first empirical comparator.
- Rich data and demonstrable independent gains: **PI-ML/PINN** candidate against physics, grey-box and appropriately matched baselines.
- No component-level evidence is automatically a field validation of the end-to-end coupled power–transportation service chain.

## Review before adoption

Request Professor Phelan's review of the proposed protocol. Once approved, version changes, execute searches, enter true counts, assess original PDFs and datasets, then define the smallest defensible modeling task.

**All contents saved for review only. No canonical thesis file was changed by this branch commit.**

## Phase 1 pilot activity — 2026-10-15

A six-stream public indexed-web pilot was **actually executed** and recorded under [pilot_2026_10_15/](pilot_2026_10_15/). It includes exact query texts, topic/data leads and source-visible preliminary evidence. Six Elicit searches were **blocked by account-level API denial**; Scopus, Web of Science, IEEE Xplore and Compendex are **still NOT RUN**. The public-search tool merges retrieved results and supplies no per-query exhaustive hit counts, so no PRISMA counts or completed systematic-review status can be inferred. Original PDFs and raw experimental time series were not opened by this pilot.

## Phase 2 search-readiness preparation — 2026-10-15

Prepared [phase2_search_readiness_2026_10_15/](phase2_search_readiness_2026_10_15/) with **28 unexecuted candidate field-syntax strings** for Scopus, WoS, IEEE Xplore and Compendex, official syntax-source links, separate known-item broad-query recall worksheet and live execution checklist. Provider syntax documentation was reviewed, but there was **no authenticated database execution or raw bibliographic export**. The query translations are `DRAFT / NOT TESTED`, not finalized protocol amendments.

## Original-PDF text verification — 2026-10-15

The first source-level paper audit is in [original_pdf_audit_2026_10_15/](original_pdf_audit_2026_10_15/): **3 actually read original PDF artifacts**, including **2 publisher versions of record and 1 explicitly versioned arXiv author manuscript**. It records 19 source-anchored scientific claims, page/equation/table links, validation boundaries and each of the 15 pilot leads' access status. Figure pixels were not visually rendered because PDF screenshot requests failed; raw time series are uninspected; all pilot leads remain **NOT SCREENED** for systematic review. This source verification is independent of PRISMA inclusion and does not unfreeze the modeling method.

## Second priority source-verification follow-up — 2026-10-15

See [priority_followup_audit_2026_10_15/](priority_followup_audit_2026_10_15/). **P008 Godina publisher-version PDF was read in full-text extraction (12 PDF pages including portal cover); P010 Villarroel complete original publisher HTML read but PDF not obtained; P001 Krama official publisher abstract confirmed, third-party 16-page text copy consulted but NOT original-PDF certified.** 12 newly anchored claims are recorded with sensor, evidence, and mathematical provenance; no raw data or complete figure visuals obtained. Cumulatively **4 original scholarly PDF artifacts have been text-read among 15 pilot leads**, **one extra publisher-indexed article text source** and **one extra third-party transcription at lower certainty**. Of 15 pilot leads **11 still lack original PDF text verification**; none has been systematically screened for inclusion. PRISMA counts and final modeling choice remain open.
