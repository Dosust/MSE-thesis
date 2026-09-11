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

Defines the 12 directed interdependencies / six bidirectional families and requires a real causal transmission mechanism for every accepted relation:

$$
\alpha\xrightarrow{M_{ij}}\beta.
$$

Every accepted interdependency is represented by

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right).
$$

Canonical Stage 2: [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md)

### Stage 3 — Coupled Hybrid Multiscale Dynamics

Defines how accepted Stage-2 mechanisms evolve through time and space using heterogeneous native subsystem dynamics, causal delay, multiple timescales, discrete events, mode switching, dynamic topology, and uncertainty.

The four-layer state remains

$$
Y(t)=[x_P(t),x_T(t),z_I(t),z_O(t)]^\top,
$$

with augmented hybrid state

$$
\widetilde Y(t)=(Y(t),m(t)).
$$

Canonical Stage 3: [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)

### Stage 4 — Observation, Organization, Feedback and Control

Defines how the evolving Stage-3 system is measured, inferred, interpreted, organizationally constrained, and acted upon under imperfect information.

The conceptual feedback spine is

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

The mathematical control architecture is

$$
(\widehat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I),
$$

$$
u(t)=\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

Here the control variable is $u(t)$. The symbol $\nu_k(t)$ is reserved only for measurement noise in the Stage-4 measurement model.

For sequential non-overlapping response processes,

$$
\begin{aligned}
\tau_{\rm response}={}&\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}
+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

The proposed diagnostic

$$
\Pi_R=\frac{\tau_{\rm response}}{\tau_{\rm cascade}}
$$

is a thesis construct, not an established resilience law.

Canonical Stage 4: [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)

---

## 4. Current scientific progression

| Stage | Scientific role |
|---|---|
| **1** | Define what exists and where interaction can occur. |
| **2** | Define why one component/layer affects another and through what mechanism. |
| **3** | Evolve accepted mechanisms through space and time. |
| **4** | Observe, infer, coordinate, and control the evolving system. |
| **5** | Evaluate controlled sustainable viability. |
| **6–7** | Translate verified resilience evidence into sustainable transformation. |

The next framework-formalization task is **Stage 5 — Viability**.

---

## 5. Scope discipline

The thesis is framework-driven and evidence-gated. It does not assume that every subsystem requires maximal simulation detail or that every mathematical concept must be implemented at the highest available fidelity.

The governing principles are

$$
\text{maximum necessary physical fidelity}\neq\text{maximum possible model detail},
$$

$$
\text{correlation/common exposure}\neq\text{causal interdependency},
$$

and

$$
\text{technically desirable action}\not\Rightarrow\text{organizationally executable action}.
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
| **5** | Evaluates whether the resulting controlled trajectory is viable. |

Stage 4 does not redefine $z_I$ or $z_O$ dynamics and does not compute $\mathcal V_{\rm sus}^{u}$, $\rho_g$, or $T_{\rm exit}$.

---

## 8. Supersession rule

Earlier P–W–T–SW, waste–drainage, equity-centered, or other historical architectures preserved elsewhere in Git history, project memory, archive folders, or research archives are **not the current thesis scope**.

They may be used only for provenance or transferable methodological insight unless explicitly reintroduced through a versioned change to the current canonical framework.
