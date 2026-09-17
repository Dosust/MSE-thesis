# Stage 7 — Sustainable Transformation Pathways: Deep Research Synthesis

![Stage](https://img.shields.io/badge/Stage%207-DEEP%20RESEARCH-9A6700)
![Status](https://img.shields.io/badge/scope-NOT%20FROZEN-6B7280)
![Evidence](https://img.shields.io/badge/evidence-10%20passes%20%7C%2050%20paper%20set-0969DA)

**Framework stage:** Stage 7 — Sustainable Transformation Pathways  
**Status:** DEEP RESEARCH COMPLETE / CANDIDATE SCOPE / **NOT FROZEN**  
**Date:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Research protocol:** ten analytical passes using a 50-paper interdisciplinary evidence set, cross-checked against current work on adaptive pathways, deep uncertainty, real options, sustainability transitions, infrastructure planning, equity and network transformation  
**Change rule:** The equations and objects in this file remain candidate Stage-7 constructs until an explicit freeze is approved.

> **Evidence notation:** `[E]` = established literature/theory; `[D]` = derived synthesis; `[P]` = proposed thesis construct requiring validation.

> **Stage boundary:** Stage 6 is frozen and provides $(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)$. Stage 7 must determine admissible interventions, sequence, timing/trigger conditions and pathway robustness. It must not reopen the Stage-6 diagnosis.

---

## RQ7 / SO7 — current canonical question

> **What should be changed, where, when and in what sequence to achieve effective, efficient and sustainable infrastructure transformation under feasibility constraints and uncertainty?**

**Specific objective:** Evaluate candidate infrastructure transformations and, where justified, intervention sequences using effectiveness, efficiency, sustainability, feasibility and uncertainty to support engineering decisions.

**Interpretation boundary:** Framework v2 and intervention-performance amendment v2.1 supersede conflicting legacy mathematics or scope below. The current RQ heading does not validate or promote legacy constructions.

**Question authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`. This 2026-09-17 wording amendment aligns the question with Chapter I; technical results and validation status are unchanged.

The Stage-6 → Stage-7 handoff is

```math
\underbrace{(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)}_{\text{Stage-6 diagnosis}}
\rightarrow
\underbrace{\text{candidate interventions}}_{\text{Stage 7}}
\rightarrow
\underbrace{\text{conditional sequencing}}_{\text{Stage 7}}
\rightarrow
\underbrace{\text{future P--T--I--O regimes}}_{\text{Stage-7 output}}.
```

The full framework is therefore provisionally represented as

```math
\{P,T,I,O\}
\rightarrow
\mathfrak I
\rightarrow
F
\rightarrow
u
\rightarrow
\mathcal V
\rightarrow
\Phi_{\mathrm{ST}}
\rightarrow
\text{Transformation Pathway}.
```

The scientific question of this research file is whether the final term should be a fixed sequence, an adaptive policy, a pathway graph, a robust Pareto set, or some combination.

---

## 1. Ten analytical passes

| Pass | Research focus | Representative strong sources | Main result for Stage 7 |
|---:|---|---|---|
| **1** | Adaptive pathways and sequencing | Haasnoot et al. (2013); Kwadijk et al. (2010); Werners et al. (2015, 2021); van der Pas et al. (2013) | A pathway is a sequence of actions whose continuation depends on changing conditions. Timing is often better represented by adaptation/decision points than by fixed calendar dates. |
| **2** | Dynamic Adaptive Policy Pathways | Haasnoot et al. (2013); Kwakkel et al. (2016); Haasnoot et al. (2024); Hamarat et al. (2013); Marchau et al. (2019) | DAPP joins near-term action, alternative future branches, monitoring and signposts. Stage 7 should retain branches and trigger conditions rather than commit to one deterministic future. |
| **3** | Multi-stage decision making under uncertainty | Lempert & Groves (2010); Hamarat et al. (2013); Hadka et al. (2015); Asadabadi & Miller-Hooks (2017); Marchau et al. (2019) | Early actions change later feasible decisions. Stage 7 therefore requires state-dependent multistage decisions and explicit path dependence. |
| **4** | Infrastructure investment timing | de Neufville et al. (2006, 2008); Asadabadi & Miller-Hooks (2017); Martello et al. (2024); Kaya et al. (2025) | Deferral, staging, expansion and irreversible commitment have engineering value. Lead time and asset lifetime must appear on pathway transitions. |
| **5** | Real options and flexibility | Buurman & Babovic (2016); Kim et al. (2017); Manocha & Babovic (2018); Martello et al. (2024); de Neufville et al. (2006) | Flexibility is an option with value, but real-options valuation is complementary to robust decision analysis; it should not force probabilistic assumptions where deep uncertainty prevents them. |
| **6** | Multi-objective optimization | Hadka et al. (2015); Doyen & Gajardo (2020); Manocha & Babovic (2018); Lin et al. (2025); Zhang et al. (2023) | Resilience, cost, environmental performance, equity and flexibility are not safely collapsed into one arbitrary weighted score. Candidate pathways should be explored through Pareto trade-offs and satisficing constraints. |
| **7** | Robust decision making | Lempert & Groves (2010); Kwakkel et al. (2016); Hadka et al. (2015); Marchau et al. (2019); Dittrich et al. (2016) | Robustness asks which strategies perform acceptably across many plausible futures. Scenario discovery can reveal conditions under which a pathway fails and should switch. |
| **8** | Transition pathways and socio-technical change | Geels (2002); Geels & Schot (2007); Verbong & Geels (2010); Loorbach et al. (2017); Kaya et al. (2025) | Infrastructure is both a constraint on and an object of transition. Pathways can reconfigure technology, institutions and inter-system relations, not merely add assets. |
| **9** | Equity, sustainability and feasibility constraints | Doyen & Gajardo (2020); McCauley & Heffron (2018); Zhang et al. (2023); Lin et al. (2025); Béné & Doyen (2018) | Equity and sustainability must remain explicit constraints/objectives. Different equity metrics can produce different intervention priorities; organizational and resource feasibility must remain explicit. |
| **10** | Formal P–T–I–O pathway synthesis | De Domenico et al. (2013); Korkali et al. (2017); Goldbeck et al. (2019); Li et al. (2019); Xu & Chopra (2023); Danziger & Barabási (2022) | A Stage-7 intervention changes the system to be operated. Every transformed P–T–I–O regime must therefore be re-evaluated through causality, dynamics, control and viability rather than judged by topology alone. |

### Research synthesis

The evidence supports five central conclusions.

1. **A fixed schedule is too weak as the fundamental object under deep uncertainty.** A realized branch may be written as $[(a_1,t_1),\ldots,(a_N,t_N)]$, but the framework should retain alternative branches and trigger conditions `[D/P]`.
2. **The best immediate intervention need not generate the best long-run pathway.** Early infrastructure actions change future options, costs, lock-in and feasible transitions `[E/D]`.
3. **Flexibility has value.** Deferral, expansion, switching, staging and abandonment can be represented explicitly where their physical/economic meaning is defensible `[E]`.
4. **There is no universal single objective called sustainability-resilience.** The pathway must preserve multiple performance dimensions and threshold constraints `[E/D]`.
5. **A transformed topology is not validated until its dynamics and viability are retested.** Graph structure is a design variable, not a substitute for physics, information, organization and control `[E/D]`.

---

## 2. Correction to the provisional deterministic pathway

The provisional representation

```math
\Pi
=
[(a_1,t_1),(a_2,t_2),\ldots,(a_N,t_N)]
```

is useful for describing **one realized intervention sequence**, but the literature does not support using it as the only Stage-7 object when the future is deeply uncertain.

Dynamic Adaptive Policy Pathways and robust decision methods retain future alternatives and switch decisions when monitored conditions indicate that the current path will no longer meet objectives (Haasnoot et al., 2013; Kwakkel et al., 2016; Lempert & Groves, 2010; Werners et al., 2021).

The stronger candidate is therefore an **adaptive transformation pathway graph** `[P]`.

---

## 3. Candidate infrastructure-regime representation

Let an admissible infrastructure regime be

```math
\mathfrak M_k
=
(\mathcal S_k,\mathbb G_k,\mathfrak I_k,F_k,\Theta_k,K_{\mathrm{sus},k},\mathcal U_k).
```

Here $\mathbb G_k$ denotes the multilayer/network-of-networks structure of the P–T–I–O regime. One possible representation is

```math
\mathbb G_k
=
(\{\mathcal G_k^\ell\}_{\ell\in\{P,T,I,O\}},
\mathcal E_k^{\times},W_k^{\times}),
```

where $\mathcal E_k^{\times}$ and $W_k^{\times}$ encode interlayer connections and weights. This topology representation does **not** replace the Stage-2 causal object $\mathfrak I_{ij}^{\alpha\beta}$.

A candidate meta-topology is

```math
\mathcal G_{\Pi}
=
(\{\mathfrak M_k\},\mathcal E_{\Pi}),
```

where each node is an entire possible P–T–I–O infrastructure regime and each edge is an admissible structural transition.

This “graph of alternative regimes” is a proposed thesis synthesis `[P]`, not established infrastructure terminology.

---

## 4. Candidate transformation actions

Stage 7 must distinguish strategic transformation actions from Stage-4 operational control. Stage 4 uses $u(t)$ to **operate the current system**. Stage 7 considers actions $a_k$ that **change the system that will subsequently be operated**.

A candidate action family is

```math
\mathcal A_7
=
\mathcal A_P
\cup\mathcal A_T
\cup\mathcal A_I
\cup\mathcal A_O
\cup\mathcal A_{\mathfrak I}.
```

Examples include structural redundancy, DER/storage or traction-power redesign in $P$; multimodal/corridor/accessibility redesign in $T$; sensing/communication/information redundancy in $I$; persistent authority, coordination and resource-sharing changes in $O$; and modification, reduction, redundancy or selective autonomy of critical interdependencies through $\mathcal A_{\mathfrak I}$.

The regime transition is provisionally

```math
\mathfrak M_{k+1}
=
\mathcal T_{a_k}(\mathfrak M_k).
```

Every action must be traceable to one or more Stage-6 requirements in $\mathcal D_6$ and to the required transformation character $\boldsymbol{\zeta}_T$.

---

## 5. Candidate adaptive pathway object

The strongest candidate fundamental object emerging from the research is

```math
\mathscr P_7
=
(\mathcal M_7,\mathcal A_7,\mathcal E_7,\mathcal Z_7,\Omega),
```

where

| Object | Candidate meaning |
|---|---|
| $\mathcal M_7$ | admissible future infrastructure regimes $\{\mathfrak M_0,\mathfrak M_1,\ldots\}$ |
| $\mathcal A_7$ | candidate structural/strategic interventions |
| $\mathcal E_7$ | feasible regime transitions |
| $\mathcal Z_7$ | monitoring/trigger regions for pathway switching |
| $\Omega$ | plausible future scenarios / states of the world |

This five-part object is `[P]`. DAPP/RDM/real-options literature supports the ingredients, not this exact P–T–I–O mathematical object.

A realized pathway remains a path through $\mathscr P_7$.

---

## 6. Trigger-dependent timing

A candidate Stage-7 monitoring state is

```math
z_7(t)
=
[\mathcal R_5(t),\mathbf d_6(t),\Lambda_{\mathrm{LT}}(t),\widehat\xi(t)]^	op,
```

where $\widehat\xi(t)$ denotes updated information about relevant external futures.

For pathway edge $e$, define a trigger region

```math
\mathcal Z_e
=
\{z_7:g_e(z_7)\ge0\},
```

with activation time

```math
\tau_e
=
\inf\{t\ge t_k:z_7(t)\in\mathcal Z_e\}.
```

These equations are `[P]` formalizations of the monitoring-and-trigger logic in adaptive-pathway research.

This changes the preferred representation from

```math
a_1@t_1\rightarrow a_2@t_2\rightarrow a_3@t_3
```

to a conditional structure such as

```math
\mathfrak M_0
\xrightarrow[\mathcal Z_1]{a_1}
\mathfrak M_1
\begin{cases}
\xrightarrow[\mathcal Z_2]{a_2}\mathfrak M_2,\\
\xrightarrow[\mathcal Z_3]{a_3}\mathfrak M_3.
\end{cases}
```

**Candidate conclusion:** Stage 7 should produce a **pathway map**, not only one predetermined pathway.

---

## 7. Sequencing, lead-time and compatibility constraints

Precedence and implementation lead time can be represented as

```math
a_i\prec a_j
\quad\Rightarrow\quad
t_j\ge t_i+L_i,
```

where $L_i$ is the implementation lead time of intervention $a_i$.

For mutually incompatible binary actions,

```math
x_i+x_j\le1.
```

A candidate transition edge should carry more than an intervention label:

```math
e_{kl}
=
(a_{kl},\mathcal Z_{kl},L_{kl},C_{kl},R_{kl},\chi_{kl},\ell_{kl}),
```

where $C_{kl}$ is life-cycle/transition cost, $R_{kl}$ resource requirement, $\chi_{kl}$ flexibility/reversibility information and $\ell_{kl}$ lock-in/path-dependence information.

This is `[P]`, motivated by infrastructure investment timing and real-options evidence.

---

## 8. Feasibility constraints

A pathway cannot be selected from technical merit alone. A candidate Stage-7 action must satisfy

```math
a_k
\in
\mathcal A_{\mathrm{feas}}
(\mathfrak M_k,z_I(t),z_O(t),B_k),
```

where $B_k$ denotes the relevant budget/resource envelope.

The feasibility architecture should preserve at least:

```math
\begin{aligned}
&\text{technical/physical feasibility}\\
&\land\ \text{budget and resource feasibility}\\
&\land\ \text{informational feasibility}\\
&\land\ \text{organizational/governance feasibility}\\
&\land\ \text{sustainability requirements}\\
&\land\ \text{equity/justice requirements}\\
&\land\ \text{robustness under uncertainty}.
\end{aligned}
```

These constraints directly answer the user's provisional Stage-7 specification while retaining the P–T–I–O ontology.

---

## 9. Multi-objective pathway evaluation

The research argues against prematurely collapsing all criteria into one scalar objective. A candidate objective vector is

```math
\mathbf J_7(\Pi,\omega)
=
\begin{bmatrix}
J_{\mathrm{viability}}\\
J_{\mathrm{service}}\\
C_{\mathrm{life}}\\
E_{\mathrm{env}}\\
D_{\mathrm{equity}}\\
L_{\mathrm{lock}}\\
J_{\mathrm{flexibility}}
\end{bmatrix},
\qquad \omega\in\Omega.
```

The signs/scales must be declared consistently. The components represent viability performance, service performance, life-cycle cost, environmental burden, distributional equity/disparity, lock-in burden and future flexibility.

This exact vector is `[P]`; the need to preserve conflicting objectives and trade-offs is `[E]`.

A candidate robust satisficing measure is

```math
R_{\mathrm{sat}}(\Pi)
=
\frac{1}{|\Omega|}
\sum_{\omega\in\Omega}
\mathbf 1[\mathbf J_7(\Pi,\omega)\preceq\mathbf b].
```

$R_{\mathrm{sat}}$ is not a probability unless the scenario set and weights have a justified probabilistic interpretation.

The preferred candidate output is therefore a robust Pareto set rather than an asserted universal optimum:

```math
\mathcal P_7^\star
=
\operatorname{ParetoRobust}
(\mathcal P_{\mathrm{feas}},\Omega,\mathbf J_7).
```

---

## 10. P–T–I–O transformation validation loop

A Stage-7 intervention is not accepted merely because it improves one network statistic or one cost metric. Every transformed regime must be re-evaluated through the upstream framework:

```math
\begin{aligned}
\text{Stage-7 intervention}
&\rightarrow\text{changed Stage-1 structure}\\
&\rightarrow\text{changed Stage-2 causal interdependencies}\\
&\rightarrow\text{Stage-3 hybrid/multiscale dynamics}\\
&\rightarrow\text{Stage-4 observation, organization and control feasibility}\\
&\rightarrow\text{Stage-5 controlled sustainable viability}\\
&\rightarrow\text{Stage-6 adequacy/transition diagnosis}.
\end{aligned}
```

A candidate pathway transition should remain admissible only if it satisfies

```math
\begin{aligned}
&\text{topological feasibility}
\land\text{physical/dynamical feasibility}
\land\text{information feasibility}\\
&\land\text{organizational feasibility}
\land\text{controlled viability}
\land\text{Stage-6 requirement satisfaction}\\
&\land\text{robustness across plausible futures}
\land\text{sustainability/equity acceptability}.
\end{aligned}
```

Counterfactual pathway ablation should later test whether removing, postponing or replacing an intervention materially changes cascade behaviour, controlled viability, sustainability requirements or equity outcomes.

---

## 11. Network/topology caution

The network-science evidence gives a strong negative result:

> **There is no universal topology that can be called “the most resilient topology” independent of mechanisms, dynamics, objectives and scenarios.**

Increased coupling can either amplify cascades or create beneficial redundancy; partial autonomy can improve robustness; intermediate coupling can be optimal; and topological controllability does not guarantee physically affordable control (Buldyrev et al., 2010; Gates & Rocha, 2016; Korkali et al., 2017; Radicchi & Bianconi, 2017; Tejedor et al., 2018).

Therefore, Stage 7 should not optimize topology in isolation. It should optimize or compare **system behaviour produced jointly by topology, physics, information and organization**.

Higher-order/simplicial representations should remain optional. They are justified only when the mechanism is genuinely irreducible to pairwise relations, not merely because the system has multiple layers.

---

## 12. Candidate Stage-7 scope emerging from research — NOT FROZEN

| Item | Candidate specification |
|---|---|
| **Stage** | Sustainable Transformation Pathways |
| **Research question** | What should be changed, where, when and in what sequence to achieve effective, efficient and sustainable infrastructure transformation under feasibility constraints and uncertainty? |
| **Primary Stage-6 input** | $(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)$ |
| **Current regime** | $\mathfrak M_0$ |
| **Candidate actions** | $\mathcal A_7=\mathcal A_P\cup\mathcal A_T\cup\mathcal A_I\cup\mathcal A_O\cup\mathcal A_{\mathfrak I}$ |
| **Transformation map** | $\mathfrak M_{k+1}=\mathcal T_{a_k}(\mathfrak M_k)$ |
| **Candidate pathway object** | $\mathscr P_7=(\mathcal M_7,\mathcal A_7,\mathcal E_7,\mathcal Z_7,\Omega)$ |
| **Timing** | calendar windows plus state/threshold triggers $\mathcal Z_e$ where appropriate |
| **Sequencing** | precedence, compatibility, lead-time and construction constraints |
| **Feasibility** | technical + budget/resource + information + organization + sustainability + equity |
| **Uncertainty** | plausible futures $\Omega$, scenario discovery and adaptive updating |
| **Decision principle** | many-objective robust/Pareto comparison; real options where monetizable flexibility is defensible |
| **Validation** | re-evaluate transformed regimes through Stages 2–6 |
| **Candidate output** | robust set/map of conditional transformation pathways, initial actions, branches, triggers, monitoring variables and future regimes |

### Candidate mathematical interpretation

A realized pathway may still be written as

```math
\Pi_{\omega}
=
[(a_1,t_1),(a_2,t_2),\ldots,(a_N,t_N)],
```

but the stronger Stage-7 research hypothesis is that the **fundamental planning object** should be the conditional pathway graph $\mathscr P_7$, from which the realized sequence $\Pi_{\omega}$ emerges as uncertainty resolves.

This is the central proposition to scrutinize before Stage 7 is frozen.

> **STAGE 7 STATUS: DEEP RESEARCH COMPLETE; CANDIDATE SCOPE DEFINED; NOT FROZEN.**

---

## 13. What remains before freeze

Before an explicit Stage-7 freeze, the framework should still verify:

| Open decision | Required check |
|---|---|
| Fundamental object | Is $\mathscr P_7$ preferable to a simpler sequence/policy representation for this thesis? |
| Regime definition | Is $\mathfrak M_k$ sufficiently precise without duplicating Stages 1–6? |
| Action granularity | Which structural actions belong to $P,T,I,O,\mathfrak I$ and which are only Stage-4 controls? |
| Trigger design | Which Stage-5/6 quantities can legitimately serve as monitoring signposts? |
| Objective set | Which objectives are indispensable and which are case-specific? |
| Equity formalism | Which equity metric(s) are defensible for P–T service and investment distribution? |
| Uncertainty representation | Scenarios, probability, robust uncertainty sets, or hybrid treatment? |
| Real-options role | Which interventions have genuine defer/expand/switch/abandon option value? |
| Validation | What counterfactual and pathway-ablation tests constitute falsification? |
| Computational representation | Path search, multistage optimization, DAPP/RDM workflow, or combined architecture? |

Only after those decisions are explicitly accepted should the complete seven-stage framework be frozen.

---

## Selected APA 7 reference base

Asadabadi, A., & Miller-Hooks, E. (2017). Optimal transportation and shoreline infrastructure investment planning under a stochastic climate future. *Transportation Research Part B: Methodological, 100*, 156–174.

Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. https://doi.org/10.1002/2017EF000660

Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., & Havlin, S. (2010). Catastrophic cascade of failures in interdependent networks. *Nature, 464*, 1025–1028. https://doi.org/10.1038/nature08932

Buurman, J., & Babovic, V. (2016). Adaptation pathways and real options analysis: An approach to deep uncertainty in climate change adaptation policies. *Policy and Society, 35*(2), 137–150. https://doi.org/10.1016/j.polsoc.2016.05.002

Danziger, M. M., & Barabási, A.-L. (2022). Recovery coupling in multilayer networks. *Nature Communications, 13*, 955. https://doi.org/10.1038/s41467-022-28379-5

De Domenico, M., Solé-Ribalta, A., Cozzo, E., Kivelä, M., Moreno, Y., Porter, M. A., Gómez, S., & Arenas, A. (2013). Mathematical formulation of multilayer networks. *Physical Review X, 3*(4), 041022. https://doi.org/10.1103/PhysRevX.3.041022

Dittrich, R., Wreford, A., & Moran, D. (2016). A survey of decision-making approaches for climate change adaptation: Are robust methods the way forward? *Ecological Economics, 122*, 79–89. https://doi.org/10.1016/j.ecolecon.2015.12.006

de Neufville, R., Scholtes, S., & Wang, T. (2006). Real options by spreadsheet: Parking garage case example. *Journal of Infrastructure Systems, 12*(2), 107–111. https://doi.org/10.1061/(ASCE)1076-0342(2006)12:2(107)

Doyen, L., & Gajardo, P. (2020). Sustainability standards, multicriteria maximin, and viability. *Natural Resource Modeling, 33*(3), e12250. https://doi.org/10.1111/nrm.12250

Gates, A. J., & Rocha, L. M. (2016). Control of complex networks requires both structure and dynamics. *Scientific Reports, 6*, 24456. https://doi.org/10.1038/srep24456

Geels, F. W. (2002). Technological transitions as evolutionary reconfiguration processes: A multi-level perspective and a case-study. *Research Policy, 31*(8–9), 1257–1274. https://doi.org/10.1016/S0048-7333(02)00062-8

Geels, F. W., & Schot, J. (2007). Typology of sociotechnical transition pathways. *Research Policy, 36*(3), 399–417. https://doi.org/10.1016/j.respol.2007.01.003

Goldbeck, N., Angeloudis, P., & Ochieng, W. Y. (2019). Resilience assessment for interdependent urban infrastructure systems using dynamic network flow models. *Reliability Engineering & System Safety, 188*, 62–79. https://doi.org/10.1016/j.ress.2019.03.007

Haasnoot, M., Kwakkel, J. H., Walker, W. E., & ter Maat, J. (2013). Dynamic adaptive policy pathways: A method for crafting robust decisions for a deeply uncertain world. *Global Environmental Change, 23*(2), 485–498. https://doi.org/10.1016/j.gloenvcha.2012.12.006

Hadka, D., Herman, J., Reed, P. M., & Keller, K. (2015). An open source framework for many-objective robust decision making. *Environmental Modelling & Software, 74*, 114–129. https://doi.org/10.1016/j.envsoft.2015.07.014

Hamarat, C., Kwakkel, J. H., & Pruyt, E. (2013). Adaptive robust design under deep uncertainty. *Technological Forecasting and Social Change, 80*(3), 408–418. https://doi.org/10.1016/j.techfore.2012.10.004

Kaya, H. D., Chan, P. W. C., Schraven, D. F. J., & Leijten, M. (2025). Infrastructure in transitions: A systematic review of how infrastructure influences and is influenced by sustainability transitions. *Environmental Innovation and Societal Transitions, 57*, 101034. https://doi.org/10.1016/j.eist.2025.101034

Kim, K., Ha, S., & Kim, H. (2017). Using real options for urban infrastructure adaptation under climate change. *Journal of Cleaner Production, 143*, 40–50. https://doi.org/10.1016/j.jclepro.2016.12.152

Korkali, M., Veneman, J. G., Tivnan, B. F., Bagrow, J. P., & Hines, P. D. H. (2017). Reducing cascading failure risk by increasing infrastructure network interdependence. *Scientific Reports, 7*, 44499. https://doi.org/10.1038/srep44499

Kwakkel, J. H., Haasnoot, M., & Walker, W. E. (2016). Comparing robust decision-making and dynamic adaptive policy pathways for model-based decision support under deep uncertainty. *Environmental Modelling & Software, 86*, 168–183. https://doi.org/10.1016/j.envsoft.2016.09.017

Lempert, R. J., & Groves, D. G. (2010). Identifying and evaluating robust adaptive policy responses to climate change for water management agencies in the American west. *Technological Forecasting and Social Change, 77*(6), 960–974. https://doi.org/10.1016/j.techfore.2010.04.007

Li, Q., Dong, S., & Mostafavi, A. (2019). Modeling of inter-organizational coordination dynamics in resilience planning of infrastructure systems: A multilayer network simulation framework. *PLOS ONE, 14*(11), e0224522. https://doi.org/10.1371/journal.pone.0224522

Lin, Y., Wang, J., & Yue, M. (2025). Equity-driven distribution power system planning for resilience enhancement. *Electric Power Systems Research, 241*, 111197. https://doi.org/10.1016/j.epsr.2024.111197

Loorbach, D., Frantzeskaki, N., & Avelino, F. (2017). Sustainability transitions research: Transforming science and practice for societal change. *Annual Review of Environment and Resources, 42*, 599–626. https://doi.org/10.1146/annurev-environ-102014-021340

Manocha, N., & Babovic, V. (2018). Real options, multi-objective optimization and the development of dynamically robust adaptive pathways. *Environmental Science & Policy, 90*, 11–18. https://doi.org/10.1016/j.envsci.2018.09.012

Marchau, V. A. W. J., Walker, W. E., Bloemen, P. J. T. M., & Popper, S. W. (Eds.). (2019). *Decision making under deep uncertainty: From theory to practice*. Springer. https://doi.org/10.1007/978-3-030-05252-2

Martello, M. V., Whittle, A. J., Oddo, P. C., & de Neufville, R. (2024). Real options analysis for valuation of climate adaptation pathways with application to transit infrastructure. *Risk Analysis, 44*(5), 1046–1066. https://doi.org/10.1111/risa.14218

McCauley, D., & Heffron, R. (2018). Just transition: Integrating climate, energy and environmental justice. *Energy Policy, 119*, 1–7. https://doi.org/10.1016/j.enpol.2018.04.014

Radicchi, F., & Bianconi, G. (2017). Redundant interdependencies boost the robustness of multiplex networks. *Physical Review X, 7*(1), 011013. https://doi.org/10.1103/PhysRevX.7.011013

Tejedor, A., Longjas, A., Foufoula-Georgiou, E., Georgiou, T. T., & Moreno, Y. (2018). Diffusion dynamics and optimal coupling in multiplex networks with directed layers. *Physical Review X, 8*(3), 031071. https://doi.org/10.1103/PhysRevX.8.031071

van der Pas, J. W. G. M., Walker, W. E., Marchau, V. A. W. J., van Wee, B., & Kwakkel, J. H. (2013). Operationalizing adaptive policymaking. *Futures, 52*, 12–26.

Verbong, G. P. J., & Geels, F. W. (2010). Exploring sustainability transitions in the electricity sector with socio-technical pathways. *Technological Forecasting and Social Change, 77*(8), 1214–1221. https://doi.org/10.1016/j.techfore.2010.04.008

Werners, S. E., Wise, R. M., Butler, J. R. A., Totin, E., & Vincent, K. (2021). Adaptation pathways: A review of approaches and a learning framework. *Environmental Science & Policy, 116*, 266–275. https://doi.org/10.1016/j.envsci.2020.11.003

Xu, Z., & Chopra, S. S. (2023). Interconnectedness enhances network resilience of multimodal public transportation systems for safe-to-fail urban mobility. *Nature Communications, 14*, 4291. https://doi.org/10.1038/s41467-023-39999-w

> **Reference note:** the broader analytical corpus contains additional network-science, infrastructure-recovery, higher-order-network and adaptive-planning papers. This file lists the most directly reusable references for the Stage-7 scope decision.
