# CPX-Q3 invalid Tau-union diagnostic — 2026-09-08

Status: **INVALID / DO NOT USE**

Observed result: `1,926,738` records.

Reason: Engineering Village enforces a rolling 50-search history. After `Z_Q3` was created, the session-local `#IDs` shifted. Reusing the pre-shift identifiers therefore no longer pointed to the intended 16 temporal atoms. The displayed expanded query begins with `coupl* NEAR/5 network*` instead of `timescale*`, proving that the wrong set was OR-combined.

Consequences:
- this result is **not** the valid `Tau` union;
- do not use it in any Q3 intersection;
- do not freeze or export it;
- retain only as provenance of the search-history-renumbering hazard.

Screenshot evidence:
- file: `4e3f7138-e82c-451f-8f87-b4e7b3b53bf9.png`
- bytes: `582761`
- SHA-256: `72e0d95c26e8fc02d4ae5a30a071efd932c2dd5f9beb3495d8d2e308fbea47c3`

Corrective action: rebuild `Tau` from the exact full temporal Boolean expression rather than session-local `#IDs`, then verify the displayed expanded query begins with `timescale*` / `time scale*` and contains all 16 frozen temporal terms exactly once.
