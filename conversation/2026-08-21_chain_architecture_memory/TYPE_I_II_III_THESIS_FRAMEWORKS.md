# Three End-to-End Thesis Frameworks

All three types traverse the complete infrastructure research chain but differ in their scientific center of gravity.

Common broad chain:

`Foundations → Representation → Dynamics → Resilience → Control → Design → Optimization → Decision`

## TYPE I — Theory-First Mathematical Physics

### Working title

**Mathematical Physics of Sustainable Infrastructure Resilience: From Coupled Dynamics to Viability, Recovery, and Optimal Intervention**

### Core verb

**UNDERSTAND**

### Central question

Which states and trajectories of a coupled infrastructure system are physically admissible, viable under disturbance, recoverable after disruption, and controllable under feasible intervention?

### Architecture

`Climate forcing xi(t)`
→ `realized hazard eta(t)`
→ `sector physical laws / constraints`
→ `P–W–T–SW multilayer representation + dynamic interfaces Z(t)`
→ `coupled nonlinear/hybrid dynamics`
→ `service-state mapping Y(t)`
→ `sustainable/equitable admissible set K_SE`
→ `Viab(K_SE)`
→ `reachable/avoid sets`
→ `Capt(K_SE)` / recoverability
→ `recovery control u(t)`
→ `design alternatives d`
→ `optimization (d*,u*)`
→ `decision a*`

### Primary mathematical objects

- coupled/hybrid state equations;
- viability kernel;
- reachable/avoid sets;
- capture/recovery basin;
- barrier/value functions;
- feasible/optimal recovery control.

### Novelty concentration

Not all stages are novel. Proposed concentration:

`dynamic interface mechanisms → viability/reachability → sustainable/equitable recoverability`

Downstream design/optimization/decision demonstrate the value of the theory.

### Best identity

Applied mathematics + mathematical physics.

---

## TYPE II — Inference / Physics-Informed Digital Twin

### Working title

**Physics-Informed Digital Twin for Sustainable Infrastructure Resilience: Identification, Prediction, Control, and Decision under Uncertainty**

### Core verbs

**INFER + PREDICT**

### Central question

Given incomplete/noisy observations, what is the hidden infrastructure state, coupling/interface structure, and parameter set; what will the system do under disturbance; and how should predictions update intervention?

### Architecture

`Real P–W–T–SW infrastructure`
→ `sensing / observations Y_obs`
→ `observability + data quality`
→ `inverse problem / system identification`
→ `posterior p(theta,Z,m | Y_obs)`
→ `state estimation / data assimilation`
→ `physics-informed digital twin`
→ `predictive distribution p(X_{t+tau} | Y_{0:t})`
→ `P(failure), P(viability), P(recovery)`
→ `virtual control experiments u_1,...,u_n`
→ `virtual design alternatives d_1,...,d_m`
→ `optimization`
→ `decision support`
→ `new observations / model update`

### Canonical inverse formulation

`theta_hat = argmin_theta [ ||Y_obs - F(theta)||^2 + lambda R(theta) ]`

or Bayesianly:

`p(theta,Z | Y_obs) ∝ likelihood × prior`

### Primary mathematical objects

- forward operator;
- inverse map;
- posterior distribution;
- state estimator/filter;
- uncertainty propagation;
- predictive risk distribution.

### Closed loop

`Reality → Data → Inference → Digital Twin → Prediction → Decision → Reality`

### Best identity

Inverse problems + UQ + scientific computing + digital twins.

---

## TYPE III — Design / Optimization / Decision

### Working title

**Optimal Design and Decision-Making for Sustainable and Resilient Coupled Infrastructure Systems under Climate Uncertainty**

### Core verbs

**DESIGN + DECIDE**

### Central question

Among physically feasible infrastructure architectures and recovery strategies, which alternatives best balance resilience, cost, recovery time, sustainability, equity, and uncertainty?

### Architecture

`climate/hazard scenarios xi_1,...,xi_S`
→ `physical constraints`
→ `design-dependent network G(d)`
→ `dynamic simulation X(t;d,u,xi)`
→ `resilience/performance metrics R(d,u,xi)`
→ `control options u`
→ `design space D`
→ `multiobjective/stochastic/robust optimization`
→ `Pareto set P_Pareto`
→ `decision/policy a*`
→ `implementation + learning`

### Design vector example

`d = [d_P, d_W, d_T, d_SW, d_I]^T`

where `d_I` represents interface architecture.

### Multiobjective structure

A representative objective vector may include:

- capital/operational cost;
- recovery time;
- service loss;
- emissions/environmental burden;
- inequity;
- failure probability.

Subject to physical, service, budget, and institutional constraints.

### Primary mathematical objects

- design space;
- feasible control/design set;
- stochastic/robust objective;
- Pareto frontier;
- final decision rule.

### Best identity

Operations research + systems engineering + infrastructure optimization.

---

# Comparison

| Dimension | Type I | Type II | Type III |
|---|---|---|---|
| Main question | What is physically viable/recoverable? | What is the real hidden system and what will it do? | What should be built/done? |
| Primary unknown | viable/recoverable region | hidden state/parameters/interfaces | optimal/robust design & intervention |
| Dynamics | central | central | simulation engine |
| Inverse problems | supporting | central | optional |
| UQ | important | central | important |
| Resilience | central object | predicted property | objective/constraint |
| Control | downstream | closed-loop | decision variable |
| Design | downstream demonstration | virtual experiment | central |
| Optimization | downstream | downstream decision support | central |
| Decision | interpretation | operational/planning recommendation | final objective |
| Current MSE fit | strongest | strong extension | larger reorientation |

# Recommended current use

For the present MSE thesis, retain **Type I** as the primary architecture but allow it to demonstrate downstream consequences through control/design/optimization/decision.

Do not claim independent novelty at all eight steps.

Suggested novelty center:

`Dynamic Interfaces + Coupled Dynamics + Sustainable/Equitable Viability + Recoverability`

Type II and Type III remain coherent alternative thesis families and potential future research extensions.