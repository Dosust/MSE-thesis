# S0 integrated Scopus search — uploaded-export integrity and 13-search union audit

**Audit date:** 2026-11-05  
**Original file:** `S0.csv` uploaded by user; archived unchanged as `SCOPUS_S0_2026-11-05_original.csv`  
**Source SHA-256:** `4e2bfdb7d38759f3e7b6d12e1b2ea1244e7263c1901a713db1d1048640bdde50`  
**Bytes:** 51,166,050  
**Original archived URL:** https://drive.google.com/file/d/1ySzWE5kvxTcPgAXRsUtzylUuUYB0npaJ/view

## 1. Export integrity

| Check | Observed |
|---|---:|
| Scopus rows | 5,662 |
| Scopus metadata fields | 45 |
| Year range | 2000–2026 |
| Invalid/out-of-range years | 0 |
| Missing EID | 0 |
| Repeated EID inside S0 | 0 |
| Missing DOI | 539 |
| Missing abstract | 0 |
| Missing references | 350 |
| Unique DOI values | 5,118 |
| Different EIDs sharing one DOI inside S0 | 5 DOI groups |

**Caveat:** The CSV verifies export structure/content, not the verbatim executed query, native Scopus result count or completeness. Retain native Scopus search-history evidence and verify the reported hit count before freezing S0.

## 2. Union with existing twelve thematic searches (A0–F1)

| Measure | Count |
|---|---:|
| Original A0–F1 unique Scopus EIDs | 23,862 |
| S0 unique Scopus EIDs | 5,662 |
| Scopus EIDs common to S0 and A0–F1 | 1,996 |
| **New EIDs contributed by S0** | **3,666** |
| **13-search EID-level union** | **27,528** |
| A0–F1 EIDs not recovered by S0 | 21,866 |
| Distinct DOI values assigned to >1 EID within A0–F1 | 15 groups |
| Distinct DOI values assigned to >1 EID in 13-search union | **19 groups** (38 EID records) |

**New collision DOI values introduced in the 13-search union:**

1. `10.4271/2012-01-2226`
2. `10.4271/2012-01-1003`
3. `10.4271/2012-01-1774`
4. `10.1016/S0378-7753(02)00197-0`

**Decision unchanged:** preserve every search occurrence; treat EID as bibliographic record identity, not study identity; verify same-DOI/different-EID cases before canonical merging. One verified bibliographic work may have multiple scientifically justified SO1/SO2/SO3/supporting roles but must not be counted multiple times as an independent study.

## 3. Retrospective retrieval check: 25 previously identified pilot records

| Assistant's preliminary title/abstract category | Retrieved in submitted S0 export | Total |
|---|---:|---:|
| Core candidates | **5** | **5** |
| Supporting candidates | 2 | 6 |
| Uncertain-supporting | 2 | 9 |
| Provisional exclusions | 1 | 5 |

Coverage tested by normalized DOI exact match to the `S0.csv` file. The core pilot was selected from earlier Scopus searches, so this is a **retrospective convenience test**, not an unbiased, preregistered validation set or a measured estimate of sensitivity. There are no formal reviewer decisions or final inclusions.

## 4. Required next scientific gates

1. Retrieve the exact native Scopus S0 executed query, its search date, filters and original returned hit count; check that the CSV export is complete. **Not documented by this CSV.**
2. Check the five core known papers individually and add an independent representative reference-paper set. Ensure S0 does not falsely omit core mechanisms; improve query if needed, logging revisions.
3. Review new S0 records for false positives introduced by broad acronyms (`EV`, `EVs`), generic grid and temperature terms; any edits must be version-controlled and rerun/reevaluated.
4. Retain A0–F1 because they retrieve supplementary single-subsystem physics and service publications that S0 misses.
5. Manually resolve all 19 cross-EID DOI collision groups and other publication-identity conflicts; do not silently subtract 19 from EID union.
6. Complete 25-record independent **human** screening calibration; freeze eligibility rules and proceed through approved title/abstract and full-text review and other databases.
7. Keep PRISMA records, distinct works, independent studies and role assignments as separate reporting units.

## 5. Output files and audit provenance

- `S0_LIVE_EXPORT_INTEGRITY_AND_COVERAGE_AUDIT.json` — export metadata and raw pilot DOI coverage.
- `S0_PILOT25_NATIVE_EXPORT_COVERAGE.csv` — one row per pilot record (DOI exact matching).
- `S0_UPDATED_UNION_EID_INDEX_27528.csv` — 13-search EID-level provenance index, showing `S0` membership; not an eligibility register.
- `S0_UPDATED_UNION_DOI_COLLISIONS.csv` — 19 groups requiring manual identity verification, 38 EID rows.
- `S0_UPDATED_UNION_SUMMARY.json` — audit checks and collision map.

**Review status: S0 export successfully archived and audited, but S0 NOT formally validated/frozen.**
