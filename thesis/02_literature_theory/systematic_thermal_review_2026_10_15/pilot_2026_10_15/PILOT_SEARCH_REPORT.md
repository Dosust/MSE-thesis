# Phase 1 — Six-stream pilot search execution report

**Date:** 2026-10-15  
**Branch:** `research/systematic-thermal-pt-review-protocol-20261015`; draft PR #84.  
**Status:** `PILOT SEARCH COMPLETED ON PUBLIC INDEXED WEB` / `ELICIT BLOCKED` / `SUBSCRIPTION DATABASE SEARCHES NOT RUN` / `FORMAL SYSTEMATIC SCREENING NOT STARTED`.

## Aim and frozen scope
Pilot the six complementary thermal-only retrieval lanes against known direct thermal, component electrothermal, and coupling studies. The active governing thesis has SO1–SO3; the systematic review must not activate the superseded general RQ1–RQ7 contract, assume PINN selection, or declare simulated results as experimental field validation.

## Executed tools and transparency
- Public indexed web search: **6 specified lane queries**, plus **6 topic/data follow-ups**, **4 DOI-targeted known-item checks** and **3 additional exact-identifier checks** on 2026-10-15. Exact query strings and status are in `PILOT_QUERY_LOG.csv`. Search returns were **merged/top-ranked surfaces**, so the count of hits *per query* is not available, and no search-service bulk export was provided. This supports discovery and known-item findability, not reproducible exhaustive database coverage.
- Elicit academic index: six lane queries submitted in semantic mode requesting 20 articles each. **All six were blocked** because this connected Elicit plan lacks API access. Results: **none**, not zero matching studies.
- Scopus, Web of Science, IEEE Xplore and Compendex: **NOT RUN**. No subscription access or database result exports established.
- Publisher pages: substantive source snippets surfaced; direct `open` attempts on Elsevier publisher articles returned **403**, one MDPI direct page returned **429**. A repository PDF link led to `request-a-copy`, not a verified PDF download. **No original PDF read or page-level extraction was performed in this pilot.**
- **PRISMA counts remain BLANK/UNKNOWN**. Candidate leads are not a screened corpus. The papers in the CSV are NOT included/excluded studies.

## Six lanes — pilot outcome and refinement

| Lane | Status | Source-visible examples | Proposed query correction before approved systematic search |
| --- | --- | --- | --- |
| L1 Direct P–T_e thermal | Public pilot executed | [Godina et al. 2016](https://doi.org/10.1016/j.enconman.2016.04.087), [Ramos Muñoz et al. 2016](https://doi.org/10.1016/j.energy.2016.07.122), [EV-EcoSim 2023](https://doi.org/10.1109/TSG.2023.3339374) | Run two subqueries: explicit ambient-heat P–T_e interactions; and EV-charging load → transformer thermal stress. Search direction separately to avoid assuming symmetry. |
| L2 EVSE thermal | Executed | [Krama et al. 2026](https://doi.org/10.1016/j.ecmx.2026.101960), [KIT measured charging data](https://doi.org/10.5281/zenodo.17866847) | Include rectifier heat sinks, cooling, protective power limits and input-versus-output power; do not demand heatwave token in every query. |
| L3 Transformer thermal | Executed | [Villarroel et al. 2017](https://doi.org/10.1049/oap-cired.2017.1102), [Blomgren et al. 2023](https://doi.org/10.1016/j.segan.2023.101048) | Separate physical calibration/thermal rating from statistical forecasting and PINN; include IEC/IEEE-based transient hot spot and top-oil. |
| L4 EV battery thermal | Executed | [Mannapperuma et al. 2025](https://doi.org/10.3390/batteries11090319), [Schreiber et al. 2026](https://doi.org/10.1016/j.etran.2025.100518) | Differentiate controlled cell tests from vehicle/fleet pack data; retain observed temperature ranges and charger interface. |
| L5 Model methods | Executed | [Bragone et al. 2022](https://doi.org/10.1016/j.epsr.2022.108447), [Tang et al. 2024](https://doi.org/10.1049/hve2.12435), [Blomgren et al. 2023](https://doi.org/10.1016/j.segan.2023.101048) | Add independent physics-only thermal identification/finite-volume baselines; require common held-out target for comparative evaluation. |
| L6 Service consequences | Executed | [Krama et al. 2026](https://doi.org/10.1016/j.ecmx.2026.101960), [EV-EcoSim 2023](https://doi.org/10.1109/TSG.2023.3339374) | Split charger-session effects (offered/delivered power, completion time) from actual mobility-service outcomes (trip completion, schedule adherence). |

## What the known-item checks DO and DO NOT establish
The public pilot and targeted identifier checks located 9 thermal/coupling-relevant sentinel documents (`S02–S10`), but **some required exact DOI-targeted follow-up**. `S01` (Rinaldi) and `S11` (Doyen/De Lara) were **not checked** because they are background/contextual mathematics. **Do not report recall = 9/9** for an independent query design; running a search for a known DOI does not test broad-query sensitivity. Instead maintain `SENTINEL_SOURCE_CHECK.csv` and perform genuine per-stream known-item recall tests on the final authenticated database search.

## Core outcome (pilot only)
- Field experiments exist for **charger heat derating** and **transformer temperature** separately.
- A prior model explicitly examined **EV charging load → transformer thermal aging** using measured real-world input profiles.
- Coupled grid/EV charger multi-physical co-simulation already exists, so broad interface/coupling claims are not novel by themselves.
- PINN thermal transformer precedent exists, but one studied simulator-generated reference temperatures. A PINN using field boundary conditions may still be primarily benchmarked against numerical solutions, not independent measured internal fields.
- No **directly instrumented same-equipment same-time transformer ↔ EVSE ↔ mobility-service** joint dataset was verified from the surfaced sources. This is a **search observation**, not a proof such data do not exist.

## Formal next gates
1. Advisor review + PRESS-like peer check of translated syntax in Scopus/WoS/IEEE/Compendex; if no access, state source/coverage limitations or secure exports.
2. Execute each database field search, export full native results with timestamps and real hit counts.
3. De-duplicate based on DOI/persistent identifiers, track duplicates/preprints, independently screen when feasible, and record full-text exclusions.
4. Obtain original PDFs for priority studies and extract exact equation, figure/table and instrumentation/held-out validation anchors.
5. Open raw experimental files, verify licenses/timestamps/actual heat excursions and physical cross-interface keys; assess identifiability.
6. Only then commit to physics-only, calibrated grey-box, or PINN as a model family and design matched tests.

## Scientific governance
This is an **unapproved exploratory pilot**, not a completed SLR or a registered protocol. Do not modify frozen thesis authorities, misreport PRISMA counts, promote pilot records to the accepted evidence corpus, or assert empirical superiority of grey-box/PINN.
