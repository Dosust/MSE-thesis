# Six-Chain Scientific Ontology and Core Equations

## Chain I — Physical-System Chain

**Question:** What mathematical object represents the physical system itself?

\[
\boxed{\text{Physical Laws}\to\text{Structure}\to\text{Interdependencies}\to\text{Interfaces}\to\text{States/Flows}\to\text{Dynamics}}
\]

Generic conservation template:

\[
\boxed{\frac{\partial q}{\partial t}+\nabla\cdot J_q=s_q}
\]

with constitutive relation

\[
\boxed{J_q=\mathcal C(q,\nabla q,\theta)}.
\]

Abstract multilayer structure:

\[
\mathcal G=\{G_1,\ldots,G_N,\mathcal I\}.
\]

Dynamic interface:

\[
\boxed{\Gamma_{ij}=\mathcal I_{ij}(X_i,X_j,Z_{ij},\eta;\theta_{ij})}
\]

\[
\boxed{\dot Z_{ij}=G_{ij}(X_i,X_j,Z_{ij},u,\eta)}.
\]

Coupled state:

\[
X=[X_1^\top,\ldots,X_N^\top]^\top.
\]

Generic hybrid dynamics:

\[
\boxed{\mathcal M(X)\dot X=\mathcal F(X,Z,m,u,\eta;\theta)}
\]

\[
\boxed{\varepsilon\dot Z=\mathcal G(X,Z,m,u,\eta;\theta)}
\]

\[
\boxed{m^+=\Phi(X,Z,m,\eta,u)}.
\]

### Required mathematical checks

- existence,
- uniqueness,
- positivity/physical admissibility,
- invariants and conservation,
- dissipation/passivity where applicable,
- stability,
- continuous dependence,
- bifurcation/regime switching,
- numerical consistency.

### Literature anchors

Rinaldi, Peerenboom & Kelly (2001); Ouyang (2014); Boccaletti et al. (2014); Kivelä et al. (2014); Buldyrev et al. (2010); Gao, Barzel & Barabási (2016).

---

## Chain II — Observation–Inference–Prediction

**Question:** What do we know about the system, and with what uncertainty?

\[
\boxed{\text{Observe}\to\text{Observability}\to\text{Identify}\to\text{Identifiability}\to\text{Estimate}\to\text{UQ}\to\text{Predict}}
\]

Observation:

\[
\boxed{Y(t)=H(X(t),Z(t);\theta)+\varepsilon_Y(t)}.
\]

Regularized inverse problem:

\[
\boxed{\widehat\theta=\arg\min_\theta\left[\|Y^{obs}-\mathcal G(\theta)\|^2_{\Sigma^{-1}}+\lambda\mathcal R(\theta)\right]}.
\]

Identifiability:

\[
\boxed{\mathcal G(\theta_1)=\mathcal G(\theta_2)\Longrightarrow\theta_1=\theta_2?}
\]

Bayesian inverse problem:

\[
\boxed{p(\theta\mid Y)\propto p(Y\mid\theta)p(\theta)}.
\]

Dynamic state estimation target:

\[
\boxed{p(X_t\mid Y_{0:t})}.
\]

Forecast:

\[
\boxed{p(X_{t+\tau}\mid Y_{0:t},\eta_{t:t+\tau})}.
\]

Central output:

\[
\boxed{p(X,Z,\theta\mid D_{\mathrm{obs}})}.
\]

### Uncertainty classes

- aleatory,
- epistemic,
- structural/model-form,
- scenario/decision uncertainty.

### Literature anchors

Tarantola; Stuart (2010); system-identification/Bayesian updating literature; infrastructure inverse-problem precedents.

---

## Chain III — Hazard–Failure–Consequence

**Question:** What transforms an external disturbance into physical and societal loss?

\[
\boxed{\text{Forcing}\to\text{Hazard}\to\text{Exposure}\to\text{Damage}\to\text{Failure}\to\text{Cascade}\to\text{Function}\to\text{Service}\to\text{Consequences}}
\]

Forcing to realized hazard:

\[
\boxed{\xi(t)\to\eta(t)}.
\]

Fragility family:

\[
\boxed{P(D_i\ge d_s\mid IM)=\Phi\!\left(\frac{\ln IM-\ln\mu_{i,d_s}}{\beta_{i,d_s}}\right)}.
\]

Hybrid mode transition:

\[
m_i(t^-)\to m_i(t^+).
\]

Topology/dynamics may change:

\[
\boxed{F(X;A^-)\to F(X;A^+)}.
\]

Function/service mapping:

\[
\boxed{X\to F_{\mathrm{func}}\to S_g\to C_g}.
\]

Service mapping:

\[
\boxed{S(t)=\Psi(X(t),m(t),Z(t))}.
\]

Service deficit:

\[
D_g(t)=[S_g^{req}-S_g(t)]_+.
\]

Cumulative consequence:

\[
\boxed{L=\int_0^T\sum_g w_gD_g(t)\,dt}.
\]

Maintain:

\[
\boxed{\text{physical damage}\neq\text{functionality}\neq\text{service delivered}\neq\text{societal consequence}}.
\]

### Literature anchors

Buldyrev et al. (2010); hazard/fragility literature; Mühlhofer et al. (2023); people-centric service-resilience work including Zhang et al. (2026).

---

## Chain IV — Viability–Resilience–Recovery–Control

**Question:** Can the system remain acceptable, avoid unacceptable states, and recover?

\[
\boxed{\text{Admissibility}\to\text{Viability}\to\text{Reachability}\to\text{Resilience}\to\text{Recoverability}\to\text{Control}}
\]

Admissible set:

\[
\boxed{\mathcal K_{SER}=\mathcal K_{phys}\cap\mathcal K_{service}\cap\mathcal K_{sus}\cap\mathcal K_{eq}}.
\]

Viability kernel:

\[
\boxed{\operatorname{Viab}_{\mathcal K}=\{x_0\in\mathcal K:\exists u(\cdot),\ X(t;x_0,u)\in\mathcal K\ \forall t\ge0\}}.
\]

Representative HJ/HJI form:

\[
\boxed{\partial_tV+H(x,\nabla V)=0}
\]

with one common dynamic-game Hamiltonian convention

\[
H(x,p)=\min_u\max_dp^\top f(x,u,d).
\]

Recovery/capture basin:

\[
\boxed{\mathcal C_R=\{x_0:\exists u,\exists T<\infty,\ X(T;x_0,u)\in\mathcal V\}}.
\]

Minimum recovery time:

\[
\boxed{\tau_R(x_0)=\inf_u\{T:X(T;x_0,u)\in\mathcal V\}}.
\]

Viability-control condition conceptually:

\[
F(x,u)\in T_{\mathcal K}(x),
\]

and

\[
\boxed{\mathcal U_V(x)=\{u:F(x,u)\in T_{\mathcal K}(x)\}}.
\]

Proposed viability margin:

\[
\boxed{\rho_V(x)=\operatorname{dist}(x,\partial\mathcal V)}.
\]

### Literature anchors

Aubin/viability theory; Mitchell, Bayen & Tomlin (2005); Bruneau et al. (2003); Hosseini et al. (2016); HJ/WtE viability work discussed in 2026 literature.

---

## Chain V — Engineering Action / Lifecycle

**Question:** Given Chains I–IV, what can engineers change?

\[
\boxed{\text{Design}\to\text{Construct}\to\text{Commission}\to\text{Operate}\to\text{Maintain}\to\text{Restore}\to\text{Retrofit}\to\text{Adapt}\to\text{Replace/Transform}\to\text{Decommission}\to\text{Reuse/Recycle}}
\]

Design variables:

\[
d=(d_{topology},d_{capacity},d_{redundancy},d_{storage},d_{interface},\ldots).
\]

Design changes dynamics:

\[
\boxed{\dot X=F(X,Z,u,\eta;d)}.
\]

Thus

\[
\boxed{d\to\mathcal V(d),\qquad d\to\mathcal C(d)}.
\]

Operations:

\[
\boxed{u(t)=\pi(X(t))}.
\]

Restoration optimization template:

\[
\boxed{\min_r\int_0^TL_{service}(X(t),r(t))\,dt+C_{repair}(r)}
\]

subject to system dynamics, resource, precedence, safety, and feasibility constraints.

Planning/adaptation:

\[
\boxed{d_0\to d_1\to d_2\to\cdots}.
\]

### Multi-timescale interpretation

- fast feedback/control: seconds–hours,
- operational dispatch: hours–days,
- restoration: days–months,
- maintenance/retrofit: months–years,
- planning/adaptation: years–decades.

### Literature anchors

Ouyang & Dueñas-Osorio interface-topology design; Nurre et al.; Cavdaroglu et al.; Ouyang & Wang (2015); restoration/resource-allocation literature; OR/optimal control/adaptation literature.

---

## Chain VI — Sustainability–Evaluation–Decision

**Question:** Which technically feasible solution should actually be chosen?

\[
\boxed{\text{Evaluate}\to\text{Trade off}\to\text{Decide}\to\text{Implement}\to\text{Learn}}.
\]

Vector objective:

\[
\boxed{
J(d,u)=
\begin{bmatrix}
C_{economic}\\
E_{carbon}\\
L_{service}\\
I_{inequity}\\
T_{recovery}\\
R_{risk}
\end{bmatrix}}
\]

Sustainability constraints may be hard constraints:

\[
E_{carbon}\le E_{max},\qquad M_{resource}\le M_{max}.
\]

Equity floor:

\[
\boxed{S_g(t)\ge S_g^{min}\quad\forall g}.
\]

Multiobjective problem:

\[
\boxed{\min_d(J_1(d),\ldots,J_k(d))}.
\]

Pareto set:

\[
\boxed{\mathcal P^\star}.
\]

Expected-utility decision:

\[
\boxed{a^\star=\arg\max_a\mathbb E_\xi[U(a,\xi)]}.
\]

Risk-sensitive alternative:

\[
\boxed{\min_a\operatorname{CVaR}_\alpha[L(a,\xi)]}.
\]

Robust alternative:

\[
\boxed{\min_a\max_{\xi\in\Xi}L(a,\xi)}.
\]

Learning closes the loop:

\[
\boxed{p(\theta\mid D_{0:t})\to p(\theta\mid D_{0:t+1})}.
\]

### Literature anchors

Coleman et al. (2024); sustainable infrastructure MCDA; DMDU/adaptive pathways; economics/game theory/governance literature.

---

# Coupled architecture

The scientifically correct relationship is not one long chain. A useful abstraction is

\[
I\to III\to IV\to V\to VI
\]

while

\[
II\leftrightarrow I,III,IV,V
\]

and

\[
VI\to IV
\]

because societal sustainability/equity requirements help define the admissible set used in viability analysis.

The closed loop is therefore:

\[
\boxed{\text{physics}\to\text{observation}\to\text{stress}\to\text{viability}\to\text{action}\to\text{decision}\to\text{new observations}.}
\]
