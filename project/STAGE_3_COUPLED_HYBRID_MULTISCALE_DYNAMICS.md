# Stage 3 — Coupled Hybrid Multiscale Dynamics

**Framework stage:** Stage 3 — Coupled Hybrid Multiscale Dynamics  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Change rule:** Do not revise this Stage-3 scope unless explicitly requested and versioned.  
**Framework preservation rule:** This document formalizes Stage 3 only. It does **not** alter the frozen seven-stage framework, the Stage-1 system definition, or the Stage-2 interdependency object.

---

## Research question

$$
\boxed{\textbf{How do the coupled systems evolve over space and time, and how do disruptions propagate?}}
$$

The first three stages form a strict scientific progression:

$$
\boxed{
\underbrace{\{P,T,I,O\}}_{\text{Stage 1: what exists}}
\rightarrow
\underbrace{\mathfrak I_{ij}^{\alpha\beta}}_{\text{Stage 2: why / through what mechanism}}
\rightarrow
\underbrace{\text{dynamic evolution and propagation}}_{\text{Stage 3: how / when / where}}
}
$$

Stage 1 establishes the entities, layers, and possible locations of interaction. Stage 2 identifies the causal mechanisms through which one component or layer affects another. Stage 3 determines how accepted mechanisms alter system states over space and time once active. Dynamic interdependency research shows that infrastructure interactions can evolve over multiple temporal horizons and that static representations are insufficient for many cascading-failure, recovery, and disequilibrium problems (Zhang & Peeta, 2014).

---

## 1. Scientific object of Stage 3

To preserve the canonical Stage-1 notation, the four-layer system state remains

$$
\boxed{
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}
}
$$

with

$$
x_P(t)=\text{physical state of the power system},
$$

$$
x_T(t)=\text{physical state of the multimodal transportation system},
$$

$$
z_I(t)=\text{dynamic state of the information layer},
$$

and

$$
z_O(t)=\text{dynamic state of the organizational layer}.
$$

Stage 3 introduces an additional **hybrid operating mode**

$$
\boxed{m(t)=\text{current operating, disruption, cascading, or recovery mode}}
$$

without redefining the Stage-1 state symbol. The augmented Stage-3 state is therefore

$$
\boxed{\widetilde Y(t)=\big(Y(t),m(t)\big).}
$$

This distinction prevents mode information from being counted twice when the hybrid equations already condition on $m(t)$.

The constituent systems are not forced into a single homogeneous equation class. Power and transportation obey different physical laws; information contains communication, availability, latency and estimation-related processes; organizational recovery contains state transitions, resources, schedules and discrete events. Coupled power–transport models also span different spatial and temporal resolutions (Sun et al., 2021), while multi-domain co-simulation is specifically designed to allow heterogeneous simulators to interact without removing their native dynamics (Hardy et al., 2024).

Therefore,

$$
\boxed{\textbf{Coupled does not mean mathematically identical.}}
$$

Rather,

$$
\boxed{\textbf{Coupled}=\text{heterogeneous dynamical systems exchanging causal state variables}.}
$$

---

## 2. Governing Stage-3 architecture

The canonical Stage-3 architecture is a **hybrid delayed multirate dynamical system**. Partition the state variables into continuous/quasi-continuous states $Y_c$ and discrete states $Y_d$ while keeping the operating mode $m$ explicit:

$$
\boxed{
\begin{aligned}
\dot Y_c(t)
&=F^{m(t)}\!\left[
Y_c(t),Y_d(t),Y(t-\boldsymbol\delta),h(\mathbf r,t);
\mathcal G(t),\mathcal H_t
\right],\\[1mm]
0
&=G^{m(t)}\!\left[
Y_c(t),Y_d(t),h(\mathbf r,t);\mathcal G(t)
\right],\\[1mm]
Y_d(t_e^+)
&=R_e\!\left[\widetilde Y(t_e^-),e\right],\\[1mm]
m(t_e^+)
&=\Delta_m\!\left[m(t_e^-),\widetilde Y(t_e^-),e\right],\\[1mm]
\mathcal G(t_e^+)
&=\Psi\!\left[\mathcal G(t_e^-),\widetilde Y(t_e^-),e,\mathcal H_t\right].
\end{aligned}
}
\tag{S3.1}
$$

This formulation is **proposed in this thesis**. It is a synthesis of established ideas from dynamic infrastructure interdependency modeling, temporal networks, hybrid disruption/recovery modeling, delayed cyber-physical systems, and federated co-simulation (Cimellaro et al., 2024; Goldbeck et al., 2019; Hardy et al., 2024; Zhang & Peeta, 2014).

Here,

$$
Y_c=\text{continuous or quasi-continuous states},
$$

$$
Y_d=\text{discrete states},
$$

$$
\boldsymbol\delta=\{\delta_{ij}\}=\text{causal delays inherited from Stage 2},
$$

$$
h(\mathbf r,t)=\text{spatiotemporal hazard/disturbance field},
$$

$$
R_e=\text{event-reset map},\qquad
\Delta_m=\text{mode-transition operator},\qquad
\Psi=\text{network/coupling update operator}.
$$

Temporal-network research shows that event ordering can materially alter cascading outcomes, so chronology must not be erased by purely static representations (Cimellaro et al., 2024).

---

## 3. Native dynamics of the four-layer system

The framework retains native model families appropriate to each subsystem.

| System | Dynamic quantities in Stage 3 | Appropriate model family |
|---|---|---|
| Power $P$ | voltage, power flow, frequency where needed, DER, storage, charging, traction power | AC/DC power flow, DistFlow, algebraic or DAE formulations |
| Road $T_R$ | density, flow, speed, congestion, accessibility | CTM, dynamic traffic assignment, microscopic simulation |
| Electric bus $T_B$ | location, route, SOC, charging, queue | vehicle dynamics, routing, SOC and queue models |
| Urban rail $T_U$ | metro/MRT/LRT/tram position, speed, traction demand | train-motion and traction-power models |
| Heavy/regional rail $T_H$ | commuter/intercity rail movement and traction demand | train-motion and traction-network models |
| Information $I$ | availability, latency, freshness, loss, information error | delay, stochastic and discrete-event models |
| Organization $O$ | organizational state, resources, crews, coordination, mobilization, repair | state-transition, discrete-event, routing and scheduling models |

Coupled power and transportation literature explicitly distinguishes short-, medium-, and long-term representations, demonstrating that a single temporal resolution is generally inadequate for all relevant P–T processes (Sun et al., 2021).

---

## 4. Power-system dynamics

At infrastructure-resilience timescales, full electromagnetic-transient simulation is not automatically required. Power-system feasibility may be represented through algebraic constraints,

$$
\boxed{0=G_P\!\left(x_P,x_T,z_I,h;\mathcal G_P,m\right),}
$$

or, when genuinely dynamic electrical states are necessary,

$$
\boxed{M_P\dot x_P=F_P\!\left(x_P,x_T,z_I,h;\mathcal G_P,m\right).}
$$

Representative states are

$$
\boxed{x_P=[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC_B]^\top.}
$$

The model must permit state-changing events such as overloads, line/feeder trips, substation failures, capacity loss, switching, islanding, and restoration.

Rail transport must not be reduced to an abstract electrical load when the research question concerns interdependency and propagation. Explicit railway–traction–external-power modeling has been shown to alter vulnerability and cascading-failure conclusions (Bellè et al., 2022). Hence,

$$
\boxed{P_{Tr/D}\leftrightarrow P_{TP}\leftrightarrow (T_U,T_H).}
$$

---

## 5. Multimodal transportation dynamics

Stage 1 established

$$
\boxed{T=\{T_R,T_B,T_U,T_H,T_M\}.}
$$

Stage 3 therefore permits heterogeneous multimodal transportation dynamics.

For road traffic, a generic conservation law is

$$
\boxed{\frac{\partial k(x,t)}{\partial t}+\frac{\partial q(x,t)}{\partial x}=s(x,t),}
$$

or an equivalent discrete Cell Transmission Model / microscopic representation when required.

For EVs and electric buses, battery state may evolve as

$$
\boxed{
\dot{SOC}_v
=-\frac{P_v^{drive}}{E_v}
+\eta_c\frac{P_v^{ch}}{E_v}
-\frac{P_v^{V2G}}{\eta_dE_v}.
}
$$

Dynamic P–T studies show that departure time, route choice, charging queues, charging demand, and distribution-network states can interact dynamically rather than through a static charging-load approximation alone (Li et al., 2024).

For rail,

$$
\boxed{\dot s_r=v_r,}
$$

$$
\boxed{M_r\dot v_r=F_r^{tr}-F_r^{res}-F_r^{br}.}
$$

Traction demand is consequently state dependent:

$$
\boxed{P_r^{tr}(t)=\mathcal P(s_r,v_r,a_r,V_{TP},\eta_r).}
$$

Therefore,

$$
\boxed{\text{train motion}\rightleftarrows\text{traction-power state}.}
$$

Explicit railway–traction–power modeling provides direct precedent for this bidirectional representation (Bellè et al., 2022).

---

## 6. Information dynamics

Stage 3 represents the **dynamic condition of information**, not the design of the observer or feedback controller.

Use

$$
\boxed{z_I(t)=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_I]^\top,}
$$

where $A_I$ is availability, $L_I$ latency, $Q_I$ information quality, $\Delta_I$ information freshness, $p_{\rm loss}$ packet/data loss, and $e_I$ information/estimation error.

A delayed measurement channel may be represented as

$$
\boxed{y_I(t)=H_I[X(t-\delta_I)]+\nu_I(t).}
$$

Information freshness is distinct from communication latency. Age of Information is defined by Yates et al. (2021) as

$$
\boxed{\Delta_I(t)=t-U(t),}
$$

where $U(t)$ is the generation time of the newest received status update.

Communication delay can also alter physical behavior. Wang et al. (2021) showed in a DER–AGC cyber-physical co-simulation that instability risk generally increased with communication delay under the tested settings.

However,

$$
\boxed{\widehat X(t)=\mathcal E(y,I)}
$$

is an **observer/state-estimation design** and remains in Stage 4.

---

## 7. Organizational dynamics

Organizational processes must not be assigned artificial physical equations simply to make all four layers mathematically identical.

A Stage-3 organizational state may be represented by

$$
\boxed{z_O(t)=[m_O,R_O,W_O,C_O,N_{\rm crew},\tau_D,\tau_M]^\top,}
$$

representing organizational mode, resources, workforce, coordination status, available crews, decision delay, and mobilization delay.

A typical response sequence is

$$
\boxed{
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
}
$$

Transportation accessibility creates a measurable $T\rightarrow O\rightarrow P$ dynamic mechanism. Contemporary coupled-resilience studies show that damaged/congested road networks can constrain emergency-resource deployment and affect power recovery (Lian et al., 2026; Yang & Zhang, 2026).

For crew $c$ travelling to damaged component $j$,

$$
\boxed{
\tau_{\rm arrival}^{c,j}
=\tau_{\rm dispatch}^{c}+TT_{r(c,j)}[x_T(t)].
}
$$

The corresponding restoration time is

$$
\boxed{t_{{\rm restore},j}=\tau_{\rm arrival}^{c,j}+\tau_{{\rm repair},j}.}
$$

Thus transportation dynamics alter the time at which a future restoration event occurs in the power network. Stage 3 evolves these states and event times; **the policy that chooses which crew to dispatch or which asset to prioritize belongs to Stage 4**.

---

## 8. Translation of Stage-2 interdependencies into Stage-3 dynamics

Stage 2 established

$$
\boxed{
\mathfrak I_{ij}^{\alpha\beta}
=\left(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t\right).
}
$$

Stage 3 does not replace this object. It maps each accepted causal mechanism into a dynamic transmission operator. Define

$$
\boxed{
\mathcal C_{ij}^{\alpha\beta}(t)
=a_{ij}(t)\,w_{ij}(t)\,
\mathcal M_{ij}^{\alpha\beta}
\!\left[
E_i^\alpha(t-\delta_{ij}),
E_j^\beta(t),
m(t),
\mathcal H_t
\right],
}
\tag{S3.2}
$$

where $\mathcal M_{ij}^{\alpha\beta}$ is the **dynamic transmission map induced by the Stage-2 mechanism $M_{ij}$**.

Thus,

$$
\boxed{
\text{Stage-2 causal mechanism}
\xrightarrow{\mathcal C_{ij}^{\alpha\beta}}
\text{Stage-3 dynamic consequence}.
}
$$

For EV charging,

$$
P_D\rightarrow P_C\rightarrow T_R,
$$

and a supply shortage may propagate as

$$
\boxed{
P_c(t)<P_c^{req}(t)
\Rightarrow
\dot{SOC}_v(t)\downarrow
\Rightarrow
\mathcal R_v(t)\downarrow
\Rightarrow
q_a(t+\tau)\text{ changes}.
}
$$

For transportation-dependent restoration,

$$
T_R\rightarrow O_L\rightarrow P_D,
$$

and

$$
\boxed{
TT_{\rm road}\uparrow
\Rightarrow
t_{\rm crew-arrival}\uparrow
\Rightarrow
t_{\rm repair}\uparrow
\Rightarrow
P_{\rm served}(t)\downarrow.
}
$$

The governing distinction is

$$
\boxed{
\text{Stage 2 identifies the causal edge; Stage 3 evolves its consequence through time.}
}
$$

---

## 9. Hybrid dynamics

The system contains continuous evolution and discrete changes. Dynamic infrastructure-recovery models combine changing flows with failures, repair actions, resource constraints, and restoration events (Goldbeck et al., 2019); recent P–T hazard studies similarly combine network performance with discrete damage, accessibility, deployment, and restoration states (Lian et al., 2026; Yang & Zhang, 2026).

Hence,

$$
\boxed{\text{Hybrid dynamics}=\text{continuous evolution}+\text{discrete events}+\text{mode switching}.}
$$

Provisionally,

$$
\boxed{m(t)\in\mathcal M=\{N,D,C,R\},}
$$

where

$$
N=\text{normal},\quad
D=\text{degraded},\quad
C=\text{cascading},\quad
R=\text{recovery}.
$$

The taxonomy remains **provisional at the mode-label level** and may be refined when the case study and event logic are calibrated; doing so does not alter the Stage-3 architecture.

Interdependency activation may also be mode dependent, e.g.

$$
a_{ij}^{N}=0,\qquad a_{ij}^{R}=1.
$$

Recovery-coupling research provides precedent for interdependencies that become important specifically during restoration (Danziger & Barabási, 2022).

---

## 10. Dynamic topology and state-dependent interdependencies

Stage 3 does not assume

$$
\mathcal G=\text{constant}.
$$

Instead,

$$
\boxed{\mathcal G(t)=\mathcal G[Y(t),m(t),h(t),\mathcal H_t].}
$$

The feedback is

$$
\boxed{
\mathcal G(t)
\rightarrow
F_{\mathcal G(t)}
\rightarrow
Y(t)
\rightarrow
\{a_{ij}(t),w_{ij}(t),m(t)\}
\rightarrow
\mathcal G(t+\Delta t).
}
$$

Zhang and Peeta (2014) explicitly represent interdependency evolution across short and longer horizons, while Cimellaro et al. (2024) demonstrate the importance of temporal adjacency and event sequence.

Therefore,

$$
\boxed{\mathcal G\rightleftarrows\text{Dynamics}.}
$$

This does not mean every physical edge continuously changes. It means that the **effective coupled structure available for propagation may change with state, mode, damage, recovery, and history**.

---

## 11. Multiscale temporal structure

Different subsystems and mechanisms operate on different characteristic timescales. Coupled P–T literature distinguishes short-, medium-, and long-term processes, while co-simulation frameworks support models with different internal clocks and synchronization requirements (Hardy et al., 2024; Sun et al., 2021).

Define

$$
\boxed{
\boldsymbol\tau_{S3}
=\{\tau_P,\tau_{T_R},\tau_{T_B},\tau_{T_U},\tau_{T_H},\tau_I,\tau_O,
\tau_{\rm travel},\tau_{\rm repair},\tau_C\}.
}
$$

The framework does not impose a universal ordering. Rather,

$$
\boxed{\tau_P,\tau_T,\tau_I,\tau_O\text{ need not be equal}.}
$$

Stage 2 distinguishes

$$
\boxed{\delta_{ij}=\text{delay before the causal effect becomes observable}}
$$

from

$$
\boxed{\tau_{ij}=\text{characteristic time over which that mechanism evolves}.}
$$

Hence,

$$
\boxed{\delta_{ij}\neq\tau_{ij}.}
$$

This distinction is essential for delayed information, charging queues, travel-constrained repair, and organizational mobilization.

---

## 12. Spatial cascade dynamics

Stage 3 asks two distinct questions:

$$
\boxed{\text{Where does disruption propagate?}}
$$

and

$$
\boxed{\text{When does it arrive?}}
$$

For component $j$, define the proposed cascade-arrival time

$$
\boxed{
T_C(j)=\inf\{t>t_0:j\text{ enters a predefined disrupted state}\}.
}
\tag{S3.3}
$$

For propagation mechanisms with a meaningful spatial front, define an evolving cascade radius $r_c(t)$ and

$$
\boxed{v_c(t)=\frac{dr_c(t)}{dt}.}
$$

Zhao et al. (2016) found approximately radial, near-constant-velocity propagation for the specific spatially embedded overload-cascade models they studied. This motivates explicit space–time propagation analysis but **does not establish constant-velocity propagation as a universal infrastructure law**.

Accordingly, the thesis may test

$$
\boxed{v_c=v_c(Y,\mathcal G,m,h),}
\tag{S3.4}
$$

allowing propagation velocity to depend on state, topology, mode, and hazard.

---

## 13. Discrete-event scope

The Stage-3 event set is restricted to events capable of modifying state, topology, capacity, interdependency activation, or recovery chronology:

$$
\boxed{
\mathcal E_{S3}=\{
\text{failure},
\text{trip},
\text{capacity reduction},
\text{road closure},
\text{communication loss},
\text{charging event},
\text{switching},
\text{dispatch event},
\text{crew arrival},
\text{repair},
\text{restoration}
\}.
}
$$

An event produces

$$
\boxed{(Y,m,\mathcal G,a)\rightarrow(Y^+,m^+,\mathcal G^+,a^+).}
$$

**Boundary rule:** a dispatch event may be consumed by Stage 3 as a discrete event, but the decision rule that generates that dispatch belongs to Stage 4.

---

## 14. Uncertainty

Stage 3 admits uncertainty in quantities that materially alter the dynamic trajectory:

$$
\boxed{
\Xi=\{h,\text{failure state},\text{demand},\text{travel time},\text{repair time},\delta_I,A_I\}.
}
$$

Uncertainty is not promoted to a separate framework stage. It is used to test robustness of dynamic conclusions. Scenario generation, Monte Carlo simulation, and sensitivity analysis are appropriate where hazard damage, traffic/accessibility, resource availability, travel, repair, or restoration outcomes are uncertain (Lian et al., 2026; Yang & Zhang, 2026).

---

## 15. Computational architecture

The preferred computational structure is

$$
\boxed{\textbf{hybrid multirate co-simulation}.}
$$

Conceptually,

$$
\boxed{
\begin{array}{ccc}
P&\longleftrightarrow&T\\
\updownarrow&&\updownarrow\\
I&\longleftrightarrow&O
\end{array}
}
$$

operates through a **Hybrid Event and Synchronization Manager**.

HELICS is an established federated co-simulation framework in which heterogeneous models from power, transportation, communications, and other domains can exchange variables at runtime while retaining native representations and clocks (Hardy et al., 2024).

The thesis therefore follows

$$
\boxed{\text{maximum necessary physical fidelity}\neq\text{maximum possible model detail}.}
$$

Electromagnetic-transient power simulation, packet-level communication simulation, microscopic transportation simulation, and detailed behavioral organizational simulation will not all be used simultaneously unless the research question requires those resolutions.

---

## 16. Stage-3 validation and falsification

Stage 3 must validate not only final performance but also the **mechanism through which outcomes are generated**. Validation therefore examines:

- native subsystem behavior;
- dimensional and physical consistency;
- cross-system interface consistency;
- event chronology;
- coupling effects;
- limiting cases;
- parameter and timescale sensitivity;
- uncertainty sensitivity;
- system-level trajectories;
- numerical synchronization / convergence where applicable.

A representative integrated chronology is

$$
\boxed{
t_{\rm failure}
<t_{\rm detected}
<t_{\rm estimated}
<t_{\rm decision}
<t_{\rm mobilisation}
<t_{\rm arrival}
<t_{\rm repair}.
}
\tag{S3.5}
$$

This chronology is a **cross-stage interface chronology**: Stage 3 evolves the physical/information/organizational state and event times, while Stage 4 supplies observer and decision-policy logic where those timestamps depend on estimation or control.

A key falsification technique is **coupling ablation**. For a selected Stage-2 mechanism,

$$
\boxed{\mathcal I^{\alpha\beta}\rightarrow0,}
$$

and the model is rerun under otherwise matched conditions.

Use unambiguous model-variant notation, for example

$$
\mathscr M_{PT},\qquad
\mathscr M_{PTI},\qquad
\mathscr M_{PTIO},
$$

to avoid confusion with the Stage-2 mechanism symbol $M_{ij}$.

If removing a coupling produces no meaningful and reproducible change in state trajectory, event order, cascade arrival, recovery trajectory, or later viability assessment, the explanatory importance of that coupling must be reconsidered rather than assumed.

---

## 17. Boundary of Stage 3

Stage 3 remains bounded so that it does not consume Stages 4–7.

### Stage 3 does not redefine interdependencies

The interdependency object remains

$$
\mathfrak I_{ij}^{\alpha\beta}.
$$

### Stage 3 does not design the observer

$$
\widehat X(t)=\mathcal E(y,I)
$$

belongs to Stage 4.

### Stage 3 does not design the decision/control policy

$$
u(t)=\pi(\widehat X,I,O)
$$

belongs to Stage 4.

### Stage 3 does not compute Stage-5 viability objects

The sustainable viability kernel

$$
\mathcal V_{\rm sus}^{u},
$$

geometric viability margin

$$
\rho_g,
$$

and time to viability loss

$$
T_{\rm exit}
$$

remain Stage-5 quantities.

Therefore,

$$
\boxed{
\text{Stage 3 produces trajectories; Stage 4 observes and controls them; Stage 5 evaluates their viability.}
}
$$

---

## Final frozen Stage-3 scope

| Item | Canonical Stage-3 specification |
|---|---|
| **Stage** | Coupled Hybrid Multiscale Dynamics |
| **Question** | How do the coupled systems evolve over space and time, and how do disruptions propagate? |
| **Four-layer state** | $Y(t)=[x_P,x_T,z_I,z_O]^\top$ |
| **Augmented hybrid state** | $\widetilde Y(t)=(Y(t),m(t))$ |
| **Power** | power-flow/DAE, DER, storage, charging, traction |
| **Transportation** | traffic flow, EV/eBus SOC and queues, train motion |
| **Information** | availability, latency, freshness, information error |
| **Organization** | resources, crews, coordination, mobilization states |
| **Interdependency input** | $\mathfrak I_{ij}^{\alpha\beta}$ |
| **Hybrid structure** | continuous dynamics + algebraic constraints + discrete events + mode switching |
| **Network evolution** | $\mathcal G(t)\rightleftarrows Y(t)$ |
| **Temporal structure** | $\delta_{ij}$ + multiple characteristic timescales |
| **Spatial structure** | $T_C(j),r_c(t),v_c(t)$ where spatial-front interpretation is meaningful |
| **Uncertainty** | hazard, failure, demand, travel, repair, information |
| **Computation** | hybrid multirate co-simulation |
| **Outputs** | $Y(t),m(t),\mathcal G(t)$, event sequence, $T_C(j)$, $v_c(t)$ where applicable, service/recovery trajectories |

The canonical progression is

$$
\boxed{
\underbrace{\{P,T,I,O\}}_{\textbf{Stage 1: what exists}}
\rightarrow
\underbrace{\mathfrak I_{ij}^{\alpha\beta}}_{\textbf{Stage 2: why / through what mechanism}}
\rightarrow
\underbrace{\{Y(t),m(t),\mathcal G(t),T_C,v_c\}}_{\textbf{Stage 3: how effects evolve and propagate}}.
}
$$

The central research opportunity is an explicit **causal–temporal bridge** joining multimodal power–transport dynamics, traction-power interactions, information delay, organizational response, dynamic interdependencies, and disruption propagation. The cited literature establishes these elements individually or in smaller combinations; the thesis must test the value of their joint P–T–I–O representation rather than presume novelty from combination alone.

---

## Evidence-status rule

The literature citations below support specific precedents used in Stage 3. They do **not** by themselves prove that the complete proposed P–T–I–O Stage-3 architecture is novel. Novelty remains a falsifiable evidence question.

Principal bibliographic records and DOIs were cross-checked against publisher, institutional, or indexing records before this scope was frozen on 2026-09-11.

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
