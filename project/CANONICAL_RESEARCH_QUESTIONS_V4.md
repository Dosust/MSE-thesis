# Canonical Research Questions — v4.0

![Authority](https://img.shields.io/badge/authority-CANONICAL-0969DA)
![Logic](https://img.shields.io/badge/RQ0%20%2B%20RQ1--RQ7-v4.0%20OFFICIAL-1A7F37)
![Spatiotemporal](https://img.shields.io/badge/spatiotemporal-EXPLICIT-8250DF)
![SoS](https://img.shields.io/badge/System%20of%20Systems-ARCHITECTURE-0969DA)

**Status:** CANONICAL v4.0 / OFFICIAL RESEARCH-QUESTION AUTHORITY  
**Effective date:** 2026-09-20  
**User authorization:** Explicitly authorized in conversation on 2026-09-20.  
**Framework authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Prior RQ authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Supersession rule:** This file supersedes v3.0 **only for the exact wording and titles of RQ0 and RQ1–RQ7**. `CANONICAL_RQ_SO_HYPOTHESES_V4.md` is authoritative for SO1–SO7 and H1–H5 wording and test logic. No hypothesis, threshold, dataset, validation gate, or confirmatory metric is changed by this RQ-only authority update.

---

## 0. Frozen scientific distinctions

The official research questions preserve three distinct scientific objects:

```math
\boxed{
\underbrace{\mathcal S_{PT}}_{\text{System-of-Systems architecture}}
\neq
\underbrace{\mathfrak G_{PT}(x,t)}_{\text{spatiotemporal structure}}
\neq
\underbrace{F_q[Y(x,t)]}_{\text{complex spatiotemporal dynamics}}
}
```

Interpretation:

- **System of Systems** identifies the constituent systems and supporting domains and preserves their identities.
- **Spatiotemporal structure** identifies what exists, where it exists, when it is relevant, and where/when interaction can occur.
- **Complex spatiotemporal dynamics** describe how states, mechanisms, disturbances, feedback, cascades, delays, controls, and recovery evolve across space and time.

The physical core remains `P+T`; Information and Organization remain supporting domains governing knowledge and feasible action.

---

# RQ0 — Overarching Research Question

> **How can coupled Power–Transportation infrastructure be represented as an interdependent System of Systems and modeled as a spatiotemporal complex dynamical system to connect qualified directional dependencies, observation- and organization-constrained feasible response, uncertainty-aware service resilience, engineering intervention consequences, and defensible engineering decisions?**

**Status:** FROZEN.

RQ0 is answered compositionally from the qualified outputs of RQ1–RQ7:

```math
\boxed{
A(RQ_0)
=
\mathscr S
\left[
A(RQ_1),A(RQ_2),A(RQ_3),A(RQ_4),A(RQ_5),A(RQ_6),A(RQ_7)
\right].
}
```

---

# RQ1 — Spatiotemporal System-of-Systems Structure

> **What constituent systems, supporting Information and Organization domains, services, entities, states, spatial locations, temporal characteristics, and candidate interfaces constitute the bounded Power–Transportation System of Systems, and where and when can interactions occur?**

**Scientific job:** establish the bounded SoS ontology and its spatiotemporal instantiation.  
**Stage:** 1.  
**Does not establish:** causality.

Conceptual output:

```math
\boxed{
Z_1=
\left(
\mathcal S_{PT},
\mathfrak G_{PT}(x,t),
Q_P,
Q_T,
\mathcal I^{cand}
\right).
}
```

---

# RQ2 — Evidence-Qualified Spatiotemporal Directional Dependencies

> **Which candidate Power–Transportation relations can be admitted as evidence-qualified directional dependency mechanisms, through what mechanisms, where and when do they activate, under what operating and hazard conditions, with what delays, characteristic timescales, and uncertainty, and within what validity domain?**

**Scientific job:** convert candidate relations into qualified directional mechanisms.  
**Stage:** 2.

```math
\boxed{
\mathcal I^{cand}
\longrightarrow
\mathcal I^{qualified}.
}
```

Mandatory causal firewall:

```math
\text{co-location}\neq\text{dependency},
\qquad
\text{association}\neq\text{causality},
\qquad
P\rightarrow T\not\Rightarrow T\rightarrow P.
```

---

# RQ3 — Complex Spatiotemporal Coupled Dynamics

> **How do qualified and dynamically ready directional dependency mechanisms evolve, interact, and propagate across space and time, and how do they alter coupled physical states and electricity and mobility service trajectories relative to independent and static-coupling representations?**

**Scientific job:** determine how qualified mechanisms change coupled physical and service behavior across space and time.  
**Stage:** 3.  
**Confirmatory mapping:** H1.

Canonical dynamical form:

```math
\boxed{
\frac{\partial Y(x,t)}{\partial t}
=
F_q
\left(
Y(x,t),
u(x,t),
\eta(x,t);
\theta,
\mathcal I(x,t)
\right).
}
```

Comparator architecture remains:

```math
\boxed{
M_0\quad\text{vs}\quad M_1\quad\text{vs}\quad M_2.
}
```

---

# RQ4 — Spatiotemporal Observation, Organization, and Feasible Response

> **How do spatially and temporally distributed observations, state estimation, information availability, organizational conditions, and feasible control shape the response and recovery of the evolving coupled Power–Transportation system?**

**Scientific job:** determine what can be known and what can actually be done as the coupled system evolves.  
**Stage:** 4.  
**Confirmatory mapping:** H2.

```math
\boxed{
Y(x,t)
\rightarrow
y(x,t)
\rightarrow
\widehat Y(x,t)
\rightarrow
(I,O)
\rightarrow
\mathcal U_{\mathrm{feas}}(x,t)
\rightarrow
u(x,t).
}
```

---

# RQ5 — Uncertainty-Aware Spatiotemporal Service Resilience

> **Under what spatiotemporal conditions can required electricity and mobility services remain acceptable or be recovered under feasible actions and uncertainty, and what additional engineering information do viability and reachability provide beyond conventional service-recovery measures?**

**Scientific job:** determine maintainability, recoverability, and confidence for required services across space and time.  
**Stage:** 5.  
**Confirmatory mapping:** H3.

```math
\boxed{
\underbrace{\text{Remain}}_{\text{viability}}
+
\underbrace{\text{Return}}_{\text{reachability}}
+
\underbrace{\text{Confidence}}_{\text{uncertainty}}
}
```

where the plus signs denote conceptual composition, not scalar addition.

---

# RQ6 — Spatiotemporally Targeted Engineering Intervention Consequences

> **How do candidate engineering interventions, characterized by type, location, timing, and scale where relevant, differ in resilience effectiveness, resource requirements and efficiency, and admitted sustainability consequences under independently qualified requirements, declared accounting boundaries, and uncertainty?**

**Scientific job:** evaluate what changes when the system is deliberately modified and keep resilience, resources, efficiency, and admitted sustainability consequences distinct.  
**Stage:** 6.  
**Confirmatory mapping:** H4.

Conceptually:

```math
\boxed{
a_k=
(
\text{type},
\text{location},
\text{timing},
\text{scale},
\text{capacity/resources}
).
}
```

and

```math
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right).
}
```

---

# RQ7 — Defensible Spatiotemporal Engineering Decision

> **Which candidate interventions or infrastructure transformations, including their location, timing, and scale where relevant, remain defensible when resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty are evaluated jointly?**

**Scientific job:** determine the defensible engineering decision set without assuming a universally optimal solution or mandatory intervention sequence.  
**Stage:** 7.  
**Confirmatory mapping:** H5.

```math
\boxed{
\mathcal A_{\rm def}
\subseteq
\mathcal A_{\rm candidate}.
}
```

Sequential adaptation

```math
a_0\rightarrow a_1\rightarrow\cdots\rightarrow a_H
```

remains a conditional Stage-7 extension and is not assumed by the primary RQ7 wording.

---

# Seven-question dependency chain

The official questions are not independent thematic questions. They form a controlled scientific dependency chain:

```math
\boxed{
RQ_1
\rightarrow
RQ_2
\rightarrow
RQ_3
\rightarrow
RQ_4
\rightarrow
RQ_5
\rightarrow
RQ_6
\rightarrow
RQ_7
\rightarrow
RQ_0.
}
```

The arrows denote scientific dependency, not strict mathematical implication.

| RQ | Primary scientific obligation | Explicit space–time role | Stage |
|---|---|---|---:|
| RQ1 | SoS architecture | entities, geography, temporal characteristics, interfaces | 1 |
| RQ2 | directional mechanism qualification | activation location/time, delay, timescale, hazard/mode | 2 |
| RQ3 | complex coupled dynamics | evolution and propagation of `Y(x,t)` | 3 |
| RQ4 | knowledge and feasible response | distributed observations, estimates and feasible controls across `x,t` | 4 |
| RQ5 | service resilience | where/when service remains acceptable or recovers | 5 |
| RQ6 | intervention consequences | what/where/when/how much is changed | 6 |
| RQ7 | engineering decision | which location/timing/scale of change remains defensible | 7 |

---

# Thesis-wide scientific chain

```math
\boxed{
\begin{aligned}
&\textbf{Critical electricity and mobility services}\\
&\downarrow\\
&\textbf{Spatiotemporal P--T System-of-Systems architecture}\\
&\downarrow\\
&\textbf{Evidence-qualified directional dependencies}\\
&\downarrow\\
&\textbf{Complex spatiotemporal coupled dynamics}\\
&\downarrow\\
&\textbf{Spatiotemporal observation, estimation, organization, and feasible control}\\
&\downarrow\\
&\textbf{Uncertainty-aware spatiotemporal service viability and recovery}\\
&\downarrow\\
&\textbf{Spatially and temporally targeted engineering interventions}\\
&\downarrow\\
&\textbf{Resource and admitted sustainability consequences}\\
&\downarrow\\
&\textbf{Defensible engineering decision}.
\end{aligned}
}
```

---

# Governance and traceability rule

This authority changes **research-question wording only**.

Until a separately authorized synchronization is made:

```text
RQ wording authority: CANONICAL_RESEARCH_QUESTIONS_V4.md
SO/H wording and test-logic authority: CANONICAL_RQ_SO_HYPOTHESES_V3.md
Framework authority: CANONICAL_7_STAGE_FRAMEWORK_V2.md
```

Existing mappings remain:

```math
RQ1/SO1,\;RQ2/SO2\rightarrow\text{developmental evidence supporting H1},
```

```math
RQ3\rightarrow H1,\quad
RQ4\rightarrow H2,\quad
RQ5\rightarrow H3,\quad
RQ6\rightarrow H4,\quad
RQ7\rightarrow H5.
```

If any existing SO or H wording is inconsistent with this v4 RQ authority, the inconsistency must be resolved by a separately versioned amendment; it must not be silently harmonized.

