# Stages 1–2 — APA 7 Evidence-Grounded Canonical Specification

![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Scope](https://img.shields.io/badge/Stages%201--2-CANONICAL-0969DA)

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**System:** Power–Transportation–Information–Organization (P–T–I–O)  
**Status:** Canonical evidence-grounded companion to Stages 1 and 2  
**Citation standard:** APA 7th edition author–date  
**Updated:** 2026-09-11

> **Scope rule:** This document preserves the current Stage-1 ontology and frozen Stage-2 interdependency scope. It adds literature grounding; it does not alter the seven-stage framework.

> **Evidence rule:** Citations support the specific claims to which they are attached. The complete thesis interdependency tuple is a thesis synthesis and is not attributed to any single source.

> **Rendering rule:** Long verbal statements are kept outside mathematics; taxonomies use tables; equations use GitHub-compatible display math without oversized boxes.

---

# Stage 1 — System Ontology and Multilayer Structure

## RQ1 / SO1 — current canonical question

> **What entities exist, what layers constitute the system, and where can interactions occur?**

**Specific objective:** Define the coupled Power–Transportation system boundary, entities, layers, locations, interfaces, states and service requirements, with Information and Organization as supporting domains.

**Question authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`. This 2026-09-17 wording amendment aligns the question with Chapter I; technical results and validation status are unchanged.

The system is

```math
\mathcal S=\{P,T,I,O\},
```

with

```math
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
```

Critical infrastructures can be mutually dependent through physical, cyber/informational, geographic, logical, and organizational relationships; therefore, interdependent infrastructure cannot always be represented adequately as isolated physical networks (Mohebbi et al., 2020; Ouyang, 2014; Rinaldi et al., 2001).

The framework-level state is

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
```

---

## 1. Power infrastructure system $P$

```math
P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP}.
```

The scope includes conventional electricity infrastructure together with charging and traction-power interfaces because transportation electrification creates interactions across distribution networks, charging infrastructure, and railway traction-power systems (Bellè et al., 2022; Sun et al., 2021; Unterluggauer et al., 2022).

| Subsystem | Framework-level content |
|---|---|
| $P_G$ — Generation | conventional generation, solar, wind, distributed generation |
| $P_{Tr}$ — Transmission | high-voltage buses, lines, bulk substations, transformers |
| $P_D$ — Distribution | substations, feeders, transformers, buses, LV/MV networks, critical loads |
| $P_{DER}$ — DER/storage | BESS, distributed PV, microgrids, local generation, flexible DERs |
| $P_C$ — Charging | EV chargers, fast chargers, bus-depot/opportunity chargers, converters, bidirectional charging, smart charging, V2G interfaces |
| $P_{TP}$ — Traction power | traction substations/transformers, rectifiers, inverters, feeders, catenary, third rail, return circuits, wayside storage, AC/DC traction systems |

Charging infrastructure is an explicit interface between transportation demand and distribution-network operation, and its planning/operation depends jointly on transportation and electrical conditions (Unterluggauer et al., 2022). Railway–power interdependency should retain traction-power infrastructure because traction substations mediate interaction between external power networks and railway operations (Bellè et al., 2022).

A representative physical state is

```math
x_P=[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC_B]^\top.
```

---

## 2. Transportation infrastructure system $T$

```math
T=T_R\cup T_B\cup T_U\cup T_H\cup T_M.
```

The transportation system is deliberately multimodal because power–transport interdependency is not limited to private EVs: road mobility interacts with charging and restoration logistics, while metro and railway systems interact directly with power networks through traction-power supply (Bellè et al., 2022; Sun et al., 2021).

| Subsystem | Framework-level content |
|---|---|
| $T_R$ — Road | links, intersections, traffic signals/flows, vehicles, EVs, shared mobility, charging access, emergency/repair routes |
| $T_B$ — Electric bus | buses, routes, depots, terminals, charging, schedules, fleet operations |
| $T_U$ — Urban rail | metro, MRT, subway, LRT, tram; trains, tracks, stations, signaling, traction interfaces, depots, schedules |
| $T_H$ — Regional/heavy electrified rail | commuter, suburban, regional, intercity, high-speed and relevant electrified freight rail |
| $T_M$ — Multimodal transfer | intermodal stations, transfer hubs, road–rail/bus–rail connections, alternative routes, passenger transfers, emergency substitution |

Power-dependent traffic signals and road accessibility provide explicit physical and functional links between transportation and electric-power systems (Fotouhi et al., 2017).

A representative state is

```math
x_T=[q,k,v,TT,A,SOC_{EV},s_{\rm rail}]^\top,
```

where $A$ captures accessibility and $s_{\rm rail}$ represents relevant rail operational states.

---

## 3. Information layer $I$

```math
I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_{\tau}.
```

Modern infrastructure operation combines physical assets with sensing, communication, computation, monitoring, and control; cyber-physical power systems provide a well-established example (Alvarez-Alvarado et al., 2024; Rinaldi et al., 2001).

| Subsystem | Framework-level content |
|---|---|
| $I_S$ — Sensing | SCADA, PMUs, meters, IEDs, feeder/substation sensors, traffic detectors, cameras, vehicle/bus/train telemetry |
| $I_C$ — Communication | utility WAN, SCADA/PMU/AMI networks, V2V/V2I/V2X, cellular/ITS, train-to-wayside and rail radio/fiber |
| $I_D$ — Data | databases, synchrophasor/AMI/traffic data, telemetry, charging data, event logs, APIs, streams, fusion |
| $I_E$ — Estimation support | power/traffic state information, topology/load/outage information, congestion/accessibility estimates, train localization |
| $I_A$ — Automation/signaling | EMS, DMS, SCADA logic, protection, DER/charging control, adaptive signals, route guidance, CBTC, ATP, ATO, ATS |
| $I_X$ — Cross-domain interoperability | EV-grid communication, smart charging, V2G exchange, power–transport APIs, traction energy management, energy–mobility coordination |
| $I_{\tau}$ — Timing/synchronization | timestamps, clock synchronization, GNSS/location, update timing, train positioning, measurement synchronization, information freshness |

Information freshness is distinct from conventional transmission latency. Age of Information provides an established framework for measuring freshness of received information (Yates et al., 2021).

A representative information state is

```math
z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top.
```

Conceptually,

```math
I:\quad
\text{SENSE}\rightarrow\text{COMMUNICATE}\rightarrow\text{ESTIMATE/SIGNAL}\rightarrow\text{KNOW}.
```

---

## 4. Organizational layer $O$

```math
O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K.
```

Infrastructure resilience is influenced not only by physical assets but also by organizational characteristics, managerial strategies, human actors, coordination structures, and resource availability (Mohebbi et al., 2020; Rasoulkhani & Mostafavi, 2018).

| Subsystem | Framework-level content |
|---|---|
| $O_A$ — Actors/responsibilities | utilities, grid/distribution operators, charging/traction operators, road/traffic/rail agencies, telecoms, emergency authorities, regulators, contractors, suppliers |
| $O_G$ — Governance | laws, regulations, contracts, policies, procedures, emergency plans, authority structures, restoration priorities |
| $O_D$ — Decision making | assessment, prioritization, intervention/repair/service decisions, centralized/decentralized/collaborative decisions |
| $O_C$ — Coordination | intra-/inter-agency coordination, power–transport coordination, emergency command, joint planning, information sharing |
| $O_R$ — Resources | repair crews, vehicles, equipment, spare parts, mobile generation, batteries, budgets, technical resources |
| $O_W$ — Workforce | engineers, operators, dispatchers, maintenance staff, specialists, training, expertise, availability |
| $O_L$ — Logistics/mobilization | crew dispatch, equipment deployment, staging, spare delivery, route selection, mobile-generation deployment |
| $O_M$ — Restoration management | inspection/repair priorities, crew assignment, restoration sequence/scheduling, critical-service priorities |
| $O_X$ — Cross-sector collaboration | power, transportation, communication, emergency and regulatory coordination |
| $O_K$ — Learning/adaptation | after-action learning, institutional memory, procedure updates, adaptive governance, lessons learned |

Transportation accessibility can constrain movement of repair crews and mobile energy resources and thereby alter power-system recovery (Li et al., 2022).

A representative organizational state is

```math
z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^{O},\tau_M]^\top.
```

Conceptually,

```math
O:\quad
\text{DECIDE}\rightarrow\text{COORDINATE}\rightarrow\text{RESOURCE}\rightarrow\text{MOBILIZE}.
```

---

## 5. Principal physical Power–Transportation couplings

The two physical systems interact through several interfaces, not one generic $P\leftrightarrow T$ arrow. Explicit coupling points and linking variables are established approaches in coupled transportation–power modeling (Fotouhi et al., 2017; Unterluggauer et al., 2022).

| Coupling chain | Physical interpretation |
|---|---|
| $P_D\leftrightarrow P_C\leftrightarrow T_R$ | road-EV charging, smart charging, V2G |
| $P_D\leftrightarrow P_C\leftrightarrow T_B$ | electric-bus charging |
| $P_{Tr/D}\leftrightarrow P_{TP}\leftrightarrow T_U$ | urban-rail traction power and regenerative braking |
| $P_{Tr}\leftrightarrow P_{TP}\leftrightarrow T_H$ | regional/heavy electrified rail |
| $T_R\rightarrow O_L\rightarrow P_D$ | road accessibility affecting repair-crew/mobile-resource deployment |

Railway–power models show that traction-power interfaces can transmit cascading consequences in both directions between railway and external power networks (Bellè et al., 2022). Transport accessibility can directly constrain repair-crew and mobile-resource deployment during distribution-system recovery (Li et al., 2022).

---

## 6. Structural observation and control interface

At framework level,

```math
X
\rightarrow y
\rightarrow I
\rightarrow\widehat X
\rightarrow O
\rightarrow u
\rightarrow X,
```

with

```math
X=
\begin{bmatrix}
x_P\\x_T
\end{bmatrix}.
```

The separation among physical infrastructure, informational functions, and human/organizational processes is consistent with cyber-physical-social infrastructure-resilience research (Alvarez-Alvarado et al., 2024; Mohebbi et al., 2020; Rinaldi et al., 2001). Estimator and policy design remain Stage-4 responsibilities.

---

# Stage 2 — Interdependency Mechanisms

## RQ2 / SO2 — current canonical question

> **Why and through which mechanisms do components and layers affect each other?**

**Specific objective:** Establish evidence-supported directional causal mechanisms, activation conditions, parameters, uncertainties and validity boundaries linking components and layers.

**Question authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`. This 2026-09-17 wording amendment aligns the question with Chapter I; technical results and validation status are unchanged.

Stage 2 starts from the Stage-1 ontology and adds causal transmission:

```math
\{P,T,I,O\}
\longrightarrow
\mathfrak I_{ij}^{\alpha\beta}.
```

Interdependency analysis requires more than identifying coexisting networks; it requires specifying the mechanism through which the state or operation of one infrastructure influences another (Ouyang, 2014; Rinaldi et al., 2001).

---

## 1. Complete directed scope

```math
\begin{aligned}
\mathcal I=\{&P\to T,\ T\to P,\ P\to I,\ I\to P,\ P\to O,\ O\to P,\\
&T\to I,\ I\to T,\ T\to O,\ O\to T,\ I\to O,\ O\to I\}.
\end{aligned}
```

Equivalently, the six bidirectional families are

```math
\begin{aligned}
&P\leftrightarrow T,
\qquad P\leftrightarrow I,
\qquad P\leftrightarrow O,\\
&T\leftrightarrow I,
\qquad T\leftrightarrow O,
\qquad I\leftrightarrow O.
\end{aligned}
```

The inclusion of physical, informational, and organizational directions is consistent with interdependency frameworks that distinguish physical/cyber dependencies and later cyber-physical-social research that integrates organizational characteristics (Mohebbi et al., 2020; Rinaldi et al., 2001).

---

## 2. Interdependency families and measurable effects

| Direction | Interdependencies in scope | Main measurable effect |
|---|---|---|
| $P\rightarrow T$ | EV/eBus charging, traffic signals, station power, metro/MRT/LRT and railway traction power | mobility capacity, train operation, charging availability (Bellè et al., 2022; Fotouhi et al., 2017; Unterluggauer et al., 2022) |
| $T\rightarrow P$ | repair-crew accessibility, equipment logistics, EV/V2G, regenerative braking, transport-dependent restoration | repair time, restoration, grid injection/load (Bellè et al., 2022; Li et al., 2022) |
| $P\rightarrow I$ | electricity supply to sensors, communication equipment, control centers, SCADA/ITS/rail control | information availability (Rinaldi et al., 2001) |
| $I\rightarrow P$ | measurements, SCADA, state estimation, protection information, DER/charging/traction control | observability, control accuracy, response delay (Alvarez-Alvarado et al., 2024) |
| $P\rightarrow O$ | outage severity, damaged assets, critical-service loss, restoration requirements | organizational workload and resource demand (Mohebbi et al., 2020) |
| $O\rightarrow P$ | switching, repair sequencing, crew allocation, DER dispatch, load restoration | power-state and recovery trajectory (Li et al., 2022; Mohebbi et al., 2020) |
| $T\rightarrow I$ | traffic states, accessibility, EV SOC, bus telemetry, train position/speed, service status | transport situational awareness (Mohebbi et al., 2020) |
| $I\rightarrow T$ | V2X, traffic control, routing, fleet control, CBTC, ATP, ATO, ATS | mobility operation and safety (Mohebbi et al., 2020) |
| $T\rightarrow O$ | congestion, blocked roads, inaccessible assets, rail disruption, logistics constraints | feasible response actions (Li et al., 2022) |
| $O\rightarrow T$ | road management, rerouting, dispatch, rail scheduling, emergency routing | transport-state/recovery trajectory (Mohebbi et al., 2020) |
| $I\rightarrow O$ | estimated state, alarms, forecasts, damage information, confidence, information freshness | decision quality and decision time (Mohebbi et al., 2020; Yates et al., 2021) |
| $O\rightarrow I$ | monitoring priorities, reporting rules, information sharing, communication priorities, access authority | information availability and flow (Mohebbi et al., 2020) |

The P–T mechanisms have particularly direct modeling precedents: Fotouhi et al. (2017) represent power-dependent traffic signals and coupled traffic–power resilience; Bellè et al. (2022) explicitly represent railway–traction–power dependency; and Li et al. (2022) represent road-constrained movement of repair crews and mobile energy resources during power-system restoration.

---

## 3. Subsystem-level decomposition

For a directed family such as $P\rightarrow T$,

```math
\mathcal I^{P\rightarrow T}
=
\bigcup_{p\in P}
\bigcup_{t\in T}
\mathcal I_{pt}^{P\rightarrow T}.
```

A component-level edge is retained only when a real causal mechanism exists. The same decomposition principle is applied to all 12 directions.

---

## 4. Canonical interdependency object

Every accepted interdependency is represented by

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,
E_j^\beta,
M_{ij},
w_{ij},
\delta_{ij},
\tau_{ij},
a_{ij},
m,
\mathcal H_t
\right).
```

This is a **proposed canonical thesis object**. It synthesizes established dimensions of heterogeneous, directional, and state-sensitive infrastructure dependency with the thesis requirements for explicit mechanism, strength, delay, timescale, activation, mode, and history (Danziger & Barabási, 2022; Ouyang, 2014; Rinaldi et al., 2001; Zhang & Peeta, 2014).

| Element | Meaning |
|---|---|
| $E_i^\alpha$ | source entity/component |
| $E_j^\beta$ | receiving entity/component |
| $M_{ij}$ | causal transmission mechanism |
| $w_{ij}$ | interdependency strength |
| $\delta_{ij}$ | cause-to-effect delay |
| $\tau_{ij}$ | characteristic mechanism timescale |
| $a_{ij}$ | activation state/condition |
| $m$ | system operating mode |
| $\mathcal H_t$ | relevant system/event history |

The minimum accepted representation is

```math
\text{Source}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Receiver}
\rightarrow
\text{Effect}.
```

---

## 5. Causal admissibility rule

Correlation, co-occurrence, co-location, or common exposure alone is insufficient. For example,

```math
h(\mathbf r,t)\rightarrow P_i,
\qquad
h(\mathbf r,t)\rightarrow T_j
```

does **not** by itself establish

```math
P_i\rightarrow T_j.
```

A retained Stage-2 edge requires evidence for a causal transmission mechanism:

```math
P_i\xrightarrow{M_{ij}}T_j,
```

or generally

```math
\alpha\xrightarrow{M_{ij}}\beta.
```

This is consistent with interdependency taxonomies that distinguish common/geographic exposure from a physical or cyber dependency in which the state of one system directly affects another (Ouyang, 2014; Rinaldi et al., 2001).

---

## 6. Position inside the seven-stage framework

The first five stages connect as

```math
\begin{aligned}
\{P,T,I,O\}
&\rightarrow \mathfrak I_{ij}^{\alpha\beta}
\rightarrow \{Y,\mathcal G,m,T_C\}\\
&\rightarrow \{\widehat X,\mathcal U,u,\tau_{\rm response}\}\\
&\rightarrow \{K_{\rm sus},\mathcal V,\partial\mathcal V,\rho,T_{\mathcal V},T_K\}.
\end{aligned}
```

**Bounded Stage-2 responsibility:** identify, classify, parameterize, and evidence causal interdependencies among $P$, $T$, $I$, and $O$; do not yet solve their full coupled dynamics. This boundary is consistent with the distinction between identifying interdependency structure/mechanisms and subsequently modeling dynamic evolution (Ouyang, 2014; Zhang & Peeta, 2014).

---

## 7. Freeze statement

Stage 2 remains frozen. Future Stage-2 diagrams, evidence tables, subsystem matrices, equations, simulations, and thesis text must remain consistent with the canonical specification unless an explicit versioned revision is approved.

---

# APA 7 reference list

References are alphabetized by first-author surname. Article titles use sentence case; journal titles and volume numbers are italicized; DOI identifiers are expressed as canonical `https://doi.org/...` URLs.

Alvarez-Alvarado, M. S., Apolo-Tinoco, C., Ramirez-Prado, M. J., Alban-Chacón, F. E., Pico, N., Aviles-Cedeno, J., Recalde, A. A., Moncayo-Rea, F., Velasquez, W., & Rengifo, J. (2024). Cyber-physical power systems: A comprehensive review about technologies drivers, standards, and future perspectives. *Computers & Electrical Engineering, 116*, 109149. https://doi.org/10.1016/j.compeleceng.2024.109149

Bellè, A., Zeng, Z., Duval, C., Sango, M., & Barros, A. (2022). Modeling and vulnerability analysis of interdependent railway and power networks: Application to British test systems. *Reliability Engineering & System Safety, 217*, 108091. https://doi.org/10.1016/j.ress.2021.108091

Danziger, M. M., & Barabási, A.-L. (2022). Recovery coupling in multilayer networks. *Nature Communications, 13*(1), Article 955. https://doi.org/10.1038/s41467-022-28379-5

Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026

Li, Z., Tang, W., Lian, X., Chen, X., Zhang, W., & Qian, T. (2022). A resilience-oriented two-stage recovery method for power distribution system considering transportation network. *International Journal of Electrical Power & Energy Systems, 135*, 107497. https://doi.org/10.1016/j.ijepes.2021.107497

Mohebbi, S., Zhang, Q., Christian Wells, E., Zhao, T., Nguyen, H., Li, M., Abdel-Mottaleb, N., Uddin, S., Lu, Q., Wakhungu, M. J., Wu, Z., Zhang, Y., Tuladhar, A., & Ou, X. (2020). Cyber-physical-social interdependencies and organizational resilience: A review of water, transportation, and cyber infrastructure systems and processes. *Sustainable Cities and Society, 62*, 102327. https://doi.org/10.1016/j.scs.2020.102327

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040

Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674

Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131

Sun, Y., Zhao, P., Wang, L., & Malik, S. M. (2021). Spatial and temporal modelling of coupled power and transportation systems: A comprehensive review. *Energy Conversion and Economics, 2*(2), 55–66. https://doi.org/10.1049/enc2.12034

Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. https://doi.org/10.1016/j.etran.2022.100163

Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. (2021). Age of information: An introduction and survey. *IEEE Journal on Selected Areas in Communications, 39*(5), 1183–1210. https://doi.org/10.1109/JSAC.2021.3065072

Zhang, P., & Peeta, S. (2014). Dynamic and disequilibrium analysis of interdependent infrastructure systems. *Transportation Research Part B: Methodological, 67*, 357–381. https://doi.org/10.1016/j.trb.2014.04.008

