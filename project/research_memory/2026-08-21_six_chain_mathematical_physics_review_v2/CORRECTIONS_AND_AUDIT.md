# CORRECTIONS AND AUDIT LEDGER

## E1 — Mergeability was overreported
A prior response stated PR #5 was mergeable. GitHub connector calls later returned inconsistent `mergeable=true` and `mergeable=false` values. **Correction:** mergeability is transient live metadata and must never be frozen as a durable research-memory fact.

## E2 — Branch synchronization text became stale
The first PR body said the feature branch was zero commits behind. A later live compare showed it had diverged and was behind `main`. **Correction:** V2 was created from the then-current `main`; future chats must query live ahead/behind status rather than repeat stored prose.

## E3 — Actual figures were not in the first PR
The initial PR had 17 changed files but no `.drawio`, `.svg`, or `.png` filename. **Correction:** V2 includes actual editable Draw.io and vector SVG assets.

## E4 — Current conversation memory was incomplete
The first subthread archive did not contain the later correction request. **Correction:** U6 is preserved in this folder, while broader exact/preserved chat segments are linked in `SOURCE_MAP.md`.

## E5 — Literature completeness was overstated
The foundational anchor list was useful but several broad/recent papers explicitly discussed later were not represented. **Correction:** V2 records Ji et al. (2024), Wang et al. (2024), Akiyama (2025), Tong et al. (2025), Kumar & Hashem Mehany (2026), and Anvari & Timme (2026) as important closest-existing reviews/bridges.

## E6 — Equation provenance was too coarse
A citation beside a formula can be mistaken for direct source-level equation provenance. **Correction:** `FORMULA_PROVENANCE_V2.csv` distinguishes:
- `DIRECT_OR_EXPLICITLY_EXTRACTED`
- `CANONICAL_FORMALISM`
- `THESIS_SYNTHESIS_NOTATION`

## E7 — Scope conflict was silently at risk of being overwritten
Project history contains an earlier executable Power–Water–Transport demonstrator and later conceptual expansion including Solid Waste. **Correction:** preserve this as an open project-state difference; do not guess which is currently frozen.

## E8 — “Full chains” must remain review-testable
“Full” means the broadest ontology currently synthesized, not proof that no other layer exists. A systematic/scoping review is allowed to add, merge, split, or rename layers when evidence supports it.

## E9 — Duplicate memory can reduce reproducibility
Creating many competing summaries causes drift. **Correction:** V2 uses explicit upstream paths in `SOURCE_MAP.md` and acts as a correction/canonical-index layer rather than pretending older repository memory does not exist.
