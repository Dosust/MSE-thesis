# Source Snapshot — Six-Chain Literature-Grounded Architecture

This is a distilled archival snapshot of the long-form six-chain source supplied in the 2026-08-21 session. It preserves the core architecture, equations, and literature anchors needed for future recall. It is not labeled as a verbatim copy of the entire uploaded document.

## Chain/layer distinction

A **chain** is a family of scientific questions. A **layer** is a distinct mathematical/physical stage inside that family. Optimization, UQ, numerical analysis, ML, and statistics are cross-cutting methods rather than separate physical stages.

---

# Chain I — Physical System

\[
\boxed{\text{Physical Laws}\to\text{Structure}\to\text{Interdependencies}\to\text{Interfaces}\to\text{States/Flows}\to\text{Dynamics}}
\]

Generic conservation law:

\[
\frac{\partial q}{\partial t}+\nabla\cdot J_q=s_q.
\]

Multilayer structure:

\[
\mathcal G=\{G_P,G_W,G_T,G_{SW},\mathcal I\}.
\]

Block adjacency/coupling representation:

\[
\mathcal A=
\begin{bmatrix}
A_{PP}&A_{PW}&A_{PT}&A_{P,SW}\\
A_{WP}&A_{WW}&A_{WT}&A_{W,SW}\\
A_{TP}&A_{TW}&A_{TT}&A_{T,SW}\\
A_{SW,P}&A_{SW,W}&A_{SW,T}&A_{SW,SW}
\end{bmatrix}.
\]

Interface mechanism:

\[
I_{ij}:(X_i,X_j,Z_{ij},\eta)\mapsto\Gamma_{ij}.
\]

Key distinction:

\[
\boxed{\text{connection}\neq\text{interdependency}\neq\text{interface mechanism}.}
\]

Coupled state:

\[
X(t)=\begin{bmatrix}X_P(t)\\X_W(t)\\X_T(t)\\X_{SW}(t)\end{bmatrix}.
\]

Dynamics:

\[
M(X)\dot X=F(X,Z,m,u,\eta;\theta),
\]

\[
\varepsilon\dot Z=G(X,Z,m,\eta;\theta),
\]

\[
m^+=\Phi(X,Z,m,\eta).
\]

Representative literature anchors: Rinaldi, Peerenboom & Kelly (2001); Ouyang (2014); Boccaletti et al. (2014); Kivelä et al. (2014); Gao et al.; multilayer/interdependency literature.

---

# Chain II — Observation–Inference–Prediction

\[
\boxed{\text{Observe}\to\text{Identify}\to\text{Estimate}\to\text{Quantify Uncertainty}\to\text{Predict}}
\]

Observation:

\[
Y(t)=H(X(t),Z(t);\theta)+\varepsilon_Y(t).
\]

Regularized identification:

\[
\widehat\theta=\arg\min_\theta\left[\|Y^{obs}-\mathcal G(\theta)\|^2_{\Sigma^{-1}}+\lambda\mathcal R(\theta)\right].
\]

Identifiability:

\[
\mathcal G(\theta_1)=\mathcal G(\theta_2)\Rightarrow\theta_1=\theta_2?
\]

Bayesian inversion:

\[
p(\theta\mid Y)\propto p(Y\mid\theta)p(\theta).
\]

Filtering:

\[
p(X_t\mid Y_{0:t}).
\]

Prediction:

\[
p(X_{t+\tau}\mid Y_{0:t},\eta_{t:t+\tau}).
\]

Representative anchors: Tarantola; Stuart (2010); infrastructure system-identification and Bayesian-updating literature.

---

# Chain III — Hazard–Failure–Consequence

\[
\boxed{\text{Hazard}\to\text{Exposure}\to\text{Damage}\to\text{Failure}\to\text{Cascade}\to\text{Service Loss}\to\text{Consequences}}
\]

Forcing/hazard separation:

\[
\xi(t)\to\eta(t).
\]

Fragility family:

\[
P(D_i\ge d_s\mid IM)=\Phi\left(\frac{\ln IM-\ln\mu_{i,d_s}}{\beta_{i,d_s}}\right).
\]

Failure-induced switching:

\[
F(X;A^-)\to F(X;A^+).
\]

Cascade:

\[
m_i\to X_j\to m_j\to X_k\to\cdots
\]

Service mapping:

\[
S(t)=\Psi(X(t),m(t),Z(t)).
\]

Service deficit:

\[
D_i(t)=[S_i^{req}-S_i(t)]_+.
\]

Cumulative consequence:

\[
L=\int_0^T\sum_iw_iD_i(t)\,dt.
\]

Representative anchors: Buldyrev et al. (2010); Mühlhofer et al. (2023); fragility/multihazard literature; service-resilience literature.

---

# Chain IV — Viability–Resilience–Recovery–Control

\[
\boxed{\text{Admissibility}\to\text{Viability}\to\text{Reachability}\to\text{Resilience}\to\text{Recoverability}\to\text{Control}}
\]

Admissible region:

\[
K_R=K_{phys}\cap K_{service}\cap K_{sus}\cap K_{eq}.
\]

Viability kernel:

\[
\operatorname{Viab}_{K_R}=\{x_0\in K_R:\exists u(\cdot),\ X(t;x_0,u)\in K_R\ \forall t\ge0\}.
\]

Representative HJ equation:

\[
\partial_tV+H(x,\nabla V)=0.
\]

One common dynamic-game Hamiltonian:

\[
H(x,p)=\min_u\max_dp^\top f(x,u,d).
\]

Recovery/capture:

\[
\mathcal C_R=\{x_0:\exists u,\exists T<\infty,\ X(T;x_0,u)\in\mathcal V_R\}.
\]

Recovery time:

\[
\tau_R(x_0)=\inf_u\{T:X(T;x_0,u)\in\mathcal V_R\}.
\]

Viability control condition:

\[
F(x,u)\in T_{K_R}(x).
\]

Representative anchors: Aubin/viability theory; Mitchell, Bayen & Tomlin (2005); Bruneau et al. (2003); Cimellaro et al.; Hosseini et al. (2016).

---

# Chain V — Engineering Action

\[
\boxed{\text{Design}\to\text{Operate}\to\text{Maintain}\to\text{Restore}\to\text{Plan}\to\text{Adapt}}
\]

Design vector:

\[
d=(d_{topology},d_{capacity},d_{redundancy},d_{storage},d_{interface}).
\]

Design-dependent dynamics:

\[
\dot X=F(X,Z,u,\eta;d).
\]

Thus:

\[
d\to\mathcal V_R(d).
\]

Operation:

\[
u(t)=\pi(X(t)).
\]

Restoration optimization template:

\[
\min_r\int_0^T L_{service}(X(t),r(t))dt+C_{repair}(r)
\]

subject to dynamics, resource, and precedence constraints.

Adaptation under nonstationarity:

\[
d_0\to d_1\to d_2\to\cdots.
\]

Representative anchors: Ouyang & Dueñas-Osorio; Cavdaroglu et al.; Nurre et al.; Ouyang & Wang (2015); restoration and resilience-optimization literature.

---

# Chain VI — Sustainability–Evaluation–Decision

\[
\boxed{\text{Evaluate}\to\text{Trade off}\to\text{Decide}\to\text{Implement}\to\text{Learn}}
\]

Evaluation vector:

\[
J(d,u)=\begin{bmatrix}
C_{economic}\\E_{carbon}\\L_{service}\\I_{inequity}\\T_{recovery}\\R_{risk}
\end{bmatrix}.
\]

Sustainability as admissibility:

\[
E_{carbon}\le E_{max},\qquad M_{resource}\le M_{max}.
\]

Equity floor:

\[
S_g(t)\ge S_g^{min}\quad\forall g.
\]

Multiobjective decision:

\[
\min_d(J_1(d),\ldots,J_k(d))
\]

with Pareto set

\[
\mathcal P^\star.
\]

Expected utility:

\[
a^\star=\arg\max_a\mathbb E_\xi[U(a,\xi)].
\]

CVaR alternative:

\[
\min_a\operatorname{CVaR}_\alpha[L(a,\xi)].
\]

Robust alternative:

\[
\min_a\max_{\xi\in\Xi}L(a,\xi).
\]

Learning:

\[
p(\theta\mid D_{0:t})\to p(\theta\mid D_{0:t+1}).
\]

Representative anchors: Coleman et al. (2024); sustainability/MCDA literature; DMDU/adaptive pathways; economics/governance/game-theory literature.

---

# Coupled architecture and maturity map

The source emphasized that the chains are coupled rather than sequential:

\[
I\to III\to IV\to V\to VI,
\]

\[
II\leftrightarrow I,III,IV,V,
\]

and

\[
VI\to IV
\]

because sustainability/equity decisions help define the admissible region.

Working maturity assessment preserved from the source:

- interdependency taxonomy — very mature,
- multilayer representation — very mature,
- cascading failure — very mature,
- classical resilience metrics — very mature,
- restoration optimization — very mature,
- viability/HJ as general mathematics — very mature,
- inverse problems as general mathematics — very mature,
- equity metrics — growing/mature in parts,
- dynamic interface identification — much narrower,
- interface-identification uncertainty → viability boundaries — much narrower,
- sustainability/equity as hard viability constraints — narrower integration,
- capture/recovery geometry for coupled systems — narrower,
- waste–drainage–flood feedback inside viability analysis — narrower combined problem.

The defensible research space lies in **specific mathematical couplings among mature theories**, not in claiming those mature theories are new.
