# Framework Visual Fidelity Protocol — v2.0

![Framework](https://img.shields.io/badge/stages%201--7-v2.1%20ALIGNED-1A7F37)
![RQ/SO/H](https://img.shields.io/badge/research%20contract-v4.0-0969DA)
![Protocol](https://img.shields.io/badge/figure%20QA-MANDATORY-8250DF)

**Status:** ACTIVE VISUAL-QA PROTOCOL  
**Effective date:** 2026-09-21  
**Supersedes for active thesis figures:** \`FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md\`  
**Framework authority:** \`../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md\`  
**Semantic alignment authority:** \`../project/CANONICAL_7_STAGE_FRAMEWORK_V2_1_ALIGNMENT_AMENDMENT.md\`  
**RQ authority:** \`../project/CANONICAL_RESEARCH_QUESTIONS_V4.md\`  
**SO/H authority:** \`../project/CANONICAL_RQ_SO_HYPOTHESES_V4.md\`  
**Mathematical synthesis support:** \`../project/PHYSICS_MATHEMATICS_ENGINEERING_SYNTHESIS_V1.md\`

> **Governing rule:** improve visual hierarchy without altering scientific meaning, stage identity, evidence status, uncertainty semantics, or the research contract.

---

## 1. Scientific hierarchy

A full-framework figure must distinguish six different roles:

1. **Input:** critical electricity and mobility service requirements;
2. **Scientific spine:** the seven canonical stages;
3. **Cross-cutting controls:** evidence qualification, identification, parameter provenance, VVUQ, sensitivity, falsification, reproducibility, and claim/validity ceilings;
4. **Research contract:** RQ0, RQ1–RQ7, SO1–SO7, H1–H5;
5. **Execution realizations:** gate-controlled cases, datasets, demonstrators, and experiments;
6. **Foundational reasoning:** systems thinking and systems engineering.

These roles may not be drawn as if they were additional framework stages.

---

## 2. Canonical seven-stage identity

| Stage | Canonical name | Scientific responsibility |
|---:|---|---|
| **1** | **Spatiotemporal System-of-Systems Structure** | define the bounded P–T SoS, services, entities, states, locations, temporal characteristics, and candidate interfaces |
| **2** | **Evidence-Qualified Spatiotemporal Directional Dependencies** | qualify direction, mechanism, activation, space/time support, delay, timescale, uncertainty, evidence, and validity |
| **3** | **Complex Spatiotemporal Coupled Dynamics** | determine how dynamically ready mechanisms evolve, interact, propagate, and alter physical/service trajectories |
| **4** | **Spatiotemporal Observation, Estimation, Organization, and Feasible Control** | determine what can be observed/estimated and what can actually be executed |
| **5** | **Uncertainty-Aware Spatiotemporal Service Resilience** | determine maintainability and recoverability of required services under feasible actions and qualified uncertainty |
| **6** | **Spatiotemporally Targeted Engineering Intervention Consequences** | compare resilience effects, resource requirements/efficiency, admitted sustainability consequences, feasibility, and uncertainty |
| **7** | **Defensible Spatiotemporal Engineering Decision** | determine the defensible decision set without assuming universal optimality |

The order is immutable unless the canonical framework itself is formally amended.

---

## 3. Stage-2→3 identification handoff

Parameter identification is a cross-stage handoff, **not Stage 2.5** and not an eighth stage.

A full framework figure may show:

\[
\boxed{
\mathcal I^{qualified}
\rightarrow
\Theta_{\rm id}
\rightarrow
\mathcal I^{ready}
\rightarrow
F_q
}
\]

or, in words:

\[
\boxed{
\text{qualified mechanism}
\rightarrow
\text{identifiable parameterization}
\rightarrow
\text{estimated/qualified parameters}
\rightarrow
\text{dynamic readiness}.
}
\]

Required firewall:

\[
\boxed{
\text{mechanism existence}
\neq
\text{parameter identifiability}
\neq
\text{adequate parameter estimation}.
}
\]

---

## 4. Canonical scientific chain

When the full thesis spine is shown, use:

\[
\boxed{
\begin{aligned}
&\text{Critical electricity and mobility services}\\
&\downarrow\\
&\text{Spatiotemporal P--T System-of-Systems structure}\\
&\downarrow\\
&\text{Evidence-qualified directional dependencies}\\
&\downarrow\\
&\text{Identification / parameter-readiness handoff}\\
&\downarrow\\
&\text{Complex spatiotemporal coupled dynamics}\\
&\downarrow\\
&\text{Observation, estimation, organization, feasible control}\\
&\downarrow\\
&\text{Uncertainty-aware service resilience}\\
&\downarrow\\
&\text{Targeted intervention consequences}\\
&\downarrow\\
&\text{Defensible engineering decision}.
\end{aligned}
}
\]

The identification line is a handoff/control layer and does not alter the seven-stage count.

---

## 5. Non-negotiable scientific distinctions

A full figure must preserve:

\[
\boxed{
\mathcal S_{PT}
\neq
\mathfrak G_{PT}(x,t)
\neq
F_q[Y(x,t)].
}
\]

Interpretation:

- \(\mathcal S_{PT}\): System-of-Systems architecture;
- \(\mathfrak G_{PT}(x,t)\): spatiotemporal structure;
- \(F_q[Y(x,t)]\): complex spatiotemporal behavior/dynamics.

Also preserve:

\[
\text{co-location}\neq\text{dependency},
\qquad
\text{association}\neq\text{causality},
\qquad
P\rightarrow T\not\Rightarrow T\rightarrow P.
\]

Stage 1 remains structural and non-causal.

---

## 6. Stage-3 behavior versus representation

The behavior being studied is **complex spatiotemporal coupled dynamics**. A physics-based hybrid multiscale model is the principal mathematical representation used to study that behavior.

A full figure may show:

\[
\boxed{
\frac{\partial Y(x,t)}{\partial t}
=
F_q
\left(
Y(x,t),
u(x,t),
\eta(x,t);
\theta,
\mathcal I^{ready}(x,t)
\right)
}
\]

with hybrid reset

\[
Y^+=J_{q\rightarrow q'}(\cdot)
\]

where justified.

Do not rename Stage 3 itself as merely “hybrid multiscale dynamics.”

---

## 7. Stage-4 chain

Use the canonical knowledge/action chain:

\[
\boxed{
Y(x,t)
\rightarrow
y(x,t)
\rightarrow
\widehat Y(x,t)
\rightarrow
(I,O)
\rightarrow
\mathcal U_{\rm feas}(x,t)
\rightarrow
u(x,t).
}
\]

Required distinctions:

\[
Y\neq y\neq\widehat Y,
\qquad
\text{physical possibility}\neq\text{operational feasibility}.
\]

Operational control \(u(x,t)\) remains distinct from persistent engineering intervention \(a_k\).

---

## 8. Stage-5 uncertainty semantics

The current canonical resilience composition is:

\[
\boxed{
\text{Resilience}
=
\underbrace{\text{Remain}}_{\text{viability}}
+
\underbrace{\text{Return}}_{\text{reachability}}
+
\underbrace{\text{Uncertainty qualification}}_{\Gamma_U}.
}
\]

The plus signs denote conceptual composition, not arithmetic addition.

Probability is conditional:

\[
\boxed{
\Gamma_U=
\begin{cases}
\text{probabilistic qualification}, & \text{if a probability model is defensible},\\
\text{scenario / interval / robust / sensitivity qualification}, & \text{otherwise}.
\end{cases}
}
\]

Therefore a canonical figure must **not** state “Probability = confidence layer” as a universal rule.

Preferred top-level Stage-5 objects:

\[
\boxed{
K_{\rm sus},\qquad
\mathcal V,\qquad
\mathcal R,\qquad
\Gamma_U.
}
\]

---

## 9. Stage-6 consequence typing

The typed consequence object is:

\[
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right).
}
\]

A figure must preserve:

\[
\boxed{
\text{resilience effect}
\neq
\text{effectiveness}
\neq
\text{resource requirement}
\neq
\text{resource efficiency}
\neq
\text{admitted sustainability consequence}.
}
\]

Core resources are bounded to qualified direct cost and operational energy:

\[
\mathbf r_{\rm core}\subseteq(C_{\rm direct},E_{\rm op}).
\]

The principal admitted environmental sustainability consequence is:

\[
\mathbf J_{\rm sus,core}\subseteq(CO_{2e}).
\]

Accessibility/equity remains conditional on separate qualification and must not be drawn as automatically admitted.

---

## 10. Stage-7 decision semantics

Use:

\[
\boxed{
\text{feasibility}
\rightarrow
\text{native-unit criteria}
\rightarrow
\text{Pareto/dominance}
\rightarrow
\text{robustness/regret}
\rightarrow
\text{preference/value model if justified}.
}
\]

Primary H5 compares:

\[
\boxed{
\mathcal A_R^\star
\quad\text{vs}\quad
\mathcal A_{\rm joint}^\star.
}
\]

Required guardrail:

\[
\boxed{
\text{defensible}\neq\text{universally optimal}.
}
\]

Adaptive/sequential pathways are a **conditional extension**, not the primary Stage-7 identity.

---

## 11. RQ/SO/H traceability

A full figure must not imply seven one-to-one hypotheses.

Use:

\[
\boxed{
RQ_1/SO_1 + RQ_2/SO_2
\rightarrow
\text{structural/dependency prerequisites}
}
\]

and:

\[
\boxed{
RQ_3/SO_3\rightarrow H_1,\quad
RQ_4/SO_4\rightarrow H_2,\quad
RQ_5/SO_5\rightarrow H_3,\quad
RQ_6/SO_6\rightarrow H_4,\quad
RQ_7/SO_7\rightarrow H_5.
}
\]

H1 primary comparison:

\[
M_2\text{ vs }M_1,
\qquad
M_0\text{ reference}.
\]

H2 is a matched information/organization contrast; a specific \(P+T\), \(P+T+I\), \(P+T+I+O\) implementation is subordinate to that meaning.

H3 tests incremental information from viability/reachability beyond conventional service/recovery measures.

H4 tests intervention-consequence heterogeneity.

H5 tests whether joint evaluation changes the defensible/nondominated decision set, dominance relations, or regret relative to resilience-only evaluation.

All H1–H5 remain **NOT TESTED** until their confirmatory prerequisites are satisfied.

---

## 12. Execution-realization guardrails

Cases, datasets, and demonstrators are not framework stages or theory authorities.

As of 2026-09-21:

- Austin \`AUS-P5U-2018-V1\`: active case candidate, **NOT YET ADMISSIBLE**;
- Houston H3 demonstrator: architecture frozen, confirmatory execution **BLOCKED**;
- NYC/ACN H1 public architecture: partial-pass/component-validation roles only.

A full theory figure should either omit case details or place them in a clearly subordinate “gate-controlled execution realizations” branch.

---

## 13. Evidence-state display

| Label | Meaning |
|---|---|
| \`[E]\` | established external evidence/theory |
| \`[D]\` | thesis-derived synthesis/adaptation |
| \`[P]\` | proposed construct/method requiring validation |
| \`[A]\` | declared assumption |
| \`[U]\` | unresolved/open item |
| \`[R]\` | empirical/computational result |

A frozen thesis object does not become external theory merely because it is canonical internally.

---

## 14. Semantic colors

| Scientific role | Preferred color | Hex | Redundant cue |
|---|---|---:|---|
| Power \(P\) | Navy | \`#0B1F3A\` | P label / power geometry |
| Transportation \(T\) | Teal | \`#0F766E\` | T label / route geometry |
| Information \(I\) | Blue | \`#2563EB\` | I label / dashed line |
| Organization \(O\) | Amber | \`#D97706\` | O label / dotted line |
| Viability / acceptable service | Green | \`#15803D\` | set/boundary label |
| Hazard / violated constraint | Red | \`#B91C1C\` | warning/boundary cue |
| Derived synthesis / handoff | Purple | \`#7E22CE\` | [D]/handoff label |
| Conditional / unresolved | Gray | \`#6B7280\` | text status |

Color is never the sole carrier of meaning.

---

## 15. Line semantics

| Line style | Meaning |
|---|---|
| Solid | physical/operational/scientific dependency |
| Dashed | sensing, information, or cross-cutting support |
| Dotted | organizational/decision/coordination relation |
| Double/emphasized | closed-loop feedback when needed |
| Red boundary | hazard or violated constraint only |

No unlabeled decorative arrows.

---

## 16. Production and typography

For repository architecture maps, Mermaid is acceptable. For thesis-ready publication figures, prefer deterministic vector production: TikZ/LaTeX, SVG, draw.io, or Figma.

Where supported, use **Times New Roman** for the manuscript-facing version. Mathematical notation must remain native/vector, not raster screenshots.

A final figure must have:

- no paragraph-length node text;
- no unexplained acronym at first meaningful use;
- no equation wider than the intended frame;
- exact canonical symbols;
- explicit uncertainty semantics;
- explicit evidence/conditional status where needed;
- a caption stating conceptual/synthetic/simulated/empirical status.

---

## 17. Mandatory metadata

Every thesis-ready full-framework figure records:

| Field | Requirement |
|---|---|
| Figure ID | stable identifier |
| Framework authority | file path + commit/SHA where practical |
| RQ/SO/H authority | current v4 files |
| Semantic amendment | v2.1 alignment |
| Mathematical support | relevant synthesis/specification |
| Evidence state | [E]/[D]/[P]/[A]/[U]/[R] |
| Data status | conceptual/synthetic/simulated/calibrated/empirical |
| Execution snapshot | if cases are shown |
| Verification | semantic + render QA |
| Limitation | main interpretation boundary |

---

## 18. Figure statuses

| Status | Meaning |
|---|---|
| \`CANONICAL-VERIFIED\` | current authorities synchronized and semantic + render QA passed |
| \`DRAFT-UNVERIFIED\` | content or render QA still open |
| \`ILLUSTRATIVE-NONCANONICAL\` | intentionally simplified/additive visual |
| \`SUPERSEDED\` | replaced by a later figure |

A derived figure may be \`CANONICAL-VERIFIED\` for fidelity while remaining non-authoritative relative to its canonical source files.

---

## 19. Mandatory audit gate

\[
\boxed{
G_{\rm fig}
=
G_{\rm authority}
\land
G_{\rm stages}
\land
G_{\rm notation}
\land
G_{\rm uncertainty}
\land
G_{\rm consequence}
\land
G_{\rm traceability}
\land
G_{\rm execution}
\land
G_{\rm render}.
}
\]

Audit template:

\`\`\`text
Figure file:
Audit date:
Framework authority:
RQ/SO/H authority:
Stage identity: PASS / FAIL
Stage order: PASS / FAIL
Architecture/behavior distinction: PASS / FAIL
Stage-2 causal firewall: PASS / FAIL
Identification handoff: PASS / FAIL
Stage-5 uncertainty semantics: PASS / FAIL
Stage-6 consequence typing: PASS / FAIL
Stage-7 decision semantics: PASS / FAIL
RQ/SO/H traceability: PASS / FAIL
Execution/case status: PASS / FAIL / N/A
Notation: PASS / FAIL
Color/line semantics: PASS / FAIL / N/A
No silent additions: PASS / FAIL
Render QA: PASS / OPEN / FAIL
Overall status:
Notes:
\`\`\`
