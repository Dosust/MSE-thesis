# Stage 4 — Observation, Organization, Feedback and Control

**Framework stage:** Stage 4 — Observation, Organization, Feedback and Control  
**Status:** CANONICAL / FROZEN  
**Frozen:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Citation standard:** APA 7th edition author–date  
**Evidence basis:** 10 analytical passes; 31 core studies  
**Change rule:** Do not revise this Stage-4 scope unless explicitly requested and versioned.  
**Framework preservation rule:** This document formalizes Stage 4 only. It does **not** alter the frozen seven-stage framework or redefine Stages 1–3.

> **Evidence notation:** `[E]` = established literature; `[D]` = derived synthesis; `[P]` = proposed thesis construct.

> **Boundary rule:** Stage 4 observes, infers, interprets, coordinates, and controls the Stage-3 system. It does not redefine Stage-3 dynamics and does not compute the Stage-5 viability objects.

---

## Frozen research question

$$
\boxed{ \textbf{How is the system observed, interpreted, coordinated and controlled?} }
$$

The scientific progression is

$$
\boxed{ \underbrace{\{P,T,I,O\}}_{\text{Stage 1}} \rightarrow \underbrace{\mathfrak I_{ij}^{\alpha\beta}}_{\text{Stage 2}} \rightarrow \underbrace{Y(t),\mathcal G(t),m(t),T_C}_{\text{Stage 3}} \rightarrow \underbrace{\text{observation, inference, organization, feedback and action}}_{\text{Stage 4}}. }
$$

### Notation bridge

The dynamic information and organizational states are inherited from Stage 3 as $z_I(t)$ and $z_O(t)$. In the conceptual spine, the labels $I$ and $O$ denote the corresponding information and organizational functions. Mathematical operators in Stage 4 use $z_I$ and $z_O$ explicitly to avoid conflating a layer label with its time-varying state.

Stage 3 determines how the actual coupled system evolves. Stage 4 addresses a fundamentally different problem: **the true physical state is not automatically known to the decision maker**. Measurements are incomplete, asynchronous, noisy, delayed, or unavailable; the state must therefore be inferred before an intervention can be selected and executed. This distinction is fundamental in both power-system state estimation and transportation-network observability research (Castillo et al., 2015; Cheng et al., 2024; Gentili & Mirchandani, 2012).

---

## Step 1 — What the 10 literature passes established

| Pass | Scientific problem | Main evidence-supported conclusion |
|---:|---|---|
| **1** | Measurement | Sensors produce partial observations of reality, not the state itself (Cheng et al., 2024; Gentili & Mirchandani, 2012). |
| **2** | Observability | State recoverability depends on measurement placement, topology, available prior information, and model structure (Castillo et al., 2015; Cheng et al., 2024). |
| **3** | State estimation | Estimation must accommodate uncertainty, multiple reporting rates, asynchronous data, cyber failures, and changing states (Cheng et al., 2024; Zhou et al., 2024). |
| **4** | Information quality | Delay, packet loss, sampling, and information age can materially alter closed-loop performance (Liu et al., 2017; Mena & Núñez, 2023; Yates et al., 2021; Zhang et al., 2017). |
| **5** | Situation awareness | Measurement and estimation alone do not guarantee correct interpretation; comprehension and anticipation matter to operational decisions (Endsley, 1995; Panteli & Kirschen, 2015). |
| **6** | Organizational decision | Authority, coordination, resources, information sharing, and organizational structure influence feasible response (Li et al., 2019; McAlister et al., 2024; Mohebbi et al., 2020). |
| **7** | Partial observability | Decisions under damaged sensing/communication differ from full-information decisions; POMDP formulations provide one established route (Arcieri et al., 2023; Qiu et al., 2023). |
| **8** | Feedback and control | Communication imperfections and estimation errors must enter the closed loop rather than remain external metadata (Ding et al., 2021; Liu et al., 2017; Zhang et al., 2017). |
| **9** | Multi-actor coordination | Centralized, decentralized, and collaborative decision structures can produce different restoration outcomes (Iloglu et al., 2025; Magoua et al., 2026). |
| **10** | Response versus disruption | Sensing-to-action is a timed process; effective response depends on whether information, decision, coordination, mobilization, and actuation occur fast enough relative to system evolution (Panteli & Kirschen, 2015; Prostejovsky et al., 2019; Qiu et al., 2023). |

The repeated result across the ten passes is important:

$$
\boxed{ \text{measurement} \neq \text{information} \neq \text{estimated state} \neq \text{situation awareness} \neq \text{decision} \neq \text{executed action}. }
$$

That distinction is the backbone of Stage 4.

---

## Step 2 — The 31-paper core evidence base

The ranking below is by **direct usefulness for constructing Stage 4**, not citation count.

| Rank | Core study | Contribution to Stage 4 |
|---:|---|---|
| **1** | Panteli and Kirschen (2015) | Data/ICT → situation awareness → operator decision making. |
| **2** | Cheng et al. (2024) | Power-system measurement, observability, estimation, asynchronous data, and uncertainty. |
| **3** | Endsley (1995) | Foundational perception → comprehension → projection structure for situation awareness. |
| **4** | Zhou et al. (2024) | Dynamic state estimation under cyber-physical uncertainty. |
| **5** | Yates et al. (2021) | Rigorous information-freshness concept through Age of Information. |
| **6** | Prostejovsky et al. (2019) | Human operators and decision-support systems under increasing automation. |
| **7** | Ding et al. (2021) | Secure estimation and feedback control under cyber-physical disruption. |
| **8** | Liu et al. (2020) | Bidirectional power–communication dependency in monitoring and control. |
| **9** | Zhang et al. (2017) | Networked-control treatment of sampling, delay, packet loss, quantization, and communication constraints. |
| **10** | Liu et al. (2017) | Delay-induced degradation and compensation in communication-based power control. |
| **11** | Mena and Núñez (2023) | Information freshness linked directly to networked-control systems. |
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

## Step 3 — What Stage 4 scientifically means

The evidence changes the central chain from a simple block diagram into a **closed-loop partially observable socio-technical control process**:

$$
\boxed{ X(t) \rightarrow y(t) \rightarrow I(t) \rightarrow \hat X(t) \rightarrow O(t) \rightarrow u(t) \rightarrow X(t). }
$$

This chain is the conceptual spine.

Its elements mean:

$$
\boxed{ \begin{aligned} X(t)&=\text{actual physical }P-T\text{ state},\\ y(t)&=\text{available measurements},\\ I(t)&=\text{information capability and information condition},\\ \hat X(t)&=\text{estimated/believed physical state},\\ O(t)&=\text{organizational interpretation and response capability},\\ u(t)&=\text{executed intervention}. \end{aligned} }
$$

Power-system research clearly distinguishes the physical system state from measurements and estimated states, while traffic-network research makes the same distinction between observed flows and quantities that require estimation or prediction (Castillo et al., 2015; Cheng et al., 2024).

Therefore:

$$
\boxed{ X\neq y\neq I\neq\hat X\neq O\neq u. }
$$

---

## Step 4 — Observation

The first Stage-4 process is

$$
\boxed{ X(t)\longrightarrow y(t). }
$$

A general measurement model is

$$
\boxed{ y_k(t) = H_k \left[ X(t-\delta_k) \right] + \nu_k(t), } \tag{S4.1}
$$

where $H_k$ is the measurement function, $\delta_k$ represents measurement/communication delay, and $\nu_k$ represents measurement error.

This form is consistent with established state-estimation frameworks in which system states are inferred from SCADA, PMU, AMI and related measurements rather than directly observed (Cheng et al., 2024; Zhou et al., 2024).

For $P$, measurements may include

$$
\boxed{ y_P= \{ V,\, P_{ij},\, Q_{ij},\, P_{\rm inj},\, f,\, SOC,\, P_{\rm traction}, P_{\rm charge} \}. }
$$

For $T$,

$$
\boxed{ y_T= \{ q,\, k,\, v,\, TT,\, \text{vehicle position}, SOC_{EV}, \text{bus position}, \text{train position/speed} \}. }
$$

Traffic observability research shows that sensor placement determines which flows can be directly reconstructed and which require additional assumptions, prior information or estimation (Castillo et al., 2015; Gentili & Mirchandani, 2012; Owais, 2022).

---

## Step 5 — Observability

The critical question is not simply whether sensors exist, but whether available observations contain enough information to distinguish relevant states.

For a local linear representation,

$$
x_{k+1}=Ax_k, \qquad y_k=Cx_k,
$$

with classical observability benchmark

$$
\boxed{ \operatorname{rank} \begin{bmatrix} C\\ CA\\ CA^2\\ \vdots\\ CA^{n-1} \end{bmatrix} =n. } \tag{S4.2}
$$

This is treated only as a **local/classical benchmark** because the Stage-3 system is nonlinear, hybrid, delayed, and multilayer.

The general Stage-4 question is therefore

$$
\boxed{ X_1\neq X_2 \quad\Rightarrow\quad \mathcal H_{\rm obs}(X_1) \neq \mathcal H_{\rm obs}(X_2), }
$$

over the relevant observation horizon.

Power-system state-estimation research shows that observability depends on measurement availability, sensor type, topology, and measurement configuration, while transportation research has an analogous flow-observability problem (Cheng et al., 2024; Gentili & Mirchandani, 2012).

---

## Step 6 — Information and state estimation

Observation produces $y$, but the system requires an estimate:

$$
\boxed{ \hat X(t) = \mathcal E \left( y_{[0,t]}, z_I(t) \right). } \tag{S4.3}
$$

The estimator should return not only a point estimate but an uncertainty representation:

$$
\boxed{ \left( \hat X(t), \Sigma_X(t) \right) = \mathcal E \left( y_{[0,t]}, z_I(t) \right). } \tag{S4.4}
$$

This follows modern state-estimation literature, which explicitly treats measurement uncertainty, asynchronous reporting rates, correlated data sources, missing measurements and cyber-security issues (Cheng et al., 2024; Zhou et al., 2024).

The information state inherited from Stages 1–3 remains

$$
\boxed{ z_I= [ A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync} ]^\top. }
$$

Stage 4 **uses** these variables to determine what can be reliably inferred; it does not redefine their dynamics:

$$
\boxed{ \underbrace{\dot z_I}_{\text{Stage 3}} \qquad\neq\qquad \underbrace{\hat X=\mathcal E(y,z_I)}_{\text{Stage 4}}. }
$$

---

## Step 7 — Information freshness

For dynamic resilience, having information is insufficient if it is stale. Age of Information provides

$$
\boxed{ \Delta_I(t)=t-U(t), } \tag{S4.5}
$$

where $U(t)$ is the generation time of the freshest received update (Yates et al., 2021).

Networked-control research additionally shows that sampling, delays, packet dropouts, communication constraints and variable transmission behavior can degrade closed-loop performance (Liu et al., 2017; Zhang et al., 2017).

Therefore,

$$
\boxed{ \text{available information} \not\Rightarrow \text{timely information}, }
$$

and

$$
\boxed{ \text{timely information} \not\Rightarrow \text{accurate state estimate}. }
$$

These remain separate concepts.

---

## Step 8 — Partial observability and belief state

During disruption,

$$
\boxed{ \hat X(t)\neq X(t) }
$$

is not an exceptional case; it may be central.

Infrastructure-control studies increasingly formulate restoration under incomplete information through MDP/POMDP-type decision processes. Qiu et al. (2023), for example, formulate coupled transport–energy repair-crew dispatch as a decentralized partially observable Markov decision process, while Arcieri et al. (2023) combine uncertain observations and sequential infrastructure decisions.

A belief-state formulation is

$$
\boxed{ b_t(x) = p \left( X(t)=x \mid y_{[0,t]}, u_{[0,t)} \right). } \tag{S4.6}
$$

Stage 4 can therefore reason from

$$
\boxed{ \hat X \quad\text{or, when necessary,}\quad b_t(X) }
$$

without assuming omniscient knowledge.

Importantly,

$$
\boxed{ \text{POMDP is a candidate decision formalism, not Stage 4 itself}. }
$$

Stage 4 remains method-independent.

---

## Step 9 — Situation awareness and interpretation

State estimation and situation awareness are not identical. Endsley (1995) conceptualizes situation awareness through

$$
\boxed{ \text{perception} \rightarrow \text{comprehension} \rightarrow \text{projection}. }
$$

Panteli and Kirschen (2015) transfer situation-awareness reasoning to electric-power operation and show why incomplete or incorrect awareness can impair operational decisions during disturbances.

Situation awareness does **not** become a fifth infrastructure layer. Instead,

$$
\boxed{ I \rightarrow \hat X \rightarrow \underbrace{\text{interpretation / situation awareness}}_{\text{functional bridge}} \rightarrow O. }
$$

A proposed processing representation is

$$
\boxed{ \mathcal A_{\rm SA}(t)=\mathscr A\!\left[\hat X(t),\Sigma_X(t),m(t),\mathcal G(t)\right]. } \tag{S4.7}
$$

$\mathcal A_{\rm SA}$ is a **Stage-4 processing construct [P]**, not a new infrastructure layer.

---

## Step 10 — Organization

Stage 1 defined the organizational layer, and Stage 3 determines how organizational states evolve. Stage 4 asks:

$$
\boxed{ \text{Given available knowledge, who can decide, coordinate and authorize action?} }
$$

Organizational-resilience literature supports retaining authority, coordination, knowledge sharing, resources and interorganizational structure because these factors influence infrastructure decision making and recovery effectiveness (Li et al., 2019; McAlister et al., 2024; Mohebbi et al., 2020).

The organizational state remains

$$
z_O= [ A_O,C_O,R_O,W_O,\tau_D,\tau_C^O,\tau_M ]^\top.
$$

Stage 4 uses that capability to constrain action:

$$
\boxed{ \mathcal U_{\rm available}(t)=\mathcal U\!\left[z_I(t),z_O(t)\right]. } \tag{S4.8}
$$

Hence

$$
\boxed{ u(t)\in\mathcal U(z_I(t),z_O(t)). }
$$

A technically desirable action may remain organizationally infeasible because authorization, coordination, resources, workforce or mobilization are unavailable. Dynamic organizational-network research and collaborative infrastructure-restoration research provide evidence that organizational configuration changes achievable recovery outcomes (Damaschin et al., 2026; Li et al., 2019; Magoua et al., 2026).

Therefore,

$$
\boxed{ \text{technically desirable action} \not\Rightarrow \text{organizationally executable action}. }
$$

---

## Step 11 — Decision and control

The Stage-4 feedback policy is represented generically as

$$
\boxed{ u(t)=\pi\!\left[\hat X(t),z_I(t),z_O(t)\right],\qquad u(t)\in\mathcal U(z_I,z_O). } \tag{S4.9}
$$

The thesis does **not** freeze Stage 4 to MPC, reinforcement learning, dynamic programming, MILP, game theory, or another solver. Different studies use robust optimization, POMDP/MARL, multi-agent reinforcement learning, cooperative game theory, and non-cooperative game theory for different infrastructure decision problems (Iloglu et al., 2025; Magoua et al., 2026; Qiu et al., 2023; Yang et al., 2024; Zhu et al., 2024).

Thus,

$$
\boxed{ \pi = \text{decision/control policy}, }
$$

while the algorithm used to compute $\pi$ remains an implementation choice.

---

## Step 12 — Feedback closure

Stage 4 closes the loop:

$$
\boxed{ X \rightarrow y \rightarrow I \rightarrow \hat X \rightarrow O \rightarrow u \rightarrow X. }
$$

This is more rigorous than

$$
\text{failure}\rightarrow\text{optimization}\rightarrow\text{repair}
$$

because the controller acts on $\hat X$ rather than necessarily on $X$.

The implemented intervention returns to the Stage-3 dynamics:

$$
\boxed{ u(t) \rightarrow F^{m(t)} \rightarrow Y(t+\Delta t). }
$$

Networked-control theory explicitly treats measurement, communication and actuation as parts of a closed feedback system and shows that communication imperfections can influence control-system performance and stability (Liu et al., 2017; Zhang et al., 2017).

---

## Step 13 — Control actions in the P–T–I–O system

The action vector may be represented as

$$
\boxed{ u(t)= \begin{bmatrix} u_P(t)\\ u_T(t)\\ u_I(t)\\ u_O(t) \end{bmatrix}. } \tag{S4.10}
$$

| Action family | Examples |
|---|---|
| $u_P$ | switching, DER dispatch, storage dispatch, charging limitation, load restoration, traction-power reconfiguration |
| $u_T$ | traffic control, rerouting, bus dispatch, rail scheduling, road opening/closure |
| $u_I$ | measurement prioritization, communication routing, sampling/update priority, information-sharing activation |
| $u_O$ | crew assignment, resource allocation, mobilization, cross-agency coordination, restoration priority |

Collaborative restoration and mobile-resource studies demonstrate that performance depends not only on physical action but also on how resources and decisions are coordinated across infrastructures (Jiang et al., 2026; Magoua et al., 2026; Qiu et al., 2023).

Importantly,

$$
\boxed{ u_O \text{ represents organizational interventions, not physical organizational dynamics}. }
$$

---

## Step 14 — Response time

The complete response pathway is

$$
\boxed{ \text{sense} \rightarrow \text{communicate} \rightarrow \text{estimate} \rightarrow \text{decide} \rightarrow \text{coordinate} \rightarrow \text{mobilize} \rightarrow \text{act}. }
$$

For a sequential, non-overlapping response path, the thesis uses the derived decomposition

$$
\boxed{ \tau_{\rm response} = \tau_{\rm sense} + \tau_{\rm comm} + \tau_{\rm est} + \tau_{\rm decision} + \tau_{\rm coord} + \tau_{\rm mobilization} + \tau_{\rm act}. } \tag{S4.11}
$$

If processes overlap or execute in parallel, $\tau_{\rm response}$ is the completion time of the relevant critical path rather than the arithmetic sum of all component durations.

This is a **derived synthesis [D]** of established process delays, not a metric attributed to one source. Communication/control literature establishes communication and processing delays; situation-awareness research establishes information-to-decision effects; and infrastructure-restoration research establishes decision, dispatch and resource-mobilization processes (Liu et al., 2017; Panteli & Kirschen, 2015; Qiu et al., 2023).

Stage 3 provides the competing disruption clock

$$
\boxed{ \tau_{\rm cascade} \quad\text{or component-specific}\quad T_C(j). }
$$

Therefore the central engineering question becomes

$$
\boxed{ \textbf{Can the system know, decide, coordinate and act before the disruption reaches the target?} }
$$

---

## Step 15 — Proposed response-to-cascade diagnostic

Only after separating the established quantities do we propose

$$
\boxed{ \Pi_R = \frac{\tau_{\rm response}} {\tau_{\rm cascade}}. } \tag{S4.12}
$$

This is explicitly

$$
\boxed{[P]\ \textbf{a thesis diagnostic, not an established resilience law}.}
$$

Potential interpretation:

- $\Pi_R<1$: nominal response completes faster than the characteristic cascade process;
- $\Pi_R\approx1$: strong temporal competition;
- $\Pi_R>1$: nominal response is slower.

However,

$$
\boxed{ \Pi_R<1 \not\Rightarrow \text{successful control}. }
$$

Successful intervention also requires observability, estimation accuracy, authority, resources, accessibility, controllability, and appropriate action. A local future quantity may compare $\tau_{\rm response}(j)$ with Stage 3's $T_C(j)$, but that remains a **candidate analysis**, not a universal definition.

---

## Step 16 — Partial-information control as a central test

A strong nested model-comparison experiment emerging from the review is

$$
\boxed{ \mathscr M_0 = \text{perfect observation + instantaneous organization} }
$$

versus

$$
\boxed{ \mathscr M_1 = \text{imperfect/delayed information} }
$$

versus

$$
\boxed{ \mathscr M_2 = \text{imperfect information + organizational constraints} }
$$

versus

$$
\boxed{ \mathscr M_3 = \text{full closed-loop }P-T-I-O. }
$$

This nested design is **proposed [P]**; the symbols $\mathscr M_k$ denote model variants and are intentionally distinct from the Stage-2 mechanism symbol $M_{ij}$. It is grounded in literature showing separately that imperfect information changes estimation/control and organizational coordination changes restoration outcomes (Arcieri et al., 2023; Cheng et al., 2024; Magoua et al., 2026; Qiu et al., 2023).

It allows the contrasts

$$
\mathscr M_1-\mathscr M_0 = \text{information effect},
$$

$$
\mathscr M_2-\mathscr M_1 = \text{organizational effect},
$$

and

$$
\mathscr M_3-\mathscr M_0 = \text{full coupled response effect}.
$$

This is a stronger thesis test than simply showing that a controller works.

---

## Step 17 — Stage-4 validation

Stage 4 is validated at the level of the entire inference-to-action chain:

$$
\boxed{ \text{measurement} \rightarrow \text{estimation} \rightarrow \text{decision} \rightarrow \text{action} \rightarrow \text{closed-loop consequence}. }
$$

Validation therefore tests sensor/measurement coverage, observability, estimation error and uncertainty, delay and information freshness, decision feasibility, resource/organizational feasibility, action execution time, and the closed-loop system trajectory.

For estimation, relevant quantities include

$$
RMSE(\hat X,X), \qquad \Sigma_X, \qquad P(\text{correct state classification}).
$$

For information,

$$
\delta_I,\quad \Delta_I,\quad p_{\rm loss},\quad A_I.
$$

For organization,

$$
\tau_{\rm decision}, \quad \tau_{\rm coord}, \quad \tau_{\rm mobilization}, \quad N_{\rm crew}, \quad R_O.
$$

For control,

$$
\boxed{u(t)\in\mathcal U(z_I,z_O)}
$$

must be verified rather than assumed.

---

## Step 18 — Critical boundary with Stage 3

Stage 3 already contains $z_I(t)$ and $z_O(t)$ because information and organizational conditions evolve dynamically. Stage 4 does **not** repeat those dynamics.

$$
\boxed{ \begin{array}{lll} \textbf{Stage 3} && \text{How do }z_I,z_O\text{ evolve?}\\[1mm] \textbf{Stage 4} && \text{How do current }z_I,z_O \text{ constrain knowledge and intervention?} \end{array} }
$$

For example,

$$
\boxed{ \text{Stage 3: } A_I(t)\downarrow,\; \delta_I(t)\uparrow }
$$

then

$$
\boxed{ \text{Stage 4: } A_I,\delta_I \rightarrow y \rightarrow \hat X \rightarrow u. }
$$

Similarly,

$$
\boxed{ \text{Stage 3: } R_O(t),C_O(t),N_{\rm crew}(t) }
$$

evolve, while

$$
\boxed{ \text{Stage 4: } (R_O,C_O,N_{\rm crew}) \rightarrow \mathcal U(z_I,z_O) }
$$

determines which interventions are feasible.

This protects the architecture from duplication.

---

## Step 19 — Critical boundary with Stage 5

Stage 4 ends at **controlled response**. It does not determine

$$
\mathcal V_{\rm sus}^{u},\qquad \rho_g,\qquad T_{\rm exit}.
$$

Those belong to Stage 5.

Therefore,

$$
\boxed{ \text{Stage 3 generates the trajectory} }
$$

$$
\boxed{ \text{Stage 4 closes the observation-decision-control loop} }
$$

$$
\boxed{ \text{Stage 5 asks whether that controlled trajectory remains viable}. }
$$

The precise interface is

$$
\boxed{ u(t) \longrightarrow Y^{u}(t) \longrightarrow \mathcal V_{\rm sus}^{u}. }
$$

---

## Step 20 — Research gap supported by the reviewed corpus

The sampled literature is mature in separate areas including power state estimation, traffic observability, networked control, information freshness, situation awareness, organizational coordination, repair-resource optimization, and POMDP/MARL restoration.

The sampled work does not reveal a mature standard framework that explicitly carries the entire causal chain

$$
\boxed{ X \rightarrow y \rightarrow I \rightarrow \hat X \rightarrow O \rightarrow u \rightarrow X }
$$

across a physically explicit **power–multimodal-transportation system** while simultaneously retaining information degradation, organizational feasibility, cross-layer interdependencies, and the Stage-3 cascade clock. This is a synthesis from the reviewed corpus rather than a claim that no such study could exist (Cheng et al., 2024; Li et al., 2019; Mohebbi et al., 2020; Qiu et al., 2023).

The defensible research niche is therefore:

$$
\boxed{ \textbf{response is not only a control problem;} }
$$

it is a

$$
\boxed{ \textbf{partial-observation + information + organization + actuation problem}. }
$$

---

## Final frozen Stage-4 scope

| Item | Canonical Stage-4 specification |
|---|---|
| **Stage** | Observation, Organization, Feedback and Control |
| **Question** | How is the system observed, interpreted, coordinated and controlled? |
| **Physical reality** | $X(t)=[x_P(t),x_T(t)]^\top$ |
| **Measurement** | $y(t)=H[X(t-\delta)]+\nu(t)$ |
| **Observability** | determine whether relevant P–T states can be inferred |
| **Information state** | $z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top$ |
| **State estimation** | $(\hat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I)$ |
| **Partial observability** | $b_t(X)=p(X_t\mid y_{[0,t]},u_{[0,t)})$ |
| **Interpretation** | situation awareness from estimated state and uncertainty |
| **Organization** | authority, coordination, resources, workforce, mobilization |
| **Feasible actions** | $u(t)\in\mathcal U(z_I(t),z_O(t))$ |
| **Control policy** | $u(t)=\pi[\hat X(t),z_I(t),z_O(t)]$ |
| **Feedback** | $X\rightarrow y\rightarrow I\rightarrow\hat X\rightarrow O\rightarrow u\rightarrow X$ |
| **Temporal response** | sensing + communication + estimation + decision + coordination + mobilization + actuation |
| **Stage-3 interface** | compare $\tau_{\rm response}$ with $\tau_{\rm cascade}$ or $T_C(j)$ |
| **Uncertainty** | measurement, estimation, communication, decision, and resource uncertainty |
| **Validation** | observability, estimation, timing, decision feasibility, and closed-loop tests |
| **Primary outputs** | $\hat X(t),\Sigma_X(t),b_t,\mathcal U(z_I,z_O),u(t),\tau_{\rm response},Y^u(t)$ |

The scientific essence is

$$
\boxed{ \underbrace{X}_{\text{reality}} \rightarrow \underbrace{y}_{\text{measure}} \rightarrow \underbrace{I}_{\text{know}} \rightarrow \underbrace{\hat X}_{\text{infer}} \rightarrow \underbrace{O}_{\text{interpret/coordinate}} \rightarrow \underbrace{u}_{\text{act}} \rightarrow \underbrace{X}_{\text{changed reality}}. }
$$

The first four stages therefore form

$$
\boxed{ \underbrace{\{P,T,I,O\}}_{\textbf{Stage 1: what exists}} \rightarrow \underbrace{\mathfrak I_{ij}^{\alpha\beta}}_{\textbf{Stage 2: why it affects}} \rightarrow \underbrace{Y(t),\mathcal G(t),m(t),T_C}_{\textbf{Stage 3: how it evolves}} \rightarrow \underbrace{\hat X,I,O,u,\tau_{\rm response}}_{\textbf{Stage 4: how it is known and controlled}}. }
$$

### Status

$$
\boxed{\textbf{STAGE 4 SCIENTIFIC SCOPE: FROZEN}}
$$

The ratio

$$
\boxed{ \Pi_R = \frac{\tau_{\rm response}} {\tau_{\rm cascade}} }
$$

remains explicitly a **proposed thesis diagnostic [P]**, not an established metric and not part of the theoretical definition of resilience.

---

## Freeze statement

This gives Stage 4 a literature-supported scientific boundary: **observe the Stage-3 system, reconstruct its relevant state under imperfect information, convert that knowledge through organizational capability into feasible actions, and close the feedback loop—without yet asking whether the resulting controlled trajectory lies inside the sustainable viability set.**

The seven-stage framework remains unchanged. Stage 4 is frozen at the framework level; later method choices must instantiate this scope without redefining it.

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
