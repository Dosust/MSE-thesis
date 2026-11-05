# V5-to-GitHub record reconciliation — content-level, 5 November 2026

**Scope and authority:** frozen SO1–SO3, extreme heat, thermal Power–Electrified Transportation. The original 533-row GitHub master is unchanged. Records are **not studies**; the V5 AI/rule-assisted screen is **not** a second human review or PRISMA eligibility result.

## Provenance and access controls
- Source V5: Library item `/My thesis/Unified_Thesis_Research_Master_V5_Reconciled_2026-11-04.xlsx`, Library file ID `libfile_3bee6aba6eb8819198499b97c52b9879`, version **2**, size **554533 bytes**, indexed text with 31 tab exports; source creation in Library 2026-11-05.
- **IMPORTANT LIMITATION**: original XLSX raw-byte materialization failed with “This Project file does not have an authorized raw-byte materialization path.” These checks use the **indexed text of the V5 Master Literature sheet**. The original XLSX binary SHA-256, formulas and formatting are **NOT authenticated or synchronized to GitHub**; the source remains in Library.
- GitHub baseline: `project/systematic_literature_review/MASTER_SYSTEMATIC_LITERATURE_REGISTER_V01.csv` at branch `user-data-qualification-2026-11-03`, independently fetched raw CSV (533 records), content/blob SHA `0f14e852fbec7ed9e189b6edb81de889c0838aa8`.
- Method: parse RFC-style double-quoted CSV, match stable LIT canonical ID, compare original recorded DOI and normalized titles/year/relevance. Preserve both original values and V5 provisional values; no forced overwrite.

## Audited results (records, not independent studies)

| Metric | Result |
|---|---:|
| V5 source records | 590 |
| Previously existing canonical ID matches | 533 / 533 |
| Additional IDs in V5 | 57 (LIT-0534–0590) |
| DOI/title/relevance differences among 533 | 0 / 0 / 0 |
| V5 populated DOI strings / unique normalized DOI strings | 555 / 555 |
| Missing DOI cells | 35 |
| Same-normalized-title groups within 590 | 16 (32 record rows; study-family identity **open**) |
| V5 year differences against GitHub | 74 |
| Old blank year → "TO VERIFY" | 73 |
| Recorded year → "TO VERIFY" regression | 1: LIT-0003 (GitHub 2024, V5 TO VERIFY) |
| Current V5 provisional TA | 98 ADVANCE, 126 BACKGROUND, 259 EXCLUDE PROVISIONAL, 107 UNCERTAIN |
| Current V5 formal eligibility | 404 PENDING, 186 NOT_STARTED — **not adjudicated** |

## Duplicate study-family candidates
The 16 title-identical groups have mismatched DOI identities or missing DOI. They include obvious journal/preprint relationships and conference versus later journal versions, alongside one same-title 2003 vs 2005 conference pair. **Do not delete or merge automatically:** compare authors, DOI resolution, underlying datasets, methods, venue and results first. The two conference/journal pairs LIT-0226/0285 and LIT-0228/0283 can correspond to related but materially different analyses; keep independent record provenance and assign linked-study family after full text.

## Remaining strict finish gates
1. Acquire the actual original V5 XLSX bytes from the Library download or direct user attachment for complete immutable SHA-256 and all 31 native-sheet audits. Indexed content cannot prove workbook/formula integrity.
2. Verify all 16 duplicate-title groups with primary metadata and classify record-level preprint/journal/conference version vs distinct study.
3. Reconcile year LIT-0003 and 73 unverified original year blanks against publisher DOI metadata. Do not treat "TO VERIFY" as a publication year.
4. Execute and export actual **database-native** Scopus, Web of Science, IEEE and Compendex A–F searches with platform permissions, date, exact query, all records and export checksums. Public web indexed searches are supplemental only.
5. Human screening of all 590 + newly exported candidate records, independent audit, full text of eligible candidates, excluded reason table and PRISMA flow, critical equations and evidence quality.
6. Preserve frozen scope and study/report distinction. No formal complete SLR or novelty claim from this reconciliation alone.

**Machine-readable companions**:
- `V5_GITHUB_RECORD_CROSSWALK_2026-11-05.csv`: one row per 590 source records with old/new fields, match status, year/duplicate flags.
- `V5_POTENTIAL_STUDY_FAMILY_DUPLICATES_2026-11-05.csv`: all 16 title groups.
- `V5_YEAR_FIELD_REVIEW_QUEUE_2026-11-05.csv`: all 74 year differences.

**Status:** content-level 533↔590 **COMPLETE**, binary XLSX provenance and independent study-level dedup **NOT COMPLETE**.
