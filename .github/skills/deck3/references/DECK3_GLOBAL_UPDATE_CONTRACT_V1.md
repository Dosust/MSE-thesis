# Deck3 Global Update Technical Annex V1 — All-Skill, All-Stage Change Control

## Deck3 all-forms v2 learning contract (2026-10-09)
For every Deck3 text-in-chat, Stage 1 PPTX, one-slide edit, AI scientific figure, mechanism diagram, engineering framework, mathematical visualization, Stage 3 assembly, animation, export and QA, apply `.github/skills/deck3/references/DECK3_ALL_FORMS_WEAKNESS_LEARNING_V2.md` and corrected Dossiya Research Expert `.github/skills/dossiya-research-expert/references/DECK3_WEAKNESS_TO_VERIFIED_LEARNING_V2.md`. The two old Deck3 learning V1 protocols remain historical and are superseded for active work. Use the actual A13/B13/C13 feature mapping. **Do not equate frozen objectives with validated physics; preserve research scope.** For physical slides, prefer one unified scientifically plausible real-equipment AI scene + scientifically meaningful clearly directed arrows + minimal exact on-scene labels; use native editable labels/ports/equations when possible. Do not turn science into unrelated abstract boxes, invented outputs or embedded literature-card panels. Apply gates G01–G15, falsification cases A01–A20, source/citation review and stage-specific tests; record NOT_RUN rather than PASS for unperformed verification.


**Status:** IMPLEMENTATION / QA ANNEX to the **primary** `.github/skills/deck3/references/DECK3_GLOBAL_UPDATE_CONTRACT.md`, subordinate to current scientific authorities and the canonical Deck3 palette. It elaborates technical checks; in case of textual conflict, primary contract and frozen authorities prevail. This is NOT a second competing policy.
**Trigger:** A user instruction such as **“update Deck3”**, **“make update of Deck3”**, **“upgrade the Deck3 design solution”**, or an unqualified Deck3 skills update.
**Scope:** the entire related Deck3 ecosystem, not merely the file named in the most recent turn.

## Deck3 v1.8.1 figure-media routing and fail-closed approval

**Read** `.github/skills/deck3/references/DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md` for every Deck3 text, figures, image-generation, assemble, and release task. **A scientific diagram is not automatically an AI image.** Use equipment-centered original images only where physical objects matter; use **native editable PowerPoint** for literature/gap matrices, RQ/SO alignment, evidence-gated cross-system pathways, methodological workflows, contribution maps and chapter roadmaps. The strict no-embedded-explanatory-panels rule still applies to all images, and AI-rendered author citations are not evidence. Frozen GO/SO1–SO3 and the actual user-approved slide count must be preserved verbatim; the current 13-slide Chapter 1 baseline remains authoritative unless explicitly changed. **The prior ten AI PNG draft figures are provisional, not approved Stage 2 assets.** Do not use SVG checks, correct output dimensions, or a saved PPTX as a substitute for source review, mechanism trace, figure-only panel inspection, rendered readability, native editing and real animation playback.

## Deck3 v1.8 — scientific-mechanism traceability (binding for Deck3 outputs)

Read `.github/skills/deck3/references/DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md` (relative from repository root). Design each relevant figure to show **real components, independently defined physical/model/simulation boundaries, labeled directed interfaces, carried quantities/units or explicit OPEN, physical laws/operator status, observation/control/feedback, and state-time/service consequences**—not generic attractive boxes. Distinguish physical/electrical transport from measured data, estimates, control decisions, simulations and post-model assessments. Require independently evidenced P→T_e and T_e→P candidate mechanism gates; for T_e→P, grid-side AC behavior is a mandatory evidentiary distinction. Shared extreme heat is external forcing, not proof of interdependency. **A curved arrow is not a nonlinear equation**; two directions are two separate claims.

A scientific figure can supply a same-stem `*.trace.json` sidecar validated with Deck3 `examples/mechanism_trace_qa.py`; successful structural review does not validate the physics. Missing trace means **provisional**, and malformed/provenance-inconsistent trace blocks Deck3 image audit/assembly. Science-source checking, native-PPTX geometry, effective visual occupancy, editable object ID mapping, animation click order, exact 13-token sRGB colors and actual PowerPoint playback remain separate acceptance requirements. Keep approved slide text, real adjacent citations, full P and T_e scope, frozen GO/SO1–SO3 and white-only authored interiors unchanged. The IEEE figure supplied by the user is *design inspiration only*; do not copy its artwork or infer the paper's unverified scientific claims.

## 1. User-intent contract

An unqualified **update Deck3** request means:
1. Read the current `.github/skills/deck3/SKILL.md`, this contract, the dependency registry and the exact authoritative palette.
2. Inventory **every** relevant stage and its shared skill and implementation: scientific scope/evidence, user-facing writing, text and citation production, layout, scientific figures, SVG/vector/PNG/raster image generation, mathematical diagrams and plots, arrow geometry, native editable PPTX construction, assembly, animation, accessible exports, rendered review, and release QA.
3. Establish the requested change's **impact across all these categories**, not automatically change unrelated files. For unaffected categories, explicitly record **REVIEWED_NO_CHANGE** and why.
4. Implement all impacted changes consistently in instructions **and** applicable runtime generators/tests, not only a Markdown sentence.
5. Confirm source authority, evidence and palette **before** generating; regenerate older affected assets when asked to revise them. Never silently replace an approved source deck or assert that existing artifacts are retroactively compliant.
6. Run the applicable tests and examine actual generated products. Mark pending tests **NOT_RUN** and absent data **OPEN**, never PASS by inference.
7. Commit changed files to GitHub and provide an impact/QA ledger with commit/PR refs. Repository changes are the durable project source of truth. Memory features outside GitHub are not asserted as changed unless separately confirmed.

A scoped request such as “Deck3 figures slide 5” or “Deck3 change heading color only” overrides breadth of execution, **not** the requirement to identify/test affected dependencies. The update command is a dependency-review rule, not permission to create unrelated slides.

## 2. Dependency hierarchy and included skill families

The machine-readable registry is `DECK3_DEPENDENCY_REGISTRY.json` alongside this file. Review:
- **Scientific authority:** `AI_RESEARCH_INSTRUCTIONS.md`, current thesis authority index, evidence/non-invention standard, official objectives/scope/state-time and citation rules. These cannot be overridden by visual instructions.
- **Core Deck3:** `deck3/SKILL.md`, `references/WORKFLOW.md`, `examples/deck3.py`, `tests/`, `.github/workflows/deck3-tests.yml`.
- **Copy:** `dossiya-writing/SKILL.md`; exact native slide text, invisible manuscript/template metadata, citations, typography, notes.
- **Research expertise:** `dossiya-research-expert/SKILL.md`; classify claims, sources, mechanisms and validation, and stop unsupported inference.
- **Scientific figures:** `scientific-infographic-design/SKILL.md`, `scientific-diagram-design/SKILL.md`, generators and their tests.
- **Framework and mathematics:** `engineering-framework-design/SKILL.md`, `mathematical-visualization-design/SKILL.md`; real system/active model distinctions, equation and chart admission, physical vs methodological arrows.
- **PowerPoint advanced:** `deck3/advanced_powerpoint/SKILL.md`, object/arrow/reveal registries, tests, graphic/animation capabilities, editable shape/text/citation preservation.
- **Export and accessibility:** visible proof-size, image/SVG integrity, XML/PPTX archive and native object checks, citations and notes, reading order, contrast and reliable static fallback.

## 3. EXACT COLOR AUTHORITY — NO LEGACY PALETTE

The single allowed authored palette is `.github/skills/deck3/references/DECK3_SRGB_PALETTE.json`. Every generator MUST **read it at runtime**; no copied dictionary and no hardcoded alternative RGB palette may supersede it. Exactly 13 permitted 8-bit sRGB tokens.

- All slide backgrounds, plot canvases, diagram panels, text-box fills, headers, legends and interiors MUST equal `#FFFFFF`.
- ASU Maroon `#8C1D40`: institutional heading identity; ASU Gold `#FFC627`: **nonessential small accent only**. Bright Turquoise `#6ACEEE`: optional nonessential accent only. Gold/turquoise fail critical-text or thin-arrow contrast on white.
- Use the palette's semantic roles; essential text contrast >=4.5:1, essential diagram marks >=3:1 on white. Colors must not be the only scientific distinction.
- Noncanonical authored strokes, labels, chart series, icons, SVG gradients, fills, theme overrides and raster-derived diagram palettes are violations. `#183D63`, `#2670AC`, `#207775`, `#505B67`, `#BAC6CF`, `#202932`, `#B16B26` are **historical rejection examples, not acceptable fallbacks**.
- Source photos and genuinely photorealistic equipment retain authentic observed colors. Do not indiscriminately require each photograph pixel to match the authored 13-color registry. A photo exception must be explicitly classified and verified; it does not allow tinted graphics/overlays.

### Color verification order

1. Check design source (named tokens and SVG/CSS/PowerPoint authored style properties) **before composition**.
2. Check authored text/shape/arrow/chart properties in composed PPTX at OOXML/native-shape level when tooling supports it; flag unresolved theme colors. Pictures alone cannot be certified from PPTX object properties.
3. For authored PNG diagrams, require a proven color-controlled editable/vector source or documented raster exception; antialiased pixels should not be compared naively to 13 exact RGB triplets.
4. Visually inspect rendered slides for tinted fills, low contrast and substitutions. No generator's own PASS flag substitutes for independent inspection.
5. An old off-palette scientific figure must be regenerated from the corrected generator. **Do not silently map arbitrary legacy colors to nearest colors**; map by scientific role.

## 4. Six release gates for every Deck3 change

| Gate | Mandatory verification | Status on failure |
|---|---|---|
| S — science/citations | Frozen scope/objectives verbatim; claim-level source, arrow and equation provenance; candidate vs established | BLOCK |
| W — writing/text | Meaningful claim text, editable copy, no visible `MAIN MESSAGE`/`THREE KEY POINTS`, citations/notes unchanged | BLOCK |
| C — colors/surfaces | Canonical token audit in each created SVG, generator, graphic and slide; pure-white authored interiors | BLOCK |
| F — figures/geometry | Correct full Power vs T_e boundary, arrow meanings, real visual label legibility, 70–80% **effective meaningful content** share or justified exception | BLOCK or PROVISIONAL |
| A — assemble/animation | Figure mapping, hash and aspect ratio, native editing, exact slide text/notes, correct OnClick sequence, independent playback if claimed | BLOCK / UNVERIFIED |
| Q — final review | All slides rendered, visually audited, scientific qualification and release report with evidence for every passed gate | PROVISIONAL until verified |

**Precise outcomes:** `SOURCE_ONLY` ≠ `TESTED_RUNTIME` ≠ `RENDERED_QA_PASS` ≠ `POWERPOINT_PLAYBACK_VERIFIED` ≠ `PHYSICALLY_VALIDATED`. Partial tests must never be called full certification.

## 5. Existing-artifact rule

Any older assembled PPTX or scientific image from a legacy off-palette generator is **PROVISIONAL_NOT_COLOR_CERTIFIED** until:
1. authoritative source palette comparison is performed;
2. invalid authored marks are mapped by semantic role and regenerated;
3. the independent SVG/source, full PPTX authored shape/theme properties and final render are audited as applicable;
4. scientific mechanism and evidence status are reviewed;
5. geometry, readable typography, frozen objective strings, notes and animation behavior are checked.

An actual thermal interdependency is not established by a P↔T_e graphic, charging connection, common extreme heat, or simulated trajectory alone.

## 6. Change request and completion format

Every update should record:
```yaml
trigger: "update Deck3"
baseline_commit: <actual sha>
affected:
  science: REVIEWED_NO_CHANGE | CHANGED | BLOCKED
  writing_text: REVIEWED_NO_CHANGE | CHANGED | BLOCKED
  color_palette: REVIEWED_NO_CHANGE | CHANGED | BLOCKED
  figures_vector_raster: REVIEWED_NO_CHANGE | CHANGED | BLOCKED
  mathematical_graphics: REVIEWED_NO_CHANGE | CHANGED | BLOCKED
  pptx_assembly_animation: REVIEWED_NO_CHANGE | CHANGED | BLOCKED
  accessibility_exports: REVIEWED_NO_CHANGE | CHANGED | BLOCKED
tested: [{name: exact_command, result: PASS | FAIL | NOT_RUN}]
reviewed_outputs: [{path: actual_existing_path, status: VERIFIED | PROVISIONAL | BLOCKED}]
scientific_blockers: [explicit unresolved items]
git_commit_or_pr: <actual reference>
release: PASS | PROVISIONAL | BLOCKED
```

Do not fabricate a memory update or an approval. Durable behavior is defined in the repository; a ChatGPT Memory change requires its own product process.

## 7. Maintenance

Whenever this contract changes, update the **parent Deck3 dispatch**, linked skill route notices, machine-readable registry, CI/test inventory and source-generator QA. Evaluate each affected presentation before releasing. If current source/canonical authority conflicts with an older example, **current canonical wins** and the example is migrated, quarantined or explicitly marked legacy.
