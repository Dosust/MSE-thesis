# MSE Thesis Scope

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Phase](https://img.shields.io/badge/next-hypothesis%20specification%20%26%20validation-0969DA)

**Status:** SUPERSEDED FOR ACTIVE FRAMEWORK INTERPRETATION — retained for provenance

> **Current authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md` and `CANONICAL_RQ_SO_HYPOTHESES_V3.md` supersede the stage semantics, RQ/SO/H mapping, resilience core, and Stage-6/7 interpretation in this file. Do not use this file as active authority where it conflicts with v2/v3.  
**Effective date:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Citation standard:** APA 7th edition author–date  
**Change control:** The complete seven-stage conceptual/mathematical framework is frozen. Any scientific revision requires explicit approval and versioning.

---

## 1. System class

The thesis studies a **multilayer interdependent infrastructure system** with

```math
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
```

The precise system description is:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

The system object is

```math
\mathcal S=\{P,T,I,O\}.
```

Canonical definition: [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md)

---

## 2. Frozen seven-stage architecture

```math
\begin{aligned}
\text{Multilayer Structure}
&\rightarrow\text{Causal Mechanisms}
\rightarrow\text{Coupled Hybrid Multiscale Dynamics}\\
&\rightarrow\text{Observation, Organization, Feedback and Control}\\
&\rightarrow\text{Viability}
\rightarrow\text{Resilience-to-Sustainability Transformation Interface}\\
&\rightarrow\text{Sustainable Transformation Pathways}.
\end{aligned}
```

Canonical framework: [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md)

---

## 3. Frozen stage scope

| Stage | Core object / relation | Scientific responsibility |
|---:|---|---|
| **1** | $\mathcal S$, $Y=[x_P,x_T,z_I,z_O]^\top$ | define what exists and where interactions can occur |
| **2** | $\mathfrak I_{ij}^{\alpha\beta}$ | retain only explicit causal cross-layer mechanisms |
| **3** | $F_{\mathcal G}^{m}$, $\widetilde Y=(Y,m)$ | evolve accepted mechanisms through time, mode, events and topology |
| **4** | $X\to y\to I\to\widehat X\to O\to u\to X$ | infer the physical state and generate feasible operational control |
| **5** | $K_{\rm sus}$, $\mathcal V_{\rm sus}^{u,T}$, $\rho$, $T_{\mathcal V}$, $T_K$ | evaluate acceptability, maintainability and proximity to loss |
| **6** | $\Phi_{\rm ST}\mapsto(c_6,\mathcal D_6,\boldsymbol\zeta_T)$ | diagnose regime adequacy and specify why/what/how-deep change is required |
| **7** | $\mathfrak P_{\rm ST}$ | generate/test adaptive strategic pathways over alternative future regimes |

---

## 4. Stage 2 — Causal Mechanisms

A retained relation requires

```math
\alpha\xrightarrow{M_{ij}}\beta,
```

with

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right).
```

Common hazard exposure or correlation is not sufficient.

Canonical file: [`STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](STAGE_2_INTERDEPENDENCY_MECHANISMS.md)

---

## 5. Stage 3 — Coupled Hybrid Multiscale Dynamics

The mode is kept separate from the integrated state:

```math
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
```

Stage 3 owns heterogeneous dynamics, causal delays, multiple timescales, discrete events, dynamic topology and uncertainty.

Canonical file: [`STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)

---

## 6. Stage 4 — Observation, Organization, Feedback and Control

```math
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow\widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
```

Stage 4 uses $u(t)$ to **operate the current regime**.

Canonical file: [`STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)

---

## 7. Stage 5 — Viability

The acceptable region and controlled viable set are different:

```math
K_{\rm sus}
\supseteq
\mathcal V_{\rm sus}^{u,T},
```

and

```math
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
```

Canonical file: [`STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)

---

## 8. Stage 6 — Resilience-to-Sustainability Transformation Interface

The frozen translation is

```math
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol\zeta_T).
```

Stage 6 answers

```math
\text{WHY change}
+
\text{WHAT must change}
+
\text{HOW DEEP}.
```

Its output is directly

```math
(c_6,\mathcal D_6,\boldsymbol\zeta_T),
```

with no extra alias required.

Canonical file: [`STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md)

---

## 9. Stage 7 — Sustainable Transformation Pathways

Stage 7 answers

```math
\text{WHICH intervention}
+
\text{ORDER}
+
\text{WHEN}
+
\text{CONDITIONS}.
```

The candidate future regime is

```math
\mathfrak M_k
=
(\mathcal S_k,\mathcal G_k,\mathfrak I_k,F_k,\Theta_k,K_{{\rm sus},k},\mathcal U_k).
```

The strategic transformation vector is

```math
\mathbf a_k
=
\begin{bmatrix}
a_k^P\\a_k^T\\a_k^I\\a_k^O\\a_k^{\mathfrak I}
\end{bmatrix},
```

and

```math
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k).
```

The Stage-4 / Stage-7 separation is

```math
\underbrace{u(t)}_{\text{operate current regime}}
\neq
\underbrace{\mathbf a_k}_{\text{transform regime}}.
```

The terminal object is

```math
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
```

Stage 7 is an **adaptive, viability-constrained, many-objective reachability problem over evolving P–T–I–O infrastructure regimes**.

Canonical file: [`STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md)

---

## 10. Complete mathematical progression

```math
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
```

---

## 11. Primary hypotheses

The five-primary-hypothesis logic is frozen:

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

Numerical thresholds $\delta_1,\ldots,\delta_5$ and exact confirmatory test specifications remain unfrozen until justified *a priori* in the Hypothesis Specification Matrix.

Canonical file: [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md)

---

## 12. Scope discipline

Mandatory separations include

```math
\text{structure}\neq\text{causal mechanism},
```

```math
\text{event time}\neq\text{causal delay}\neq\text{timescale},
```

```math
K_{\rm sus}\neq\mathcal V_{\rm sus}^{u,T},
```

```math
u(t)\neq\mathbf a_k,
```

```math
a_{ij}\neq\mathbf a_k,
```

and

```math
\text{current-regime viability}
\neq
\text{long-horizon regime adequacy}.
```

---

## 13. Validation loop

Every Stage-7 candidate is replayed through the upstream framework:

```math
\begin{aligned}
\text{Stage-7 candidate}
&\rightarrow\text{Stage-1 structural update}\\
&\rightarrow\text{Stage-2 mechanism update}\\
&\rightarrow\text{Stage-3 dynamic simulation}\\
&\rightarrow\text{Stage-4 observation/control evaluation}\\
&\rightarrow\text{Stage-5 viability evaluation}\\
&\rightarrow\text{Stage-6 adequacy diagnosis}\\
&\rightarrow\text{Stage-7 accept / reject / refine}.
\end{aligned}
```

The loop validates candidate transformations; it does not reorder the seven stages.

---

## 14. Current phase

> **STAGES 1–7: CONCEPTUAL AND MATHEMATICAL FRAMEWORK FROZEN.**

The immediate scientific work is the Hypothesis Specification Matrix, followed by case-study design, computation, falsification and validation.

---

## 15. Supersession rule

Earlier P–W–T–SW, waste–drainage, earlier six-chain, or pre-freeze Stage-7 formulations are historical/provenance material. They are not current thesis authority unless explicitly reintroduced through a versioned revision.
