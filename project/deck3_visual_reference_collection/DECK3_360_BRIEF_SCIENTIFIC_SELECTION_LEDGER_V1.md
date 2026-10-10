# Deck3 — Scientific Minimal Selection Ledger V1
**Date:** 2026-10-10
**Status:** DESIGN SELECTION COMPLETE; SCIENTIFIC FIGURE RELEASE NOT APPROVED.
**Inputs:** Original 160 conceptual briefs from `main`, plus new 200 simplified briefs on `feature/deck3-unified-agent-20261009`. Per slide inspected 16 + 20 brief entries = **36** alternatives, Slides 3–12; **360** entries total. This is comparative **brief selection**, not verification of 360 rendered images.
**Governance:** `.github/skills/deck3/references/DECK3_SCIENTIFIC_MINIMAL_INFOGRAPHIC_STANDARD_V1.md`; current thesis authority index; `project/CONCEPTUAL_FRAMEWORK_CAUSAL_QUALIFICATION_APPLICATION_V1.md`; canonical 14-slide text on feature branch. All freezes, qualifications and sourcing requirements remain controlling.

## Chosen figure grammar: one central scientific purpose per slide

| Slide | Selected conceptual lead(s) | Considered competing lead(s) | Smallest justified figure and reason for selection | Scientific disposition |
|---|---|---|---|---|
| 3 — Systems | **D3N-003** Feeder-to-EVSE functional boundary | D3-005, D3-011, D3N-005, D3N-011 | One P boundary + one T_e boundary; one unambiguous AC measurement/energy-input port. Recognizable equipment optional only if it clarifies subsystem membership. Do not draw V,I,P,Q as four flow arrows or infer V2G. | CONCEPT SELECTED; port topology/source details OPEN |
| 4 — Heat | **D3N-021** Ambient heat common cause | D3-017, D3-021, D3N-027, D3N-037 | One external ambient forcing node feeding **two separate** physical response branches; transformer and EVSE, each with an equipment thermal state. Time histories may appear only if needed and explicitly conceptual. | CONCEPT SELECTED; device-specific response OPEN |
| 5 — Problem | **D3N-041 + D3N-043** Hypothetical P→T_e and T_e→P mechanisms | D3-033, D3-035, D3-037, D3-039, D3N-045, D3N-047, D3N-051, D3N-057 | Two symmetric conditional branches are necessary because **comparison of direction is the central message**. Place common heat as independent forcing above both. Embed an operating-restriction condition and measured grid-side AC response inside the pathways. **Not** automatic bidirectional energy transfer. | CONCEPT SELECTED; both transmission directions **CANDIDATE, NOT VALIDATED** |
| 6 — Literature | **D3N-075** Supported vs proposed conclusions | D3-049, D3-051, D3-057, D3-063, D3N-069, D3N-071 | Two-column evidence boundary: admitted published component behavior vs unresolved coupled-level inference. Publication citations appear as editable native text; novelty stays OPEN. | CONCEPT SELECTED; source-to-claim audit OPEN |
| 7 — Questions | **D3-071** Inquiry stages | D3-065, D3-067, D3-069, D3N-081, D3N-083, D3N-085 | Three equal-height RQ cards with **question roles**, without invented mathematical response curves. Workflow arrows only if approved interpretation is sequential. Exact RQ text remains outside graphic in editable slide text. | CONCEPT SELECTED; RQ authority comparison OPEN |
| 8 — Objectives | **D3N-115** Objective hierarchy not causal flow | D3-081, D3-089, D3-095, D3N-101, D3N-109 | One general objective parent, three objective children. Connectors mean hierarchy only (no causal arrows). Exact frozen GO/SO1–SO3 in editable Times New Roman text. | CONCEPT SELECTED; exact source-wording QA required |
| 9 — Boundary | **D3N-121** Full inventory versus active model | D3-097, D3-099, D3-101, D3-103, D3-105, D3N-127, D3N-133 | One thin overview boundary (19 P + 21 T_e **candidate entries**, not devices/states) above a single selected feeder-transformer–AC-port–EVSE–vehicle chain. IEEE 13 B0/B1 and IEEE 123 roles as small accurate labels only. | CONCEPT SELECTED; benchmark configuration still needs source-level proof |
| 10 — Physics | **D3N-141** Conservation control volume | D3-113, D3-121, D3-123, D3N-143, D3N-151 | One control-volume diagram, distinct heat-generation and net heat-out terms, one correctly typed energy-balance relation; optional adjacent minimal hybrid DAE after independent mathematical check. Avoid fabricated temperature curves. | CONCEPT SELECTED; constitutive closure and parameter validation OPEN |
| 11 — Methodology | **D3N-179** Open gate instead of passed checkmark | D3-129, D3-131, D3-133, D3-139, D3N-161, D3N-163, D3N-177 | Five-step evidence→B0→B1→thermal qualification→IEEE 123 investigation with **open gates**; distinguish verification, thermal validation and causal inference. No success checkmarks. | CONCEPT SELECTED; simulations and field validation NOT_RUN |
| 12 — Outcomes | **D3N-185 + D3N-187** Direct vs engineering-response pathways | D3-145, D3-147, D3-149, D3-151, D3-153, D3N-199 | Two clear consequence pathways from **defined electricity/mobility services**. Separate matched baselines; env/econ/social metrics placeholders only when data and factors exist. | CONCEPT SELECTED; measured consequences OPEN |

**Mode selection:** use **NATIVE_SCIENTIFIC** or **NATIVE_SCHEMATIC** for every scientific relationship; `EQUIPMENT_ASSET_ONLY` and older `HYBRID_SCENE` are optional supplemental equipment imagery, never a source of science. At most one equipment illustrative scene per mechanism group when needed; omit if a minimal schematic is clearer.

## Slide 5 — Falsifiable scientific storyboard, pending validation
**Single question:** Can extreme-heat-conditioned operational changes cause attributable cross-system effects in either direction, beyond common heat exposure?

**Visual construction**
- Top center: `T_a(t)`: **shared external forcing**. Two separately drawn exposure arrows toward P equipment and T_e equipment. Exposure arrows represent boundary thermal conditions, NOT energy transfers from P to T_e.
- Left branch `P→T_e` (hypothesis): transformer thermal state `x_P^{th}(t)` → **verified-if-applicable thermal operating constraint** → admissible grid AC delivery/EVSE charging capability → possible mobility service impact, if service requirements are defined.
- Right branch `T_e→P` (hypothesis): EVSE thermal/control state `x_{T_e}^{th}(t)` → evidence-qualified controller action → measured or modeled `\Delta P_{AC}(t),\Delta I_{AC}(t)` at defined interface → possible change in transformer losses/thermal state. Sign **may be negative, zero or positive depending on response/scenario**; never draw automatic temperature rise.
- Center: one **grid-side AC port**, `V_{AC},I_{AC},P_{AC},Q_{AC}` as observables, not four energy-flow arrows. Distinguish electrical energy transfer from operational influence. No unsupported V2G/reverse energy export.
- Bottom note: `Conditional mechanisms — directional attribution not yet established; common ambient heat is a competing explanation.`
- Required comparative tests: matched ambient/exposure and demand/control trajectories, transformer limit evidence, verified charger topology and derating law, independently measured grid-side AC response, chosen service metric and threshold/time definitions.

**No compulsory mathematical figure clutter:** equations and evidence can sit in neighboring native text and notes, preserving a simple visual. Native editable labels + typed arrows; actual device scene optional and unlabelled.

## Individual release gate audit (design-stage, not simulation stage)
| Gate | What checked | Result / unresolved work |
|---|---|---|
| G0 authority | Current scope + exact frozen objectives, 14-slide purpose alignment | **PASS for selection logic**, exact final slide text reproduction NOT_RUN |
| G1 physical correctness | Correct ontology, AC versus heat/control, shared forcing, direction status | **PASS for storyboard semantics**, device-specific mechanism qualification OPEN |
| G2 evidence/rights | Design briefs have no external figure assets; actual paper claims and future equipment imagery need traceable provenance | **OPEN** (not 360 licensed images; no external artwork admitted yet) |
| G3 simplicity | One principal message and minimum concepts, two groups only on comparison slides | **PASS for design selection**, projected reading test NOT_RUN |
| G4 render geometry | Times New Roman, white, 13 palette, 16:9 prescribed | **NOT_RUN** until rendered and reviewed |
| G5 editability | Native objects required; no all-raster scientific figure | **NOT_RUN** until PPTX constructed |
| G6 animation | Reveals planned by physical meaning, retain prior groups | **NOT_RUN** until PowerPoint playback observed |
| G7 provenance | Selected brief IDs and rationale recorded here | **PASS for brief selection**, final files/hashes and per-slide figure ledger OPEN |

**Non-compensatory:** “Selected” does NOT mean “scientifically validated” or “release-ready.” Even an excellent render fails publication/animation acceptance until G0–G7 gates pass with evidence.

## Practical next execution
(1) Build slide 5 only from native diagrams and optional equipment-only illustration; (2) independently inspect physical arrow ledger, citations, font and readability; (3) verify actual animation in Microsoft PowerPoint; (4) only then assemble remaining slides using the ten selected grammars. Do **not** expand the 360-brief library.
