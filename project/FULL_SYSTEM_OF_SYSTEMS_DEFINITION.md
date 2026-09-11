# Full P–T–I–O Framework-Level System Definition

> **Filename note:** `FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md` is retained for provenance. The current ontology contains two physical infrastructure systems ($P,T$) plus informational and organizational layers ($I,O$); it must not be read as four standalone infrastructure systems.

**Status:** CANONICAL FRAMEWORK-LEVEL DECOMPOSITION  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**System:** Power–Transportation–Information–Organization (P–T–I–O)  
**Rendering:** GitHub-compatible mathematics; long taxonomies use tables rather than oversized formulas

The framework-level system is

$$
\mathcal S=\{P,T,I,O\},
$$

with

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

The complete state is

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
$$

> **Canonical description:** A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.

---

## 1. Power infrastructure system $P$

The framework-level decomposition is

$$
P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP}.
$$

| Symbol | Subsystem | Representative content |
|---|---|---|
| $P_G$ | Generation | conventional generation, solar, wind, distributed generation |
| $P_{Tr}$ | Transmission | high-voltage buses, lines, bulk substations, transmission transformers |
| $P_D$ | Distribution | distribution substations, feeders, transformers, buses, LV/MV networks, critical loads |
| $P_{DER}$ | Distributed energy resources and storage | BESS, distributed PV, microgrids, local generation, flexible DERs |
| $P_C$ | Charging power infrastructure | EV chargers, fast chargers, bus-depot/opportunity chargers, converters, bidirectional charging, smart charging, V2G interfaces |
| $P_{TP}$ | Traction-power supply | traction substations/transformers, rectifiers, inverters, feeders, catenary, third rail, return circuits, wayside storage, AC/DC traction systems |

A representative power state is

$$
x_P=
[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC_B]^\top.
$$

---

## 2. Transportation infrastructure system $T$

The framework-level decomposition is

$$
T=T_R\cup T_B\cup T_U\cup T_H\cup T_M.
$$

| Symbol | Subsystem | Representative content |
|---|---|---|
| $T_R$ | Road transportation | links, intersections, signals, traffic flows, private vehicles, EVs, shared mobility, charging access, emergency routes, repair-crew routes |
| $T_B$ | Electric-bus transportation | buses, routes, depots, terminals, charging, scheduling, fleet operations |
| $T_U$ | Urban rail transit | metro, MRT, subway, LRT, tram, tracks, stations, signaling, traction interfaces, depots, operating schedules |
| $T_H$ | Regional/heavy electrified rail | commuter, suburban, regional, intercity, high-speed, and relevant electrified freight rail |
| $T_M$ | Multimodal/transfer system | intermodal stations, transfer hubs, road–rail and bus–rail connections, alternative routes, passenger transfers, emergency modal substitution |

A representative transportation state is

$$
x_T=
[q,k,v,TT,A,SOC_{EV},s_{\rm rail}]^\top,
$$

where $A$ denotes accessibility and $s_{\rm rail}$ denotes relevant rail operational states.

---

## 3. Information layer $I$

The framework-level decomposition is

$$
I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_{\tau}.
$$

| Symbol | Information function | Representative content |
|---|---|---|
| $I_S$ | Sensing and measurement | SCADA, PMUs, smart meters, IEDs, traffic detectors, cameras, vehicle/bus/train telemetry, traction and charging measurements |
| $I_C$ | Communication and networking | utility WAN, SCADA/PMU/AMI networks, V2V/V2I/V2X, cellular/ITS, train-to-wayside, rail radio/fiber |
| $I_D$ | Data acquisition and management | databases, synchrophasor/AMI/traffic streams, charging data, telemetry, event logs, APIs, data fusion |
| $I_E$ | Estimation support and situational information | state-estimation inputs/capability, topology/load/outage information, congestion/accessibility estimates, train localization |
| $I_A$ | Automation, signaling and control logic | EMS, DMS, SCADA logic, protection commands, DER/charging control, adaptive signals, route guidance, CBTC, ATP, ATO, ATS |
| $I_X$ | Cross-domain interoperability | EV-grid communication, smart charging, V2G exchange, power–transport APIs, traction energy management, energy–mobility coordination |
| $I_{\tau}$ | Timing, synchronization and positioning | timestamps, clock synchronization, GNSS/location, update timing, train positioning, measurement synchronization, information freshness |

The canonical information state is

$$
z_I=
[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top.
$$

The conceptual shorthand is

$$
I:\quad \text{SENSE}\rightarrow\text{COMMUNICATE}\rightarrow\text{ESTIMATE/SIGNAL}\rightarrow\text{KNOW}.
$$

Actual Stage-4 state estimation is not defined by this layer decomposition; it is represented separately as

$$
\widehat X(t)=\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
$$

---

## 4. Organizational layer $O$

The framework-level decomposition is

$$
O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K.
$$

| Symbol | Organizational function | Representative content |
|---|---|---|
| $O_A$ | Actors and responsibilities | utilities, grid/distribution operators, charging/traction operators, road/traffic/rail agencies, telecoms, emergency authorities, regulators, contractors, suppliers |
| $O_G$ | Governance and institutional rules | laws, regulations, contracts, policies, procedures, emergency plans, authority structures, restoration priorities |
| $O_D$ | Decision making | damage interpretation, prioritization, intervention selection, repair/service decisions, centralized/decentralized/collaborative decisions |
| $O_C$ | Coordination | intra-/inter-agency coordination, power–transport coordination, emergency command, joint planning, information sharing |
| $O_R$ | Resource allocation | crews, maintenance vehicles, equipment, spare parts, mobile generation, batteries, emergency vehicles, budgets |
| $O_W$ | Workforce capability | engineers, operators, dispatchers, maintenance staff, specialists, training, expertise, availability |
| $O_L$ | Logistics and mobilization | crew dispatch, equipment deployment, staging, spare-part delivery, route selection, mobile-generator deployment |
| $O_M$ | Restoration management | inspection/repair priorities, crew assignment, restoration sequence/scheduling, critical-service priorities |
| $O_X$ | Cross-sector collaboration | coordination among power, transportation, communication, emergency, regulatory, and contractor organizations |
| $O_K$ | Learning and adaptation | after-action learning, institutional memory, procedure updates, adaptive governance, lessons learned |

The organizational network may be represented as

$$
\mathcal G_O(t)=\bigl(V_O,E_O(t),W_O(t)\bigr).
$$

The canonical organizational state is

$$
z_O=
[A_O,C_O,R_O,W_O,\tau_D,\tau_C^{O},\tau_M]^\top.
$$

The conceptual shorthand is

$$
O:\quad \text{DECIDE}\rightarrow\text{COORDINATE}\rightarrow\text{RESOURCE}\rightarrow\text{MOBILIZE}.
$$

---

## 5. Principal physical Power–Transportation couplings

The two physical systems interact through several distinct interfaces rather than one generic $P\leftrightarrow T$ arrow.

| Physical interface | Principal mechanism |
|---|---|
| $P_D\leftrightarrow P_C\leftrightarrow T_R$ | EV charging, smart charging, V2G, charging availability |
| $P_D\leftrightarrow P_C\leftrightarrow T_B$ | depot/opportunity charging and electric-bus operations |
| $P_{Tr/D}\leftrightarrow P_{TP}\leftrightarrow T_U$ | urban-rail traction power and regenerative braking |
| $P_{Tr}\leftrightarrow P_{TP}\leftrightarrow T_H$ | regional/heavy-rail traction power |
| $T_R\rightarrow O_L\rightarrow P_D$ | road accessibility constraining crew and equipment movement for power restoration |

These are examples of Stage-2 mechanisms; they do not exhaust the full 12-direction P–T–I–O interdependency scope.

---

## 6. Observation–organization–control architecture

The physical systems and the informational/organizational layers interact through the Stage-4 feedback spine

$$
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow \widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t),
$$

where

$$
X(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix}.
$$

The current informational and organizational states constrain feasible intervention:

$$
u(t)
\in
\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

The layer labels $I$ and $O$ describe functions in the conceptual chain; their dynamic states remain $z_I(t)$ and $z_O(t)$.

---

## 7. Full architecture summary

| Layer/system | Canonical decomposition |
|---|---|
| $P$ | $\{P_G,P_{Tr},P_D,P_{DER},P_C,P_{TP}\}$ |
| $T$ | $\{T_R,T_B,T_U,T_H,T_M\}$ |
| $I$ | $\{I_S,I_C,I_D,I_E,I_A,I_X,I_{\tau}\}$ |
| $O$ | $\{O_A,O_G,O_D,O_C,O_R,O_W,O_L,O_M,O_X,O_K\}$ |

The global state remains

$$
Y(t)=[x_P(t),x_T(t),z_I(t),z_O(t)]^\top.
$$

The six bidirectional layer families are

$$
\begin{aligned}
&P\leftrightarrow T,
\qquad P\leftrightarrow I,
\qquad P\leftrightarrow O,\\
&T\leftrightarrow I,
\qquad T\leftrightarrow O,
\qquad I\leftrightarrow O.
\end{aligned}
$$

This file defines **what is contained in the system and layers**. Causal admissibility belongs to Stage 2, dynamic evolution to Stage 3, observation/control to Stage 4, and viability evaluation to Stage 5.
