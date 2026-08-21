# Six Interacting Scientific Chains and Their Layers

## Why six chains

The original long layer sequence mixed physical causation, epistemic workflow, lifecycle actions, methods, and normative decisions. The revised structure separates these roles while still allowing interactions.

## Chain I — Physical-System Chain

**Question:** What is the infrastructure system, and how does it behave?

\[
\boxed{
\text{Physical Laws}
\rightarrow
\text{System Structure}
\rightarrow
\text{Interdependencies & Interfaces}
\rightarrow
\text{States & Flows}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Cascades}
}
\]

Core layers:
1. sector-specific physical laws and constitutive relations;
2. infrastructure components, spatial configuration and network topology;
3. cross-sector interdependencies and dynamic interface mechanisms;
4. coupled states, stocks, flows and capacities;
5. nonlinear, hybrid and stochastic system dynamics;
6. disturbance propagation, feedback and cascading behaviour.

Representative coupled model:

\[
\boxed{
M(X)\dot X = F(X,Z,m,u,\eta;\theta),\qquad
\varepsilon\dot Z = G(X,Z,m,\eta;\theta),\qquad
m^+=\Phi(X,Z,m,\eta)
}
\]

This chain should carry the strongest **mathematical-physics foundation**: well-posedness, existence, uniqueness, conservation, stability, bifurcation, multiscale coupling and physically meaningful interfaces.

## Chain II — Observation–Inference–Prediction

**Question:** What do we know about the system, and how confidently?

\[
\boxed{
\text{Observe}
\rightarrow
\text{Identify}
\rightarrow
\text{Estimate}
\rightarrow
\text{Quantify Uncertainty}
\rightarrow
\text{Predict}
}
\]

Layers:
1. measurement/sensing/data acquisition;
2. observability and data quality;
3. system identification, calibration and inverse inference;
4. state estimation/data assimilation;
5. parameter, structural and state UQ;
6. forecasting/predictive simulation/scenarios.

Observation model:

\[
y_k=h(x_k,\theta)+\varepsilon_k.
\]

Bayesian inverse form:

\[
p(\theta,Z\mid y)\propto p(y\mid \theta,Z)p(\theta,Z).
\]

Identifiability question:

\[
\boxed{\mathcal G(\theta_1)=\mathcal G(\theta_2)\Rightarrow\theta_1=\theta_2?}
\]

## Chain III — Hazard–Failure–Consequence

**Question:** How does external stress become infrastructure and societal consequence?

\[
\boxed{
\text{Hazard}
\to\text{Exposure}
\to\text{Vulnerability}
\to\text{Damage}
\to\text{Cascades}
\to\text{Function Loss}
\to\text{Service Loss}
\to\text{Consequences}
\to\text{Risk}
}
\]

Critical distinction:

\[
\boxed{
\text{physical damage}
\neq
\text{component functionality}
\neq
\text{service delivered}
\neq
\text{societal consequence}
}
\]

Recommended mapping:

\[
X(t)\to F(t)\to S_g(t)\to C_g(t).
\]

This is also the natural location for fragility, threshold failure, hybrid topology switching, common-cause stressors, climate extremes and cascading loss.

## Chain IV — Resilience–Viability–Recovery

**Question:** Can the system remain acceptable, and if not, can it recover?

\[
\boxed{
\text{State}
\to
\text{Viability}
\to
\text{Reachability}
\to
\text{Resilience}
\to
\text{Recovery}
\to
\text{Adaptive Control}
}
\]

Admissible set:

\[
K_R=K_{\mathrm{phys}}\cap K_{\mathrm{service}}\cap K_{\mathrm{sus}}\cap K_{\mathrm{eq}}.
\]

Viability kernel:

\[
\boxed{
\operatorname{Viab}_{K_R}
=
\{x_0\in K_R:\exists u(\cdot),\;X(t;x_0,u)\in K_R\;\forall t\ge0\}
}
\]

Recovery/capture set:

\[
\boxed{
\mathcal C_R=\{x_0:\exists u(\cdot),\exists T<\infty,\;X(T;x_0,u)\in\mathcal V_R\}
}
\]

Hamilton–Jacobi reachability prototype:

\[
\partial_tV+H(x,\nabla V)=0.
\]

This chain offers the strongest theorem-building opportunity together with Chain I.

## Chain V — Engineering Design–Operation–Adaptation

**Question:** What should engineers build and do?

\[
\boxed{
\text{Requirements}
\to
\text{Design}
\to
\text{Deploy}
\to
\text{Operate}
\to
\text{Maintain}
\to
\text{Expand / Retrofit}
\to
\text{Adapt}
\to
\text{Decommission / Circularize}
}
\]

Optimization is **not** a single stage here; it is a cross-cutting method that can act on design, dispatch, maintenance, restoration, investment and adaptation.

Generic design problem:

\[
\boxed{d^*=\arg\min_d J(d)}
\]

subject to physics, service, sustainability, equity, recovery and budget constraints.

## Chain VI — Sustainability–Equity–Governance–Decision

**Question:** What should society ultimately choose?

\[
\boxed{
\text{Needs}
\to
\text{Alternatives}
\to
\text{Evaluate}
\to
\text{Trade Off}
\to
\text{Decide}
\to
\text{Implement}
\to
\text{Learn}
\to
\text{Adapt}
}
\]

Parallel evaluation dimensions include technical performance, resilience/risk, environmental sustainability, economics/finance, equity/accessibility/justice, governance/institutional feasibility, and human behaviour/social acceptability.

## Infrastructure lifecycle chain

\[
\boxed{
\text{Need}
\to\text{Planning}
\to\text{Design}
\to\text{Construction}
\to\text{Commissioning}
\to\text{Operation}
\to\text{Monitoring}
\to\text{Aging}
\to\text{Maintenance}
\to\text{Retrofit}
\to\text{Replacement/Transformation}
\to\text{Decommissioning}
\to\text{Reuse/Recycling/Circularity}
}
\]

## Cross-cutting mathematical spine

These are overlapping methods, not causal stages:
- mathematical modelling;
- probability/stochastic processes;
- statistics/Bayesian inference;
- inverse problems/system identification;
- network science/graph theory;
- dynamical systems/PDEs;
- numerical analysis/scientific computing;
- uncertainty quantification;
- control theory;
- optimization/Operations Research;
- machine learning/physics-informed AI;
- game theory/decision science.

## Priority for mathematical rigor

For theorem-quality mathematical physics and a defensible unique contribution, the current priority is:

\[
\boxed{\text{Chain I + Chain II + Chain IV}}
\]

with Chain III supplying stress/failure mechanisms, Chain V supplying engineering decisions, and Chain VI defining admissibility/objectives/trade-offs.

A rigorous hierarchy is:

\[
\boxed{
\text{Model Definition}
\to
\text{Existence}
\to
\text{Uniqueness}
\to
\text{Stability}
\to
\text{Sensitivity}
\to
\text{Identifiability}
\to
\text{Computability}
\to
\text{Validation}
}
\]
