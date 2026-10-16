# Scopus Search 5 — Experimental Evidence and Validation

**16 October 2026 | Scopus Advanced Search | Draft PR #84**

**Recorded query:** [SCOPUS_SEARCH_05_RECORDED_QUERY.txt](SCOPUS_SEARCH_05_RECORDED_QUERY.txt). The query **and year limits** are visibly verified against the researcher's 2026-10-16 **Scopus Exports Dashboard screenshot**; the live Search History/results page and total hit count are still NOT verified. The visible limits are `PUBYEAR > 1969 AND PUBYEAR < 2028` (1970–2027 inclusive). This is narrower than a database-inception search and must be documented as an active filter.

**Export audited:** 20,000 records, 35 columns, 18,746 DOIs, no duplicate EIDs. SHA-256: `940f46c2e4fe44750866e06b5460107ca57614cc2881788f942948ab3e34ae36`.

**Critical caveat:** Scopus CSV export limit is 20,000 items. The file hits this limit exactly; total search hits and coverage remain UNCONFIRMED. Check displayed results and export any missing portion through appropriate separate documented queries or approved options. Count 20,000 as *exported*, not as a confirmed complete search.

**Purpose:** We used Scopus to find experimental, calibration, validation and physics-informed thermal research relevant to power transformers and electrified transportation. After formal screening, these publications will help establish physical thermal mechanisms (SO1), governing differential equations and measurable state-time dynamics (SO2), and temperature-dependent service limitations, timing and recovery (SO3). We will identify which results are measured, calibrated, simulation-only or independently validated, test existing prior art, and decide whether physics-only or physics-informed models are justified by the data.

**Cross-search comparison:** Search 5 overlaps the earlier four uploaded exports in 6,727 EIDs; it adds 13,273 new EIDs. Five file sets contain 35,006 distinct EIDs before relevance screening. The query is broad, and results may contain unrelated AI Transformer or battery-only research. No novelty or model selection is established.

**Original CSV:** `export_8f61939a-0941-4160-ac56-a41d496093ae_2026-10-16T161631.093642874.csv` (76,536,950 bytes). Full export NOT committed: Scopus bulk retention/sharing rights for GitHub are unconfirmed. Preserve the original in approved research storage. Only this metadata, research description and query are committed.

**Follow-up screenshot audit, 2026-10-16:** The Scopus Exports Dashboard displayed **two Search 5 export jobs**, each labeled **20,000 documents** and showing the **same query plus `PUBYEAR > 1969 AND PUBYEAR < 2028`**. One job was *Export in Progress* and another offered *Download CSV*. This is evidence of **two export jobs**, NOT that the result set has 40,000 hits or that the jobs cover distinct EIDs. Neither job card reports the **total search result count**. Treat the total, percentage exported, and de-duplication of these two jobs as UNKNOWN until independently checked; avoid merging the jobs as separate batches based on the screenshot alone.

**Next:** Open the full Scopus Search 5 results/Search History page and provide the overall document-hit count. Confirm whether the existing 20,000-row CSV covers that total; if not, export genuinely disjoint documented slices. Record year filter in systematic-review search logs. Then deduplicate and screen and inspect original studies.


## Scopus results-page verification — 2026-10-16

**EVIDENCE:** User-provided screenshot from actual Search 5 results page visibly states **23,054 documents found** for the Search 5 expression. The visible query includes `PUBYEAR > 1969`; the previously provided Exports Dashboard confirms `PUBYEAR < 2028` as well. Thus report **23,054 Scopus hits** under the documented Search 5 year filters, not 20,000 total.

The existing original user-uploaded CSV has **20,000 EIDs**; **3,054 records were not contained in that export**. Two 20,000-record export jobs with the same query are not necessarily disjoint and cannot be summed. Exact set difference remains to be checked once complementary exports are obtained.

**Required completion procedure:** Re-execute the same Search 5 conceptual expression while partitioning **only by nonoverlapping publication years**, e.g. `PUBYEAR > 1969 AND PUBYEAR < 2020` versus `PUBYEAR > 2019 AND PUBYEAR < 2028`. For each slice record its actual hit count and ensure it is below the per-export 20,000 cap; otherwise split the slice again. Export both complete ranges, retain original export and partition query metadata, and compare the combined unique Scopus EIDs with the search-results-page total (acknowledging possible index changes between query times). No claim that the two slices have already been run. The 23,054 count is a **database hit count, not screened included literature**.


## Latest status correction — 2026-10-16 (overrides earlier incomplete-export warning)

A new **8,366-record 1970–2019** supplement was uploaded and audited. Its EID overlap with the original Search 5 20,000-record file is **5,312**; combined distinct EIDs equal **23,054**, matching the Scopus results-page screenshot exactly. **Search 5 EID coverage is now reconciled.** See [deduplication/coverage report](SCOPUS_SEARCH_05_FINAL_EID_RECONCILIATION_2026_10_16.md).

The 5,932-record additional upload is byte-identical to Search 2 and does not increase the bibliography. Total distinct EIDs across all five search streams now **37,376**. Earlier statements in this log requiring more Search 5 records are **superseded**. The exact 1970–2019 submitted year-partition query still needs independent screenshot/history verification. Full-text screening and model validation remain unexecuted.
