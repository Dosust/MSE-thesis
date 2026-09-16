# Full P–T–I–O Framework-Level System Definition

> **Filename note:** `FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md` is retained for provenance. The current ontology contains two physical infrastructure systems ($P,T$) plus informational and organizational layers ($I,O$); it must not be read as four standalone infrastructure systems.

**Status:** CANONICAL FRAMEWORK-LEVEL DECOMPOSITION  
**Notation synchronization:** 2026-09-16  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**System:** Power–Transportation–Information–Organization (P–T–I–O)  
**Framework:** frozen Stages 1–7  
**Rendering:** GitHub-compatible mathematics; long taxonomies use tables rather than oversized formulas

The framework-level system is

```math
\mathcal S=\{P,T,I,O\},
```

with

```math
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
```

The complete state is

```math
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
```

> **Canonical description:** A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.

---

## 1. Power infrastructure system $P$

```math
P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP}.
```

| Symbol | Subsystem | Representative content |
|---|---|---|
| $P_G$ | Generation | conventional generation, solar, wind, distributed generation |
| $P_{Tr}$ | Transmission | high-voltage buses, lines, bulk substations, transmission transformers |
| $P_D$ | Distribution | distribution substations, feeders, transformers, buses, LV/MV networks, critical loads |
| $P_{DER}$ | Distributed energy resources and storage | BESS, distributed PV, microgrids, local generation, flexible DERs |
| $P_C$ | Charging power infrastructure | EV chargers, bus chargers, converters, bidirectional charging, smart charging, V2G interfaces |
| $P_{TP}$ | Traction-power supply | traction substations/transformers, rectifiers/inverters, feeders, catenary, third rail, return circuits, wayside storage |

A representative power state is

```math
x_P=[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC_B]^\top.
```

---

## 2. Transportation infrastructure system $T$

```math
T=T_R\cup T_B\cup T_U\cup T_H\cup T_M.
```

| Symbol | Subsystem | Representative content |
|---|---|---|
| $T_R$ | Road transportation | links, intersections, signals, traffic flows, private vehicles, EVs, shared mobility, emergency/repair routes |
| $T_B$ | Electric-bus transportation | buses, routes, depots, terminals, charging, scheduling, fleet operations |
| $T_U$ | Urban rail transit | metro/MRT/subway/LRT/tram, tracks, stations, signaling, traction interfaces, depots, schedules |
| $T_H$ | Regional/heavy electrified rail | commuter, regional, intercity, high-speed and relevant electrified freight rail |
| $T_M$ | Multimodal/transfer system | intermodal stations, transfer hubs, road–rail/bus–rail connections, alternative routes, passenger transfers |

A representative transportation state is

```math
x_T=[q,k,v,TT,A,SOC_{EV},s_{\rm rail}]^\top,
```

where $A$ denotes accessibility and $s_{\rm rail}$ relevant rail operational states.

---

## 3. Information layer $I$

```math
I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_{\tau}.
```

| Symbol | Information function | Representative content |
|---|---|---|
| $I_S$ | Sensing and measurement | SCADA, PMUs, smart meters, IEDs, traffic detectors, cameras, vehicle/bus/train telemetry |
| $I_C$ | Communication and networking | utility WAN, SCADA/PMU/AMI networks, V2V/V2I/V2X, cellular/ITS, rail radio/fiber |
| $I_D$ | Data acquisition and management | databases, data streams, charging data, telemetry, event logs, APIs, fusion |
| $I_E$ | Estimation support and situational information | state-estimation inputs, topology/outage information, congestion/accessibility estimates, train localization |
| $I_A$ | Automation/signaling/control logic | EMS/DMS/SCADA logic, protection commands, DER/charging control, adaptive signals, CBTC/ATP/ATO/ATS |
| $I_X$ | Cross-domain interoperability | EV-grid communication, smart charging, V2G exchange, power–transport APIs, energy–mobility coordination |
| $I_{\tau}$ | Timing/synchronization/positioning | timestamps, synchronization, GNSS/location, update timing, information freshness |

The canonical information state is

```math
z_I=[A_I,L_I,Q_I,\Delta_I,p_{\rm loss},e_X,\epsilon_{\rm sync}]^\top.
```

The conceptual shorthand is

```math
I:\quad
\text{SENSE}
\rightarrow\text{COMMUNICATE}
\rightarrow\text{ESTIMATE/SIGNAL}
\rightarrow\text{KNOW}.
```

Actual Stage-4 state estimation is represented separately by

```math
\widehat X(t)=\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
```

---

## 4. Organizational layer $O$

```math
O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K.
```

| Symbol | Organizational function | Representative content |
|---|---|---|
| $O_A$ | Actors/responsibilities | utilities, grid/distribution operators, charging/traction operators, road/traffic/rail agencies, telecoms, emergency authorities, regulators, contractors |
| $O_G$ | Governance/institutional rules | laws, regulations, contracts, procedures, emergency plans, authority structures, restoration priorities |
| $O_D$ | Decision making | damage interpretation, prioritization, intervention selection, repair/service decisions |
| $O_C$ | Coordination | intra-/inter-agency coordination, power–transport coordination, emergency command, information sharing |
| $O_R$ | Resource allocation | crews, maintenance vehicles, equipment, spare parts, mobile generation, batteries, budgets |
| $O_W$ | Workforce capability | engineers, operators, dispatchers, maintenance staff, specialists, training, availability |
| $O_L$ | Logistics/mobilization | crew dispatch, equipment deployment, staging, spare-part delivery, route selection |
| $O_M$ | Restoration management | inspection/repair priorities, crew assignment, restoration sequencing, critical-service priorities |
| $O_X$ | Cross-sector collaboration | coordination among power, transportation, communication, emergency, regulatory and contractor organizations |
| $O_K$ | Learning/adaptation | after-action learning, institutional memory, procedure updates, adaptive governance |

The organizational network may be represented as

```math
\mathcal G_O(t)=\bigl(V_O,E_O(t),W_O(t)\bigr).
```

The canonical organizational state is

```math
z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^O,\tau_M]^\top.
```

The conceptual shorthand is

```math
O:\quad
\text{DECIDE}
\rightarrow\text{COORDINATE}
\rightarrow\text{RESOURCE}
\rightarrow\text{MOBILIZE}.
```

---

## 5. Principal physical Power–Transportation couplings

The two physical systems interact through several distinct interfaces rather than one generic $P\leftrightarrow T$ arrow.

| Physical interface | Principal mechanism |
|---|---|
| $P_D\leftrightarrow P_C\leftrightarrow T_R$ | EV charging, smart charging, V2G, charging availability |
| $P_D\leftrightarrow P_C\leftrightarrow T_B$ | depot/opportunity charging and electric-bus operations |
| $P_{Tr/D}\leftrightarrow P_{TP}\leftrightarrow T_U$ | urban-rail traction power and regenerative braking |
| $P_{Tr}\leftrightarrow P_{TP}\leftrightarrow T_H$ | regional/heavy-rail traction power |
| $T_R\rightarrow O_L\rightarrow P_D$ | road accessibility constraining crew/equipment movement for power restoration |

These are examples of Stage-2 mechanisms; they do not exhaust the full 12-direction P–T–I–O interdependency scope. Each accepted directed relation is encoded by

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e),
\qquad
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e),
```

and the active set is

```math
\mathbb I(t)=\{\mathfrak d_e(t):e\in\mathcal E(t)\}.
```

---

## 6. Observation–organization–control architecture

```math
X(t)
\rightarrow y(t)
\rightarrow I(t)
\rightarrow\widehat X(t)
\rightarrow O(t)
\rightarrow u(t)
\rightarrow X(t),
```

where

```math
X(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)
\end{bmatrix}.
```

The current informational and organizational states constrain feasible operational control:

```math
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
```

The labels $I,O$ describe layer functions; the dynamic states remain $z_I(t),z_O(t)$.

---

## 7. Complete layer/system summary

| Layer/system | Canonical decomposition |
|---|---|
| $P$ | $\{P_G,P_{Tr},P_D,P_{DER},P_C,P_{TP}\}$ |
| $T$ | $\{T_R,T_B,T_U,T_H,T_M\}$ |
| $I$ | $\{I_S,I_C,I_D,I_E,I_A,I_X,I_{\tau}\}$ |
| $O$ | $\{O_A,O_G,O_D,O_C,O_R,O_W,O_L,O_M,O_X,O_K\}$ |

The six bidirectional layer families are

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

---

## 8. Stage-6 regime interpretation

Stage 6 evaluates whether preserving the current regime remains adequate. The current regime is

```math
\mathfrak M_0
=
(\mathcal S,\mathcal G,\mathbb I,F,\Theta,K_{\rm sus},\mathcal U).
```

The Stage-6 translation is

```math
\Phi_{\rm ST}
:
(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto
(c_6,\mathcal D_6,\boldsymbol\zeta_T).
```

This specifies why change is required, what must change and how deep the change must be.

---

## 9. Stage-7 regime transformation

A future candidate regime uses the same object class:

```math
\mathfrak M_k
=
(\mathcal S_k,\mathcal G_k,\mathbb I_k,F_k,\Theta_k,K_{{\rm sus},k},\mathcal U_k).
```

Stage-7 strategic transformation is

```math
\mathfrak M_{k+1}
=
\mathcal T_{\mathbf a_k}(\mathfrak M_k,\xi_k),
```

where

```math
\mathbf a_k
=
[a_k^P,a_k^T,a_k^I,a_k^O,a_k^{\mathbb I}]^\top.
```

The action hierarchy is mandatory:

```math
\underbrace{u(t)}_{\text{Stage-4 operational control}}
\neq
\underbrace{\mathbf a_k}_{\text{Stage-7 strategic transformation}}
\neq
\underbrace{\gamma_e}_{\text{Stage-2 dependency activation guard}}.
```

The terminal Stage-7 object is

```math
\mathfrak P_{\rm ST}
=
(\mathbb G_{\rm ST},\boldsymbol\pi_{\rm ST},\Omega,\mathcal A^{\rm feas},\mathbf J,\mathbb M_{\rm sus}).
```

---

## 10. Cross-stage responsibility

This file defines **what is contained in $P,T,I,O$**. The seven-stage responsibilities are:

| Stage | Responsibility |
|---:|---|
| **1** | system/layer composition and structure |
| **2** | causal admissibility and mechanism specification |
| **3** | hybrid/multiscale dynamic evolution |
| **4** | observation, organizational feasibility and operational control |
| **5** | controlled sustainable viability |
| **6** | long-horizon regime-adequacy diagnosis |
| **7** | adaptive strategic transformation pathways |

Subsystem lists in this file therefore do not, by themselves, establish causal interdependency, dynamics, viability or transformation value; those must be demonstrated in their corresponding stages.
