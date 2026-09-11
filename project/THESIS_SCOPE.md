# MSE Thesis Scope

![Frozen](https://img.shields.io/badge/scientific%20scopes-2--6%20FROZEN-1A7F37)
![Research](https://img.shields.io/badge/Stage%207-DEEP%20RESEARCH-9A6700)

**Status:** CANONICAL CURRENT SCOPE  
**Effective date:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Citation standard:** APA 7th edition author–date  
**Change control:** This scope remains authoritative until explicitly revised and versioned.

---

## 1. System class

The thesis studies a **multilayer interdependent infrastructure system** with

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

The precise system description is:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

The framework-level system is

$$
\mathcal S=\{P,T,I,O\}.
$$

Canonical definition: [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md)

---

## 2. Governing seven-stage framework

The canonical architecture is

$$
\begin{aligned}
\text{Multilayer Structure}
&\rightarrow \text{Causal Mechanisms}
\rightarrow \text{Coupled Hybrid Multiscale Dynamics}\\
&\rightarrow \text{Observation, Organization, Feedback and Control}\\
&\rightarrow \text{Viability}
\rightarrow \text{Resilience-to-Sustainability Transformation Interface}\\
&\rightarrow \text{Sustainable Transformation Pathways}.
\end{aligned}
$$

Canonical framework: [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md)

---

## 3. Current scientific boundary

### Stage 1 — Multilayer Structure

Defines the P–T–I–O system, subsystem decomposition, states, and potential interface locations.

$$
Y(t)=[x_P(t),x_T(t),z_I(t),z_O(t)]^\top.
$$

### Stage 2 — Causal Mechanisms

Defines the 12 directed interdependencies / six bidirectional families. A retained relation requires

$$
\alpha\xrightarrow{M_{ij}}\beta,
$$

and every accepted interdependency is represented by

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t\right).
$$

Canonical Stage 2: [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md)

### Stage 3 — Coupled Hybrid Multiscale Dynamics

Defines how accepted Stage-2 mechanisms evolve through time and space using heterogeneous native subsystem dynamics, causal delays, multiple timescales, discrete events, mode switching, dynamic topology and uncertainty.

$$
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
$$

Canonical Stage 3: [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)

### Stage 4 — Observation, Organization, Feedback and Control

Defines how the evolving Stage-3 system is measured, inferred, interpreted, organizationally constrained and acted upon under imperfect information.

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

$$
(\widehat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I),
$$

$$
u(t)=\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

Canonical Stage 4: [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)

### Stage 5 — Controlled Sustainable Viability

Stage 5 distinguishes acceptable states from states that remain maintainable under admissible control.

$$
K_{\rm sus}(t)
=
\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\},
$$

$$
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
$$

The canonical distinction is

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
$$

The temporal margins remain

$$
T_{\mathcal V}=\text{time to loss of maintainability},
\qquad
T_K=\text{time to actual acceptability violation}.
$$

Canonical Stage 5: [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)

### Stage 6 — Resilience-to-Sustainability Transformation Interface

Stage 6 is now **formally frozen** as **Resilience-to-Sustainability Transition**.

Its frozen research question is:

> **When is recovery insufficient, and what conditions require adaptation or transformation?**

Stage 6 asks whether preserving the current infrastructure regime remains adequate under validated Stage-5 evidence and longer-horizon sustainability, equity, adaptation-limit, lock-in, maladaptation and structural evidence.

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

The frozen translation is

$$
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T),
$$

where

$$
c_6\in\{R,A,T\}
$$

classifies recovery adequacy, adaptation requirement or transformation requirement;

$$
\mathcal D_6
=
\{\mathcal D_P,\mathcal D_T,\mathcal D_I,\mathcal D_O,
\mathcal D_{\mathfrak I},\mathcal D_{\rm env},\mathcal D_{\rm eq}\}
$$

contains the required system/interdependency changes; and

$$
\boldsymbol{\zeta}_T
=
[\zeta_{\rm depth},\zeta_{\rm scope},\zeta_{\rm scale},\zeta_{\rm pace},
\zeta_{\rm equity},\zeta_{\rm environment}]^\top
$$

characterizes the required transformation.

Canonical Stage 6: [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md)

### Stage 7 — Sustainable Transformation Pathways

Stage 7 is the active research stage and is **not frozen**.

The retained research question is:

> **What sequence of interventions leads to a more resilient, equitable and sustainable future system?**

The frozen Stage-6 handoff is

$$
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)
\longrightarrow
\text{Stage-7 intervention/pathway design}.
$$

Current research is testing whether the basic deterministic path

$$
\Pi=[(a_1,t_1),\ldots,(a_N,t_N)]
$$

is sufficient, or whether the primary Stage-7 object should be an adaptive, trigger-dependent pathway graph under deep uncertainty.

Research file: [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS_RESEARCH.md)

---

## 4. Current scientific progression

| Stage | Scientific role | Status |
|---|---|---|
| **1** | Define what exists and where interaction can occur. | Defined / canonical |
| **2** | Define why one component/layer affects another and through what mechanism. | Frozen |
| **3** | Evolve accepted mechanisms through space and time. | Frozen |
| **4** | Observe, infer, coordinate and control the evolving system. | Frozen |
| **5** | Evaluate controlled sustainable viability and proximity to loss. | Frozen |
| **6** | Diagnose regime adequacy and translate resilience evidence into recovery/adaptation/transformation requirements. | **Frozen** |
| **7** | Determine intervention sequencing and transformation pathways under feasibility and uncertainty. | **Deep research complete; scope not frozen** |

---

## 5. Current mathematical progression

The frozen progression through Stage 6 is

$$
\begin{aligned}
\{P,T,I,O\}
&\rightarrow\mathfrak I
\rightarrow\{F,\mathcal G,m\}\\
&\rightarrow\{\widehat X,\mathcal U,u,\tau_{\rm response}\}\\
&\rightarrow\{K_{\rm sus},\mathcal V,\partial\mathcal V,\rho,T_{\mathcal V},T_K\}\\
&\rightarrow\Phi_{\rm ST}
\rightarrow(c_6,\mathcal D_6,\boldsymbol{\zeta}_T).
\end{aligned}
$$

The Stage-7 terminal object remains under research.

---

## 6. Scope discipline

The thesis is framework-driven and evidence-gated. The governing principles include

$$
\text{maximum necessary physical fidelity}\neq\text{maximum possible model detail},
$$

$$
\text{correlation/common exposure}\neq\text{causal interdependency},
$$

$$
\text{technically desirable action}\not\Rightarrow\text{organizationally executable action},
$$

$$
\text{acceptable now}\not\Rightarrow\text{maintainable over the required horizon},
$$

and

$$
\text{recovery of the current regime}\not\Rightarrow\text{long-horizon regime adequacy}.
$$

Each stage must answer a distinct research question and create a corresponding validation obligation.

---

## 7. Stage boundary rule

| Stage | Boundary |
|---|---|
| **3** | Produces trajectories and evolving information/organizational states. |
| **4** | Uses those states to constrain knowledge, feasible action and feedback control. |
| **5** | Evaluates acceptability, maintainability, geometric/temporal proximity to loss and interdependency sensitivity. |
| **6** | Diagnoses whether the present regime remains adequate and specifies what must change and how deep the change must be. |
| **7** | Selects/sequences admissible strategic changes; it does not reopen the Stage-6 need-for-change diagnosis. |

The central Stage-6/7 separation is

$$
\underbrace{\text{WHY / WHAT / HOW DEEP}}_{\text{Stage 6}}
\quad\rightarrow\quad
\underbrace{\text{WHICH / ORDER / WHEN / UNDER WHAT CONDITIONS}}_{\text{Stage 7}}.
$$

---

## 8. Supersession rule

Earlier P–W–T–SW, waste–drainage, equity-centered or other historical architectures preserved in Git history, project memory or archives are **not the current thesis scope**.

They may be used only for provenance or transferable methodological insight unless explicitly reintroduced through a versioned change to the current canonical framework.
