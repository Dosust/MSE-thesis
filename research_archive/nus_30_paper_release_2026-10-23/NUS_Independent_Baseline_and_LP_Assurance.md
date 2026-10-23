# NUS 30-paper constrained correction: independent findings

## What was corrected

Only three notation cells in the approved NUS-52 record: `visual and general!C95`, `Verified!C15`, and `Verified!E15`. The time-dependent reliability index now uses `β(t)` consistently, and the adopted reliability constraint is displayed with the correct mathematical beta symbol. The separately corrected `Verified!I15` was already aligned and was NOT edited in this run.

## Evidence and preservation

- All **30 paper records** exist and are nonempty, including the six new paper records in both research sheets.
- Exactly **75 embedded figures** and **75 comments**, all authored **Dossiya Dakou**, are present. All review timestamps are distinct; these are review times, **not historic creation times**.
- The 12 papers to which figures were added have **at least two embedded figures anchored within each original paper block**.
- Both sheet structures, all row/column settings, all existing drawings, comment text, timestamps, figure media files and relationships are preserved.
- **No new rows, columns, or worksheets**; no paper research outcomes changed in the current pass.
- Independently compared to the authoritative 24-paper 2026-10-22 workbook: the four known content differences are the three notation-only cells edited here and the previously corrected `Verified!I15`. All other first-24 paper research cell values match.
- Running the algorithm against its corrected output has objective **zero** and proposes **no further edits** (idempotence).

## Scope of the LP algorithm

The 0/1 mixed-integer linear program (HiGHS through `scipy.optimize.milp`) selects only vetted notation changes and minimizes edits under hard author, row/column, paper-ID, content, comment and figure-preservation gates. It does **not** reconstruct source mathematics, validate published experimental data, or treat simulated examples as experiments. It deliberately does not rewrite the 15 historical audit issues; their prior dispositions remain in the included historical issue file.

## Remaining scientific qualifications

- NUS-153 remains on **source-integrity/provenance hold**; its computational examples are not independently reproducible from the provided data.
- NUS-2 contains published embodied-carbon/embodied-energy prose inconsistencies, which should not be silently changed.
- NUS-120, NUS-124, NUS-9 and NUS-127 retain the documented method and sustainability-scope qualifications.
- Independent numerical reproduction of each reported result has **not** been established by this LP audit.

**Decision:** the workbook passes the tested structural, notation and metadata checks. A blanket scientific 'zero errors' claim is not justified.
