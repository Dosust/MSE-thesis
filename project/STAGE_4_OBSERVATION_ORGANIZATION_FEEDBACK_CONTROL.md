# Stage 4 — Observation, Organization, Feedback and Control

![Stage](https://img.shields.io/badge/Stage%204-FROZEN-1A7F37)

**Framework stage:** Stage 4 — Observation, Organization, Feedback and Control  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Evidence basis:** 10 analytical passes; 31 core studies  
**Change rule:** Do not revise this Stage-4 scientific scope unless explicitly requested and versioned.  
**Framework preservation rule:** This document formalizes Stage 4 only. It does not alter the frozen seven-stage framework or redefine Stages 1–3.

> **Evidence notation:** `[E]` = established literature; `[D]` = derived synthesis; `[P]` = proposed thesis construct.

> **Boundary rule:** Stage 4 observes, infers, interprets, coordinates, and controls the Stage-3 system. It does not redefine Stage-3 dynamics and does not compute Stage-5 viability objects.

> **Rendering rule:** The control variable is always $u$; measurement noise is $\varepsilon$. Long conceptual statements use tables or multiline displays rather than oversized boxed expressions.

---

## Frozen research question

> **How is the system observed, interpreted, coordinated and controlled?**

The scientific progression is

```math
\{P,T,I,O\}
\rightarrow
\mathfrak I_{ij}^{\alpha\beta}
\rightarrow
\{Y(t),\mathcal G(t),m(t),T_C\}
\rightarrow
\{\widehat X,\Sigma_X,b_t,z_I,z_O,\mathcal U,u,\tau_{\rm response}\}.
```

The dynamic information and organizational states inherited from Stage 3 are $z_I(t)$ and $z_O(t)$. In the conceptual feedback spine, $I$ and $O$ denote the corresponding information and organizational functions.

Stage 3 determines how the actual coupled system evolves. Stage 4 addresses a different problem: **the true physical state is not automatically known to the decision maker**. Measurements may be incomplete, asynchronous, noisy, delayed, or unavailable; state must therefore be inferred before an intervention is selected and executed. This distinction is fundamental in power-system state estimation and transportation-network observability research (Castillo et al., 2015; Cheng et al., 2024; Gentili & Mirchandani, 2012).

---

## 1. What the 10 literature passes established

| Pass | Scientific problem | Evidence-supported conclusion |
|---:|---|---|
| **1** | Measurement | Sensors produce partial observations of reality, not the state itself (Cheng et al., 2024; Gentili & Mirchandani, 2012). |
| **2** | Observability | State recoverability depends on measurement placement, topology, prior information, and model structure (Castillo et al., 2015; Cheng et al., 2024). |
| **3** | State estimation | Estimation must accommodate uncertainty, heterogeneous reporting rates, asynchronous data, cyber failures, and changing states (Cheng et al., 2024; Zhou et al., 2024). |
| **4** | Information quality | Delay, packet loss, sampling, and information age can materially alter closed-loop performance (Liu et al., 2017; Mena & Núñez, 2023; Yates et al., 2021; Zhang et al., 2017). |
| **5** | Situation awareness | Measurement and estimation alone do not guarantee correct interpretation; comprehension and anticipation matter to operational decisions (Endsley, 1995; Panteli & Kirschen, 2015). |
| **6** | Organizational decision | Authority, coordination, resources, information sharing, and organizational structure influence feasible response (Li et al., 2019; McAlister et al., 2024; Mohebbi et al., 2020). |
| **7** | Partial observability | Decisions under damaged sensing/communication differ from full-information decisions; POMDP formulations provide one established route (Arcieri et al., 2023; Qiu et al., 2023). |
| **8** | Feedback and control | Communication imperfections and estimation errors must enter the closed loop rather than remain external metadata (Ding et al., 2021; Liu et al., 2017; Zhang et al., 2017). |
| **9** | Multi-actor coordination | Centralized, decentralized, and collaborative decision structures can produce different restoration outcomes (Iloglu et al., 2025; Magoua et al., 2026). |
| **10** | Response versus disruption | Sensing-to-action is timed; effective response depends on whether information, decision, coordination, mobilization, and actuation occur fast enough relative to system evolution (Panteli & Kirschen, 2015; Prostejovsky et al., 2019; Qiu et al., 2023). |

The backbone of Stage 4 is the separation

```math
\begin{aligned}
\text{measurement}
&\neq\text{information}
\neq\text{estimated state}\\
&\neq\text{situation awareness}
\neq\text{decision}
\neq\text{executed action}.
\end{aligned}
```

---

## 2. Core evidence base

The ranking is by direct usefulness for constructing Stage 4, not citation count.

| Rank | Core study | Contribution to Stage 4 |
|---:|---|---|
| **1** | Panteli and Kirschen (2015) | Data/ICT → situation awareness → operator decision making |
| **2** | Cheng et al. (2024) | Power-system measurement, observability, estimation, asynchronous data, uncertainty |
| **3** | Endsley (1995) | Perception → comprehension → projection structure for situation awareness |
| **4** | Zhou et al. (2024) | Dynamic state estimation under cyber-physical uncertainty |
| **5** | Yates et al. (2021) | Information freshness through Age of Information |
| **6** | Prostejovsky et al. (2019) | Human operators and decision support under increasing automation |
| **7** | Ding et al. (2021) | Secure estimation and feedback control under cyber-physical disruption |
| **8** | Liu et al. (2020) | Bidirectional power–communication dependency in monitoring/control |
| **9** | Zhang et al. (2017) | Sampling, delay, packet loss, quantization, communication constraints |
| **10** | Liu et al. (2017) | Delay-induced degradation and compensation in communication-based power control |
| **11** | Mena and Núñez (2023) | Information freshness in networked-control systems |
| **12** | Gentili and Mirchandani (2012) | Traffic-network sensor placement and flow observability |
| **13** | Castillo et al. (2015) | Separation of transportation observation, estimation, and prediction |
| **14** | Owais (2022) | Review of traffic sensor-location and observability research |
| **15** | Li et al. (2019) | Dynamic multilayer interorganizational coordination |
| **16** | Mohebbi et al. (2020) | Cyber-physical-social and organizational infrastructure resilience |
| **17** | Rasoulkhani and Mostafavi (2018) | Human–infrastructure feedback and endogenous human actions |
| **18** | McAlister et al. (2024) | Organizational characteristics, knowledge, finance, communication, decision dynamics |
| **19** | Qiu et al. (2023) | Dec-POMDP/repair-crew decision support in coupled transport–energy infrastructure |
| **20** | Arcieri et al. (2023) | Belief-based infrastructure decision making under uncertain monitoring |
| **21** | Yang et al. (2024) | Multi-agent decision support for infrastructure recovery |
| **22** | Zhu et al. (2024) | Restoration decisions under uncertain switch information |
| **23** | Magoua et al. (2026) | Cross-system collaborative restoration and centralized/decentralized control |
| **24** | Damaschin et al. (2026) | Time-dependent governance/coordination structures in recovery networks |
| **25** | Sun et al. (2024) | Time evolution of organizational collaboration and resource flows |
| **26** | Hardy et al. (2024) | Multi-domain synchronization and closed-loop co-simulation |
| **27** | Shalaby et al. (2025) | Partial-observation resilient control under wildfire uncertainty |
| **28** | Jiang et al. (2026) | Multi-agent coordination of mobile resources across energy/transport networks |
| **29** | Iloglu et al. (2025) | Game-theoretic implications of decentralized infrastructure owners |
| **30** | Bellini et al. (2025) | Situation awareness as a cyber-resilience capability |
| **31** | Jørgensen and Ma (2026) | Digital models, human operators, coordination, and accountability in grid control rooms |

---

## 3. Scientific meaning of Stage 4

The central architecture is a **closed-loop partially observable socio-technical control process**:

```math
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow\widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
```

| Symbol | Meaning |
|---|---|
| $X(t)$ | actual physical $P$–$T$ state |
| $y(t)$ | available measurements |
| $I(t)$ | information function/capability; dynamic state represented by $z_I(t)$ |
| $\widehat X(t)$ | estimated or believed physical state |
| $O(t)$ | organizational interpretation/response function; dynamic state represented by $z_O(t)$ |
| $u(t)$ | executed intervention |

Thus

```math
X\neq y\neq I\neq\widehat X\neq O\neq u.
```

---

## 4. Observation

**Equation S4.1 — Measurement model**

```math
y_k(t)
=
H_k\!\left[X(t-\delta_k)\right]
+\varepsilon_k(t).
```

Here $H_k$ is the measurement function, $\delta_k$ is measurement/communication delay, and $\varepsilon_k$ is measurement error. This is consistent with state-estimation frameworks in which states are inferred from SCADA, PMU, AMI, and related measurements rather than directly observed (Cheng et al., 2024; Zhou et al., 2024).

Representative measurements include

```math
y_P=\{V,P_{ij},Q_{ij},P_{\rm inj},f,SOC,P_{\rm traction},P_{\rm charge}\},
```

and

```math
y_T=\{q,k,v,TT,\text{vehicle position},SOC_{EV},\text{bus position},\text{train position/speed}\}.
```

Traffic-observability research shows that sensor placement determines which flows can be reconstructed directly and which require assumptions, prior information, or estimation (Castillo et al., 2015; Gentili & Mirchandani, 2012; Owais, 2022).

---

## 5. Observability

For a local linear representation,

```math
x_{k+1}=Ax_k,
\qquad
y_k=Cx_k.
```

**Equation S4.2 — Classical local observability benchmark**

```math
\operatorname{rank}
\begin{bmatrix}
C\\CA\\CA^2\\\vdots\\CA^{n-1}
\end{bmatrix}
=n.
```

This is only a local/classical benchmark because the Stage-3 system is nonlinear, hybrid, delayed, and multilayer.

A more general condition is

```math
X_1\neq X_2
\quad\Rightarrow\quad
\mathcal H_{\rm obs}(X_1)\neq\mathcal H_{\rm obs}(X_2)
```

over the relevant observation horizon. Power-system observability depends on measurement availability, sensor type, topology, and measurement configuration; transportation has an analogous flow-observability problem (Cheng et al., 2024; Gentili & Mirchandani, 2012).

---

## 6. Information and state estimation

**Equation S4.3 — State estimate**

```math
\widehat X(t)
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
```

**Equation S4.4 — Estimate with uncertainty**

```math
\left(\widehat X(t),\Sigma_X(t)\right)
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
```

Modern state-estimation literature treats measurement uncertainty, asynchronous reporting rates, correlated data sources, missing measurements, and cyber-security issues (Cheng et al., 2024; Zhou et al., 2024).

The canonical information state remains

```math
z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top.
```

Stage 3 evolves $z_I$; Stage 4 uses the current $z_I$ to infer physical state.

---

## 7. Information freshness

**Equation S4.5 — Age of Information**

```math
\Delta_I(t)=t-U(t),
```

where $U(t)$ is the generation time of the freshest received update (Yates et al., 2021).

Networked-control research shows that sampling, delay, packet loss, communication constraints, and variable transmission behavior can degrade closed-loop performance (Liu et al., 2017; Zhang et al., 2017).

Therefore,

```math
\text{available information}\not\Rightarrow\text{timely information},
```

and

```math
\text{timely information}\not\Rightarrow\text{accurate state estimate}.
```

---

## 8. Partial observability and belief state

During disruption, $\widehat X(t)\neq X(t)$ may be central rather than exceptional. Qiu et al. (2023) formulate repair-crew dispatch under partial observation, while Arcieri et al. (2023) combine uncertain observations and sequential infrastructure decisions.

**Equation S4.6 — Belief state**

```math
b_t(x)
=
p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right).
```

Stage 4 can therefore reason from $\widehat X$ or, when needed, $b_t$. POMDP is a candidate decision formalism, not the definition of Stage 4.

---

## 9. Situation awareness and interpretation

Endsley (1995) conceptualizes situation awareness as

```math
\text{perception}\rightarrow\text{comprehension}\rightarrow\text{projection}.
```

Panteli and Kirschen (2015) apply situation-awareness reasoning to electric-power operation and show how incomplete or incorrect awareness can impair decisions during disturbances.

Situation awareness is not a fifth layer. It is a functional bridge:

```math
I\rightarrow\widehat X\rightarrow\text{situation awareness}\rightarrow O.
```

**Equation S4.7 — Proposed situation representation [P]**

```math
\mathcal A_{\rm SA}(t)
=
\mathscr A\!\left[\widehat X(t),\Sigma_X(t),m(t),\mathcal G(t)\right].
```

$\mathcal A_{\rm SA}$ is a Stage-4 processing construct, not an infrastructure layer.

---

## 10. Organization

The canonical organizational state remains

```math
z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^O,\tau_M]^\top.
```

Organizational-resilience literature supports retaining authority, coordination, knowledge sharing, resources, and interorganizational structure because they affect infrastructure decision making and recovery (Li et al., 2019; McAlister et al., 2024; Mohebbi et al., 2020).

**Equation S4.8 — Available action set**

```math
\mathcal U_{\rm available}(t)
=
\mathcal U\!\left(z_I(t),z_O(t)\right).
```

Thus

```math
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
```

A technically desirable action may remain organizationally infeasible because authorization, coordination, resources, workforce, or mobilization are unavailable (Damaschin et al., 2026; Li et al., 2019; Magoua et al., 2026).

---

## 11. Decision and control

**Equation S4.9 — Generic Stage-4 policy**

```math
u(t)
=
\pi\!\left[\widehat X(t),z_I(t),z_O(t)\right],
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
```

The policy symbol $\pi$ denotes the decision/control mapping. Stage 4 does not freeze MPC, reinforcement learning, dynamic programming, MILP, game theory, or another solver (Iloglu et al., 2025; Magoua et al., 2026; Qiu et al., 2023; Yang et al., 2024; Zhu et al., 2024).

---

## 12. Feedback closure

The controller acts on inferred state, not necessarily true state:

```math
X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X.
```

The executed intervention returns to Stage-3 dynamics:

```math
u(t)\rightarrow F^{m(t)}\rightarrow Y(t+\Delta t).
```

Networked-control theory explicitly treats measurement, communication, and actuation as parts of a closed feedback system and shows that communication imperfections can affect performance and stability (Liu et al., 2017; Zhang et al., 2017).

---

## 13. Control-action families

**Equation S4.10 — Action vector**

```math
u(t)=
\begin{bmatrix}
u_P(t)\\
u_T(t)\\
u_I(t)\\
u_O(t)
\end{bmatrix}.
```

| Action family | Examples |
|---|---|
| $u_P$ | switching, DER/storage dispatch, charging limitation, load restoration, traction-power reconfiguration |
| $u_T$ | traffic control, rerouting, bus dispatch, rail scheduling, road opening/closure |
| $u_I$ | measurement prioritization, communication routing, sampling/update priority, information-sharing activation |
| $u_O$ | crew assignment, resource allocation, mobilization, cross-agency coordination, restoration priority |

Collaborative restoration and mobile-resource studies show that outcome depends not only on physical action but also on how resources and decisions are coordinated (Jiang et al., 2026; Magoua et al., 2026; Qiu et al., 2023).

---

## 14. Response time

The response pathway is

```math
\text{sense}\rightarrow\text{communicate}\rightarrow\text{estimate}
\rightarrow\text{decide}\rightarrow\text{coordinate}\rightarrow\text{mobilize}\rightarrow\text{act}.
```

**Equation S4.11 — Sequential response-time decomposition [D]**

```math
\begin{aligned}
\tau_{\rm response}={}&
\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
```

If processes overlap or execute in parallel, $\tau_{\rm response}$ is the completion time of the relevant critical path rather than the arithmetic sum of all durations. This is a derived synthesis [D] of established process delays, not a metric attributed to one source (Liu et al., 2017; Panteli & Kirschen, 2015; Qiu et al., 2023).

Stage 3 provides a competing disruption clock, $\tau_{\rm cascade}$ or component-specific $T_C(j)$.

> **Engineering question:** Can the system know, decide, coordinate, and act before disruption reaches the target?

---

## 15. Proposed response-to-cascade diagnostic [P]

**Equation S4.12 — Timing diagnostic**

```math
\Pi_R
=
\frac{\tau_{\rm response}}{\tau_{\rm cascade}}.
```

| Regime | Interpretation |
|---|---|
| $\Pi_R<1$ | nominal response completes faster than the characteristic cascade process |
| $\Pi_R\approx1$ | strong temporal competition |
| $\Pi_R>1$ | nominal response is slower |

However,

```math
\Pi_R<1\not\Rightarrow\text{successful control}.
```

Successful intervention also requires observability, estimation accuracy, authority, resources, accessibility, controllability, and appropriate action.

---

## 16. Partial-information control comparison [P]

| Model variant | Assumption |
|---|---|
| $\mathscr M_0$ | perfect observation + instantaneous organization |
| $\mathscr M_1$ | imperfect/delayed information |
| $\mathscr M_2$ | imperfect information + organizational constraints |
| $\mathscr M_3$ | full closed-loop P–T–I–O system |

The symbols $\mathscr M_k$ denote model variants and are intentionally distinct from the Stage-2 mechanism symbol $M_{ij}$. The design is grounded in literature showing separately that imperfect information changes estimation/control and organizational coordination changes restoration outcomes (Arcieri et al., 2023; Cheng et al., 2024; Magoua et al., 2026; Qiu et al., 2023).

The intended contrasts are

```math
\mathscr M_1-\mathscr M_0=\text{information effect},
```

```math
\mathscr M_2-\mathscr M_1=\text{organizational effect},
```

and

```math
\mathscr M_3-\mathscr M_0=\text{full coupled-response effect}.
```

---

## 17. Stage-4 validation

Stage 4 is validated across the entire inference-to-action chain:

```math
\text{measurement}\rightarrow\text{estimation}\rightarrow\text{decision}
\rightarrow\text{action}\rightarrow\text{closed-loop consequence}.
```

| Validation family | Representative quantities/checks |
|---|---|
| Observation | sensor coverage, observability |
| Estimation | $RMSE(\widehat X,X)$, $\Sigma_X$, state-classification accuracy |
| Information | $\delta_I$, $\Delta_I$, $p_{\rm loss}$, $A_I$ |
| Organization | $\tau_{\rm decision}$, $\tau_{\rm coord}$, $\tau_{\rm mobilization}$, crew/resource availability |
| Control | verify $u(t)\in\mathcal U(z_I,z_O)$ rather than assume it |
| Closed loop | trajectory, service, timing, and recovery consequences |

---

## 18. Boundary with Stage 3

| Stage | Responsibility |
|---|---|
| **3** | determine how $z_I(t)$ and $z_O(t)$ evolve |
| **4** | determine how current $z_I(t)$ and $z_O(t)$ constrain knowledge and feasible intervention |

For example,

```math
\text{Stage 3: }A_I(t)\downarrow,\ \delta_I(t)\uparrow,
```

while

```math
\text{Stage 4: }(A_I,\delta_I)\rightarrow y\rightarrow\widehat X\rightarrow u.
```

---

## 19. Boundary with Stage 5

Stage 4 ends at **controlled response**. It does not compute the Stage-5 objects

```math
K_{\rm sus},
\qquad
\mathcal V_{\rm sus}^{u,T},
\qquad
\rho_E,\rho_g,
\qquad
T_{\mathcal V},T_K.
```

The cross-stage interface is

```math
u(t)
\longrightarrow
Y^u(t)
\longrightarrow
\{K_{\rm sus},\mathcal V_{\rm sus}^{u,T},\partial\mathcal V,T_{\mathcal V},T_K\}.
```

| Stage | Output/question |
|---|---|
| **3** | generates the evolving system trajectory |
| **4** | closes the observation–decision–control loop and produces feasible $u(t)$ and controlled trajectory $Y^u(t)$ |
| **5** | tests acceptability, maintainability, and proximity to loss |

---

## 20. Research gap supported by the reviewed corpus

The sampled literature is mature in separate areas including power state estimation, traffic observability, networked control, information freshness, situation awareness, organizational coordination, repair-resource optimization, and POMDP/MARL restoration.

The sampled work does not reveal a mature standard framework carrying the entire chain

```math
X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X
```

across a physically explicit power–multimodal-transportation system while simultaneously retaining information degradation, organizational feasibility, cross-layer interdependencies, and a cascade clock. This is a synthesis from the reviewed corpus, not a claim that no such study could exist (Cheng et al., 2024; Li et al., 2019; Mohebbi et al., 2020; Qiu et al., 2023).

> **Defensible niche:** Response is not only a control problem; it is a partial-observation + information + organization + actuation problem.

---

## Final frozen Stage-4 scope

| Item | Canonical specification |
|---|---|
| **Stage** | Observation, Organization, Feedback and Control |
| **Physical reality** | $X(t)=[x_P(t),x_T(t)]^\top$ |
| **Measurement** | $y(t)=H[X(t-\delta)]+\varepsilon(t)$ |
| **Information state** | $z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top$ |
| **State estimate** | $(\widehat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I)$ |
| **Partial observability** | $b_t(X)=p(X_t\mid y_{[0,t]},u_{[0,t)})$ |
| **Organization state** | $z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^O,\tau_M]^\top$ |
| **Feasible actions** | $u(t)\in\mathcal U(z_I(t),z_O(t))$ |
| **Control policy** | $u(t)=\pi[\widehat X(t),z_I(t),z_O(t)]$ |
| **Feedback** | $X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X$ |
| **Temporal response** | sequential sum or corresponding critical path when processes overlap |
| **Stage-3 timing interface** | compare $\tau_{\rm response}$ with $\tau_{\rm cascade}$ or $T_C(j)$ |
| **Primary outputs** | $\widehat X$, $\Sigma_X$, $b_t$, $\mathcal U$, $u$, $\tau_{\rm response}$, $Y^u$ |

> **STAGE 4 SCIENTIFIC SCOPE: FROZEN**

The ratio $\Pi_R$ remains a proposed thesis diagnostic [P], not an established resilience law.

---

## References

Arcieri, G., Hoelzl, C., Schwery, O., Straub, D., Papakonstantinou, K. G., & Chatzi, E. (2023). Bridging POMDPs and Bayesian decision making for robust maintenance planning under model uncertainty: An application to railway systems. *Reliability Engineering & System Safety, 239*, 109496. https://doi.org/10.1016/j.ress.2023.109496

Bellini, E., D’Aniello, G., Flammini, F., & Gaeta, R. (2025). Situation awareness for cyber resilience: A review. *International Journal of Critical Infrastructure Protection, 49*, 100755. https://doi.org/10.1016/j.ijcip.2025.100755

Castillo, E., Grande, Z., Calviño, A., Szeto, W. Y., & Lo, H. K. (2015). A state-of-the-art review of the sensor location, flow observability, estimation, and prediction problems in traffic networks. *Journal of Sensors, 2015*, 903563. https://doi.org/10.1155/2015/903563

Cheng, G., Lin, Y., Abur, A., Gómez-Expósito, A., & Wu, W. (2024). A survey of power system state estimation using multiple data sources: PMUs, SCADA, AMI, and beyond. *IEEE Transactions on Smart Grid, 15*(1), 1129–1151. https://doi.org/10.1109/TSG.2023.3286401

Damaschin, L., Giardini, F., & Wittek, R. (2026). Structure, time and effectiveness: An integrative review for resilient interorganizational networks in post-disaster recovery. *Progress in Disaster Science, 30*, 100607. https://doi.org/10.1016/j.pdisas.2026.100607

Ding, D., Han, Q.-L., Ge, X., & Wang, J. (2021). Secure state estimation and control of cyber-physical systems: A survey. *IEEE Transactions on Systems, Man, and Cybernetics: Systems, 51*(1), 176–190. https://doi.org/10.1109/TSMC.2020.3041121

Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32–64. https://doi.org/10.1518/001872095779049543

Gentili, M., & Mirchandani, P. B. (2012). Locating sensors on traffic networks: Models, challenges and research opportunities. *Transportation Research Part C: Emerging Technologies, 24*, 227–255. https://doi.org/10.1016/j.trc.2012.01.004

Hardy, T. D., Palmintier, B., Top, P., Krishnamurthy, D., & Fuller, J. C. (2024). HELICS: A co-simulation framework for scalable multi-domain modeling and analysis. *IEEE Access, 12*, 24325–24347. https://doi.org/10.1109/ACCESS.2024.3363615

Iloglu, S., Albert, L. A., & Michini, C. (2025). Facility location and restoration games. *Computers & Operations Research, 174*, 106896. https://doi.org/10.1016/j.cor.2024.106896

Jiang, C., Zhou, L., Xu, H., Lin, J., Shao, Z., Zhou, Y., & Lin, Z. (2026). Coupled energy-transportation network resilience improvement strategy considering dynamic traffic flow distribution: Multi-type mobile emergency resources collaborative scheduling. *Applied Energy, 408*, 127367. https://doi.org/10.1016/j.apenergy.2026.127367

Jørgensen, B. N., & Ma, Z. G. (2026). Infostructure: A scoping review and reference architectural framework for situation awareness in future power system control rooms. *Energies, 19*(6), 1472. https://doi.org/10.3390/en19061472

Li, Q., Dong, S., & Mostafavi, A. (2019). Modeling of inter-organizational coordination dynamics in resilience planning of infrastructure systems: A multilayer network simulation framework. *PLOS ONE, 14*(11), e0224522. https://doi.org/10.1371/journal.pone.0224522

Liu, S., Liu, P. X., & Wang, X. (2017). Stability analysis and compensation of network-induced delays in communication-based power system control: A survey. *ISA Transactions, 66*, 143–153. https://doi.org/10.1016/j.isatra.2016.09.022

Liu, X., Chen, B., Chen, C., & Jin, D. (2020). Electric power grid resilience with interdependencies between power and communication networks—A review. *IET Smart Grid, 3*, 182–193. https://doi.org/10.1049/iet-stg.2019.0202

Magoua, J. J., Huang, J., Kwak, Y. H., & Li, N. (2026). Collaborative decision making for natural disaster recovery of interdependent infrastructure systems. *Reliability Engineering & System Safety, 272*, 112472. https://doi.org/10.1016/j.ress.2026.112472

McAlister, M. M., Murali, P. S., Zhang, Q., Wells, E. C., & Mohebbi, S. (2024). Improving and quantifying organizational resilience for sustainable management of critical infrastructures: A multi-level system dynamics approach. *International Journal of Disaster Risk Reduction, 115*, 105079. https://doi.org/10.1016/j.ijdrr.2024.105079

Mena, J. P., & Núñez, F. (2023). Age of information in IoT-based networked control systems: A MAC perspective. *Automatica, 147*, 110652. https://doi.org/10.1016/j.automatica.2022.110652

Mohebbi, S., Zhang, Q., Wells, E. C., Zhao, T., Nguyen, H., Li, M., Abdel-Mottaleb, N., Uddin, S., Lu, Q., Wakhungu, M. J., Wu, Z., Zhang, Y., Tuladhar, A., & Ou, X. (2020). Cyber-physical-social interdependencies and organizational resilience: A review of water, transportation, and cyber infrastructure systems and processes. *Sustainable Cities and Society, 62*, 102327. https://doi.org/10.1016/j.scs.2020.102327

Owais, M. (2022). Traffic sensor location problem: Three decades of research. *Expert Systems with Applications, 208*, 118134. https://doi.org/10.1016/j.eswa.2022.118134

Panteli, M., & Kirschen, D. S. (2015). Situation awareness in power systems: Theory, challenges and applications. *Electric Power Systems Research, 122*, 140–151. https://doi.org/10.1016/j.epsr.2015.01.008

Prostejovsky, A. M., Brosinsky, C., Heussen, K., Westermann, D., Kreusel, J., & Marinelli, M. (2019). The future role of human operators in highly automated electric power systems. *Electric Power Systems Research, 175*, 105883. https://doi.org/10.1016/j.epsr.2019.105883

Qiu, D., Wang, Y., Zhang, T., Sun, M., & Strbac, G. (2023). Hierarchical multi-agent reinforcement learning for repair crews dispatch control towards multi-energy microgrid resilience. *Applied Energy, 336*, 120826. https://doi.org/10.1016/j.apenergy.2023.120826

Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674

Shalaby, A. A., Abdeltawab, H., & Mohamed, Y. A.-R. I. (2025). Safe deep reinforcement learning for resilient self-proactive distribution grids against wildfires. *IEEE Transactions on Smart Grid, 16*(6), 5065–5082. https://doi.org/10.1109/TSG.2025.3602849

Sun, F., Li, H., Cai, J., Hu, S., & Xing, H. (2024). Examining organizational collaboration and resource flows of disaster response system based on a time-dynamic perspective. *International Journal of Disaster Risk Reduction, 108*, 104565. https://doi.org/10.1016/j.ijdrr.2024.104565

Yang, S., Zhang, Y., Lu, X., Guo, W., & Miao, H. (2024). Multi-agent deep reinforcement learning based decision support model for resilient community post-hazard recovery. *Reliability Engineering & System Safety, 242*, 109754. https://doi.org/10.1016/j.ress.2023.109754

Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. (2021). Age of information: An introduction and survey. *IEEE Journal on Selected Areas in Communications, 39*(5), 1183–1210. https://doi.org/10.1109/JSAC.2021.3065072

Zhang, D., Shi, P., Wang, Q.-G., & Yu, L. (2017). Analysis and synthesis of networked control systems: A survey of recent advances and challenges. *ISA Transactions, 66*, 376–392. https://doi.org/10.1016/j.isatra.2016.09.026

Zhou, Z., Zhang, X., Zhang, J., & Taylor, G. (2024). Comprehensive review on dynamic state estimation techniques with cybersecurity applications. *IET Smart Grid, 7*(4), 370–385. https://doi.org/10.1049/stg2.12168

Zhu, H., Xie, H., Tang, L., Fu, W., & Gao, J. (2024). Robust post-disaster repair crew dispatch for distribution systems considering the uncertainty of switches. *International Journal of Electrical Power & Energy Systems, 155*, 109550. https://doi.org/10.1016/j.ijepes.2023.109550
