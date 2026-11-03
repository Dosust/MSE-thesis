# WP1 implementation and evidence-readiness register — Phelan plan v2.0
**Created:** 2026-11-03. **Authority:** `PHELAN_RESEARCH_EXECUTION_PLAN_V02_2026-11-03.md`; `SYSTEMATIC_REVIEW_EXECUTION_PROTOCOL_V02_2026-11-03.md`.  
**Branch:** `user-data-qualification-2026-11-03`, not `main`.  
**Status:** DRAFT IMPLEMENTATION. **Not method-locked, not supervisor-approved, not an executed systematic search.**

## Source-governance rules
- Six objectives O1–O6 of plan v2.0 and frozen thermal SO1–SO3 remain active. v2.0's **eight** WP1–WP8 and 44 tasks are authoritative; T42–T44 downstream.
- Primary review type: **systematic scoping/evidence map** using JBI and PRISMA-ScR; focused critical mathematical/thermal-model synthesis as separate layer. PRISMA-S for full search reporting.
- Literature questions **SLR-Q1 to SLR-Q6** and original F1–F7 claim-level evidence classification are unchanged from method v0.2.
- No finding from an abstract can certify measured temperature or connected-system causality. Distinguish measured field, controlled laboratory, field-driven model, numerical-only and reviews.
- Do not call the research plan "approved," searches "completed," or a source "systematically included" without actual screening records. Do not promote prior 17 seeds or old 200/325 paper corpora into formal search totals.

## WP1 — four tasks and truthful gates
| Task | Existing basis | Executed now | Remaining acceptance blocker | Status |
|---|---|---|---|---|
| T01 review objectives | Method v0.2 SLR-Q1–Q6 and frozen SO1–SO3 | Cross-referenced exactly; no change to scope | Explicit dated review-scope lock and any supervisor comments | **PARTIAL** |
| T02 eligibility/reviewer | Method v0.2 §C, E–H, F1–F7 and review reporting | Retained prior eligibility, confounding rules; drafted screening/reviewer declaration below | Human independent methodological check (where feasible) and accepted version lock | **PARTIAL** |
| T03 archive + traceability | Method v0.2 §E/G; templates already exist | Created folder convention, source provenance/ID scheme and privacy rules below | Lock after T02, verify actual first export/sha and functioning citation-manager manifest | **PARTIAL — advanced from not started** |
| T04 database-native search | Method v0.2 six separate A–F families | Wrote **24 unexecuted** platform-specific query drafts or builder recipes in `WP1_SEARCH_TRANSLATIONS_DRAFT_V1.csv`; official field-code documentation checked | Live platform syntax check, peer/PRESS quality review, seed-recall pilot and dated query freeze | **PARTIAL** |

### T03 evidence archive convention
Use research folder:
`project/data_qualification/2026-11-03/systematic_review_v02/` for **source-permitted metadata, audit logs and derived results**, with local or authorized private storage of restricted original files (do not upload paywalled PDFs or sensitive field logs to GitHub).

```text
00_protocol/       protocol snapshot, amendments, reviewer declarations
01_search_logs/    literal platform query, dated source total, filters, status
02_raw_exports/    authorized original RIS/CSV/BibTeX (if redistribution allowed)
03_dedup/          DOI/title-year merges and original-to-canonical record IDs
04_screen/         title abstract/full-text decisions, reasons, reviewer
05_fulltext_index/ source URLs, page coordinates, access status (not illicit PDFs)
06_extraction/     claim-level equation, sensor/asset/clock, physical gate
07_quality/        six-domain appraisal and evidence stratum F1–F7
08_synthesis/      what others did, counterexample matrix, bounded gap
09_method_choice/  measured data readiness, conventional physics baseline, PINN gate
10_reporting/      flow, bibliography, supervisor brief, version summary
```

**Identifiers:** Record ID `SR2026-{platform}-{block}-{export_index}`; Study ID `ST-{normalized_DOI_or_hash}`; evidence-unit ID `EV-{study_id}-{claim_index}`; dataset ID retain canonical FD-xxx/Dxx. All source URLs and DOI preserved, original metadata not silently corrected.

**File naming:** `2026-11-03_<database>_<block>_<queryVersion>_<UTCrunstamp>.<ris|bib|csv>`; raw export SHA-256, byte count, database field selection, source query and platform recorded separately. Include access level and permitted reuse. This is a schema, not a claim of existing exports.

**Dedup policy:** normalized DOI as primary; otherwise exact canonical title/year with authors, manual adjudication of ambiguous records; retain many-to-one crosswalk, distinguish technical report from updated final journal paper and preprint versions.

**Human roles:** single thesis researcher presently documented. Second reviewer/adviser/information specialist not yet confirmed. No dual human screening, PRESS signoff, formal protocol preregistration or supervisor approval claimed.

**Versioning:** Current v0.2 is DRAFT. Once wording, sources, query translations and reviewer mode have been checked, save dated explicit locked snapshot on branch, sha256 of its bytes and amendment/change ledger; never edit frozen source history silently.

### T04 platform semantics verified (syntax alone, not searches)
- Scopus `TITLE-ABS-KEY()` and `PUBYEAR AFT/BEF`: https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search
- WoS Core Collection `TS=()` topic, `PY` and interface filters: https://webofscience.zendesk.com/hc/en-us/articles/26916347018257-Web-of-Science-Core-Collection-Advanced-Search-Field-Tags
- Engineering Village Compendex Expert `WN KY` subject/title/abstract and separate database selection: https://www.elsevier.support/engineering-village/answer/what-are-the-search-fields-in-the-compendex-database ; https://www.elsevier.support/engineering-village/answer/how-can-i-improve-my-expert-search
- IEEE Xplore Advanced Search: **All Metadata** field-option known; direct query syntax NOT validated in a signed-in interface. Builder instructions recorded instead of inventing ready-to-run expression: https://xplorestaging.ieee.org/Xplorehelp/personalization-settings/search-preferences
- Bibliographic years planned 2000–2026-11-03 as in v0.2. For any results with 2026 final/early-access discrepancies, preserve both publication date fields and actual retrieval time. No universal language restriction.
- Important: “verified field code” does **not** equal verified retrieval, hits, database coverage, successful export, complete query recall, or search-method approval.

### Before G1 can pass
[ ] T01 full scope/question lock recorded with reviewers/date  
[ ] T02 eligibility and F1–F7 finalized, reviewer limitation documented  
[ ] T03 archive/citation manager design tested and versioned  
[ ] T04 each search block copied into live platform to verify syntax; exact query and filters preserved; PRESS/peer audit or explicit limitation recorded  
[ ] Protocol frozen with SHA/date and amendments; supervisor comments/approval recorded only if actually obtained

### Then WP2 (NOT DONE)
T05–T08 authentic platform searches: execute A–F with exact timestamp, result count, complete export and hash. T09 citation chaining and seed-recall evaluation. Only *then* run title/abstract screening and count PRISMA flow. Do not populate the untouched source search log or report invented counts now.

**Summary:** WP1 artifacts **advanced** but gate G1 remains OPEN; WP2 G2 remains NOT STARTED. Original research plan v2.0 and frozen thesis authorities remain unchanged.
