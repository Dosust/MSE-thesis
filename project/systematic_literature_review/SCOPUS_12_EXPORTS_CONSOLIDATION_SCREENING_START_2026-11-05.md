# Scopus A0–F1 12-export consolidation and initial screening — 2026-11-05

**Scope:** engineering/mathematical-physics thesis on extreme-heat thermal power–electrified transportation interdependencies, frozen SO1–SO3.
**Status:** computational data audit and non-destructive initial lexical prioritization; **not** human title/abstract screening, study inclusion, full-text assessment, model validation or final PRISMA count.

## Results verified from 12 original user-supplied Scopus CSV files

| Metric | Verified value |
|---|---:|
| Original Scopus files (A0, A1, B0, B1, C0, C1, D0, D1, E0, E1, F0, F1) | 12 |
| Raw retrieved CSV record occurrences | 29,736 |
| Repeated occurrences of the exact Scopus EID across exports | 5,874 |
| Unique Scopus EIDs | 23,862 |
| EIDs found in more than one export | 4,902 |
| Different EIDs sharing a DOI | 15 DOI groups: manual review OPEN |
| Different EIDs with identical normalized title and year | 104 groups: manual review OPEN |
| Same EID with conflicting DOI, normalized title or year across the 12 exports | 0 / 0 / 0 |
| Formally human-screened eligible studies | **NOT DETERMINED** (human decisions = 0) |
| Independent 25-record pilot | 25 candidates prepared; human decisions pending |

### Raw export sizes and row counts

| Search | Scopus CSV rows |
|---|---:|
| A0 transformer thermal physics | 6,179 |
| A1 transformer + EV charging | 244 |
| B0 EVSE thermals | 734 |
| B1 EVSE derating under heat | 13 |
| C0 connected power–charging infrastructure | 8,890 |
| C1 field/site monitoring | 2,407 |
| D0 coupled dynamics and resilience | 8,265 |
| D1 thermal/service consequences | 958 |
| E0 physics-based modeling | 656 |
| E1 PINN / hybrid learning | 64 |
| F0 standards and validation | 1,295 |
| F1 transformer thermal experimental validation | 31 |
| **Sum, before deduplication** | **29,736** |

**Raw original exports remain intact** in [Google Drive/systematic review data](https://drive.google.com/drive/folders/12qHPDstoacvQJu1M8amBjufvf002NnUs).

**Derived consolidated outputs** are saved in [Drive/SCOPUS_consolidation_2026-11-05](https://drive.google.com/drive/folders/1lNautf6ECIi-VpQBzcCXmYo0szP5DnZG). These include 12-file SHA-256 source manifest, per-occurrence provenance crosswalk (29,736), 23,862-record EID screening register, 12×12 overlap matrix, 15 DOI collision groups, 104 title/year groups, 25-record calibration sample, research audit report, Excel control workbook and a 60.6 MB full ZIP including the 165.5 MB canonical CSV. For direct Drive access, the canonical CSV has been losslessly split into four data shards of 6,000, 6,000, 6,000 and 5,862 EIDs; an index of shard SHA-256 hashes is present.

### Deterministic lexical *priority only*, not human eligibility

| Priority signal | Unique EIDs |
|---|---:|
| P1 power+EV+thermal+empirical terminology | 506 |
| P2 power+EV+thermal model terminology | 961 |
| P3 coupled service without thermal signal | 2,611 |
| P4 thermal single-component or method terminology | 7,308 |
| P5 lower lexical signal / requires human inspection | 12,476 |

These are search-priority labels derived mechanically from **title and abstract wording only**. No item is excluded or definitively included. Real full-text and reviewer evidence may disagree with these labels.

### Original comparator checks (DOI exact matching)
- Gong 2015: `SCU-011871` (A0/A1/C1/F0).
- Pan 2025: `SCU-000767` (A0/A1/C1).
- Krama 2026: `SCU-005690` (B0/B1).
- Bragone 2022: `SCU-017152` (A0/E0/E1/F0).
- Acker 2025/2026 DOI `10.1007/s41104-025-00157-7`: no exact match in this Scopus export union. Database indexing and query coverage require verification; no global absence claim.
- Fletcher–Khan report remains a grey-literature source outside this Scopus index snapshot.

### Review gates not complete
1. Obtain Scopus-native saved-search history showing **verbatim executed queries, execution date, filters and hit count** for all exports; project chat contains intended queries, but these are not native server logs.
2. Resolve the 15 same-DOI/different-EID and 104 same-title/year/different-EID groups without losing any source provenance.
3. Obtain an independent real reviewer and conduct 25-record calibration. The screening register's `HUMAN_NOT_STARTED` values and reviewer blanks must not be backfilled as if human decisions were made.
4. Apply documented eligibility to all Scopus candidates; separate title/abstract exclusion, unavailable full text, full-text reasons and study-family identity.
5. Complete the other database/grey-literature searches and final PRISMA-ScR, not just Scopus.

**Method rule:** Scopus EID is a bibliographic identity, not evidence that different EIDs represent independent studies. The consolidated record count must not be treated as scientifically included studies or a finished PRISMA denominator until eligibility and source provenance are complete.
