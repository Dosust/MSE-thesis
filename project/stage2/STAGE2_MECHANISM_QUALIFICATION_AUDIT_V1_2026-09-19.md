# Stage 2 Mechanism Qualification Audit V1 — 2026-09-19

**Status:** QUALIFIED MECHANISM UNIVERSE V1 — FROZEN AT LITERATURE / INDUSTRY LEVEL  
**Case-specific causal qualification:** OPEN  
**Stage:** 2 — Evidence-Grounded Causal Interdependencies  
**RQ2:** Why and through which mechanisms do components and layers affect each other?  
**SO2:** Establish evidence-supported directional causal mechanisms, activation conditions, parameters, uncertainties and validity boundaries linking components and layers.  
**General-objective authority:** `../CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Framework authority:** `../CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Discovery register:** `Stage2_Mechanism_Discovery_Register.xlsx`

---

## 0. Scientific decision

The 38-row discovery register is not a set of 38 independent causal mechanisms.

The qualification workflow produces:

```math
\boxed{
38\ \text{discovery entries}
\rightarrow
13\ \text{core causal mechanism families}
+
1\ \text{external third-sector mechanism}
+
10\ \text{frontier instances/compositions}
+
8\ \text{discovery controls}
}
```

This normalization prevents double-counting technologies, modes, or implementations as if they were distinct causal laws.

Permanent distinction:

```math
\boxed{
\text{technology}
\neq
\text{mechanism}
\neq
\text{mechanism instance}
}
```

Examples:

- V2G, V2B, electric-bus support, and mobile EV storage instantiate bidirectional/mobile energy transfer.
- Repair-crew access, operator access, and mobile-generator routing instantiate mobility/access mechanisms with different receivers and activation conditions.
- Dynamic wireless charging, megawatt truck charging, and battery swapping are technology/mode instances or compositions of existing charging-demand and charging-service mechanisms.

No case-specific relation is accepted merely because its mechanism family is established in literature.

```math
\boxed{
\text{literature-established mechanism}
\neq
G_2^{case}=\mathrm{PASS}
}
```

---

# 1. Sequence execution

| Step | Operation | Result |
|---|---|---|
| 1 | Normalize 38 discovery entries | COMPLETE |
| 2 | Deep review verification | COMPLETE for mechanism-family qualification |
| 3 | Identify primary mechanism evidence | COMPLETE to V1 evidence depth |
| 4 | Verify industrial / standards evidence | COMPLETE to V1 evidence depth |
| 5 | Identify contrary evidence, substitutes, and deactivation conditions | COMPLETE |
| 6 | Assign evidence status | COMPLETE |
| 7 | Freeze qualified mechanism universe | COMPLETE — this file |
| 8 | Derive thesis boundary from RQ0/general objective | COMPLETE at conceptual level; experimental/case boundary remains OPEN |

---

# 2. Qualification object

For every normalized mechanism family (q_i):

```math
\mathcal Q_i=
(
S_i,
R_i,
\chi_i,
\Phi_i,
\mathcal A_i,
O_i,
E_i^{lit},
E_i^{ind},
U_i,
V_i,
F_i
)
```

where:

- (S_i): causal source;
- (R_i): receiver;
- (\chi_i): exchanged service/resource;
- (\Phi_i): causal pathway;
- (\mathcal A_i): activation conditions;
- (O_i): observable consequence;
- (E_i^{lit}): peer-reviewed evidence;
- (E_i^{ind}): industrial/standards/operational evidence;
- (U_i): uncertainty;
- (V_i): validity domain;
- (F_i): falsification / rival explanation.

Evidence-status vocabulary:

```text
ESTABLISHED
CONDITIONAL
EMERGING-INSTANCE
DISCOVERY-CONTROL
OUTSIDE-CORE
UNSUPPORTED
```

No mechanism is promoted from literature status to case acceptance without the seven G2 gates.

---

# 3. Normalized core causal mechanism universe

## Q01 — Electrical service to transportation operational assets

**Parent mapping:** M01 + M02 + M03  
**Direction:** (P\rightarrow T)  
**Status:** **ESTABLISHED**, with asset-specific activation.

```math
P_{service}
\rightarrow
\{\text{signal, ITS, sensing, lighting, ventilation, pumping, control}\}
\rightarrow
Q_T
```

### Evidence
- Zhu et al. (2021), DOI: 10.1155/2021/5599073 — explicit modeled pathway from power outage to traffic-signal failure and transportation-capacity effects.
- FHWA, *Learning from the 2003 Blackout* — operational evidence that traffic signals, ITS field equipment, traffic-management-center systems, and fueling facilities require continuity/backup power.
- FTA emergency-preparedness guidance — emergency lighting, communications, ventilation, pumps, and other rail support systems require normal/alternative electrical supply.

### Activation
External electrical service is required and adequate backup/redundancy is unavailable, failed, or exhausted.

### Main falsifiers / substitutes
- adequate UPS/generator endurance;
- fail-safe/local control preserving the declared service;
- independent device/controller fault;
- direct road damage dominating traffic response.

---

## Q02 — Electric traction / propulsion energy supply

**Parent mapping:** M04; relevant portions of M08  
**Direction:** (P\rightarrow T)  
**Status:** **CONDITIONAL** — mechanism established, mode-specific.

```math
P_{traction}
\rightarrow
\text{traction availability}
\rightarrow
Q_T
```

### Evidence
- Gabbar et al. (2020), DOI: 10.1049/iet-est.2019.0145 — electrified railway dependence on electric-grid supply and resilience-oriented alternative supply.
- FTA emergency-preparedness guidance treats traction power and emergency power as integral transit-system functions.

### Falsifiers / substitutes
- non-electrified transport mode;
- independent onboard propulsion;
- redundant traction supply/microgrid maintaining service.

---

## Q03 — Charging-energy service availability and grid operating constraints

**Parent mapping:** M05 + M06  
**Direction:** (P\rightarrow T)  
**Status:** **ESTABLISHED**.

```math
X_P
\rightarrow
P_{EVSE}^{avail}
\rightarrow
\text{charging rate/availability}
\rightarrow
\text{SOC/mobility service}
```

### Evidence
- Wei et al. (2019), DOI: 10.1007/s40565-019-0516-7 — charging stations are explicit coupling points; power-system capacity/security constraints affect charging and traffic behavior.
- Wang et al. (2022), DOI: 10.1111/mice.12736 — charging-station failure changes electrified-road-network performance.
- DOE FEMP managed charging — grid/equipment capacity and fleet operational needs jointly constrain charging.

### Falsifiers / substitutes
- alternative charging station;
- sufficient vehicle SOC/range;
- local storage/PV/backup maintaining charging;
- EVSE hardware failure unrelated to grid state.

---

## Q04 — Physical obstruction / right-of-way interaction from power assets

**Parent mapping:** M09  
**Direction:** (P\rightarrow T)  
**Status:** **CONDITIONAL** — real event pathway; spatial/event activation required.

```math
\text{power-asset physical state}
\rightarrow
\text{road obstruction / safety closure}
\rightarrow
C_T
```

### Evidence
- Operational incidents document downed power lines closing roads and rail corridors.
- BC Hydro documented removal of downed lines affecting road and rail traffic.
- FHWA emergency/re-entry practice explicitly requires handling downed power lines before safe roadway use.
- NYC climate-infrastructure synthesis identifies spatial/functional power–transport interactions.

### Evidence boundary
The general pathway is real, but a case-specific relation requires verified spatial co-location and an actual obstruction/safety pathway. Co-location alone is insufficient.

### Falsifiers / substitutes
- no shared right-of-way;
- asset is underground or outside roadway influence zone;
- line is safely de-energized/removed without capacity effect;
- alternate road preserves the declared transport service.

---

## Q05 — Mobility-derived charging demand and spatial redistribution

**Parent mapping:** M10 + M11  
**Direction:** (T\rightarrow P)  
**Status:** **ESTABLISHED**.

```math
\{\text{trip, route, arrival, SOC, dwell, station choice}\}
\rightarrow
D_{charge}(x,t)
\rightarrow
X_P
```

### Evidence
- Wei et al. (2019), DOI: 10.1007/s40565-019-0516-7 — transportation flow and charging-station choice determine charging demand; grid/security constraints feed back to station behavior.
- Alizadeh et al. (2017), DOI: 10.1109/TCNS.2016.2590259 — EV travel/charging decisions jointly respond to road congestion and spatial electricity prices.
- Wang et al. (2022), DOI: 10.1049/els2.12050 — real-time traffic/grid information and pricing alter charging-station choice and distribution-grid state.

### Falsifiers / substitutes
- negligible EV penetration;
- charging load is externally fixed and independent of modeled mobility;
- charging is geographically decoupled from the modeled transportation network.

---

## Q06 — Transportation access for field power-system intervention

**Parent mapping:** M12 + M13  
**Direction:** (T\rightarrow P)  
**Status:** **ESTABLISHED**.

```math
X_T^{route}
\rightarrow
T_{arrival}
\rightarrow
A_{field}
\rightarrow
X_P^{restore}
```

### Evidence
- Anokhin et al. (2021), DOI: 10.1111/poms.13393 — repair crews/mobile power sources are scheduled under transportation-network constraints.
- Liu et al. (2026), DOI: 10.1002/tee.70253 — mobile emergency generator travel time in transportation networks affects restoration speed.
- Distribution-restoration literature distinguishes automatic/remote switching from field work that requires crew access.

### Falsifiers / substitutes
- task is fully remote/automatic;
- required crew/resource is already on site;
- an unaffected alternate route produces no meaningful intervention delay;
- repair/task duration dominates so strongly that transport state has no identifiable contribution at the selected resolution.

---

## Q07 — Restoration logistics for crews, equipment, fuel, and spare parts

**Parent mapping:** M14  
**Direction:** (T\rightarrow P)  
**Status:** **ESTABLISHED**.

```math
\text{transport/logistics}
\rightarrow
\text{resource availability at task}
\rightarrow
\text{repair feasibility/time}
\rightarrow
X_P^{restore}
```

### Evidence
- Wang et al. (2004), DOI: 10.1016/S0377-2217(02)00803-2 — power-restoration depot/location model explicitly includes poles, transformers, crews, vehicles, and shipment of resources.
- Distribution-resilience reviews explicitly treat repair crews and spare-parts management as restoration resources.

### Falsifiers / substitutes
- required resources are pre-positioned at the failure site;
- local inventory is sufficient;
- logistics delay is negligible relative to all other restoration times.

---

## Q08 — Mobile power-resource positioning through transportation

**Parent mapping:** M15  
**Direction:** (T\rightarrow P)  
**Status:** **ESTABLISHED**.

```math
X_T
\rightarrow
\text{MEG/MESS/mobile-transformer position}
\rightarrow
\text{temporary electrical service}
\rightarrow
Q_P
```

### Evidence
- Anokhin et al. (2021), DOI: 10.1111/poms.13393.
- Liu et al. (2026), DOI: 10.1002/tee.70253.
- Industry deploys road-transportable mobile transformers and mobile emergency resources specifically for rapid restoration.

### Falsifiers / substitutes
- stationary DER/microgrid provides the required service;
- target cannot physically accept/connect the mobile resource;
- resource is unavailable or unreachable;
- transport time is immaterial at the selected temporal scale.

---

## Q09 — Bidirectional/mobile stored-energy export to the power system

**Parent mapping:** M16  
**Direction:** (T\rightarrow P)  
**Status:** **CONDITIONAL** — technology established; activation/deployment not universal.

```math
\{SOC,location,availability\}
+
\text{bidirectional interface}
+
\text{authorization}
\rightarrow
P_{export}
\rightarrow
X_P
```

### Evidence
- Galus et al. (2012), DOI: 10.1002/wene.56 — EV storage and V2G roles in smart grids.
- DOE FEMP documents V2B/V2G and EVs as mobile storage/resilience resources.
- ISO 15118-20:2022 specifies communication sequences for bidirectional power transfer.

### Falsifiers / substitutes
- no bidirectional hardware;
- insufficient SOC;
- vehicle unavailable at required location/time;
- utility/interconnection rules prohibit export;
- stationary storage supplies the same service.

---

## Q10 — Transport-induced physical damage to power assets

**Parent mapping:** M17  
**Direction:** (T\rightarrow P)  
**Status:** **CONDITIONAL** — event-dependent but directly observable.

```math
\text{vehicle/roadwork/excavation action}
\rightarrow
\text{mechanical damage}
\rightarrow
X_P^{failure}
```

### Evidence
- Singapore Energy Market Authority documented excavation works damaging a 66-kV cable and causing an electricity outage.
- Utility/transport safety practice recognizes vehicle strikes and excavation as direct asset-damage pathways.

### Evidence boundary
This mechanism is causal only where a physical impact/interference event is verified. It must not be inferred from simple spatial proximity.

### Falsifiers
- no physical interference;
- asset failure predates transport/roadwork action;
- independent electrical/protection failure explains the outage.

---

## Q11 — Information/control-mediated power–transport coupling

**Parent mapping:** M18  
**Direction:** (P\leftrightarrow I\leftrightarrow T)  
**Status:** **ESTABLISHED**.

```math
X_P,X_T
\rightarrow
I
\rightarrow
\text{price/command/status/schedule}
\rightarrow
u_P,u_T
\rightarrow
X_P,X_T
```

### Evidence
- Alizadeh et al. (2017), DOI: 10.1109/TCNS.2016.2590259 — coupled travel/charging coordination through pricing.
- Wang et al. (2022), DOI: 10.1049/els2.12050 — EV–traffic–grid information network, charging guidance, and grid constraints.
- IEEE 2030.5-2023 — application-layer mechanisms for demand response, load control, pricing, DER, and EV management.
- SAE J2847/1_202505 — smart-charging communication.
- ISO 15118-20:2022 — EV–EVSE communication and bidirectional transfer.

### Falsifiers / substitutes
- local autonomous/static control makes communication irrelevant;
- information path exists but does not alter any physical action;
- communication signal is not used by the relevant controller/operator.

---

## Q12 — Communication/cyber availability, integrity, and latency

**Parent mapping:** M19  
**Direction:** (I\rightarrow\{P,T\}) and mediated (P\leftrightarrow T)  
**Status:** **CONDITIONAL** — cyber/communication dependency established, exact physical consequence function-specific.

```math
\{availability,integrity,latency\}_I
\rightarrow
\text{control/coordination quality}
\rightarrow
X_P,X_T
```

### Evidence
- Critical-infrastructure literature recognizes cyber/information dependencies.
- IEEE 2030.5 and ISO 15118 define message exchanges and security/communication interfaces required by smart-grid/EV functions.
- FHWA blackout evidence shows transport sensing/communication functions can fail when supporting power/communications are lost.

### Falsifiers / substitutes
- local fail-safe operation preserves service;
- redundant communications preserve the required function;
- physical mechanism operates independently of communication.

---

## Q13 — Organizational, rule-mediated, pricing, and dispatch coupling

**Parent mapping:** M20  
**Direction:** (P\leftrightarrow O\leftrightarrow T)  
**Status:** **CONDITIONAL** — logical/rule-mediated interdependency is established; case rule/action must be observed.

```math
\text{rule / authority / priority / price}
\rightarrow
\text{human or algorithmic action}
\rightarrow
X_P,X_T
```

### Evidence
- González et al. (2016), DOI: 10.1111/mice.12171 — restoration interdependency includes logical/human-decision pathways.
- Yu et al. (2024/2025 issue), DOI: 10.1111/risa.16555 — formal/informal rules can mediate infrastructure states and provide a method to identify logical interdependencies.
- Alizadeh et al. (2017), DOI: 10.1109/TCNS.2016.2590259 — pricing coordinates coupled power/transport behavior.
- Wang et al. (2022), DOI: 10.1049/els2.12050 — price-guided charging alters EV choices and grid response.
- DOE FEMP notes that V2G reverse power flow depends on utility/interconnection permission.

### Falsifiers
- written rule is not implemented;
- price/priority has no measurable effect on action;
- observed outcome is fully explained by a binding physical constraint;
- authority is absent from the actual decision pathway.

---

# 4. External third-sector mechanism

## QX01 — Power-dependent fueling service

**Parent mapping:** M07  
**Chain:** (P\rightarrow FUEL\rightarrow T)  
**Status:** **CONDITIONAL / OUTSIDE CORE PHYSICAL BOUNDARY**.

FHWA operational evidence confirms that electrical outages can disable fueling facilities and therefore constrain vehicle operation. However, this is not a direct (P\rightarrow T) two-sector mechanism: it introduces a third physical infrastructure/resource system.

Therefore:

```math
\boxed{
QX01\notin\mathcal M_{PT}^{core}
}
```

unless the thesis explicitly expands its physical system boundary beyond (P+T).

It may remain an external boundary condition for emergency mobility.

---

# 5. Original-row normalization

| Original entry | V1 disposition |
|---|---|
| M01 | Q01 instance — signal/control |
| M02 | Q01 instance — monitoring/information equipment |
| M03 | Q01 instance — safety/support equipment |
| M04 | Q02 |
| M05 | Q03 — service availability |
| M06 | Q03 — capacity/quality constraint |
| M07 | QX01 external third-sector chain |
| M08 | NOT an independent mechanism; non-road mode bucket mapped to Q01/Q02/Q03 as appropriate |
| M09 | Q04 |
| M10 | Q05 — demand generation |
| M11 | Q05 — spatial redistribution |
| M12 | Q06 — repair access |
| M13 | Q06 — manual/operator access |
| M14 | Q07 |
| M15 | Q08 |
| M16 | Q09 |
| M17 | Q10 |
| M18 | Q11 |
| M19 | Q12 |
| M20 | Q13 |

---

# 6. Frontier rows: mechanism or instance?

The ten frontier rows are retained for technology scanning but are **not ten new causal mechanism families**.

| Frontier | V1 interpretation | Status |
|---|---|---|
| F01 Dynamic wireless road charging | instance/composition of Q03 + Q05 + Q11 | EMERGING-INSTANCE |
| F02 Autonomous-EV fleet/grid coupling | composition of Q05 + Q11 + Q13 | EMERGING-INSTANCE |
| F03 Megawatt truck charging | high-intensity instance of Q03 + Q05 | EMERGING-INSTANCE |
| F04 Battery swapping | instance/composition of Q03 + Q05 | EMERGING-INSTANCE |
| F05 Electric buses/fleets as emergency energy | instance of Q08 + Q09 | EMERGING-INSTANCE |
| F06 Regenerative transport energy export | mode-specific instance of Q09 | EMERGING-INSTANCE |
| F07 Electric maritime/aviation charging | mode-specific instance of Q03 + Q05 | EMERGING-INSTANCE |
| F08 Hydrogen/e-fuel coupling | (P\rightarrow E\rightarrow T), introduces third physical energy-vector system | OUTSIDE-CORE |
| F09 Transactive EV markets | composition of Q05 + Q11 + Q13 | EMERGING-INSTANCE |
| F10 Autonomous mobile microgrids | composition of Q08 + Q09 + Q11 + Q13 | EMERGING-INSTANCE |

This treatment is consistent with recent reviews of coupled power–transportation systems, which organize the field around EV charging/discharging, routing, pricing, mobile energy resources, markets, resilience, and coordination rather than treating each technology implementation as a new causal law.

---

# 7. Unknown/discovery rows

U01–U08 are **not mechanisms**. They are retained as discovery controls.

```math
\boxed{
\mathcal U_D
=
\{
U01,\ldots,U08
\}
\not\subset
\mathcal M_{PT}^{qualified}
}
```

| ID | Role |
|---|---|
| U01 | search for undocumented physical/interface dependency |
| U02 | search for hidden mediator |
| U03 | search for state-dependent activation threshold |
| U04 | search for causal delay/endurance effect |
| U05 | search for nonlinear feedback/tipping |
| U06 | search for redundancy/substitution masking |
| U07 | search for organizationally latent dependency |
| U08 | search for technology-created future dependency |

Any newly discovered relation must still specify source, receiver, exchanged quantity/service, mechanism, activation, validity domain, uncertainty, rivals, and falsification before G2.

---

# 8. Contrary evidence and substitution rule

A mechanism family is not automatically active.

For every case relation (e):

```math
\boxed{
\Phi_e\ \text{known}
\not\Rightarrow
\mathcal A_e(t)=1
}
```

The qualification workflow must explicitly test suppression/substitution:

1. backup power or redundancy;
2. alternative route;
3. remote/automatic operation;
4. pre-positioned crew/resource;
5. alternative charging station;
6. stationary DER/storage;
7. adequate EV SOC/range;
8. redundant communication;
9. rule/price not implemented;
10. common hazard or independent failure as rival explanation.

A valid mechanism may therefore be **inactive** in a specific scenario without being scientifically false.

---

# 9. Evidence-status assignment

## Core qualified families

```text
Q01  ESTABLISHED
Q02  CONDITIONAL — transport-mode specific
Q03  ESTABLISHED
Q04  CONDITIONAL — event/spatial activation required
Q05  ESTABLISHED
Q06  ESTABLISHED
Q07  ESTABLISHED
Q08  ESTABLISHED
Q09  CONDITIONAL — deployment/SOC/authorization dependent
Q10  CONDITIONAL — physical-event dependent
Q11  ESTABLISHED
Q12  CONDITIONAL — function/communication architecture dependent
Q13  CONDITIONAL — actual rule/decision implementation required
QX01 CONDITIONAL / OUTSIDE-CORE
```

## Discovery rows

```text
F01–F07, F09–F10 = EMERGING INSTANCES / COMPOSITIONS
F08                 = OUTSIDE-CORE THIRD-SECTOR EXTENSION
U01–U08             = DISCOVERY CONTROLS, NOT MECHANISMS
```

No qualified core family is currently classified as UNSUPPORTED at the family level. This does **not** mean every original wording, technology instance, case connection, or parameter is supported.

---

# 10. Qualified mechanism universe freeze

The literature/industry-qualified universe is frozen as:

```math
\boxed{
\mathcal M_{PT}^{Q1}
=
\{
Q01,Q02,Q03,Q04,Q05,Q06,Q07,Q08,Q09,Q10,Q11,Q12,Q13
\}
}
```

with external boundary mechanism:

```math
\boxed{
\mathcal M_{ext}^{Q1}
=
\{QX01\}
}
```

and discovery controls:

```math
\boxed{
\mathcal U_D
=
\{U01,\ldots,U08\}.
}
```

**Freeze meaning:** no new parent causal mechanism family should be added, removed, merged, or split without an explicit evidence-backed amendment and re-audit.

**Freeze does not mean:**
- case-specific presence is proven;
- activation is proven;
- coupling strength is known;
- parameters are calibrated;
- any G2 gate has passed;
- any mechanism may yet enter Stage 3.

Current accepted case set remains:

```math
\boxed{
\mathbb I_{acc}=\varnothing
}
```

until case-specific G2 qualification.

---

# 11. Thesis boundary derived from RQ0 and the general objective

The canonical general objective is to develop and validate an evidence-grounded mathematical and engineering framework for coupled Power–Transportation infrastructure linking structure, causal interdependencies, hybrid dynamics, information/organizational control, resilience, intervention, sustainability consequences, and engineering decision under uncertainty.

Therefore a mechanism belongs to the **conceptual thesis core** if it can affect at least one downstream object:

```math
F_{\mathcal G}^{m},
\qquad
Q(Y,t),
\qquad
\mathfrak R_T,
\qquad
a_k,
\qquad
\mathbf J_{sus}.
```

Conceptual boundary:

```math
\boxed{
\mathcal M_{thesis}^{concept}
=
\mathcal M_{PT}^{Q1}
}
```

because Q01–Q13 cover:
- physical service dependencies;
- operating-demand coupling;
- failure propagation;
- restoration access/logistics;
- mobile resilience resources;
- physical cross-damage;
- information/cyber mediation;
- organizational/decision mediation.

### Excluded from the core physical boundary
- QX01 as a direct core mechanism because it requires an additional fuel infrastructure;
- F08 because it requires a hydrogen/e-fuel energy-vector infrastructure;
- mode/technology examples as independent mechanisms;
- common-hazard co-damage without a directional pathway;
- pure spatial proximity without a causal pathway.

### Experimental boundary
The **experimental/case mechanism subset is NOT frozen here**.

```math
\boxed{
\mathcal M_{thesis}^{experiment}
\subseteq
\mathcal M_{PT}^{Q1}
}
```

It must later be selected by:

```math
m_i\in\mathcal M_{thesis}^{experiment}
\iff
\begin{cases}
\text{causally defensible},\\
\text{case connection demonstrated},\\
\text{activation observable/testable},\\
\text{dynamically material},\\
\text{data sufficient},\\
\text{falsifiable}.
\end{cases}
```

The repository currently contains no case-specific G2 PASS record for these mechanisms. Therefore further narrowing on presumed case data would be premature.

---

# 12. Stage-2 handoff after this audit

The next admissible operation is **case materialization**, not additional generic mechanism invention:

```math
\boxed{
\mathcal M_{PT}^{Q1}
\rightarrow
\text{case-specific candidate instances}
\rightarrow
\mathfrak D_e^{(2)}
\rightarrow
G_2(e)
}
```

For each case candidate:

```math
G_2(e)
=
G_{2-M}
\land
G_{2-C}
\land
G_{2-X}
\land
G_{2-A}
\land
G_{2-E}
\land
G_{2-V}
\land
G_{2-F}.
```

Only:

```math
G_2(e)=\mathrm{PASS}
```

permits:

```math
\mathfrak r_e^{(1)}
\rightarrow
\mathfrak I_e
\rightarrow
F_{\mathcal G}^{m}.
```

---

# 13. Principal verified evidence anchors

## Peer-reviewed reviews / synthesis
1. Rinaldi, Peerenboom & Kelly (2001), *Identifying, understanding, and analyzing critical infrastructure interdependencies*. DOI: https://doi.org/10.1109/37.969131
2. Ouyang (2014), *Review on modeling and simulation of interdependent critical infrastructure systems*. DOI: https://doi.org/10.1016/j.ress.2013.06.040
3. Wei et al. (2019), *Interdependence between transportation system and power distribution system: a comprehensive review on models and applications*. DOI: https://doi.org/10.1007/s40565-019-0516-7
4. Galus et al. (2012), *The role of electric vehicles in smart grids*. DOI: https://doi.org/10.1002/wene.56
5. Kandaperumal & Srivastava (2020), *Resilience of the electric distribution systems: concepts, classification, assessment, challenges, and research needs*. DOI: https://doi.org/10.1049/iet-stg.2019.0176
6. Hu, Wang & Tan (2024), *Electric Vehicle Integration in Coupled Power Distribution and Transportation Networks: A Review*. DOI: https://doi.org/10.3390/en17194775
7. Yang et al. (2025), *Recent advances in coordination and optimization of power-transportation systems: An overview*. DOI: https://doi.org/10.1016/j.rser.2025.115786
8. Oladigbolu et al. (2025), *A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources*. DOI: https://doi.org/10.1016/j.est.2025.118419
9. Yu et al. (2024; issue 2025), *Logical interdependencies in infrastructure*. DOI: https://doi.org/10.1111/risa.16555

## Primary / mechanism-oriented studies
10. Fotouhi, Moryadee & Miller-Hooks (2017), DOI: https://doi.org/10.1016/j.ress.2017.01.026
11. Alizadeh et al. (2017), DOI: https://doi.org/10.1109/TCNS.2016.2590259
12. Zhu et al. (2021), DOI: https://doi.org/10.1155/2021/5599073
13. Anokhin et al. (2021), DOI: https://doi.org/10.1111/poms.13393
14. Wang et al. (2022), charging-station resilience, DOI: https://doi.org/10.1111/mice.12736
15. Wang et al. (2022), pricing/information coordination, DOI: https://doi.org/10.1049/els2.12050
16. Liu et al. (2026), DOI: https://doi.org/10.1002/tee.70253
17. Zhang et al. (2025), DOI: https://doi.org/10.1049/ein2.70010
18. Wang et al. (2004), restoration resources/logistics, DOI: https://doi.org/10.1016/S0377-2217(02)00803-2
19. Gabbar et al. (2020), traction-power resilience, DOI: https://doi.org/10.1049/iet-est.2019.0145
20. González et al. (2016), DOI: https://doi.org/10.1111/mice.12171

## Industrial / official standards and operational evidence
21. FHWA, *Learning from the 2003 Blackout*: https://ops.fhwa.dot.gov/publications/fhwahop08015/lit5_9_1.htm
22. FHWA power/ITS lessons: https://ops.fhwa.dot.gov/publications/fhwahop08015/lit5_2_3.htm
23. DOE FEMP managed EV charging: https://www.energy.gov/cmei/femp/managed-ev-charging-federal-fleets
24. DOE FEMP bidirectional/mobile storage: https://www.energy.gov/cmei/femp/bidirectional-charging-and-electric-vehicles-mobile-storage
25. ISO 15118-20:2022: https://www.iso.org/standard/77845.html
26. IEEE 2030.5-2023: https://standards.ieee.org/ieee/2030.5/11216/
27. SAE J2847/1_202505: https://saemobilus.sae.org/standards/j28471_202505-communication-smart-charging-plug-electric-vehicles-using-smart-energy-profile-20
28. FTA emergency preparedness: https://www.transit.dot.gov/regulations-and-guidance/safety/recommended-emergency-preparedness-guidelines-rail-transit-systems
29. FAA power/runway-lighting resilience evidence: https://www.faa.gov/sites/faa.gov/files/2021-11/PL_115-254_Sec330_Certain_Aviation_Safety_Risks.pdf
30. Singapore EMA cable-damage incident: https://www.ema.gov.sg/news-events/news/media-releases/2011/company-fined-150000-for-damaging-electricity-cable-which-resulted-in-blackout

---

# 14. Final audit conclusion

```math
\boxed{
\mathcal M_{discovery}
\xrightarrow{normalization+evidence}
\mathcal M_{PT}^{Q1}
=
\{Q01,\ldots,Q13\}
}
```

and

```math
\boxed{
\text{Qualified mechanism universe frozen}
\quad\text{but}\quad
\mathbb I_{acc}=\varnothing.
}
```

The scientifically valid next stage is case-specific instantiation and G2 testing of mechanisms drawn from (mathcal M_{PT}^{Q1}), with no simulation-generated causal evidence and no mechanism entering Stage 3 before G2 PASS.
