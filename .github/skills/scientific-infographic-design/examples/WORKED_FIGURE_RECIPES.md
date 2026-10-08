# Worked Scientific Figure Recipes — From Research Claim to Diagram and Code

**Status:** Worked illustration specifications, not new scientific findings.  
**Controlling sources:** \`AI_RESEARCH_INSTRUCTIONS.md\`, current authority index, \`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md\`, \`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md\`, \`thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md\`.

**Important:** All diagram arrows have independent \`scientific meaning\` and \`evidence status\`. A proposed mechanism is not made established by drawing a solid arrow.

## Recipe A — Slide 3: complete system architecture

**Question:** Which technical elements belong to P and the *full* T_e, and what is the actual cross-system exchange?  
**Figure type:** two nonoverlapping system boundaries with labeled cross-boundary transfers/effects.  
**Message:** P and T_e are separate physical systems; electrical exchange/charging load do not prove a thermal interdependency.

**Element register**

| Object | Semantic type | System | Required meaning |
|---|---|---|---|
| P | physical system boundary | P | relevant electricity supply/network/transformer |
| T_e | physical system boundary | T_e | road vehicle + RESS + propulsion + auxiliaries + vehicle supply circuit + EVSE + physical charging interface + required communication/control; bidirectional transfer where supported |
| charging-energy supply | electrical transfer | P→T_e | actual electricity supplied to T_e when in the selected operating mode |
| charging load | electrical loading influence | T_e→P | behavior of the electrical load presented to P; not necessarily exported electric power |
| mobility service | outcome, outside technical composition | service | service metric must be separately defined |

**Arrow register**

| Source → target | Arrow meaning | Evidence status | Citations |
|---|---|---|---|
| P→T_e | electrical energy supply under selected operating conditions | established general interface; operating case OPEN | internal canonical scope; ISO 15118 family where verified |
| T_e→P | charging-demand/loading influence, not V2G export | general prior art, case-specific temperature behavior OPEN | Qian et al. (2015); Diahovchenko et al. (2023) |
| P↔T_e *thermal* | do **not draw** on Slide 3 | not independently qualified | canonical thermal scope |

**Design:** 16:9 white; P border blue, T_e border green, black text; **two independently directed and labeled arrows**, no third EVSE boundary, no spurious heat arrow.  
**Caption:** "System membership and electricity/charging-load interactions. A thermal interdependency is not inferred from connection alone (Qian et al., 2015; Canonical Electrified Transportation Scope V1)."  
**Failure test:** reduce T_e to EVSE only ⇒ FAIL. Label T_e→P as "V2G" without a supported bidirectional operating mode ⇒ FAIL.

## Recipe B — Slide 4: parallel heat exposure (a controlled counterexample)

**Question:** How can heat influence both systems without creating an interdependency?  
**Figure type:** external forcing above two **independent parallel** state→capability lanes.

**Objects:** outside forcing H; P thermal state; P thermally conditioned capability; T_e thermal state; T_e thermally conditioned capability.  
**Connections:** \`H→P_state\`, \`P_state→P_capability\`; separately \`H→Te_state\`, \`Te_state→Te_capability\`. **No P→T_e or T_e→P thermal arrow.**

**Why:** shared exogenous input can be associated with two responses without establishing a between-system causal dependence.

**Source precision:** transformer thermal loading guidance (IEEE C57.91-2025, edition verification required for clauses), and an **equipment-specific** charger thermal response (Krama et al., 2026). Do not apply that field result to every EVSE chemistry or design.

**Caption:** "Conceptual parallel heat-response paths; NOT a demonstrated interdependency. Thermally conditioned Power operation: IEEE C57.91-2025. Case-specific EVSE response: Krama et al. (2026)."  
**Test:** any cross arrow appears ⇒ FAIL, unless separately sourced and status-labeled (and then Slide 4 no longer serves its intended question).

## Recipe C — Slide 5: two candidate thermal-interdependency directions

**Question:** What exact evidence would qualify a directional heat-conditioned cross-system effect?  
**Figure type:** two horizontal mechanism lanes, one per direction; each lane ends in an explicit evidence gate.

**Candidate P→T_e:** \`P thermal state\` → \`P heat-conditioned operating limit\` → \`actually enforced electrical supply limit at interface\` → \`observed/derived T_e charging effect\` → \`service consequence relative to requirement\`.

**Candidate T_e→P:** \`T_e device thermal state\` → \`EVSE delivered-power constraint\` → **verify AC input electrical behavior** → \`P loading behavior\` → \`P thermal-state response\` → \`electricity-service implication, if measured/defined\`.

Each arrow has one separate real-world mechanism that requires proof. **A measured drop in EVSE DC output does not uniquely determine grid-side AC real/reactive/harmonic quantities** without evidence. A T_e→P path cannot simply skip this interface.

**Gate fields:** literature mechanism evidence; source equipment identification; operating limits and controls; time-aligned temperatures; AC-side power/current; cross-system transfer quantity; declared electricity/mobility service requirement; uncertainty and validation feasibility.

**Citations:** Qian et al. (2015); Visakh & Selvan (2023); Krama et al. (2026) separately support component-level prior art. **They do not validate both full chains as a combined case.**

**Caption:** "Two candidate, not yet case-qualified, thermal-interdependency pathways. Each link requires independent physical and interface evidence. Component prior art: Qian et al. (2015); Visakh & Selvan (2023); Krama et al. (2026)."  
**Test:** no AC input gate in the T_e→P lane ⇒ FAIL. "Bidirectional thermal feedback VERIFIED" ⇒ FAIL.

## Recipe D — Slide 6: bounded research-gap matrix

**Question:** Which part is already studied, and which precise handoff remains unresolved for our selected application?  
**Figure type:** evidence / ability / applicability / remaining test matrix.

| Source | Supports (carefully worded) | Does not automatically establish | Our bounded next test |
|---|---|---|---|
| Qian et al. (2015) | EV charging cases relevant to transformer thermal aging | all charger equipment thermal behavior under extreme heat | qualify P-side heat-dependent behavior |
| Visakh & Selvan (2023) | EV charging, transformer thermal loading and service disruption | our full P↔T_e extreme-heat bidirectional time propagation | reproduce closest baseline and quantify only incremental claim |
| Krama et al. (2026) | tested fast-charger heat-related behavior | transferability to all chargers or the power transformer thermal state | qualify actual EVSE AC input and case conditions |

**Narrative:** established → study limitation → selected application handoff → what will be tested.  
**Caution:** "no study ever" requires systematic reproducible prior-art audit and must remain OPEN otherwise.

## Recipe E — Slide 9: scope versus model subset

**Question:** Why does a full component definition not imply modeling every thermal/operational variable?  
**Figure type:** full enclosing P boundary and full enclosing T_e boundary; smaller **active model** outlines located within each. External extreme heat drawn outside. Service outcomes drawn downstream, not part of the technical vehicle.

**Hard rules:** EVSE and physical charging connection **inside T_e**. Power system **outside T_e**. Mobility service **not a physical vehicle component**. A charging installation may be a subset but does not redefine the full T_e definition.

**Test:** active-model outline has a geometric area that appears to replace T_e entire enclosure ⇒ FAIL. Using "Boundary condition: EVSE belongs to T_e" ⇒ FAIL.

## Recipe F — Slide 10: evidence-led research workflow

**Question:** What must happen before a model-derived scientific result is admissible?  
**Figure type:** a **method workflow**, not a physical interaction diagram.

\`\`\`text
SOURCE ADMISSION
  ↓
DIRECTIONAL PHYSICAL MECHANISM GATE (qualified?)
  ↓ yes                                    ↘ no / insufficient → OPEN
MINIMUM-SUFFICIENT PHYSICS MODEL
  ↓
NUMERICAL VERIFICATION (implementation?)
  ↓
INDEPENDENT PHYSICAL VALIDATION (if available; distinct from verification)
  ↓
UNCERTAINTY / TRANSFER DOMAIN
  ↓
SERVICE CONSEQUENCE + QUALIFIED ENGINEERING INTERPRETATION
\`\`\`

**Important:** a yes/no decision diamond is procedural; its arrow does not claim physical energy flow. Evidence status and provenance appear at the gate. A test passing numerical verification does **not** imply model validation.

**Method reference:** Oberkampf & Trucano (2002), https://doi.org/10.1016/S0376-0421(02)00005-2.  
**Canonical source:** Evidence and Non-Invention Standard V1.

## Recipe G — Slide 12: services, resilience, sustainability

**Question:** Where does resilience begin, and where do sustainability consequences enter?  
**Figure type:** left service chain plus distinct right assessment branches.

\`\`\`text
EXTERNAL HEAT → PHYSICAL STATE → CAPABILITY → REQUIRED SERVICES
                                                   ├─ SERVICE RESILIENCE:
                                                   │    maintain or recover required
                                                   │    electricity & mobility services
                                                   └─ TWO SUSTAINABILITY PATHWAYS:
                                                        1. thermal interdependency
                                                           → service consequence
                                                           → E / E / S consequence
                                                        2. engineering response
                                                           → state / capability / service change
                                                           → E / E / S consequence
\`\`\`

**Important:** service maintenance/recovery is the thesis-defined resilience criterion; the environmental/economic/social assessment is separately bounded. A resilient response can increase costs or emissions. Do not draw a causal arrow "resilience automatically produces sustainability".

**Internal citations:** Canonical Resilience Definition V1; Canonical Two-Pathway Sustainability Assessment V1.  
**Relevant external literature:** Poulin & Kane (2021), DOI https://doi.org/10.1016/j.ress.2021.107926 for resilience-performance curve context; this is **not** authorship of the thesis-specific definition.

## Recipe H — Mathematically rigorous *program-generated* event/timing figure

**Question:** How can a defensible event-time and propagation-delay figure be computed from a declared state-time dataset?

**Candidate definitions**, **not a frozen physical model**:

\[
\tau_i=\inf\{t\in[t_0,t_1]:g_i(X_i(t),t)\le0\},\qquad
\delta_{i\to j}=\tau_j-\tau_i .
\]

**Required inputs:** strictly increasing numerical time with declared units, state arrays with units, a component-specific **justified** event function/threshold, a documented interpolation scheme, event-pair definition, uncertainty/time resolution, and supported directional mechanism.

**Software unit test only:** \`time = [0.0, 1.0, 2.0]\`, **dimensionless** state sequence \`[0.9, 0.7, 0.4]\` and hypothetical test threshold \`0.5\`. A linear-interpolation crossing is a mathematical test, not a real transformer thermal event. Do NOT place this as a measured curve on Chapter 1 slides.

**Code** \`examples/mathematical_metrics.py\` computes this case and checks multiple edge conditions. Render a schematic event-time diagram only when the relationship is permitted and label \`SYNTHETIC / NOT VALIDATED\`.

## Recipe I — Exact design prompt and renderer code responsibilities

The prompt/scene builder must specify:
1. **Objects** with IDs, type, owner and exact labels;
2. **Edges** with typed meaning, evidence status, source and destination;
3. **Geometry** 16:9, original vector components, declared scale;
4. **Citation** source in the claim/figure, internal authority distinguished;
5. **Hard exclusions** no fake heat coupling, no third EVSE system, no unverified numerical data;
6. **QA** tests and rendered inspection;
7. **Deliverables** editable PPTX and/or original SVG plus scripts and source notes.

**Wrong prompt:** "Make an advanced futuristic resilience diagram with many arrows, glowing energy, and a heat catastrophe."

**Correct prompt:** "Draw two distinct, entirely white Power P and full Electrified Transportation T_e enclosures on a pure-white 16:9 slide. Put external heat above both and show exactly two independently labeled forcing→thermal-state→capability lanes. No thermal link between them. Use black text, blue and green borders, dark-red heat arrows, no gradients, cite the transformer and specific EVSE thermal sources, state CONCEPTUAL—not measured."

## Testing and minimum deliverable record

- Arrow registry and component membership passes semantic tests.
- No source-dependent proposition lacks an adjacent citation.
- No arbitrary position, color intensity or box size purports to be a measured quantity.
- Vector output parses as SVG/XML; PPTX is a valid zip and contains expected editable shapes if produced.
- A rendered preview is visually inspected for white interiors, unclipped labels and correct arrowheads.
- Store the figure source, design brief, software version, QA results and limitations.

**References (domain):** Qian et al. (2015), Visakh & Selvan (2023), Diahovchenko et al. (2023), Krama et al. (2026), Oberkampf & Trucano (2002), as precisely identified in the thesis literature register.  
**References (design):** Jambor & Bornhäuser (2024), Rougier et al. (2014), Jambor (2025). These are *visual design evidence*, not support for physical mechanism claims.
