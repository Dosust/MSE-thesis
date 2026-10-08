---
name: scientific-infographic-design
description: Convert scientific claims, presentations, chapter introductions, research problems, literature comparisons, and evidence-grounded engineering content into original, accessible, editable infographics. Select the correct visual family, declare system and model boundaries, register meaningful arrows and evidence status, keep adjacent scientific citations, and run scientific, visual, accessibility, and PowerPoint QA. Use for science-presentation infographic redesign, graphical abstracts, mechanism figures, comparison matrices, research workflows, and cited thesis slides; defer formal framework semantics to engineering-framework-design and diagram grammar to scientific-diagram-design.
license: MIT
metadata:
  version: "1.0.0"
---

# Scientific Infographic Design — Evidence-First Presentation Agent

## 0. Mission, precedence, and activation

Turn a supported **scientific message** into an original explanatory figure that can be understood at presentation size *without claiming more than the evidence proves*. This is not a decorative slide-template generator.

Use for scientific infographics and presentation/graphical-abstract figures. For formal systems-engineering framework specification, **load and obey** `.github/skills/engineering-framework-design/SKILL.md`. For element/relationship semantics and exact mathematical figures, **load and obey** `.github/skills/scientific-diagram-design/SKILL.md` and, when needed, `.github/skills/mathematical-visualization-design/SKILL.md`. This skill governs **visual compression and communication**, not the truth of a physical mechanism.

For this repository, always read in order:
1. `AI_RESEARCH_INSTRUCTIONS.md`;
2. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`;
3. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`;
4. `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`;
5. relevant frozen scientific scope/system/definition/objective files.

Never change the thesis title, frozen objective wording, full Electrified Transportation System composition, or extreme-heat thermal-only scope when simplifying graphics. A model subset is not the full system definition.

## 1. Peer-reviewed design evidence

Design method is grounded in:
- **Jambor & Bornhäuser (2024)**, *Ten simple rules for designing graphical abstracts*, https://doi.org/10.1371/journal.pcbi.1011789 — Figs 1 (sketch → draft → final), 5 (purposeful layouts), 6 (arrow ambiguity), and 2 (consistent pictograms).
- **Rougier, Droettboom, & Bourne (2014)**, *Ten Simple Rules for Better Figures*, https://doi.org/10.1371/journal.pcbi.1003833 — Figs 3 (paper vs oral presentation), 6 (misleading scales), 7 (clutter vs small multiples).
- **Kosslyn et al. (2012)**, https://doi.org/10.3389/fpsyg.2012.00230 — perceptual/cognitive presentation flaws.
- **Wong (2011)**, *Color blindness*, https://doi.org/10.1038/nmeth.1618; *Avoiding color*, https://doi.org/10.1038/nmeth.1642 — redundancy beyond hue.
- **Fujii (2026)**, *How to design effective scientific figures*, https://doi.org/10.1038/s41562-026-02466-9, Fig 1 — message, audience, chart form, iteration; figure visible on publisher page, full article may be subscription only.
- **W3C WCAG 2.2**, https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html — required graphical objects at least 3:1 contrast.
- **Microsoft PowerPoint accessibility**, https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities — reading order, alt text, titles, contrast.

Consult `references/FIGURE_REFERENCE_LIBRARY.md` for selected original figure links and **what can be learned**, not what should be copied. Do not confuse these visual-design sources with scientific evidence for domain-specific physics.

## 2. Required figure contract — before drawing

For **each** infographic prepare:

```yaml
slide_number:
slide_title:
audience:
one_main_message:
one_question_figure_answers:
figure_family:
internal_scope_authority:
physical_systems_and_boundaries:
elements_and_semantic_types:
directional_relationships:
  - source:
    target:
    transfer_or_mechanism:
    arrow_semantic_class:
    evidence_status: # ESTABLISHED / THESIS-DEFINED / CANDIDATE / OPEN
    adjacent_citation:
state_and_time_meaning:
service_consequences:
prohibited_visual_implications:
visual_layout:
visible_source_note:
speaker_note_detail:
output_format:
accessibility_and_QA:
```

If evidence for a claimed directional dependency is OPEN, either show it explicitly as a **candidate** with its gate or omit it. A decorative arrow is prohibited.

## 3. Scientific figure family selection

| Actual question | Figure family | Never confuse with |
|---|---|---|
| What belongs to the system? | **separate enclosing boundaries / architecture view** | operational/service boundary condition |
| What external factor acts on the equipment? | **parallel forcing → state → capability lanes** | proven cross-system coupling |
| How might a source influence a receiver? | **directional, source→constraint→interface→receiver mechanism lane** | association or shared exposure |
| Which mechanisms have evidence? | **source-by-claim / qualification matrix** | unjustified all-or-none novelty claim |
| What remains to be studied? | **established→documented limitation→bounded handoff→proposed test** | “nobody has done this” |
| Which objective leads to what output? | **objective-to-output traceability** | boxes whose links are arbitrary |
| What happens with state and time? | **state-time timeline/trajectory with admitted thresholds** | invented measured/simulated data |
| How does research advance? | **evidence/qualification/model/VVUQ workflow with gates** | physical causal flow |
| What outcome is delivered? | **physical state → capability → service → service-based resilience** | state = service |
| How compare response consequences? | **side-by-side cases / two-pathway assessment** | automatically beneficial sustainability |
| How explain many series? | **small multiples / aligned comparison** | rainbow/3D/clutter charts |

Prefer **one principal figure family per slide**. Avoid turning a formal architecture into an infographic with untraceable arrows.

## 4. Arrow grammar and evidence status must be orthogonal

**Never silently redefine a line style that the active framework/diagram skill already assigns a semantic meaning.** Default repository grammar:

- solid direction: physical or information transfer;
- heavy direction: justified cause/effect propagation;
- dashed: control/intervention;
- dotted return: observation/feedback;
- thin non-directional line: membership/association;
- bidirectional: only where the two separate directions are individually justified.
- If the graphic is solely a *method workflow*, declare a distinct methodological-process grammar/legend; do not imply a physical conservation flow.

**Evidence status is a separate textual attribute, never encoded by dash style alone:**
`ESTABLISHED`, `THESIS-DEFINED`, `CANDIDATE — qualification required`, `OPEN — source verification required`.

For every arrow record source, target, actual mechanism/exchange, direction, arrow class, evidence status, and adjacent source. A two-headed P↔T_e identity symbol denotes the *investigation scope* only if expressly labeled; it must not be presented as proven bidirectional thermal physics.

## 5. Visual grammar and accessibility

- Exact **white #FFFFFF background and white box/panel interiors**. No gray/off-white tints, filled colored cards, gradients, shadows, gold, textures, or invented visual effects.
- Use **black text**. Allow controlled semantic color for borders, headings, large arrows, and small accents only. Thesis profile defaults: blue=Power, green=Electrified Transportation, muted red=external extreme heat; always label components in text.
- No mini arrows. Every arrow must be thick/large enough to be understood at slide scale.
- Consistent typefaces, aligned margins, whitespace, label placement, line widths, and diagram icon family.
- Do not rely on hue to differentiate components/directions/status. Verify grayscale meaning and color-vision accessibility (Wong, 2011).
- Important graphical lines/icons must be distinguishable (WCAG non-text 3:1 criterion); use adequate text contrast and legible projection typography.
- Prefer editable PowerPoint shapes/text and vector SVG export. Native shapes are the default for boundary/arrow/evidence workflows.
- **No invented data trajectories, thresholds, temperature figures, derating curves, plots, equations, validation findings, or numerical service deficits.** Conceptual shapes/axes must say `CONCEPTUAL / NOT MEASURED` if interpretation otherwise ambiguous.
- A caption/source note is part of the scientific figure, not an optional footer.
- For slides, use compact adjacent APA author–date citations to externally supported claims; a final reference list alone **fails**.

## 6. Design pipeline (non-optional)

1. **Read authority and evidence:** establish what the exact literature supports, full-system boundary, active model subset, and OPEN items.
2. **Distill the one-sentence message:** reject “show resilience” / “draw systems” as insufficient.
3. **Select figure family:** choose based on the scientific question and audience, not aesthetics.
4. **Draft a storyboard:** arrange correct objects/lanes/boundaries and register arrows and evidence status.
5. **Prototype a black/white layout:** hierarchy, negative space, arrows; test that grayscale-only still reads correctly.
6. **Add semantic accents and citations:** source metadata verified, exact claim-source match, meaningful arrow labels.
7. **Render editable artifact:** use deterministic geometry whenever feasible; speaker notes carry derivations and extended context.
8. **Run four hard QA gates:** scientific truth, citation/evidence, visual meaning, accessibility/technical integrity. If blocked, explicitly report `BLOCKED / OPEN`.
9. **Render/review at multiple scales:** native 16:9 and thumbnail; inspect clipping, label collision, genuine arrow direction, and reading order; correct before delivery.

Jambor & Bornhäuser (2024) Fig 1 is a precedent for iterating from rough structure to usable figure, NOT permission to trace its artwork. Rougier et al. (2014) Fig 3 specifically motivates simplifying oral-presentation views without changing the underlying scientific message.

## 7. Thesis-specific non-negotiables

The two physical systems are the **Power System P** and the full canonical **Electrified Transportation System T_e**. The latter includes electrically propelled road vehicle, RESS, propulsion/auxiliary electrical systems, vehicle power-supply circuit, EVSE, physical connection, and communication/control needed for power transfer (bidirectional where supported). EVSE is not a third infrastructure. `System Boundary` is not a mathematical `Boundary Condition`.

Extreme heat is an **external forcing**; its separate effects on P and T_e do **not** independently prove thermal interdependency. For each candidate P→T_e and T_e→P direction, show an evidence gate and label admission status. A decreased EVSE DC charging output does not by itself establish the sign, shape, or timing of upstream AC input change; qualified equipment and measured/defensible interface behavior are required. Physical state, thermal capability, electricity/mobility service, resilience, and sustainability are distinct objects. Critical state-transition time, propagation delay, service-consequence time, and recovery time cannot be conflated.

Keep frozen GO and SO1–SO3 **verbatim**. Final RQs/hypotheses, component models, equipment cases, numerical thresholds, validation results, and exact novelty remain OPEN until admitted under the current canonical authorities.

## 8. Chapter 1 figure-routing guide

Use `references/CHAPTER1_FIGURE_STORYBOARD.md` as the figure-by-figure plan for the active 16-slide introductory presentation. Source-specific design citations belong with that storyboard; domain physics literature is assessed separately for each scientific claim.

## 9. Failure cases and hard stop

FAIL and revise if any figure:
- shows gray or tinted interior/background without explicit user permission;
- silently narrows full T_e to EVSE alone;
- promotes a proposed thermal interaction to an established mechanism;
- uses dashed arrow to mean uncertainty when that style is already reserved for control;
- adds arrows for decoration or reading order alone;
- puts a method workflow arrow in the physical-causation grammar without explanation;
- has bibliography-only citations without adjacent domain-claim attribution;
- shows measured-looking curves or numerical thresholds with no source;
- merges resilience and sustainability or claims response automatically improves both;
- cannot be edited when the deliverable requires editable diagrams;
- clips any label, equation, source note, or crucial boundary;
- borrows protected figures/artwork without permission and attribution.

## 10. Verification fixtures

**Fixture A — Parallel extreme-heat exposure (Chapter 1 Slide 4):**
`heat [outside] → P thermal state → P capability` and independently `heat [outside] → T_e thermal state → T_e capability`. PASS only if *no thermal P↔T_e coupling is inferred*. Cite a transformer thermal source and a charger-specific heat response source on the respective lanes.

**Fixture B — Directional mechanisms (Slide 5):**
Two lanes, P→T_e and T_e→P, with separately specified source thermal state, thermal constraint, power-transfer interface, receiver response, time consequence, and evidence gate. PASS only if missing data are labeled CANDIDATE or OPEN; no fake two-way feedback loop or inferred AC electrical response.

**Fixture C — System boundary (Slide 9):**
Show full T_e scope, separate P scope, explicit electrical interface, and a smaller **active model subset** drawn as a different enclosing boundary. PASS only if EVSE remains part of T_e and mobility service is an output, not a physical component.

## 11. Version history

### 1.0.0 — 2026-10-08
Established peer-reviewed figure-reference workflow, figure family routing, presentation-level semantic compression, explicit arrow-vs-evidence orthogonality, mandatory adjacent in-text scientific citations, frozen P–T_e thesis boundary, PowerPoint accessibility checks, and three scientific fixtures.

