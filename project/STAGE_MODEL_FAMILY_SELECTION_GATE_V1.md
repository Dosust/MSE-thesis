# Seven-Stage Model-Family Selection Gate v1.0

**Status:** CURRENT SUPPORTING SPECIFICATION  
**Date:** 2026-09-16  
**Framework authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**RQ–SO–H authority:** `CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Execution method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  

> **Scope rule:** this file does **not** create a new framework and does **not** rename the seven canonical stages. It defines the preferred mathematical-family hierarchy inside each existing stage and the evidence/validation gate that must be passed before a specific implementation is adopted.

---

## 1. Governing hierarchy

The thesis must preserve

```math
\boxed{
\text{Framework stage}
>
\text{mathematical model family}
>
\text{specific algorithm / implementation}.
}
```

Therefore SCM, POMDP, MPC, Hamilton–Jacobi methods, Monte Carlo, DBNs, GNNs, reinforcement learning, robust optimization, and similar techniques are **candidate implementations** inside a stage. They may not redefine the scientific role of that stage.

The method-selection rule follows the canonical reasoning protocol:

```math
\boxed{
\text{engineering question}
\rightarrow
\text{mechanism}
\rightarrow
\text{evidence}
\rightarrow
\text{mathematical structure}
\rightarrow
\text{candidate family}
\rightarrow
\text{assumption compatibility}
\rightarrow
\text{benchmark}
\rightarrow
\text{verification/validation}.
}
```

This is consistent with the broader interdependent-infrastructure literature, where network, dynamical, probabilistic, simulation, optimization, and socio-technical models serve different scientific functions rather than one universal representation (Ouyang, 2014; Tong et al., 2025).

---

## 2. Final stage-to-model-family mapping

| Stage | Canonical stage role | Preferred mathematical family | Status |
|---|---|---|---|
| **1** | Spatiotemporal Multilayer SoS Structure | **Spatial attributed multilayer network with dynamic dependency activation** | primary family selected |
| **2** | Evidence-Grounded Causal Interdependencies | **Evidence-grounded mechanistic causal dependency model**; dynamic SCM semantics optional when justified | primary family selected; SCM not mandatory |
| **3** | Physics-Based Hybrid Multiscale Dynamics | **Physics-based hybrid multiscale dynamical system** | primary family selected |
| **4** | Observation, State Estimation, Organization and Control | **Partially observed constrained stochastic control architecture** | primary family selected; POMDP/MPC are conditional implementations |
| **5** | Uncertainty-Aware Viability and Reachability Resilience | **Finite-horizon uncertainty-aware viability + reach–avoid analysis** | primary theory selected; solver open |
| **6** | Resilience Diagnosis, Intervention and Sustainability Consequences | **Matched mechanistic intervention analysis + sustainability consequence functionals** | primary experiment family selected |
| **7** | Engineering Decision and Adaptive Transformation | **Multi-objective decision under uncertainty with adaptive pathway capability** | primary decision family selected; uncertainty formulation open |

The resulting mathematical backbone is

```math
\boxed{
\mathcal G(x,t)
\rightarrow
\mathbb I(x,t,Y,m)
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
(b_t,\mathcal U_t,\pi_t)
\rightarrow
\mathfrak R_T
\rightarrow
(\Delta\mathfrak R,\Delta\mathbf J_{\rm sus})
\rightarrow
\mathcal A_{R,S}^{\star}.
}
```

---

# 3. Stage 1 — structure

## Canonical stage

**Spatiotemporal Multilayer SoS Structure**

## Preferred family

```math
\boxed{
\text{Spatial attributed multilayer network}
+
\text{dynamic dependency activation}.
}
```

The structural graph contains possible relationships,

```math
\mathcal G=(\mathcal V,\mathcal E,X),
```

while the operational importance/activation of a dependency is represented separately, for example by

```math
\gamma_e(x,t,Y,m)
```

or an equivalent activation state already carried by the canonical dependency contract.

### Scientific reason

**[D/P]** Physical topology and functional activation are not identical. A road, line, charger, communication path, or institutional relation may structurally exist while its cross-system effect changes with location, time, state, or operating mode.

### Baseline

```text
single-layer / independent network;
static multilayer network.
```

### Validation question

> Does the multilayer spatial representation plus state-dependent activation reproduce the observed cross-system structural/functional relationships required by the downstream dynamics better than simpler structural representations?

---

# 4. Stage 2 — causal interdependencies

## Canonical stage

**Evidence-Grounded Causal Interdependencies**

## Preferred family

```math
\boxed{
\text{Evidence-grounded mechanistic causal dependency model}.
}
```

The primary object remains the canonical dependency contract

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e),
```

not a generic statistical edge.

A dynamic structural-equation or SCM representation may be used when useful, for example

```math
X_j(t+\Delta t)
=
f_j\!\left(
X_j(t),
X_i(t-\tau_e),
u_t,\eta_t;	heta_e
\right),
```

but only after the mechanism, direction, activation semantics, provenance, and uncertainty have passed EGMIV evidence gates.

### Scientific reason

**[D/P]** SCM semantics can formalize interventions and counterfactuals, but causal structure must not be manufactured from observational association alone. Feedback such as `P -> T -> P` also requires explicit temporal/state semantics rather than an unqualified static DAG (Peters et al., 2017).

### EGMIV rule

```math
\boxed{
\text{SCM may formalize an accepted mechanism; it may not substitute for mechanism evidence.}
}
```

### Baseline

```text
correlation/association network;
static dependency map;
independent-system representation.
```

### Validation question

> Does the mechanism-constrained causal representation improve intervention/root-cause explanation or prediction relative to association/static representations under matched evidence and scenarios?

---

# 5. Stage 3 — dynamics

## Canonical stage

**Physics-Based Hybrid Multiscale Dynamics**

## Preferred family

```math
\boxed{
\text{Physics-based hybrid multiscale dynamical system}.
}
```

The constituent systems retain their own physics,

```math
\dot x_P=F_P(\cdot),
\qquad
\dot x_T=F_T(\cdot),
```

while accepted interdependencies enter the coupled dynamics

```math
\dot Y
=
F_{\mathcal G}^{m}(Y,u,\eta;\mathbb I)
```

and discrete events/mode transitions satisfy an explicit jump map such as

```math
Y^+=\Psi^{m\to m'}(Y^-,\eta,u).
```

### Scientific reason

**[D/P]** Network structure and causal arrows do not themselves generate physically valid cascade and recovery trajectories. Hybrid dynamics are required because the demonstrator contains continuous flows/queues plus discrete failures, switching, access loss, restoration, and other mode changes.

### Implementation note

Co-simulation may be used to integrate constituent simulators, but

```math
\boxed{
\text{co-simulation}=\text{implementation architecture},
\quad
\text{hybrid dynamics}=\text{mathematical model}.
}
```

### Baseline

```text
static/load-capacity cascade;
uncoupled forward simulation;
non-hybrid continuous approximation where applicable.
```

### Validation question

> Does the physics-based hybrid model reproduce state trajectories, event timing, cascade order, service loss, and recovery within declared validation tolerances?

---

# 6. Stage 4 — observation, organization and control

## Canonical stage

**Observation, State Estimation, Organization and Control**

## Preferred family

```math
\boxed{
\text{Partially observed constrained stochastic control architecture}.
}
```

The canonical decomposition remains

```math
Y_t
\rightarrow
\mathcal I_t
\rightarrow
b_t(Y)
\rightarrow
\mathcal U(z_I,z_O)
\rightarrow
u_t.
```

Information determines what is known,

```math
z_I\rightarrow b_t(Y),
```

while organization determines what can be done,

```math
z_O\rightarrow\mathcal U_t.
```

Operational control satisfies

```math
u_t=\pi_t(b_t,z_I,z_O),
\qquad
u_t\in\mathcal U_t.
```

### Scientific reason

**[D/P]** The stage asks about state knowledge and feasible action, not necessarily long-horizon reward maximization. A full POMDP is therefore a conditional implementation only when optimal sequential decision-making under partial observation is needed and its transition, observation, action, and objective models can be justified.

### Candidate implementations

```text
Bayesian filter / particle filter / ensemble estimator;
output-feedback MPC;
stochastic MPC;
robust MPC;
POMDP when sequential partial-observation decision semantics are required.
```

None is selected merely because it is powerful or common.

### Baseline

```text
perfect/current-state assumption;
point estimate;
open-loop or less-constrained response.
```

### Validation question

> Does explicit state estimation plus feasible feedback improve state reconstruction, constraint satisfaction, response timing, or recovery relative to simpler information/control assumptions?

---

# 7. Stage 5 — resilience

## Canonical stage

**Uncertainty-Aware Viability and Reachability Resilience**

## Preferred family

```math
\boxed{
\text{Finite-horizon uncertainty-aware viability}
+
\text{stochastic/robust reach--avoid}.
}
```

The active resilience object remains

```math
\mathfrak R_T
=
\left(
\mathcal V_{\alpha,T_V},
\mathcal R_{\beta,T_R},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
```

Stochastic viability formalizes the probability of remaining within admissible constraints under feasible policies (Doyen & De Lara, 2010). Stochastic target-tube reachability provides a common constrained-control framework containing stochastic viability and reach–avoid formulations (Vinod & Oishi, 2021).

### Scientific reason

This stage exactly matches the thesis resilience semantics:

```math
\boxed{
\text{remain}
+
\text{return}
+
\text{confidence}.
}
```

### Solver rule

The theory is frozen; the solver is **not**.

```math
\boxed{
\text{viability/reachability theory}
\neq
\text{HJ by default}.
}
```

Hamilton–Jacobi, dynamic programming, Lagrangian/set propagation, sampling, Monte Carlo components, or verified surrogates remain candidate numerical methods selected only after `\mathcal C_{H3}` is frozen. Classical gridded HJ methods face severe state-dimensional scaling, which is why dimensionality and reduction must be audited before solver choice (Bansal et al., 2017; Maidens et al., 2013).

### Baseline

```text
conventional performance/recovery curve;
reliability/service metrics;
point-estimate resilience quantities.
```

### Validation question

> Do viability/reachability quantities add predictive or decision-relevant information beyond the conventional benchmark under the preregistered H3 skill metric?

---

# 8. Stage 6 — diagnosis, intervention and sustainability consequences

## Canonical stage

**Resilience Diagnosis, Intervention and Sustainability Consequences**

## Preferred family

```math
\boxed{
\text{Matched mechanistic intervention analysis}
+
\text{sustainability consequence functionals}.
}
```

The intervention acts on the validated model

```math
\mathfrak M
\xrightarrow{a_k}
\mathfrak M^{a_k},
```

and matched scenarios compare

```math
Y^0(t;\omega)
\quad\text{with}\quad
Y^{a_k}(t;\omega).
```

The primary outputs are

```math
\boxed{
\Delta\mathfrak R^{a_k},
\qquad
\Delta\mathbf J_{\rm sus}^{a_k}.
}
```

with sustainability functionals such as

```math
\mathbf J_{\rm sus}
=
[J_{\rm access},J_{\rm energy},J_{\rm carbon},J_{\rm cost}]^\top
```

only where each outcome passes its causal/data/evidence gate.

### Scientific reason

**[D/P]** Counterfactual notation is useful, but a simulated difference is not automatically an empirically identified causal effect. The primary thesis claim is therefore a matched mechanistic intervention effect inside a validated model; formal SCM counterfactual attribution is added only when its causal-identification assumptions are defensible.

### Baseline

```text
structural centrality ranking;
one-at-a-time sensitivity;
no-intervention baseline;
resilience-only consequence accounting.
```

### Validation question

> Under matched disturbances, do interventions selected from the resilience diagnosis produce reproducible changes in resilience and evidence-supported sustainability outcomes, and are the mechanism-specific changes physically explainable?

---

# 9. Stage 7 — engineering decision and adaptive transformation

## Canonical stage

**Engineering Decision and Adaptive Transformation**

## Preferred family

```math
\boxed{
\text{Multi-objective decision under uncertainty}
+
\text{adaptive pathway capability}.
}
```

The decision object remains

```math
\mathcal A_{R,S}^{\star}
=
\operatorname{Pareto}
\{a_k:\mathfrak R^{a_k},\mathbf J_{\rm sus}^{a_k},C^{a_k},\mathcal U^{a_k}\}.
```

If decisions evolve over time,

```math
\mathfrak M_{k+1}
=
\mathcal T_{a_k}(\mathfrak M_k,\xi_k),
```

with adaptation triggered only when the problem requires sequential pathways.

### Uncertainty-selection rule

```math
\begin{cases}
\text{stochastic multi-objective optimization},
& P(\omega)\text{ is qualified};\\
\text{robust multi-objective optimization},
& \omega\in\Omega\text{ is bounded/deep uncertainty};\\
\text{distributionally robust optimization},
& \text{distributional ambiguity is quantified};\\
\text{adaptive pathway decision},
& \text{future information can trigger sequential changes}.
\end{cases}
```

The thesis does not freeze one uncertainty paradigm before the Stage-5/6 uncertainty evidence is known.

### Scientific reason

**[D/P]** A static robust Pareto set is insufficient when the scientific question includes adaptation through future information and trigger-based transformation. Adaptive-pathway logic is therefore available at Stage 7 without being forced into every experiment.

### Baseline

```text
deterministic single-objective decision;
static multi-objective decision;
resilience-only Pareto set;
non-adaptive intervention sequence.
```

### Validation question

> Does joint resilience–sustainability evaluation under the qualified uncertainty model materially change the feasible/nondominated decision set, and—if adaptation is modeled—does the pathway remain defensible across held-out or stress-tested futures?

---

# 10. Events are cross-cutting, not an eighth stage

Events support temporal identifiability across the framework:

```math
\boxed{
\text{Stage 2: event causation}
\rightarrow
\text{Stage 3: event generation/propagation}
\rightarrow
\text{Stage 4: event detection/action}
\rightarrow
\text{Stage 5: event path to viability/recovery}
\rightarrow
\text{Stage 6: intervention consequence}.
}
```

No additional “event stage” is introduced.

---

# 11. Complexity-admission gate

A more sophisticated model, algorithm, AI method, or geometry is admitted only if all applicable conditions pass:

```math
\boxed{
G_M
=
G_{need}
\land
G_{mechanism}
\land
G_{evidence}
\land
G_{assumption}
\land
G_{ident}
\land
G_{compute}
\land
G_{verify}
\land
G_{value}.
}
```

where:

```text
G_need       = simpler model cannot answer the scientific question adequately;
G_mechanism  = the method represents the required physical/causal mechanism;
G_evidence   = required inputs/parameters have admissible evidence;
G_assumption = method assumptions match the declared domain;
G_ident      = important states/parameters/effects are identifiable enough for the intended claim;
G_compute    = computation is feasible and reproducible;
G_verify     = implementation can be independently verified;
G_value      = incremental explanatory, predictive, control, resilience, or decision value can be tested.
```

If any mandatory gate fails, the method remains exploratory/supporting rather than primary.

---

# 12. Stage-wise benchmark obligation

| Stage | Preferred family must add value beyond | Primary falsifiable question |
|---|---|---|
| **1** | independent layers / static graph | Does multilayer spatial + activation structure reproduce required cross-system relationships better? |
| **2** | association/static dependency model | Does mechanism-constrained causality improve intervention/root-cause inference or prediction? |
| **3** | static/load-capacity cascade | Does hybrid physics reproduce trajectories, timing and cascade/recovery order? |
| **4** | perfect-state / point-estimate / open-loop baseline | Does estimation + feasible feedback improve reconstruction/action/recovery outcomes? |
| **5** | conventional resilience curve | Does `\mathfrak R_T` add preregistered predictive/decision information? |
| **6** | centrality / simple sensitivity / no intervention | Do selected interventions produce larger validated resilience and sustainability changes? |
| **7** | resilience-only or deterministic/static decision | Does joint uncertainty-aware decision analysis materially change the admissible/nondominated intervention set? |

This benchmark obligation prevents mathematical complexity from becoming its own justification.

---

# 13. What is selected versus what remains open

## Selected at model-family level

```text
Stage 1 family: spatial attributed multilayer structure + dynamic activation
Stage 2 family: evidence-grounded mechanistic causal dependencies
Stage 3 family: physics-based hybrid multiscale dynamics
Stage 4 family: partially observed constrained stochastic control architecture
Stage 5 family: finite-horizon viability + reach–avoid under uncertainty
Stage 6 family: matched mechanistic intervention + sustainability functionals
Stage 7 family: multi-objective decision under uncertainty + adaptive pathway capability
```

## Not yet selected

```text
Stage-2 exact SCM implementation: NOT REQUIRED / OPTIONAL
Stage-4 estimator family: OPEN
Stage-4 controller family: OPEN
Stage-4 POMDP use: CONDITIONAL
Stage-5 reduced state: OPEN
Stage-5 numerical solver: OPEN
Stage-5 probability/robust uncertainty model: OPEN
Stage-6 formal SCM counterfactual identification: CONDITIONAL
Stage-7 stochastic vs robust vs DRO formulation: OPEN
Stage-7 adaptive-pathway implementation: CONDITIONAL
AI/GNN/RL/surrogate roles: SUPPORTING ONLY UNTIL G_M PASSES
```

---

# 14. Immediate implication for current H3 work

This file does **not** reopen the framework or H3 package. It reinforces the existing H3 rule:

```math
\boxed{
\text{qualify }K,G_{\rm rec},F,T_V,T_R
\rightarrow
\text{qualify uncertainty}
\rightarrow
\Pi_{\rm adm}
\rightarrow
\mathcal C_{H3}
\rightarrow
\text{select/verify solver}.
}
```

Therefore the immediate next scientific task remains evidence qualification for

```math
\boxed{
\left\{
s_P^{\min},
s_T^{\min},
s_{P,\rm rec},
s_{T,\rm rec},
F,
T_V,
T_R
\right\}.
}
```

No model-family discussion should delay that gate unless new evidence exposes a material contradiction in the canonical framework.

---

# 15. Do-not-regress rules

Future work must not:

1. rename or replace the canonical seven stages because a specific algorithm is selected;
2. replace the Stage-2 dependency contract with a statistically inferred edge set;
3. introduce POMDP or MPC before their decision/control assumptions are justified;
4. equate viability theory with Hamilton–Jacobi computation;
5. call simulation differences empirically identified causal effects without identification evidence;
6. freeze robust optimization before uncertainty semantics are qualified;
7. introduce AI/GNN/RL/surrogate methods without incremental-value and verification gates;
8. add an eighth “event” stage;
9. use mathematical sophistication as evidence of scientific contribution;
10. alter frozen H1–H5 logic merely to fit a preferred method.

---

# 16. References — APA 7

Bansal, S., Chen, M., Herbert, S. L., & Tomlin, C. J. (2017). Hamilton-Jacobi reachability: A brief overview and recent advances. In *2017 IEEE 56th Annual Conference on Decision and Control (CDC)* (pp. 2242–2253). IEEE. https://doi.org/10.1109/CDC.2017.8263977

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Maidens, J. N., Kaynama, S., Mitchell, I. M., Oishi, M. M. K., & Dumont, G. A. (2013). Lagrangian methods for approximating the viability kernel in high-dimensional systems. *Automatica, 49*(7), 2017–2029. https://doi.org/10.1016/j.automatica.2013.03.020

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60.

Peters, J., Janzing, D., & Schölkopf, B. (2017). *Elements of causal inference: Foundations and learning algorithms*. MIT Press.

Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. https://doi.org/10.1016/j.ijcip.2025.100793

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458
