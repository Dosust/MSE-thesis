# MSE Thesis Scope

**Status:** CANONICAL CURRENT SCOPE  
**Effective date:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Change control:** This scope remains authoritative until explicitly revised and versioned.

---

## 1. System class

The thesis studies a

$$
\boxed{\text{multilayer interdependent infrastructure system}}
$$

with

$$
\boxed{P,T=\text{physical infrastructure systems}}
$$

and

$$
\boxed{I,O=\text{informational and organizational layers}.}
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

The thesis follows the frozen architecture

$$
\text{Multilayer Structure}
\rightarrow
\text{Causal Mechanisms}
\rightarrow
\text{Coupled Hybrid Multiscale Dynamics}
\rightarrow
\text{Feedback \& Control}
\rightarrow
\text{Viability}
\rightarrow
\text{Resilience-to-Sustainability Transformation Interface}
\rightarrow
\text{Sustainable Transformation Pathways}.
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
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t).
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

---

## 4. Current scientific progression

$$
\boxed{
\underbrace{\{P,T,I,O\}}_{\text{Stage 1}}
\rightarrow
\underbrace{\mathfrak I_{ij}^{\alpha\beta}}_{\text{Stage 2}}
\rightarrow
\underbrace{\{Y(t),m(t),\mathcal G(t),T_C,v_c\}}_{\text{Stage 3}}
\rightarrow
\underbrace{I\rightarrow O\rightarrow u}_{\text{Stage 4}}
\rightarrow
\underbrace{\mathcal V_{\rm sus}^{u}}_{\text{Stage 5}}
\rightarrow
\underbrace{\text{Stages 6--7}}_{\text{sustainable transformation}}
}
$$

The next framework-formalization task is **Stage 4 — Feedback & Control**.

---

## 5. Scope discipline

The thesis is framework-driven and evidence-gated. It does not assume that every subsystem requires maximal simulation detail or that every mathematical concept must be implemented at the highest available fidelity.

The governing principles are:

$$
\text{maximum necessary physical fidelity}
\neq
\text{maximum possible model detail},
$$

and

$$
\text{correlation/common exposure}
\neq
\text{causal interdependency}.
$$

Each mathematical layer must answer a defined research question and create a corresponding validation obligation.

---

## 6. Evidence and validation discipline

The evidence workflow is

$$
\text{literature}
\rightarrow
\text{mechanism evidence}
\rightarrow
\text{formal mathematical object}
\rightarrow
\text{simulation/analysis}
\rightarrow
\text{falsification and validation}.
$$

The thesis distinguishes:

- empirical/domain evidence;
- transferable methodological evidence;
- mathematical theory;
- thesis-proposed synthesis.

A proposed construct remains a candidate contribution until novelty and performance claims survive systematic comparison and falsification.

---

## 7. Supersession rule

Earlier P–W–T–SW, waste–drainage, equity-centered, or other historical architectures preserved elsewhere in Git history, project memory, archive folders, or research archives are **not the current thesis scope**.

They may be used only for provenance or transferable methodological insight unless explicitly reintroduced through a versioned change to the current canonical framework.
