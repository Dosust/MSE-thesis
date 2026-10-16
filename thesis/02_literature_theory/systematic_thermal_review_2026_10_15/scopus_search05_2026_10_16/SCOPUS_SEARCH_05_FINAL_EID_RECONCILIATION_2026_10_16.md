# Scopus Search 5 — Completed EID Coverage from 1970–2019 Supplement

**Date:** 16 October 2026  
**Scientific status:** Scopus Search 5 *bibliographic EID set reconciliation complete against displayed 23,054 hits*. **Paper selection, source review and scientific novelty assessments NOT YET COMPLETE.**

## Source and query identity
- Search 5 base query on experiments, measured/calibrated/validated thermal models and physics-informed studies in power/EV topics: [parent query](SCOPUS_SEARCH_05_RECORDED_QUERY.txt), confirmed from Scopus Exports Dashboard with `PUBYEAR > 1969 AND PUBYEAR < 2028`.
- **Supplemental file:** `export_0a135ac4-9b38-4e4a-ae65-69ffbdcabd90_2026-10-16T164754.064628789.csv`. It contains only years **1970–2019** and 8,366 rows. Matching proposed search text: [SCOPUS_SEARCH_05_1970_2019_QUERY_TO_CONFIRM.txt](SCOPUS_SEARCH_05_1970_2019_QUERY_TO_CONFIRM.txt). **The export does not contain query history; exact submitted Search 5 year-partition text still needs confirmation in Scopus Search History.**
- **Original baseline S5 file:** `export_8f61939a-0941-4160-ac56-a41d496093ae_2026-10-16T161631.093642874.csv` — 20,000 rows (Scopus export cap).
- **Scopus result count:** 23,054 documents, independently shown in user screenshot of Search 5 results page, with 1970–2027 date filters documented by prior Exports Dashboard.
- **Second uploaded file:** `export_3afecaa7-7afa-4c92-9fbd-6db8c0fd08bf_2026-10-16T155530.041806193(1).csv` — **byte-for-byte identical SHA-256** to previously registered Scopus **Search 2** export; it is NOT a new partition of Search 5, and should not be counted again.

## EID reconciliation from actual uploaded CSVs
| Test | Verified value |
|---|---:|
| Search 5 original 20,000-row export (EIDs) | 20,000 |
| New Search 5 1970–2019 export (EIDs) | 8,366 |
| EID intersection of the above | 5,312 |
| Unique EIDs in their union (`20000+8366−5312`) | **23,054** |
| Scopus screenshot's reported Search 5 result count | **23,054** |
| Search 5 EID set matches reported hit count | **YES** |
| Missing EIDs relative to reported total | **0 by count**, at the screenshot/export dates |
| New EIDs beyond original 20,000 | 3,054 |
| New EIDs beyond all previous Search 1–5 exported EIDs | 2,370 |
| Updated unique EIDs across Search 1–5 | **37,376** |

The matching total strongly supports complete Search 5 EID retrieval under the original search conditions, subject to normal bibliographic index changes. It does not prove that the initial 20k export and 1970–2019 slice each use precisely identical query filters without inspection of recorded Scopus Search History. Do not sum the two 20,000 export jobs as distinct files.

## Source quality audit of the 1970–2019 CSV

- Actual file size **25,356,172 bytes**; SHA-256 `5169e270bf4752d96a216e82644c5f31f454770a0c561ed5cf29383175824d39`.
- 8,366 rows, 35 columns, 8,366 unique nonempty Scopus EIDs, 0 duplicated EIDs.
- 6,392 DOIs, 8,366 abstracts, 8,365 nonempty titles; one title is blank — flag on screening.
- All recorded publication years are **1970–2019** (not 2020–2027).
- The second uploaded file is **identical to the original Search 2**, 5,932 rows, 18,745,858 bytes, SHA-256 `78b091fc9bcab397e2c5b4819f3237709041630f0357aaacfdce49ea4f5ae5ef`, so it is excluded as a redundant receipt.
- Search 5 is broad: papers that use "transformer" for AI must still be screened out; actual measured thermal state, source location and independently validated service outcomes must be verified in original studies.

## Short thesis-use statement

**We used Scopus Advanced Search to identify thermal experiments, measurements, calibration, model validation and physics-informed methods relevant to electrical power and electrified transportation. The complete 23,054-record Search 5 set will be deduplicated with the four earlier searches and screened to identify governing physics, mathematical state-time equations, thermal interface mechanisms, observed operating constraints, and independently validated electricity/mobility service effects. We will use the resulting evidence to test prior art and select a justified physics-based or physics-informed model without assuming novelty, causality or PINN superiority.**

## Custody and research gates

Scopus bulk bibliographic content has not been committed to this private GitHub repository while retention/sharing permissions for this third-party destination are unverified. This branch stores original file basenames, byte sizes, SHA-256s, query records, counts, evidence purposes and exclusion decisions; original user-provided CSVs must be held in an institutionally authorized environment. Permission, if granted, should be documented before any raw content upload.

**Next scientific work:** Verify the slice's exact Search History string, run systematic deduplication by EID/DOI and title/abstract eligibility screening across the 37,376 distinct search-hit set, read all priority eligible original articles, and extract physical equations, measured states, assumptions and validation evidence. **37,376 are raw candidate records, not 37,376 eligible papers.**
