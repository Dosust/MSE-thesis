# Research milestones and evidence-acceptance gates

**Status at start 2026-11-03:** Protocol v0.1 and first public-web seed identification available. **Not yet a PRISMA-counted systematic search** and not an empirical coupled system validation.

## Work completed to start the systematic review

| Gate | Requirement | Status as of 2026-11-03 | Evidence |
|---|---|---|---|
| G0 | Scope grounded in frozen SO1–SO3 | DONE — draft protocol scoped | PROTOCOL_V0_1.md |
| G1 | A–D search concepts and database query drafts | DONE — draft, not run on paid databases | SEARCH_STRATEGIES_V0_1.md |
| G2 | Executed discovery log | DONE — 9 public-web pilot searches with no exhaustive hit totals | SEARCH_EXECUTION_LOG.csv |
| G3 | Seed literature and type classification | DONE — 27 records, 18 prior + 9 new, not formally included | FIRST_PASS_SEED_REGISTER.csv |
| G4 | Predeclared extraction and appraisal rubric | DONE — empty study-level template and written criteria | EVIDENCE_EXTRACTION_TEMPLATE.csv, PROTOCOL_V0_1.md |
| G5 | Search calibration and formal exports | NOT RUN | Each Scopus/WoS/IEEE search requires access and exact export |
| G6 | DOI/title deduplication | NOT RUN | Record immutable master export before computing counts |
| G7 | Independent title/abstract and full-text screen | NOT RUN | Human second reviewer required to claim independent double screening |
| G8 | Primary study equation/sensor extraction | NOT RUN systematically | Must cite exact full-text figure/table/equations |
| G9 | Engineering evidence and V&V concern appraisal | NOT RUN systematically | LOW/SOME/HIGH/NOT REPORTED/N/A per domain |
| G10 | Structured qualitative synthesis and gap proof | NOT RUN | Separate matched field/site and simulated systems |
| G11 | PRISMA 2020 reporting and diagram | NOT RUN | Only fill counts after actual exports/screening |
| G12 | Supervisor audit and frozen protocol/decision | NOT RUN | Record signed/acknowledged version, modifications, reviewer comments |

## Immediate high-priority research decisions

### A. Which thermal mechanism is already supported?
- Power-system equipment: independently measured transformer temperature with load and ambient (SINTEF). **Cannot** transplant exact coefficients to another transformer without site verification.
- Transportation equipment: KU Leuven battery states and EV electrical boundaries are measured, but **internal EVSE thermal states are not**.
- Charger extreme heat: Qatar 50 kW charger field paper measures internal rectifier and ambient, offered/delivered power, with raw data available on request. It is **charger-only**, not an experimentally verified SINTEF transformer–EVSE same-site connection.
- Coupled system: qualifying a literature article that actually verifies same physical feeder and measured thermal states on both devices is the **highest-value evidence question**.
- Mathematical transfer: if comparable measured sites are absent, evidence supports mathematical mechanism definitions and conditional sensitivity, NOT independent transfer validation.

### B. Exact article-level next test
For every candidate paper we must establish: 
(1) original empirical vs theoretical vs simulated results, 
(2) actual system/transformer/EVSE IDs and electrical connection,
(3) thermal state instrumentation and physical placement, 
(4) time resolution and alignment, ambient extremes and disturbances, 
(5) thermal law and units, 
(6) training calibration and genuine holdout, 
(7) parameter identifiability/UQ, 
(8) propagation/service observations, 
(9) independently demonstrated transfer and original data/code availability.

### C. Formal search/test next operations
1. Validate draft searches against seed articles to check retrieval sensitivity; revise and version **before locking queries**.
2. Run each eligible database/platform, record exact executed query, filters, retrieval count, export and SHA-256. Scopus/Web of Science access must be documented; if unavailable, report it, do not invent comprehensive coverage.
3. Deduplicate exported records and reconcile unique studies and multiple reports.
4. Title/abstract screen against preregistered rules. Discuss ambiguous papers with independent human reviewer.
5. Full-text extraction with source/page references, evidence-rating and review-stream assignment.
6. Synthesize model equations, experiment designs, field-vs-simulation support and gap matrix; only then decide physics-only vs PINN based on data and independent test design.
7. Report actual selection counts and full search reproducibility in PRISMA 2020 + PRISMA-S supplements.

## Review acceptance criteria (no shortcuts)

**Scientific support hierarchy:** verified physically connected simultaneous transformer/EVSE field observation > separately observed original instrumented component experiments > physics-derived simulation with justified measured inputs > unvalidated synthetic models > reviews/theory/source leads. All classes can teach methods; they cannot support the same empirical claims.

**Disqualifying shortcut:** Do not claim two datasets sampled at different sites establish a causal heat cascade, use the battery temperature as rectifier temperature, or infer P→T_e restriction from nominal charger power rating.

**No invented PRISMA:** The number of hits visible in search engine output is not the raw count retrieved from an academic database; entries in the seed matrix are not the final included-paper count.

**No uncontrolled model choice:** Physics-only first; any PINN comparison must be justified by a measurable advantage, known physical parameters/boundary conditions and independent holdout, not enthusiasm for an algorithm.

## Review-status sentence suitable for supervisor

“A systematic-review protocol has been drafted and versioned, search strategies and extraction rules have been specified, and 27 previously identified or newly discovered references have been tagged as a provisional seed corpus. The comprehensive bibliographic exports, independent screening, engineering critical appraisal, PRISMA flow and formal synthesis remain outstanding.”

## Key references
- [PRISMA 2020](https://www.prisma-statement.org/prisma-2020)
- [PRISMA-S](https://doi.org/10.1186/s13643-020-01542-z)
- [Krama et al. Qatar extreme-heat charger](https://doi.org/10.1016/j.ecmx.2026.101960)
- [SINTEF measured transformer data](https://doi.org/10.5281/zenodo.17223516)
- [Zakaria et al. measured-EV-input dynamic thermal rating modelling](https://doi.org/10.1049/gtd2.13025)
