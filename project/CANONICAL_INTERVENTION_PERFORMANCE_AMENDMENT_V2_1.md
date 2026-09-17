# Canonical Intervention-Performance Amendment — v2.1

![Authority](https://img.shields.io/badge/authority-CANONICAL%20AMENDMENT-0969DA)
![Framework](https://img.shields.io/badge/framework-v2.1-1A7F37)
![Scope](https://img.shields.io/badge/scope-Stages%206--7-8250DF)

**Effective date:** 2026-09-17  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Status:** CANONICAL AMENDMENT v2.1  
**Base framework:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Base RQ–SO–H specification:** `CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Change type:** clarification and extension of intervention-performance evaluation; no change to the Stage-5 resilience core.  

> **Authority rule:** Until a consolidated v2.1 framework file is issued, this amendment supersedes the Stage-6/Stage-7 passages of v2.0 only where they concern the sequence from engineering intervention to sustainability and final decision. All unaffected v2.0 definitions remain authoritative.

---

# 1. Scientific decision

The thesis explicitly distinguishes three different engineering properties:

```math
\boxed{
\text{Resilience}
\neq
\text{Effectiveness}
\neq
\text{Efficiency}
}
```

They answer different questions:

| Property | Engineering question | Thesis role |
|---|---|---|
| **Resilience** | Can the coupled system maintain or recover acceptable service under disturbance and uncertainty? | System-level property; remains the Stage-5 uncertainty-aware viability + reachability + probability core. |
| **Effectiveness** | Did a proposed intervention achieve the required resilience/service outcome? | Intervention-performance verification. |
| **Efficiency** | What resources were required to obtain the achieved intervention outcome? | Resource-to-performance assessment. |
| **Sustainability** | What broader accessibility, energy, carbon, cost, and other evidence-supported consequences follow? | Broader consequence assessment; not replaced. |

The core conceptual distinction is therefore

```math
\boxed{
\begin{aligned}
\text{Resilience} &:\ \text{system capability},\\
\text{Effectiveness} &:\ \text{intervention target attainment},\\
\text{Efficiency} &:\ \text{resource use relative to achieved outcome},\\
\text{Sustainability} &:\ \text{broader consequence profile}.
\end{aligned}
}
```

---

# 2. What changes and what does not

| Current thesis element | Revised element | Reason |
|---|---|---|
| **Resilience / Controlled Viability** | **No change** | Still answers whether the system can maintain or recover acceptable service. |
| **Intervention** `a_k` | **Intervention + Effectiveness** | Explicitly verifies that the intervention achieves the required resilience/service target. |
| Direct jump **Intervention → Sustainability consequences** | **Intervention → Effectiveness → Efficiency → Sustainability consequences** | Separates target attainment from resource-performance before broader sustainability assessment. |
| Cost, time, energy, crews/resources embedded mainly in optimization | **Explicit Efficiency assessment** | Makes resource-performance trade-offs visible rather than leaving them implicit inside an objective function. |
| **Sustainability Translation / Consequences** | **No replacement** | Sustainability remains the broader environmental, economic, service/accessibility, and social consequence assessment where evidence supports each quantity. |
| **Engineering Decision** | **Resilience + Effectiveness + Efficiency + Sustainability decision** | Provides a clearer systems-engineering basis for comparing interventions under uncertainty. |

The principal replacement is

```math
\boxed{
\text{Intervention}
\rightarrow
\text{Sustainability}
}
```

with

```math
\boxed{
\text{Intervention}
\rightarrow
\text{Effectiveness}
\rightarrow
\text{Efficiency}
\rightarrow
\text{Sustainability}
}
```

This amendment **does not replace resilience or sustainability**. It fills the missing intervention-performance evaluation between them.

---

# 3. Stage-5 boundary — unchanged

The canonical Stage-5 resilience object remains

```math
\boxed{
\mathfrak R_T(t)
=
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
}
```

with the conceptual composition

```math
\boxed{
\textbf{Resilience}
=
\underbrace{\text{remain}}_{\text{viability}}
+
\underbrace{\text{return}}_{\text{reachability}}
+
\underbrace{\text{confidence}}_{\text{probability}}
}
```

where `+` denotes conceptual composition rather than scalar addition.

No effectiveness or efficiency quantity is inserted into `\mathfrak R_T`; they evaluate **interventions after resilience diagnosis**.

---

# 4. Revised Stage 6 — Resilience Diagnosis, Intervention Performance, and Sustainability Consequences

## Purpose

Convert resilience diagnosis into engineering interventions and evaluate each intervention in the correct sequence:

```math
\boxed{
\mathfrak R_T
\rightarrow
\mathcal D_R
\rightarrow
 a_k
\rightarrow
\text{Effectiveness}
\rightarrow
\text{Efficiency}
\rightarrow
\mathbf J_{\rm sus}^{a_k}.
}
```

The intervention still modifies the coupled model:

```math
\mathfrak M
\overset{a_k}{\longrightarrow}
\mathfrak M^{a_k},
```

and produces a new trajectory

```math
Y^0(x,t)
\rightarrow
Y^{a_k}(x,t).
```

The resilience change remains

```math
\Delta\mathfrak R^{a_k}.
```

## 4.1 Effectiveness

Effectiveness is **target attainment**, not a synonym for resilience and not an arbitrary new resilience score.

For intervention `a_k`, define the effectiveness question as

```math
\boxed{
\text{Does }a_k\text{ achieve the preregistered resilience/service requirement?}
}
```

The exact effectiveness decision rule must be derived from already-defined service requirements, Stage-5 resilience quantities, and preregistered intervention targets. A generic form is

```math
\boxed{
\mathcal E_{\rm fx}(a_k)
=
\mathbf 1
\left[
\text{declared resilience/service target is satisfied}
\right].
}
```

A continuous or vector-valued effectiveness measure may be used only when its engineering meaning, units, threshold, evidence basis, and validation rule are specified before confirmatory analysis.

## 4.2 Efficiency

Efficiency is the relationship between achieved intervention outcome and resources used.

Let

```math
\mathbf C^{a_k}_{\rm res}
```

denote the **evidence-supported resource vector** for intervention `a_k`. Candidate dimensions may include cost, implementation time, energy, personnel/crew effort, or material/resource use, but a dimension enters the confirmatory model only if its definition, unit, accounting boundary, data source, and validation path are established.

Efficiency is therefore represented generically as

```math
\boxed{
\mathcal E_{\rm fy}(a_k)
=
\mathcal F_{\rm eff}
\left(
\text{achieved outcome},
\mathbf C^{a_k}_{\rm res}
\right).
}
```

The thesis does **not** assume that one scalar efficiency index is scientifically justified. Unless defensible weighting is established, efficiency remains multi-dimensional and is compared through normalized resource-performance ratios, Pareto dominance, or another preregistered decision rule.

## 4.3 Sustainability consequences — retained

Sustainability remains a distinct downstream consequence assessment:

```math
\boxed{
\mathbf J_{\rm sus}^{a_k}
=
\mathcal J\left[Y^{a_k}(x,t)\right].
}
```

with the current core vector

```math
\boxed{
\mathbf J_{\rm sus}
=
\begin{bmatrix}
J_{\rm access}\\
J_{\rm energy}\\
J_{\rm carbon}\\
J_{\rm cost}
\end{bmatrix}.
}
```

Additional outcomes require evidence, units, causal linkage, accounting boundary, and validation before confirmatory use.

## 4.4 Revised Stage-6 output

```math
\boxed{
a_k
\rightarrow
Y^{a_k}
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right).
}
```

### Fundamental distinctions

```math
\boxed{
\text{efficient}
\not\Rightarrow
\text{effective}
}
```

```math
\boxed{
\text{effective}
\not\Rightarrow
\text{efficient}
}
```

```math
\boxed{
\text{efficient recovery}
\neq
\text{sustainable recovery}.
}
```

---

# 5. Revised Stage 7 — Engineering Decision and Adaptive Transformation

The final intervention decision must now expose four distinct evaluation dimensions:

```math
\boxed{
\text{Resilience}
+
\text{Effectiveness}
+
\text{Efficiency}
+
\text{Sustainability}
}
```

under feasibility and uncertainty.

The decision architecture becomes

```math
\boxed{
\mathcal A^{\star}
=
\operatorname{Decision}
\left\{
a_k:
\mathfrak R^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\mathbf J_{\rm sus}^{a_k},
\text{feasibility},
\text{uncertainty}
\right\}.
}
```

The exact construction — constrained optimum, Pareto set, satisficing set, robust nondominated set, regret rule, or another justified formulation — remains a preregistration decision. No method is selected merely because it is mathematically convenient.

---

# 6. Revised seven-stage interpretation

The number of framework stages remains **seven**.

| Stage | Scientific role | Main question |
|---|---|---|
| **1. Spatiotemporal Multilayer SoS Structure** | Define systems, components, layers, and geography | What exists and where? |
| **2. Evidence-Grounded Causal Interdependencies** | Define directional mechanisms | Why and through what mechanism are systems coupled? |
| **3. Physics-Based Hybrid Multiscale Dynamics** | Propagate mechanisms through time and space | How, where, and how fast do effects propagate? |
| **4. Observation, State Estimation, Organization and Control** | Determine system knowledge and feasible actions | What do operators know and what can they do? |
| **5. Uncertainty-Aware Viability and Reachability Resilience** | Quantify remain + return + confidence | Can service remain or recover acceptably, and with what probability? |
| **6. Resilience Diagnosis, Intervention Performance, and Sustainability Consequences** | Diagnose, intervene, verify effectiveness, assess efficiency, and quantify sustainability consequences | Does the intervention work, how resource-efficiently, and with what broader consequences? |
| **7. Engineering Decision and Adaptive Transformation** | Select defensible interventions under uncertainty | Which intervention/pathway is justified when resilience, effectiveness, efficiency, sustainability, feasibility, and uncertainty are considered together? |

---

# 7. Revised thesis flow

The high-level engineering chain is now

```math
\boxed{
\begin{gathered}
\text{Need}
\rightarrow
\text{Structure}
\rightarrow
\text{Causality}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Knowledge \& Action}\\
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Effectiveness}
\rightarrow
\text{Efficiency}
\rightarrow
\text{Sustainability}
\rightarrow
\text{Decision}.
\end{gathered}
}
```

In question form:

```math
\boxed{
\text{Can it recover?}
\rightarrow
\text{Does the intervention work?}
\rightarrow
\text{How resource-efficiently?}
\rightarrow
\text{What sustainability consequences follow?}
\rightarrow
\text{What should be implemented?}
}
```

---

# 8. RQ/SO/H dependency impact

This amendment does **not** silently rewrite the frozen v2.0 hypotheses. It establishes the conceptual correction that the next consolidated RQ–SO–H revision must propagate.

Required v2.1 re-audit:

1. **RQ0 / General Objective** — add explicit intervention effectiveness and efficiency between resilience evaluation and sustainability consequences.
2. **SO4 / RQ4 / H4** — distinguish intervention target attainment (**effectiveness**) from resource-performance (**efficiency**) and from sustainability-consequence heterogeneity.
3. **SO5 / RQ5 / H5** — final decision logic must consider resilience, effectiveness, efficiency, sustainability, feasibility, and uncertainty rather than resilience and sustainability alone.
4. **Traceability matrix** — add explicit effectiveness and efficiency metrics/decision objects before H4/H5 preregistration closes.
5. **Figures, mind maps, thesis prose, and experiments** — remove any direct conceptual jump from intervention to sustainability where intervention performance is being evaluated.

Until those dependent documents are consolidated, this amendment is the controlling interpretation for Stages 6–7.

---

# 9. What remains open

This amendment freezes the **conceptual distinction and sequence**, not arbitrary numerical measures.

Still open and requiring evidence/preregistration:

- the exact effectiveness target vector and pass/fail or continuous decision rule;
- the exact efficiency resource vector;
- normalization across heterogeneous resource units;
- whether a scalar efficiency measure is scientifically defensible;
- H4 effectiveness/efficiency thresholds;
- H5 decision-set construction after the new dimensions are incorporated;
- empirical validation of any claimed effectiveness or efficiency advantage.

No threshold, weight, ratio, or ranking may be selected after viewing confirmatory results merely because it produces a favorable conclusion.

---

# 10. Change-control statement

```math
\boxed{
\textbf{Stage 5 remains unchanged.}
}
```

```math
\boxed{
\textbf{Stage 6 now explicitly contains Intervention Performance}
=
\text{Effectiveness} + \text{Efficiency}.
}
```

```math
\boxed{
\textbf{Stage 7 integrates Resilience + Effectiveness + Efficiency + Sustainability under uncertainty.}
}
```

This is a conceptual and traceability update. It does not claim empirical superiority of any intervention, efficiency formulation, or sustainability pathway.