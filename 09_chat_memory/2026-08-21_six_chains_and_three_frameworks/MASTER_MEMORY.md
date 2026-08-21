# MASTER MEMORY — Six Chains and Three End-to-End Thesis Frameworks

## 1. Broad research chain

The discussion began from the long sequence

\[
\boxed{
\text{Foundations}
\rightarrow
\text{Representation}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Resilience}
\rightarrow
\text{Control}
\rightarrow
\text{Design}
\rightarrow
\text{Optimization}
\rightarrow
\text{Decision/Policy}
}
\]

with inverse problems and uncertainty quantification treated as cross-cutting rather than confined to one position.

The current thesis was positioned mainly at

\[
\boxed{
\text{Dynamics}
\rightarrow
\textbf{Resilience / Viability}
\rightarrow
\text{Control}
}
\]

with

\[
\boxed{\text{Inverse Problems / Identification}}
\qquad+\qquad
\boxed{\text{Uncertainty Quantification}}
\]

crossing those layers.

The strongest current scientific spine is

\[
\boxed{
\mathcal D_{\rm obs}
\rightarrow
(\hat G,\hat\theta,\Sigma_\theta)
\rightarrow
\mathcal F_{\rm dyn}
\rightarrow
K_{\rm sus,eq}
\rightarrow
\mathcal V_{\rm sus,eq}
\rightarrow
\mathcal C_{\rm sus,eq}
}
\]

with the viability boundary \(\partial\mathcal V\) treated as a central mathematical object.

---

# 2. Six scientific chains

## Chain I — Physical System / Mathematical Physics

\[
\boxed{
\text{Physical Laws}
\rightarrow
\text{System Structure}
\rightarrow
\text{Interdependencies/Interfaces}
\rightarrow
\text{States/Flows}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Cascades}
}
\]

Main question: **What is the system and how does it evolve?**

Representative sector forms include:

Power:
\[
M_i\ddot\delta_i+D_i\dot\delta_i
=
P_i-\sum_j B_{ij}\sin(\delta_i-\delta_j).
\]

Water continuity:
\[
\sum_j q_{ji}-\sum_j q_{ij}=d_i.
\]

Transportation conservation:
\[
\frac{\partial\rho}{\partial t}
+
\frac{\partial Q(\rho)}{\partial x}=0.
\]

Solid-waste stock-flow skeleton:
\[
\dot x=\text{generation}-\text{collection/processing/removal}.
\]

Basic and multilayer structure:
\[
G=(V,E),
\qquad
\mathcal G=(V,E,\mathcal L),
\qquad
\mathcal L=\{P,W,T,SW\}.
\]

Integrating thesis interface notation:
\[
m_{ij}(t)=\text{physical/operational state of interface }i\leftrightarrow j.
\]

Stacked states:
\[
X(t)=
\begin{bmatrix}
X_P(t)\\X_W(t)\\X_T(t)\\X_{SW}(t)
\end{bmatrix},
\qquad M(t)=\{m_{ij}(t)\}.
\]

Unified dynamics:
\[
\boxed{\mathcal M(X)\dot X=\mathcal F(X,M,\eta,u;\theta)}
\]

or

\[
\boxed{\dot X=F(X,M,\eta,u;\theta)}.
\]

A useful decomposition is
\[
F(X,M)=
\begin{bmatrix}
F_P(X_P)\\F_W(X_W)\\F_T(X_T)\\F_{SW}(X_{SW})
\end{bmatrix}
+C(X,M).
\]

Existing literature already covers interdependencies, multilayer representations, overload/dependency cascades, percolation, and dynamic cascading. The thesis therefore cannot claim novelty merely for using coupled networks or cascading failures.

---

## Chain II — Observation / Identification / Inference / Prediction

\[
\boxed{
\text{Observe}
\rightarrow
\text{Estimate}
\rightarrow
\text{Identify}
\rightarrow
\text{Quantify Uncertainty}
\rightarrow
\text{Predict}
}
\]

Main question: **What can actually be learned from measurements?**

Observation model:
\[
\boxed{y_k=h(X_k,\theta)+\varepsilon_k}.
\]

Linear state-space example:
\[
x_{k+1}=Ax_k+Bu_k+w_k,
\qquad y_k=Hx_k+v_k.
\]

State-estimation update:
\[
\hat x_{k|k}
=
\hat x_{k|k-1}
+
K_k(y_k-H\hat x_{k|k-1}).
\]

Regularized inverse problem:
\[
\boxed{
\hat\theta
=
\arg\min_\theta
\|H(X_\theta)-y^{obs}\|^2
+
\lambda\mathcal R(\theta)
}.
\]

Identifiability question:
\[
\mathcal G(\theta_1)=\mathcal G(\theta_2)
\Rightarrow
\theta_1=\theta_2?
\]

Bayesian inference:
\[
\boxed{p(\theta\mid y)\propto p(y\mid\theta)p(\theta)}.
\]

Important outputs:
\[
\hat\theta,\qquad\Sigma_\theta,\qquad\text{credible regions}.
\]

For this thesis the uncertain output may itself be a set:
\[
\theta\mapsto\mathcal V(\theta),
\]
not just a scalar quantity.

Infrastructure-network reconstruction from cascading-failure observations already exists, so novelty cannot be “infer hidden interdependencies.” The stronger question is how inference uncertainty propagates into viability, recoverability, and control trustworthiness.

---

## Chain III — Hazard / Damage / Failure / Consequence

\[
\boxed{
\text{External Forcing}
\rightarrow
\text{Realized Hazard}
\rightarrow
\text{Damage}
\rightarrow
\text{Failure}
\rightarrow
\text{Cascade}
\rightarrow
\text{Functionality Loss}
\rightarrow
\text{Service Consequence}
}
\]

Main question: **How does external stress become service loss?**

Separate climate forcing from realized local hazard:
\[
\boxed{\xi\rightarrow\eta=\mathcal H(\xi,\text{local conditions})}.
\]

Representative fragility form:
\[
P(D\ge d\mid IM)
=
\Phi\left[
\frac{\ln(IM)-\ln(IM_{m,d})}{\beta_d}
\right].
\]

Failure can create a hybrid system:
\[
A(t^-)\rightarrow A(t^+),
\qquad
F(X;A^-)\rightarrow F(X;A^+).
\]

Service mapping:
\[
\boxed{Y(t)=\pi(X(t),M(t))}.
\]

Critical ontology rule:
\[
\boxed{\text{component functionality}\neq\text{service delivered to people}}.
\]

Hazard, damage, failure, cascade, functionality, and service must remain separate objects in the model.

---

## Chain IV — Resilience / Viability / Recovery

\[
\boxed{
\text{Admissible State}
\rightarrow
\text{Viability}
\rightarrow
\text{Reachability}
\rightarrow
\text{Resilience}
\rightarrow
\text{Recoverability}
\rightarrow
\text{Control}
}
\]

Main question: **Which states can survive, remain admissible, or recover?**

Admissible set:
\[
\boxed{
K=K_{\rm phys}
\cap K_{\rm service}
\cap K_{\rm sus}
\cap K_{\rm eq}
}.
\]

Viability kernel:
\[
\boxed{
\operatorname{Viab}_K(F)
=
\{x_0\in K:\exists u(\cdot),\ x(t)\in K,\ \forall t\}
}.
\]

Representative HJ/HJI form:
\[
\boxed{
\partial_tV
+
\min_u\max_\eta
\{\nabla V\cdot f(x,u,\eta)\}=0
}.
\]

A conventional resilience performance measure can be written
\[
R=\frac1T\int_0^TQ(t)\,dt,
\]
but this must not be confused with a viability kernel:
\[
\boxed{\text{resilience scalar}\neq\text{viability geometry}}.
\]

Capture/recovery set:
\[
\boxed{
\mathcal C_K(C)
=
\{x_0\in K:\exists u,\exists T<\infty,\ x(T)\in C\}
}.
\]

Minimum recovery time:
\[
\boxed{T_R(x_0)=\inf\{T:x(T)\in C\}}.
\]

Viability theory, reachability, HJ/HJI methods, and even HJ viability in an infrastructure system already exist. The candidate contribution therefore concerns how uncertain dynamic interfaces deform these sets and boundaries.

---

## Chain V — Engineering Action / Design / Optimization

\[
\boxed{
\text{Control}
\rightarrow
\text{Operation}
\rightarrow
\text{Restoration}
\rightarrow
\text{Adaptation}
\rightarrow
\text{Design}
\rightarrow
\text{Optimization}
}
\]

Main question: **What can engineers change?**

Controlled system:
\[
\dot X=F(X,M,\eta,u;\theta).
\]

Optimal-control skeleton:
\[
\boxed{
u^*=\arg\min_{u(\cdot)}\left[\int_0^T\ell(X,u)\,dt+\phi(X(T))\right]}
\]
subject to \(X(t)\in K\).

Design variables:
\[
d=(\text{topology, capacity, redundancy, storage, interfaces, routing, backup}).
\]

Then
\[
\dot X=F_d(X,M,\eta,u),
\qquad
\mathcal V=\mathcal V(d).
\]

Possible later viability-oriented design objective:
\[
\boxed{d^*=\arg\max_d\operatorname{Vol}[\mathcal V_{\rm sus,eq}(d)]}.
\]

Restoration scheduling, resource allocation, and network-design optimization are already mature. For the current Type-I MSE, Chain V should mainly supply downstream control/design implications.

---

## Chain VI — Sustainability / Equity / Decision

\[
\boxed{
\text{Evaluate}
\rightarrow
\text{Trade Off}
\rightarrow
\text{Decide}
\rightarrow
\text{Implement}
\rightarrow
\text{Learn}
}
\]

Main question: **Which technically possible trajectories and designs are environmentally and socially admissible?**

Sustainability constraints may include
\[
E_{\rm carbon}(X,u,d)\le E_{\max},
\qquad
M_{\rm resource}(X,u,d)\le M_{\max}.
\]

Thus
\[
K_{\rm sus}=\{x:g_{\rm environmental}(x)\le0\}.
\]

Equity/service constraints may include
\[
S_g(X)\ge S_g^{min},\qquad\forall g,
\]
or
\[
\max_{g,h}|S_g-S_h|\le\Delta_{\max}.
\]

A multiobjective design/decision vector can be written
\[
\min_{d,u}
\begin{bmatrix}
C_{\rm lifecycle}\\
E_{\rm carbon}\\
I_{\rm inequity}\\
T_R\\
-\operatorname{Vol}(\mathcal V)
\end{bmatrix}.
\]

The current architecture treats sustainability and equity primarily as admissibility constraints and downstream decision criteria, not as synonyms for resilience.

---

# 3. Chain-layer ontology rules

1. Hazard is not damage.
2. Damage is not failure.
3. Failure is not automatically service loss.
4. Component functionality is not population service.
5. Resilience performance is not the same mathematical object as viability.
6. Sustainability is not synonymous with resilience.
7. A network edge is not automatically a physical interface law.
8. Parameter uncertainty is not identical to stochastic forcing.
9. Control changes system evolution; design changes architecture.
10. Optimization selects among feasible options; it does not establish governing physics.

---

# 4. Type I — Resilience-Centered Mathematical Physics

Primary scientific objects:
\[
\boxed{\mathcal V_{\rm sus,eq},\ \partial\mathcal V_{\rm sus,eq},\ \mathcal C_{\rm sus,eq}}.
\]

Mathematical spine:
\[
\boxed{
\xi
\rightarrow
\eta
\rightarrow
(X,Z,m)
\rightarrow
Y
\rightarrow
K_{\rm sus,eq}
\rightarrow
\mathcal V
\rightarrow
\mathcal C
\rightarrow
u
\rightarrow
d
}.
\]

Type I asks which states remain viable, which fail, which are recoverable, and which controls can preserve or restore viability. It is the closest continuation of the current MSE architecture.

Candidate uncertainty-to-geometry object:
\[
\boxed{
E_{\rm inv}
=
d_H[\mathcal V(\theta^*),\mathcal V(\hat\theta)]
}.
\]

Candidate sensitivity:
\[
\boxed{
S_j^{\mathcal V}
=
\lim_{\delta\to0}
\frac{d_H[\mathcal V(\theta),\mathcal V(\theta+\delta e_j)]}{|\delta|}
}.
\]

Candidate timescale diagnostic:
\[
\boxed{
\Pi_M
=
\frac{\tau_{\rm interface}}{\tau_{\rm system/hazard}}
}.
\]

Recommended MSE use: **primary architecture**.

---

# 5. Type II — Identification / Physics-Informed Digital Twin

Primary unknown:
\[
\boxed{(\hat G,\hat\theta,\Sigma_\theta)}.
\]

Spine:
\[
\boxed{
\mathcal D_{\rm obs}
\rightarrow
(\hat G,\hat\theta,\Sigma_\theta)
\rightarrow
\hat F_{\rm dyn}
\rightarrow
\hat{\mathcal V}
\rightarrow
\hat{\mathcal C}
\rightarrow
u^*
\rightarrow
d^*
\rightarrow
a^*
}.
\]

Central question:

> **How accurately must dynamic cross-infrastructure interfaces be identified before downstream viability and control predictions can be trusted?**

Possible monitoring/sensor objective:
\[
\mathcal S^*
=
\arg\min_{\mathcal S}
\mathbb E\left[
d_H(\mathcal V_{\rm true},\mathcal V_{\rm estimated|\mathcal S})
\right].
\]

Type II is the strongest alternative for a digital-twin / inverse-problem research identity, but should not claim that infrastructure topology reconstruction itself is new.

---

# 6. Type III — Resilience-by-Design

Primary unknown:
\[
\boxed{d^*,u^*}.
\]

Spine:
\[
\boxed{
d\rightarrow F_d\rightarrow K(d)\rightarrow\mathcal V(d)\rightarrow u^*(d)\rightarrow J(d)\rightarrow d^*\rightarrow a^*}.
\]

Possible objective:
\[
\boxed{
d^*
=
\arg\max_d
\left[
\alpha\operatorname{Vol}(\mathcal V(d))
+
\beta\operatorname{Vol}(\mathcal C(d))
-
\gamma T_R(d)
-
\lambda C_{\rm lifecycle}(d)
-
\mu E_{\rm carbon}(d)
-
\nu I_{\rm eq}(d)
\right]
}.
\]

Type III asks what system should be built so that it is intrinsically more viable, recoverable, sustainable, and equitable. It is naturally more design/optimization heavy and is broader than the preferred current MSE scope.

---

# 7. The three types as one research program

Common system:
\[
\boxed{\dot X=F(X,M,\eta,u;d,\theta)}.
\]

| Type | Primary unknown | Research verb |
|---|---|---|
| I | \(\mathcal V,\mathcal C,\partial\mathcal V\) | Understand |
| II | \(G,\theta,\Sigma_\theta\) | Learn / Infer |
| III | \(u^*,d^*,a^*\) | Build / Decide |

Unified program:
\[
\boxed{
\underbrace{\mathcal D_{\rm obs}\rightarrow(\hat G,\hat\theta,\Sigma_\theta)}_{\text{Type II — Learn}}
\rightarrow
\underbrace{F\rightarrow K\rightarrow\mathcal V\rightarrow\mathcal C}_{\text{Type I — Understand}}
\rightarrow
\underbrace{u^*\rightarrow d^*\rightarrow a^*}_{\text{Type III — Control/Design/Decide}}
}.
\]

Recommended current thesis boundary:
\[
\boxed{
\text{Type I core}
+
\text{one Type-II inverse/UQ component}
+
\text{limited downstream control implication}
}.
\]

---

# 8. Canonical notation contract

| Symbol | Meaning |
|---|---|
| \(P,W,T,SW\) | Power, Water, Transportation, Solid Waste |
| \(\xi\) | external climate forcing |
| \(\eta\) | realized hazard |
| \(X\) | stacked physical infrastructure state |
| \(Z\) | auxiliary/interface/environmental states where required |
| \(M,m_{ij}\) | dynamic cross-infrastructure interface states |
| \(G\) | topology/network representation |
| \(\theta\) | model/interface parameters |
| \(\mathcal D_{\rm obs}\) | observations |
| \(\hat G,\hat\theta\) | inferred structure and parameters |
| \(\Sigma_\theta\) | identification uncertainty |
| \(u(t)\) | intervention/control |
| \(d\) | design variables |
| \(Y\) | service/recovery state |
| \(\pi\) | physical-state → service/population mapping |
| \(K\) | admissible state set |
| \(\mathcal V\) | viability kernel |
| \(\partial\mathcal V\) | viability boundary |
| \(\mathcal C\) | capture/recoverability set |
| \(T_R\) | minimum recovery time |
| \(d_H\) | Hausdorff distance |
| \(\Pi_M\) | interface/system timescale ratio |

Do not silently redefine these symbols in future chats.

---

# 9. Mathematical rigor hierarchy

The thesis should distinguish and, where feasible, establish:

\[
\boxed{
\text{Model Definition}
\rightarrow
\text{Existence}
\rightarrow
\text{Uniqueness}
\rightarrow
\text{Stability}
\rightarrow
\text{Sensitivity}
\rightarrow
\text{Identifiability}
\rightarrow
\text{Computability}
\rightarrow
\text{Validation}
}.
\]

“Unique solution” must always specify whether it means uniqueness of a physical trajectory, inverse parameter solution, viscosity solution of an HJ equation, optimal control, or optimal design.

---

# 10. Existing literature vs candidate contribution

Already established or substantially developed:

- sector conservation and flow physics;
- graph/multilayer representations;
- infrastructure interdependencies;
- cascading failures and percolation;
- dynamic/transient cascade effects;
- system identification and Bayesian inverse problems;
- Bayesian reconstruction of interdependent infrastructure networks;
- fragility/hazard-damage models;
- resilience performance metrics;
- viability kernels/capture basins;
- HJ/HJI reachability;
- HJ viability in an infrastructure system;
- restoration and recovery optimization;
- sustainability/resilience integration;
- equity-aware resilience;
- multiobjective design and decision analysis.

Therefore the candidate thesis intersection is

\[
\boxed{
\mathcal D_{\rm obs}
\rightarrow
(\hat G,\hat\theta,\Sigma_\theta)
\rightarrow
M(t)
\rightarrow
F_{\rm dyn}
\rightarrow
\mathcal V_{\rm sus,eq}
}
\]

with emphasis on dynamic-interface identifiability, timescale validity, uncertainty propagation into viability/recovery sets, and boundary deformation.

Possible reduction-theorem target retained from earlier project work:
\[
\mathcal V_{\rm red}\subseteq\Pi(\mathcal V_{\rm full})
\]
or
\[
d_H[\mathcal V_{\rm red},\Pi(\mathcal V_{\rm full})]\le\varepsilon_R.
\]

Generic HJ decomposition/reduction results already exist, so any theorem must be infrastructure-specific and assumptions must be stated.

Novelty status remains **candidate, not globally frozen** until full systematic novelty falsification is complete.

---

# 11. Framework image paths

- Combined: `08_framework_images/combined_three_frameworks.webp`
- Type I: `08_framework_images/type_I_resilience_centered_mathematical_physics.webp`
- Type II: `08_framework_images/type_II_identification_digital_twin.webp`
- Type III: `08_framework_images/type_III_resilience_by_design.webp`

The images are conceptual visualizations, not empirical results. Their notation must be checked against this memory file before thesis publication.
