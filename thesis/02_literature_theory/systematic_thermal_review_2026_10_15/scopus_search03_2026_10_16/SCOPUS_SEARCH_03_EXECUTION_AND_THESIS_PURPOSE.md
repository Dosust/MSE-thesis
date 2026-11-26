# Scopus Search 3 — Extreme heat and electrified transportation (2026-10-16)

**Status:** Export verified; **EXACT EXECUTED QUERY NOT YET RECONFIRMED IN SCOPUS SEARCH HISTORY**; screening not yet performed.  
**Original CSV:** `export_11a30dfb-e1a1-4e89-a69d-4e5e85e92400_2026-10-16T160243.361739678.csv` (uploaded to the conversation; **NOT COMMITTED to GitHub**).  
**Database:** Scopus — Advanced Search — Title/Abstract/Keywords.  
**Recorded query:** [SCOPUS_SEARCH_03_RECORDED_QUERY.txt](SCOPUS_SEARCH_03_RECORDED_QUERY.txt) — copied from the project's previously given Search 3 instructions. The CSV does not include the executed query or Scopus Search History; before registering the exact query as frozen execution evidence, confirm its characters/filters against the live Scopus search history.

## Purpose and use in our physics/mathematics-first thesis

We used Scopus to retrieve publications about **extreme/ambient heat, heat transfer and thermal management in EVs and EV charging equipment**, identifying source-side Tₑ heat mechanisms: converter/cabinet/cable/battery thermal states, power derating and charging capability changes. This is the *Tₑ-side component evidence stream*, not an independently proven P↔Tₑ field coupling search.

After deduplication and screening, the selected studies will support:

- **SO1:** Identify physically meaningful temperatures/heat flows, temperature-conditioned operating constraints and plausible **Tₑ→P** mechanisms, without mistaking shared ambient heat for coupling.
- **SO2:** Extract governing conservation/heat-balance ODEs/PDEs, constitutive losses/heat rejection, state-time evolution, boundary conditions, parameter-identification and modeling uncertainty. Physics and mathematics govern even when a learning method is evaluated.
- **SO3:** Examine thermal thresholds, derating-onset/recovery times, AC-to-DC power, charging consequences and **independently required** electricity/mobility-service metrics, separating predictions/proxies from measured service fulfillment.
- **Novelty/data gate:** Compare existing physics-based, grey-box and physics-informed research with **actual measured thermal states, independent validation** and prior P-side findings. Only then propose a warranted model choice and gap.

## Observed CSV audit — exact original file

- **9,595 records**, **35 columns**, **9,008 nonempty DOIs**, **0 duplicate Scopus EIDs**, **9,595 nonempty titles and abstracts**.
- File length **35,932,669 bytes**; SHA-256 `b1f3746a38f1db15c49424c1aaaa20573601fa5bfd17799d63e8fb89137768b6`.
- Search 1 EID overlap: **473**; Search 2 EID overlap: **75**; overlap across all three: **65**. Combined distinct EIDs for Searches 1–3: **17,908** (before eligibility screening).
- Subject breadth warning from **title-only heuristic, NOT a screening result**: **4,890** titles mention battery/batteries; **1,496** mention charg*; just **62** mention transformer. Battery-only thermal-system papers may not belong in the main coupled-infrastructure evidence corpus; screen scientifically.
- `Document Type=Retracted`: 11 records; **flag separately** before inclusion, check retraction provenance. Reviews/secondary sources should not be counted as primary experiments.
- **References column absent** from this export. Plan reference chasing through native article records or a permitted bibliography export.
- **Actual displayed Scopus results count:** Confirm `9,595` in Scopus UI; it is the validated file record count, not a screenshot-confirmed displayed hit total.

## Reproducibility and custody

Exact query, export basename, file checksum and aggregate statistics are in [SCOPUS_SEARCH_03_EXPORT_MANIFEST.csv](SCOPUS_SEARCH_03_EXPORT_MANIFEST.csv). Original bibliographic records contain many publisher-owned abstracts, affiliation and correspondence data. Under [Elsevier Scopus terms](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions/elsevier-scopus-terms-and-conditions), large-scale storage/redistribution is restricted and explicit authorization for a GitHub repository is not established. Thus **no bulk original CSV is stored in this private GitHub repository**; the attached original remains the user-owned/source file, to be retained only in a licensed/authorized research environment.

**Scientific status:** source query completed by user, export quality verified; screening and mathematical source extraction pending; no coupled data/validation or novel mathematical theorem claimed.

**Next:** Confirm Search 3 query/results in Scopus History. Run Search 4 — mathematical and physics-based thermal models, export and register similarly. When all searches are available, deduplicate, prioritize actual P↔Tₑ papers and read governing equations in original full text.
