# Stage 5 — Controlled Sustainable Viability

**Framework stage:** Stage 5 — Controlled Sustainable Viability  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Evidence basis:** 10-pass literature audit spanning viability theory, controlled invariance, Hamilton–Jacobi reachability, robust and stochastic viability, resilience, geometric margins, temporal margins, and scalable computation  
**Change rule:** Do not revise this Stage-5 scientific scope unless explicitly requested and versioned.  
**Framework preservation rule:** This document formalizes Stage 5 only. It does **not** alter the frozen seven-stage framework or redefine Stages 1–4.

> **Evidence notation:** `[E]` = established literature; `[D]` = derived synthesis; `[P]` = proposed thesis construct.

> **Boundary rule:** Stage 5 evaluates whether controlled Stage-4 trajectories remain acceptable and maintainable. It does not redesign Stage-3 dynamics, redefine Stage-4 control, or yet prescribe Stage-6/7 transformation pathways.

> **Rendering rule:** Mathematical notation uses GitHub-compatible display blocks. Long scientific statements are expressed as tables or multiline equations rather than oversized boxed expressions.

---

## Frozen research question

> **Under what conditions can acceptable functions be maintained, and how far and how long is the system from unacceptable states?**

The Stage-5 scientific progression is

```math
K_{\rm sus}
\rightarrow
\mathcal V_{\rm sus}^{u,T}
\rightarrow
\partial\mathcal V
\rightarrow
\{\rho,T_{\mathcal V},T_K\}
\rightarrow
\{S_{\mathcal V},S_K,S_{ij}^{\mathcal V}\}.
```

Stage 5 therefore separates five questions:

| Question | Mathematical object |
|---|---|
| What states are acceptable? | Constraint set $K_{\rm sus}$ |
| From which acceptable states can constraints still be maintained? | Controlled viability set $\mathcal V_{\rm sus}^{u,T}$ |
| Where is maintainability lost? | Boundary $\partial\mathcal V$ |
| How far and how long is the current trajectory from loss? | $\rho$, $T_{\mathcal V}$, $T_K$ |
| Which interdependencies most alter these margins? | $S_{ij}^{\mathcal V}$ |

---

## 1. Core viability logic

Viability theory defines the viability kernel as the set of initial states from which at least one admissible evolution or control keeps the state within the prescribed constraint set (Aubin, 1990; Aubin et al., 2011).

The controlled Stage-4 trajectory is written

```math
Y^u(t)=Y\!\left(t;Y_0,u,h,\mathfrak I,\mathcal G,m\right),
```

with

```math
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
```

The Stage-5 core is therefore the controlled viability set

```math
\mathcal V_{\rm sus}^{u,T}
=
\operatorname{Viab}^{T}_{F,\mathcal U}(K_{\rm sus}).
```

More explicitly,

```math
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
```

This is established viability logic adapted to the thesis P–T–I–O state, interdependency, dynamics, and control architecture (Aubin, 1990; Aubin et al., 2011; Gajardo & Hermosilla, 2019).

---

## 2. Constraint set and sustainability interpretation

The notation $K_{\rm sus}$ does not become sustainable merely because it is named so. Viability theory determines whether specified constraints can be maintained; it does not itself determine which thresholds qualify as sustainability requirements. Those thresholds must be justified independently from engineering, environmental, social, economic, service, or policy requirements (Doyen & Gajardo, 2020).

The framework uses

```math
K_{\rm sus}(t)
=
\left\{
Y:g_r(Y,t)\le0,\quad r=1,\ldots,n_K
\right\}.
```

A useful decomposition is

```math
K_{\rm sus}=K_P\cap K_T\cap K_I\cap K_O,
```

provided each layer-specific constraint has a defensible threshold and physical meaning.

Representative constraint families include service, voltage/frequency, mobility/travel-time, information freshness/availability, and organizational resource/response requirements. The **threshold justification**, not the mathematical symbol alone, establishes the sustainability interpretation.

---

## 3. Finite-horizon and infinite-horizon viability

Finite-horizon viability is the primary Stage-5 object because the framework explicitly contains disturbance, response, and recovery times. Infinite-horizon viability remains the theoretical reference (Aubin et al., 2011; Gajardo & Hermosilla, 2019).

The finite-horizon set is

```math
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus},
\ \forall t\in[0,T]
\right\}.
```

The horizon $T$ must be declared explicitly and linked to the modeled disruption-response-recovery interval. Infinite-horizon viability is denoted

```math
\mathcal V_{\rm sus}^{u,\infty}.
```

---

## 4. Robust and stochastic viability are distinct

Worst-case robust viability and stochastic viability are not interchangeable.

### Robust viability

For bounded or adversarial uncertainty,

```math
\mathcal V_{\rm rob}^{T}
=
\left\{
Y_0:
\exists\pi\in\Pi_{\rm adm},
\ \forall\xi\in\Xi,
\ Y^{\pi,\xi}(t)\in K_{\rm sus}
\ \forall t\in[0,T]
\right\}.
```

The quantifier order is essential:

```math
\exists\pi\quad\forall\xi.
```

This is consistent with robust controlled-invariance formulations under bounded perturbations (Rungger & Tabuada, 2017).

### Stochastic viability

For probabilistic uncertainty,

```math
\mathcal V_{\varepsilon}^{T}
=
\left\{
Y_0:
\exists\pi,
\ \Pr\!\left[Y^{\pi}(t)\in K_{\rm sus}\ \forall t\in[0,T]\right]
\ge1-\varepsilon
\right\}.
```

This follows stochastic viability and target-tube reachability logic (Doyen & De Lara, 2010; Vinod & Oishi, 2021).

Therefore,

```math
\text{robust viability}\neq\text{stochastic viability}.
```

The framework keeps both mathematically separate; the uncertainty interpretation must determine which one is used in a specific analysis.

---

## 5. Acceptability and viability are different sets

A state may currently satisfy every acceptability constraint and still lie outside the viability kernel. In that case, the system has not yet violated $K_{\rm sus}$, but no admissible future control can maintain the constraints over the required horizon.

Hence,

```math
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
```

This distinction is fundamental in viability theory (Aubin et al., 2011; Maidens et al., 2013).

Stage 5 therefore preserves two boundaries:

```math
\partial\mathcal V_{\rm sus}^{u,T}
=\text{loss-of-maintainability boundary},
```

and

```math
\partial K_{\rm sus}
=\text{actual acceptability boundary}.
```

---

## 6. Two temporal margins

Because loss of viability and actual constraint violation are different events, a single generic time-to-exit quantity is insufficient.

### Time to loss of viability

```math
T_{\mathcal V}^{\pi,\xi}(Y_0)
=
\inf\left\{
t>0:
Y^{\pi,\xi}(t)
\notin
\mathcal V_{\rm sus}^{u,T-t}
\right\}.
```

Interpretation:

> $T_{\mathcal V}$ is the time until maintainability or recoverability within the prescribed viability condition is lost.

### Time to actual acceptability violation

```math
T_K^{\pi,\xi}(Y_0)
=
\inf\left\{
t>0:
Y^{\pi,\xi}(t)\notin K_{\rm sus}
\right\}.
```

Interpretation:

> $T_K$ is the time until an unacceptable state actually occurs.

Along trajectories where viability is lost before constraints are violated,

```math
T_{\mathcal V}\le T_K.
```

The distinction is consistent with viability-theoretic treatments of crisis time and admissible behavior (Doyen & Saint-Pierre, 1997).

---

## 7. Geometric margin

A geometric proximity measure is retained, but its evidential status is explicit.

### Established baseline [E]

State coordinates must first be normalized or otherwise made dimensionally comparable:

```math
\widetilde Y=D^{-1}(Y-Y_{\rm ref}).
```

A baseline distance is then

```math
\rho_E(Y)
=
d\!\left(
\widetilde Y,
\partial\widetilde{\mathcal V}
\right).
```

### Proposed thesis extension [P]

The proposed state-dependent geometric margin is

```math
\rho_g(Y)
=
d_{g_\psi}\!\left(
Y,
\partial\mathcal V_{\rm sus}^{u,T}
\right),
```

with

```math
g_\psi(Y)\succ0.
```

The Riemannian metric $g_\psi$ is **not** treated as an established infrastructure-viability metric. Its contribution must be demonstrated against normalized Euclidean or weighted baselines.

---

## 8. Hamilton–Jacobi value and geometric distance must remain separate

Hamilton–Jacobi reachability can represent reachable or viable sets through level sets of value functions (Bansal et al., 2017; Gajardo & Hermosilla, 2019; Mitchell et al., 2005).

A representation such as

```math
\mathcal V=\{Y:V_{\rm HJ}(Y)\le0\}
```

may therefore be appropriate. However,

```math
|V_{\rm HJ}(Y)|
\neq
d(Y,\partial\mathcal V)
```

in general. The HJ value depends on the terminal function, dynamics, game formulation, and normalization.

Stage 5 therefore keeps

```math
V_{\rm HJ}(Y)=\text{dynamic safety/reachability value}
```

separate from

```math
\rho_g(Y)=\text{geometric distance to a viability boundary}.
```

---

## 9. Control barrier functions are a method, not the Stage-5 theory

Control barrier functions can certify forward invariance and embed safety constraints in online control (Ames et al., 2017). For delayed systems, control barrier functionals provide related safety-critical formulations (Kiss et al., 2023).

However,

```math
\text{CBF certificate}
\neq
\text{maximal viability kernel}
```

in general.

Therefore:

| Role | Status in this thesis |
|---|---|
| Viability theory | Stage-5 theoretical foundation |
| HJ / set-invariance / viability algorithms | Candidate computational methods |
| Control barrier functions/functionals | Candidate certification/control methods |
| Learned reachability methods | Candidate approximation methods requiring verification |

No computational solver is frozen into Stage 5.

---

## 10. State reduction and computational validity

Stage-3 hybrid delayed multiscale dynamics may be too high-dimensional for direct exact viability computation. Exact delays can also enlarge the effective state representation substantially. The framework therefore permits a viability projection

```math
Y_V=\mathcal P_V(Y),
```

where $Y_V$ is a reduced viability state.

This projection is **not free**: it creates a validation obligation. The reduced state must preserve the constraints, control authority, interdependencies, and failure/recovery mechanisms that materially affect Stage-5 conclusions.

High-dimensional reachability and viability computation is a known challenge; alternative Lagrangian, implicit, decomposed, and learned approximations trade computational scalability against structural assumptions and approximation risk (Bansal et al., 2017; Bansal & Tomlin, 2021; Maidens et al., 2013; Solanki et al., 2025).

---

## 11. Viability and recoverability after violation

Remaining inside an acceptable set and recovering after leaving it are different problems. Viability-based resilience literature distinguishes viability from capture/recovery concepts (Béné & Doyen, 2018; Martin et al., 2011).

Therefore,

```math
\text{viability}
\neq
\text{recoverability after violation}.
```

Controlled viability remains the core Stage-5 object. Capture or recovery basins may be introduced only when the framework explicitly permits temporary excursion outside $K_{\rm sus}$ and when doing so does not blur the Stage-5/Stage-6 boundary.

---

## 12. Interface sensitivity and criticality [P]

The original differential sensitivity

```math
-\frac{\partial\rho_g}{\partial w_{ij}}
```

is not adopted as the default because viability boundaries need not be smooth.

The primary proposed interface sensitivity is therefore finite perturbation:

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
\theta_{ij}
=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
```

Possible viability functionals include

```math
\operatorname{Vol}(\mathcal V),
\qquad
\rho_E,
\qquad
\rho_g,
\qquad
T_{\mathcal V},
\qquad
T_K.
```

Differentiability-based sensitivity may be used only where smoothness is demonstrated.

---

## 13. Response-to-viability timing margins [P]

Stage 4 provides the response time $\tau_{\rm response}$. Stage 5 compares it with both maintainability loss and actual constraint violation.

Define

```math
S_{\mathcal V}
=T_{\mathcal V}-\tau_{\rm response},
```

and

```math
S_K
=T_K-\tau_{\rm response}.
```

Interpretation:

| Diagnostic | Meaning |
|---|---|
| $S_{\mathcal V}>0$ | Nominal response can complete before viability is lost. |
| $S_K>0$ | Nominal response can complete before an actual acceptability constraint is violated. |

Dimensionless versions are

```math
\Pi_{\mathcal V}
=
\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K
=
\frac{\tau_{\rm response}}{T_K}.
```

These are **proposed thesis diagnostics [P]**, not established universal resilience laws. Positive slack or a ratio below one does not by itself guarantee successful control.

---

## 14. Evidence status of Stage-5 objects

| Object | Status |
|---|---|
| Constraint set $K$ | **[E]** |
| Viability kernel | **[E]** |
| Finite-horizon viability | **[E]** |
| Robust controlled invariant / viable set | **[E]** |
| Stochastic viability | **[E]** |
| Capture basin | **[E]** |
| HJ reachable/viable-set computation | **[E]** |
| Control barrier functions | **[E]** |
| Euclidean/weighted distance to a set | **[E]** |
| $K_{\rm sus}$ for the thesis P–T–I–O system | **[P] application/synthesis** |
| $g_\psi(Y)$ Riemannian viability metric | **[P]** |
| $\rho_g=d_g(Y,\partial\mathcal V)$ for infrastructure resilience | **[P]** |
| Joint use of $T_{\mathcal V}$ and $T_K$ in the P–T–I–O system | **[D/P]** |
| $S_{\mathcal V},S_K$ | **[P]** |
| $\Pi_{\mathcal V},\Pi_K$ | **[P]** |
| $S_{ij}^{\mathcal V}$ interface sensitivity | **[P]** |
| Learned/certified reachability methods | **[E] method; optional computational choice** |

Freezing Stage 5 freezes this **status classification**. It does not relabel proposed constructs as established theory.

---

## 15. Final frozen Stage-5 scope

| Item | Canonical Stage-5 specification |
|---|---|
| **Stage** | Controlled Sustainable Viability |
| **Question** | Under what conditions can acceptable functions be maintained, and how far and how long is the system from unacceptable states? |
| **Inputs** | $F^m$, $\mathcal G(t)$, $\mathfrak I$, $\mathcal U(z_I,z_O)$, $u$, $h$, uncertainty class $\Xi$ |
| **Viability state** | $Y_V=\mathcal P_V(Y)$, when reduction is required and validated |
| **Constraint region** | $K_{\rm sus}(t)=\{Y_V:g_r(Y_V,t)\le0\}$ |
| **Core set** | $\mathcal V_{\rm sus}^{u,T}=\operatorname{Viab}_{F,\mathcal U}^{T}(K_{\rm sus})$ |
| **Robust extension** | $\mathcal V_{\rm rob}^{T}$ |
| **Stochastic extension** | $\mathcal V_{\varepsilon}^{T}$ |
| **Boundary** | $\partial\mathcal V_{\rm sus}^{u,T}$ |
| **Baseline geometry** | $\rho_E=d(\widetilde Y_V,\partial\widetilde{\mathcal V})$ |
| **Proposed geometry** | $\rho_g=d_{g_\psi}(Y_V,\partial\mathcal V)$ |
| **Time to viability loss** | $T_{\mathcal V}$ |
| **Time to unacceptable state** | $T_K$ |
| **Response margins** | $S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response}$ and $S_K=T_K-\tau_{\rm response}$ |
| **Dimensionless timing diagnostics** | $\Pi_{\mathcal V}=\tau_{\rm response}/T_{\mathcal V}$ and $\Pi_K=\tau_{\rm response}/T_K$ |
| **Interface analysis** | $S_{ij}^{\mathcal V}$ through finite perturbation/sensitivity |
| **Computation** | Validated set-computation, HJ, invariance, decomposition, or approximation methods |
| **Certification** | Classical/analytical benchmarks first; learned methods only with explicit verification |
| **Primary outputs** | $K_{\rm sus}$, $\mathcal V$, $\partial\mathcal V$, $\rho$, $T_{\mathcal V}$, $T_K$, $S_{\mathcal V}$, $S_K$, $S_{ij}^{\mathcal V}$ |

The key mathematical relation is

```math
K_{\rm sus}
\supseteq
\mathcal V_{\rm sus}^{u,T}.
```

The distinction then becomes

```math
\mathcal V_{\rm sus}^{u,T}
\rightarrow
\partial\mathcal V
\rightarrow
\{\rho,T_{\mathcal V},T_K\}.
```

The first five stages connect as

```math
\{P,T,I,O\}
\rightarrow
\mathfrak I
\rightarrow
\{F,\mathcal G,m\}
\rightarrow
\{\widehat X,\mathcal U,u,\tau_{\rm response}\}
\rightarrow
\{K_{\rm sus},\mathcal V,\partial\mathcal V,\rho,T_{\mathcal V},T_K\}.
```

### Status

> **STAGE 5 SCIENTIFIC SCOPE: FROZEN**

The proposed objects $g_\psi$, $\rho_g$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$, and $S_{ij}^{\mathcal V}$ remain explicitly **[P] thesis constructs** inside the frozen Stage-5 scope.

---

## 16. Stage boundaries

| Stage | Responsibility |
|---|---|
| **3** | Generate coupled hybrid multiscale trajectories. |
| **4** | Observe, infer, coordinate, and control those trajectories. |
| **5** | Determine acceptability, maintainability, geometric/temporal proximity to loss, and interdependency sensitivity. |
| **6** | Translate verified resilience results into sustainability-transition requirements. |

Stage 5 therefore ends with **validated viability evidence**, not with transformation prescriptions.

---

## References

Ames, A. D., Xu, X., Grizzle, J. W., & Tabuada, P. (2017). Control barrier function based quadratic programs for safety critical systems. *IEEE Transactions on Automatic Control, 62*(8), 3861–3876. https://doi.org/10.1109/TAC.2016.2638961

Aubin, J.-P. (1990). A survey of viability theory. *SIAM Journal on Control and Optimization, 28*(4), 749–788. https://doi.org/10.1137/0328044

Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability theory: New directions* (2nd ed.). Springer. https://doi.org/10.1007/978-3-642-16684-6

Bansal, S., Chen, M., Herbert, S. L., & Tomlin, C. J. (2017). Hamilton-Jacobi reachability: A brief overview and recent advances. In *2017 IEEE 56th Annual Conference on Decision and Control* (pp. 2242–2253). IEEE. https://doi.org/10.1109/CDC.2017.8263977

Bansal, S., & Tomlin, C. J. (2021). DeepReach: A deep learning approach to high-dimensional reachability. In *2021 IEEE International Conference on Robotics and Automation* (pp. 1817–1824). IEEE. https://doi.org/10.1109/ICRA48506.2021.9561949

Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth’s Future, 6*(7), 979–996. https://doi.org/10.1002/2017EF000660

Blanchini, F. (1999). Set invariance in control. *Automatica, 35*(11), 1747–1767. https://doi.org/10.1016/S0005-1098(99)00113-2

De Lara, M., & Doyen, L. (2008). *Sustainable management of natural resources: Mathematical models and methods*. Springer. https://doi.org/10.1007/978-3-540-79074-7

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Doyen, L., & Gajardo, P. (2020). Sustainability standards, multicriteria maximin, and viability. *Natural Resource Modeling, 33*(3), e12250. https://doi.org/10.1111/nrm.12250

Doyen, L., & Saint-Pierre, P. (1997). Scale of viability and minimal time of crisis. *Set-Valued Analysis, 5*(3), 227–246. https://doi.org/10.1023/A:1008610123440

Gajardo, P., & Hermosilla, C. (2019). The viability kernel of dynamical systems with mixed constraints: A level-set approach. *Systems & Control Letters, 127*, 6–12. https://doi.org/10.1016/j.sysconle.2019.03.006

Kiss, A. K., Molnar, T. G., Ames, A. D., & Orosz, G. (2023). Control barrier functionals: Safety-critical control for time delay systems. *International Journal of Robust and Nonlinear Control*. https://doi.org/10.1002/rnc.6751

Lygeros, J., Tomlin, C., & Sastry, S. (1999). Controllers for reachability specifications for hybrid systems. *Automatica, 35*(3), 349–370. https://doi.org/10.1016/S0005-1098(98)00193-9

Maidens, J. N., Kaynama, S., Mitchell, I. M., Oishi, M. M. K., & Dumont, G. A. (2013). Lagrangian methods for approximating the viability kernel in high-dimensional systems. *Automatica, 49*(7), 2017–2029. https://doi.org/10.1016/j.automatica.2013.03.020

Martin, S., Deffuant, G., & Calabrese, J. M. (2011). Defining resilience mathematically: From attractors to viability. In *Viability and resilience of complex systems* (pp. 15–36). Springer. https://doi.org/10.1007/978-3-642-20423-4_2

Mitchell, I. M., Bayen, A. M., & Tomlin, C. J. (2005). A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games. *IEEE Transactions on Automatic Control, 50*(7), 947–957. https://doi.org/10.1109/TAC.2005.851439

Rungger, M., & Tabuada, P. (2017). Computing robust controlled invariant sets of linear systems. *IEEE Transactions on Automatic Control, 62*(7), 3665–3670. https://doi.org/10.1109/TAC.2017.2672859

Saint-Pierre, P. (1994). Approximation of the viability kernel. *Applied Mathematics & Optimization, 29*, 187–209. https://doi.org/10.1007/BF01204182

Solanki, P., Vertovec, N., Schnitzer, Y., van Beers, J., de Visser, C., & Abate, A. (2025). Certified Approximate Reachability (CARe): Formal error bounds on deep learning of reachable sets. In *2025 IEEE Conference on Decision and Control*. https://doi.org/10.1109/CDC57313.2025.11312709

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458
