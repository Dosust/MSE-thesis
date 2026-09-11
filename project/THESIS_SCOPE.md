# MSE Thesis Scope

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

The frozen architecture is

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

## 3. Current frozen research boundary

### Stage 1 — Multilayer Structure

Defines the $P$–$T$–$I$–$O$ system, subsystem decomposition, states, and potential interface locations.

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

Defines how accepted Stage-2 mechanisms evolve through time and space using heterogeneous native subsystem dynamics, causal delay, multiple timescales, discrete events, mode switching, dynamic topology, and uncertainty.

$$
Y(t)=[x_P(t),x_T(t),z_I(t),z_O(t)]^\top,
\qquad
\widetilde Y(t)=(Y(t),m(t)).
$$

Canonical Stage 3: [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)

### Stage 4 — Observation, Organization, Feedback and Control

Defines how the evolving Stage-3 system is measured, inferred, interpreted, organizationally constrained, and acted upon under imperfect information.

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

For sequential non-overlapping response processes,

$$
\begin{aligned}
\tau_{\rm response}={}&\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

Canonical Stage 4: [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)

### Stage 5 — Controlled Sustainable Viability

Stage 5 is frozen at framework level under the seven-stage label **Viability**. It distinguishes acceptable states from states that remain maintainable under admissible control.

The acceptable region is

$$
K_{\rm sus}(t)
=
\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\},
$$

and the primary finite-horizon viability object is

$$
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
$$

Stage 5 preserves

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus},
$$

so the viability boundary $\partial\mathcal V$ and actual acceptability boundary $\partial K_{\rm sus}$ remain distinct.

Robust and stochastic viability are separate mathematical extensions:

$$
\text{robust viability}\neq\text{stochastic viability}.
$$

The baseline geometric margin is $\rho_E$ after appropriate state normalization. The Riemannian margin

$$
\rho_g=d_{g_\psi}(Y,\partial\mathcal V),
\qquad g_\psi(Y)\succ0,
$$

remains a proposed thesis construct `[P]`.

The temporal distinction is

$$
T_{\mathcal V}=\text{time to loss of maintainability},
\qquad
T_K=\text{time to actual acceptability violation}.
$$

Stage 4 and Stage 5 connect through

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response},
$$

with proposed dimensionless diagnostics

$$
\Pi_{\mathcal V}=\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K=\frac{\tau_{\rm response}}{T_K}.
$$

Interface criticality is treated through finite perturbation sensitivity unless smoothness is demonstrated.

Canonical Stage 5: [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)

---

## 4. Current scientific progression

| Stage | Scientific role | Status |
|---|---|---|
| **1** | Define what exists and where interaction can occur. | Defined |
| **2** | Define why one component/layer affects another and through what mechanism. | Frozen |
| **3** | Evolve accepted mechanisms through space and time. | Frozen |
| **4** | Observe, infer, coordinate, and control the evolving system. | Frozen |
| **5** | Evaluate controlled sustainable viability and proximity to loss. | Frozen |
| **6** | Translate verified resilience results into sustainability-transition requirements. | **Next** |
| **7** | Define and evaluate sustainable transformation pathways. | Downstream |

---

## 5. Scope discipline

The thesis is framework-driven and evidence-gated. The governing principles are

$$
\text{maximum necessary physical fidelity}\neq\text{maximum possible model detail},
$$

$$
\text{correlation/common exposure}\neq\text{causal interdependency},
$$

$$
\text{technically desirable action}\not\Rightarrow\text{organizationally executable action},
$$

and

$$
\text{acceptable now}\not\Rightarrow\text{maintainable over the required horizon}.
$$

Each mathematical layer must answer a defined research question and create a corresponding validation obligation.

---

## 6. Evidence and validation discipline

The evidence workflow is

$$
\begin{aligned}
\text{Literature}
&\rightarrow \text{Mechanism evidence}
\rightarrow \text{Formal mathematical object}\\
&\rightarrow \text{Simulation / analysis}
\rightarrow \text{Falsification and validation}.
\end{aligned}
$$

The thesis distinguishes empirical/domain evidence, transferable methodological evidence, mathematical theory, derived synthesis, and thesis-proposed constructs. In-text citations and reference lists follow **APA 7th edition**.

A proposed construct remains a candidate contribution until novelty and performance claims survive systematic comparison and falsification.

---

## 7. Stage boundary rule

| Stage | Boundary |
|---|---|
| **3** | Produces trajectories and evolving information/organizational states. |
| **4** | Uses those states to constrain knowledge, feasible action, and feedback control. |
| **5** | Evaluates acceptability, maintainability, geometric/temporal proximity to loss, and interdependency sensitivity. |
| **6** | Uses only validated resilience evidence to formulate sustainability-transition requirements. |

Stage 5 does not redefine Stage-4 control and does not prescribe Stage-6/7 transformations.

---

## 8. Supersession rule

Earlier P–W–T–SW, waste–drainage, equity-centered, or other historical architectures preserved elsewhere in Git history, project memory, archive folders, or research archives are **not the current thesis scope**.

They may be used only for provenance or transferable methodological insight unless explicitly reintroduced through a versioned change to the current canonical framework.
