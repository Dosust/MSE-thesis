# Mathematical Foundation

**Status:** CURRENT / SYNCHRONIZED WITH STAGES 1–5  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**System:** Power–Transportation–Information–Organization (P–T–I–O)  
**Purpose:** Compact cross-stage mathematical foundation; detailed authority remains in the canonical stage files

---

## 1. Scientific object

The thesis treats infrastructure resilience as a **controlled, partially observable, hybrid multiscale dynamical-systems problem under explicit sustainability constraints**.

The framework-level state is

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix},
$$

with physical state

$$
X(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix},
$$

and augmented hybrid state

$$
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
$$

The central object is not a scalar resilience score. The thesis studies the interaction among causal interdependencies, dynamic trajectories, observation/control, and controlled viability.

---

## 2. Stage-2 causal interdependency object

Every accepted cross-layer interdependency is represented by

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right),
$$

where

$$
\alpha,\beta\in\{P,T,I,O\},
\qquad
\alpha\neq\beta.
$$

A retained relation requires an explicit causal mechanism:

$$
\alpha\xrightarrow{M_{ij}}\beta.
$$

Common hazard exposure alone does not establish an interdependency.

---

## 3. Stage-3 hybrid delayed multirate dynamics

Partition the state into continuous/quasi-continuous states $Y_c$ and discrete states $Y_d$. A general Stage-3 representation is

**Equation F.1 — Coupled hybrid dynamics**

$$
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
$$

The temporal discipline is

$$
\text{event time}
\neq
\text{causal delay }\delta
\neq
\text{characteristic timescale }\tau.
$$

For component $j$, cascade-arrival time may be represented as

$$
T_C(j)=\inf\{t>t_0:j\text{ enters a predefined disrupted state}\}.
$$

A spatial propagation velocity $v_c(t)$ is used only where a physically meaningful spatial-front interpretation exists.

---

## 4. Stage-3 native subsystem states

The framework does not force all layers into one equation class.

| Layer/system | Representative state/process variables | Typical mathematical family |
|---|---|---|
| Power $P$ | voltage, power flow, frequency, DER/storage, charging, traction power | algebraic power flow, DistFlow, DAE, dynamic models where required |
| Transportation $T$ | density, flow, speed, travel time, accessibility, EV/eBus SOC, train motion | conservation laws, CTM/DTA, routing, queueing, train-motion models |
| Information $I$ | availability, latency, quality, freshness, loss, estimation error, synchronization | delay, stochastic, discrete-event, communication models |
| Organization $O$ | authority, coordination, resources, workforce, decision/mobilization times | state-transition, scheduling, routing, resource-allocation, discrete-event models |

The canonical information and organizational states are

$$
z_I=
[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top,
$$

and

$$
z_O=
[A_O,C_O,R_O,W_O,\tau_D,\tau_C^{O},\tau_M]^\top.
$$

---

## 5. Stage-4 observation and inference

The true physical state is not assumed to be directly known. A generic measurement model is

**Equation F.2 — Measurement model**

$$
y_k(t)=H_k\!\left[X(t-\delta_k)\right]+\varepsilon_k(t),
$$

where $\varepsilon_k(t)$ is measurement noise/error.

State estimation is represented as

$$
\left(\widehat X(t),\Sigma_X(t)\right)
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
$$

Under partial observability, a belief state may be used:

$$
b_t(x)
=
p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right).
$$

The canonical conceptual spine is

$$
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow \widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
$$

---

## 6. Stage-4 organizational feasibility and control

Current information and organizational states restrict the feasible action set:

$$
\mathcal U_{\rm available}(t)
=
\mathcal U\!\left(z_I(t),z_O(t)\right),
$$

and

$$
u(t)
=
\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

No specific solver is part of the framework definition. MPC, mathematical programming, dynamic programming, POMDP methods, game-theoretic methods, or learning-based control may instantiate the policy $\pi$ only when justified by the research question and validation design.

For a sequential non-overlapping response process,

$$
\begin{aligned}
\tau_{\rm response}={}&
\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

When processes overlap, $\tau_{\rm response}$ is the relevant critical-path completion time.

---

## 7. Stage-5 acceptability and controlled viability

The acceptable region is defined by justified constraints:

$$
K_{\rm sus}(t)
=
\left\{
Y:g_r(Y,t)\le0,
\quad r=1,\ldots,n_K
\right\}.
$$

The primary finite-horizon controlled viability set is

**Equation F.3 — Controlled finite-horizon viability**

$$
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}
\ \forall t\in[0,T]
\right\}.
$$

The central set distinction is

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
$$

Thus the loss-of-maintainability boundary $\partial\mathcal V$ is distinct from the actual acceptability boundary $\partial K_{\rm sus}$.

---

## 8. Robust and stochastic viability

Worst-case robust viability and stochastic viability remain mathematically separate.

For bounded/adversarial uncertainty,

$$
\mathcal V_{\rm rob}^{T}
=
\left\{
Y_0:
\exists\pi\in\Pi_{\rm adm},
\ \forall\xi\in\Xi,
\ Y^{\pi,\xi}(t)\in K_{\rm sus}
\ \forall t\in[0,T]
\right\}.
$$

For probabilistic uncertainty,

$$
\mathcal V_{\varepsilon}^{T}
=
\left\{
Y_0:
\exists\pi,
\ \Pr\!\left[Y^{\pi}(t)\in K_{\rm sus}\ \forall t\in[0,T]\right]
\ge1-\varepsilon
\right\}.
$$

Therefore,

$$
\text{robust viability}\neq\text{stochastic viability}.
$$

---

## 9. Geometric and temporal proximity to viability loss

A normalized Euclidean or weighted distance is the baseline geometric diagnostic. With

$$
\widetilde Y=D^{-1}(Y-Y_{\rm ref}),
$$

use

$$
\rho_E(Y)
=
d\!\left(\widetilde Y,\partial\widetilde{\mathcal V}\right).
$$

The proposed thesis extension is the state-dependent Riemannian margin

$$
\rho_g(Y)
=
d_{g_\psi}\!\left(Y,\partial\mathcal V_{\rm sus}^{u,T}\right),
\qquad
g_\psi(Y)\succ0.
$$

This is a proposed thesis construct and must be compared against justified Euclidean/weighted baselines.

Two temporal quantities are retained:

$$
T_{\mathcal V}^{\pi,\xi}(Y_0)
=
\inf\left\{t>0:Y^{\pi,\xi}(t)\notin\mathcal V_{\rm sus}^{u,T-t}\right\},
$$

and

$$
T_K^{\pi,\xi}(Y_0)
=
\inf\left\{t>0:Y^{\pi,\xi}(t)\notin K_{\rm sus}\right\}.
$$

Along trajectories where maintainability is lost before actual constraint violation,

$$
T_{\mathcal V}\le T_K.
$$

---

## 10. Response-to-viability diagnostics

The proposed response slacks are

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response}.
$$

Dimensionless versions are

$$
\Pi_{\mathcal V}=\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K=\frac{\tau_{\rm response}}{T_K}.
$$

These quantities are proposed diagnostics, not universal resilience laws. A positive slack or a ratio below one does not by itself guarantee successful control.

---

## 11. Interdependency sensitivity

Because viability boundaries need not be smooth, finite perturbation is the default proposed sensitivity:

$$
S_{ij}^{\mathcal V}(\Delta\theta)
=
\frac{
\mathcal M_{\mathcal V}(\theta_{ij}+\Delta\theta)
-
\mathcal M_{\mathcal V}(\theta_{ij})
}{\|\Delta\theta\|},
$$

where

$$
\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
$$

Differential sensitivity is used only where smoothness is demonstrated.

---

## 12. Reduced viability state and computation

The full Stage-3 state may be too high-dimensional for exact viability computation. A reduced viability state may therefore be defined by

$$
Y_V=\mathcal P_V(Y).
$$

The projection must preserve or conservatively bound the constraints, control authority, interdependencies, and mechanisms that materially affect Stage-5 conclusions. State reduction is therefore a validation obligation, not merely a computational convenience.

Hamilton–Jacobi, set-invariance, decomposition, control-barrier, and learned reachability methods are candidate computational or certification tools. None of them is identical to Stage-5 theory itself.

---

## 13. Cross-stage mathematical chain

The current mathematical architecture is

$$
\begin{aligned}
\{P,T,I,O\}
&\rightarrow \mathfrak I_{ij}^{\alpha\beta}
\rightarrow \{Y,\mathcal G,m,T_C\}\\
&\rightarrow \{\widehat X,\Sigma_X,b_t,\mathcal U,u,\tau_{\rm response}\}\\
&\rightarrow \{K_{\rm sus},\mathcal V,\partial\mathcal V,
\rho,T_{\mathcal V},T_K\}.
\end{aligned}
$$

Stages 6–7 must use only validated outputs from this chain when translating resilience evidence into sustainability-transition requirements and transformation pathways.

---

## 14. Mathematical discipline

The foundation is governed by five separations:

$$
\begin{aligned}
\text{structure}&\neq\text{causal mechanism},\\
\text{event time}&\neq\text{causal delay}\neq\text{timescale},\\
X&\neq y\neq\widehat X,\\
K_{\rm sus}&\neq\mathcal V_{\rm sus}^{u,T},\\
V_{\rm HJ}&\neq d(\cdot,\partial\mathcal V)\quad\text{in general}.
\end{aligned}
$$

These distinctions are mandatory in equations, simulations, figures, and interpretation.
