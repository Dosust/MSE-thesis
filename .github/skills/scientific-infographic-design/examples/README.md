# Reproducible Scientific Infographic Examples

**Purpose:** Demonstrate complete, original, source-aware scientific design workflows—not merely styling prompts. None of the examples represents admitted case-specific transformer, battery, or EVSE performance data.

## Start here

| Need | Read / run | What it produces | Why it matters |
|---|---|---|---|
| Decide how to communicate a source-backed claim | \`WORKED_FIGURE_RECIPES.md\` | Registered element/arrow/claim specification | Physical semantics precede drawing |
| Generate 16:9 editable vector scientific scenes | \`python figures.py --out build/\` | \`build/chapter1_slide_03.svg\`, \`04.svg\`, \`05.svg\` | Fully original deterministic SVG/XML shapes and text |
| Generate native-editable PowerPoint shapes | \`python pptx_builder.py --out build/infographic_examples.pptx\` | Three example PowerPoint slides | Text, panels, arrows remain native editable objects |
| Compute mathematically declared event times | \`python mathematical_metrics.py\` | Synthetic unit-test PASS/FAIL | Validates implementation of formula, not equipment physics |
| Select generator and import into an existing 16-slide PPTX | \`pptx_recipe.md\` | Safe slide-revision workflow | Preserve unchanged slides, frozen content and citations |
| Test numerical/semantic invariants | \`python -m unittest discover -s tests -v\` from skill root | Python tests | Catch implementation errors and scope/arrow regressions |

### Installation

Python 3.10+ recommended. \`figures.py\` and \`mathematical_metrics.py\` require only the standard library. Editable PPTX generation additionally needs:

\`\`\`bash
python -m pip install python-pptx
\`\`\`

### Commands (run from skill root)

\`\`\`bash
python examples/mathematical_metrics.py
python examples/figures.py --out build
python examples/pptx_builder.py --out build/chapter1_prototypes.pptx
python -m unittest discover -s tests -v
\`\`\`

**Notes:** Slides 3,4,5 are original *conceptual examples*. If a renderer, package, or source file is unavailable, log \`BLOCKED\`; do not replace missing experiment data with invented numeric curves. Python code produces a three-slide demonstration and does **not** overwrite or alter the canonical 16-slide user presentation by default.

## Evidence and caption handling

The SVG/PPTX examples include source names on the same slide but the complete thesis must still maintain a verified author–date citation-to-reference mapping. The design-library sources teach *visual presentation practices*; they cannot support transformer physics or case-specific charging limits.

Full technical T_e composition is controlled by \`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md\`; active thermal-only scope by \`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md\`. Do not let a small panel's visible list be mistaken for exhaustive T_e membership.

## Expected test categories

1. **SVG technical:** valid XML, all rectangular interiors #FFFFFF, no flattened bitmap images.
2. **System semantics:** separate P and full T_e, EVSE inside T_e, no unintended external hazard as internal system component.
3. **Heat semantic:** exactly two independent external-forcing effects; zero P↔T_e thermal causal arrow.
4. **Mechanism semantic:** P→T_e and T_e→P candidate tracks; grid-side AC input gate required for thermal influence on P.
5. **Numerical mathematical:** strict time ordering; finite values; linear crossing; absent event; simultaneous events; propagation event ordering; service-deficit sign crossings and units.
6. **PowerPoint technical:** opens, all three demonstration slides have numerous editable native shapes and no raster pictures. Actual slide rendering still requires visual review outside those tests.
7. **Citation:** scientifically sourced claims have visible author–date text or exact internal source notes; unverified claims labeled OPEN/CANDIDATE.

## Scientific validation limitations

*Passing a software test is not model verification in its full physical sense, and model verification is not independent empirical validation.* The example functions deliberately avoid physical equipment constants, data transfer assumptions, calibrated thermal laws and actual resilience findings.

**Method reference:** Oberkampf & Trucano (2002), https://doi.org/10.1016/S0376-0421(02)00005-2.  
**Design reference:** Jambor & Bornhäuser (2024), https://doi.org/10.1371/journal.pcbi.1011789 ; Rougier et al. (2014), https://doi.org/10.1371/journal.pcbi.1003833.
