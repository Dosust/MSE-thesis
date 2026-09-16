# Canonical SoS–Complex System Interpretation v1.0

**Date:** 2026-09-16  
**Status:** CANONICAL CONCEPTUAL INTERPRETATION  
**Scope:** Coupled Power–Transportation infrastructure thesis  
**Purpose:** Preserve the structural/behavioral distinction used throughout the thesis.

---

## 1. Difference

| Concept | Meaning | Best use in this thesis |
|---|---|---|
| **System of Systems (SoS)** | Several systems remain **operationally and managerially independent**, but interact to produce system-level behavior (Maier, 1998). | Describes **what Power + Transportation are structurally**. |
| **Complex System** | A system of interacting components whose nonlinear interdependencies, feedbacks and adaptation can produce **emergent behavior, cascades and unexpected system-level effects** (Rinaldi et al., 2001). | Describes **how the coupled P–T system behaves dynamically**. |

Infrastructure literature supports both views. Interdependent infrastructures are often treated as complex adaptive systems because interactions can amplify disturbances and produce cascading failures (Rinaldi et al., 2001; Ouyang, 2014). Integrated-infrastructure reviews also combine interdependency analysis with complex-network and system-level modeling.

---

## 2. Canonical hierarchical interpretation

Use both concepts, hierarchically:

```math
\boxed{
\textbf{Power–Transportation System of Systems}
\quad
\text{modeled as}
\quad
\textbf{an interdependent complex dynamical system}
}
```

The distinction is:

```math
\boxed{
\text{SoS}=\text{architecture}
\qquad
\text{Complex system}=\text{behavior}
}
```

This distinction must remain consistent throughout the thesis.

---

## 3. Canonical thesis wording

> **This research represents coupled Power–Transportation infrastructure as an interdependent system of systems and studies its behavior as a complex dynamical system governed by time-varying interdependencies, feedbacks, cascading effects and recovery processes.**

This wording preserves the thesis unification idea without forcing the constituent infrastructures to lose their independent physics.

---

## 4. Modeling implication

The constituent systems retain their own governing physics:

```math
\dot x_P=f_P(\cdot),
\qquad
\dot x_T=f_T(\cdot),
```

while their unified behavior emerges through evidence-supported directed interdependencies and feedbacks:

```math
\mathbb I(t)
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y(t).
```

Therefore, **unification does not mean identical physics**. It means different physical systems are connected through a common mathematical architecture of states, interfaces, causal dependencies, feedbacks and controls.

---

## 5. Literature anchors

- Maier, M. W. (1998). *Architecting principles for systems-of-systems*. Systems Engineering, 1(4), 267–284.
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). *Identifying, understanding, and analyzing critical infrastructure interdependencies*. IEEE Control Systems Magazine, 21(6), 11–25. https://doi.org/10.1109/37.969131
- Ouyang, M. (2014). *Review on modeling and simulation of interdependent critical infrastructure systems*. Reliability Engineering & System Safety, 121, 43–60.

---

## 6. Use rule

For proposal, thesis chapters, figures and presentations, use the following hierarchy unless explicitly revised:

```math
\boxed{
\text{Structural identity: Interdependent Power–Transportation System of Systems}
}
```

```math
\boxed{
\text{Behavioral model: Interdependent complex dynamical system}
}
```

This note complements `CANONICAL_SYSTEM_DEFINITION.md` and `CANONICAL_7_STAGE_FRAMEWORK.md`; it does not alter the frozen seven-stage sequence or dependency contract.
