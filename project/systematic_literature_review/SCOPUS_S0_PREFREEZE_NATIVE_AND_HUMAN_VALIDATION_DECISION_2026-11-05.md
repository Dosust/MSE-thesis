# S0 v0.1 — pre-freeze decision, native Scopus verification and human specificity audit

**Decision date:** 2026-11-05  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Review unit:** Scopus bibliographic EIDs and separately adjudicated distinct works/studies  
**Current status:** **CANDIDATE PRIMARY SEARCH — NOT FROZEN**

## Formal decision

**Retain the existing exact S0 v0.1 query as a candidate principal coupled-system search.** Preserve A0–F1 (12 thematic blocks) as complementary retrieval sources. Do not add, discard, or merge studies automatically on the basis of S0 search membership, title tokens, or repeated DOI. Continue the already recorded 19 cross-EID/shared-DOI groups as manually unresolved.

**Reasoning:** 5 of 5 previously selected core pilot candidates appear in the S0 export, but only 2 of 6 supporting pilot records do. A narrow P AND T AND H query deliberately excludes some single-component physics/method/standards papers. Additionally, generic keywords and broad Scopus indexing produce possible off-target records. S0 should therefore be assessed for both recall and precision before signoff, with the thematic blocks retained to preserve supplementary coverage.

## What has actually been established

- Uploaded original Scopus CSV contains **5,662 records** and **45 columns**; no repeated EID within this file; 2000–2026 years. SHA-256: `4e2bfdb7d38759f3e7b6d12e1b2ea1244e7263c1901a713db1d1048640bdde50`, size **51,166,050 bytes**.
- Against 12 earlier A0–F1 exports: 1,996 shared EIDs, 3,666 new EIDs, 27,528 EIDs in the new union. The shared-DOI/different-EID audit comprises 19 DOI groups; identities still require human evidence review.
- All five previously labeled core pilot papers are present, but the pilot is **not an independent, held-out or human-calibrated sensitivity sample**.
- S0 contains **299 records designated `Conference review`**, including some whole-proceedings summaries; **6 records designated `Retracted`**. **4,604 titles lack explicit thermal-vocabulary tokens**, while **253 titles mention broad power, transport and thermal terms together**. These last two are **title-only descriptive diagnostics, not relevant/irrelevant counts**: abstracts and keywords may provide the actual search match.
- Examples needing human scrutiny include Scopus EID `2-s2.0-105030827483` (whole ICETA conference proceedings); `2-s2.0-85141219940` (whole SeFeT proceedings); `2-s2.0-78650308053` (solar PV irradiance study); `2-s2.0-105009268153` (solar cell dye simulation); `2-s2.0-84933037185` (power network voltage regulation with EV and line thermal limits); `2-s2.0-105009302889` (transformer-area flexible support with EV loads and overload). Their scientific status remains undecided until review; some can still supply genuine context/constraints.

## Gate 1 — Verify exact live Scopus execution: **PARTIAL — NATIVE COUNT CONFIRMED; QUERY/FILTERS/DATE PENDING**

From the user's institutional Scopus session obtain **native screenshot or Search History/export-details evidence** that shows: platform/database Scopus; complete exact executed query; search date/time/timezone; all active year/language/document/subject filters; total **Scopus-reported hit count**; and any automatic query rewriting or errors. Compare the executed text against the archived exact S0 v0.1 file, not a paraphrase. Check whether the **native reported hit count equals 5,662 CSV rows**. The native platform count **5,662 documents found** is now confirmed by a user-uploaded Scopus screenshot and matches the 5,662 exported CSV rows. The screenshot shows only the beginning of the search string; exact full query, filter settings and native execution timestamp remain unverified. A repeat search may have a different count due to indexing changes; log the date and cause rather than silently forcing agreement.

If the native count differs, investigate export pagination/caps, post-search selection limits, added filters, modified search syntax, and indexing updates. Preserve both versions and a discrepancy memo; never rewrite the original S0 file.

**Required sign-off fields:** search executor; actual execution timestamp; native query capture identifier; verbatim-query-match Y/N; native hit count; export row count; difference; explanation; reviewer approval.

## Gate 2 — Independent human eligibility calibration: **PENDING**

Complete the original **25-paper pilot** with two independent human assessors using blinded decisions and reasons (`INCLUDE_CORE`, `INCLUDE_SUPPORTING`, `INCLUDE_CONTEXT`, `EXCLUDE` with E01–E07 reason, `UNCLEAR`). Resolve disagreements, document adjudication and check full texts when abstracts are ambiguous. Do not present assistant preliminary suggestions to assessors as final truth. Approval of this evidence boundary precedes high-volume screening.

## Gate 3 — S0 specificity / possible false-positive audit: **PREPARED; HUMAN REVIEW PENDING**

- A reproducible **100-record simple random sample** from all 5,662 S0 rows (RNG seed 20261105; distinct EIDs; not restricted by paper type) permits a *reviewer-confirmed* approximate precision calculation after adjudication. No numerical precision estimate is justified yet.
- An **additional 30 deliberately non-random challenge records** assess the vulnerability of the broad query: 10 entire-proceedings/conference reviews, 10 PV/solar titles without EV in the title, and 10 grid-only titles lacking explicit EV or thermal wording. The extra 30 must **NOT** be pooled into an unbiased precision denominator.
- Neither sample contains preset include/exclude outcomes. Every reviewer field is intentionally blank; read title/abstract and relevant full text independently. Human reviewers should distinguish CORE vs SUPPORTING vs CONTEXT rather than calling all non-core papers false positives.
- Separately examine all `Retracted` labels for research integrity status before evidence extraction; preserve retrieved records and report retractions transparently.

## Gate 4 — Query acceptance / refinement: **PENDING**

After Gate 1–3 and independent seed-paper testing, decide `ACCEPT_S0_v0.1`, `REVISE_S0_v0.2`, or `REJECT_AS_PRIMARY`; explain the evidence and supervisor approval. If revised, run a new native Scopus search, preserve old/new queries and both original exports, log seed recall and human-judged specificity. Versioned changes only; no silent post-hoc edits.

## Gate 5 — Wider database searches and synthesis: **PENDING**

Translate and run documented comparable queries in Web of Science, IEEE Xplore and Engineering Village where accessible; citation chaining and standards search separately. Reconcile bibliographic work/study identity, complete reviewer-screened selection and PRISMA-ScR/PRISMA-S records. Screening and data extraction must distinguish SO1 physical interface evidence, SO2 validated equations, and SO3 time/service consequences; a paper may hold multiple justified roles but count once as a verified publication.

## Records and authoritative files

- S0 query v0.1: `S0_SCOPUS_ADVANCED_PROVISIONAL_QUERY.txt` (Google Drive folder `S0_integrated_search_protocol_2026-11-05_v0_1`).
- S0 original archived: https://drive.google.com/file/d/1ySzWE5kvxTcPgAXRsUtzylUuUYB0npaJ/view
- Older eligibility protocol: `S0_ELIGIBILITY_SEARCH_PROTOCOL_V0_1.md`.
- Current sampling worksheet: `S0_PREFREEZE_130_RECORD_BLIND_HUMAN_SCREENING_SAMPLE.csv`.
- Source indicators: `S0_PREFREEZE_SAMPLING_AND_NOISE_INDICATORS.json`.
- Specific examples: `S0_EIGHT_CONCRETE_SEARCH_NOISE_EXAMPLES.csv`.

**Do not claim:** complete native Scopus query/history/settings verified; S0 formally validated; off-target count measured; pilot complete; supervisor approved; or records fully screened. **The 5,662 native results count is now independently evidenced.** These gates are open.


## 2026-11-05 evidence update — platform count verified

- User screenshot shows Scopus **“5,662 documents found”**, matching the original S0 export row count **5,662** (difference 0).
- Beginning of visible TITLE-ABS-KEY text matches the archived S0 v0.1 query prefix. The rest of the query and filters are not visible, and execution date/time is not shown.
- Original image SHA-256: `3d89ed2dc7ef9813ab5f5eed2d8c650b19afe59b5a6aca2a75a41d3f727dfe7e` (400,314 bytes).
- [Native Scopus screenshot preserved in Drive](https://drive.google.com/file/d/1o6wEGlV8Dgz9dgIpEwFzdo-qJ-D6YyNf/view).
- [Auditable screenshot verification memo and remaining gates](https://drive.google.com/file/d/13ewxVld1DI3j86qCOlPvR1mNRuRo9hsL/view).
- **Decision unchanged:** S0 v0.1 remains candidate primary search; not frozen until complete native query/filters/date verification, reviewer calibration and precision checks.
