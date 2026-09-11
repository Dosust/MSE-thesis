# Canonical System Definition

![Authority](https://img.shields.io/badge/authority-CANONICAL-0969DA)
![Degree](https://img.shields.io/badge/degree-MSE-0969DA)

**Adopted:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Scope:** Multilayer interdependent infrastructure resilience and sustainability research  
**Change rule:** Use this system description throughout the thesis unless it is explicitly revised and versioned.

> **Degree nomenclature rule:** This research is an **MSE (Master of Science in Engineering)** thesis.

---

## 1. Canonical system class

The thesis studies a **multilayer interdependent infrastructure system** with

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

The most precise system description is:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

The framework-level layer set is

$$
\mathcal L=\{P,T,I,O\}.
$$

---

## 2. Layer interpretation

| Symbol | Type | Role |
|---|---|---|
| $P$ | Physical infrastructure system | Power generation, transmission, distribution, DER/storage, charging, and traction-power supply. |
| $T$ | Physical infrastructure system | Road, electric-bus, urban-rail, heavy/regional-rail, and multimodal transportation. |
| $I$ | Informational layer | Sensing, communication, data availability, information quality, latency, synchronization, estimation support, and signaling. |
| $O$ | Organizational layer | Authority, coordination, decision making, resource allocation, workforce, logistics, mobilization, and intervention capability. |

The physical state is

$$
X(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)
\end{bmatrix}.
$$

The informational–organizational state is

$$
Z(t)=
\begin{bmatrix}
z_I(t)\\
z_O(t)
\end{bmatrix}.
$$

The integrated system state is therefore

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
$$

This notation is canonical: $I$ and $O$ name the layers, whereas $z_I(t)$ and $z_O(t)$ denote their time-varying states.

---

## 3. Modeling discipline

The thesis must not reduce the system to a purely physical Power–Transportation network when informational or organizational mechanisms materially affect observation, coordination, control, propagation, recovery, or viability.

Accordingly,

$$
R_{\mathrm{system}}\neq R(P,T)
$$

in the general case studied here. The working dependence is

$$
R_{\mathrm{system}}
=
R(P,T,I,O,\mathbb I),
$$

where $\mathbb I$ denotes the set of explicitly characterized interdependency objects.

The canonical Stage-2 interdependency object is

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,
E_j^\beta,
M_{ij},
w_{ij},
\delta_{ij},
\tau_{ij},
a_{ij},
m,
\mathcal H_t
\right),
$$

with

$$
\alpha,\beta\in\{P,T,I,O\},
\qquad
\alpha\neq\beta.
$$

---

## 4. Canonical cross-stage interpretation

| Stage | Uses the system definition to answer |
|---|---|
| **1 — Multilayer Structure** | What exists and where interaction can occur. |
| **2 — Causal Mechanisms** | Which cross-layer relations are truly causal and how they transmit effects. |
| **3 — Coupled Hybrid Multiscale Dynamics** | How the state $Y(t)$ and effective topology evolve. |
| **4 — Observation, Organization, Feedback and Control** | How the physical state is measured, inferred, organizationally interpreted, and acted upon. |
| **5 — Viability** | Whether controlled trajectories remain acceptable and maintainable. |

---

## 5. Canonical thesis statement

> **The research studies a multilayer interdependent Power–Transportation infrastructure system in which Power and Transportation form the physical infrastructure systems, while Information and Organization form interacting informational and organizational layers that shape observation, coordination, control, propagation, recovery, viability, and sustainable transformation.**

This is the default system identity for the MSE thesis, presentations, literature extraction, mathematical modeling, simulation, validation, and framework design unless explicitly changed through versioned revision.
