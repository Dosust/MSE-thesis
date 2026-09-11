# Mathematical Foundation

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![System](https://img.shields.io/badge/system-P--T--I--O-0969DA)

**Status:** CURRENT / SYNCHRONIZED WITH STAGES 1–7  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Purpose:** Compact cross-stage mathematical foundation; detailed authority remains in the frozen stage-specific files.

---

## 1. Scientific object

The thesis treats infrastructure resilience and sustainable transformation as a **controlled, partially observable, hybrid multiscale dynamical-systems problem under explicit sustainability constraints, regime-adequacy requirements and adaptive architecture transformation**.

The integrated state is

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix},
```

with physical state

```math
X(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix},
```

and augmented hybrid state

```math
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
```

The framework does not reduce resilience or transformation to one scalar score. It keeps causal mechanisms, dynamic trajectories, information/organization, operational control, controlled viability, regime adequacy and strategic transformation mathematically distinct.

---

## 2. Stage 2 — causal interdependency object

Every accepted cross-layer interdependency is represented by

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right),
```

where

```math
\alpha,\beta\in\{P,T,I,O\},
\qquad
\alpha\neq\beta.
```

A retained relation requires an explicit causal mechanism:

```math
\alpha\xrightarrow{M_{ij}}\beta.
```

Common hazard exposure or correlation alone does not establish an interdependency.

---

## 3. Stage 3 — hybrid delayed multirate dynamics

Partition the state into continuous/quasi-continuous states $Y_c$ and discrete states $Y_d$.

**Equation F.1 — Coupled hybrid dynamics**

```math
\begin{aligned}
\dot Y_c(t)
&=F^{m(t)}\!\left[
Y_c(t),Y_d(t),Y(t-\boldsymbol\delta),h(\mathbf r,t);
\mathcal G(t),\mathcal H_t
\right],\\
0
&=G^{m(t)}\!\left[
Y_c(t),Y_d(t),h(\mathbf r,t);\mathcal G(t)
\right],\\
Y_d(t_e^+)
&=R_e\!\left[\widetilde Y(t_e^-),e\right],\\
m(t_e^+)
&=\Delta_m\!\left[m(t_e^-),\widetilde Y(t_e^-),e\right],\\
\mathcal G(t_e^+)
&=\Psi\!\left[\mathcal G(t_e^-),\widetilde Y(t_e^-),e,\mathcal H_t\right].
\end{aligned}
```

The temporal discipline is

```math
\text{event time}
\neq
\text{causal delay }\delta
\neq
\text{characteristic timescale }\tau.
```

For component $j$, cascade-arrival time may be represented by

```math
T_C(j)=\inf\{t>t_0:j\text{ enters a predefined disrupted state}\}.
```

Spatial propagation velocity is used only where a physically meaningful spatial-front interpretation exists.

---

## 4. Native P–T–I–O processes

| Layer/system | Representative variables | Typical mathematical family |
|---|---|---|
| Power $P$ | voltage, power flow, frequency, DER/storage, charging, traction power | power flow, DistFlow, DAE/dynamic models as required |
| Transportation $T$ | density, flow, speed, travel time, accessibility, EV/eBus SOC, train motion | conservation laws, CTM/DTA, routing, queueing, train-motion models |
| Information $I$ | availability, latency, quality, freshness, loss, estimation error, synchronization | delay, stochastic, discrete-event, communication models |
| Organization $O$ | authority, coordination, resources, workforce, decision/mobilization times | state-transition, scheduling, routing, resource-allocation, discrete-event models |

Representative informational and organizational state vectors are

```math
z_I
=
[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top,
```

```math
z_O
=
[A_O,C_O,R_O,W_O,\tau_D,\tau_C^O,\tau_M]^\top.
```

---

## 5. Stage 4 — observation and inference

The true physical state is not assumed to be directly known.

**Equation F.2 — Measurement model**

```math
y_k(t)
=
H_k\!\left[X(t-\delta_k)\right]
+\varepsilon_k(t).
```

State estimation is represented by

```math
(\widehat X(t),\Sigma_X(t))
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
```

Under partial observability, a belief state may be used:

```math
b_t(x)
=
p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right).
```

The conceptual feedback spine is

```math
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow\widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
```

---

## 6. Stage 4 — organizational feasibility and operational control

Information and organizational states constrain the feasible action set:

```math
\mathcal U_{\rm available}(t)
=
\mathcal U\!\left(z_I(t),z_O(t)\right),
```

```math
u(t)
=
\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
```

No specific solver is part of the framework definition.

For a sequential non-overlapping response process,

```math
\begin{aligned}
\tau_{\rm response}={}&
\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
```

When processes overlap, $\tau_{\rm response}$ is the relevant critical-path completion time.

---

## 7. Stage 5 — acceptability and controlled viability

The acceptable region is

```math
K_{\rm sus}(t)
=
\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\}.
```

**Equation F.3 — Controlled finite-horizon viability**

```math
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}
\ \forall t\in[0,T]
\right\}.
```

The central distinction is

```math
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
```

Thus the loss-of-maintainability boundary $\partial\mathcal V$ is distinct from the actual acceptability boundary $\partial K_{\rm sus}$.

---

## 8. Robust and stochastic viability remain distinct

For bounded/adversarial uncertainty and probabilistic uncertainty, the quantifier structures differ. Therefore

```math
\text{robust viability}
\neq
\text{stochastic viability}.
```

The selected uncertainty interpretation determines the proper mathematical form and computation.

---

## 9. Geometric and temporal proximity to viability loss

Normalize state variables before Euclidean distance is interpreted:

```math
\widetilde Y=D^{-1}(Y-Y_{\rm ref}).
```

The geometric baseline is

```math
\rho_E(Y)
=
d\!\left(\widetilde Y,\partial\widetilde{\mathcal V}\right).
```

The proposed state-dependent extension is

```math
\rho_g(Y)
=
d_{g_\psi}\!\left(Y,\partial\mathcal V_{\rm sus}^{u,T}\right),
\qquad
g_\psi(Y)\succ0.
```

Two temporal quantities are retained:

```math
T_{\mathcal V}^{\pi,\xi}(Y_0)
=
\inf\{t>0:Y^{\pi,\xi}(t)\notin\mathcal V_{\rm sus}^{u,T-t}\},
```

```math
T_K^{\pi,\xi}(Y_0)
=
\inf\{t>0:Y^{\pi,\xi}(t)\notin K_{\rm sus}\}.
```

---

## 10. Response-to-viability diagnostics `[P]`

```math
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response},
```

```math
\Pi_{\mathcal V}
=\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K
=\frac{\tau_{\rm response}}{T_K}.
```

Neither a positive slack nor a ratio below one is sufficient by itself for successful control.

---

## 11. Interdependency sensitivity `[P]`

When smoothness is not established, use finite perturbation by default:

```math
S_{ij}^{\mathcal V}(\Delta\theta)
=
\frac{
\mathcal M_{\mathcal V}(\theta_{ij}+\Delta\theta)
-
\mathcal M_{\mathcal V}(\theta_{ij})
}{\|\Delta\theta\|},
```

where

```math
\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
```

The scalar viability functional $\mathcal M_{\mathcal V}$ must be declared before use; a set $\mathcal V$ itself cannot be subtracted as a scalar outcome without a defined set metric/functional.

---

## 12. Reduced viability state

When exact viability computation is infeasible in the full Stage-3 state space, define

```math
Y_V=\mathcal P_V(Y).
```

The projection must preserve or conservatively bound constraints, control authority, interdependencies and mechanisms that materially affect Stage-5 conclusions. Reduction is a validation obligation, not merely a computational convenience.

---

## 13. Stage 6 — regime-adequacy diagnosis

The current infrastructure regime is

```math
\mathfrak M_0
=
(\mathcal S,\mathcal G,\mathfrak I,F,\Theta,K_{\rm sus},\mathcal U).
```

The Stage-5 evidence interface is

```math
\mathcal R_5
=
\{\mathcal V,\rho,T_{\mathcal V},T_K,S_{\mathcal V},S_K,S_{ij}^{\mathcal V}\}.
```

The proposed diagnostic vector is

```math
\mathbf d_6
=
[d_{\mathcal V},d_{\rm limit},d_{\rm lock},d_{\rm mal},d_{\rm sus},d_{\rm eq},d_{\rm struct}]^\top.
```

**Equation F.4 — Resilience-to-sustainability transition**

```math
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol\zeta_T).
```

Stage 6 determines **why change is required, what must change and how deep the change must be**. It does not choose the strategic pathway.

---

## 14. Stage 7 — infrastructure-regime transformation

Stage 7 receives

```math
(c_6,\mathcal D_6,\boldsymbol\zeta_T)
```

and transforms candidate future regimes represented by

```math
\mathfrak M_k
=
(\mathcal S_k,\mathcal G_k,\mathfrak I_k,F_k,\Theta_k,K_{{\rm sus},k},\mathcal U_k).
```

Stage-4 operational control and Stage-7 strategic transformation remain distinct:

```math
\underbrace{u(t)}_{\text{operate current regime}}
\neq
\underbrace{\mathbf a_k}_{\text{transform regime}}.
```

The strategic action vector is

```math
\mathbf a_k
=
\begin{bmatrix}
a_k^P\\a_k^T\\a_k^I\\a_k^O\\a_k^{\mathfrak I}
\end{bmatrix},
```

and the regime transition is

```math
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k).
```

---

## 15. Stage 7 — transformation meta-graph

The graph of alternative regimes is

```math
\mathbb G_{\rm ST}
=(\mathbb V_{\rm ST},\mathbb E_{\rm ST}),
```

with

```math
v_k\equiv\mathfrak M_k.
```

A meta-edge represents an admissible strategic transformation rather than an ordinary component-to-component infrastructure link.

---

## 16. Stage 7 — adaptive policy, triggers and path dependence

The step policy is

```math
\mathbf a_k
=
\pi_k^{\rm ST}
\!\left(
\widehat X_k,
z_{I,k},
z_{O,k},
\mathfrak M_k,
\mathcal H_k
\right),
```

with

```math
\boldsymbol\pi_{\rm ST}
=
\{\pi_0^{\rm ST},\pi_1^{\rm ST},\ldots,\pi_N^{\rm ST}\}.
```

For monitored signpost

```math
s_j(t)
=
s_j\!\left(\widehat X(t),z_I(t),z_O(t),\mathfrak M(t),\xi(t)\right),
```

and trigger region $\mathcal Z_j$,

```math
\tau_j
=
\inf\{t:s_j(t)\in\mathcal Z_j\}.
```

Path dependence is represented by

```math
\mathcal A_{k+1}
=
\mathcal A\!\left(\mathfrak M_{k+1},\mathcal H_{t_{k+1}}\right),
```

and in general

```math
\mathcal T_{\mathbf a_2}\circ\mathcal T_{\mathbf a_1}
\neq
\mathcal T_{\mathbf a_1}\circ\mathcal T_{\mathbf a_2}.
```

---

## 17. Stage 7 — feasibility, viability and target set

The feasible strategic set includes technical, budget, informational, organizational, sustainability, equity and temporal requirements:

```math
\begin{aligned}
\mathcal A_k^{\rm feas}
={}&
\mathcal A_k^{\rm tech}
\cap\mathcal A_k^{\rm budget}
\cap\mathcal A_k^{I}
\cap\mathcal A_k^{O}\\
&\cap\mathcal A_k^{\rm sus}
\cap\mathcal A_k^{\rm equity}
\cap\mathcal A_k^{\rm temporal}.
\end{aligned}
```

Every candidate regime is reevaluated through Stage 5:

```math
\mathcal V_{\rm sus}^{u,T}(\mathfrak M_k).
```

The sustainable target-regime set is

```math
\mathbb M_{\rm sus}
=
\left\{
\mathfrak M:
\text{declared resilience, sustainability, equity and feasibility criteria are satisfied}
\right\}.
```

The reachability problem is

```math
(\mathfrak M_0,Y_0)
\overset{\boldsymbol\pi_{\rm ST}}{\longrightarrow}
\mathbb M_{\rm sus}.
```

---

## 18. Stage 7 — objectives and uncertainty

The many-objective vector is

```math
\mathbf J(\Pi,\omega)
=
\begin{bmatrix}
J_{\rm risk}\\
J_{\rm service}\\
J_{\rm cost}\\
J_{\rm carbon}\\
J_{\rm inequity}\\
J_{\rm time}\\
J_{\rm flexibility}
\end{bmatrix},
\qquad
\omega\in\Omega.
```

The framework keeps

```math
\xi\sim P,
\qquad
P\in\mathcal P,
\qquad
\omega\in\Omega
```

separate for probabilistic uncertainty, distributional ambiguity and deep uncertainty respectively.

A scenario fraction under $\Omega$ is not a probability unless probabilities or justified weights have been defined.

---

## 19. Frozen Stage-7 object `[P]`

**Equation F.5 — Adaptive transformation-pathway object**

```math
\mathfrak P_{\rm ST}
=
\left(
\mathbb G_{\rm ST},
\boldsymbol\pi_{\rm ST},
\Omega,
\mathcal A^{\rm feas},
\mathbf J,
\mathbb M_{\rm sus}
\right).
```

Its framework definition is frozen while its scientific utility remains subject to falsification and numerical validation.

A realized pathway is

```math
\Pi_{\boldsymbol\pi_{\rm ST},\omega}
=
\left[
(\mathfrak M_0,\mathbf a_0,\tau_0),
(\mathfrak M_1,\mathbf a_1,\tau_1),
\ldots,
\mathfrak M_N
\right].
```

---

## 20. Complete cross-stage mathematical chain

```math
\begin{aligned}
\underbrace{\mathcal S}_{1}
&\rightarrow
\underbrace{\mathfrak I}_{2}
\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{3}\\
&\rightarrow
\underbrace{X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u}_{4}\\
&\rightarrow
\underbrace{K_{\rm sus},\mathcal V,\rho,T_{\mathcal V},T_K}_{5}\\
&\rightarrow
\underbrace{\Phi_{\rm ST}\rightarrow(c_6,\mathcal D_6,\boldsymbol\zeta_T)}_{6}\\
&\rightarrow
\underbrace{\mathfrak P_{\rm ST}}_{7}.
\end{aligned}
```

Conceptually:

```math
\text{ontology}
\rightarrow
\text{causal coupling}
\rightarrow
\text{dynamics}
\rightarrow
\text{knowledge/control}
\rightarrow
\text{viability}
\rightarrow
\text{transformation diagnosis}
\rightarrow
\text{adaptive transformation pathway}.
```

---

## 21. Seven-stage validation loop

Every candidate transformation is replayed through Stages 1–6:

```math
\begin{aligned}
\text{Stage-7 candidate}
&\rightarrow\text{Stage-1 structural update}\\
&\rightarrow\text{Stage-2 mechanism update}\\
&\rightarrow\text{Stage-3 dynamic simulation}\\
&\rightarrow\text{Stage-4 observation/control evaluation}\\
&\rightarrow\text{Stage-5 viability evaluation}\\
&\rightarrow\text{Stage-6 adequacy diagnosis}\\
&\rightarrow\text{Stage-7 accept / reject / refine}.
\end{aligned}
```

The loop validates candidates; it does not replace or reorder the stages.

---

## 22. Mathematical discipline

The mandatory separations are

```math
\begin{aligned}
\text{structure}&\neq\text{causal mechanism},\\
\text{event time}&\neq\text{causal delay}\neq\text{timescale},\\
X&\neq y\neq\widehat X,\\
K_{\rm sus}&\neq\mathcal V_{\rm sus}^{u,T},\\
V_{\rm HJ}&\neq d(\cdot,\partial\mathcal V)\quad\text{in general},\\
\text{current-regime viability}&\neq\text{long-horizon regime adequacy},\\
u(t)&\neq\mathbf a_k,\\
a_{ij}&\neq\mathbf a_k,\\
\text{fixed realized pathway}&\subset\text{adaptive transformation policy}.
\end{aligned}
```

These distinctions are mandatory in equations, simulations, figures and interpretation.

---

## 23. Final framework state

> **STAGES 1–7: CONCEPTUAL AND MATHEMATICAL FRAMEWORK FROZEN.**

The next phase is hypothesis specification, operationalization, numerical testing, falsification and validation.
