# Q0 Cross-Database Master Evidence Corpus — v1

Status: **MERGE + CONSERVATIVE DEDUPLICATION COMPLETE; confirmatory screening pending**

## Input boundary
Frozen direct Power–Transportation resilience Q0 runs only:

- Scopus: N=253
- IEEE Xplore: N=189
- Compendex: N=245

Raw identified records:

`253 + 189 + 245 = 687`

## Conservative deduplication result

- raw database records: **687**
- canonical master records: **404**
- redundant database records consolidated: **283**
- reduction: **41.2%**
- multi-database master clusters: **218**
- single-database master clusters: **186**

Presence categories:

- Scopus only: 36
- IEEE only: 120
- Compendex only: 30
- Scopus + Compendex only: 149
- Scopus + IEEE only: 4
- IEEE + Compendex only: 1
- all three: 64

Linked overlaps after conservative missing-DOI reconciliation:

- Scopus ∩ IEEE: 68
- Scopus ∩ Compendex: 213
- IEEE ∩ Compendex: 65
- triple overlap: 64

The earlier exact-key-only union was 406. Conservative exact-title/year linkage, only where DOI evidence did not conflict, safely reconciled two additional missing-DOI database records and produced 404 master records.

## Deduplication rule

1. Exact normalized DOI equality -> auto-merge.
2. Exact normalized title + exact year -> auto-merge only when the group has no more than one distinct non-empty DOI.
3. Different non-empty DOIs -> **never auto-merge**.
4. Fuzzy-title similarity -> flag only for manual publication/version review.
5. Metadata conflicts are preserved instead of silently reconciled.

## Publication/version control

- **17** possible preprint / conference-journal / publication-version pairs were flagged.
- automatic merge = **NO**.
- **3** master records contain metadata conflicts requiring review.

## Prior pilot screening

Prior native-pilot screening was mapped to **160 unique master records** without decision conflicts:

- Include: 74
- Exclude: 85
- Unclear: 1

These are preserved as **pilot provenance only**. They are not silently promoted to final PRISMA eligibility because the pilot samples were originally used to validate search performance.

All **404** master records remain in the confirmatory title/abstract screening worklist.

## Mechanism extraction architecture

The full-text extraction template is prepared for:

`X, Z, I, O, h, e, tau, F, J, K, V, rho_V, u`

plus:

- P2T / T2P dependency
- hazard/disturbance
- propagation mechanism
- recovery mechanism
- organizational component
- mathematical model
- data/case study
- calibration
- validation
- uncertainty treatment
- main limitation/gap
- EML and quality dimensions

Formal mechanism fields must be filled from source-supported evidence; they are intentionally not inferred from abstracts where unsupported.

## Raw-source integrity

- Scopus raw SHA-256: `cee449fe72fabd5f265dc042d6b2d85e907de1de1694b21cded3d28f04368079`
- IEEE raw SHA-256: `37c66cac8015bd44455a9cbcb1ae930ff1893bc5870322cb5a27719dfbea710c`
- Compendex raw SHA-256: `2c15662b02f27a085dc39f50245d33c4f2166c63839050feb8fc2eb22f7816a8`

## Controlled local artifacts

The detailed master CSV/workbook and provenance files contain database-provided abstracts/metadata, so they are retained in controlled thesis storage rather than committed to Git by default. Their cryptographic fingerprints are in `ARTIFACT_MANIFEST.csv`.

## Scientific state

`SEARCH -> MERGE -> CONSERVATIVE DEDUP -> CONFIRMATORY TITLE/ABSTRACT SCREEN -> FULL TEXT -> MECHANISM EXTRACTION`

Compendex Q3 remains a separate search-development task and is paused at atomic-search completion pending stable native access.
