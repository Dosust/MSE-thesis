# Mathematical Foundation

**Status:** CURRENT / SYNCHRONIZED WITH STAGES 1–6  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**System:** Power–Transportation–Information–Organization (P–T–I–O)  
**Purpose:** Compact cross-stage mathematical foundation; detailed authority remains in the canonical stage files  
**Stage 7:** deep research complete; exact mathematical scope not frozen

---

## 1. Scientific object

The thesis treats infrastructure resilience and sustainable transformation as a **controlled, partially observable, hybrid multiscale dynamical-systems problem under explicit sustainability constraints and regime-adequacy requirements**.

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

The framework does not reduce resilience or transformation to one scalar score. It preserves causal mechanisms, dynamic trajectories, observation/control, controlled viability and long-horizon regime adequacy as distinct mathematical layers.

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

Partition the state into continuous/quasi-continuous states $Y_c$ and discrete states $Y_d$.

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

For component $j$,

$$
T_C(j)=\inf\{t>t_0:j\text{ enters a predefined disrupted state}\}.
$$

A spatial propagation velocity is used only where a meaningful physical spatial-front interpretation exists.

---

## 4. Native subsystem states

| Layer/system | Representative state/process variables | Typical mathematical family |
|---|---|---|
| Power $P$ | voltage, power flow, frequency, DER/storage, charging, traction power | power flow, DistFlow, DAE/dynamic models where needed |
| Transportation $T$ | density, flow, speed, travel time, accessibility, EV/eBus SOC, train motion | conservation laws, CTM/DTA, routing, queueing, train-motion models |
| Information $I$ | availability, latency, quality, freshness, loss, estimation error, synchronization | delay, stochastic, discrete-event, communication models |
| Organization $O$ | authority, coordination, resources, workforce, decision/mobilization times | state-transition, scheduling, routing, resource-allocation, discrete-event models |

The canonical informational and organizational states are

$$
z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top,
$$

$$
z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^{O},\tau_M]^\top.
$$

---

## 5. Stage-4 observation and inference

The true physical state is not assumed to be directly known.

**Equation F.2 — Measurement model**

$$
y_k(t)=H_k\!\left[X(t-\delta_k)\right]+\varepsilon_k(t).
$$

State estimation is

$$
(\widehat X(t),\Sigma_X(t))
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
$$

Under partial observability,

$$
b_t(x)=p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right).
$$

The conceptual feedback spine is

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

---

## 6. Stage-4 organizational feasibility and control

Current information and organizational states restrict the feasible action set:

$$
\mathcal U_{\rm available}(t)
=
\mathcal U\!\left(z_I(t),z_O(t)\right),
$$

$$
u(t)=\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

No specific solver is part of the framework definition.

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

The acceptable region is

$$
K_{\rm sus}(t)
=
\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\}.
$$

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

The central distinction is

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
$$

Thus the loss-of-maintainability boundary $\partial\mathcal V$ is distinct from the actual acceptability boundary $\partial K_{\rm sus}$.

---

## 8. Robust and stochastic viability

Worst-case robust viability and stochastic viability remain mathematically separate:

$$
\text{robust viability}\neq\text{stochastic viability}.
$$

The selected uncertainty interpretation determines the appropriate quantifiers and computation.

---

## 9. Geometric and temporal proximity to viability loss

With normalized state

$$
\widetilde Y=D^{-1}(Y-Y_{\rm ref}),
$$

the baseline geometric diagnostic is

$$
\rho_E(Y)=d\!\left(\widetilde Y,\partial\widetilde{\mathcal V}\right).
$$

The proposed state-dependent extension is

$$
\rho_g(Y)=d_{g_\psi}\!\left(Y,\partial\mathcal V_{\rm sus}^{u,T}\right),
\qquad g_\psi(Y)\succ0.
$$

Two temporal quantities are retained:

$$
T_{\mathcal V}^{\pi,\xi}(Y_0)
=
\inf\{t>0:Y^{\pi,\xi}(t)\notin\mathcal V_{\rm sus}^{u,T-t}\},
$$

$$
T_K^{\pi,\xi}(Y_0)
=
\inf\{t>0:Y^{\pi,\xi}(t)\notin K_{\rm sus}\}.
$$

---

## 10. Response-to-viability diagnostics

The proposed response slacks are

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response},
$$

with dimensionless forms

$$
\Pi_{\mathcal V}=\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K=\frac{\tau_{\rm response}}{T_K}.
$$

These are proposed diagnostics; neither a positive slack nor a ratio below one is by itself sufficient for successful control.

---

## 11. Interdependency sensitivity

Finite perturbation is the default proposed sensitivity when smoothness is not established:

$$
S_{ij}^{\mathcal V}(\Delta\theta)
=
\frac{
\mathcal M_{\mathcal V}(\theta_{ij}+\Delta\theta)
-
\mathcal M_{\mathcal V}(\theta_{ij})
}{\|\Delta\theta\|},
$$

$$
\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
$$

---

## 12. Reduced viability state

When required,

$$
Y_V=\mathcal P_V(Y),
$$

but the projection must preserve or conservatively bound constraints, control authority, interdependencies and mechanisms that materially affect Stage-5 conclusions. Reduction is therefore a validation obligation.

---

## 13. Stage-6 regime-adequacy diagnosis

Stage 6 asks whether **preserving the present system/decision space remains the correct objective** under longer-horizon sustainability and equity requirements.

The current regime is

$$
\mathfrak M_0
=
(\mathcal S,\mathcal G,\mathfrak I,F,\Theta,K_{\rm sus},\mathcal U).
$$

The Stage-5 evidence interface is

$$
\mathcal R_5
=
\{\mathcal V,\rho,T_{\mathcal V},T_K,S_{\mathcal V},S_K,S_{ij}^{\mathcal V}\}.
$$

The proposed diagnostic vector is

$$
\mathbf d_6
=
[d_{\mathcal V},d_{\rm limit},d_{\rm lock},d_{\rm mal},d_{\rm sus},d_{\rm eq},d_{\rm struct}]^\top.
$$

The frozen Stage-6 translation is

**Equation F.4 — Resilience-to-sustainability transition**

$$
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T),
$$

where

$$
c_6\in\{R,A,T\},
$$

$$
\mathcal D_6
=
\{\mathcal D_P,\mathcal D_T,\mathcal D_I,\mathcal D_O,
\mathcal D_{\mathfrak I},\mathcal D_{\rm env},\mathcal D_{\rm eq}\},
$$

and

$$
\boldsymbol{\zeta}_T
=
[\zeta_{\rm depth},\zeta_{\rm scope},\zeta_{\rm scale},\zeta_{\rm pace},
\zeta_{\rm equity},\zeta_{\rm environment}]^\top.
$$

The formal Stage-6 distinction is

$$
\underbrace{\text{viability of the current regime}}_{\text{Stage 5}}
\neq
\underbrace{\text{adequacy of preserving that regime}}_{\text{Stage 6}}.
$$

Stage 6 determines **why change is required, what must change and how deep the change must be**. It does not select the intervention sequence.

---

## 14. Stage-7 handoff — candidate research only

The frozen input to Stage 7 is

$$
(c_6,\mathcal D_6,\boldsymbol{\zeta}_T)
\longrightarrow
\text{candidate strategic interventions and pathways}.
$$

The deterministic representation

$$
\Pi=[(a_1,t_1),\ldots,(a_N,t_N)]
$$

remains a candidate representation of one realized branch. Current Stage-7 research is testing whether the fundamental object should instead be an adaptive, trigger-dependent pathway graph under deep uncertainty.

No Stage-7 mathematical object is frozen in this foundation yet.

---

## 15. Cross-stage mathematical chain

The frozen mathematical architecture through Stage 6 is

$$
\begin{aligned}
\{P,T,I,O\}
&\rightarrow\mathfrak I_{ij}^{\alpha\beta}
\rightarrow\{Y,\mathcal G,m,T_C\}\\
&\rightarrow\{\widehat X,\Sigma_X,b_t,\mathcal U,u,\tau_{\rm response}\}\\
&\rightarrow\{K_{\rm sus},\mathcal V,\partial\mathcal V,
\rho,T_{\mathcal V},T_K\}\\
&\rightarrow\Phi_{\rm ST}
\rightarrow(c_6,\mathcal D_6,\boldsymbol{\zeta}_T).
\end{aligned}
$$

Stage 7 must begin from this handoff and must not redefine the upstream frozen objects.

---

## 16. Mathematical discipline

The foundation is governed by the separations

$$
\begin{aligned}
\text{structure}&\neq\text{causal mechanism},\\
\text{event time}&\neq\text{causal delay}\neq\text{timescale},\\
X&\neq y\neq\widehat X,\\
K_{\rm sus}&\neq\mathcal V_{\rm sus}^{u,T},\\
V_{\rm HJ}&\neq d(\cdot,\partial\mathcal V)\quad\text{in general},\\
\text{current-regime viability}&\neq\text{long-horizon regime adequacy},\\
u(t)&\neq a_k\quad\text{(operational control versus structural transformation action)}.
\end{aligned}
$$

These distinctions are mandatory in equations, simulations, figures and interpretation.
