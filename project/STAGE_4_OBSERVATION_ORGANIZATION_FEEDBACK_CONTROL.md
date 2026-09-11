# Stage 4 — Observation, Organization, Feedback and Control

**Framework stage:** Stage 4 — Observation, Organization, Feedback and Control  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Evidence basis:** 10 analytical passes; 31 core studies  
**Change rule:** Do not revise this Stage-4 scientific scope unless explicitly requested and versioned.  
**Framework preservation rule:** This document formalizes Stage 4 only. It does **not** alter the frozen seven-stage framework or redefine Stages 1–3.

> **Evidence notation:** `[E]` = established literature; `[D]` = derived synthesis; `[P]` = proposed thesis construct.

> **Boundary rule:** Stage 4 observes, infers, interprets, coordinates, and controls the Stage-3 system. It does not redefine Stage-3 dynamics and does not compute Stage-5 viability objects.

> **Rendering rule:** Mathematical notation is written with GitHub-compatible display blocks. Long conceptual statements are presented as tables or multiline equations rather than oversized boxed expressions. The control variable is always $u$; measurement noise is written as $\varepsilon$ to prevent visual confusion.

---

## Frozen research question

> **How is the system observed, interpreted, coordinated and controlled?**

The scientific progression is:

| Stage | Scientific role |
|---|---|
| **1** | Define the system and its layers. |
| **2** | Identify causal interdependency mechanisms. |
| **3** | Evolve those mechanisms through space and time. |
| **4** | Observe, infer, coordinate, and control the evolving system. |

In compact form,

$$
\{P,T,I,O\}
\rightarrow
\mathfrak I_{ij}^{\alpha\beta}
\rightarrow
\{Y(t),\mathcal G(t),m(t),T_C\}
\rightarrow
\{\widehat X,z_I,z_O,u,\tau_{\rm response}\}.
$$

### Notation bridge

The dynamic information and organizational states inherited from Stage 3 are $z_I(t)$ and $z_O(t)$. In the conceptual spine, $I$ and $O$ denote the corresponding information and organizational functions. Stage-4 mathematical operators use $z_I$ and $z_O$ explicitly.

Stage 3 determines how the actual coupled system evolves. Stage 4 addresses a different problem: **the true physical state is not automatically known to the decision maker**. Measurements may be incomplete, asynchronous, noisy, delayed, or unavailable; the state must therefore be inferred before an intervention is selected and executed. This distinction is fundamental in power-system state estimation and transportation-network observability research (Castillo et al., 2015; Cheng et al., 2024; Gentili & Mirchandani, 2012).

---

## 1. What the 10 literature passes established

| Pass | Scientific problem | Main evidence-supported conclusion |
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
| **10** | Response versus disruption | Sensing-to-action is a timed process; effective response depends on whether information, decision, coordination, mobilization, and actuation occur fast enough relative to system evolution (Panteli & Kirschen, 2015; Prostejovsky et al., 2019; Qiu et al., 2023). |

The repeated result is:

$$
\begin{aligned}
\text{measurement}
&\neq \text{information}
\neq \text{estimated state}\\
&\neq \text{situation awareness}
\neq \text{decision}
\neq \text{executed action}.
\end{aligned}
$$

This distinction is the backbone of Stage 4.

---

## 2. Core evidence base

The following ranking is by direct usefulness for constructing Stage 4, not citation count.

| Rank | Core study | Contribution to Stage 4 |
|---:|---|---|
| **1** | Panteli and Kirschen (2015) | Data/ICT → situation awareness → operator decision making. |
| **2** | Cheng et al. (2024) | Power-system measurement, observability, estimation, asynchronous data, and uncertainty. |
| **3** | Endsley (1995) | Perception → comprehension → projection structure for situation awareness. |
| **4** | Zhou et al. (2024) | Dynamic state estimation under cyber-physical uncertainty. |
| **5** | Yates et al. (2021) | Information freshness through Age of Information. |
| **6** | Prostejovsky et al. (2019) | Human operators and decision-support systems under increasing automation. |
| **7** | Ding et al. (2021) | Secure estimation and feedback control under cyber-physical disruption. |
| **8** | Liu et al. (2020) | Bidirectional power–communication dependency in monitoring and control. |
| **9** | Zhang et al. (2017) | Sampling, delay, packet loss, quantization, and communication constraints in networked control. |
| **10** | Liu et al. (2017) | Delay-induced degradation and compensation in communication-based power control. |
| **11** | Mena and Núñez (2023) | Information freshness linked to networked-control systems. |
| **12** | Gentili and Mirchandani (2012) | Traffic-network sensor placement and flow observability. |
| **13** | Castillo et al. (2015) | Separation of transportation observation, estimation, and prediction. |
| **14** | Owais (2022) | Review of traffic sensor-location and observability research. |
| **15** | Li et al. (2019) | Dynamic multilayer representation of interorganizational coordination. |
| **16** | Mohebbi et al. (2020) | Cyber-physical-social and organizational infrastructure resilience. |
| **17** | Rasoulkhani and Mostafavi (2018) | Human–infrastructure feedback and endogenous human actions. |
| **18** | McAlister et al. (2024) | Organizational characteristics, communication, knowledge, finance, and decision dynamics. |
| **19** | Qiu et al. (2023) | Dec-POMDP formulation of crew decisions in coupled transport–energy infrastructure. |
| **20** | Arcieri et al. (2023) | Belief-based infrastructure decision making with uncertain monitoring information. |
| **21** | Yang et al. (2024) | Multi-agent decision support for interdependent infrastructure recovery. |
| **22** | Zhu et al. (2024) | Restoration decisions with uncertain remote-switch information. |
| **23** | Magoua et al. (2026) | Cross-system collaborative restoration and centralized/decentralized control limits. |
| **24** | Damaschin et al. (2026) | Time-dependent governance and coordination structures in recovery networks. |
| **25** | Sun et al. (2024) | Time evolution of organizational collaboration and resource flows. |
| **26** | Hardy et al. (2024) | Multi-domain synchronization and closed-loop co-simulation. |
| **27** | Shalaby et al. (2025) | Partial-observation resilient control under wildfire uncertainty. |
| **28** | Jiang et al. (2026) | Multi-agent coordination of mobile resources across coupled energy and transport networks. |
| **29** | Iloglu et al. (2025) | Game-theoretic implications of decentralized infrastructure owners during restoration. |
| **30** | Bellini et al. (2025) | Situation awareness as a cyber-resilience capability. |
| **31** | Jørgensen and Ma (2026) | Integration of digital models, human operators, coordination, and accountability in future grid control rooms. |

---

## 3. Scientific meaning of Stage 4

The central architecture is a **closed-loop partially observable socio-technical control process**:

$$
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow \widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t).
$$

| Symbol | Meaning |
|---|---|
| $X(t)$ | Actual physical $P$–$T$ state. |
| $y(t)$ | Available measurements. |
| $I(t)$ | Information capability/function; dynamic state represented by $z_I(t)$. |
| $\widehat X(t)$ | Estimated or believed physical state. |
| $O(t)$ | Organizational interpretation/response function; dynamic state represented by $z_O(t)$. |
| $u(t)$ | Executed intervention. |

Therefore,

$$
X\neq y\neq I\neq\widehat X\neq O\neq u.
$$

---

## 4. Observation

The first Stage-4 process is

$$
X(t)\longrightarrow y(t).
$$

**Equation S4.1 — Measurement model**

$$
y_k(t)=H_k\!\left[X(t-\delta_k)\right]+\varepsilon_k(t).
$$

Here $H_k$ is the measurement function, $\delta_k$ is measurement/communication delay, and $\varepsilon_k$ is measurement error. Using $\varepsilon$ for measurement noise keeps the intervention symbol $u$ visually unambiguous.

This form is consistent with state-estimation frameworks in which system states are inferred from SCADA, PMU, AMI, and related measurements rather than directly observed (Cheng et al., 2024; Zhou et al., 2024).

Representative measurements include

$$
y_P=\{V,P_{ij},Q_{ij},P_{\rm inj},f,SOC,P_{\rm traction},P_{\rm charge}\},
$$

and

$$
y_T=\{q,k,v,TT,\text{vehicle position},SOC_{EV},\text{bus position},\text{train position/speed}\}.
$$

Traffic-observability research shows that sensor placement determines which flows can be directly reconstructed and which require assumptions, prior information, or estimation (Castillo et al., 2015; Gentili & Mirchandani, 2012; Owais, 2022).

---

## 5. Observability

The critical question is whether available observations contain enough information to distinguish relevant states.

For a local linear representation,

$$
x_{k+1}=Ax_k,\qquad y_k=Cx_k.
$$

**Equation S4.2 — Classical local observability benchmark**

$$
\operatorname{rank}
\begin{bmatrix}
C\\CA\\CA^2\\\vdots\\CA^{n-1}
\end{bmatrix}
=n.
$$

This is only a local/classical benchmark because the Stage-3 system is nonlinear, hybrid, delayed, and multilayer.

A more general Stage-4 condition is

$$
X_1\neq X_2
\quad\Rightarrow\quad
\mathcal H_{\rm obs}(X_1)\neq\mathcal H_{\rm obs}(X_2)
$$

over the relevant observation horizon.

Power-system state-estimation research shows that observability depends on measurement availability, sensor type, topology, and measurement configuration; transportation research has an analogous flow-observability problem (Cheng et al., 2024; Gentili & Mirchandani, 2012).

---

## 6. Information and state estimation

Observation produces $y$, but the system requires an estimate.

**Equation S4.3 — State estimator**

$$
\widehat X(t)=\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
$$

**Equation S4.4 — State estimate with uncertainty**

$$
\left(\widehat X(t),\Sigma_X(t)\right)
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
$$

Modern state-estimation literature explicitly treats measurement uncertainty, asynchronous reporting rates, correlated data sources, missing measurements, and cyber-security issues (Cheng et al., 2024; Zhou et al., 2024).

The information state inherited from Stages 1–3 remains

$$
z_I=
[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top.
$$

Stage 4 uses these variables to determine what can be inferred; it does not redefine their dynamics:

$$
\dot z_I\ \text{belongs to Stage 3},
\qquad
\widehat X=\mathcal E(y,z_I)\ \text{belongs to Stage 4}.
$$

---

## 7. Information freshness

For dynamic resilience, information can be available yet stale.

**Equation S4.5 — Age of Information**

$$
\Delta_I(t)=t-U(t),
$$

where $U(t)$ is the generation time of the freshest received update (Yates et al., 2021).

Networked-control research shows that sampling, delay, packet loss, communication constraints, and variable transmission behavior can degrade closed-loop performance (Liu et al., 2017; Zhang et al., 2017).

Thus,

$$
\text{available information}\not\Rightarrow\text{timely information},
$$

and

$$
\text{timely information}\not\Rightarrow\text{accurate state estimate}.
$$

---

## 8. Partial observability and belief state

During disruption,

$$
\widehat X(t)\neq X(t)
$$

may be central rather than exceptional.

Qiu et al. (2023) formulate coupled transport–energy repair-crew dispatch as a decentralized partially observable Markov decision process, while Arcieri et al. (2023) combine uncertain observations and sequential infrastructure decisions.

**Equation S4.6 — Belief state**

$$
b_t(x)
=
p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right).
$$

Stage 4 can therefore reason from $\widehat X$ or, when needed, the belief state $b_t$. POMDP is a candidate decision formalism, not the definition of Stage 4 itself.

---

## 9. Situation awareness and interpretation

State estimation and situation awareness are not identical. Endsley (1995) conceptualizes situation awareness through

$$
\text{perception}\rightarrow\text{comprehension}\rightarrow\text{projection}.
$$

Panteli and Kirschen (2015) transfer situation-awareness reasoning to electric-power operation and show why incomplete or incorrect awareness can impair operational decisions during disturbances.

Situation awareness does **not** become a fifth infrastructure layer. It is a functional bridge:

$$
I\rightarrow\widehat X\rightarrow\text{situation awareness}\rightarrow O.
$$

**Equation S4.7 — Proposed situation representation [P]**

$$
\mathcal A_{\rm SA}(t)
=
\mathscr A\!\left[\widehat X(t),\Sigma_X(t),m(t),\mathcal G(t)\right].
$$

$\mathcal A_{\rm SA}$ is a Stage-4 processing construct, not a new infrastructure layer.

---

## 10. Organization

Stage 1 defines the organizational layer; Stage 3 determines how organizational states evolve. Stage 4 asks:

> **Given available knowledge, who can decide, coordinate, authorize, resource, and execute action?**

Organizational-resilience literature supports retaining authority, coordination, knowledge sharing, resources, and interorganizational structure because these affect infrastructure decision making and recovery effectiveness (Li et al., 2019; McAlister et al., 2024; Mohebbi et al., 2020).

The organizational state remains

$$
z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^O,\tau_M]^\top.
$$

**Equation S4.8 — Available action set**

$$
\mathcal U_{\rm available}(t)
=
\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

Hence,

$$
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

A technically desirable action may remain organizationally infeasible because authorization, coordination, resources, workforce, or mobilization are unavailable. Dynamic organizational-network and collaborative restoration studies provide evidence that organizational configuration changes achievable recovery outcomes (Damaschin et al., 2026; Li et al., 2019; Magoua et al., 2026).

Therefore,

$$
\text{technically desirable action}
\not\Rightarrow
\text{organizationally executable action}.
$$

---

## 11. Decision and control

**Equation S4.9 — Generic Stage-4 policy**

$$
u(t)
=
\pi\!\left[\widehat X(t),z_I(t),z_O(t)\right],
\qquad
u(t)\in\mathcal U(z_I,z_O).
$$

The thesis does **not** freeze Stage 4 to MPC, reinforcement learning, dynamic programming, MILP, game theory, or another solver. Different studies use robust optimization, POMDP/MARL, multi-agent reinforcement learning, cooperative game theory, and non-cooperative game theory for different infrastructure decision problems (Iloglu et al., 2025; Magoua et al., 2026; Qiu et al., 2023; Yang et al., 2024; Zhu et al., 2024).

The policy symbol $\pi$ denotes the decision/control mapping; the algorithm used to compute $\pi$ remains a later methodological choice.

---

## 12. Feedback closure

Stage 4 closes the loop:

$$
X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X.
$$

The controller acts on the inferred state $\widehat X$, not necessarily on the true state $X$. The implemented intervention returns to Stage-3 dynamics:

$$
u(t)\rightarrow F^{m(t)}\rightarrow Y(t+\Delta t).
$$

Networked-control theory explicitly treats measurement, communication, and actuation as parts of a closed feedback system and shows that communication imperfections can affect control-system performance and stability (Liu et al., 2017; Zhang et al., 2017).

---

## 13. Control actions in the P–T–I–O system

**Equation S4.10 — Action vector**

$$
u(t)=
\begin{bmatrix}
u_P(t)\\
u_T(t)\\
u_I(t)\\
u_O(t)
\end{bmatrix}.
$$

| Action family | Examples |
|---|---|
| $u_P$ | switching, DER dispatch, storage dispatch, charging limitation, load restoration, traction-power reconfiguration |
| $u_T$ | traffic control, rerouting, bus dispatch, rail scheduling, road opening/closure |
| $u_I$ | measurement prioritization, communication routing, sampling/update priority, information-sharing activation |
| $u_O$ | crew assignment, resource allocation, mobilization, cross-agency coordination, restoration priority |

Collaborative restoration and mobile-resource studies show that performance depends not only on physical action but also on how resources and decisions are coordinated across infrastructures (Jiang et al., 2026; Magoua et al., 2026; Qiu et al., 2023).

$u_O$ represents organizational interventions, not physical organizational dynamics.

---

## 14. Response time

The response pathway is

$$
\text{sense}
\rightarrow\text{communicate}
\rightarrow\text{estimate}
\rightarrow\text{decide}
\rightarrow\text{coordinate}
\rightarrow\text{mobilize}
\rightarrow\text{act}.
$$

**Equation S4.11 — Sequential response-time decomposition [D]**

$$
\begin{aligned}
\tau_{\rm response}={}&
\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

If processes overlap or execute in parallel, $\tau_{\rm response}$ is the completion time of the relevant critical path rather than the arithmetic sum of all durations.

This is a derived synthesis [D], not a metric attributed to one source. Communication/control literature establishes communication and processing delays; situation-awareness research establishes information-to-decision effects; infrastructure-restoration research establishes decision, dispatch, and resource-mobilization processes (Liu et al., 2017; Panteli & Kirschen, 2015; Qiu et al., 2023).

Stage 3 provides the competing disruption clock $\tau_{\rm cascade}$ or component-specific $T_C(j)$.

The central engineering question is:

> **Can the system know, decide, coordinate, and act before disruption reaches the target?**

---

## 15. Proposed response-to-cascade diagnostic

**Equation S4.12 — Proposed timing diagnostic [P]**

$$
\Pi_R=
\frac{\tau_{\rm response}}{\tau_{\rm cascade}}.
$$

Potential interpretation:

| Regime | Interpretation |
|---|---|
| $\Pi_R<1$ | Nominal response completes faster than the characteristic cascade process. |
| $\Pi_R\approx1$ | Strong temporal competition. |
| $\Pi_R>1$ | Nominal response is slower. |

However,

$$
\Pi_R<1\not\Rightarrow\text{successful control}.
$$

Successful intervention also requires observability, estimation accuracy, authority, resources, accessibility, controllability, and appropriate action. A local future quantity may compare $\tau_{\rm response}(j)$ with $T_C(j)$, but that remains a candidate analysis rather than a universal definition.

---

## 16. Partial-information control as a central test

A strong nested comparison is:

| Model variant | Assumption |
|---|---|
| $\mathscr M_0$ | Perfect observation + instantaneous organization. |
| $\mathscr M_1$ | Imperfect/delayed information. |
| $\mathscr M_2$ | Imperfect information + organizational constraints. |
| $\mathscr M_3$ | Full closed-loop P–T–I–O system. |

This design is proposed [P]. The symbols $\mathscr M_k$ denote model variants and are intentionally distinct from the Stage-2 mechanism symbol $M_{ij}$. The design is grounded in literature showing separately that imperfect information changes estimation/control and organizational coordination changes restoration outcomes (Arcieri et al., 2023; Cheng et al., 2024; Magoua et al., 2026; Qiu et al., 2023).

The intended contrasts are

$$
\mathscr M_1-\mathscr M_0=\text{information effect},
$$

$$
\mathscr M_2-\mathscr M_1=\text{organizational effect},
$$

and

$$
\mathscr M_3-\mathscr M_0=\text{full coupled response effect}.
$$

---

## 17. Stage-4 validation

Stage 4 is validated at the level of the entire inference-to-action chain:

$$
\text{measurement}
\rightarrow\text{estimation}
\rightarrow\text{decision}
\rightarrow\text{action}
\rightarrow\text{closed-loop consequence}.
$$

Validation must test:

- sensor/measurement coverage;
- observability;
- estimation error and uncertainty;
- delay and information freshness;
- decision feasibility;
- organizational/resource feasibility;
- action execution time;
- closed-loop system trajectory.

Representative quantities include

$$
RMSE(\widehat X,X),\qquad \Sigma_X,\qquad P(\text{correct state classification}),
$$

$$
\delta_I,\quad\Delta_I,\quad p_{\rm loss},\quad A_I,
$$

and

$$
\tau_{\rm decision},\quad\tau_{\rm coord},\quad\tau_{\rm mobilization},\quad N_{\rm crew},\quad R_O.
$$

Control feasibility must be verified:

$$
u(t)\in\mathcal U(z_I,z_O).
$$

---

## 18. Boundary with Stage 3

Stage 3 contains $z_I(t)$ and $z_O(t)$ because information and organizational conditions evolve dynamically. Stage 4 does **not** repeat those dynamics.

| Stage | Responsibility |
|---|---|
| **3** | Determine how $z_I(t)$ and $z_O(t)$ evolve. |
| **4** | Determine how current $z_I(t)$ and $z_O(t)$ constrain knowledge and intervention. |

For example,

$$
\text{Stage 3: }A_I(t)\downarrow,\ \delta_I(t)\uparrow,
$$

while

$$
\text{Stage 4: }(A_I,\delta_I)\rightarrow y\rightarrow\widehat X\rightarrow u.
$$

Similarly, Stage 3 evolves $R_O(t)$, $C_O(t)$, and $N_{\rm crew}(t)$; Stage 4 maps them into the feasible action set $\mathcal U(z_I,z_O)$.

---

## 19. Boundary with Stage 5

Stage 4 ends at **controlled response**. It does not determine

$$
\mathcal V_{\rm sus}^{u},\qquad\rho_g,\qquad T_{\rm exit}.
$$

Those are Stage-5 quantities.

| Stage | Output / question |
|---|---|
| **3** | Generates the system trajectory. |
| **4** | Closes the observation–decision–control loop and produces $u(t)$ and $Y^u(t)$. |
| **5** | Tests whether $Y^u(t)$ remains inside the sustainable viability set. |

The interface is

$$
u(t)\longrightarrow Y^u(t)\longrightarrow\mathcal V_{\rm sus}^{u}.
$$

---

## 20. Research gap supported by the reviewed corpus

The sampled literature is mature in separate areas: power state estimation, traffic observability, networked control, information freshness, situation awareness, organizational coordination, repair-resource optimization, and POMDP/MARL restoration.

The sampled work does not reveal a mature standard framework that explicitly carries the entire causal chain

$$
X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X
$$

across a physically explicit power–multimodal-transportation system while simultaneously retaining information degradation, organizational feasibility, cross-layer interdependencies, and the Stage-3 cascade clock. This is a synthesis from the reviewed corpus rather than a claim that no such study could exist (Cheng et al., 2024; Li et al., 2019; Mohebbi et al., 2020; Qiu et al., 2023).

The defensible research niche is:

> **Response is not only a control problem; it is a partial-observation + information + organization + actuation problem.**

---

## Final frozen Stage-4 scope

| Item | Canonical Stage-4 specification |
|---|---|
| **Stage** | Observation, Organization, Feedback and Control |
| **Question** | How is the system observed, interpreted, coordinated and controlled? |
| **Physical reality** | $X(t)=[x_P(t),x_T(t)]^\top$ |
| **Measurement** | $y(t)=H[X(t-\delta)]+\varepsilon(t)$ |
| **Observability** | Determine whether relevant P–T states can be inferred. |
| **Information state** | $z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top$ |
| **State estimation** | $(\widehat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I)$ |
| **Partial observability** | $b_t(X)=p(X_t\mid y_{[0,t]},u_{[0,t)})$ |
| **Interpretation** | Situation awareness from estimated state and uncertainty. |
| **Organization** | Authority, coordination, resources, workforce, mobilization. |
| **Feasible actions** | $u(t)\in\mathcal U(z_I(t),z_O(t))$ |
| **Control policy** | $u(t)=\pi[\widehat X(t),z_I(t),z_O(t)]$ |
| **Feedback** | $X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X$ |
| **Temporal response** | Sensing + communication + estimation + decision + coordination + mobilization + actuation, or the corresponding critical path when processes overlap. |
| **Stage-3 interface** | Compare $\tau_{\rm response}$ with $\tau_{\rm cascade}$ or $T_C(j)$. |
| **Uncertainty** | Measurement, estimation, communication, decision, and resource uncertainty. |
| **Validation** | Observability, estimation, timing, decision feasibility, and closed-loop tests. |
| **Primary outputs** | $\widehat X(t),\Sigma_X(t),b_t,\mathcal U(z_I,z_O),u(t),\tau_{\rm response},Y^u(t)$ |

The scientific essence is

$$
X_{\rm reality}
\rightarrow y_{\rm measure}
\rightarrow I_{\rm know}
\rightarrow \widehat X_{\rm infer}
\rightarrow O_{\rm coordinate}
\rightarrow u_{\rm act}
\rightarrow X_{\rm changed}.
$$

### Status

> **STAGE 4 SCIENTIFIC SCOPE: FROZEN**

The ratio

$$
\Pi_R=\frac{\tau_{\rm response}}{\tau_{\rm cascade}}
$$

remains explicitly a **proposed thesis diagnostic [P]**, not an established metric and not part of the theoretical definition of resilience.

---

## Freeze statement

Stage 4 has the following literature-supported boundary: **observe the Stage-3 system, reconstruct its relevant state under imperfect information, convert that knowledge through organizational capability into feasible actions, and close the feedback loop—without yet asking whether the resulting controlled trajectory lies inside the sustainable viability set.**

The seven-stage framework remains unchanged. Stage 4 is frozen at framework level; later method choices instantiate this scope without redefining it.

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
