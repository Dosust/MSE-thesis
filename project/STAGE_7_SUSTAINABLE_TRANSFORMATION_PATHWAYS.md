# Stage 7 — Sustainable Transformation Pathways

> **AUTHORITY-DRIFT CLEANUP 2026-09-19 — HISTORICAL STAGE-7 THEORY / ACTIVE DECISION SCOPE SUPERSEDED**
>
> This 2026-09-11 frozen pathway theory is preserved as methodological provenance. Active Stage-7 interpretation is governed by `CANONICAL_RQ_SO_HYPOTHESES_V3.md`, `CANONICAL_INTERVENTION_PERFORMANCE_AMENDMENT_V2_1.md`, and `project/stage7/STAGE7_MASTER_REGISTER_V1.xlsx` pending v2.1 alignment.  
> Current H5 is the resilience-only versus joint resilience–sustainability decision test. Adaptive/sequential pathways are conditional extensions only when separately justified and preregistered.


![Stage](https://img.shields.io/badge/Stage%207-FROZEN-1A7F37)
![Evidence](https://img.shields.io/badge/evidence-50--paper%20synthesis-0969DA)

**Framework stage:** Stage 7 — Sustainable Transformation Pathways  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Change rule:** Do not revise the Stage-7 scientific scope without an explicit versioned framework change.  
**Framework preservation rule:** Stage 7 transforms candidate P–T–I–O regimes; it does not redefine the scientific responsibilities of Stages 1–6.

> **Evidence notation:** `[E]` = established literature/theory; `[D]` = derived synthesis; `[P]` = proposed thesis construct requiring validation.

> **Rendering rule:** GitHub-facing equations use `$$...$$`; equation labels are Markdown headings; long verbal specifications use tables rather than oversized mathematical boxes.

---

## RQ7 / SO7 — current canonical question

> **What should be changed, where, when and in what sequence to achieve effective, efficient and sustainable infrastructure transformation under feasibility constraints and uncertainty?**

**Specific objective:** Evaluate candidate infrastructure transformations and, where justified, intervention sequences using effectiveness, efficiency, sustainability, feasibility and uncertainty to support engineering decisions.

**Interpretation boundary:** Framework v2 and intervention-performance amendment v2.1 supersede conflicting legacy mathematics or scope below. The current RQ heading does not validate or promote legacy constructions.

**Question authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`. This 2026-09-17 wording amendment aligns the question with Chapter I; technical results and validation status are unchanged.

The Stage-6 / Stage-7 separation is

```math
\underbrace{\text{WHY change + WHAT must change + HOW DEEP}}_{\text{Stage 6}}
\quad\longrightarrow\quad
\underbrace{\text{WHICH intervention + ORDER + WHEN + CONDITIONS}}_{\text{Stage 7}}.
```

Stage 7 receives the frozen Stage-6 output

```math
(c_6,\mathcal D_6,\boldsymbol\zeta_T)
```

and converts those requirements into adaptive transformation pathways.

---

## 1. State control and regime transformation are different

Stage 4 operates a given infrastructure regime through $u(t)$. Stage 7 changes the regime that will subsequently be operated.

```math
\underbrace{u(t)}_{\text{Stage 4 operational control}}
\neq
\underbrace{\mathbf a_k}_{\text{Stage 7 strategic transformation action}}.
```

The canonical Stage-7 infrastructure-regime object is

```math
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
```

| Component | Meaning |
|---|---|
| $\mathcal S_k$ | P–T–I–O system composition |
| $\mathcal G_k$ | multilayer topology |
| $\mathfrak I_k$ | causal interdependency set |
| $F_k$ | hybrid multiscale dynamics |
| $\Theta_k$ | parameters, capacities and configuration |
| $K_{{\rm sus},k}$ | justified acceptability/sustainability constraints |
| $\mathcal U_k$ | available operational-control capability |

This notation extends the frozen Stage-6 regime object consistently rather than introducing a second regime symbol.

---

## 2. Three distinct topology levels

Stage 7 distinguishes topology **within a layer**, topology **across layers**, and topology **across alternative future regimes**.

### Level I — within-layer topology

For layer or physical system $\alpha$,

```math
G_k^\alpha=(V_k^\alpha,E_k^\alpha),
\qquad
\alpha\in\mathcal L,
\qquad
\mathcal L=\{P,T,I,O\}.
```

### Level II — multilayer P–T–I–O topology

A generic representation is

```math
\mathcal G_k
=
\left(
\{G_k^\alpha\}_{\alpha\in\mathcal L},
\{E_k^{\alpha\beta}\}_{\alpha,\beta\in\mathcal L}
\right).
```

This structural representation does not replace the Stage-2 causal object $\mathfrak I_{ij}^{\alpha\beta}$.

### Level III — graph of alternative infrastructure regimes `[P]`

The Stage-7 transformation meta-graph is

```math
\mathbb G_{\rm ST}
=
(\mathbb V_{\rm ST},\mathbb E_{\rm ST}),
```

with

```math
v_k\equiv\mathfrak M_k,
```

and an admissible transformation edge

```math
\mathfrak M_k
\xrightarrow{\mathbf a_{k\ell}}
\mathfrak M_\ell.
```

This is the thesis interpretation of a **graph of alternative multilayer infrastructure regimes**. Multilayer-network mathematics motivates the representation, but the complete meta-graph is a proposed thesis construct `[P]` (De Domenico et al., 2013).

---

## 3. Transformation operator

A strategic intervention changes the infrastructure regime according to

```math
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}
\left(
\mathfrak M_k,\xi_k
\right),
```

where $\xi_k$ represents uncertainty or exogenous conditions relevant to the transformation step.

A transformation may modify

```math
\mathcal G,
\qquad
\mathfrak I,
\qquad
F,
\qquad
\Theta,
\qquad
K_{\rm sus},
\qquad
\mathcal U.
```

Stage 7 is therefore stronger than graph rewiring alone: it can change structure, causal coupling, physical capability, institutional capability, future control authority, and the applicable long-horizon design constraints.

---

## 4. Strategic intervention space

Use the bold vector $\mathbf a_k$ for Stage-7 actions so it cannot be confused with the Stage-2 activation variable $a_{ij}$.

```math
\mathbf a_k
=
\begin{bmatrix}
a_k^P\\
a_k^T\\
a_k^I\\
a_k^O\\
a_k^{\mathfrak I}
\end{bmatrix}.
```

| Action family | Representative transformations |
|---|---|
| $a_k^P$ | DER/storage, microgrids, hardening, traction-power redundancy, grid redesign |
| $a_k^T$ | road redundancy, multimodal corridors, charging access, bus/rail alternatives |
| $a_k^I$ | sensing/communication redundancy, backup power, interoperability, distributed information capability |
| $a_k^O$ | authority redesign, coordination institutions, mutual aid, workforce/resource arrangements |
| $a_k^{\mathfrak I}$ | intentional modification of cross-layer causal dependence |

Information and organization remain genuine design spaces because coordination and information exchange affect infrastructure response and recovery (Li et al., 2019).

---

## 5. Direct Stage-2 → Stage-7 connection

Stage 2 defines

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right).
```

Stage 7 may intentionally redesign an accepted interdependency:

```math
\mathfrak I_{ij}^{\alpha\beta}
\longrightarrow
{\mathfrak I'}_{ij}^{\alpha\beta}.
```

Possible changes include

```math
w_{ij}\rightarrow w'_{ij},
\qquad
\delta_{ij}\rightarrow\delta'_{ij},
\qquad
\tau_{ij}\rightarrow\tau'_{ij},
\qquad
a_{ij}:1\rightarrow0.
```

The objective is not universally to reduce coupling. Depending on mechanism and context, Stage 7 may weaken harmful dependence, add redundancy, introduce selective autonomy, or strengthen beneficial interdependence.

---

## 6. Adaptive transformation policy

A fixed schedule

```math
\Pi_F=[(\mathbf a_1,t_1),\ldots,(\mathbf a_N,t_N)]
```

is retained as a valid **realized pathway** or fixed comparator. Under deep uncertainty, however, the fundamental Stage-7 decision object is adaptive.

A candidate policy is

```math
\mathbf a_k
=
\pi_k^{\rm ST}
\left(
\widehat X_k,
 z_{I,k},
 z_{O,k},
 \mathfrak M_k,
 \mathcal H_k
\right),
```

with policy family

```math
\boldsymbol\pi_{\rm ST}
=
\{\pi_0^{\rm ST},\pi_1^{\rm ST},\ldots,\pi_N^{\rm ST}\}.
```

The superscript `ST` distinguishes the long-horizon transformation policy from the Stage-4 operational control policy $\pi$.

Dynamic Adaptive Policy Pathways retain future alternatives and allow switching when monitored conditions invalidate the current path (Haasnoot et al., 2013).

---

## 7. Monitoring and trigger conditions

Let a Stage-7 signpost be

```math
s_j(t)
=
s_j\!\left(
\widehat X(t),
z_I(t),
z_O(t),
\mathfrak M(t),
\xi(t)
\right).
```

Let $\mathcal Z_j$ denote the trigger region for signpost $j$. The corresponding trigger time is

```math
\tau_j
=
\inf\{t\ge t_k:s_j(t)\in\mathcal Z_j\}.
```

The long-horizon decision loop is therefore

```math
\text{observe}
\rightarrow
\text{update}
\rightarrow
\text{detect trigger}
\rightarrow
\text{select strategic intervention}.
```

Stage 4 remains active because information and organization determine what can be observed, interpreted and implemented; Stage 7 uses those capabilities for long-horizon adaptation rather than redefining Stage 4.

---

## 8. Transformation timing and path dependence

Stage 7 distinguishes several clocks:

| Symbol | Meaning |
|---|---|
| $t_k$ | decision/initiation time |
| $\ell_k$ | implementation lead time |
| $d_k$ | implementation duration |
| $\tau_k$ | trigger time |
| $T_H$ | planning horizon |

An intervention becomes active at

```math
t_k^{\rm active}=t_k+\ell_k.
```

Stage 3 is multiscale in physical/process dynamics; Stage 7 is multiscale in strategic decision and implementation time.

The future action set is path dependent:

```math
\mathcal A_{k+1}
=
\mathcal A\!\left(
\mathfrak M_{k+1},
\mathcal H_{t_{k+1}}
\right).
```

In general, transformation order need not commute:

```math
\mathcal T_{\mathbf a_2}\circ\mathcal T_{\mathbf a_1}
\neq
\mathcal T_{\mathbf a_1}\circ\mathcal T_{\mathbf a_2}.
```

Thus **order matters** whenever one intervention changes the feasibility or value of later interventions.

---

## 9. Transformation-edge object `[P]`

Each meta-graph edge may be represented as

```math
e_{k\ell}
=
\left(
\mathbf a_{k\ell},
C_{k\ell},
L_{k\ell},
D_{k\ell},
R_{k\ell},
\chi_{k\ell},
\mathcal Z_{k\ell}
\right).
```

| Term | Meaning |
|---|---|
| $C_{k\ell}$ | life-cycle / transition cost |
| $L_{k\ell}$ | lead time |
| $D_{k\ell}$ | implementation duration |
| $R_{k\ell}$ | resource requirement |
| $\chi_{k\ell}$ | reversibility, flexibility and lock-in information |
| $\mathcal Z_{k\ell}$ | trigger region / activation condition |

This representation captures the real-options insight that deferrable, expandable, switchable or reversible interventions can have different value from irreversible commitments under uncertainty (Buurman & Babovic, 2016).

---

## 10. Feasible transformation set

A strategic action is admissible only if it lies in the intersection

```math
\begin{aligned}
\mathcal A_k^{\rm feas}
={}&
\mathcal A_k^{\rm tech}
\cap\mathcal A_k^{\rm budget}
\cap\mathcal A_k^{I}
\cap\mathcal A_k^{O}\\
&\cap\mathcal A_k^{\rm sus}
\cap\mathcal A_k^{\rm equity}
\cap\mathcal A_k^{\rm temporal}.
\end{aligned}
```

Hence

```math
\mathbf a_k\in\mathcal A_k^{\rm feas}.
```

Representative constraints include

```math
\sum_i C_i x_{ik}\le B_k
```

for budget,

```math
x_j\le x_i
```

for precedence when intervention $j$ requires intervention $i$, and

```math
t_j\ge t_i+d_i+\ell_i
```

for a declared sequential timing relation. Organizational and information feasibility remain explicit rather than assuming unlimited implementation capacity.

---

## 11. Viability as a pathway constraint

Each candidate future regime is reevaluated using Stage 5:

```math
\mathcal V_{\rm sus}^{u,T}(\mathfrak M_k).
```

Where continuous controlled viability is required over a declared transformation interval,

```math
Y(t)\in K_{{\rm sus},k}(t)
```

and the relevant trajectory should remain within the corresponding controlled viable set over the required horizon.

This does not imply that all transformation problems must forbid temporary constraint excursion. If temporary violation is scientifically allowed, the recovery/capture formulation must be declared explicitly rather than silently replacing viability.

---

## 12. Sustainable future as a target set `[P]`

Stage 7 does not target one unique final state. Define the candidate sustainable-regime set

```math
\mathbb M_{\rm sus}
=
\left\{
\mathfrak M:
\begin{array}{l}
\text{declared resilience, sustainability, equity,}\\
\text{and feasibility conditions are satisfied}
\end{array}
\right\}.
```

The Stage-7 reachability question is

```math
(\mathfrak M_0,Y_0)
\overset{\boldsymbol\pi_{\rm ST}}{\longrightarrow}
\mathbb M_{\rm sus}.
```

This is the thesis interpretation of **reachability in infrastructure-regime space** `[P]`.

---

## 13. Many-objective pathway evaluation

Do not hide conflicting objectives inside arbitrary weights before the trade-offs are understood. Use the objective vector

```math
\mathbf J(\Pi,\omega)
=
\begin{bmatrix}
J_{\rm risk}\\
J_{\rm service}\\
J_{\rm cost}\\
J_{\rm carbon}\\
J_{\rm inequity}\\
J_{\rm time}\\
J_{\rm flexibility}
\end{bmatrix},
\qquad
\omega\in\Omega.
```

| Objective | Preferred direction before normalization |
|---|---|
| $J_{\rm risk}$ | minimize |
| $J_{\rm service}$ | maximize |
| $J_{\rm cost}$ | minimize |
| $J_{\rm carbon}$ | minimize |
| $J_{\rm inequity}$ | minimize |
| $J_{\rm time}$ | minimize |
| $J_{\rm flexibility}$ | maximize |

Any Pareto computation must normalize or orient the objectives consistently before dominance is evaluated.

Under deep uncertainty, `RobustPareto` is used as a **thesis shorthand `[P]`** for nondominated pathways under a declared robustness rule and scenario set; it is not assumed to be a universal mathematical operator.

---

## 14. Uncertainty regimes remain distinct

Stage 7 preserves three different interpretations:

```math
\xi\sim P
```

for ordinary probabilistic uncertainty,

```math
P\in\mathcal P
```

for distributional ambiguity, and

```math
\omega\in\Omega
```

for deep uncertainty represented by plausible futures.

Scenario fractions under $\Omega$ must not be described as probabilities unless scenario probabilities or justified weights have actually been defined.

The methodological combination is therefore

```math
\text{adaptive pathways}
+
\text{robust decision analysis}
+
\text{many-objective search},
```

with real-options valuation added only where monetizable flexibility assumptions are defensible.

---

## 15. Topology is a design variable, not the resilience objective

The literature does not support a universal rule such as

```math
|E|\uparrow
\quad\Rightarrow\quad
\text{resilience}\uparrow.
```

Nor does maximizing one graph statistic automatically maximize infrastructure resilience. Coupling can amplify cascades, create redundancy, enable substitution or generate new dependencies depending on mechanism and dynamics (Buldyrev et al., 2010; Gates & Rocha, 2016; Kaiser et al., 2021).

Every structural candidate must therefore be replayed through the physical and decision layers:

```math
\mathbf a_k
\rightarrow
\mathfrak M_{k+1}
\rightarrow
F_{\mathfrak M_{k+1}}
\rightarrow
Y(t)
\rightarrow
\mathcal V_{\rm sus}^{u,T}
\rightarrow
\mathbf J.
```

---

## 16. Frozen Stage-7 fundamental object

The canonical Stage-7 object is

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

| Component | Role |
|---|---|
| $\mathbb G_{\rm ST}$ | graph of possible P–T–I–O regimes |
| $\boldsymbol\pi_{\rm ST}$ | adaptive transformation policy |
| $\Omega$ | plausible future conditions |
| $\mathcal A^{\rm feas}$ | feasible strategic transformation actions |
| $\mathbf J$ | many-objective evaluation |
| $\mathbb M_{\rm sus}$ | acceptable sustainable future-regime set |

A realized pathway under policy $\boldsymbol\pi_{\rm ST}$ and future $\omega$ is

```math
\Pi_{\boldsymbol\pi_{\rm ST},\omega}
=
\left[
(\mathfrak M_0,\mathbf a_0,\tau_0),
(\mathfrak M_1,\mathbf a_1,\tau_1),
\ldots,
\mathfrak M_N
\right].
```

The frozen interpretation is:

> **Stage 7 is an adaptive, viability-constrained, many-objective reachability problem over a graph of evolving P–T–I–O infrastructure regimes.**

---

## 17. Candidate optimization statement `[P]`

A compact implementation target is

```math
\begin{aligned}
\text{find}\quad
&\boldsymbol\pi_{\rm ST}\\
\text{to obtain}\quad
&\text{robustly nondominated }\mathbf J
\text{ across }\omega\in\Omega\\
\text{subject to}\quad
&\mathfrak M_{k+1}
 =\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k),\\
&\mathbf a_k
 =\pi_k^{\rm ST}(\widehat X_k,z_{I,k},z_{O,k},\mathfrak M_k,\mathcal H_k),\\
&\mathbf a_k\in\mathcal A_k^{\rm feas},\\
&\text{declared Stage-5 viability/recovery conditions},\\
&\text{budget, resource, precedence and lead-time constraints},\\
&\mathfrak M_N\in\mathbb M_{\rm sus}.
\end{aligned}
```

This formulation is `[P]`: it synthesizes established multilayer-network, viability, adaptive-pathway, robust-decision, organizational-resilience and many-objective methods into the thesis architecture.

---

## 18. Relationship to every previous stage

| Stage | Frozen input to Stage 7 | Stage-7 use |
|---|---|---|
| **1 — Multilayer Structure** | $\mathcal S=\{P,T,I,O\}$ | transforms subsystem/layer architecture without redefining ontology |
| **2 — Causal Mechanisms** | $\mathfrak I_{ij}^{\alpha\beta}$ | redesigns selected dependency strength, delay, activation or mechanism |
| **3 — Coupled Hybrid Multiscale Dynamics** | $F^m,\mathcal G(t),Y(t)$ | dynamically tests every candidate future regime |
| **4 — Observation, Organization, Feedback and Control** | $\widehat X,z_I,z_O,\mathcal U,u$ | supplies observability, triggers and implementation feasibility |
| **5 — Controlled Sustainable Viability** | $K_{\rm sus},\mathcal V,\rho,T_{\mathcal V},T_K$ | evaluates maintainability and pathway constraints |
| **6 — Resilience-to-Sustainability Transition** | $(c_6,\mathcal D_6,\boldsymbol\zeta_T)$ | specifies why/what/how-deep change must be |
| **7 — Sustainable Transformation Pathways** | $\mathfrak P_{\rm ST}$ | generates and compares adaptive transformation pathways |

---

## 19. Seven-stage validation loop

A Stage-7 candidate is not accepted from topology or cost alone. It is replayed through the upstream framework:

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

This is a validation loop around the frozen stages; it does not reorder or replace them.

---

## 20. Evidence status

| Object / concept | Status |
|---|---|
| Multilayer/network-of-networks representation | `[E]` |
| Adaptive pathways / DAPP | `[E]` |
| Robust decision making | `[E]` |
| Many-objective optimization | `[E]` |
| Real options / flexibility | `[E]` |
| Viability constraints | `[E]` |
| Path dependence | `[E]` |
| Topology–dynamics interaction | `[E]` |
| $\mathfrak M_k$ unified P–T–I–O regime | `[P]` |
| $\mathbb G_{\rm ST}$ graph of alternative infrastructure regimes | `[P]` |
| $\mathbf a_k$ explicit cross-layer transformation vector | `[P]` |
| $\mathcal T_{\mathbf a_k}$ transformation operator | `[P]` |
| $\mathfrak P_{\rm ST}$ complete Stage-7 object | `[P]` |
| Seven-stage validation loop | `[D/P]` |
| Robust-Pareto architecture-space reachability formulation | `[P]` |

Freezing Stage 7 freezes these definitions and evidence labels; it does **not** convert `[P]` constructs into validated scientific results.

---

## 21. Final frozen Stage-7 scope

| Item | Canonical specification |
|---|---|
| **Stage** | Sustainable Transformation Pathways |
| **Question** | What sequence of interventions leads to a more resilient, equitable and sustainable future system? |
| **Input** | $(c_6,\mathcal D_6,\boldsymbol\zeta_T)$ |
| **Current regime** | $\mathfrak M_0$ |
| **Transformation graph** | $\mathbb G_{\rm ST}$ |
| **Strategic intervention** | $\mathbf a_k=[a_k^P,a_k^T,a_k^I,a_k^O,a_k^{\mathfrak I}]^\top$ |
| **Transformation** | $\mathfrak M_{k+1}=\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k)$ |
| **Adaptive policy** | $\boldsymbol\pi_{\rm ST}$ |
| **Trigger** | $\tau_j=\inf\{t:s_j(t)\in\mathcal Z_j\}$ |
| **Feasibility** | technical + budget + information + organization + sustainability + equity + temporal |
| **Uncertainty** | probability, ambiguity or deep-uncertainty scenarios kept distinct |
| **Viability** | candidate regimes reevaluated through Stage 5 |
| **Objectives** | risk, service, cost, carbon, inequity, time and flexibility |
| **Target** | $\mathfrak M_N\in\mathbb M_{\rm sus}$ |
| **Fundamental object** | $\mathfrak P_{\rm ST}$ |
| **Validation** | every candidate replayed through Stages 1–6 |

> **STAGE 7 SCIENTIFIC SCOPE: FROZEN**

The complete conceptual framework is now closed. The next scientific phase is operationalization, numerical case-study design, falsification and validation—not redesign of the seven-stage framework.

---

## Core APA 7 references

Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. https://doi.org/10.1002/2017EF000660

Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., & Havlin, S. (2010). Catastrophic cascade of failures in interdependent networks. *Nature, 464*, 1025–1028. https://doi.org/10.1038/nature08932

Buurman, J., & Babovic, V. (2016). Adaptation pathways and real options analysis: An approach to deep uncertainty in climate change adaptation policies. *Policy and Society, 35*(2), 137–150. https://doi.org/10.1016/j.polsoc.2016.05.002

De Domenico, M., Solé-Ribalta, A., Cozzo, E., Kivelä, M., Moreno, Y., Porter, M. A., Gómez, S., & Arenas, A. (2013). Mathematical formulation of multilayer networks. *Physical Review X, 3*(4), 041022. https://doi.org/10.1103/PhysRevX.3.041022

Doyen, L., & Gajardo, P. (2020). Sustainability standards, multicriteria maximin, and viability. *Natural Resource Modeling, 33*(3), e12250. https://doi.org/10.1111/nrm.12250

Gates, A. J., & Rocha, L. M. (2016). Control of complex networks requires both structure and dynamics. *Scientific Reports, 6*, 24456. https://doi.org/10.1038/srep24456

Haasnoot, M., Kwakkel, J. H., Walker, W. E., & ter Maat, J. (2013). Dynamic adaptive policy pathways: A method for crafting robust decisions for a deeply uncertain world. *Global Environmental Change, 23*(2), 485–498. https://doi.org/10.1016/j.gloenvcha.2012.12.006

Hadka, D., Herman, J., Reed, P. M., & Keller, K. (2015). An open source framework for many-objective robust decision making. *Environmental Modelling & Software, 74*, 114–129. https://doi.org/10.1016/j.envsoft.2015.07.014

Kaiser, F., Latora, V., & Witthaut, D. (2021). Network isolators inhibit failure spreading in complex networks. *Nature Communications, 12*, 3143. https://doi.org/10.1038/s41467-021-23292-9

Li, Q., Dong, S., & Mostafavi, A. (2019). Modeling of inter-organizational coordination dynamics in resilience planning of infrastructure systems: A multilayer network simulation framework. *PLOS ONE, 14*(11), e0224522. https://doi.org/10.1371/journal.pone.0224522

