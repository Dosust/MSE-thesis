# Canonical Seven-Stage Thesis Framework

![Authority](https://img.shields.io/badge/authority-CANONICAL-0969DA)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Degree](https://img.shields.io/badge/degree-MSE-0969DA)

**Effective date:** 2026-09-09  
**Final framework freeze:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Scope:** Complete conceptual and mathematical thesis framework  
**Change control:** Any scientific revision requires explicit approval, versioning, Git history and re-audit of dependent files/figures.  
**Representation rule:** Visual redesign may change hierarchy, layout, typography, geometry and color; it may not change scientific content.

---

## 1. Frozen sequence

1. **Multilayer Structure**
2. **Causal Mechanisms**
3. **Coupled Hybrid Multiscale Dynamics**
4. **Observation, Organization, Feedback and Control**
5. **Viability**
6. **Resilience-to-Sustainability Transformation Interface**
7. **Sustainable Transformation Pathways**

The sequence is

$$
1\rightarrow2\rightarrow3\rightarrow4\rightarrow5\rightarrow6\rightarrow7.
$$

```mermaid
flowchart LR
    S1["1 · Multilayer Structure"] --> S2["2 · Causal Mechanisms"]
    S2 --> S3["3 · Coupled Hybrid Multiscale Dynamics"]
    S3 --> S4["4 · Observation, Organization, Feedback and Control"]
    S4 --> S5["5 · Viability"]
    S5 --> S6["6 · Resilience-to-Sustainability Transformation Interface"]
    S6 --> S7["7 · Sustainable Transformation Pathways"]

    classDef canonical fill:#DDF4FF,stroke:#0969DA,color:#0B1F33,stroke-width:2px;
    classDef frozen fill:#DAFBE1,stroke:#1A7F37,color:#0B1F33,stroke-width:2px;
    class S1 canonical;
    class S2,S3,S4,S5,S6,S7 frozen;
```

Blue marks the canonical ontology stage; green marks frozen scientific scopes. Text labels remain authoritative if color is unavailable.

---

## 2. Stage responsibilities

| Stage | Main responsibility | Frozen question |
|---|---|---|
| **1 — Multilayer Structure** | define P–T–I–O ontology, states, subsystems and possible interaction locations | **What exists, and where can interaction occur?** |
| **2 — Causal Mechanisms** | define directed cross-layer causal interdependencies | **Why and through what mechanism does one component/layer affect another?** |
| **3 — Coupled Hybrid Multiscale Dynamics** | evolve accepted mechanisms through heterogeneous dynamics, delays, events, modes, topology and timescales | **How, when and where do effects evolve and propagate?** |
| **4 — Observation, Organization, Feedback and Control** | reconstruct system state and map information/organization into feasible operational action | **How is the system observed, interpreted, coordinated and controlled?** |
| **5 — Viability** | evaluate acceptability, maintainability and proximity to loss | **Under what conditions can acceptable functions be maintained, and how far and how long is the system from unacceptable states?** |
| **6 — Resilience-to-Sustainability Transformation Interface** | diagnose current-regime adequacy and specify why/what/how-deep change is required | **When is recovery insufficient, and what conditions require adaptation or transformation?** |
| **7 — Sustainable Transformation Pathways** | determine adaptive, feasible and robust strategic transformation pathways | **What sequence of interventions leads to a more resilient, equitable and sustainable future system?** |

---

## 3. Frozen system ontology

$$
\mathcal S=\{P,T,I,O\},
$$

with

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

The integrated state is

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix},
$$

and the physical state is

$$
X(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix}.
$$

---

## 4. Stage 2 — causal interdependency object

Every accepted directed interdependency is represented by

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right),
$$

where $\alpha,\beta\in\{P,T,I,O\}$ and $\alpha\neq\beta$.

A retained relation requires an explicit causal mechanism:

$$
\alpha\xrightarrow{M_{ij}}\beta.
$$

Common hazard exposure or correlation alone does not establish interdependency.

---

## 5. Stage 3 — hybrid multiscale evolution

The operating mode remains separate from the continuous/discrete system state:

$$
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
$$

Stage 3 owns delayed, hybrid, multirate and topology-dependent evolution through $F_{\mathcal G}^{m}$, including event logic, cascade timing and uncertainty where required.

The temporal discipline is

$$
\text{event time}
\neq
\text{causal delay}
\neq
\text{characteristic timescale}.
$$

---

## 6. Stage 4 — observation, organization and operational control

The feedback spine is

$$
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow\widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
$$

Feasible control is constrained by the informational and organizational states:

$$
u(t)=\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

Here $u(t)$ is operational control. It is not the Stage-7 strategic transformation action.

---

## 7. Stage 5 — controlled sustainable viability

The acceptability set is distinct from the controlled viable set:

$$
K_{\rm sus}
\supseteq
\mathcal V_{\rm sus}^{u,T}.
$$

The central implication is

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
$$

Stage-5 outputs include

$$
\partial\mathcal V,
\qquad
\rho,
\qquad
T_{\mathcal V},
\qquad
T_K,
\qquad
S_{ij}^{\mathcal V},
$$

with proposed quantities retaining `[P]` status until validated.

---

## 8. Stage 6 — regime-adequacy translation

Stage 6 receives validated Stage-5 evidence and long-horizon requirements through

$$
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol\zeta_T).
$$

It answers

$$
\text{WHY change}
+
\text{WHAT must change}
+
\text{HOW DEEP}.
$$

Its output is

$$
(c_6,\mathcal D_6,\boldsymbol\zeta_T),
$$

not an intervention sequence.

---

## 9. Stage 7 — strategic transformation of regimes

Stage 7 changes the regime itself. The frozen regime object is

$$
\mathfrak M_k
=
\left(
\mathcal S_k,
\mathcal G_k,
\mathfrak I_k,
F_k,
\Theta_k,
K_{{\rm sus},k},
\mathcal U_k
\right).
$$

Operational and strategic actions are distinct:

$$
\underbrace{u(t)}_{\text{operate current regime}}
\neq
\underbrace{\mathbf a_k}_{\text{transform regime}}.
$$

The strategic action vector is

$$
\mathbf a_k
=
\begin{bmatrix}
a_k^P\\a_k^T\\a_k^I\\a_k^O\\a_k^{\mathfrak I}
\end{bmatrix},
$$

and the regime transition is

$$
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k).
$$

The adaptive transformation policy is denoted $\boldsymbol\pi_{\rm ST}$, with step policy $\pi_k^{\rm ST}$.

---

## 10. Stage-7 graph of alternative regimes

The transformation meta-graph is

$$
\mathbb G_{\rm ST}
=
(\mathbb V_{\rm ST},\mathbb E_{\rm ST}),
$$

where

$$
v_k\equiv\mathfrak M_k
$$

and each edge represents an admissible strategic transformation.

A monitored trigger region $\mathcal Z_j$ produces trigger time

$$
\tau_j
=
\inf\{t\ge t_k:s_j(t)\in\mathcal Z_j\}.
$$

The feasible action set includes technical, budget, informational, organizational, sustainability, equity and temporal constraints.

---

## 11. Frozen Stage-7 object

The terminal framework object is

$$
\mathfrak P_{\rm ST}
=
\left(
\mathbb G_{\rm ST},
\boldsymbol\pi_{\rm ST},
\Omega,
\mathcal A^{\rm feas},
\mathbf J,
\mathbb M_{\rm sus}
\right).
$$

Stage 7 is therefore interpreted as an **adaptive, viability-constrained, many-objective reachability problem over evolving P–T–I–O infrastructure regimes**.

---

## 12. Complete frozen mathematical chain

$$
\begin{aligned}
\underbrace{\mathcal S}_{1}
&\rightarrow
\underbrace{\mathfrak I}_{2}
\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{3}\\
&\rightarrow
\underbrace{X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u}_{4}\\
&\rightarrow
\underbrace{K_{\rm sus},\mathcal V,\rho,T_{\mathcal V},T_K}_{5}\\
&\rightarrow
\underbrace{\Phi_{\rm ST}\rightarrow(c_6,\mathcal D_6,\boldsymbol\zeta_T)}_{6}\\
&\rightarrow
\underbrace{\mathfrak P_{\rm ST}}_{7}.
\end{aligned}
$$

---

## 13. Frozen stage boundaries

| Boundary | Scientific meaning |
|---|---|
| Stage 1 → 2 | possible structural relation becomes a retained interdependency only after causal admissibility |
| Stage 2 → 3 | accepted mechanism is evolved through state, time, mode and topology |
| Stage 3 → 4 | evolving trajectory becomes partially observed and operationally controllable |
| Stage 4 → 5 | feasible control is evaluated against acceptability and maintainability |
| Stage 5 → 6 | resilience/viability evidence is translated into regime-adequacy requirements |
| Stage 6 → 7 | why/what/how-deep change becomes which/order/when/under-what-conditions |

---

## 14. Seven-stage validation loop

Every candidate Stage-7 transformation must be replayed through the upstream framework:

$$
\begin{aligned}
\text{Stage-7 candidate}
&\rightarrow\text{Stage-1 structural update}\\
&\rightarrow\text{Stage-2 causal-mechanism update}\\
&\rightarrow\text{Stage-3 dynamic simulation}\\
&\rightarrow\text{Stage-4 observation/control evaluation}\\
&\rightarrow\text{Stage-5 viability evaluation}\\
&\rightarrow\text{Stage-6 adequacy diagnosis}\\
&\rightarrow\text{Stage-7 accept / reject / refine}.
\end{aligned}
$$

The validation loop checks the stages; it does not reorder or replace them.

---

## 15. Representation authority

For final figures and documents:

1. scientific source of truth: this file plus frozen stage-specific files;
2. notation/rendering source: `MATHEMATICAL_PRESENTATION_V3.md`;
3. exact mathematical production: LaTeX/TikZ, Figma/SVG or another deterministic vector workflow;
4. computed figures: Python or Julia with source code and provenance;
5. framework visuals: must pass `../figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`.

> **COMPLETE SEVEN-STAGE CONCEPTUAL AND MATHEMATICAL FRAMEWORK: FROZEN.**
