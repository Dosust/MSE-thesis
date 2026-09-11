# Project Memory Entry Point

![Frozen](https://img.shields.io/badge/stages%202--6-FROZEN-1A7F37)
![Research](https://img.shields.io/badge/Stage%207-DEEP%20RESEARCH-9A6700)

## Repository authority — 2026-09-11

The sole active repository for this thesis is `Dossiya-SE/MSE-thesis`.

All active thesis updates, framework revisions, equations, figures, research notes, evidence records, validation artifacts and canonical files must be written to **MSE-thesis** unless explicitly instructed otherwise.

`Dossiya-SE/Optimization-for-sustainability-and-resilience` is historical/reference only.

For project navigation, start with [`project/README.md`](project/README.md).

---

## Citation and reference standard

The thesis-wide citation standard is **APA 7th edition**. A citation must not support a stronger claim than its source establishes. Thesis-proposed mathematical objects remain labeled `[P]` unless evidence justifies a different status.

---

## Current canonical authority

Read the active files in this order:

1. [`project/README.md`](project/README.md)
2. [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md)
3. [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)
4. [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
5. [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)
6. [`project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md)
7. [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)
8. [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)
9. [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)
10. [`project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)
11. [`project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md)
12. [`project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md`](project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md) — research only; not canonical/frozen
13. [`project/MATHEMATICAL_FOUNDATION.md`](project/MATHEMATICAL_FOUNDATION.md)
14. [`project/SCIENTIFIC_PROPOSITIONS.md`](project/SCIENTIFIC_PROPOSITIONS.md)
15. [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md)
16. [`figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`](figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md)

Frozen files override older framework descriptions whenever conflicts occur. The Stage-7 research file is evidence for the next scope decision and does **not** yet override frozen upstream definitions.

---

## Current scientific state

The thesis studies

$$
\mathcal S=\{P,T,I,O\},
$$

where

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

Canonical description:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

Current stage status:

| Stage | Status |
|---|---|
| **1 — Multilayer Structure** | Defined / canonical |
| **2 — Causal Mechanisms** | Frozen |
| **3 — Coupled Hybrid Multiscale Dynamics** | Frozen |
| **4 — Observation, Organization, Feedback and Control** | Frozen |
| **5 — Viability** | Frozen as Controlled Sustainable Viability |
| **6 — Resilience-to-Sustainability Transformation Interface** | **Frozen as Resilience-to-Sustainability Transition** |
| **7 — Sustainable Transformation Pathways** | **Deep research complete; candidate scope not frozen** |

---

## Frozen Stage-2 object

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right).
$$

A retained relation requires

$$
\alpha\xrightarrow{M_{ij}}\beta.
$$

Common exposure alone is not an interdependency.

---

## Frozen Stage-3 object

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix},
\qquad
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
$$

Stage 3 owns heterogeneous native subsystem dynamics, causal delays, multiple timescales, discrete events, mode switching, dynamic topology, trajectory uncertainty, cascade-arrival time and spatial propagation where physically meaningful.

---

## Frozen Stage-4 object

Stage 4 is a closed-loop partially observable socio-technical control process:

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

Core objects include

$$
(\widehat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I),
$$

$$
u(t)=\pi(\widehat X(t),z_I(t),z_O(t)),
\qquad
u(t)\in\mathcal U(z_I(t),z_O(t)).
$$

Measurement noise is $\varepsilon_k(t)$. For sequential non-overlapping processes,

$$
\begin{aligned}
\tau_{\rm response}={}&\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

---

## Frozen Stage-5 object

Stage 5 is formalized as **Controlled Sustainable Viability** under the framework label **Viability**.

$$
K_{\rm sus}(t)=\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\},
$$

$$
\mathcal V_{\rm sus}^{u,T}
=
\{Y_0\in K_{\rm sus}:\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]\}.
$$

The canonical distinction is

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
$$

The temporal quantities are $T_{\mathcal V}$ and $T_K$; the normalized Euclidean/weighted distance $\rho_E$ is the geometric baseline; $\rho_g$, the response margins and $S_{ij}^{\mathcal V}$ remain proposed `[P]` constructs.

---

## Frozen Stage-6 object

Stage 6 is frozen as **Resilience-to-Sustainability Transition** under the framework label **Resilience-to-Sustainability Transformation Interface**.

Frozen research question:

> **When is recovery insufficient, and what conditions require adaptation or transformation?**

The current regime is

$$
\mathfrak M_0
=
(\mathcal S,\mathcal G,\mathfrak I,F,\Theta,K_{\rm sus},\mathcal U).
$$

The Stage-5 evidence interface is

$$
\mathcal R_5
=
\{\mathcal V,\rho,T_{\mathcal V},T_K,S_{\mathcal V},S_K,S_{ij}^{\mathcal V}\}.
$$

The diagnostic vector is

$$
\mathbf d_6
=
[d_{\mathcal V},d_{\rm limit},d_{\rm lock},d_{\rm mal},d_{\rm sus},d_{\rm eq},d_{\rm struct}]^\top.
$$

The frozen Stage-6 translation is

$$
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T),
$$

where

$$
c_6\in\{R,A,T\},
$$

$$
\mathcal D_6
=
\{\mathcal D_P,\mathcal D_T,\mathcal D_I,\mathcal D_O,
\mathcal D_{\mathfrak I},\mathcal D_{\rm env},\mathcal D_{\rm eq}\},
$$

and

$$
\boldsymbol{\zeta}_T
=
[\zeta_{\rm depth},\zeta_{\rm scope},\zeta_{\rm scale},\zeta_{\rm pace},
\zeta_{\rm equity},\zeta_{\rm environment}]^\top.
$$

Stage 6 determines **WHY change, WHAT must change and HOW DEEP the change must be**. It does not select the intervention sequence.

---

## Active Stage-7 research

Stage 7 asks:

> **What sequence of interventions leads to a more resilient, equitable and sustainable future system?**

Its frozen input boundary is

$$
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)
\longrightarrow
\text{Stage-7 intervention/pathway research}.
$$

The ten-pass deep research has tested adaptive pathways, DAPP, multistage decision making, infrastructure investment timing, real options, multi-objective optimization, robust decision making, socio-technical transitions, equity/sustainability constraints and formal P–T–I–O pathway synthesis.

The leading **candidate**, not-yet-frozen interpretation is that

$$
\Pi=[(a_1,t_1),\ldots,(a_N,t_N)]
$$

is useful for one realized pathway, but the fundamental planning object may need to be an adaptive trigger-dependent pathway graph that retains alternative future branches under deep uncertainty.

No Stage-7 candidate equation is canonical until an explicit freeze is approved.

---

## Stage-6 / Stage-7 boundary

$$
\underbrace{\text{WHY / WHAT / HOW DEEP}}_{\text{Stage 6}}
\quad\longrightarrow\quad
\underbrace{\text{WHICH / ORDER / WHEN / UNDER WHAT CONDITIONS}}_{\text{Stage 7}}.
$$

The immediate framework task is to evaluate and refine the Stage-7 candidate scope, then explicitly freeze Stage 7 and only then declare the complete seven-stage conceptual/mathematical framework frozen.

---

## Mathematical rendering rule

Active project files follow [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md): readable GitHub display math, no long prose inside mathematical boxes, no fragile `\tag` dependence, semantic colors only with redundant labels, and tables for taxonomies/specifications.

Historical P–W–T–SW, waste–drainage, earlier six-chain or other superseded architectures remain provenance only unless explicitly reintroduced through a versioned revision.
