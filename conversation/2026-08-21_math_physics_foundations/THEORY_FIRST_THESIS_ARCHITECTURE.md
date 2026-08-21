# Theory-First Thesis Architecture

## Proposed intellectual identity

**Mathematical Physics of Sustainable Resilient Systems: Foundations and Applications to Infrastructure**

The thesis mathematics should not begin with named sectors. It should begin with a class of open, coupled, dissipative, resource-constrained, dynamically evolving physical systems whose acceptable operation is defined by physical, service, sustainability, and equity requirements.

## 1. Abstract system

\[
\boxed{\mathfrak S=(\mathcal X,\mathcal Z,\mathcal M,\mathcal U,\mathcal D,\mathcal Y)}
\]

with state \(X\), interface states \(Z\), modes \(m\), controls \(u\), disturbances \(\eta\), observations \(Y\), and uncertain parameters \(\theta\).

\[
\boxed{\mathcal M(X)\dot X=\mathcal F(X,Z,m,u,\eta;\theta)}
\]

\[
\boxed{\varepsilon\dot Z=\mathcal G(X,Z,m,u,\eta;\theta)}
\]

\[
\boxed{m^+=\Phi(X,Z,m,\eta,u)}.
\]

## 2. Mathematical-physical foundation

Start from:

\[
\boxed{\text{Conservation}+\text{Constitutive Relations}+\text{Dissipation}+\text{Constraints}+\text{Interfaces}.}
\]

Generic conservation:

\[
\frac{\partial q}{\partial t}+\nabla\cdot J_q=s_q.
\]

Constitutive relation:

\[
J_q=\mathcal C(q,\nabla q,\theta).
\]

Energy/storage balance template:

\[
\frac{dH}{dt}=P_{in}-P_{out}-\mathcal D(X),\qquad \mathcal D(X)\ge0.
\]

## 3. Foundation questions before resilience

1. Does a solution exist?
2. Is it unique?
3. Are physical constraints/invariants preserved?
4. Is the system positive where required?
5. Is it dissipative/passive where relevant?
6. Is an equilibrium/invariant set stable?
7. Does the solution depend continuously on data/parameters?
8. What bifurcations/mode transitions can occur?

Only after these are addressed should the model be used for inference, resilience, optimization, or AI.

## 4. Observation and knowledge

\[
Y_k=\mathcal H(X_k,Z_k;\theta)+\varepsilon_k.
\]

Questions:

- observability of \(X,Z\),
- identifiability of \(\theta\),
- posterior uncertainty,
- model-form uncertainty,
- prediction under disturbance scenarios.

Bayesian object:

\[
\boxed{p(X,Z,\theta\mid D_{obs})}.
\]

## 5. Disturbance

Introduce generic external disturbance

\[
\eta(t)\in\mathcal D.
\]

The initial theory does not require labeling \(\eta\) as flood, heat, earthquake, cyberattack, demand shock, etc. Those become later instantiations.

## 6. Sustainable–equitable admissibility

\[
\boxed{\mathcal K_{SER}=\mathcal K_{phys}\cap\mathcal K_{func}\cap\mathcal K_{service}\cap\mathcal K_{sus}\cap\mathcal K_{eq}}.
\]

Possible sustainability bounds:

\[
E(X)\le E_{max},\qquad M(X)\le M_{max},\qquad W(X)\le W_{max}.
\]

Possible service/equity floor:

\[
S_g(X)\ge S_g^{min}\quad\forall g.
\]

## 7. Central geometric object

\[
\boxed{\mathcal V_{SER}=\operatorname{Viab}(\mathcal K_{SER})}.
\]

Research questions:

- Is \(\mathcal V_{SER}\) nonempty?
- What is \(\partial\mathcal V_{SER}\)?
- Is it connected?
- How does it change with \(\theta\)?
- How does uncertainty deform it?
- How does control enlarge it?
- How does design enlarge it?
- How does disturbance shrink it?

Proposed viability margin:

\[
\rho_V(x)=\operatorname{dist}(x,\partial\mathcal V_{SER}).
\]

## 8. Recovery

\[
\mathcal C(\mathcal V)=\{x_0:\exists u,\exists T<\infty,\ X(T;x_0,u)\in\mathcal V\}.
\]

\[
\tau_R(x_0)=\inf_u\{T:X(T;x_0,u)\in\mathcal V\}.
\]

Recovery is therefore a capture/reachability problem, not merely a rising performance curve.

## 9. Uncertain viability geometry

If interfaces depend on uncertain parameters \(\theta\):

\[
\mathcal V=\mathcal V(\theta).
\]

A set-distance sensitivity measure is

\[
\boxed{d_H(\mathcal V(\theta_1),\mathcal V(\theta_2))}.
\]

With Bayesian parameter/interface uncertainty:

\[
\theta\sim p(\theta\mid D)
\]

so viability becomes a random/uncertain set:

\[
\boxed{\mathcal V\sim p(\mathcal V\mid D)}.
\]

This is the main bridge to the dynamic-interface inverse problem.

## 10. Decision comes after physics and geometry

\[
a^\star=\arg\min_{a\in\mathcal A}J(a)
\]

subject to acceptable/viable behavior.

Robust example:

\[
\min_a\max_{\eta\in\Xi}J(a,\eta).
\]

Risk-sensitive example:

\[
\min_a\operatorname{CVaR}_\alpha[L(a,\eta)].
\]

Optimization is downstream of mathematical physics, not a substitute for it.

## 11. Only then instantiate infrastructure

After the abstract theory is developed, introduce a domain mapping such as

\[
\mathfrak S=\mathfrak S_P\oplus\mathfrak S_W\oplus\mathfrak S_T\oplus\mathfrak S_{SW}.
\]

Then map generic quantities to sector-specific physical variables, constitutive laws, interface mechanisms, services, hazards, and controls.

This makes infrastructure an **instantiation of the theory**, not the definition of the theory.

## 12. Suggested thesis parts

### Part I — Mathematical-Physical Foundations

1. Sustainable resilient systems as mathematical objects
2. Conservation, constitutive relations, and coupled dynamics
3. Well-posedness, stability, and dynamic interfaces

### Part II — Knowledge and Uncertainty

4. Observation, observability, and inverse problems
5. Identifiability and Bayesian uncertainty

### Part III — Disturbance and Survival Geometry

6. Disturbance, hybrid transitions, and loss
7. Sustainable/equitable admissibility
8. Viability, reachability, and recovery

### Part IV — Engineering and Decision

9. Control and lifecycle intervention
10. Multiobjective sustainable decision

### Part V — Infrastructure Instantiation

11. Map the abstract theory to a selected infrastructure demonstrator
12. Numerical/empirical tests and falsification of the selected propositions

## 13. One-sentence research program

> **Develop a mathematical-physics theory for the observation, evolution, sustainable viability, disturbance response, recovery, and lifecycle control of dynamically coupled physical systems under uncertainty, and instantiate the theory for resilient infrastructure.**
