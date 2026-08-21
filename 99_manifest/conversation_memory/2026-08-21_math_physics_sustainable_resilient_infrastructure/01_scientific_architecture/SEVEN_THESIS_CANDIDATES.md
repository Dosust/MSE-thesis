# Seven High-Rigor Thesis Candidates

The seven candidates are designed for the research ambition:

\[
\boxed{
\text{Mathematics + Physics for Sustainable Resilient Infrastructure}
\quad\text{from foundations to decision-making across the lifecycle}
}
\]

They are **different centers of gravity**, not seven modules that should automatically be combined into one master's thesis.

## Candidate I — Unified Sustainable Viability Theory for Coupled Infrastructure

**Working title:** *Mathematical Physics of Sustainable Infrastructure Viability: A Unified Framework for Coupled Infrastructure Systems Across Disturbance, Recovery, Adaptation and Lifecycle Decision-Making*

Core model:

\[
M(X)\dot X=F(X,Z,u,\eta;\theta),\qquad
X=[X_P,X_W,X_T,X_{SW}]^T.
\]

Service map:

\[
S=\mathcal S(X).
\]

Sustainable/equitable admissible set:

\[
\mathcal K_{\mathrm{sus}}=\{X:S_g(X)\ge S_g^{\min},\;E(X)\le E_{\max},\;C(X)\le C_{\max},\;R(X)\le R_{\max},\;Q_{eq}(X)\ge Q_{\min}\}.
\]

Central object:

\[
\boxed{
\mathcal V_{\mathrm{sus}}
=\{x_0\in\mathcal K_{\mathrm{sus}}:\exists u(\cdot),\;X(t)\in\mathcal K_{\mathrm{sus}}\;\forall t\}
}
\]

Why it matters: one geometric language can connect design, operation, disturbance absorption, recovery, adaptation and end-of-life decisions.

**Best match to the full long-term vision.**

## Candidate II — Dynamic Interface Identification → Viability Uncertainty

**Working title:** *Inverse Mathematical Physics of Coupled Infrastructure: Identifying Dynamic Interfaces and Their Uncertainty Effects on Sustainable Service Viability*

Coupled dynamics:

\[
\dot X_i=f_i(X_i)+\sum_{j\neq i}g_{ij}(X_i,X_j;\theta_{ij}).
\]

Observation/inference:

\[
y_k=H(X_k,\theta)+\varepsilon_k,
\qquad
p(\theta,Z\mid y)\propto p(y\mid\theta,Z)p(\theta,Z).
\]

Identifiability:

\[
\mathcal G(\theta_1)=\mathcal G(\theta_2)\Rightarrow\theta_1=\theta_2?
\]

Uncertainty propagation:

\[
p(\theta\mid y)\rightarrow p(X)\rightarrow p(S)\rightarrow p(\mathcal V).
\]

Possible error metric:

\[
\boxed{
\Delta_{\mathcal V}=d_H[\mathcal V(\theta^*),\mathcal V(\widehat\theta)]
}
\]

**Current strongest thesis-sized narrow gap.**

## Candidate III — Port-Hamiltonian / Energy-Based Mathematical Physics

**Working title:** *A Port-Hamiltonian Mathematical Physics Framework for Sustainable and Resilient Coupled Infrastructure Systems*

Core structure:

\[
\boxed{
\dot x=[J(x)-R(x)]\nabla H(x)+G(x)u,
\quad J^T=-J,
\quad R\succeq0
}
\]

Energy balance:

\[
\dot H=-\nabla H^TR\nabla H+y^Tu.
\]

Sector subsystems may be interconnected through ports:

\[
\Sigma=\Sigma_P\Join\Sigma_W\Join\Sigma_T\Join\Sigma_{SW}.
\]

Mathematical depth: differential geometry, Hamiltonian mechanics, Dirac structures, dissipativity, passivity, Lyapunov stability, nonlinear control, operator/PDE theory.

Strength: deepest pure mathematical-physics candidate.  
Challenge: not all transport/social/equity phenomena fit energy-based structure naturally.

## Candidate IV — Stochastic Hybrid Multiscale Infrastructure Physics

**Working title:** *Stochastic Hybrid Mathematical Physics of Multi-Infrastructure Resilience Under Climate and Operational Uncertainty*

Continuous state + discrete mode:

\[
dX_t=f_{m_t}(X_t,u_t)dt+G_{m_t}(X_t)dW_t,
\]

with mode transitions such as:

\[
P[m(t+\Delta t)=j\mid m(t)=i]=q_{ij}(X,t)\Delta t.
\]

Topology-changing failure:

\[
A^-\rightarrow A^+.
\]

Methods: SDEs, stochastic/hybrid systems, Markov jump systems, rare-event theory, large deviations, percolation, switching control.

Strength: naturally represents normal → degraded → failed → isolated → repaired lifecycle modes.

## Candidate V — Lifecycle Optimal Control and Operations Research

**Working title:** *Mathematics for Optimal Sustainable Infrastructure Lifecycle Decisions Under Dynamic Risk and Deep Uncertainty*

Decision state:

\[
X_t=\{\text{condition, capacity, service, environment, risk}\}.
\]

Action set:

\[
a_t\in\{\text{operate, inspect, maintain, repair, replace, expand, adapt, retire}\}.
\]

Transition:

\[
X_{t+1}\sim P(X_{t+1}\mid X_t,a_t,\xi_t).
\]

Lifecycle objective:

\[
\boxed{
\min_\pi E_\pi\left[\sum_{t=0}^{T}\gamma^t(C_t+\lambda_RR_t+\lambda_EE_t+\lambda_SS_t^{deficit})\right]
}
\]

Methods: dynamic programming, MDP/POMDP, robust/stochastic optimization, real options, network optimization, bilevel/multiobjective optimization, optimal control.

Strength: strongest direct utility for planners, utilities, asset managers, government and finance.  
Challenge: becomes OR rather than mathematical physics unless physics/viability constraints remain central.

## Candidate VI — People-Centric Sustainable Service Viability

**Working title:** *Equity-Constrained Mathematical Physics of Critical-Service Viability in Interdependent Infrastructure Systems*

Physical-to-human chain:

\[
X(t)\rightarrow F(t)\rightarrow S_g(t)\rightarrow C_g(t).
\]

Service adequacy example:

\[
S_g(t)=\frac{D_g^{served}(t)}{D_g^{required}(t)}.
\]

Equity-constrained admissibility:

\[
\mathcal K_{eq}=\{X:S_g(X)\ge S_g^{\min}\;\forall g,\;E(X)\le E_{max},\;C(X)\le C_{max}\}.
\]

Then:

\[
\mathcal V_{eq}=\operatorname{Viab}(\mathcal K_{eq}).
\]

Key idea: equity becomes a mathematical constraint on admissible state geometry, not a decorative post-hoc score.

## Candidate VII — Verified Scientific-AI Infrastructure Digital Twin

**Working title:** *Verified Physics-Informed Digital Twins for Sustainable Infrastructure: Learning, Uncertainty, Viability and Safe Decision-Making*

Architecture:

\[
\text{Physical System}\leftrightarrow\text{Sensors}\leftrightarrow\text{Inverse Model}\leftrightarrow\text{Scientific AI}\leftrightarrow\text{Formal Safety}\leftrightarrow\text{Decision}.
\]

Physics-informed learning:

\[
\mathcal L=\lambda_D\mathcal L_D+\lambda_P\|\mathcal N[u_\theta]-f\|^2+\lambda_B\mathcal L_B.
\]

Operator learning:

\[
\mathcal G_\theta:a(\cdot)\mapsto u(\cdot).
\]

Verification requirement:

\[
\|\mathcal G(a)-\mathcal G_\theta(a)\|\le\varepsilon(a),
\qquad
P[X_t^{AI}\in\mathcal K\;\forall t]\ge1-\delta.
\]

Core principle:

\[
\boxed{
\text{AI learns}\rightarrow\text{physics constrains}\rightarrow\text{UQ quantifies}\rightarrow\text{formal mathematics certifies}
}
\]

Strength: most future-facing.  
Challenge: too broad for one master's thesis unless heavily reduced.

# Comparative interpretation

## Whole lifecycle coverage
1. Unified Sustainable Viability Theory
2. Lifecycle Optimal Control / OR
3. Verified Scientific-AI Digital Twin
4. Stochastic Hybrid Multiscale Physics
5. People-Centric Service Viability
6. Dynamic Interface Identification + UQ
7. Port-Hamiltonian Physics

## Deepest mathematical physics
1. Port-Hamiltonian mathematical physics
2. Stochastic hybrid multiscale physics
3. Unified viability theory
4. Dynamic interface inverse problem
5. HJ/service viability
6. Lifecycle optimal control
7. Scientific-AI twin

## Strongest likely originality from current gap work
1. Dynamic Interface Identification → Viability Uncertainty
2. Unified Sustainable Viability Theory
3. People-Centric Sustainable Service Viability
4. Verified Physics/AI Viability Twin
5. Port-Hamiltonian coupled infrastructure
6. Stochastic hybrid lifecycle physics
7. Lifecycle optimal control

## Master's-feasibility interpretation
The most realistic high-rigor thesis-sized focus is Candidate II, followed by Candidate VI, then a carefully reduced Candidate I.

## Three-level research program

**Level A — Master's thesis**  
Observed dynamic interfaces → uncertainty → service viability.

**Level B — PhD-scale mathematical theory**  
Mathematical Physics of Sustainable Infrastructure Viability, generalizing physics → interfaces → dynamics → viability → recovery → lifecycle control.

**Level C — long-term discipline-enabling platform**  
Mathematical Foundations for Sustainable and Resilient Infrastructure Systems, spanning physical laws through identification, uncertainty, risk, service, viability, control, lifecycle engineering and sustainable/equitable decisions.
