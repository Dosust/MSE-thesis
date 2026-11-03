# Systematic review — Day 1 execution status and next actions

**Date:** 2026-11-03. **Thesis:** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience.

## What was actually accomplished today

- Created canonical [one-review hub](./README.md) linking the official eight-work-package plan, 44 tasks, prior 17 seed references, draft systematic protocol, and blank formal search/screening/extraction audit templates. The older scientific review files were **not** deleted or overwritten.
- Created [C1–C6, F1–F7, S0–S6 codebook](./CLASSIFICATION_CODEBOOK_V01.md) distinguishing a paper's topic, claim-specific evidence type and **our** review completion.
- Ran a **bounded pilot** of six indexed-web discovery queries (A–F). These returned a merged ranking—not a database-native, per-query complete bibliography. Logged the exact queries and provenance in [pilot access log](./PILOT_SEARCH_ACCESS_LOG_2026-11-03.csv).
- Ran one **Wiley Scholar Gateway** fulltext relevance search with known returned output: **12 passages from 10 articles**, 2012–2026. This is passage-level relevance discovery, *not* 10 formally screened papers or a Wiley corpus-wide total; actual primary text must be verified.
- Attempted one Elicit scholarly search; **blocked** with explicit \`api_access_denied\` (current plan lacks API access). No Elicit search, review session or count is claimed.
- Consolidated **17 existing bibliographic seed records** with **eight additional publisher-discovered candidates** into [25-row pilot reference register](./PILOT_SOURCE_REGISTER_2026-11-03.csv). Each source has a unique provisional ID, C1–C6 primary/secondary tags, claim-level evidence caveats, access status, source maturity and a flag \`prisma_countable=NO\`. The 25 is a *working-seed total only*, **NOT a systematic inclusion count**.
- Conducted **text/equation-level source extraction** of (i) Bragone et al. 2022 transformer thermal PINN and (ii) Acker, Hofmann and Konrad 2025/26 battery/coolant measured-data and NMPC paper; records and source equation references in [day-1 source audit](./EXTRACTION_BRAGONE_ACKER_DAY01_2026-11-03.md). No new numerical reproduction/independent validation was claimed. Bragone original PDF screenshot endpoint failed; figures still require visual source review.

## Three defensible scientific findings

1. **No novelty in applying PINNs to transformer thermal prediction by itself.** Bragone 2022 already incorporated measured transformer load/ambient/top-oil into a one-dimensional heat-diffusion PINN and compared it to FVM. Their conclusion states that under the available data setup PINNs **did not outperform FVM**; field boundary top-oil used in training is not an independently forecast thermal distribution. DOI: https://doi.org/10.1016/j.epsr.2022.108447 .
2. **Physically detailed vehicle battery/coolant heat balances already exist.** Acker et al. 2025 online/2026 volume use battery heat \(R_\mathrm{int}i^2\), measured coolant circuit/flow and ambient terms, and parameter fitting from production BEV measurements. Their controller improvement is evaluated using a validated simulation model, not an observed grid-connected transformer–EVSE experiment. DOI: https://doi.org/10.1007/s41104-025-00157-7 .
3. **Power–transportation planning and thermal ratings already have close predecessors.** Reviews and 2025 studies cover multi-timescale P–T planning, dynamic thermal rating of cables/transformers with EV response, and simulated service resilience. This reinforces the need to test the narrow **actual interface, time delays, service observations and external transfer** novelty hypotheses rather than claim that coupled system methods are generally new. Example: https://doi.org/10.1049/hve2.70024 ; https://doi.org/10.1049/enc2.12034 .

**Open scientific question:** No verified original paper/dataset acquired in today's pilot proves a single field-installed, synchronized P↔EVSE internal thermal transformer-charger-vehicle interface and its measured mobility-service effects. This is not evidence that no such study exists globally; systematic counterexample search is required.

## Milestone ledger: status must reflect work, not plan volume

| Work package | State after Day 1 | What blocks a claim of completion |
|---|---|---|
| WP1 review governance | **PARTIAL** | Dated protocol freeze; platform-ready exact queries, screening scope and reviewer process |
| WP2 literature discovery | **PILOT EXECUTED** | Formal accessible database searches with exact query strings, all records, dates, total hits and reproducible exports |
| WP3 study selection | **NOT STARTED FORMALLY** | Dedup of formal records; title/abstract/fulltext screening; genuine PRISMA-ScR flow |
| WP4 source/equation extraction | **TWO PRIMARY SOURCES PARTIAL** | Full source-page/figure checks, all eligible papers and measured-v-simulated appraisals |
| WP5 critical synthesis | **EARLY COMPARATOR FINDINGS** | Closest counterexample for every proposed research gap; domain coverage |
| WP6 experimental data | **PREEXISTING PARTIAL AUDIT** | Actual connected system field measurement; TUM code decoding; raw Qatar/other data |
| WP7 physics vs PINN decision | **NOT DECIDED** | Independently benchmarked and qualified physical model; matched PINN/gray-box trial if admissible |
| WP8 research reporting | **NOT COMPLETE** | Review manuscript, source-linked bibliography and supervisor-ready answer |

## Immediate follow-on in exact order

1. **WP1 protocol lock:** ensure research questions LQ1–LQ6 and C/F/S codebook are approved internally as a version/date; no supervisor endorsement assumed.
2. **WP2 reproducible bibliography:** run exact supported **Scopus, Web of Science, IEEE Xplore, Engineering Village** queries if access; use open scholarly bibliographic sources where accessible and explicitly identify differing database coverage. Export citation metadata and record source count/hash and seed recall. **No fabricated counts**.
3. **WP3 screen:** normalize DOI and title, detect same-study report families (e.g. Bragone journal/IFAC conference), and screen actual search corpus independently or with declared single-reviewer limitations.
4. **WP4 deeper paper audit:** finish visual Bragone diagrams and source boundary/units, source-specific RACE dynamics, Qatar charging thermals, Li bus-transformer interface, Cao neural Transformer, and Acker empirical validation.
5. **WP5 novelty:** test F1/F2 connected-site evidence by seeking explicit transformer feeder topology, EVSE rectifier heat, charging state/load, temperature and restriction reason codes and actual service outcomes.
6. **WP6+WP7 parallel:** qualify SINTEF/TUM/EVSE measurements and construct comparative pure-physics baseline with fair validation before attempting PINNs.
7. **WP8:** release review report and concise response to Prof. Phelan only after evidence gates, with honest limitations.

## Data and ethics controls

Original measurements remain in their source locations; do not merge SINTEF Norway, Slovenia station, TUM Germany and Qatar EVSE logs into a fictitious single same-site experiment. Pilot abstracts and scholarly passages do not prove original equations or full experimental validation. Do not upload copyrighted articles or licensed commercial bibliographic exports publicly. Record original sources with DOI and page references, source access restrictions, native exports and hashes. Retain null/blocked states where data or database access is unavailable.

**Review flow:** Define → Search → Screen → Retrieve → Extract → Verify → Compare → Synthesize → Gap → Data QA → Model decision → Validate → Report.
