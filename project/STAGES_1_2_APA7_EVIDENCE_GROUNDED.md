# Stages 1–2 — APA 7 Evidence-Grounded Canonical Specification

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**System:** Power–Transportation–Information–Organization (P–T–I–O)  
**Status:** Canonical evidence-grounded companion to Stages 1 and 2  
**Citation standard:** APA 7th edition author–date  
**Updated:** 2026-09-11

> **Scope rule:** This document preserves the current Stage-1 system ontology and the frozen Stage-2 interdependency scope. It adds literature grounding and APA 7 citations; it does not alter the seven-stage framework. The thesis remains at framework level here; no separate implementation-level subsection is included.

> **Evidence rule:** Citations support the specific claims to which they are attached. The complete thesis interdependency tuple is a thesis synthesis and is not attributed to any single source.

---

# Stage 1 — System Ontology and Multilayer Structure

## Research question

$$
\boxed{\textbf{What entities exist, what layers constitute the system, and where can interactions occur?}}
$$

The System of Systems is

$$
\boxed{\mathcal S=\{P,T,I,O\}}.
$$

We study a

$$
\boxed{\textbf{Multilayer Physical–Informational–Organizational Interdependent Infrastructure System}}
$$

with

$$
\boxed{\underbrace{P,T}_{\text{physical infrastructure systems}}\qquad\underbrace{I,O}_{\text{informational and organizational layers}}}.
$$

Critical infrastructures can be mutually dependent through physical, cyber/informational, geographic, logical, and organizational relationships; consequently, interdependent infrastructure cannot be represented adequately as isolated physical networks alone (Mohebbi et al., 2020; Ouyang, 2014; Rinaldi et al., 2001).

The framework-level system state is

$$
\boxed{
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}
}.
$$

## 1. Power system $P$

$$
\boxed{P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP}}.
$$

The scope includes conventional electricity infrastructure together with charging and traction-power interfaces because transportation electrification creates interactions across distribution networks, charging infrastructure, and railway traction-power systems (Bellè et al., 2022; Sun et al., 2021; Unterluggauer et al., 2022).

| Subsystem | Framework-level content |
|---|---|
| $P_G$ — Generation | conventional generation, solar, wind, distributed generation |
| $P_{Tr}$ — Transmission | high-voltage buses, lines, bulk substations, transformers |
| $P_D$ — Distribution | substations, feeders, transformers, buses, LV/MV networks, critical loads |
| $P_{DER}$ — DER/storage | BESS, distributed PV, microgrids, local generation, flexible DERs |
| $P_C$ — Charging | EV chargers, fast chargers, bus-depot/opportunity chargers, converters, bidirectional charging, smart charging, V2G interfaces |
| $P_{TP}$ — Traction power | traction substations/transformers, rectifiers, inverters, feeders, catenary, third rail, return circuits, wayside storage, AC/DC traction systems |

Charging infrastructure forms an explicit interface between transportation demand and distribution-network operation, and its planning and operation depend jointly on transportation and electrical conditions (Unterluggauer et al., 2022). Railway–power interdependency should explicitly retain traction-power infrastructure because traction substations mediate interaction between external power networks and railway operations (Bellè et al., 2022).

A representative physical state is

$$
\boxed{x_P=[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC]^{\top}}.
$$

## 2. Transportation system $T$

$$
\boxed{T=T_R\cup T_B\cup T_U\cup T_H\cup T_M}.
$$

The transportation layer is deliberately multimodal because power–transport interdependency is not limited to private EVs: road mobility interacts with charging and restoration logistics, while metro and railway systems interact directly with power networks through traction-power supply (Bellè et al., 2022; Sun et al., 2021).

| Subsystem | Framework-level content |
|---|---|
| $T_R$ — Road | links, intersections, traffic signals/flows, vehicles, EVs, shared mobility, charging access, emergency/repair routes |
| $T_B$ — Electric bus | buses, routes, depots, terminals, charging, schedules, fleet operations |
| $T_U$ — Urban rail | Metro, MRT, Subway, LRT, Tram; trains, tracks, stations, signaling, traction interfaces, depots, schedules |
| $T_H$ — Regional/heavy electrified rail | commuter, suburban, regional, intercity, high-speed and relevant electrified freight rail |
| $T_M$ — Multimodal transfer | intermodal stations, transfer hubs, road–rail/bus–rail connections, alternative routes, passenger transfers, emergency substitution |

Power-dependent traffic signals and road accessibility provide explicit physical and functional links between transportation and electric-power systems (Fotouhi et al., 2017).

A representative state is

$$
\boxed{x_T=[q,k,v,TT,A,SOC_{EV},s_{\rm rail}]^{\top}},
$$

where $A$ captures accessibility and $s_{\rm rail}$ represents relevant rail operational states.

## 3. Information layer $I$

$$
\boxed{I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_{\tau}}.
$$

Modern infrastructure operation increasingly combines physical infrastructure with sensing, communication, computation, monitoring, and control; cyber-physical power systems provide a well-established example of this integration (Alvarez-Alvarado et al., 2024; Rinaldi et al., 2001).

| Subsystem | Framework-level content |
|---|---|
| $I_S$ — Sensing | SCADA, PMUs, meters, IEDs, feeder/substation sensors, traffic detectors, cameras, vehicle/bus/train telemetry |
| $I_C$ — Communication | utility WAN, SCADA/PMU/AMI networks, V2V/V2I/V2X, cellular/ITS, train-to-wayside and rail radio/fiber |
| $I_D$ — Data | databases, synchrophasor/AMI/traffic data, telemetry, charging data, event logs, APIs, streams, fusion |
| $I_E$ — Estimation | power/traffic state estimation, topology/load estimation, outage/congestion/accessibility estimation, train localization |
| $I_A$ — Automation/signaling | EMS, DMS, SCADA logic, protection, DER/charging control, adaptive signals, route guidance, CBTC, ATP, ATO, ATS |
| $I_X$ — Cross-domain interoperability | EV-grid communication, smart charging, V2G exchange, power–transport APIs, traction energy management, energy–mobility coordination |
| $I_{\tau}$ — Timing/synchronization | timestamps, clock synchronization, GNSS/location, update timing, train positioning, measurement synchronization, information freshness |

Information freshness is distinct from conventional transmission latency. Age of Information provides an established framework for measuring freshness of received information (Yates et al., 2021).

A representative information state is

$$
\boxed{z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^{\top}}.
$$

Conceptually,

$$
\boxed{I=\text{SENSE + COMMUNICATE + ESTIMATE + SIGNAL}=\textbf{KNOW}}.
$$

## 4. Organizational layer $O$

$$
\boxed{O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K}.
$$

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

$$
\boxed{z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^{O},\tau_M]^{\top}}.
$$

Conceptually,

$$
\boxed{O=\text{DECIDE + COORDINATE + RESOURCE + MOBILIZE}}.
$$

## 5. Physical Power–Transportation coupling

The two physical systems interact through several interfaces, not one generic $P\leftrightarrow T$ arrow. Explicit coupling points and linking variables are established approaches in coupled transportation–power modeling (Fotouhi et al., 2017; Unterluggauer et al., 2022).

$$
P_D\leftrightarrow P_C\leftrightarrow T_R
$$

for road EV charging, smart charging and V2G;

$$
P_D\leftrightarrow P_C\leftrightarrow T_B
$$

for electric-bus charging;

$$
P_{Tr/D}\leftrightarrow P_{TP}\leftrightarrow T_U
$$

for Metro/MRT/Subway/LRT/Tram traction power and regenerative braking; and

$$
P_{Tr}\leftrightarrow P_{TP}\leftrightarrow T_H
$$

for regional/heavy electrified rail. Railway–power models demonstrate that traction-power interfaces can transmit cascading consequences in both directions between railway and external power networks (Bellè et al., 2022).

A restoration dependency is

$$
\boxed{T\rightarrow\text{crew accessibility}\rightarrow\text{power restoration}},
$$

because transport-network accessibility can directly constrain repair-crew and mobile-resource deployment during distribution-system recovery (Li et al., 2022).

## 6. Structural cognitive and control interfaces

At framework level, the four layers connect through

$$
\boxed{X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X},
$$

with

$$
X=\begin{bmatrix}x_P\\x_T\end{bmatrix},\qquad I=\textbf{KNOW},\qquad O=\textbf{DECIDE/COORDINATE/MOBILIZE},\qquad u=\textbf{ACT}.
$$

The separation between physical infrastructure, cyber/information functions, and human/organizational processes is consistent with cyber-physical-social infrastructure-resilience research (Alvarez-Alvarado et al., 2024; Mohebbi et al., 2020; Rinaldi et al., 2001). Observer and policy design remain Stage 4 responsibilities.

---

# Stage 2 — Interdependency Mechanisms

## Research question

$$
\boxed{\textbf{Why and through which mechanisms do components and layers affect each other?}}
$$

## 1. Stage role

$$
\boxed{\text{Stage 1 defines }P,T,I,O\quad\Longrightarrow\quad\text{Stage 2 defines how }P,T,I,O\text{ causally affect one another}}.
$$

Interdependency analysis requires more than identifying coexisting infrastructure networks: it requires specifying the mechanism through which the state or operation of one infrastructure influences another (Ouyang, 2014; Rinaldi et al., 2001).

## 2. Complete directed scope

$$
\boxed{
\mathcal I=\{
P\to T,T\to P,
P\to I,I\to P,
P\to O,O\to P,
T\to I,I\to T,
T\to O,O\to T,
I\to O,O\to I
\}}
$$

or, equivalently, six bidirectional families:

$$
\boxed{
P\leftrightarrow T,\quad
P\leftrightarrow I,\quad
P\leftrightarrow O,\quad
T\leftrightarrow I,\quad
T\leftrightarrow O,\quad
I\leftrightarrow O
}.
$$

The inclusion of physical, informational, and organizational directions is consistent with infrastructure-interdependency frameworks that distinguish physical and cyber dependencies and with later cyber-physical-social research integrating organizational characteristics (Mohebbi et al., 2020; Rinaldi et al., 2001).

## 3. Interdependency families and measurable effects

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

The P–T mechanisms have particularly direct modeling precedents. Fotouhi et al. (2017) represented power-dependent traffic signals and coupled traffic–power resilience; Bellè et al. (2022) explicitly represented railway–traction–power dependency; and Li et al. (2022) represented road-constrained movement of repair crews and mobile energy resources during power-system restoration.

## 4. Subsystem-level decomposition

For each directed family,

$$
\boxed{\mathcal I^{P\rightarrow T}=\bigcup_{p\in P}\bigcup_{t\in T}\mathcal I_{pt}^{P\rightarrow T}}.
$$

An edge is included only when a real causal mechanism exists. Examples include

$$
P_D\rightarrow P_C\rightarrow T_R
$$

for EV charging (Unterluggauer et al., 2022),

$$
P_D\rightarrow P_C\rightarrow T_B
$$

for electric-bus charging,

$$
P_{Tr/D}\rightarrow P_{TP}\rightarrow T_U
$$

for Metro/MRT traction (Bellè et al., 2022),

$$
P_{Tr}\rightarrow P_{TP}\rightarrow T_H
$$

for heavy/intercity rail (Bellè et al., 2022), and

$$
T_R\rightarrow O_L\rightarrow P_D
$$

for road accessibility affecting power repair (Li et al., 2022).

The same subsystem-to-subsystem decomposition is to be developed for all 12 directions.

## 5. Canonical interdependency object

Every accepted interdependency is represented by

$$
\boxed{
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
\right)
}.
$$

This is the **proposed canonical object of this thesis**. It synthesizes established dimensions of infrastructure interdependency with the thesis requirements for explicit causal mechanism, strength, delay, activation, mode, timescale, and history. Existing literature supports representing infrastructure dependencies as heterogeneous, directional, and state-sensitive relationships, while dynamic studies show that interdependency behavior can vary over time and across disruption and recovery conditions (Danziger & Barabási, 2022; Ouyang, 2014; Rinaldi et al., 2001; Zhang & Peeta, 2014).

The minimum accepted causal representation is

$$
\boxed{\text{Source}\rightarrow\text{Mechanism}\rightarrow\text{Receiver}\rightarrow\text{Effect}}.
$$

Each accepted relation must characterize its strength $w$, delay $\delta$, characteristic timescale $\tau$, activation $a$, mode $m$, and relevant history $\mathcal H_t$. The complete tuple is a thesis synthesis and is not attributed to any single cited paper.

## 6. Causal admissibility rule

$$
\boxed{\text{same hazard affects }P\text{ and }T\;\not\Rightarrow\;P\leftrightarrow T}.
$$

Correlation, co-occurrence, co-location, or common exposure alone is insufficient. An accepted interdependency requires a causal transmission mechanism:

$$
\boxed{\alpha\xrightarrow{M_{ij}}\beta}.
$$

This distinction is consistent with established infrastructure-interdependency taxonomies in which geographic co-location is conceptually different from a physical or cyber dependency in which the state of one system directly affects another (Ouyang, 2014; Rinaldi et al., 2001).

Thus,

$$
h(\mathbf r,t)\rightarrow P_i,\qquad h(\mathbf r,t)\rightarrow T_j
$$

does not itself establish

$$
P_i\rightarrow T_j.
$$

A Stage-2 edge requires evidence for

$$
\boxed{P_i\xrightarrow{M_{ij}}T_j}.
$$

## 7. Position inside the seven-stage framework

$$
\boxed{
\underbrace{\{P,T,I,O\}}_{\text{Stage 1: system}}
\rightarrow
\underbrace{\mathcal I^{\alpha\beta}}_{\text{Stage 2: interdependencies}}
\rightarrow
\underbrace{F(Y,\ldots)}_{\text{Stage 3: dynamics}}
\rightarrow
\underbrace{I\rightarrow O\rightarrow u}_{\text{Stage 4}}
\rightarrow
\underbrace{\mathcal V_{\rm sus}^{u}}_{\text{Stage 5}}
\rightarrow
\underbrace{\text{Stages 6--7}}_{\text{transition and transformation}}
}.
$$

**Bounded scientific responsibility of Stage 2:** identify, classify, parameterize, and evidence the causal interdependencies among $P$, $T$, $I$, and $O$; do not yet solve their full coupled dynamics. This boundary is methodologically consistent with the distinction between identifying interdependency structure/mechanisms and subsequently modeling their dynamic evolution (Ouyang, 2014; Zhang & Peeta, 2014).

## 8. Freeze statement

Stage 2 remains frozen. Future Stage-2 diagrams, evidence tables, subsystem matrices, equations, simulations, and thesis text must remain consistent with the canonical specification unless an explicit versioned revision is approved.

The first-two-stage logic is

$$
\boxed{
\underbrace{\{P,T,I,O\}}_{\textbf{Stage 1: what exists / where interaction can occur}}
\rightarrow
\underbrace{\mathfrak I_{ij}^{\alpha\beta}}_{\textbf{Stage 2: why / through what mechanism an effect occurs}}
}.
$$

Stage 3 receives these objects without redefining them.

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
