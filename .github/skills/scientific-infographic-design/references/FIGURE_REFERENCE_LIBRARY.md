# Curated Figure Reference Library — Original Scientific Design Examples
**Status:** Working figure-precedent registry | **2026-10-08**  
**Purpose:** Study the visual grammar and scientific-communication function of original figures; do not use their domain objects, experimental data, unique illustrations, or styling as thesis-specific evidence.

The figure DOI/URL points to the **original figure in its publication**. Textual observations concern design decisions, not validation of the thesis's Power–Transportation physics.


## How the agent actually uses this library (v2.0)

This is a **reference-selection** file, not a prompt to replicate someone else's graphic. For exact **when/why/how**, worked arrow registers, publication-vs-slide reduction, and figure-by-figure failure tests, read \`FIGURE_DESIGN_APPLICATION_GUIDE.md\`.

**Six high-value direct mappings:**
1. **Fig 5 / Jambor & Bornhäuser (2024):** parallel lanes for shared heat, nested/disjoint enclosures for scope, sequential gates for methodology. Why: layout itself communicates which relation exists.
2. **Fig 6 / Jambor & Bornhäuser (2024):** label \`electricity supply\`, \`charging-load effect\`, \`external heat forcing\`, or \`candidate mechanism\` on each respective direction. Why: arrows are not all causality.
3. **Fig 3 / Rougier et al. (2014):** move long physics derivations into notes while retaining exact boundary, status, and same-slide citation. Why: oral display requires faster comprehension.
4. **Fig 7 / Rougier et al. (2014):** separate verified scenarios/services on aligned axes rather than making a cluttered multiseries plot. Why: independent comparison is clearer.
5. **Fig 1 / Jambor & Bornhäuser (2024):** start with registries and a wireframe, then create a deterministic figure, then rerender and revise. Why: scientific correctness is cheapest to fix before visual polishing.
6. **Fig 6 / Rougier et al. (2014):** label quantitative axes and scales, never imply important-looking magnitude without data. Why: visual encodings can distort scientific findings.

**Added verified references for checklists and communication:**
- Jambor (2025), *A checklist for designing and improving the visualization of scientific data*, https://doi.org/10.1038/s41556-025-01684-z — final figure design and feedback QA.
- Oliverio & Wright (2025), *The art of the graphical abstract—a visual approach to scientific storytelling*, https://doi.org/10.1002/1873-3468.70163 — reading order and visual hierarchy.
- W3C WCAG 2.2 non-text contrast guidance, https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html — graphical-object contrast.
- Microsoft PowerPoint accessibility guidance, https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities — titles, reading order and alternative text.

**Rigor check:** each original article must support only the *visual rule* attributed to it. Transformer, charger, mobility-service, P/T_e causality, and model equations need different sources under the frozen repository citation standard.

**Runnable examples:** \`../examples/figures.py\` (three schematic SVG scenes); \`../examples/pptx_builder.py\` (three native-editable PPTX scenes); \`../examples/mathematical_metrics.py\` (synthetic software tests); \`../tests/test_examples.py\` (regression suite); \`../examples/README.md\` (instructions).

## Ranked primary figures

| Priority | Source and exact figure | What the original demonstrates | Rule to transfer | Thesis slide | Licensing/reuse |
|---|---|---|---|---|---|
| 1 | **Jambor & Bornhäuser (2024), Fig 5**. https://doi.org/10.1371/journal.pcbi.1011789.g005 | Different layouts with clear beginning/end; linear, circular, comparative/nested depending on message | Select layout from causal/process/static-comparison semantics; never force everything into a flowchart | 2, 5, 8, 10, 13 | PLOS article CC BY 4.0; attribute. Do not copy source pictograms into a thesis figure |
| 2 | **Jambor & Bornhäuser (2024), Fig 6**. https://doi.org/10.1371/journal.pcbi.1011789.g006 | Different arrow forms and context-dependent interpretations | Define exactly what each arrow means; prevent control/causality/status collision | 3–5, 9–12 | CC BY 4.0; attribute |
| 3 | **Rougier et al. (2014), Fig 3**. https://doi.org/10.1371/journal.pcbi.1003833.g003 | Same underlying simulation represented for journal versus oral presentation | Oral slides need simplified lines/labels/annotations; data meaning must stay identical | 4–6, 10–12 | PLOS article CC0, public-domain dedication |
| 4 | **Rougier et al. (2014), Fig 7**. https://doi.org/10.1371/journal.pcbi.1003833.g007 | Many cluttered overlapping plots versus readable small multiples | Split rather than overplot; avoid rainbow series and obstructing legends | 6, 10, 12; eventual results | CC0 |
| 5 | **Jambor & Bornhäuser (2024), Fig 1**. https://doi.org/10.1371/journal.pcbi.1011789.g001 | Sketch → rapid draft → final scientific composition | Storyboard first; iterative improvement after semantic correctness | all infographic slides | Figure's authors report CC0 for their drawings; article CC BY attribution |
| 6 | **Rougier et al. (2014), Fig 6**. https://doi.org/10.1371/journal.pcbi.1003833.g006 | Circle-area and truncated-axis encodings alter perceptions | Never distort a service gap or numerical comparison; label units/scales and reject decorative size coding | 6, 11, 12; results | CC0 |
| 7 | **Jambor & Bornhäuser (2024), Fig 2**. https://doi.org/10.1371/journal.pcbi.1011789.g002 | Consistent pictograms versus inconsistent icon mixtures | Adopt one minimal icon family; prioritize technical labels over pictograms | 3, 9 | Mixed third-party icon licenses noted in caption; do not reuse those assets |
| 8 | **Fujii (2026), Fig 1**. https://doi.org/10.1038/s41562-026-02466-9 | Match intended message and audience to chart/design form | Select figure based on description/difference/association and oral-audience context | planning across all slides | Publisher rights; view for principle, do not save/redistribute figure |
| 9 | **Wong (2011), figure examples**. https://doi.org/10.1038/nmeth.1618 and https://doi.org/10.1038/nmeth.1642 | Redundancy beyond hue and limits of color-only encoding | Always combine color with words/shape/line distinctions | all figures | Publisher rights; principles only |
| 10 | **BioRender's Figure Guidelines & Checklist**. https://www.biorender.com/template/figure-guidelines-checklist | Practical before/after checks of flow, alignment, spacing and legibility | Use QA questions; do not borrow icons/layout templates or assume design guide proves science | final QA | Proprietary design examples; principles only |

**Original articles:**
- Jambor, H. K., & Bornhäuser, M. (2024). *Ten simple rules for designing graphical abstracts*. PLOS Computational Biology, 20(2), e1011789. https://doi.org/10.1371/journal.pcbi.1011789
- Rougier, N. P., Droettboom, M., & Bourne, P. E. (2014). *Ten Simple Rules for Better Figures*. PLOS Computational Biology, 10(9), e1003833. https://doi.org/10.1371/journal.pcbi.1003833
- Kosslyn, S. M., Kievit, R. A., Russell, A. G., & Shephard, J. M. (2012). *PowerPoint Presentation Flaws and Failures: A Psychological Analysis*. Frontiers in Psychology, 3, 230. https://doi.org/10.3389/fpsyg.2012.00230

**Not scientific evidence for this thesis:** These figures establish communication precedents, NOT transformer limits, charger derating, thermal causality, physics equations, novelty, or quantitative resilience. Domain evidence must be independently sourced and cited adjacent to every factual scientific claim.

### Access and reuse policy

- PLOS Rougier et al. work is expressly CC0; author-created Fig 1 drawings in Jambor & Bornhäuser are reported CC0 in its caption. The Jambor & Bornhäuser article is CC BY 4.0, and Fig 2 credits third-party icons of mixed licenses. Check each individual figure/asset license before redistributing.
- Nature and commercial BioRender figures may be *viewed as examples* and linked but not automatically copied into the repository, redrawn, or embedded into a deliverable.
- Use original, newly authored editable shapes for actual thesis slide production, and visibly cite the **scientific domain evidence** for claims plus the design source only when discussing design principles.
