# S0 pre-freeze random-100 and targeted-30 execution audit
**Execution:** 2026-11-06 | **Status:** source/sample integrity PASS; human search precision NOT ESTIMABLE
**Source:** archived user original `SCOPUS_S0_2026-11-05_original.csv` (Google Drive: https://drive.google.com/file/d/1ySzWE5kvxTcPgAXRsUtzylUuUYB0npaJ/view)
**Source checksum:** SHA-256 `4e2bfdb7d38759f3e7b6d12e1b2ea1244e7263c1901a713db1d1048640bdde50`, verified byte-for-byte from fetched original file.
**Original size:** 51,166,050 bytes; 5,662 unique, nonblank Scopus EIDs and 45 metadata fields.
**Methods script:** `s0_scopus_relevance_audit.py` executed locally against complete source, existing 130 review worksheet, existing 25 pilot.
**130 worksheet:** https://drive.google.com/file/d/1NzkyNmOM6C0_tRoBzG09Hto8LurEbXcq/view
**25 pilot:** https://drive.google.com/file/d/1Eh2raiXDZel6H11i22qgHvKlM1djqOzN/view

## Tests performed
1. `verify --s0 ... --sample ...` PASS: 5,662 original EIDs, exact original SHA, 100 random + 30 targeted, all 130 EIDs and titles present and identical to original S0, zero sample duplicates.
2. Independently replayed `random.Random(20261105).sample(range(5662),100)` against original source row order: **100/100 random EIDs identical in order**, confirming deterministic original sampling algorithm and seed.
3. `analyze --sample ... --pilot ... --report S0_precision_results.json` executed successfully with scientific block: 0/100 first-reviewer decisions, 0/100 second-reviewer decisions, 0/100 final adjudications; 0/25 paired human calibration reviews. **No numerical precision, Wilson 95% interval or Cohen's kappa can be reported.**
4. Random-100 descriptive metadata, **not relevance:** 55 Article; 35 Conference paper; 4 Conference review; 4 Book chapter; 2 Review; 7 missing DOI; publication years 2007–2026.
5. Targeted 30: 10 assigned conference review, 10 solar/PV-without-EV-title, 10 grid-only-without-EV/thermal-title. **8 assignments fail the current script's literal keyword rule:** 5 solar/PV candidates (e.g. unhandled `photovoltaics`, broad `charging` exclusion), **3 grid-only candidates have an explicit EV term in title**, so this label is truly contradicted. All 10 conference-review cases satisfy current rule. Do not report the 30 as 100%-compliant with the scripted targeting logic. Preserve the 130 original; use a versioned recode or amended challenge subset, never alter the 100 unbiased sample.
6. The original `verify` function tests sample membership, not historic random-selection mechanism; the separately executed replay provides stronger confirmation. The existing 25-human-review calibration remains a separate design.

## Statistical status and next gates
`precision_status=BLOCKED_UNTIL_ALL_100_HUMAN_ADJUDICATED`. Intended primary positive classifications: `INCLUDE_CORE` + `INCLUDE_SUPPORTING`, and `INCLUDE_CONTEXT` reported separately. Non-random 30 and pilot 25 NEVER pooled into denominator. After two independent reviewers, adjudication and a declared eligibility rule, compute k/100 and 95% Wilson interval; this is **sample-based record search precision, not coverage/recall**.
Work remains to establish native search history, complete reviewer calibration, conduct 100 screened cases, resolve 30 targeted category mismatches, and carry out known-study/other-database retrieval audits.

**Integrity:** No manual relevance was fabricated; publisher abstracts, raw original CSV and reviewer worksheets remain private in Drive and were not committed to GitHub. Neither formal JBI screening nor PRISMA completion is claimed. Canonical title and SO1–SO3 remain unchanged.
