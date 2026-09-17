# Stage 3 — Coupled Hybrid Multiscale Dynamics

![Stage](https://img.shields.io/badge/Stage%203-FROZEN-1A7F37)

**Framework stage:** Stage 3 — Coupled Hybrid Multiscale Dynamics  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Change rule:** Do not revise this Stage-3 scientific scope unless explicitly requested and versioned.  
**Framework preservation rule:** This file formalizes Stage 3 only. It does not alter the seven-stage framework, Stage-1 system definition, or Stage-2 interdependency object.

> **Rendering rule:** Long mathematical systems are split into readable display blocks. Equation identifiers are written as Markdown labels rather than `\tag{...}` to improve GitHub rendering.

---

## RQ3 / SO3 — current canonical question

> **How, when, and where do accepted interdependency mechanisms evolve and propagate through the coupled system?**

**Specific objective:** Develop and verify a physics-based hybrid multiscale dynamic model and test its incremental explanatory or predictive value against independent and static-coupling representations.

**Question authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`. This 2026-09-17 wording amendment aligns the question with Chapter I; technical results and validation status are unchanged.

The first three stages form the progression

```math
\{P,T,I,O\}
\rightarrow
\mathfrak I_{ij}^{\alpha\beta}
\rightarrow
\{Y(t),\mathcal G(t),m(t),T_C\}.
```

Stage 1 defines what exists. Stage 2 defines why one component or layer can causally affect another. Stage 3 evolves those accepted mechanisms through time and space.

---

## 1. Scientific object of Stage 3

The canonical four-layer state remains

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
```

| State | Meaning |
|---|---|
| $x_P(t)$ | physical state of the power system |
| $x_T(t)$ | physical state of the multimodal transportation system |
| $z_I(t)$ | dynamic state of the information layer |
| $z_O(t)$ | dynamic state of the organizational layer |

Stage 3 keeps the hybrid operating mode separate:

```math
m(t)=\text{current operating/disruption/recovery mode},
```

and therefore uses the augmented state

```math
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
```

This prevents the discrete mode from being counted twice when equations already condition on $m(t)$.

The coupled subsystems are not forced into one equation class. Power, transportation, information, and organization obey different physical or process laws and may operate at different temporal resolutions (Hardy et al., 2024; Sun et al., 2021).

> **Coupled does not mean mathematically identical.** It means heterogeneous dynamical processes exchange causal state variables through accepted interdependencies.

---

## 2. Governing hybrid delayed multirate architecture [P]

Partition the state into continuous/quasi-continuous states $Y_c$ and discrete states $Y_d$, while keeping $m$ explicit.

**Equation S3.1 — Coupled hybrid architecture**

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

This is a **thesis synthesis [P]** of established dynamic-interdependency, hybrid-system, temporal-network, delayed-system, and co-simulation concepts (Cimellaro et al., 2024; Goldbeck et al., 2019; Hardy et al., 2024; Zhang & Peeta, 2014).

| Symbol | Meaning |
|---|---|
| $Y_c$ | continuous or quasi-continuous states |
| $Y_d$ | discrete states |
| $\boldsymbol\delta=\{\delta_{ij}\}$ | causal delays inherited from Stage 2 |
| $h(\mathbf r,t)$ | spatiotemporal hazard/disturbance field |
| $R_e$ | event-reset map |
| $\Delta_m$ | mode-transition operator |
| $\Psi$ | network/coupling update operator |

Temporal-network research shows that event ordering can materially alter cascading outcomes, so chronology must not be erased by a purely static representation (Cimellaro et al., 2024).

---

## 3. Native dynamics of the P–T–I–O system

| Layer/system | Dynamic quantities | Representative model family |
|---|---|---|
| Power $P$ | voltage, power flow, frequency where needed, DER/storage, charging, traction power | AC/DC power flow, DistFlow, algebraic/DAE/dynamic models as required |
| Road $T_R$ | density, flow, speed, congestion, accessibility | CTM, dynamic traffic assignment, microscopic simulation |
| Electric bus $T_B$ | location, route, SOC, charging, queue | routing, SOC, queueing, vehicle/fleet models |
| Urban rail $T_U$ | train position, speed, traction demand, service state | train-motion and traction-power models |
| Heavy/regional rail $T_H$ | train movement and traction demand | train-motion and traction-network models |
| Information $I$ | availability, latency, quality, freshness, loss, estimation error, synchronization | delay, stochastic, communication, discrete-event models |
| Organization $O$ | authority, coordination, resources, workforce, mobilization, repair chronology | state-transition, discrete-event, routing, scheduling, resource-allocation models |

A single temporal resolution is not assumed to be adequate for all P–T–I–O processes (Hardy et al., 2024; Sun et al., 2021).

---

## 4. Power-system dynamics

At infrastructure-resilience timescales, full electromagnetic-transient simulation is not automatically required. Power-system feasibility may be represented by algebraic constraints

```math
0=G_P\!\left(x_P,x_T,z_I,h;\mathcal G_P,m\right),
```

or by dynamic/DAE formulations when the research question requires them:

```math
M_P\dot x_P
=F_P\!\left(x_P,x_T,z_I,h;\mathcal G_P,m\right).
```

A representative power state is

```math
x_P=
[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC_B]^\top.
```

The model must permit state-changing events such as overloads, feeder/line trips, substation failures, capacity loss, switching, islanding, and restoration.

Rail interaction retains the traction-power interface:

```math
P_{Tr/D}
\leftrightarrow
P_{TP}
\leftrightarrow
(T_U,T_H),
```

because explicit railway–traction–power representation can change vulnerability and cascading conclusions (Bellè et al., 2022).

---

## 5. Multimodal transportation dynamics

Stage 1 defines

```math
T=\{T_R,T_B,T_U,T_H,T_M\}.
```

For road traffic, a generic conservation law is

```math
\frac{\partial k(x,t)}{\partial t}
+
\frac{\partial q(x,t)}{\partial x}
=s(x,t),
```

or an equivalent CTM, dynamic-traffic-assignment, or microscopic representation.

For EVs and electric buses, a battery-SOC model may take the form

```math
\dot{SOC}_v
=-\frac{P_v^{\mathrm{drive}}}{E_v}
+\eta_c\frac{P_v^{\mathrm{ch}}}{E_v}
-\frac{P_v^{\mathrm{V2G}}}{\eta_dE_v}.
```

Dynamic P–T studies show that departure time, route choice, charging queues, charging demand, and distribution states can interact dynamically rather than through a static charging-load approximation alone (Li et al., 2024).

For rail,

```math
\dot s_r=v_r,
\qquad
M_r\dot v_r=F_r^{\mathrm{tr}}-F_r^{\mathrm{res}}-F_r^{\mathrm{br}},
```

with state-dependent traction demand

```math
P_r^{\mathrm{tr}}(t)
=
\mathcal P(s_r,v_r,a_r,V_{TP},\eta_r).
```

Thus

```math
\text{train motion}
\rightleftarrows
\text{traction-power state}.
```

---

## 6. Information-layer dynamics

Stage 3 represents the **dynamic condition of information**, not the Stage-4 estimator or controller.

The canonical information state is

```math
z_I(t)
=
[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top.
```

A delayed measurement channel may be represented as

```math
y_I(t)
=
H_I\!\left[X(t-\delta_I)\right]
+\varepsilon_I(t).
```

Information freshness remains distinct from communication latency. Age of Information is

```math
\Delta_I(t)=t-U(t),
```

where $U(t)$ is the generation time of the freshest received update (Yates et al., 2021).

The estimator

```math
\widehat X(t)=\mathcal E\!\left(y_{[0,t]},z_I(t)\right)
```

belongs to Stage 4; Stage 3 only evolves the information conditions that affect it.

---

## 7. Organizational-layer dynamics

Organizational processes are not assigned artificial physical equations merely to make all layers mathematically identical.

The canonical organizational state is

```math
z_O(t)
=
[A_O,C_O,R_O,W_O,\tau_D,\tau_C^{O},\tau_M]^\top.
```

Auxiliary variables such as crew count or component-specific repair status may be introduced when a model requires them, but they do not replace the canonical state definition.

A typical response chronology is

```math
\text{monitor}
\rightarrow
\text{assess}
\rightarrow
\text{decide}
\rightarrow
\text{coordinate}
\rightarrow
\text{mobilize}
\rightarrow
\text{execute}.
```

Transportation accessibility creates a measurable $T\rightarrow O\rightarrow P$ pathway. For crew $c$ travelling to damaged component $j$,

```math
\tau_{\mathrm{arrival}}^{c,j}
=
\tau_{\mathrm{dispatch}}^{c}
+TT_{r(c,j)}[x_T(t)],
```

and the associated restoration time may be

```math
t_{\mathrm{restore},j}
=
\tau_{\mathrm{arrival}}^{c,j}
+\tau_{\mathrm{repair},j}.
```

Stage 3 evolves travel, arrival, repair, and restoration times; the policy selecting crews or priorities belongs to Stage 4.

---

## 8. Translating Stage-2 mechanisms into Stage-3 dynamics

Stage 2 provides

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t\right).
```

Stage 3 maps the accepted mechanism $M_{ij}$ into a dynamic transmission map.

**Equation S3.2 — Dynamic interdependency transmission**

```math
\begin{aligned}
\mathcal C_{ij}^{\alpha\beta}(t)
={}&a_{ij}(t)w_{ij}(t)\\
&\times\mathcal M_{ij}^{\alpha\beta}\!\left[
E_i^\alpha(t-\delta_{ij}),
E_j^\beta(t),m(t),\mathcal H_t
\right].
\end{aligned}
```

Here $\mathcal M_{ij}^{\alpha\beta}$ is the dynamic transmission map induced by the Stage-2 causal mechanism $M_{ij}$. The two symbols are intentionally distinct.

For EV charging,

```math
P_D\rightarrow P_C\rightarrow T_R,
```

and a shortage can propagate through a mechanism-specific chain such as

```math
P_c<P_c^{\mathrm{req}}
\Rightarrow
SOC_v\downarrow
\Rightarrow
\text{mobility availability}\downarrow.
```

For transportation-dependent restoration,

```math
T_R\rightarrow O_L\rightarrow P_D,
```

and increasing road travel time can delay crew arrival, repair, and restoration.

> **Stage 2 identifies the causal edge; Stage 3 evolves its consequence through time.**

---

## 9. Hybrid modes and events

The system combines continuous evolution, discrete events, and mode switching.

A provisional mode set is

```math
m(t)\in\mathcal M=\{N,D,C,R\},
```

where $N$ = normal, $D$ = degraded, $C$ = cascading, and $R$ = recovery. These labels may be refined without changing the Stage-3 architecture.

Interdependency activation may depend on mode, for example

```math
a_{ij}^{N}=0,
\qquad
a_{ij}^{R}=1,
```

when a recovery-specific coupling is inactive during normal operation and active during restoration (Danziger & Barabási, 2022).

The Stage-3 event set may include failures, trips, capacity reductions, road closures, communication losses, charging events, executed switching, dispatched-resource arrivals, repairs, and restorations.

An event can produce

```math
(Y,m,\mathcal G,a)
\rightarrow
(Y^+,m^+,\mathcal G^+,a^+).
```

A dispatch **decision rule** belongs to Stage 4; Stage 3 may consume the resulting executed dispatch as an event.

---

## 10. Dynamic topology and state-dependent coupling

The effective coupled graph is not assumed constant:

```math
\mathcal G(t)
=
\mathcal G\!\left[Y(t),m(t),h(t),\mathcal H_t\right].
```

A compact feedback representation is

```math
\mathcal G(t)
\rightarrow
F_{\mathcal G(t)}
\rightarrow
Y(t)
\rightarrow
\{a_{ij}(t),w_{ij}(t),m(t)\}
\rightarrow
\mathcal G(t+\Delta t).
```

The statement $\mathcal G\rightleftarrows Y$ means that the **effective structure available for propagation** may change with state, damage, mode, recovery, and history; it does not imply that every physical edge continuously changes.

---

## 11. Multiscale temporal structure

The framework does not impose one universal timescale. A representative Stage-3 set is

```math
\boldsymbol\tau_{S3}
=
\{\tau_P,\tau_{T_R},\tau_{T_B},\tau_{T_U},\tau_{T_H},
\tau_I,\tau_O,\tau_{\rm travel},\tau_{\rm repair},\tau_C\}.
```

The governing timing distinction is

```math
\text{event time}
\neq
\delta_{ij}
\neq
\tau_{ij}.
```

Here $\delta_{ij}$ is the cause-to-effect lag, whereas $\tau_{ij}$ is the characteristic rate/duration of the mechanism.

---

## 12. Spatial cascade dynamics

Stage 3 distinguishes **where** disruption propagates from **when** it arrives.

**Equation S3.3 — Cascade-arrival time**

```math
T_C(j)
=
\inf\{t>t_0:j\text{ enters a predefined disrupted state}\}.
```

For mechanisms with a meaningful spatial front, define $r_c(t)$ and

```math
v_c(t)=\frac{dr_c(t)}{dt}.
```

Constant-velocity propagation is not assumed. The thesis may test

```math
v_c=v_c(Y,\mathcal G,m,h)
```

when the spatial-front interpretation is physically defensible. Zhao et al. (2016) provide precedent for space–time cascade analysis in a specific class of spatial networks, not a universal infrastructure law.

---

## 13. Uncertainty

Stage 3 admits uncertainty in variables that materially alter dynamic trajectories, for example

```math
\Xi
=
\{h,\text{failure state},\text{demand},\text{travel time},
\text{repair time},\delta_I,A_I\}.
```

Scenario generation, Monte Carlo simulation, and sensitivity analysis may be used when consistent with the uncertainty model. Uncertainty is not promoted to a separate framework stage.

---

## 14. Computational architecture

The preferred integration principle is **hybrid multirate co-simulation**, allowing heterogeneous subsystem models to retain their native equations and clocks. HELICS provides an established example of federated multi-domain co-simulation (Hardy et al., 2024).

The governing fidelity rule is

```math
\text{maximum necessary physical fidelity}
\neq
\text{maximum possible model detail}.
```

A model resolution is justified only when it materially supports the research question and validation obligation.

---

## 15. Validation and falsification

Stage 3 validation must test both system outcomes and the mechanisms that generate them.

| Validation target | Example check |
|---|---|
| Native subsystem behavior | physical/dimensional consistency and known limiting cases |
| Cross-layer coupling | interface balance, sign, units, and causal direction |
| Event chronology | event ordering and reproducibility |
| Timing | sensitivity to delay and characteristic timescale |
| Topology | dynamic-graph consistency under failure/recovery |
| Numerical integration | synchronization and convergence where applicable |
| Uncertainty | scenario/sensitivity robustness |
| Coupling importance | ablation of selected Stage-2 mechanisms |

A representative chronology is

```math
\begin{aligned}
t_{\rm failure}
&<t_{\rm detected}
<t_{\rm estimated}
<t_{\rm decision}\\
&<t_{\rm mobilized}
<t_{\rm arrival}
<t_{\rm repair},
\end{aligned}
```

but this ordering is a **testable chronology**, not a universal law; parallel or reordered processes may occur.

For coupling ablation, a selected mechanism is removed or neutralized while other conditions are matched. Model variants should use symbols such as

```math
\mathscr M_{PT},
\qquad
\mathscr M_{PTI},
\qquad
\mathscr M_{PTIO},
```

to avoid collision with the Stage-2 mechanism symbol $M_{ij}$.

If removing a coupling produces no meaningful and reproducible change in trajectories, event order, cascade arrival, recovery, or later viability, its explanatory importance must be reconsidered.

---

## 16. Boundary of Stage 3

| Object/question | Stage ownership |
|---|---|
| $\mathfrak I_{ij}^{\alpha\beta}$ and causal admissibility | Stage 2 |
| $Y(t)$, $m(t)$, $\mathcal G(t)$, dynamic propagation | **Stage 3** |
| $\widehat X$, $b_t$, $\mathcal U$, policy $u=\pi(\cdot)$ | Stage 4 |
| $K_{\rm sus}$, $\mathcal V_{\rm sus}^{u,T}$, $\rho_E$, $\rho_g$, $T_{\mathcal V}$, $T_K$ | Stage 5 |

The stage boundary is therefore:

> **Stage 3 produces trajectories; Stage 4 observes and controls them; Stage 5 evaluates their viability.**

---

## 17. Final frozen Stage-3 scope

| Item | Canonical Stage-3 specification |
|---|---|
| **Stage** | Coupled Hybrid Multiscale Dynamics |
| **Question** | How, when, and where do accepted interdependency mechanisms evolve and propagate? |
| **Four-layer state** | $Y(t)=[x_P,x_T,z_I,z_O]^\top$ |
| **Augmented hybrid state** | $\widetilde Y(t)=(Y(t),m(t))$ |
| **Interdependency input** | $\mathfrak I_{ij}^{\alpha\beta}$ |
| **Hybrid structure** | continuous dynamics + algebraic constraints + discrete events + mode switching |
| **Network evolution** | $\mathcal G(t)\rightleftarrows Y(t)$ |
| **Temporal structure** | causal delays $\delta_{ij}$ + heterogeneous characteristic timescales $\tau$ |
| **Spatial structure** | $T_C(j)$ and, only where meaningful, $r_c(t),v_c(t)$ |
| **Uncertainty** | hazard, failure, demand, travel, repair, information-state uncertainty |
| **Computation** | hybrid multirate co-simulation / equivalent validated integration strategy |
| **Outputs** | $Y(t)$, $m(t)$, $\mathcal G(t)$, event sequence, $T_C(j)$, and service/recovery trajectories |

The central scientific opportunity is a causal–temporal bridge joining multimodal power–transport dynamics, traction-power interactions, information degradation, organizational response conditions, dynamic interdependencies, and disruption propagation. The thesis must test the value of this joint representation rather than presume novelty from combination alone.

---

## References

Bellè, A., Zeng, Z., Duval, C., Sango, M., & Barros, A. (2022). Modeling and vulnerability analysis of interdependent railway and power networks: Application to British test systems. *Reliability Engineering & System Safety, 217*, 108091. https://doi.org/10.1016/j.ress.2021.108091

Cimellaro, G. P., Cardoni, A., & Reinhorn, A. (2024). Modelling infrastructure interdependencies and cascading effects using temporal networks. *Resilient Cities and Structures, 3*(3), 28–42. https://doi.org/10.1016/j.rcns.2024.05.002

Danziger, M. M., & Barabási, A.-L. (2022). Recovery coupling in multilayer networks. *Nature Communications, 13*(1), Article 955. https://doi.org/10.1038/s41467-022-28379-5

Goldbeck, N., Angeloudis, P., & Ochieng, W. Y. (2019). Resilience assessment for interdependent urban infrastructure systems using dynamic network flow models. *Reliability Engineering & System Safety, 188*, 62–79. https://doi.org/10.1016/j.ress.2019.03.007

Hardy, T. D., Palmintier, B., Top, P., Krishnamurthy, D., & Fuller, J. C. (2024). HELICS: A co-simulation framework for scalable multi-domain modeling and analysis. *IEEE Access, 12*, 24325–24347. https://doi.org/10.1109/ACCESS.2024.3363615

Li, J., Xu, X., Yan, Z., Wang, H., & Chen, Y. (2024). Dynamic flow equilibrium of transportation and power distribution networks considering flexible traveling choices and voltage quality improvement. *CSEE Journal of Power and Energy Systems*. Advance online publication. https://doi.org/10.17775/CSEEJPES.2022.04810

Lian, X., Song, C., Li, Z., Qiu, L., & Liu, L. (2026). Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards. *Applied Energy, 403*, 127004. https://doi.org/10.1016/j.apenergy.2025.127004

Sun, Y., Zhao, P., Wang, L., & Malik, S. M. (2021). Spatial and temporal modelling of coupled power and transportation systems: A comprehensive review. *Energy Conversion and Economics, 2*(2), 55–66. https://doi.org/10.1049/enc2.12034

Wang, W., Fang, X., & Florita, A. (2021). Impact of DER communication delay in AGC: Cyber-physical dynamic co-simulation. In *2021 IEEE 48th Photovoltaic Specialists Conference (PVSC)* (pp. 2616–2620). IEEE. https://doi.org/10.1109/PVSC43889.2021.9518779

Yang, X., & Zhang, M. (2026). Resilience analysis of road transportation-electric power system considering interdependencies under earthquake effects. *Reliability Engineering & System Safety, 275*, 112819. https://doi.org/10.1016/j.ress.2026.112819

Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. (2021). Age of information: An introduction and survey. *IEEE Journal on Selected Areas in Communications, 39*(5), 1183–1210. https://doi.org/10.1109/JSAC.2021.3065072

Zhang, P., & Peeta, S. (2014). Dynamic and disequilibrium analysis of interdependent infrastructure systems. *Transportation Research Part B: Methodological, 67*, 357–381. https://doi.org/10.1016/j.trb.2014.04.008

Zhao, J., Li, D., Sanhedrai, H., Cohen, R., & Havlin, S. (2016). Spatio-temporal propagation of cascading overload failures in spatially embedded networks. *Nature Communications, 7*, Article 10094. https://doi.org/10.1038/ncomms10094

