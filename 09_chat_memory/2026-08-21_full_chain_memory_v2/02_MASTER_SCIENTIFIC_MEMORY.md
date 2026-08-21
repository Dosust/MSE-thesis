# Master Scientific Memory — Six Chains, Three Thesis Types, and Mathematical Objects

## 1. Broad chain

\[
\boxed{\text{Foundations}\rightarrow\text{Representation}\rightarrow\text{Dynamics}\rightarrow\text{Resilience}\rightarrow\text{Control}\rightarrow\text{Design}\rightarrow\text{Optimization}\rightarrow\text{Decision/Policy}}
\]

Cross-cutting branches:
\[
\boxed{\text{Inverse Problems / Identification}}\qquad+\qquad\boxed{\text{Uncertainty Quantification}}
\]

## 2. Six scientific chains

### Chain I — Physical System / Mathematical Physics
\[
\boxed{\text{Physical Laws}\to\text{Structure}\to\text{Interfaces}\to\text{States/Flows}\to\text{Dynamics}\to\text{Cascades}}
\]
Question: **What is the system and how does it evolve?**

Working stacked state:
\[
X(t)=\begin{bmatrix}X_P(t)\\X_W(t)\\X_T(t)\\X_{SW}(t)\end{bmatrix}.
\]

Representative sector physics already exist in the literature: power-system swing dynamics, hydraulic continuity/head-loss equations, traffic conservation PDEs, waste stock-flow dynamics, and network cascade models.

Thesis-integrating interface notation:
\[
\boxed{m_{ij}(t)=\text{state of the cross-infrastructure interface }i\leftrightarrow j.}
\]

Unified working dynamics:
\[
\boxed{\mathcal M(X)\dot X=\mathcal F(X,M,\eta,u;\theta)}
\]
or
\[
\boxed{\dot X=F(X,M,\eta,u;\theta)}.
\]

A schematic decomposition is
\[
F(X,M)=\begin{bmatrix}F_P(X_P)\\F_W(X_W)\\F_T(X_T)\\F_{SW}(X_{SW})\end{bmatrix}+C(X,M).
\]
This decomposition is integrating notation, not one literature equation.

### Chain II — Observation / Identification / Estimation / UQ / Prediction
\[
\boxed{\text{Observe}\to\text{Identify}\to\text{Estimate}\to\text{UQ}\to\text{Predict}}
\]
Question: **What can be inferred from measurements, and how uncertain is that knowledge?**

Observation model:
\[
\boxed{y_k=h(X_k,\theta)+\varepsilon_k.}
\]

Representative state-space model:
\[
x_{k+1}=Ax_k+Bu_k+w_k,\qquad y_k=Hx_k+v_k.
\]

Regularized inverse problem:
\[
\boxed{\hat\theta=\arg\min_\theta\|H(X_\theta)-y^{obs}\|^2+\lambda\mathcal R(\theta).}
\]

Identifiability question:
\[
\mathcal G(\theta_1)=\mathcal G(\theta_2)\Rightarrow\theta_1=\theta_2?
\]

Bayesian form:
\[
\boxed{p(\theta\mid y)\propto p(y\mid\theta)p(\theta).}
\]

Outputs:
\[
\hat G,\quad\hat\theta,\quad\Sigma_\theta.
\]

Important novelty guardrail: Bayesian reconstruction of interdependent infrastructure topology from cascading failures already exists. The stronger candidate question is how inference uncertainty changes downstream viability/recoverability predictions.

### Chain III — Hazard / Damage / Failure / Consequence
\[
\boxed{\xi\to\eta\to D\to\text{failure}\to\text{cascade}\to\text{functionality loss}\to\text{service loss}\to\text{consequence}}
\]

Ontological rules:
- forcing \(\xi\) is not realized hazard \(\eta\);
- hazard is not damage;
- damage is not failure;
- component functionality is not population service.

Working service mapping:
\[
\boxed{Y(t)=\pi(X(t),M(t)).}
\]
This mapping is a thesis-integrating object that forces explicit separation between physical state and delivered service.

### Chain IV — Resilience / Viability / Reachability / Recovery
\[
\boxed{\text{State}\to\text{Admissibility}\to\text{Viability}\to\text{Reachability}\to\text{Resilience}\to\text{Recovery}}
\]

Working admissible set:
\[
\boxed{K=K_{\rm phys}\cap K_{\rm service}\cap K_{\rm sus}\cap K_{\rm eq}.}
\]
The exact four-way intersection is a thesis-integrating construction.

Viability kernel:
\[
\boxed{\operatorname{Viab}_K(F)=\{x_0\in K:\exists u(\cdot),\ x(t)\in K\ \forall t\}.}
\]

Reachability/HJ representative form:
\[
\partial_tV+\min_u\max_\eta\{\nabla V\cdot f(x,u,\eta)\}=0,
\qquad\mathcal R(t)=\{x:V(x,t)\le0\}.
\]

Recovery/capture concept:
\[
\mathcal C_K(C)=\{x_0\in K:\exists u,T<\infty,\ x(t)\in K,\ x(T)\in C\}.
\]

Minimum recovery time:
\[
T_R(x_0)=\inf\{T:x(T)\in C\}.
\]

Critical distinction:
\[
\boxed{\text{resilience metric}\neq\text{viability kernel}\neq\text{recoverability set}.}
\]

HJ viability has already been used in infrastructure, so this cannot be claimed as first use.

### Chain V — Control / Design / Operation / Adaptation / Optimization
\[
\boxed{\text{Control}\to\text{Operation}\to\text{Restoration}\to\text{Design}\to\text{Adaptation}\to\text{Optimization}}
\]

Controlled dynamics:
\[
\dot X=F(X,M,\eta,u;\theta).
\]

Representative finite-horizon control problem:
\[
\boxed{u^*=\arg\min_{u(\cdot)}\left[\int_0^T\ell(X,u)\,dt+\phi(X(T))\right]}
\]
subject to the dynamics and admissibility constraints.

Design variable:
\[
d=(\text{topology, capacity, redundancy, storage, interface architecture, ...}).
\]
Then
\[
\mathcal V=\mathcal V(d).
\]

A candidate resilience-by-design objective is
\[
\boxed{d^*=\arg\max_d\Phi(\mathcal V(d),\mathcal C(d),T_R(d),C(d),E(d),I_{eq}(d)).}
\]
This is an integrating/candidate formulation. Restoration optimization itself is already mature literature.

### Chain VI — Sustainability / Equity / Decision
\[
\boxed{\text{Evaluate}\to\text{Constrain}\to\text{Trade off}\to\text{Decide}\to\text{Implement}\to\text{Learn}}
\]

Key rule:
\[
\boxed{\text{sustainability}\neq\text{resilience}.}
\]

Working hard constraints can include
\[
E_{carbon}(X,u,d)\le E_{max},\qquad S_g(X)\ge S_g^{min},\qquad \max_{g,h}|S_g-S_h|\le\Delta_{max}.
\]

Decision/optimization may yield a Pareto set rather than one unique optimum.

## 3. Current candidate cross-chain scientific center

\[
\boxed{\mathcal D_{obs}\to(\hat G,\hat\theta,\Sigma_\theta)\to M(t)\to F_{dyn}\to\mathcal V(\theta)}
\]

Candidate set-valued inference error:
\[
\boxed{E_{inv}=d_H\big(\mathcal V(\theta^\star),\mathcal V(\hat\theta)\big).}
\]

Candidate timescale ratio:
\[
\boxed{\Pi_M=\frac{\tau_{interface}}{\tau_{system/hazard}}.}
\]

Candidate quasi-static error:
\[
\boxed{E_{qs}(\Pi_M)=d_H\big(\mathcal V_{dyn}(\Pi_M),\mathcal V_{qs}\big).}
\]

Candidate viability sensitivity:
\[
\boxed{S_j^{\mathcal V}=\lim_{\delta\to0}\frac{d_H[\mathcal V(\theta),\mathcal V(\theta+\delta e_j)]}{|\delta|}.}
\]
These are candidate thesis-integrating mathematical objects; theorem conditions and global novelty remain to be established.

## 4. Three end-to-end thesis architectures

### Type I — Resilience-Centered Mathematical Physics
Purpose: **UNDERSTAND**.
\[
\boxed{(X,M,\eta)\to F\to K\to\mathcal V\to\mathcal C\to u}
\]
Primary objects: \(\mathcal V,\partial\mathcal V,\mathcal C\).

### Type II — Identification / Digital Twin
Purpose: **LEARN / INFER**.
\[
\boxed{\mathcal D_{obs}\to(\hat G,\hat\theta,\Sigma)\to\hat F\to\hat{\mathcal V}\to\hat{\mathcal C}\to u^*}
\]
Primary objects: \(\hat G,\hat\theta,\Sigma_\theta\).

### Type III — Resilience-by-Design
Purpose: **BUILD / OPTIMIZE**.
\[
\boxed{d\to F_d\to K(d)\to\mathcal V(d)\to u^*(d)\to J(d)\to d^*}
\]
Primary objects: \(u^*,d^*,a^*\).

**Selection status:** all three remain alternatives. No final type is frozen.

## 5. Unified long-term program

\[
\boxed{\underbrace{\mathcal D_{obs}\to(\hat G,\hat\theta,\Sigma)}_{\text{Type II — LEARN}}\to\underbrace{F\to K\to\mathcal V\to\mathcal C}_{\text{Type I — UNDERSTAND}}\to\underbrace{u^*\to d^*\to a^*}_{\text{Type III — BUILD}}}
\]

This is a coherent long-term research program and may exceed one normal MSE thesis unless deliberately reduced.

## 6. Working sectors and demonstrator

Working coupled sectors:
\[
\boxed{P-W-T-SW}
\]
Power, Water, Transportation, Solid Waste.

Climate/urban flooding is the current demonstrator/forcing context. It is not automatically the mathematical novelty.

## 7. Well-posedness hierarchy

A mathematically serious model should separate:
\[
\boxed{\text{Model definition}\to\text{Existence}\to\text{Uniqueness}\to\text{Stability}\to\text{Sensitivity}\to\text{Identifiability}\to\text{Computability}\to\text{Validation}}
\]

Different uniqueness questions must not be conflated: physical trajectory, inverse identification, HJ viscosity solution, optimal control, and optimal design.
