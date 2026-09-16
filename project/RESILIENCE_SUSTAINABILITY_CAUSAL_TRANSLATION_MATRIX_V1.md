# Resilience–Sustainability Causal Translation Matrix v1.0

**Date:** 2026-09-16  
**Status:** WORKING EVIDENCE-GATED MATRIX; NOT A CONFIRMATORY RESULT  
**Method:** EGMIV  
**Purpose authority:** `THESIS_PURPOSE_AND_CAUSAL_SPINE_V1.md`

## 1. Matrix object

```math
\boxed{
\mathcal T_{RS}
=
[\mathfrak d_e,M_e,\theta_e,\tau_e,R_i,a_k,J_j,D_e,U_e,V_e].
}
```

A pathway is retained only if every arrow

```math
\mathfrak d_e\rightarrow M_e\rightarrow R_i\rightarrow a_k\rightarrow J_j
```

has an explicit physical/functional interpretation and at least a plausible evidence/validation route.

Evidence classes used here:

```text
A = direct empirical or field-supported evidence;
B = peer-reviewed mechanistic/model evidence with clear physical semantics;
C = indirect/transfer evidence requiring an additional mapping;
D = unsupported for current thesis use.
```

No class-A/B pathway is automatically a thesis contribution; this matrix establishes admissibility, not novelty.

---

## 2. Candidate sustainability outcome gate

For candidate outcome `J_j`, define

```math
\boxed{
G_j=D_j\land U_j\land M_j\land T_j\land V_j
}
```

where `D_j` = precise definition, `U_j` = units, `M_j` = causal mechanism, `T_j` = time semantics, and `V_j` = validation/data route.

### v1 adjudication

| Outcome | Working definition | Unit | Causal route from P–T | Data/validation route | v1 decision |
|---|---|---:|---|---|---|
| `J_access` | loss/availability of access to required mobility or essential destinations | dimensionless fraction, person-hours, or travel-time-weighted access | direct through charging availability, road capacity, OD completion and travel time | OD/road/charging/service-location data | **RETAIN — CORE** |
| `J_energy` | operational electricity/energy use attributable to charging and restoration strategy; preferably separated into grid, renewable and curtailed energy terms | MWh | direct through charging schedule, V2G, grid dispatch and restoration | charging/load/generation profiles; dispatch model | **RETAIN — CONDITIONAL CORE** |
| `J_carbon` | operational GHG associated with electricity/transport operation over declared horizon; embodied carbon only if LCA inventory is added | kg or t CO2e | direct if generation/emission factors or dispatch are modeled | time-varying emissions factors or dispatch/LCA data | **RETAIN — CONDITIONAL CORE** |
| `J_cost` | intervention + operation + disruption/restoration economic burden | currency, NPV | direct but highly context-specific | CAPEX/OPEX, market/utility/restoration cost data | **RETAIN AS BUDGET/SECONDARY OUTCOME; NOT PRIMARY CORE** |
| `J_equity` | distribution of accessibility/service burden across declared population groups | Gini/Theil, subgroup gap, burden ratio | indirect through spatial service/accessibility plus demographic exposure | census/socioeconomic + spatial service data | **CONDITIONAL SOCIAL OUTCOME** |
| `J_resource` | lifecycle material/resource burden of structural interventions | kg material, embodied energy, water, etc. | requires intervention-specific life-cycle inventories | LCA/EPD/inventory data | **DEFER FROM MINIMAL CORE** |

### Pruning consequence

The minimal v1 sustainability vector is therefore not the original six-element vector. The core working vector is

```math
\boxed{
\mathbf J_{\rm sus}^{core}
=
[J_{access},J_{energy},J_{carbon}]^\top
}
```

with

```math
J_{cost}\ \text{used initially as a budget/secondary objective},
```

```math
J_{equity}\ \text{activated only when population-disaggregated data pass their evidence gate},
```

and

```math
J_{resource}\ \text{deferred unless Stage 7 adds validated lifecycle inventories}.
```

This is a scope-control decision, not a claim that cost, equity or material use are unimportant.

---

## 3. Causal translation matrix — v1 retained pathways

### RS-01 — Power → transportation charging availability → mobility/accessibility

```math
P_c(t)\downarrow
\rightarrow
\mu_c(t)\downarrow
\rightarrow
q_c(t)\uparrow
\rightarrow
S_T(t)\downarrow
\rightarrow
J_{access}\downarrow.
```

A minimal queue relation is

```math
\dot q_c(t)=\lambda_c(t)-\mu_c(P_c(t),x_c(t)),
\qquad q_c\ge0.
```

**Dependency:** feeder/grid energization → charging-station service.  
**Resilience quantities:** `L_T`, `q_max`, queue-clearance time, recovery time, mobility service.  
**Candidate interventions:** charger redundancy, backup/microgrid support, distributed siting, rerouting/charging control.  
**Sustainability outcome:** accessibility to mobility/essential services; equity only after demographic disaggregation.  
**Evidence:**
- Wang et al. (2021), *Resilience assessment of electrified road networks subject to charging station failures*, DOI `10.1111/mice.12736` — mechanistic optimization linking charging-station failure to road-network performance. **B**.
- Essus & Rachunok (2024), *Electric vehicles limit equitable access to essential services during blackouts*, `npj Sustainable Mobility and Transport` — computational evidence directly connecting blackout-constrained EV mobility to access to essential services. **B/A-model-data**.
- Bao & Kontou (2026), *Electric vehicle charging stations at risk from hazardous events and power outages*, DOI `10.1016/j.rser.2025.116144` — empirical outage/hazard exposure of charging infrastructure and associated mobility vulnerability. **A/B**.

**Main uncertainties:** latent requested trips, initial state-of-charge distribution, outage duration, charger functionality, spatial substitution, driver response.  
**Validation requirement:** observed charging availability plus held-out mobility/accessibility data or a clearly bounded model-validation surrogate.  
**Status:** `RETAIN_CORE`.

---

### RS-02 — Power → traffic-control loss → road performance/accessibility

```math
P_i(t)=0
\rightarrow
\text{signal/control degradation}
\rightarrow
C_\ell(t)\downarrow
\rightarrow
T_{ij}(t)\uparrow
\rightarrow
S_T(t)\downarrow
\rightarrow
J_{access}\downarrow.
```

**Dependency:** electricity supply → signalized/controlled transportation operation.  
**Resilience quantities:** travel-time increase, capacity loss, evacuation/mobility loss, `L_T`.  
**Candidate interventions:** backup power at critical signals, islanded control, prioritization of critical intersections.  
**Sustainability outcome:** accessibility/service continuity; possible secondary energy/emissions effects through congestion require an explicit traffic-emission model and are not assumed.  
**Evidence:** Zhu et al. (2021), *Modeling and Simulation of Cascading Failures in Transportation Systems during Hurricane Evacuations*, DOI `10.1155/2021/5599073` — models power-loss-induced signal failure and resulting road-capacity/evacuation impacts. **B**.

**Main uncertainties:** intersection control behavior during outage, route adaptation, congestion propagation.  
**Validation requirement:** observed signal outage/road-speed or travel-time response under comparable events.  
**Status:** `RETAIN_CORE`.

---

### RS-03 — Transportation → power restoration through crew access

```math
x_T(t)
\rightarrow
\tau_{crew}(t)
\rightarrow
\tau_{repair}(t)
\rightarrow
T_R^P
\rightarrow
L_P
\rightarrow
\{J_{access},J_{cost}\}.
```

A minimal relation is

```math
\tau_{crew,j}(t)=\min_{r\in\mathcal R_j(t)}\sum_{\ell\in r}\tau_\ell(x_T(t)),
```

with infeasibility if no admissible path exists.

**Dependency:** road availability/congestion → utility crew access → power restoration timing.  
**Resilience quantities:** crew-arrival time, power restoration time, cumulative power-service loss.  
**Candidate interventions:** crew staging, route protection, road clearance prioritization, mobile power, coordinated repair sequencing.  
**Sustainability outcome:** accessibility/service burden through outage duration; cost as secondary/budget outcome. Carbon/energy effects are not included without an explicit restoration-energy/emissions accounting model.  
**Evidence:**
- Sharkey et al.-type interdependent restoration literature explicitly models work-crew movement through damaged transportation networks; representative peer-reviewed article: *Interdependent integrated network design and scheduling problems with movement of machines*, European Journal of Operational Research (2021). **B**.
- *Optimising repair sequences for interdependent infrastructure resilience: a simulation model of power and transportation networks* (2026), DOI `10.1080/10286608.2025.2602872` — road delays affect repair-crew arrival and power restoration. **B**.
- Coupled traffic-power resilience work also requires an open path for repair crews to reach damaged power equipment. **B**.

**Main uncertainties:** road blockage truth, repair duration, crew productivity, staging location, routing behavior.  
**Validation requirement:** event-level restoration milestones plus road-state/crew-route evidence; current H1 data do not provide microscopic crew trajectories.  
**Status:** `RETAIN_CORE_MECHANISM / EMPIRICAL_VALIDATION_LIMITED`.

---

### RS-04 — Transportation charging demand / V2G → grid state → operational energy/carbon

```math
\lambda_{EV}(t),SOC(t),u_c(t)
\rightarrow
P_{EV}(t)
\rightarrow
F_P(t)
\rightarrow
\{E_{grid},E_{curt},P_{peak}\}
\rightarrow
\{J_{energy},J_{carbon},J_{cost}\}.
```

A minimal operational carbon relation is admissible only after a defensible generation/emissions model is selected:

```math
J_{carbon}^{op}
=
\int_0^{T_L} e_{grid}(t)\,P_{grid}^{EV}(t)\,dt,
```

or through dispatch-derived marginal emissions if the model supports them.

**Dependency:** mobility/charging decisions → electrical load/flexibility; V2G creates a reverse flexibility pathway.  
**Resilience quantities:** peak loading, overload state, charging-service backlog, grid-service support.  
**Candidate interventions:** managed charging, V2G, renewable-aligned charging, storage, charger siting/capacity.  
**Sustainability outcomes:** operational energy, renewable curtailment/integration, operational carbon; cost secondary.  
**Evidence:**
- Kelly et al. (2015), *Sustainability, Resiliency, and Grid Stability of the Coupled Electricity and Transportation Infrastructures*, DOI `10.1061/(ASCE)IS.1943-555X.0000251` — explicitly motivates integrated multi-timescale sustainability/resilience analysis of coupled electricity/transport. **B**.
- Nature Energy (2022), *Charging infrastructure access and operation to reduce the grid impacts of deep electric vehicle adoption*, DOI `10.1038/s41560-022-01105-7` — charging infrastructure/control reshapes grid demand, storage needs, renewable excess and emissions. **A/B model-data**.
- NREL managed-charging review/synthesis reports benefits including emissions reduction, reliability and renewable-integration support across hundreds of studies. **A/B synthesis**.
- Prospective V2G life-cycle work shows V2G can facilitate variable-renewable integration and alter system emissions; DOI `10.1016/j.apenergy.2024.123618`. **B**.

**Main uncertainties:** driver charging behavior, generation mix, marginal versus average emissions, battery degradation, V2G participation, dispatch constraints.  
**Validation requirement:** actual charging/load profiles plus independent generation/emission data or a validated dispatch model.  
**Status:** `RETAIN_CONDITIONAL_CORE`; cannot enter final `J_carbon` until the emissions accounting architecture is frozen.

---

### RS-05 — Information → state/control quality → resilience; sustainability link conditional

```math
D_{0:t}
\rightarrow
b_t(Y)
\rightarrow
u_{control}(t)
\rightarrow
u_{physical}(t)
\rightarrow
\mathbf R.
```

Communication failure can also be represented as a contraction of feasible control/information availability.

**Dependency:** sensing/communication/inference → operational decision quality and remote-control capability.  
**Resilience quantities:** detection delay, control availability, restoration delay, service loss, posterior viable mass.  
**Candidate interventions:** sensing redundancy, communication backup, local fallback control, uncertainty-aware decision logic.  
**Sustainability outcome:** no direct generic mapping is admitted. Effects on accessibility, energy, carbon or cost must pass through an explicit physical intervention/operation pathway.  
**Evidence:** power–communication literature shows loss of monitoring/control can delay detection/restoration and propagate cyber-physical failures; representative review DOI `10.1049/iet-stg.2019.0202`. EV charging cyber-resilience literature also shows communication disruption can reduce charging service and capacity utilization. **B**.

**Main uncertainties:** observation error, communication availability, estimator calibration, cyber-failure model.  
**Validation requirement:** compare `P+T`, `P+T+I` under matched disturbances and independent observation-error/communication scenarios; sustainability mapping only after physical consequence is quantified.  
**Status:** `RETAIN_RESILIENCE_LAYER / SUSTAINABILITY_TRANSLATION_CONDITIONAL`.

---

### RS-06 — Organization → feasible control/resources → recovery; sustainability link conditional

```math
z_O(t)
\rightarrow
\mathcal U(z_I,z_O,t),\tau_{response}
\rightarrow
Y(t)
\rightarrow
\mathbf R.
```

**Dependency:** authority, crews, coordination, resource availability → feasible response actions/timing.  
**Resilience quantities:** response delay, repair sequence, recovery time, service loss.  
**Candidate interventions:** resource prepositioning, coordination protocols, crew allocation, authority escalation, cross-sector repair priorities.  
**Sustainability outcome:** cost and accessibility/service burden may follow through the physical recovery pathway, but no direct generic `O → sustainability` mapping is admitted.  
**Evidence:** interdependent restoration/resource-allocation literature demonstrates that crew allocation and recovery sequencing materially alter infrastructure recovery; this supports the resilience mechanism but not a universal sustainability translation. **B**.

**Main uncertainties:** actual crew availability, institutional rules, response times, coordination quality.  
**Validation requirement:** empirical organizational/resource data or a clearly bounded scenario experiment; current thesis evidence is insufficient for final calibration.  
**Status:** `RETAIN_RESILIENCE_LAYER / EMPIRICAL_GATE_OPEN`.

---

## 4. Evidence-strength matrix

| Pathway | `d_e → R_i` | `R_i → a_k` | `a_k → J_j` | Overall v1 status |
|---|---|---|---|---|
| RS-01 charging energization → mobility/access | **A/B** | **B** | **A/B** for accessibility | **CORE** |
| RS-02 signal power → road/access | **B** | **B** | **B** for accessibility | **CORE** |
| RS-03 road state → crew restoration → service burden | **B** | **B** | **C/B** for access/cost | **CORE MECHANISM; downstream conditional** |
| RS-04 EV charging/V2G → grid → energy/carbon | **A/B** | **A/B** | **A/B** with explicit dispatch/emissions model | **CONDITIONAL CORE** |
| RS-05 information → decision/resilience | **B** | **B** | **C** | **RESILIENCE CORE; sustainability conditional** |
| RS-06 organization → feasible control/recovery | **B** | **B** | **C** | **RESILIENCE CORE; empirical gate open** |

The weakest arrows are deliberately exposed rather than filled by narrative assumptions.

---

## 5. Mathematical consequence for Stage 6

Stage 6 shall not use a free-standing mapping `J_sus=f(R)`. The minimal admissible structure is pathway/intervention mediated:

```math
\boxed{
\Phi_{RS}
:\ (
\mathbf R,\mathbf a,\mathfrak M,\omega,T_L
)
\mapsto
\Delta\mathbf J_{\rm sus}^{core}
}
```

with the intervention experiment

```math
\mathbf a_k
\rightarrow
\mathfrak M_k
\rightarrow
Y_k(t)
\rightarrow
\mathbf R_k
\rightarrow
\mathbf J_{{\rm sus},k}.
```

For matched alternatives,

```math
\Delta\mathbf R_k=\mathbf R_k-\mathbf R_0,
\qquad
\Delta\mathbf J_{{\rm sus},k}=\mathbf J_{{\rm sus},k}-\mathbf J_{{\rm sus},0}.
```

The scientific test is whether resilience-improving alternatives remain ordered after sustainability consequences are evaluated; no equality or monotonicity is presumed.

---

## 6. What this matrix changes now

1. The thesis sustainability core is provisionally reduced to accessibility + operational energy + operational carbon.
2. Cost is retained initially as a budget/secondary outcome, not automatically mixed into a sustainability score.
3. Equity requires a separate population-disaggregation gate.
4. Material/resource burden is deferred from the minimal core unless lifecycle inventory is added.
5. Information and organization remain essential resilience layers, but their sustainability consequences must be mediated through physical service/operation pathways.
6. H1 remains the first empirical gate because the Stage-6 bridge is invalid if the underlying P–T causal dynamics cannot be validated.
7. No canonical H1–H5 file is rewritten by this v1 matrix.

## 7. Next admissible work

```math
\boxed{
\text{Outcome definitions/units}
\rightarrow
\text{data-source registry}
\rightarrow
\text{equation registry}
\rightarrow
\text{validation plan}
}
```

for `J_access`, `J_energy`, and `J_carbon`, while H1 raw-data qualification proceeds independently under its existing R1–R8 gate.
