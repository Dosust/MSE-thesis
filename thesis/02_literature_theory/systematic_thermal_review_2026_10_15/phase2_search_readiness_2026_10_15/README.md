# Phase 2 Search Readiness — Database Translation and Recall Test Plan

**Date:** 2026-10-15  
**Status:** SEARCH STRATEGY DRAFT — NOT EXECUTED — NOT VALIDATED IN LIVE DATABASES.  
**GitHub governance:** PR #84 branch only, all canonical thesis files unchanged.

## Purpose
Translate the Phase 1 pilot's six thematic lanes into reproducible search candidates for **Scopus, Web of Science, IEEE Xplore and Engineering Village Compendex** without claiming authenticated database access. Add a second direct-coupling query `L1B` because early transformer thermal-aging work from electric-vehicle charging may not include an extreme-heat expression. Hence seven query variants in each of four databases = **28 candidate search strings**. The original six conceptual lanes remain; `L1A/L1B` are explicit substreams.

## Current source boundary
- Phase 1 public-web pilot: executed and archived separately.
- Elicit semantic search: blocked by account plan API limits. Do not retry repeatedly without changed access.
- Four subscription-index searches: **NOT RUN**. No database parses, actual result counts, exports or item-level systematic selection completed.
- Query vocabulary: based on documented prior literature leads; no retroactive declaration of sensitivity/recall performance.

## Search engine syntax provenance
| Engine | Proposed interface | Field syntax | Primary authority |
| --- | --- | --- | --- |
| Scopus | Advanced document search | `TITLE-ABS-KEY((A OR B) AND C)` | [Scopus official](https://service.elsevier.com/app/answers/detail/a_id/11365/supporthub/scopus/~/how-can-i-best-use-the-advanced-search%3F/) |
| Web of Science Core Collection | Advanced search | `TS=((A OR B) AND C)` | [Clarivate official](https://webofscience.help.clarivate.com/en-us/Content/search-rules.htm) |
| IEEE Xplore | Basic Search (Boolean) | `(A OR B) AND C`, uppercase Boolean | [IEEE Xplore official](https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/search-engine) |
| Compendex | Engineering Village Expert Search | `((A OR B) WN KY) AND (CPX WN DB)` | [Compendex field codes](https://www.elsevier.support/engineering-village/answer/what-are-the-search-fields-in-the-compendex-database), [DB code](https://www.elsevier.support/engineering-village/answer/what-are-the-engineering-village-database-search-codes) |

**Careful:** This table is syntax-supported *in general*. Actual complex query parsing and matching are **not yet verified**. IEEE Xplore Advanced Search's field interface differs from Basic/Command Search. For IEEE, enter candidates via Basic Search or translate them through its GUI. Web of Science and Engineering Village interface editions/limits may differ. Capture screen/error message and corrected exact executed query, not silently overwrite the planned string.

## Files
- [CANDIDATE_DB_QUERIES_NOT_RUN.csv](CANDIDATE_DB_QUERIES_NOT_RUN.csv) — 28 candidate field-syntax strings: 7 variants × 4 databases.
- [KNOWN_ITEM_RECALL_TEST_NOT_RUN.csv](KNOWN_ITEM_RECALL_TEST_NOT_RUN.csv) — 10 provisional check entries (nine unique DOIs; duplicates intentionally flagged).
- [OFFICIAL_SYNTAX_AUTHORITIES.csv](OFFICIAL_SYNTAX_AUTHORITIES.csv) — provider guidance and source URLs.
- [EXECUTION_CHECKLIST.md](EXECUTION_CHECKLIST.md) — precise test, export, and freeze gates.

## Query design decisions
1. Do NOT require a PINN/grey-box/ML keyword in L1/L2/L3/L4/L6. Method-choice comparisons arise downstream.
2. `L1A` asks specifically about extreme heat and direct P/T interface; `L1B` independently catches EV-load-induced transformer thermal work without heatwave tokens.
3. `L2` charger thermal mechanisms includes operating limits/cooling but does NOT require a grid-transformer term.
4. `L3` transformer physical/field models includes experimental data and generic dynamic modeling, not only PINNs.
5. `L4` vehicle battery thermal experiments separates lab packs from actual vehicle field studies in extraction.
6. `L5` methods returns physics-only baselines and grey-box/physics-informed comparisons, but a complementary **method-free physics baseline search** may be necessary if recall fails.
7. `L6` treats charging duration/power as a charging-service proxy, **not** real trip completion.
8. All four catalogs have different indexing and interface coverage: differences in hits are not automatically errors.

## Publication and language boundaries
No arbitrary lower-year cutoff and no English-only filter by default. Searches cover **database inception through actual search execution date**. Index-type, field, year or document-type restrictions must be explicitly logged. Separate original studies and reviews during screening; reviews may seed reference mining but are not counted as original experiments. Add database completion date to exported filename and revisioned logs.

## Known-item test rule
The `KNOWN_ITEM_RECALL_TEST_NOT_RUN.csv` is **not** a recall score. For each broad executed search, independently evaluate whether sentinel DOI is present in that result export **without querying that DOI during recall testing**. If a sentinel is omitted, distinguish (i) not indexed; (ii) excluded by concept design; (iii) missing term synonym; (iv) faulty Boolean/field syntax; (v) time/coverage; and (vi) export truncation. Avoid 'fixing' query to force unrelated background items into thermal lanes.

## Live execution sequence
1. Confirm institutional access/license and chosen database instance. Capture date (UTC/local timezone).
2. Run one query at a time, first `L1B` and `L2` in Scopus for known-item diagnostics.
3. Record exact submitted query, syntax errors, corrected query, active filters, and per-query **actual** hit count.
4. Export full bibliographic result list with DOI, title, abstract, authors, source and citation fields in RIS/BibTeX/CSV.
5. Calculate actual DOI recall **within each exported broad search**. Do not count exact-DOI lookups as evidence of sensitivity.
6. Revise and rerun only under an explicit dated protocol amendment and keep both strings/results logs.
7. Repeat across the remaining lanes and databases; keep database duplicate records until PRISMA deduplication.
8. Run deduplication, title-abstract and full text selection; keep original PDF pages and raw-data gates independent.
9. No 'final method' decision before evidence-qualified data and matched physics/grey-box/PINN comparisons.

**Do not report Phase 2 as complete on the basis of saving these 28 translations.**
