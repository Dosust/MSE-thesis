# Authenticated database search status — access tests, not executed searches

**Date:** 2026-10-15  
**Research review phase:** `AUTHENTICATION / INTERFACE ACCESS CHECK` only.  
**Never back-fill PRISMA counts from page redirects, public-web index hits, or seed-paper counts.**

| Bibliographic database | Access attempt | Actual observation | Database search run? | Query-specific results / export |
| --- | --- | --- | --- | --- |
| Scopus | https://www.scopus.com/search/form.uri?display=advanced | **403 Forbidden** | **NO** | **Unknown / none** |
| Web of Science Core Collection | https://www.webofscience.com/wos/woscc/advanced-search | **403 Forbidden** | **NO** | **Unknown / none** |
| IEEE Xplore | https://ieeexplore.ieee.org/search/advanced | **418 automated-access error** | **NO** | **Unknown / none** |
| Engineering Village / Compendex | https://www.engineeringvillage.com/search/quick.url | OAuth redirect, minimal form, **no results** | **NO** | **Unknown / none** |

Four direct interface-access requests do **NOT** fulfill the Phase 2 28-query protocol or substantiate database completeness. Elicit semantic academic searches in the pilot were blocked by account-level API restriction; a Scite integration was suggested as an optional complementary source, **not a replacement for formal Scopus/WoS/IEEE/Compendex searches**.

## Formal search prerequisite and provenance rule

An institutional library account and actual accessible database interface are needed to:
1. Execute the exact versioned query candidate in `phase2_search_readiness_2026_10_15/CANDIDATE_DB_QUERIES_NOT_RUN.csv`.
2. Save actual date/time, database coverage, query filters, untruncated hit count and provider-native RIS/BibTeX/CSV export.
3. Test sentinel-DOI recall against the **broad unmodified search**, not a targeted DOI lookup.
4. Archive the exports with unique names and cryptographic hashes; preserve both source-file date and provider.
5. Apply DOI/metadata deduplication, dual/manual screening and PRISMA reporting.

Until all provider-specific searches are complete, maintain an explicit database coverage limitation; the existing pilot remains public-web discovery. No externally supplied library credentials are to be requested inside GitHub files or copied into this repository.

## Current state
- Queries prepared: 28.
- Authenticated Scopus queries executed: **0**.
- Authenticated Web of Science queries executed: **0**.
- Authenticated IEEE Xplore queries executed: **0**.
- Authenticated Compendex queries executed: **0**.
- Actual result counts: **not available / unknown**, NOT numerical zero study matches.
- Formal review completeness: **BLOCKED** pending authenticated access.

**Request for user:** Provide provider-native export files (RIS/BibTeX/CSV) obtained through university library access, or run the live database queries in an authorized browser workspace and export those records. No fabricated substitute will be generated.
