# Historical literature reconciliation — executed methods and results v1.0

**Date:** 2026-11-03. **Status:** EXECUTED BIBLIOGRAPHIC RECONCILIATION / FORMAL REVIEW NOT COMPLETE.  
**Active thesis:** Frozen thermal-only SO1–SO3, not historical flood/curvature/Power–Water scope.

## Source restoration

The **actual materialized original** \`Q0_Evidence_Corpus_Audited_v2.xlsx\` was read sheet-by-sheet with a spreadsheet import tool. Its sheets contain **404 MASTER_Q0 rows**, **687 PROVENANCE_687 rows**, 404 preliminary SCREENING rows and 404 EXTRACTION rows (some empty). All **404 confirmatory title/abstract statuses and 404 final full-text statuses are PENDING** in the original master. Pilot predecisions on Q0: **74 Include, 85 Exclude, 1 Unclear, 244 blank**. These are historical pilot judgments, **not formal systematic review selections**. The original database row composition reported in the workbook is Scopus **253**, IEEE **189**, Compendex **245** (sum 687); the original per-platform native search strings/filters and completeness are not independently re-executed here.

**Correction of prior history:** An earlier “209-record Q0 workbook” statement arose from **partial indexed extraction/visibility**, not an independently confirmed 209-study corpus. The actual complete master contains **404**. Do not report 209 as a second verified collection.

### Reconciled historical collections

| Collection | Input entries | Disposition |
|---|---:|---|
| Q0 recovered original deduplicated master | 404 | Authoritative historical unique-record base, metadata and origin IDs; full source exports licensed, not publicly redistributed |
| October scored metadata screen | 200 | Historical score / selection decisions preserved; **176** of the scored records use Q0 master IDs; other entries may derive from augmentation |
| October priority list | 26 | Citation candidates prioritized for full-text review, **not 26 completed full-text screens** |
| October provisional thermal 26 | 26 | Different composition; provisional citations, not independently confirmed all source equations |
| November pilot candidates | 25 | 17 earlier seeds plus 8 November additions, not formally eligible studies |
| Earlier CPTS priority seed | 26 | Secondary initial source collection; not a formal included-study pool |
| Thermal school P14–P200 candidates | 77 DOI-linked slots | Historical DOI candidate index; **110 further slots were empty**, not publications |

Total **784 source-record memberships** from these inputs. Exact normalized DOI first, then strict title/year when DOI absent (no fuzzy auto-merge): **533 unique *provisional bibliographic identity records*** in [master register](./MASTER_SYSTEMATIC_LITERATURE_REGISTER_V01.csv); **784 lineage links** in [crosswalk](./HISTORICAL_BIBLIOGRAPHY_PROVENANCE_CROSSWALK_V01.csv). **498** of the 533 have a DOI field; **35** have no verified DOI field. These counts are the result of metadata merging and should not be called independently validated studies or a completed PRISMA sample.

**Automated metadata-only relevance triage** in the master (not formal eligibility screening): **48 CORE_CANDIDATE; 57 SUPPORTING_CANDIDATE; 27 HISTORICAL_BACKGROUND; 220 UNRESOLVED_RELEVANCE; 181 UNRESOLVED_OR_OUT_OF_SCOPE**. Every tag is a first-pass rule-based indicator requiring manual abstract and full-text eligibility confirmation. The distinction matters especially for engineering papers that couple power and transport but **do not** measure thermal cross-system effects.

## Audit and source preservation

- Q0 metadata-only 404 exported as [Q0 canonical public metadata](./Q0_CANONICAL_PUBLIC_METADATA_404_V01.csv). Complete licensed Q0 original remains in the user's research files; separate local original extracted CSVs contain abstracts and must **not** be uploaded to a public repo without confirming export rights.
- Saved source references, all historical IDs, original database labels and old screening statuses. The crosswalk's “match_basis” reflects a deterministic merge rule, **not publication-level manual adjudication**.
- Exact DOI key match resolves straightforward duplicate citations; absence of detected DOI conflicts does **not** prove title/family/version duplicates absent. Candidate conference/journal extensions and translation variants remain for manual checks.
- Historical code's priority/rigor score is a **reading order**, not an objective source quality score, exclusion reason, PRISMA decision or validation assessment.
- Connected-grid and thermal physics literature contains distinct research units: study, report, method, dataset descriptor and experiment. Reconcile at study versus report level before final PRISMA.
- The original Scopus, IEEE and Compendex file names/row references exist in Q0, but original platform-native query strings, dates and export checksums are not yet fully independently verified from the source runs. Thus a complete PRISMA-ScR diagram is **BLOCKED**.

## Phase 1 gate decision

**G1 HISTORICAL RECONCILIATION = PARTIAL, with a substantial verified output.** All six accessible GitHub lineage collections were merged with the original 404-row Q0 base; remaining manual duplicate/family classification, publisher DOI metadata checks, and provenance of original database export metadata are OPEN.

**Next:** (1) adjudicate uncertain source families, (2) formally lock review eligibility + six search strings, (3) execute authorized database-native searches and screen systematically, (4) reuse complete primary equations rather than re-reading already audited claims.
