# Canonical Seven-Stage Thesis Framework v2.0

![Authority](https://img.shields.io/badge/authority-CANONICAL-0969DA)
![Framework](https://img.shields.io/badge/stages%201--7-v2.0-1A7F37)
![Resilience](https://img.shields.io/badge/resilience-viability%20%2B%20reachability%20%2B%20probability-0969DA)
![VVUQ](https://img.shields.io/badge/VVUQ-cross--cutting-8250DF)

**Effective date:** 2026-09-16  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Status:** CANONICAL v2.0  
**Supersedes:** `CANONICAL_7_STAGE_FRAMEWORK.md` for active framework interpretation; the v1 file remains provenance.  
**Change basis:** literature-grounded methodological refinement plus explicit thesis decision to replace controlled viability alone with an uncertainty-aware viability–reachability resilience core.  
**Change control:** any subsequent scientific revision requires explicit approval, versioning, Git history, and re-audit of dependent hypotheses, figures, experiments, and thesis text.

> **Scientific guardrail:** v2.0 defines the thesis framework and testable mathematical architecture. It does not claim that viability–reachability is empirically superior to conventional resilience assessment. Incremental engineering value must be established by comparison and validation.

---

# Scientific identity

```math
\boxed{
\textbf{Coupled Power--Transportation infrastructure}
=
\underbrace{\text{Interdependent System of Systems}}_{\text{architecture}}
+
\underbrace{\text{Complex dynamical system}}_{\text{behavior}}
}
```

The physical core is

```math
\boxed{P+T}
```

with supporting information and organizational layers:

```math
\boxed{\mathcal S=\{P,T,I,O\}}.
```

The framework studies how **causal interdependencies propagate through space and time, affect the ability to maintain or recover critical services, and change the consequences of engineering interventions under uncertainty**.

---

# Framework input — Critical service requirements

This is not an additional stage. It defines what counts as acceptable system operation.

Let

```math
Q(Y,t)=
\begin{bmatrix}
Q_P\\
Q_T\\
Q_{PT}
\end{bmatrix}
```

represent electricity, mobility, and coupled service functions.

Define the acceptable operating set

```math
\boxed{
K(t)=
\left\{
Y:
q_j^{\min}(t)
\le Q_j(Y,t)
\le q_j^{\max}(t),
\quad j=1,\ldots,n_Q
\right\}.
}
```

This answers:

```math
\boxed{\text{What services must remain acceptable, where, and for how long?}}
```

---

# 1. Spatiotemporal Multilayer System-of-Systems Structure

## Purpose

Represent **what exists, where it exists, and where interaction can occur**.

The architecture is

```math
\boxed{\mathcal S=\{P,T,I,O\}}
```

with geographically embedded multilayer graph

```math
\boxed{
\mathcal G=(\mathcal V,\mathcal E,X),
\qquad
X=\{x_i\}_{i\in\mathcal V}.
}
```

Each component has a location and state:

```math
\boxed{
x_i\in\mathbb R^2,
\qquad
Y_i(t).
}
```

The integrated system state is

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
```

## Mandatory principle

```math
\boxed{\text{Every physically spatial cascade preserves both time and location.}}
```

## Main question

> **What systems, components, locations, interfaces, and layers constitute the coupled system?**

## Output

```math
\boxed{\mathcal S,\mathcal G,X,Y}
```

---

# 2. Evidence-Grounded Causal Interdependencies

## Purpose

Determine **how one infrastructure component or layer physically or operationally affects another**.

Every accepted directed dependency is represented by the canonical object

```math
\boxed{
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)
}
```

where

```math
\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e)
```

defines source, receiver, interaction locations, and exchanged service/resource;

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e)
```

defines the causal mechanism, activation condition, parameters, and possible internal state; and

```math
\Pi_e=(\mathcal P_e,V_e,\mathcal U_e)
```

contains provenance, validation status, and uncertainty.

The active interdependency structure becomes

```math
\boxed{\mathbb I=\mathbb I(x,t,Y,m).}
```

Therefore an interdependency may change:

```math
\boxed{
\text{with location}
+
\text{time}
+
\text{state}
+
\text{operating mode}.
}
```

## Fundamental requirement

```math
\boxed{\text{common exposure or correlation}\neq\text{causal dependency}.}
```

## Main question

> **Why, where, when, and through what mechanism does one component or layer affect another?**

## Output

```math
\boxed{\mathbb I=\{\mathfrak d_e\}}
```

---

# 3. Physics-Based Hybrid Multiscale Dynamics

## Purpose

Determine **how accepted interdependencies generate coupled behavior, cascading effects, and recovery through time and space**.

Power and Transportation retain their own physics:

```math
\dot x_P
=
F_P(x_P,u_P,\eta_P)
+
\sum_{e:T\rightarrow P}\Phi_e,
```

```math
\dot x_T
=
F_T(x_T,u_T,\eta_T)
+
\sum_{e:P\rightarrow T}\Phi_e.
```

The complete system is represented as

```math
\boxed{
\dot Y
=
F_{\mathcal G}^{m}
\left(Y,u,\eta;\mathbb I\right).
}
```

Hybrid events may satisfy

```math
Y^{+}
=
\Psi^{m\rightarrow m'}(Y,\eta,u)
```

under specified event guards.

The evolution is spatiotemporal:

```math
\boxed{Y=Y(x,t).}
```

Therefore propagation is represented as

```math
(x_0,t_0)
\rightarrow
(x_1,t_1)
\rightarrow
\cdots
\rightarrow
(x_n,t_n).
```

## Mandatory temporal distinction

```math
\boxed{
\text{event time}
\neq
\text{causal delay}
\neq
\text{characteristic timescale}.
}
```

## Main question

> **How, where, and how quickly do interdependent disruption and recovery processes evolve?**

## Output

```math
\boxed{
Y(x,t),\quad
Q(x,t),\quad
\text{cascade and recovery trajectories}
}
```

---

# 4. Observation, State Estimation, Organization and Control

## Purpose

Connect the true physical state to **what operators know and what they are actually able to do**.

Measurements satisfy, generically,

```math
y_t=h(Y_t)+\varepsilon_t.
```

Available information forms

```math
\mathcal I_t
=\{y_{0:t},\text{forecasts, messages, observations}\}.
```

State estimation produces either

```math
\widehat Y_t
```

or, under uncertainty,

```math
\boxed{
b_t(Y)=p(Y_t\mid\mathcal I_t).
}
```

DBN, HMM, Bayesian filtering, or other estimators are **candidate implementations**, not definitions of the stage.

Information and organizational states determine the feasible action set:

```math
\boxed{
\mathcal U_t
=
\mathcal U
\left(\widehat Y_t,z_I(t),z_O(t)\right).
}
```

For example,

```math
z_O=
[
\text{authority},
\text{resources},
\text{coordination},
\text{communication},
\text{response delay}
].
```

Operational control becomes

```math
u_t=\pi(\widehat Y_t,z_I,z_O),
\qquad
u_t\in\mathcal U_t.
```

The causal sequence is therefore

```math
\boxed{
Y
\rightarrow y
\rightarrow\widehat Y
\rightarrow(z_I,z_O)
\rightarrow\mathcal U
\rightarrow u.
}
```

## Main question

> **What state is the coupled system believed to be in, and what actions are physically and organizationally feasible?**

## Output

```math
\boxed{
\widehat Y_t,
\quad
p(Y_t\mid\mathcal I_t),
\quad
\mathcal U_t,
\quad
u_t
}
```

---

# 5. Uncertainty-Aware Viability and Reachability Resilience

This is the **canonical resilience core**.

It consists of three complementary concepts:

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

The plus signs represent conceptual composition, not scalar addition.

## 5.1 Viability — remain acceptable

Define

```math
\boxed{
\mathcal V_{\alpha,T}(t)
=
\left\{
y:
\exists\pi\in\Pi(z_I,z_O)
\text{ such that }
\Pr^\pi
\left[
Y_\tau\in K(\tau),
\forall\tau\in[t,t+T]
\mid\mathcal I_t
\right]
\ge\alpha
\right\}.
}
```

This asks:

```math
\boxed{\text{Can critical service remain acceptable under feasible controls?}}
```

## 5.2 Reachability — return to acceptable operation

Let `G_{\rm rec}` be the desired recovered region and `F` an unacceptable region.

Define the stochastic reach–avoid set

```math
\boxed{
\mathcal R_{\beta,T}(t)
=
\left\{
y:
\exists\pi
\text{ such that }
\Pr^\pi
\left[
\tau_{G_{\rm rec}}\le T,
\;
Y_s\notin F
\ \forall s<\tau_{G_{\rm rec}}
\mid\mathcal I_t
\right]
\ge\beta
\right\}.
}
```

This asks:

```math
\boxed{\text{Can acceptable service be recovered before unacceptable failure?}}
```

## 5.3 Probability — confidence under uncertainty

Probability qualifies both maintainability and recovery:

```math
\boxed{P_{\rm viable}}
```

and

```math
\boxed{P_{\rm recover}.}
```

It does **not** constitute a separate resilience theory.

Instead:

```math
\boxed{
\text{probability}
=
\text{uncertainty layer over viability and reachability}.
}
```

## 5.4 Final resilience object

Define

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

where

```math
\rho_{\mathcal V}=d(Y,\partial\mathcal V)
```

measures proximity to loss of maintainability,

```math
T_{\mathcal V}
```

measures time to viability loss, and

```math
T_{\rm rec}
```

measures recovery time.

### Performance-curve benchmark

Conventional resilience remains a comparator:

```math
Q(t)\rightarrow R_{\rm curve}.
```

The scientific comparison is therefore:

```math
\boxed{
R_{\rm curve}
\quad\text{versus}\quad
\mathfrak R_T.
}
```

The thesis must **test, rather than assume, whether the viability–reachability formulation provides additional engineering information**.

## Main questions

> **Can service remain acceptable?**  
> **If it becomes unacceptable, can it be recovered?**  
> **Within what time?**  
> **Under which feasible controls?**  
> **With what probability?**

---

# 6. Resilience Diagnosis, Engineering Intervention and Sustainability Consequences

## Purpose

Convert resilience information into an engineering diagnosis.

From

```math
\mathfrak R_T
```

identify:

- loss mechanisms;
- critical interfaces;
- spatial propagation paths;
- temporal bottlenecks;
- organizational constraints;
- recovery limitations.

Symbolically,

```math
\boxed{
\mathfrak R_T\rightarrow\mathcal D_R.
}
```

Candidate engineering interventions are then defined:

```math
a_k\in\mathcal A.
```

An intervention may modify:

```math
\mathcal G,
\quad
\mathbb I,
\quad
F,
\quad
\mathcal U,
\quad
K.
```

Thus

```math
\boxed{
\mathfrak M
\overset{a_k}{\longrightarrow}
\mathfrak M^{a_k}.
}
```

The intervention is rerun through the coupled model:

```math
Y^0(x,t)
\rightarrow
Y^{a_k}(x,t).
```

Changes in resilience are computed:

```math
\Delta\mathfrak R^{a_k}.
```

Sustainability is evaluated from the resulting trajectory:

```math
\boxed{
\mathbf J_{\rm sus}^{a_k}
=
\mathcal J\left[Y^{a_k}(x,t)\right].
}
```

Core outcomes include, where supported:

```math
\boxed{
\mathbf J_{\rm sus}
=
[
J_{\rm access},
J_{\rm energy},
J_{\rm carbon},
J_{\rm cost}
]^{\top}.
}
```

Therefore:

```math
\boxed{
a_k
\rightarrow
Y^{a_k}
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right).
}
```

## Fundamental principle

```math
\boxed{
\text{resilience improvement}
\not\Rightarrow
\text{simultaneous improvement of all sustainability outcomes}.
}
```

Possible outcomes include:

```math
\boxed{
\text{synergy}
\quad|\quad
\text{trade-off}
\quad|\quad
\text{burden shifting}.
}
```

## Main question

> **Which intervention changes the mechanisms responsible for resilience loss, and what resilience and sustainability consequences follow?**

---

# 7. Engineering Decision and Adaptive Transformation

## Purpose

Determine which intervention or sequence of interventions remains defensible under multiple objectives and uncertainty.

Operational control and strategic intervention remain distinct:

```math
\boxed{u(t)\neq a_k.}
```

where

```math
u(t)=\text{operate the current system},
```

while

```math
a_k=\text{change the system or regime}.
```

Candidate interventions are evaluated using resilience, sustainability, feasibility, and uncertainty:

```math
\boxed{
\mathcal A_{R,S}^{\star}
=
\operatorname{Pareto}
\left\{
a_k:
\mathfrak R^{a_k},
\mathbf J_{\rm sus}^{a_k},
C^{a_k},
\mathcal U^{a_k}
\right\}.
}
```

When long-term adaptation is required,

```math
\mathfrak M_{k+1}
=
\mathcal T_{a_k}(\mathfrak M_k,\xi_k).
```

This permits a sequence

```math
\mathfrak M_0
\rightarrow
\mathfrak M_1
\rightarrow
\cdots
\rightarrow
\mathfrak M_n.
```

MPC, robust optimization, many-objective optimization, MDP/POMDP, or other methods may be used **only where their scientific role and data requirements are justified**.

## Main question

> **What should be changed, where, when, and under which uncertainty conditions?**

## Output

```math
\boxed{\mathcal A_{R,S}^{\star}}
```

and, when appropriate,

```math
\boxed{
a^\star
\quad\text{or}\quad
(a_1^\star,\ldots,a_n^\star).
}
```

---

# Cross-Cutting Requirement — VVUQ and Falsification

Verification, validation, and uncertainty quantification are **not another stage**.

They apply throughout:

```math
\boxed{
\text{Stages }1\text{--}7
\subset
\text{VVUQ + falsification}.
}
```

Every proposed mechanism or model must expose:

```math
\boxed{
\text{assumptions}
+
\text{parameters}
+
\text{evidence}
+
\text{uncertainty}
+
\text{verification}
+
\text{validation domain}.
}
```

The principal model-comparison architecture remains:

```math
\boxed{M_0=\text{independent systems}}
```

```math
\boxed{M_1=\text{static coupling}}
```

```math
\boxed{M_2=\text{dynamic causal coupling}.}
```

The primary question is not assumed to have a predetermined answer:

```math
\boxed{M_2\overset{?}{>}M_1.}
```

---

# Final Seven-Stage Framework

| Stage | Scientific role | Main question |
|---|---|---|
| **1. Spatiotemporal Multilayer SoS Structure** | Define systems, components, layers, and geography | What exists and where? |
| **2. Evidence-Grounded Causal Interdependencies** | Define directional mechanisms | Why and through what mechanism are systems coupled? |
| **3. Physics-Based Hybrid Multiscale Dynamics** | Propagate mechanisms through time and space | How, where, and how fast do effects propagate? |
| **4. Observation, State Estimation, Organization and Control** | Determine system knowledge and feasible actions | What do operators know and what can they do? |
| **5. Uncertainty-Aware Viability and Reachability Resilience** | Quantify remain + return + confidence | Can service remain or recover acceptably, and with what probability? |
| **6. Resilience Diagnosis, Intervention and Sustainability Consequences** | Convert resilience diagnosis into interventions and consequences | What should be changed and what consequences follow? |
| **7. Engineering Decision and Adaptive Transformation** | Select defensible interventions under uncertainty | Which intervention/pathway should be implemented, where and when? |

---

# Complete Mathematical Chain

```math
\boxed{
\begin{aligned}
K(t)
&\rightarrow
\underbrace{(\mathcal S,\mathcal G,X)}_{\text{1}}\\
&\rightarrow
\underbrace{\mathbb I(x,t,Y,m)}_{\text{2}}\\
&\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{\text{3}}\\
&\rightarrow
Y(x,t)\\
&\rightarrow
\underbrace{
y_t
\rightarrow\mathcal I_t
\rightarrow p(Y_t\mid\mathcal I_t)
\rightarrow\mathcal U(z_I,z_O)
\rightarrow u_t
}_{\text{4}}\\
&\rightarrow
\underbrace{
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
P_{\rm viable},
P_{\rm recover}
\right)
}_{\text{5}}\\
&\rightarrow
\underbrace{
\mathcal D_R
\rightarrow a_k
\rightarrow Y^{a_k}
\rightarrow
(\Delta\mathfrak R,\Delta\mathbf J_{\rm sus})
}_{\text{6}}\\
&\rightarrow
\underbrace{\mathcal A_{R,S}^{\star}}_{\text{7}}.
\end{aligned}
}
```

## Simplest scientific interpretation

```math
\boxed{
\begin{gathered}
\text{Need} \rightarrow \text{Structure} \rightarrow \text{Causality} \rightarrow \text{Dynamics} \\
\rightarrow \text{Knowledge \& Action} \rightarrow \text{Remain / Return / Confidence} \\
\rightarrow \text{Intervention \& Consequences} \rightarrow \text{Decision}
\end{gathered}
}
```

The resilience core is therefore

```math
\boxed{
\textbf{Resilience}
=
\underbrace{\text{maintain acceptable service}}_{\text{viability}}
+
\underbrace{\text{recover acceptable service}}_{\text{reachability}}
+
\underbrace{\text{quantify confidence}}_{\text{probability}}.
}
```

Again, this is a conceptual composition rather than scalar addition.

---

# Validation Boundary

This framework **does not yet establish**:

- empirical superiority of `\mathfrak R_T` over performance/recovery curves;
- calibrated values of `\alpha` or `\beta`;
- validated probabilistic distributions for all hazards, dependencies, observations, or organizational response processes;
- confirmed intervention rankings;
- confirmed resilience–sustainability synergies or trade-offs.

These require preregistered experiments, VVUQ, and evidence-qualified data.

> **CANONICAL v2.0:** The seven-stage thesis architecture is retained. Stage 5 is revised from controlled viability alone to uncertainty-aware viability + reachability + probability; Stages 1–4 and 6–7 are correspondingly clarified without changing the System-of-Systems → dynamics → resilience → intervention → sustainability → decision logic.


## Question/objective consolidation — v3, 2026-09-17

**Change type:** user-authorized wording and traceability amendment. The seven scientific stages are unchanged. Use `CANONICAL_RESEARCH_QUESTIONS_V4.md` for the exact official RQ0/RQ1–RQ7 wording. Use `CANONICAL_RQ_SO_HYPOTHESES_V3.md` for SO1–SO7 and H1–H5 wording/test logic until a separately authorized synchronization.

| Stage | Question / objective | Evidence or hypothesis mapping |
|---|---|---|
| 1 | RQ1 / SO1 | Developmental qualification supporting H1 |
| 2 | RQ2 / SO2 | Developmental qualification supporting H1 |
| 3 | RQ3 / SO3 | H1 |
| 4 | RQ4 / SO4 | H2 |
| 5 | RQ5 / SO5 | H3 |
| 6 | RQ6 / SO6 | H4 |
| 7 | RQ7 / SO7 | H5 |
