# Scientific Design, Research and Agent Algorithms — Implementation Specification V1

**Status:** supplemental implementation protocol; **not a canonical thesis amendment**, not autonomous-agent deployment, not empirical model validation.
**Source:** user-provided unified technical specification (13 October 2026); this file is an executable-oriented adaptation of the conversation specification, **not** a claim that an unavailable separate 4,166-word document was imported verbatim.
**Authority:** \`AI_RESEARCH_INSTRUCTIONS.md\`; \`project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md\`; \`project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md\`; active thesis title, thermal scope, objectives, state-time definitions, and presentation-variant router.

## 1 — Fundamental scientific separation

\`Evidence → Physical Model → Mathematical Representation → Scientific Diagram → Optional Animation → Independent Verification\`

**Physical mathematics** describes energy, AC ports, heat and admitted state-time dynamics. **Design mathematics** places scientifically admitted objects and typed relationships without distorting topology. **Animation mathematics** maps physical model time or presenter reveal time to render frames. Neither visual attractiveness nor a numerically solved equation establishes experimental validity.

### Proposed model schema — not yet identified or validated

\`\`\`math
\begin{aligned}
\dot{x}(t)&=f_m(x,z,u,H;\theta),\\
0&=g_m(x,z,u,H;\theta),\\
y(t_k)&=h(x(t_k),z(t_k);\theta)+\varepsilon_k.
\end{aligned}
\`\`\`

- \`x\`: admitted evolving states, chiefly temperatures; distinguish SOC energy state, slow degradation and service outputs.
- \`z\`: algebraic AC or operating quantities, **not an independent dynamic state by default**.
- \`u\`: verified installed/external controls if admitted.
- \`H\`: ambient heat forcing, *not cross-system heat flow*.
- \`\theta\`: evidence-supported model parameters and validity ranges.
- \`m\`: operating modes **only when documented**.
- \`y(t_k)\`: actual observations if available, with disclosed measurement errors and timestamp provenance.

For the frozen thesis focus, only qualified extreme-heat thermal interdependencies \`Power ↔ Electrified Transportation\` are active. The schema does **not** automatically admit all physical devices or non-thermal relationships.

### Boundary-dependent conservation examples

- AC complex power: \`S = Σ_phase V_phase I_phase* = P + jQ\` for consistently defined RMS phasors and sign convention. **P, Q, V, I are quantities of a port, not four separate power-flow arrows.**
- Resistive copper dissipation: \`P_loss = Σ_line,phase |I|² R\`, with valid conductor/resistance operating conditions.
- Conditional steady charger balance: \`P_AC ≈ P_DC + P_loss + P_aux\` when storage/transient boundary terms are negligible and defined measurements share a control-volume boundary.
- Lumped thermal storage: \`C_th dT/dt = Qdot_gen − Qdot_out\`, conditional on a justified lumped thermal state and heat-transfer parameters.
- Battery SOC example: \`d(SOC)/dt = η_ch I_charge/Q_usable\` for a consistent signed current, capacity and units; SOC is an **energy**, not thermal, state.
- Protection transition: \`m(t+) = R_installed(...)\` only where the real monitored inputs and installed rules are documented.

These equations are **generic illustrative relations**. Their use with specific P1/P4/T1/T3 equipment requires case-appropriate sources, assumptions and verification; no default transformer trip, battery derating threshold or ambient-to-AC-demand law.

## 2 — Typed scientific graph and edges

Define \`G=(V,E)\`. A node represents an identified equipment component, physical port, state, input, observation or service output. An edge must contain its \`source\`, \`target\`, \`type\`, \`evidence_status\`, \`label\`, and independent provenance where it makes any data/source-supported assertion. Subsystem membership and ports must be explicit.

Minimum supported training pathway is:

\`\`\`text
POWER SYSTEM                       ELECTRIFIED TRANSPORTATION SYSTEM
P1 (transformer) → P2 (AC feeder) → T1 (AC-to-DC charger) → T2 (EV battery)
                      [AC port]                         [DC charging]
\`\`\`

Cooling subsystem P4 is within/attached to P1; EVSE cooling T3 within T1. P3 monitoring/control is separate from AC energy transfer and cannot be shown as an *established* temperature trip without installed logic. T4 is a vehicle auxiliary energy load, **not** an independent distribution feeder load.

Preserve the Deck3 typed relationship grammar: AC/DC electrical transfer; heat transfer; controls; observations; proposed causal links; external forcing; process sequence. **Common extreme-heat exposure** can act on P1 and T1 separately but does not demonstrate a directed P↔T thermal interdependency.

Hypotheses **I2/H1 (T_e→P)** and **I3/H2 (P→T_e)** remain separately qualified, explicitly labeled **candidate / not yet qualified** until evidence gates pass. A diagram arrow alone does not upgrade them.

## 3 — Design mathematics — hard physics constraints first

Select diagram grammar and construct \`L\`, a layout of scientific objects and connectors. A possible optimization objective is:

\`\`\`math
\min_{L}\;w_1 N_{\rm overlap} +w_2N_{\rm crossing} +w_3L_{\rm connection}
+w_4D_{\rm alignment}+w_5D_{\rm balance}.
\`\`\`

All weights are **user/design configuration**, not physical constants. Scientific constraints are *hard* and cannot be exchanged for reduced line crossings: directed topology, equipment/port boundaries, typed arrow meanings, published/conditional labels, unit semantics, and readable source provenance.

Keep 16:9 white canvas, white interiors, no gradients/shadows, Times New Roman and exact 13 governed authored colors from \`.github/skills/deck3/references/DECK3_SRGB_PALETTE.json\`. ASU Gold \`#FFC627\` is limited to small institutional accents; natural and authentic equipment photography may retain real colors. Layout geometry must not imply false thermal or electrical transmission.

## 4 — Animation mathematics — different clocks

Let \`s=k/f_fps\` denote **presentation** time and \`t=\psi(s)\` denote **physical** model time. For valid physical trajectories:

\`\`\`math
F_k = \mathcal{R}(G,x(\psi(k/f_{\rm fps})),\mathcal{S})
\`\`\`

where \`\mathcal R\` is a renderer and \`\mathcal S\` is the governed appearance. A physical-time animation requires an explicitly admitted equation, dimensional units, initial and boundary conditions, parameter sources, integration/observation timestep, solver tolerances, model scope, uncertainty and *declared validation status*. Model computation **≠ experimental validation**.

A presenter-time reveal has no physical state \`x(t)\` and must declare \`clock=PRESENTATION_TIME\` and \`physical_time_claim=false\`. Its six or eight seconds cannot be represented as electricity propagation, heat-transfer delay or charging duration. A figure may mix these clocks only with independently labeled viewports and evidence.

## 5 — Agent responsibilities and admission handoffs

The existing \`scripts/thermal_research_agent.py\` implements a JSON **policy router**, not autonomous specialized model workers. Its A0–A8 assignments remain unchanged; this specification adds a *declared data contract*, not AI execution or authorization.

| Existing role | Input/output interface responsibility |
|---|---|
| A0 Authority | Resolve frozen title, thermal-only scope, objectives, slide variant, admissible states and restricted operations |
| A1 Literature | Primary equation provenance, document version, validity/units, exact vs reconstructed status |
| A2 Physics | Equipment/port and control-volume boundaries; typed directed mechanisms; co-exposure vs causality |
| A3 Mathematics | Governing dynamics, identifiability, numerical verification, tolerances and uncertainty |
| A4 Critique | Challenge rival mechanisms, transferability and overclaimed evidence |
| A5 Verification | Run validators, physics/units checks and numerical/visual/animation tests; report NOT_RUN truthfully |
| A6 Evidence | Maintain source → claim → equation → figure provenance register |
| A7 Deck3/Design | Produce editable SVG/PPTX/animations *only after* admission; retain all evidence qualifiers |
| A8 Release | Enforce non-compensatory gate results and human approval for scientific promotion/external release |

**Important:** The existing research agent defines its own **G0–G8 research claim gates**; Deck3 visual/animation QA separately defines **G0–G7**. These different gate names must carry explicit namespaces, not be combined or mistaken for equivalent certification.

## 6 — Implemented structural prototype (scope and limits)

- \`scripts/figure_contract_example.json\` — example ordinary-charging topology with separate ambient-forcing arrows.
- \`scripts/validate_figure_contract.py\` — standard-library-only fail-closed structural admission checker.
- \`scripts/test_figure_contract.py\` — 14 Python regression cases, including rejection of false I2 promotion, wrong AC arrow direction, invalid color, misleading presenter clock and absent source provenance.

Run from repository root:

\`\`\`bash
python scripts/validate_figure_contract.py scripts/figure_contract_example.json
python -m unittest discover -s scripts -p 'test_figure_contract.py' -v
\`\`\`

Acceptance is strictly \`STRUCTURE_ACCEPTED_NOT_SCIENTIFICALLY_VERIFIED\`. It verifies **declared structural rules only**; the tool does not open actual device sources, check DOI authenticity, inspect image pixels, solve physics, certify PowerPoint editability or test desktop slideshow playback. Its simple topology-specific rules are for the **training charging pathway**, not a universal power-system graph validator. Independent physics, evidence, rendering and human gates remain mandatory.

## 7 — Required quality gates, acceptance and development sequence

Use the animation skill's non-compensatory **G0–G7** checks: authority; science; evidence/rights; simplicity; rendering; native semantics; motion/playback; reproducibility. The research claim router's G0–G8 remains separate.

1. Require the evidence register and a single-message figure contract.
2. Test actual physical boundaries and units; admit only supported equations/edges.
3. Compute trajectories only when physical-time animation is justified.
4. Optimize geometry within hard scientific constraints.
5. Generate original SVG, optional video, and a native editable PPTX companion.
6. Inspect first/middle/final frames, typography, colors, geometry, citations and arrow direction; record unrun checks.
7. Present the scientific/evidence/rights/QA record for independent review; **do not merge or scientifically promote automatically**.

**No claim of full agent autonomy, new empirical findings, licensed manufacturer artwork, or verified I2/I3 physics is created by this implementation.**
