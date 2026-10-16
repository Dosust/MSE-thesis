# Scopus Search 1 — Power–Electrified Transportation Thermal Interdependencies

**Search date:** 2026-10-16  
**Source:** Scopus, Documents, Advanced Search, Title/Abstract/Keywords (`TITLE-ABS-KEY`)  
**Search identifier:** `SCOPUS-S01-PT-THERMAL-20261016`  
**Search query:** [SCOPUS_SEARCH_01_EXACT_QUERY.txt](SCOPUS_SEARCH_01_EXACT_QUERY.txt) (verbatim user-executed search; no query modification).  
**Original user-observed Scopus results:** **3,009** documents.  
**Original user-supplied CSV:** `export_948fd5b4-d17c-4aef-a7c4-9f9d839aefbb_2026-10-16T155123.210615672.csv`  
**CSV availability:** User-uploaded conversation attachment; **NOT STORED IN THIS GITHUB BRANCH**.  
**Status:** `SEARCH_EXECUTED_CSV_RECEIVED_LOCALLY_METADATA_AUDITED`; study screening NOT RUN; zero claims about completed systematic review.

## Why this Scopus query was used

We searched titles, abstracts and keywords for the **intersection of Electrified Transportation equipment/EV charging**, **Power infrastructure (transformer, grid/network)**, and **thermal/temperature/derating/aging effects**. The aim is to locate previously modeled or measured physical heat-conditioned Power↔Tₑ relationships and to test whether the thesis's proposed physical and time-dependent mechanisms are already studied.

## How the results will be used for the frozen thesis goals

This record set is an **initial search corpus**, not a final inclusion set. With the other independently executed Scopus search results we will:

1. **Deduplicate and screen** all records against the prespecified eligibility criteria (without equating search hits to relevant studies).
2. **Read eligible primary sources**, extracting thermal/heat-transfer laws, governing ODE/PDE/state-time equations, physical P/Tₑ interface and direction, initial/boundary conditions, assumptions and operational limits.
3. **Distinguish evidence levels**: illustrative/simulated, sourced/parameter-bounded, measured/calibrated, and predictions independently validated against actual physical states. Measured transformer lid temperature is not automatically measured winding hot-spot; an EVSE internal transformer is Tₑ not P.
4. **Evaluate electricity and mobility service consequences**, critical transition times, propagation delays and their measured vs modeled status, mapping findings to SO1, SO2 and SO3.
5. **Test prior-art/novelty claims** using confirmed counterexamples (notably published thermal transformer → charging constraint work). Determine what remains unresolved without assuming the gap exists.
6. **Audit the fit of public/permissioned experimental data**, then justify a pure physics versus physics-informed modeling comparison *only if* suitable data are verified.

**Scientific boundary:** A shared extreme-heat exposure, electrical charging link, or simulation alone is NOT field evidence of temperature-conditioned directional P→Tₑ or Tₑ→P propagation. The thesis remains founded on physical laws and mathematical analysis regardless of the later learning method.

## Audited local CSV export summary

| Audit | Verified locally |
| --- | --- |
| CSV parsed row count | **3,009** |
| Scopus EID duplicate count | **0** |
| Records with nonempty DOI | **2,642** |
| File size | **10,869,578 bytes** |
| SHA-256 | `f9c2d13779c96bf1c8a5965fa10804fc3d5949284b682ef09f581a4cd33b90fd` |
| Columns | 33 |
| Core columns | Title, Authors, Year, Abstract, DOI, Author Keywords, Index Keywords, EID, Source |
| Explicit references column | **Absent** |

**Data custody restriction:** Scopus bulk exports may include licensed abstracts, author contact information and other restricted metadata. This private GitHub repo has not been used to store the original 10.9-MB CSV, because its exact redistribution/cloud-storage permissions have not been confirmed. Keep the original file in authorized individual/institutional storage; upload to repository only if Scopus/institutional terms specifically permit access/storage in this setup. See [Elsevier Scopus terms](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions/elsevier-scopus-terms-and-conditions). Do not commit complete bulk abstracts or correspondence addresses into publicly accessible history.

## What is not established

Neither experimental data for the same P↔Tₑ installation nor formal study eligibility, bibliographic dataset deduplication against Searches 2–5, full-text critical comparison, or systematic novelty judgment has been completed.

**Next operational step:** Execute Scopus Search 2 (Power-System Thermal Physics) exactly as registered, export records, record query/results/date and attach the export in authorized storage. Follow with Search 3 (EVSE thermal performance), Search 4 (mathematical models), Search 5 (measurements/validation), then deduplicate all five.
