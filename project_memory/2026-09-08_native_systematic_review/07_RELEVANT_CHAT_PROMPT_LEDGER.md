# Relevant prompt / decision ledger for this chat

This is a scientific/operational reconstruction, not a verbatim dump of low-information confirmations.

| Stage | User prompt / action | Scientific or protocol consequence |
|---|---|---|
| IEEE completion | Asked how to select/export all records and corrected the T1 no-lower-bound issue. | IEEE T1/T2 were completed and IEEE phase reached 9/9 frozen before Compendex work. |
| Compendex access | Entered Engineering Village Expert Search through ASU Library. | Compendex selected as next external database. |
| Parser failure | Reported repeated Engineering Village “system error” for the long query and asked for deeper syntax research. | Established that the failure was execution/parser-related rather than a scientific-query defect. |
| Syntax isolation | Demonstrated atomic searches such as `({power grid*} WN KY) AND (2000-2026 WN YR)` work while grouped OR formulations failed. | Adopted atomic Search-History decomposition. |
| Power block | Ran six P atoms and OR-combined them. | Final `P=504,675`. |
| Transportation block | Ran T1–T12 one by one. | First union was audited and found wrong: duplicate `transport system*`, missing `charging station*`. |
| Transportation correction | Rebuilt union from exact Search History IDs. | Final `T=375,268`; invalid 372,049 unions retained only as diagnostics. |
| Purpose check | Asked “what is our purpose to do it”. | Reaffirmed target: not export atomic sets; construct final `Q0=P∩T∩Z∩R`. |
| Interdependency block | Ran Z atoms one by one. | Final `Z=275,522`. |
| Resilience block | Ran R atoms and later built a separate R union after final-combine parser error. | Final `R=1,056,435`. |
| Final combine error | Direct `#8 AND #24 AND #49 AND (R atoms...)` failed. | Staged R union resolved parser limitation. |
| Final Q0 | Ran block intersection. | Final native Compendex Q0 result `N=245`. |
| Export | Asked where/how to export; selected My PC, CSV, Detailed record, all 245. | Untouched native export created. |
| Raw upload | Uploaded `2026-09-08_COMPENDEX_Q0_v2_2_RAW_N0245.csv`. | Full audit, deterministic dev/validation samples, anchors, overlap, and freeze completed. |
| Current request | Asked for all rigorous information needed by a new chat and full GitHub processing. | This handoff capsule, ledger, code, manifest, and GitHub research branch/PR are created. |

## Key user-provided syntax observations preserved

Working atomic pattern:
```text
({power grid*} WN KY) AND (2000-2026 WN YR)
```

Working title-field example:
```text
("Rapid transit" WN TI OR "light rail" WN TI)
```

Observed failure pattern:
large grouped OR expressions with repeated `WN KY`/year nesting could trigger a generic Engineering Village system error.

Operational resolution:
use atomic native searches + Search History unions + final block intersection.
