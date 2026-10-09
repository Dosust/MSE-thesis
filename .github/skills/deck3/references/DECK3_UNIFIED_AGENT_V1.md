# Deck3 Unified Agent — Intent Routing Contract V1
Effective 2026-10-09. Status: implemented prompt orchestration specification; individual production capabilities remain evidence-gated.

## Purpose
One short call, `Deck3 <request>`, routes automatically to the existing Deck3 skill ecosystem, choosing the minimum sufficient output. This is an **orchestrator**, NOT a new scientific authority, an autonomous background agent, or evidence that all generation backends work. In ambiguous cases infer from supplied materials and the current 13-slide baseline; ask only when a missing input makes action unsafe or infeasible. Do not silently invent artifacts or change frozen scientific scope.

## Mandatory preload, in order
1. `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md` and applicable citation/objective authorities when working on thesis science.
2. `.github/skills/deck3/SKILL.md`, `references/WORKFLOW.md`, `references/DECK3_GLOBAL_UPDATE_CONTRACT.md`, `references/DECK3_GLOBAL_UPDATE_CONTRACT_V1.md`, and `references/DECK3_DEPENDENCY_REGISTRY.json`.
3. The palette from `references/DECK3_SRGB_PALETTE.json` at runtime, and `references/DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md`.
4. For scientific visuals: `references/DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md`, AI-image/no-explanatory-panel rules when appropriate.
5. For math: `references/LATEX_TO_POWERPOINT_MATH_V1.md` and the real `main.tex` plus included sources if present.
6. For any form: V2 all-forms learning and corrected Research Expert learning references. Load other targeted skills only when relevant. If a required authority is unavailable, flag BLOCKED/OPEN instead of fabricating.

## Short-prompt intent routing
Match explicit objects and verbs first, not arbitrary keyword order. Resolve scope to the narrowest target specified, preserving all unstated frozen constraints. Accept legacy `Deck3 text/1`, `figures/2`, `assemble/3`, `all`, `QA`.

| Sample call | Route | Expected output |
|---|---|---|
| `Deck3` | Inspect available context; default to a concise current-state/next-admissible-action response. Never regenerate entire deck merely from the name. | status and next safe action |
| `Deck3 slide 9` | One-slide route. Inspect approved slide 9 source, then plan/design/build only what context supports. | approved-scope slide 9 deliverable or explicit blocker |
| `Deck3 improve slide 5` | Targeted review + revision; verify independent directional claims and frozen text. | revised slide or specific correction plan |
| `Deck3 text` | Stage 1: editable content and notes | text/PPTX with citations, as requested |
| `Deck3 figure slide 4` | Stage 2: medium-selection before tool, heat as shared external forcing | figure/source + trace + QA |
| `Deck3 diagram` | Native precise diagram when editable relationships matter; equipment imagery only if justified | editable diagram, no invented physical arrows |
| `Deck3 math slide 10` | Inspect LaTeX sources, convert supported math to genuine OMML, fallback to sourced vector | equation inventory, PPTX result, XML + render QA |
| `Deck3 animate slide 9` | Presenter reveal plan/native effects if supported; otherwise progressive slides | target IDs, click sequence, playback truth |
| `Deck3 assemble` | Stage 3; inspect Stage 1 source and Stage 2 approvals | editable assembled PPTX or fail-closed report |
| `Deck3 all` | End-to-end stages 1→2→3 with check gates | approved/provisional deliverables plus manifest |
| `Deck3 audit` / `Deck3 QA` | Independent scientific, source, XML, palette, readability, geometry and playback tests | per-gate PASS/FAIL/OPEN/NOT_RUN |
| `Deck3 compare A B` | Read actual versions and use canonical multi-version comparison | evidence-specific rubric and corrections |
| `Deck3 update` | Full dependency-review contract, modify impacted active consumers and tests | change ledger + PR when user authorizes modifications |
| `Deck3 sources` | inspect real literature, thesis authorities and LaTeX provenance | source/inference/uncertainty separated |

## Planning algorithm
1. Parse intent, output format, target slides/files, constraints, and whether task is analysis, editing, generation, or update.
2. Discover exact authoritative source files; never guess a path from a filename or claim uninspected materials were read.
3. Identify frozen elements (approved 13-slide Chapter 1 text, complete GO/SO1–SO3, scope, citations, notes), and any newer explicitly authorized revision.
4. Build a purpose-specific media plan for EACH affected slide: equipment scene vs editable workflow/matrix/roadmap vs native equations/plots vs text-only. The figure occupancy 70–80% applies only to eligible figure slides and must measure meaningful area.
5. Select the smallest toolchain that preserves native editing: text/shapes/tables/connectors, actual OMML, source SVG or reviewed physical image only where appropriate; never insert important math or scientific evidence in raster image pixels.
6. For every arrow: source ID, destination ID, direction, quantity/units or OPEN, mechanism, evidence class, boundary and whether physical/data/control/sequence. Shared extreme heat is not cross-system causation; P→T_e and T_e→P require independent gates; T_e→P requires grid-side AC evidence.
7. Produce scoped deliverables; after each file mutation run actual available tests. Retain original source and provenance.
8. Audit scientific claims and citations independently of appearance. Native editability requires saved slide XML OMML/shape verification; rendering is a separate check; desktop playback is never inferred.
9. Report file paths/commit/PR, evidence states and tests. If an external app/tool is unavailable, provide partial result rather than claiming execution.

## Invariants
- Exactly 13 approved sRGB authored colors, sourced dynamically from canonical palette; all authored backgrounds/panels/boxes white; no gradients/shadows; real photo colors excepted.
- No unapproved title, objective, scope, citation, slide count, mathematical sign/notation, or scientific mechanism changes.
- Scientific strength and visible brevity coexist: put assumptions and qualifications into notes when appropriate, not deceptive arrows or tiny text.
- Distinguish PHYSICAL, MODEL, SIMULATION, INFORMATION, ORGANIZATION and ASSESSMENT boundaries.
- Separate draft, candidate, source-established, verified, validated. No false novelty, VVUQ, model fit or SDG indicator claims.
- Keep existing legacy commands and tooling functioning; this router adds dispatch, not replacement or unrelated repos changes.

## Gate record
For each output record `intent, source_files, source_sha, target_slide, output_files, active_routes, reviewed_no_change, frozen_copy_check, palette_check, provenance_check, mechanism_trace_check, actual_omml_check, render_check, editability_check, desktop_playback_check, scientific_status, blockers`.
Every gate MUST be one of `PASS|FAIL|OPEN|NOT_RUN|NOT_APPLICABLE` and include method/evidence. `PASS` requires actual execution. Missing required evidence prevents certified release; mark PROVISIONAL or BLOCKED, never claim success from a saved PPTX or instruction text.

## Minimal command acceptance examples
- `Deck3` never invents a new deliverable.
- `Deck3 figure slide 6` routes to native editable literature matrix rather than compulsory AI PNG.
- `Deck3 heat slide 4` shows independent external forcing pathways, not a fabricated heat transfer P↔T_e.
- `Deck3 math slide 10` never claims a picture of an equation is OMML.
- `Deck3 slide 8` preserves full frozen objectives and allows text-led composition.
- `Deck3 update colors` audits the registered ecosystem but changes only impacted active consumers.
- `Deck3 animation` never claims actual PowerPoint playback without opening/testing the target.

## Versioning
This unified agent is a routing layer on top of Deck3 v1.8.4 and Dossiya Research Expert v1.4.4 as verified on 2026-10-09. A new implementation version is not claimed until related runtime tests, consumer checks and release approval are completed.
