# Stage 2 Evidence Register v2 — P↔T Causal Qualification

**Status:** ACTIVE WORKING CAUSAL-EVIDENCE REGISTER — NO CAUSAL RELATION ACCEPTED  
**Date:** 2026-09-18  
**Supersedes for active use:** `STAGE2_EVIDENCE_REGISTER_V1.md`  
**Primary evidence authority:** `supporting_evidence/STAGE2_CLAIM_LEVEL_EVIDENCE_LEDGER_V2.md`  
**Input object:** frozen Stage-1 `mathfrak r_e^(1)`.

## 1. Purpose

This register converts prior mechanism evidence into explicit, falsifiable Stage-2 candidate dossiers without crossing the case-specific causal-acceptance boundary.

~~~math
\boxed{
\mathfrak r_e^{(1)}
\rightarrow
\text{mechanism + activation + uncertainty + validity + falsification}
\rightarrow
G_2(e)
}
~~~

The first qualification priority is:

~~~math
\boxed{
P\rightarrow T:\ \text{signal electrical service}
\qquad
T\rightarrow P:\ \text{repair/restoration access}
}
~~~

These are selected first because they are directly relevant to the thesis scope, physically/operationally interpretable, supported by multiple precedents, and testable with case/simulation evidence.

## 2. Decision vocabulary

`OPEN` is a workflow state. Final G2 component decisions remain `PASS / FAIL / BLOCKED`.

A literature-supported mechanism remains `OPEN` until the actual thesis case source/interface/receiver connection is verified.

~~~math
\boxed{
\text{literature-mechanism evidence}
\neq
\text{case connection}
\neq
G_2(e)=\mathrm{PASS}
}
~~~

## 3. Core P0 register

| Field | `M2-PT-01` — P→T signal electrical service | `M2-TP-01` — T→P repair/restoration access |
|---|---|---|
| tested direction | P→T | T→P |
| source state | supplying bus/feeder/electrical-service state | road-link/route accessibility and travel-time state |
| receiver state | traffic-signal/controller operating state and resulting intersection-control state | mobile-resource/crew arrival and power-restoration task/trajectory |
| mechanism class | `M-PHYS-ELEC` | `M-MOB-ACCESS` |
| path | DIRECT at electrical interface; transportation effect may be mediated through intersection control | MEDIATED: road/route → crew or mobile resource → field intervention → power restoration |
| frozen exchange semantic `Phi_e` | required electrical service to signal/control equipment | accessibility / travel-time / route-feasibility service |
| realized interface signal `phi_e(t)` | verified electrical service delivered at controller/signal interface | feasible route state and realized resource travel/arrival process |
| parameter status | `UNESTIMATED` | `UNESTIMATED` |
| current aggregate G2 | **OPEN** | **OPEN** |

## 4. P→T dossier — `M2-PT-01`

### 4.1 Exact causal claim

> When a traffic-signal/controller requires external electrical service and no adequate substitute source maintains the required service, degradation or loss of the supplying electrical service can degrade or interrupt signal functionality; the resulting change in intersection control can alter roadway capacity and traffic state within the declared validity domain.

### 4.2 Mechanism chain

~~~math
P_{service}(t)
\rightarrow
\phi_{sig}(t)
\rightarrow
S_{sig}(t)
\rightarrow
C_{int}(t)
\rightarrow
X_T(t)
~~~

where:

- `P_service(t)`: upstream/local electrical-service state;
- `phi_sig(t)`: realized electrical service at the signal interface;
- `S_sig(t)`: controller/signal functional state;
- `C_int(t)`: effective intersection-control/capacity state;
- `X_T(t)`: transportation response variables such as flow, speed, delay or travel time.

This is a causal-evidence chain, not yet the Stage-3 dynamic law.

### 4.3 Prior evidence basis

| Evidence ID | Source role |
|---|---|
| `S2-C009` | direct P→T traffic-signal power mechanism precedent |
| `S2-C018` | open-full-text power-loss → signal-loss → capacity/traffic consequence model |
| `S2-C019` | independent bidirectional lifeline model: power outage affects traffic lights and intersection throughput |
| `S2-C022` | joint P–T repair-sequencing model: power failures create transportation delay via signal outages |
| `S2-C004/C006/C007` | interface/service and functional-dependency semantics |

### 4.4 Activation predicate

A conservative binary form is:

~~~math
\mathcal A_{PT01}(t)=
\mathbf 1[
R_{ext}=1
\land
\phi_{sig}(t)<\phi_{req}
\land
B_{eff}(t)=0
]
~~~

with:

- `R_ext=1`: signal/controller actually requires the declared external electrical service;
- `phi_req`: equipment-specific acceptable service requirement;
- `B_eff(t)=0`: backup/substitute supply is absent, unavailable, exhausted or insufficient.

If equipment behavior is not binary, activation must be generalized rather than forcing this indicator form.

### 4.5 Required case-connection evidence

A case relation cannot pass `G2-C` without:

1. signal/controller asset ID and geometry;
2. verified bus/feeder/circuit/service crosswalk;
3. controller voltage/power/service requirements;
4. backup UPS/battery/generator/local-source configuration and endurance;
5. switching/protection/fallback-control logic;
6. timestamped or scenario-resolved power-service state;
7. timestamped or scenario-resolved signal/controller state where available.

### 4.6 Receiver response variables

Potential observable outcomes are kept separate:

~~~math
y_{rec}^{PT01}
\in
\{
\text{signal functional state},
\text{intersection control state},
\text{effective capacity},
\text{queue},
\text{delay},
\text{travel time},
\text{speed},
\text{flow}
\}.
~~~

The thesis must choose only variables supported by the intended model/data.

### 4.7 Uncertainty partition

~~~math
\mathcal U_{PT01}=
(
U^{conn},
U^{act},
U^{intf},
U^{time},
U^{resp},
U^{alt}
)
~~~

Working interpretation:

- `U^conn`: uncertainty in feeder/circuit↔signal mapping;
- `U^act`: uncertainty in outage threshold, backup availability/endurance, control fallback;
- `U^intf`: uncertainty in actual electrical service delivered at equipment interface;
- `U^time`: outage onset/duration and backup depletion timing;
- `U^resp`: uncertainty in signal-loss → intersection-capacity/traffic-response representation;
- `U^alt`: communication fault, local equipment fault, maintenance, police/manual control, hazard-imposed road loss or other explanation.

### 4.8 Validity domain

At minimum declare:

~~~text
signal/controller technology
electrical supply architecture
backup/substitute configuration
intersection/control type
traffic-demand regime
operating/disruption mode
outage duration
spatial resolution
jurisdiction/equipment requirements
scenario/hazard context
~~~

### 4.9 Falsification and revision tests

The candidate must be rejected or revised if one or more of the following is demonstrated within the claimed domain:

1. the declared electrical service is lost beyond verified backup endurance while the controller remains normally functional with no alternative supply path;
2. the identified signal is not actually supplied by the declared power asset/interface;
3. the signal-state change is caused by a non-power fault while electrical service remains adequate;
4. the assumed intersection-control/capacity change does not occur under the actual fallback mode;
5. the traffic effect attributed to signal power is explained by direct road damage/demand changes without a signal-mediated contribution.

### 4.10 Current G2 state

| Gate | State | Evidence/readiness |
|---|---|---|
| `G2-M` | OPEN — prior evidence strong | multiple direct mechanism precedents |
| `G2-C` | OPEN | thesis-case feeder/circuit↔signal crosswalk missing |
| `G2-X` | OPEN | case electrical service interface must be verified |
| `G2-A` | OPEN | backup/threshold/fallback state case-specific |
| `G2-E` | OPEN | empirical/operational thesis-case evidence incomplete |
| `G2-V` | OPEN | validity domain not yet instantiated |
| `G2-F` | OPEN — test specified | observable reject/revise conditions defined |

~~~math
\boxed{G_2(M2\text{-}PT\text{-}01)=\mathrm{OPEN}}
~~~

## 5. T→P dossier — `M2-TP-01`

### 5.1 Exact causal claim

> When restoration of a failed/degraded power asset requires a crew, mobile generator, mobile storage resource or other physical field resource to reach a target location, the transportation network's route feasibility and travel conditions can alter resource arrival time and feasible intervention, thereby changing the power-restoration trajectory within the declared validity domain.

### 5.2 Mechanism chain

~~~math
X_T^{route}(t)
\rightarrow
R_{feas}(t),T_{travel}
\rightarrow
T_{arrive}
\rightarrow
A_{field}
\rightarrow
X_P^{restore}(t)
~~~

This path is explicitly mediated by the mobile actor/resource.

### 5.3 Prior evidence basis

| Evidence ID | Source role |
|---|---|
| `S2-C010` | direct transportation-access-for-power-repair precedent |
| `S2-C011` | MPS/repair-crew schedules constrained by transportation network and disrupted routes |
| `S2-C020` | stochastic traffic-congestion/travel-time treatment for RC/TPS restoration |
| `S2-C021` | road states constrain repair-crew routing and feasible restoration decisions |
| `S2-C022` | two-way P–T simulation: transportation delay changes crew arrival to damaged power nodes |
| `S2-C023` | real-time MEG routing/travel time affects restoration speed |
| `S2-C019` | phase-specific restoration mechanism: road system affects emergency-resource scheduling |

### 5.4 Activation predicate

~~~math
\mathcal A_{TP01}(t)=
\mathbf 1[
D_P=1
\land
F_{field}=1
\land
M_{res}=1
]
~~~

where:

- `D_P=1`: a power restoration/field-support task exists;
- `F_field=1`: the task requires physical field/mobile intervention;
- `M_res=1`: a mobile resource/crew must move through the transportation network.

Activation is therefore **recovery/task dependent**, not continuously active.

### 5.5 Required case-connection evidence

1. failed/target power asset ID and task requirement;
2. field intervention versus remote-restoration classification;
3. crew/MPS/MEG/MESS resource type and capability;
4. resource origin/depot/current location;
5. road-network crosswalk to target access point;
6. feasible route set and vehicle restrictions;
7. time-dependent closures, capacities, speeds and congestion state;
8. dispatch/mobilization time;
9. repair/service duration and task precedence;
10. alternative crews/resources/routes and remote switching possibilities.

### 5.6 Delay decomposition

Do not identify total restoration time with transportation travel time:

~~~math
T_{restore}
=
T_{detect}
+
T_{authorize}
+
T_{mobilize}
+
T_{travel}
+
T_{repair}
+
T_{reenergize}.
~~~

The T→P mobility mechanism acts directly on `T_travel` and route feasibility, and may interact with mobilization/dispatch logic. Other terms require separate evidence.

### 5.7 Uncertainty partition

~~~math
\mathcal U_{TP01}=
(
U^{conn},
U^{act},
U^{route},
U^{travel},
U^{resource},
U^{task},
U^{alt}
)
~~~

Working interpretation:

- `U^conn`: uncertainty in target-asset↔access-point↔road mapping;
- `U^act`: whether the restoration task truly requires field access;
- `U^route`: road passability, closure and feasible-path uncertainty;
- `U^travel`: congestion/speed/travel-time uncertainty;
- `U^resource`: crew/resource location, availability and capability;
- `U^task`: repair duration, precedence and material requirements;
- `U^alt`: remote switching, alternate resource onsite, alternative route, safety/authorization/material delays dominating restoration.

### 5.8 Validity domain

At minimum declare:

~~~text
recovery/restoration phase
power asset/task class
resource/vehicle class
road-network and access resolution
hazard-induced road-state regime
congestion/travel-time regime
resource origin/depot assumptions
remote-restoration capability
safety/authority constraints
time horizon
~~~

### 5.9 Falsification and revision tests

The candidate must be rejected or revised if:

1. the target task does not require physical access;
2. the proposed route/access path is not used or necessary;
3. restoration occurs through remote switching or an already-onsite resource;
4. route/travel-state changes do not alter arrival/intervention timing within the claimed sensitivity domain;
5. repair/material/authorization time fully dominates and the proposed transportation relation contributes no identifiable effect at the declared resolution;
6. a feasible alternative route/resource removes the claimed dependency and was omitted from the candidate.

### 5.10 Current G2 state

| Gate | State | Evidence/readiness |
|---|---|---|
| `G2-M` | OPEN — prior evidence strong | multiple direct restoration/mobility precedents |
| `G2-C` | OPEN | thesis-case asset↔route↔resource mapping missing |
| `G2-X` | OPEN | accessibility/travel-time service must be case-operationalized |
| `G2-A` | OPEN | task-specific field-intervention requirement must be verified |
| `G2-E` | OPEN | case operational/empirical evidence incomplete |
| `G2-V` | OPEN | vehicle/route/task validity domain not instantiated |
| `G2-F` | OPEN — tests specified | observable reject/revise conditions defined |

~~~math
\boxed{G_2(M2\text{-}TP\text{-}01)=\mathrm{OPEN}}
~~~

## 6. P1 mechanisms retained but not promoted

| ID | Direction | Mechanism | Current evidence state | Required next evidence |
|---|---|---|---|---|
| `M2-PT-02` | P→T | EV charging-service availability | OPEN | direct EVSE/grid service evidence + case crosswalk + charging consequence |
| `M2-TP-02` | T→P | EV charging demand | OPEN | charging-session/load evidence + distribution response + confounder control |
| `M2-TP-03` | T→P | V2G/mobile-storage support | OPEN — direct V2G gap retained | dedicated full-text V2G/aggregator/bidirectional-EVSE evidence |

No P1 mechanism inherits a PASS from the P0 literature.

## 7. Common-cause exclusion

~~~math
\eta\rightarrow P,qquad \eta\rightarrow T
\not\Rightarrow
P\rightarrow T\ \text{or}\ T\rightarrow P.
~~~

Flood, heat, earthquake, debris or other hazards remain exogenous/context causes unless an additional cross-system mechanism is separately qualified.

## 8. Stage-2 uncertainty rule

Uncertainty is not represented by one scalar by default. For every candidate, the uncertainty object must be traceable to the mechanism:

~~~math
\boxed{
\mathcal U_e=
\{
\text{connection},
\text{activation},
\text{interface},
\text{timing},
\text{response},
\text{resource/task},
\text{alternative explanation}
\}
}
~~~

Only applicable components are instantiated for a given mechanism.

## 9. Parameter boundary

~~~math
\boxed{
G_2(e)=\mathrm{PASS}
\not\Rightarrow
S_e^\theta=\mathrm{VALIDATED}
}
~~~

and

~~~math
\boxed{
S_e^\theta=\mathrm{UNESTIMATED}
\not\Rightarrow
G_2(e)=\mathrm{FAIL}.
}
~~~

Causal existence and numerical parameter readiness remain separate.

## 10. Immediate case-evidence objects required next

The next valid execution artifacts are:

~~~text
PT01_CASE_CONNECTION_REGISTER
  signal_id -> controller -> circuit/feeder/bus -> backup configuration

TP01_CASE_CONNECTION_REGISTER
  failed_power_asset -> access point -> feasible road route(s)
  -> crew/mobile-resource origin -> task requirement

PT01_ACTIVATION_AND_FALSIFICATION_TEST
TP01_ACTIVATION_AND_FALSIFICATION_TEST
P0_VALIDITY_DOMAIN_REGISTER
P0_UNCERTAINTY_REGISTER
~~~

Until these are instantiated:

~~~math
\boxed{
\mathbb I_{acc}=\varnothing
}
~~~

## 11. Stage-3 boundary

Simulation may test consequences of a declared mechanism hypothesis, but it may not manufacture the missing case connection or causal qualification.

~~~math
\boxed{
\text{Stage-2 evidence}
\rightarrow
G_2
\rightarrow
\mathfrak I_e
\rightarrow
G_{2\to3}
\rightarrow
F_{\mathcal G}^{m}
}
~~~
