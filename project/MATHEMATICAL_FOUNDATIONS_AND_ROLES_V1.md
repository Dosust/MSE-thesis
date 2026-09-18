# Mathematical Foundations and Their Roles

**Status:** CURRENT WORKING MATHEMATICAL SPECIFICATION  
**Effective date:** 2026-09-18  
**Thesis:** *Mathematical Physics of Multilayer Interdependent Power–Transportation Infrastructure Resilience*  
**Framework authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**RQ–SO–H authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Method authority:** `EGMIV_METHOD_V1.md`  
**Writing/inference authority:** `../thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

> Mathematical methods are admitted by scientific function, not by sophistication. Every method must have explicit physical or engineering semantics, trace to one or more research questions, and expose assumptions, evidence, verification, validation, uncertainty, and validity domain where applicable.

## 1. Canonical mathematical architecture

```math
\boxed{
\text{Multilayer Structure}
\rightarrow
\text{Directed Interdependencies}
\rightarrow
\text{Network Physics}
\rightarrow
\text{Hybrid Dynamics}
\rightarrow
\text{Estimation and Control}
\rightarrow
\text{Viability and Reachability}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Intervention Optimization}
\rightarrow
\text{Engineering Decision}
}
```

The mathematical stack is organized around twelve foundations. Methods marked **CORE** are required by the current thesis logic. **CORE DOWNSTREAM** and **CORE VALIDATION** methods are required only after their upstream objects are established. Conditional methods are scientifically admissible but require explicit activation criteria.

---

## M1 — Multilayer Graph Theory

**Status:** CORE  
**Research role:** Represent the Power and Transportation physical networks, supporting Information and Organization domains, spatially embedded components, and candidate cross-domain relations.

```math
\mathcal G=(\mathcal G_P,\mathcal G_T,\mathcal E_{\times}).
```

**Primary question:** What exists, where does it exist, and where can interaction occur?  
**RQ:** RQ1.

**Scientific boundary:** A graph edge is a candidate relation, not automatically a causal dependency.

---

## M2 — Spatial Network Mathematics

**Status:** CORE  
**Research role:** Preserve geographic location, component correspondence, network paths, spatial exposure, and spatiotemporal propagation.

```math
x_i\in\mathbb R^2,
\qquad
\mathcal M_{PT}:V_P\leftrightarrow V_T.
```

**Primary question:** Where do dependencies, disturbances, and recovery processes occur?  
**RQ:** RQ1–RQ3.

**Scientific boundary:** Spatial co-location or common hazard exposure does not establish causal dependency.

---

## M3 — Directed Interdependency Mathematics

**Status:** CORE  
**Research role:** Translate candidate structural relations into evidence-qualified directional dependency mechanisms.

```math
\mathfrak d_e
=
(
\text{source},
\text{receiver},
\text{mechanism},
\text{activation},
\text{parameters},
\text{uncertainty},
\text{evidence}
).
```

The thesis preserves

```math
\text{structural relation}
\neq
\text{causal dependency}
```

and

```math
P\rightarrow T
\neq
T\rightarrow P.
```

**Primary question:** Why and through what mechanism does one component affect another?  
**RQ:** RQ2.

**Scientific boundary:** Use evidence-qualified directed dependency mechanisms; do not label this formal causal-graph inference unless a causal-identification framework is separately justified.

---

## M4 — Network Physics and Conservation Laws

**Status:** CORE  
**Research role:** Preserve the physical behavior of the constituent Power and Transportation systems instead of reducing them to abstract graph topology.

```math
\dot x_P=F_P(x_P,u_P,\eta_P),
```

```math
\dot x_T=F_T(x_T,u_T,\eta_T).
```

**Primary question:** What physical laws govern each infrastructure before and during coupling?  
**RQ:** RQ3.

**Scientific boundary:**

```math
\boxed{\text{topology}\neq\text{physics}.}
```

The adopted power and transportation equations must be benchmark-appropriate, dimensionally consistent, and attributed where externally derived.

---

## M5 — Nonlinear Dynamical Systems

**Status:** CORE  
**Research role:** Translate qualified dependency mechanisms into time-dependent coupled trajectories.

```math
\dot Y
=
F_{\mathcal G}^{m}
(Y,u,\eta;\mathbb I).
```

This layer represents degradation, cross-system propagation, cascading behavior, feedback, and recovery.

**Primary question:** How does the coupled system evolve through time?  
**RQ:** RQ3.

**Scientific role:**

```math
\boxed{
\text{qualified mechanisms}
\rightarrow
\text{state trajectories}
}
```

---

## M6 — Hybrid Dynamical Systems

**Status:** CORE  
**Research role:** Represent the coexistence of continuous infrastructure evolution and discrete events such as failure, isolation, switching, repair, and restoration.

During continuous evolution,

```math
\dot Y=F_m(Y,u,\eta),
```

while a discrete event may produce

```math
Y^+
=
\Psi^{m\rightarrow m'}(Y,u,\eta).
```

**Primary question:** How do continuous physical processes interact with discrete infrastructure events?  
**RQ:** RQ3.

**Scientific boundary:** Event time, causal delay, and characteristic timescale remain distinct objects.

---

## M7 — State Estimation and Control Theory

**Status:** CORE  
**Research role:** Separate the true physical state from what operators observe and estimate, and determine which actions are physically and organizationally feasible.

```math
y_t=h(Y_t)+\varepsilon_t,
```

```math
Y_t
\rightarrow
y_t
\rightarrow
\widehat Y_t
\rightarrow
\mathcal U_t
\rightarrow
u_t.
```

```math
u_t
=
\pi(\widehat Y_t,z_I,z_O),
\qquad
u_t\in\mathcal U_t.
```

**Primary question:** What is known about the system and what can actually be done?  
**RQ:** RQ4.

**Scientific boundary:** Information and Organization affect observation, estimation, authority, resources, and feasible action; they are not automatically modeled as physical infrastructure networks.

---

## M8 — Viability Theory

**Status:** CORE  
**Research role:** Determine the states from which critical electricity and mobility services can remain inside an admissible service region under feasible controls.

Let

```math
K(t)
=
\left\{
Y:
Q(Y,t)
\text{ satisfies declared service requirements}
\right\}.
```

A viability set identifies initial states from which admissible evolution can be maintained under feasible control.

```math
\mathcal V_T
=
\left\{
Y_0:
\exists u(\cdot)
\text{ such that }
Y(t)\in K(t)
\right\}.
```

**Primary question:** Can required service remain acceptable?  
**RQ:** RQ5.

**Scientific interpretation:**

```math
\boxed{\text{viability}=\text{remain}.}
```

---

## M9 — Reachability and Reach–Avoid Theory

**Status:** CORE  
**Research role:** Determine whether a disturbed state can return to an acceptable recovered region within a declared horizon while avoiding unacceptable states.

```math
\mathcal R_{\beta,T}
=
\left\{
\text{states admitting acceptable recovery with declared confidence}
\right\}.
```

The thesis therefore distinguishes

```math
\boxed{\text{viability}=\text{remain}}
```

from

```math
\boxed{\text{reachability}=\text{return}.}
```

**Primary question:** If service becomes unacceptable, can it recover acceptably?  
**RQ:** RQ5.

---

## M10 — Probability, Uncertainty Quantification and Sensitivity

**Status:** CORE  
**Research role:** Represent and propagate uncertainty rather than attaching uncertainty only after simulation.

```math
\mathbf U
=
\left\{
U_\eta,
U_{\mathbb I},
U_{\rm model},
U_\theta,
U_{\rm obs},
U_{\rm int},
U_{\rm acc}
\right\}.
```

Outputs include, where evidence supports probabilistic treatment,

```math
P_{\rm viable},
\qquad
P_{\rm recover}.
```

Sensitivity analysis identifies which assumptions, parameters, and dependency mechanisms can materially change the engineering conclusion.

**Primary question:** With what confidence does the resilience conclusion hold?  
**RQ:** RQ3–RQ7.

The Stage-5 interpretation is

```math
\boxed{
\text{Resilience}
=
\text{Remain}
+
\text{Return}
+
\text{Confidence}
}
```

where the plus signs denote conceptual composition rather than scalar addition.

---

## M11 — Constrained and Multi-Objective Optimization

**Status:** CORE DOWNSTREAM  
**Research role:** Compare feasible engineering interventions only after the coupled physical and resilience models have been established.

For intervention `a_k`,

```math
a_k
\rightarrow
Y^{a_k}
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right).
```

Candidate interventions may then be compared through a nondominated or Pareto set,

```math
\mathcal A_{R,S}^{\star}.
```

The thesis preserves

```math
\text{effectiveness}
\neq
\text{resource efficiency}
\neq
\text{sustainability}.
```

**Primary question:** Which feasible intervention provides defensible resilience and sustainability consequences?  
**RQ:** RQ6–RQ7.

**Scientific boundary:**

```math
\boxed{
\text{optimization does not define resilience};
\quad
\text{it acts on an established resilience model}.
}
```

---

## M12 — Statistical Inference and Comparative Model Testing

**Status:** CORE VALIDATION  
**Research role:** Determine whether additional mathematical complexity produces measurable engineering information.

The principal hierarchy is

```math
M_0=\text{independent systems},
```

```math
M_1=\text{static coupling},
```

```math
M_2=\text{dynamic causal coupling}.
```

The thesis tests

```math
\boxed{
M_2
\overset{?}{>}
M_1
}
```

rather than assuming superiority.

The same comparative logic applies to later resilience and intervention hypotheses.

**Primary question:** Does the proposed mathematical representation add reproducible engineering value relative to simpler alternatives?  
**RQ:** RQ3–RQ7.

**Scientific boundary:** Model complexity is not evidence of model superiority.

---

# 2. Conditional Mathematical Methods

The following methods are scientifically admissible but are not mandatory parts of the thesis unless their activation conditions are satisfied.

## C1 — Bayesian Filtering

**Status:** CONDITIONAL  
Use only when an evidence-supported probabilistic observation and transition model exists.

A belief-state representation may be written as

```math
p(Y_t\mid\mathcal I_t),
```

but Bayesian filtering is an implementation choice rather than the definition of Stage 4.

## C2 — Explicit Time-Delay or Delay-Differential Models

**Status:** CONDITIONAL  
Use only when causal delay is materially important and identifiable separately from event time and characteristic timescale.

```math
\tau_e
=
\text{causal or process-specific delay parameter}
```

does not by itself justify a delay-differential equation.

## C3 — Robust Optimization

**Status:** CONDITIONAL  
Use only when the declared uncertainty semantics and engineering decision problem justify set-based robust decisions rather than deterministic or stochastic formulations.

## C4 — Differential or Riemannian Geometry

**Status:** RESEARCH CANDIDATE / CONDITIONAL  
Do not activate solely because geometric mathematics is attractive. Euclidean or state-space viability geometry is the baseline.

The baseline resilience margin may be

```math
\rho_{\mathcal V}(Y)
=
d(Y,\partial\mathcal V).
```

Differential or Riemannian geometry becomes admissible only if:

1. a clearly stated limitation of the baseline geometry is demonstrated;
2. a physically or statistically justified non-Euclidean metric is defined;
3. the added geometric structure produces measurable engineering information beyond the simpler baseline;
4. the corresponding comparison, uncertainty, and validation gates are preregistered.

---

# 3. External Scientific Validation Basis

The current mathematical stack is consistent with established bodies of work in:

- multilayer and multiplex network theory;
- interdependent critical-infrastructure modeling;
- coupled Power–Transportation modeling;
- hybrid dynamical systems;
- control and state estimation;
- viability theory;
- reachability and reach–avoid analysis;
- infrastructure uncertainty quantification and sensitivity analysis;
- constrained and multi-objective infrastructure optimization;
- statistical model comparison.

Representative foundational and application references include Kivelä et al. on multilayer networks, Ouyang on interdependent critical-infrastructure modeling, Wei et al. on Power–Transportation interdependence, Goebel–Sanfelice–Teel on hybrid dynamical systems, Aubin on viability theory, Hamilton–Jacobi reachability literature, and coupled traffic–power resilience work such as Fotouhi et al.

This validation establishes **methodological legitimacy**, not thesis novelty or empirical superiority. Novelty, parameter admission, implementation choice, and model superiority remain separate evidence and validation gates.

---

# 4. Governing Mathematical Rule

```math
\boxed{
\text{No mathematical method enters the thesis merely because it is advanced.}
}
```

A method enters only through

```math
\boxed{
RQ
\rightarrow
\text{physical/engineering need}
\rightarrow
\text{mathematical object}
\rightarrow
\text{assumptions}
\rightarrow
\text{data/evidence}
\rightarrow
\text{verification}
\rightarrow
\text{validation}
\rightarrow
\text{bounded inference}
}
```

This rule is subordinate to the current canonical framework, RQ–SO–H specification, EGMIV method, writing/inference standard, and higher ASU/SSEBE/committee requirements.
