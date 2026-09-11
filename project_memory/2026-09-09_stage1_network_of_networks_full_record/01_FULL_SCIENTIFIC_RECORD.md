# Full Scientific Record - Stage 1 Multilayer Network-of-Networks

## 0. Position inside the canonical seven-stage framework

The thesis framework remains:

```math
\boxed{
\text{Multilayer Structure}
\to
\text{Causal Mechanisms}
\to
\text{Coupled Hybrid Multiscale Dynamics}
\to
\text{Feedback \& Control}
\to
\text{Viability}
\to
\text{Resilience-to-Sustainability Transformation Interface}
\to
\text{Sustainable Transformation Pathways}
}
```

Stage 1 answers **What exists?** It must build the structural model and baseline state without prematurely mixing in hazard forcing, event causality, hybrid dynamics, control, viability, or sustainability evaluation.

The simulation-ready Stage-1 output is therefore the pair:

```math
\boxed{(\mathfrak N_1,Y_0)}
```

where `\mathfrak N_1` is the structural network-of-networks model and `Y_0` is the initial dynamic state.

---

# 1. System boundary

For the present thesis, the recommended system is:

```math
\boxed{\mathscr S=\{\mathcal P,\mathcal T,\mathcal I,\mathcal O\}}
```

with:

```math
\mathcal P=\text{urban/distribution electricity system}
```

```math
\mathcal T=\text{road-traffic-EV mobility system}
```

```math
\mathcal I=\text{observation/communication/information system}
```

```math
\mathcal O=\text{organizational decision/resource system}.
```

The bulk transmission system should normally be represented as an upstream supply boundary rather than modeled at the same resolution as the urban distribution grid. NIST's Smart Grid Conceptual Model distinguishes generation/DER, transmission, distribution, customer, operations, markets and service-provider domains; the proposed thesis abstraction retains the distribution-level components through which urban power-transport interactions are most directly realized (Gopstein et al., 2021).

A core conceptual rule is that Power and Transportation are definite physical network layers. Information and Organization become explicit graph layers only if their own internal topology is represented. Otherwise they remain explicit interacting subsystems/states. This is consistent with cyber-physical systems thinking, which distinguishes physical, computational, communication, sensing, actuation and human components rather than forcing them into one homogeneous graph (Griffor et al., 2017).

---

# 2. Node, link, interface asset, agent, state, and parameter

The network-of-networks must distinguish six object types:

```math
\boxed{
\text{Node}
\neq
\text{Link}
\neq
\text{Interface asset}
\neq
\text{Agent}
\neq
\text{Dynamic state}
\neq
\text{Parameter}
}
```

## 2.1 Node

A node is a fixed topological junction, injection/withdrawal location, observation point, or decision entity. Examples include an electrical bus, a road junction, a control center, or an institutional actor.

## 2.2 Link

A link primarily transfers a physical, informational, or organizational quantity between nodes. Examples include a feeder, road segment, communication channel, authority relation, or task-assignment relation.

## 2.3 Interface asset

An interface asset converts or transfers service between different systems. The most important example is an EV charging station, which couples the road-mobility and electric-power systems.

## 2.4 Agent

An agent moves, decides, or acts on a network without defining the fixed physical topology. EVs, repair crews, mobile energy storage, and mobile generators should generally be treated as agents/resources rather than fixed network nodes.

## 2.5 Dynamic state

A state changes during simulation, e.g. voltage, power flow, road speed, travel time, information latency, resource availability, or interface availability.

## 2.6 Parameter

A parameter describes fixed or slowly varying model properties such as electrical impedance, line rating, road length, nominal capacity, equipment efficiency, or a policy rule. MATPOWER's network-model architecture is a useful precedent: buses provide network connection nodes; branch elements connect nodes; loads and generators attach through ports; ratings and impedances are parameters distinct from solved operating states (MATPOWER, 2026).

---

# 3. Power subsystem

## 3.1 Recommended internal decomposition

```text
P0  Upstream supply boundary
P1  Substations / transformers / buses
P2  Distribution feeders / cables / branches
P3  Protection and switching
P4  DER and stationary storage
P5  Loads and critical services
P6  Power-transport electrical interface ports
```

NIST's Smart Grid framework supports distinguishing distribution, DER/storage, customers/loads, operations, protection and control functions (Gopstein et al., 2021).

## 3.2 Graph representation

The electrical topology should be based primarily on electrical buses:

```math
\boxed{\mathcal G_P=(V_P,E_P)}
```

with:

```math
V_P=V_{\mathrm{bus}}
```

and:

```math
E_P=E_{\mathrm{line}}\cup E_{\mathrm{transformer}}\cup E_{\mathrm{switchable\ branch}}.
```

Generators, loads, DER, BESS, hospitals and charging facilities are normally devices connected to buses through ports rather than independent electrical-topology nodes.

## 3.3 Power state

A flexible state specification is:

```math
\boxed{
X_P(t)=
[\mathbf s_P(t),\mathbf V(t),\boldsymbol\theta(t),\mathbf P(t),\mathbf Q(t),
\mathbf L_{\mathrm{served}}(t),\mathbf E_{\mathrm{storage}}(t)]^\top
}
```

while fixed electrical properties remain in:

```math
\boxed{
\Theta_P=[R,X,\bar V,\bar S,\bar P,\eta,\ldots].
}
```

Therefore:

```math
\boxed{\text{equipment capacity/rating}\rightarrow\Theta_P,
\qquad
\text{actual operating condition}\rightarrow X_P(t).}
```

## 3.4 Service outputs

The layer should expose service variables such as:

```math
Q_P(t)=\frac{L_{\mathrm{served}}(t)}{L_{\mathrm{required}}(t)}
```

or spatially disaggregated load-service ratios by zone or critical facility. These will later feed Stage 5 viability and Stage 6 sustainability translation.

---

# 4. Transportation subsystem

## 4.1 Recommended internal decomposition

```text
T1  Road topology
T2  Traffic state
T3  Traffic-control assets
T4  EV / mobility fleet
T5  Critical-access routes
T6  Depots and critical destinations
T7  Electrified public transit - optional if justified by case data
```

FHWA transportation-systems management and operations practice treats traffic flow, signals, incidents, traveler information, multimodal mobility, freight and emergency operations as interacting operational functions. SUMO represents the road system as a directed graph and supports microscopic vehicle behavior and aggregated link states (FHWA, 2019; SUMO, 2026).

## 4.2 Graph representation

```math
\boxed{\mathcal G_T=(V_T,E_T)}
```

with:

```math
V_T=V_{\mathrm{junction}}\cup V_{\mathrm{OD}}\cup V_{\mathrm{critical\ access}}
```

and:

```math
E_T=E_{\mathrm{road}}.
```

A directed road edge may have:

```math
\theta_{ij}^T=[L_{ij},N_{lane},v_{ij}^{max},q_{ij}^{max},\ldots].
```

## 4.3 Macroscopic traffic state

If using a macroscopic traffic formulation:

```math
\boxed{
X_T^{macro}(t)=
[\boldsymbol\rho(t),\mathbf q(t),\mathbf v(t),\mathbf{TT}(t),\mathbf a(t),\mathbf s_T(t)].
}
```

## 4.4 Microscopic traffic state

If using SUMO or another microscopic model:

```math
\boxed{
X_T^{micro}(t)=
[x_v(t),v_v(t),r_v(t),SOC_v(t)]_{v\in\mathcal V_{veh}}.
}
```

The two levels must be connected through explicit aggregation rather than silently mixed.

## 4.5 Mobile agents

EVs, repair crews, mobile generators and mobile energy storage move on `\mathcal G_T` and should normally be represented as agents/resources:

```math
\boxed{
a_v(t)=[location_v(t),route_v(t),SOC_v(t),destination_v(t),status_v(t)].
}
```

---

# 5. Information subsystem

The information system is needed to model what operators can observe, how quickly they receive it, and how commands reach physical assets.

## 5.1 Recommended internal decomposition

```text
I1  Sensing and measurement
I2  Communication network/pathways
I3  Data integration and telemetry
I4  Observability/state information
I5  Command pathways
I6  ICT support state - availability, latency, backup power, redundancy
```

NIST's Cyber-Physical Systems framework explicitly integrates sensing, communication, computation, actuation, physical processes and humans (Griffor et al., 2017). Mohamed (2019) provides direct infrastructure evidence by explicitly representing power, ICT and e-mobility interdependencies.

## 5.2 Optional graph representation

When communication topology is explicitly modeled:

```math
\boxed{\mathcal G_I=(V_I,E_I)}
```

with:

```math
V_I=
V_{sensor}\cup
V_{IED/RTU}\cup
V_{gateway/router}\cup
V_{control/data\ center}
```

and:

```math
E_I=
E_{telemetry}\cup
E_{communication}\cup
E_{command}.
```

Otherwise, preserve Information as an explicit subsystem without pretending its topology is known.

## 5.3 Information state

```math
\boxed{
I(t)=[\mathbf a_I(t),\boldsymbol\ell_I(t),\mathbf q_I(t),\mathbf c_I(t)]
}
```

where availability, latency, quality and completeness/observability are dynamic quantities.

The structural observation mapping is established in Stage 1:

```math
\boxed{y=H_{obs}(Y)}
```

while noise, delay and state estimation belong to Stage 4:

```math
y(t)=H_{obs}[Y(t-\tau_I)]+\varepsilon(t),
\qquad
\hat Y(t)=\mathcal E[y(t)].
```

---

# 6. Organizational subsystem

Organization must represent the capability to interpret information, coordinate actors, mobilize resources and modify physical-system trajectories.

## 6.1 Recommended internal decomposition

```text
O1  Actors and institutions
O2  Authority and responsibility
O3  Workforce and recovery resources
O4  Plans, rules and procedures
O5  Coordination and interagency relationships
O6  Financial and material capacity
O7  Knowledge, interdependency awareness and learning
```

Rasoulkhani and Mostafavi (2018) conceptualize resilience as emerging from coupled human-infrastructure dynamics. Dong et al. (2020) identify coordinated actor networks and integrated plans/policies as important components of institutional connectedness. Recent organizational-resilience modeling additionally identifies communication, financial resources, situational awareness, structural-interdependency knowledge and learning as dynamic contributors to resilience.

## 6.2 Organizational graph

When actor-to-actor structure is explicitly modeled:

```math
\boxed{\mathcal G_O=(V_O,E_O)}
```

where nodes are decision-capable actors rather than buildings:

```math
V_O=
\{\text{utility operations},\text{distribution operator},\text{DOT/TMC},
\text{emergency management},\text{EV/fleet operator},\text{repair crews}\}.
```

Links may be typed as:

```math
E_O=
E_{authority}\cup
E_{coordination}\cup
E_{task}\cup
E_{resource}\cup
E_{information-sharing}.
```

## 6.3 Organizational state

```math
\boxed{
O(t)=[R_O(t),W_O(t),C_O(t),D_O(t),F_O(t),K_O(t)]^\top
}
```

representing resources, workforce, coordination, decision capability/delay, financial capacity and knowledge.

The static organizational architecture and dynamic organizational state are different objects:

```math
\boxed{\mathcal G_O\neq O(t)}
```

just as:

```math
\boxed{\mathcal G_P\neq X_P(t).}
```

## 6.4 Rule overlay

Yu et al. (2025) argue that logical/institutional infrastructure interdependencies can be operationalized through human decisions and formal/informal rules. This supports an optional rule graph or hypergraph:

```math
\boxed{\mathcal G_R=(V_A\cup V_R\cup V_{infra},E_R)}
```

where actor, rule/task and infrastructure objects are linked explicitly.

---

# 7. Interface assets and ports

## 7.1 EV charging stations

An EV charging station should not be duplicated as separate unrelated power and transport nodes.

Define a single interface object:

```math
\boxed{c_k^{EVCS}=(\pi_k^P,\pi_k^T,X_k^C,\Theta_k^C)}
```

with:

```math
\pi_k^P\to b(k)\in V_P,
\qquad
\pi_k^T\to n(k)\in V_T.
```

The electrical side carries quantities such as charging power and V2G injection:

```math
P_k^{ch}(t),\qquad P_k^{V2G}(t),
```

while the mobility side carries arrival rate, number of EVs, queueing time and SOC distribution:

```math
\lambda_k(t),\quad N_k^{EV}(t),\quad T_k^{queue}(t),\quad SOC_k(t).
```

Coupled power-transport literature explicitly treats charging facilities as coupling elements between distribution and transportation systems (Fotouhi et al., 2017; Mohamed, 2019; later coupled EV studies).

## 7.2 General port formulation

For subsystem `\alpha`:

```math
\boxed{\mathcal S_\alpha=(\mathcal A_\alpha,X_\alpha,\Theta_\alpha,\Pi_\alpha)}
```

where `\Pi_\alpha` is the set of external interface ports.

A cross-system dependency is then:

```math
\boxed{e_{ij}^{\alpha\beta}:\pi_i^\alpha\rightarrow\pi_j^\beta.}
```

Each port must carry a physically meaningful quantity: electricity, charging demand, mobility/accessibility, information, command, task, material/resource, or another explicitly defined carrier.

---

# 8. Directed interdependency completeness

For:

```math
\mathcal L=\{P,T,I,O\},
```

there are:

```math
\boxed{|\mathcal L|(|\mathcal L|-1)=4(3)=12}
```

possible directed cross-domain blocks.

The completeness matrix is:

```math
\boxed{
\mathbf M_\times=
\begin{bmatrix}
- & M^{PT} & M^{PI} & M^{PO}\\
M^{TP} & - & M^{TI} & M^{TO}\\
M^{IP} & M^{IT} & - & M^{IO}\\
M^{OP} & M^{OT} & M^{OI} & -
\end{bmatrix}.
}
```

All 12 must be audited, but not all must be retained. Every block ends as **included**, **excluded with evidence**, or **unresolved/scenario assumption**.

A dependency is directed:

```math
\boxed{\alpha\rightarrow\beta}
```

and reciprocal interdependency is claimed only when both directions are independently justified:

```math
\boxed{\alpha\rightarrow\beta\quad\text{and}\quad\beta\rightarrow\alpha.}
```

This follows the dependency/interdependency distinction emphasized by Rinaldi et al. (2001) and later reviews such as Ouyang (2014).

---

# 9. Full recommended interdependency pathways

## 9.1 Power to Transportation - `P -> T`

Core mechanisms:

- electricity supply to EV charging;
- electricity supply to traffic signals and ITS field devices;
- power for electrified transit where explicitly modeled.

Recommended component mapping:

```math
\text{Power bus/feeder}\rightarrow\text{EVCS or powered signal controller}.
```

Fotouhi et al. (2017) explicitly represent traffic-power coupling, including power supplied to transportation functions.

## 9.2 Transportation to Power - `T -> P`

Two different mechanisms must be separated.

**Direct electrical coupling:** EV charging demand and V2G power injection:

```math
T\to P.
```

**Restoration/access coupling:** because Organization is explicitly modeled, use the mediated chain:

```math
\boxed{T\xrightarrow{accessibility}O\xrightarrow{repair/resource\ action}P.}
```

Li et al. (2022) and Fan et al. (2024) support the mechanism in which transportation accessibility and travel time constrain repair crews or mobile energy resources.

## 9.3 Power to Information - `P -> I`

```math
\text{Power bus}\rightarrow\text{router/RTU/control/communication asset}
```

carrier: electricity/backup-power availability.

Mohamed (2019) explicitly models ICT dependence on electric power.

## 9.4 Information to Power - `I -> P`

```math
\text{SCADA/control node}\rightarrow\text{switch, DER controller, grid operator view}
```

carrier: measurement, status, alarm, command.

## 9.5 Transportation to Information - `T -> I`

```math
\text{road detector / connected vehicle / intersection sensor}\rightarrow\text{traffic data node}
```

Retain only when this sensing or physical-access mechanism is explicit in the case study.

## 9.6 Information to Transportation - `I -> T`

```math
\text{TMC/control system}\rightarrow\text{signals, routing, traveler information, charger information}
```

carrier: command/information.

## 9.7 Power to Organization - `P -> O`

When information mediation is modeled, prefer:

```math
P\to I\to O
```

for outage awareness and task formation. A direct `P -> O` edge should represent a genuinely direct organizational dependence, not duplicate the information pathway.

## 9.8 Organization to Power - `O -> P`

Possible pathways:

```math
O\to I\to P
```

for remote control/switching and:

```math
O\to T\to P
```

for physical crew access and repair.

## 9.9 Transportation to Organization - `T -> O`

```math
\text{road accessibility/travel time}\rightarrow\text{crew/resource feasibility}
```

This is core whenever restoration logistics are modeled.

## 9.10 Organization to Transportation - `O -> T`

```math
\text{DOT/TMC/emergency manager}\rightarrow\text{rerouting, road repair, emergency access}
```

Often mediated through information/control channels.

## 9.11 Information to Organization - `I -> O`

```math
\text{situational information}\rightarrow\text{decision maker}
```

This represents situational awareness, forecasts, alarms and interdependency knowledge.

## 9.12 Organization to Information - `O -> I`

```math
\text{operator/institution}\rightarrow\text{reporting priorities, communication priorities, information requests}
```

This is logical/institutional and should be tied to actual procedures or case evidence.

---

# 10. Dependency taxonomy and semantics

Following Rinaldi, Peerenboom and Kelly (2001), each cross-system relation should preserve its dependency class:

```math
\boxed{
\chi_{ij}\in\{\text{Physical},\text{Cyber/Informational},\text{Geographic},\text{Logical/Institutional}\}.
}
```

Later reviews and recent logical-interdependency work refine these categories, especially the social, policy/procedural and institutional content of logical dependencies (Ouyang, 2014; Yu et al., 2025).

Every retained inter-system edge should be represented as:

```math
\boxed{
e_{ij}^{\alpha\beta}=
(i^\alpha,j^\beta,\chi_{ij},\phi_{ij},\gamma_{ij},w_{ij}^{0},\eta_{ij})
}
```

where:

- `\chi_{ij}` = dependency class;
- `\phi_{ij}` = exact physical/operational mechanism;
- `\gamma_{ij}` = carrier (electricity, information, mobility, command, resource, etc.);
- `w_{ij}^{0}` = baseline strength/capacity/availability;
- `\eta_{ij}` = evidence provenance.

This avoids reducing an interdependency to a single binary adjacency value.

---

# 11. Geographic exposure is not causal dependence

If a flood affects a nearby substation and road simultaneously, this is a common-cause exposure, not automatically a directed dependency.

Use a separate geographic/co-exposure object:

```math
\boxed{
G_{ij}^{\alpha\beta}=
\begin{cases}
1,&\text{components share relevant spatial exposure},\\
0,&\text{otherwise}.
\end{cases}
}
```

Then Stage 2 applies the hazard field:

```math
h(x,t)\rightarrow P_i,
\qquad
h(x,t)\rightarrow T_j.
```

Do not incorrectly encode this as `P_i -> T_j` unless an actual functional mechanism also exists.

---

# 12. Heterogeneous network-of-networks representation

The correct whole-system abstraction is a heterogeneous directed multilayer network, not a conventional multiplex with identical nodes repeated across layers.

Following the general multilayer formalism of Kivela et al. (2014), define:

```math
\boxed{\mathcal M=(V_M,E_M,V,\mathcal L)}
```

with:

```math
\mathcal L=\{P,T,I,O\}
```

and heterogeneous node-layer tuples:

```math
V_M=
\bigsqcup_{\alpha\in\{P,T,I,O\}}
(V_\alpha\times\{\alpha\})
\cup V_C,
```

where `V_C` contains dedicated cross-system interface assets such as EV charging stations.

The complete edge set is:

```math
\boxed{
E_M=E_P\cup E_T\cup E_I\cup E_O\cup E_\times.
}
```

De Domenico et al. (2013) and Kivela et al. (2014) provide rigorous multidimensional/multilayer frameworks for representing intra-layer and inter-layer connectivity among heterogeneous network entities.

---

# 13. Supra-adjacency matrix

For computation and visualization, use:

```math
\boxed{
\mathbf A_{sup}=
\begin{bmatrix}
A_P&C_{PT}&C_{PI}&C_{PO}\\
C_{TP}&A_T&C_{TI}&C_{TO}\\
C_{IP}&C_{IT}&A_I&C_{IO}\\
C_{OP}&C_{OT}&C_{OI}&A_O
\end{bmatrix}.
}
```

The diagonal blocks describe intra-system connectivity. Off-diagonal blocks describe directed cross-system dependencies.

Because the layers contain different node populations, a cross-layer block is generally rectangular:

```math
C_{PT}\in\mathbb R^{n_P\times n_T}.
```

And because dependencies are directional:

```math
\boxed{C_{PT}\neq C_{TP}^{\top}}
```

in general.

This representation is appropriate for graph analysis, component-level interdependency auditing, cascade tracing, and feeding Stage 3 dynamic equations.

---

# 14. Avoid double-counting mediated causality

When Information and Organization are explicit subsystems, some apparent direct dependencies should be decomposed into causal chains.

For crew-mediated restoration:

```math
\boxed{
T\xrightarrow{accessibility}O\xrightarrow{repair}P
}
```

rather than simultaneously adding both `T -> P` and `T -> O -> P` for the same mechanism.

For outage awareness and remote response:

```math
\boxed{
P\to I\to O\to I\to P
}
```

may be more faithful than direct `P <-> O` edges if sensing and command channels are explicitly modeled.

This is a modeling discipline designed to make Stage 2 causal mechanisms identifiable and prevent duplicate propagation pathways.

---

# 15. Evidence gate and completeness audit

The thesis should use an explicit evidence gate for every interdependency.

A thesis-specific evidence hierarchy is:

```math
\boxed{E_3>E_2>E_1>E_0}
```

with:

```text
E3 Direct       - utility/GIS/operator/official technical evidence for the relation
E2 Mechanistic  - peer-reviewed mechanism plus defensible component mapping
E1 Hypothesized - physically plausible but unverified for the case; sensitivity only
E0 Unsupported  - exclude
```

This hierarchy is a methodological protocol for the thesis, not a universal published standard.

Rules:

```math
E_3,E_2\to\text{main model}
```

```math
E_1\to\text{sensitivity/scenario analysis}
```

```math
E_0\to\text{exclude}.
```

Domain-level completeness is:

```math
\boxed{C_{domain}=\frac{N_{audited}}{12}}
```

and Stage 1 requires:

```math
\boxed{C_{domain}=1.}
```

This means all 12 possible directional domain relationships were examined - not that all 12 necessarily exist.

---

# 16. Interdependency register

Every retained component-level relationship should have a traceable record:

```text
ID
Source component
Target component
Direction
Source/target layer
Node/link/agent/interface geometry
Dependency class
Exact mechanism
Carrier/service
Spatial mapping
Baseline availability/capacity
Evidence level
Literature/data source
Model inclusion status
```

Examples:

```text
D001  Feeder P17 -> EVCS C04
      Direction: P -> T
      Type: Physical
      Mechanism: electrical supply to charging station
      Carrier: electricity
      Evidence: utility/GIS + literature

D002  Road R28 -> Repair Crew O12 -> Line P09
      Direction: T -> O -> P
      Type: Physical/functional + organizational
      Mechanism: route accessibility constrains repair arrival
      Carrier: mobility/resource
      Evidence: road data + Li et al. (2022)

D003  SCADA I04 -> Switch P22
      Direction: I -> P
      Type: Cyber/informational
      Mechanism: remote measurement/control
      Carrier: information/command

D004  Dispatcher O02 -> Crew O12
      Direction: O -> O
      Type: Logical/organizational
      Mechanism: task assignment
      Carrier: authority/resource
```

The register is the auditable bridge from literature to empirical data to mathematical model.

---

# 17. Stage-1 canonical mathematical object

The complete recommended structural object is:

```math
\boxed{
\mathfrak N_1=
\left(
\{\mathcal G_P,\mathcal G_T,\mathcal G_I,\mathcal G_O\},
V_C,
E_\times,
G_{geo},
\chi_\times,
\Phi_\times,
\Theta,
\mathcal E_{prov},
\Lambda_{sus}
\right).
}
```

Interpretation:

```text
G_P       electrical topology
G_T       mobility topology
G_I       observation/communication topology if explicitly modeled
G_O       actor/coordination topology if explicitly modeled
V_C       dedicated interface assets
E_x       directed cross-system dependencies
G_geo     common spatial exposure
chi_x     dependency classes/types
Phi_x     exact mechanisms and carriers
Theta     fixed model parameters
E_prov    evidence provenance
Lambda_sus sustainability-ready metadata
```

The initial dynamic state is:

```math
\boxed{
Y_0=
\begin{bmatrix}
X_P(0)\\
X_T(0)\\
Z(0)\\
I(0)\\
O(0)
\end{bmatrix}.
}
```

Therefore:

```math
\boxed{\text{Stage 1 output}=(\mathfrak N_1,Y_0).}
```

---

# 18. Boundary with Stages 2-5

Do not put the following mathematical objects inside Stage 1:

```math
h,\;e,\;\tau,\;F,\;J,\;u,\;K,\;\mathcal V.
```

The correct handoff is:

```math
\boxed{
\underbrace{(\mathfrak N_1,Y_0)}_{Stage\ 1}
\to
\underbrace{(h,e,\mathcal C)}_{Stage\ 2}
\to
\underbrace{(F,J,\tau)}_{Stage\ 3}
\to
\underbrace{(H_{obs},\hat Y,I,O,\pi,u)}_{Stage\ 4}
\to
\underbrace{(K,\mathcal V,R)}_{Stage\ 5}.
}
```

This separation prevents structural definition, causal mechanism, dynamics and control from being mixed.

---

# 19. Sustainability-ready Stage 1 without contaminating the resilience core

Sustainability must not be introduced as a fifth Stage-1 network layer.

Do not define:

```math
\mathcal G_S=\text{``sustainability network''}.
```

Instead, attach sustainability-ready metadata to the physical assets and links:

```math
\boxed{
\lambda_i^{sus}=
[technology,energy\ source,material\ class,service\ zone,ownership,asset\ type]
}
```

and:

```math
\boxed{
\lambda_{ij}^{sus}=
[length,technology,material,capacity,mode].
}
```

Collect these as:

```math
\Lambda_{sus}.
```

These are Stage-1 descriptors, not sustainability scores.

Later:

```math
\boxed{
\text{Stage 5 resilience outputs}
+\Lambda_{sus}
+D_{sus}
\xrightarrow{\Phi_{sus}}
\text{Stage 6 transformation requirements}
}
```

and:

```math
\boxed{
\text{Stage 6 requirements}
\to
\text{Stage 7 technical + organizational + environmental + policy pathways}.
}
```

This preserves the final framework governance: Stages 1-5 remain the resilience core; Stages 6-7 translate resilience evidence into long-term sustainable transformation. Integrated-infrastructure reviews emphasize the relevance of cross-sector modeling to life-cycle efficiency, investment decisions and sustainability goals, while eGRID and GREET provide later-stage emissions/energy/life-cycle factors rather than Stage-1 physical dynamics (Hall et al., 2016/2017; EPA eGRID; DOE/Argonne GREET).

---

# 20. Simulation-oriented representation

The full Stage-1 simulator should instantiate:

```text
1. Power topology and devices
2. Transportation topology and mobile agents
3. Information topology/observation pathways where data justify it
4. Organizational actor and resource structure
5. Interface assets and ports
6. Component-level cross-layer mappings
7. Geographic co-exposure relationships
8. Dependency semantics and carriers
9. Parameter sets
10. Initial state Y0
11. Evidence provenance
12. Sustainability-ready metadata
```

This produces a reproducible baseline network-of-networks ready for Stage 2 disruption and Stage 3 dynamics.

---

# 21. Scientific rules to freeze

```math
\boxed{\text{Topology}\neq\text{Dependency}\neq\text{Parameter}\neq\text{Dynamic state}.}
```

```math
\boxed{\text{Common hazard exposure}\neq\text{causal interdependency}.}
```

```math
\boxed{\text{Dependency direction must be established independently}.}
```

```math
\boxed{\text{Do not duplicate mediated causal pathways}.}
```

```math
\boxed{\text{Every retained interdependency requires direction + mechanism + component mapping + type + evidence}.}
```

```math
\boxed{\text{Sustainability is downstream translation, not a fifth Stage-1 network layer}.}
```

---

# 22. Citation-ready methodology text

## 22.1 Network-of-networks representation

The coupled system is represented as a heterogeneous multilayer network rather than a conventional multiplex because the constituent infrastructures contain different classes of nodes and links. The power layer is represented through electrical buses connected by lines and transformers, while generation, loads and distributed resources connect to buses through device ports; the transportation layer contains junction nodes connected by directed road links; the information layer contains sensing, communication and control entities when its topology is explicitly represented; and the organizational layer contains decision-capable actors connected through authority, coordination, task and information-sharing relations. Inter-system dependencies are represented through directed and typed inter-layer edges and dedicated interface assets such as EV charging stations. This construction is consistent with general multilayer-network theory, which permits distinct node-layer tuples and inter-layer connections between heterogeneous entities (De Domenico et al., 2013; Kivela et al., 2014), and with coupled power-transport studies in which charging facilities, road accessibility, repair crews and information exchanges generate explicit cross-system interactions (Fotouhi et al., 2017; Li et al., 2022; Mohamed, 2019).

## 22.2 Interdependency identification

Cross-infrastructure relationships are identified using a directed and typed dependency framework rather than assuming generic bidirectional coupling. Following Rinaldi et al. (2001), infrastructure relations are classified by physical, cyber/informational, geographic and logical mechanisms, while later work refines especially functional, social, policy/procedural and institutional mechanisms (Ouyang, 2014; Yu et al., 2025). Every ordered relationship among Power, Transportation, Information and Organization is systematically audited, but a relation is retained only when a defensible component-level mechanism and evidence source can be established. Common spatial exposure is represented separately from causal dependence.

## 22.3 Power-transportation coupling

The physical Power-Transportation representation distinguishes electricity-dependent transportation functions from transportation-enabled power restoration. Power-to-transport dependencies include electricity supply to traffic control and charging infrastructure, whereas transportation-to-power mechanisms include EV charging demand/V2G and, during recovery, the accessibility of repair crews and mobile energy resources. The latter should be represented through a mediated `T -> O -> P` chain when organizational agents are explicitly modeled, preventing double-counting of the same mechanism (Fotouhi et al., 2017; Li et al., 2022; Fan et al., 2024).

## 22.4 Information and organization

Information and organizational interactions are modeled separately from physical infrastructure topology. ICT constitutes an explicit graph layer only when communication components and connectivity are represented; otherwise information remains an explicit observation/communication state. Organizational representation includes actors, authority, workforce/resources, plans, coordination, financial/material capability and organizational knowledge because resilience emerges from coupled human-infrastructure dynamics and institutional connectedness (Rasoulkhani & Mostafavi, 2018; Dong et al., 2020; Yu et al., 2025).

## 22.5 Sustainability handoff

Stage 1 does not introduce sustainability as an additional infrastructure layer. Instead, assets and links are annotated with sustainability-relevant descriptors needed for later translation. After Stage 5 quantifies service loss, recovery, critical interfaces, resource use and viability, Stage 6 combines those outputs with sustainability factors to identify transformation requirements, and Stage 7 compares technical, organizational, environmental and policy pathways. This separation preserves causal and physical rigor in the resilience model while allowing direct transformation of resilience evidence into sustainability decisions.

---

# 23. Next implementation artifact

The next model artifact should be the component-level interdependency matrix and register:

```math
\boxed{
\mathcal R_{dep}=
\{r_{ij}^{\alpha\beta}\}
}
```

with one row per real component-level relationship and fields for:

```text
source -> target -> direction -> geometry -> type -> mechanism -> carrier ->
spatial mapping -> baseline condition -> evidence -> data source -> inclusion status.
```

This will be the auditable empirical-to-mathematical bridge for Stage 1.
