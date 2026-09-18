# Stage 2 Case-Specific G2 Audit v1 — 2026-09-19

**Status:** EXECUTED — CASE-SPECIFIC CAUSAL QUALIFICATION  
**Case:** GreenEVT/SMART-DS Greensboro H1 Level-2 realization  
**Inputs:**
- `STAGE2_CASE_PRESENCE_AUDIT_V1_2026-09-19.md`
- `STAGE2_CASE_CONNECTION_REGISTER_V1.md`
- `STAGE2_CASE_ACTIVATION_REGISTER_V1.md`
- `STAGE2_G2_GATE_SPECIFICATION_V1.md`

## 1. Decision rule

For a case relation (e):

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

A required BLOCKED component makes the aggregate BLOCKED. A decisive FAIL makes the aggregate FAIL. Only seven PASS decisions create a causally qualified case interdependency.

Parameter readiness is separate:

```math
G_{2\to3}(e)=G_2(e)\land G_P(e).
```

## 2. Component results

| Relation | Parent | G2-M | G2-C | G2-X | G2-A | G2-E | G2-V | G2-F | Aggregate |
|---|---|---|---|---|---|---|---|---|---|
| `SIGNAL_P_to_T` | Q01 | PASS | BLOCKED | PASS | BLOCKED | BLOCKED | PASS | PASS | **BLOCKED** |
| `EV_P_to_T` | Q03 | PASS | PASS | PASS | BLOCKED | BLOCKED | PASS | PASS | **BLOCKED** |
| `EV_T_to_P` | Q05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| `REPAIR_T_to_P` | Q06 | PASS | BLOCKED | PASS | BLOCKED | BLOCKED | PASS | PASS | **BLOCKED** |

No G2 decision is issued for Q02,Q04,Q07-Q13 because no case-specific relation instance is currently registered for those parent families.

## 3. Q01 — SIGNAL_P_to_T

### Exact claim
When a case-mapped traffic signal/controller requires electrical service from a case-mapped power source and no adequate backup maintains that service, insufficient/lost power can change signal control state and thereby transportation operation.

### Gate findings
- **G2-M PASS:** physically interpretable and strongly supported by literature/engineering practice.
- **G2-C BLOCKED:** no verified signal/controller -> circuit/feeder/bus service mapping.
- **G2-X PASS:** exchanged service is electrical power/availability to the controller.
- **G2-A BLOCKED:** backup configuration/endurance and case source state are not known.
- **G2-E BLOCKED:** generic evidence is strong, but decisive case evidence is missing.
- **G2-V PASS:** validity can be limited to mapped electrically dependent signal controllers under stated backup conditions.
- **G2-F PASS:** concrete falsifiers are defined.

### Decision
```text
G2(SIGNAL_P_to_T) = BLOCKED
```

The block is epistemic/case-specific, not a rejection of the mechanism family.

## 4. Q03 — EV_P_to_T

### Exact claim
When EV charging demand is connected to a distribution-bus charging interface, insufficient bus/charger electrical availability can reduce served charging and mobility-energy fulfillment.

### Gate findings
- **G2-M PASS:** physical service mechanism is defensible.
- **G2-C PASS:** GreenEVT explicitly connects EV charging to distribution buses.
- **G2-X PASS:** exchanged service is electrical power availability/served charging power.
- **G2-A BLOCKED:** the native case does not yet qualify the bus energization/constraint -> served charging response under outage/stress.
- **G2-E BLOCKED:** literature and architecture support the mechanism, but the thesis-specific case response is not yet evidenced/implemented sufficiently for causal acceptance.
- **G2-V PASS:** validity domain can be restricted to GreenEVT-style grid-connected EV charging.
- **G2-F PASS:** conservation/limit and alternate-supply falsifiers are explicit.

### Decision
```text
G2(EV_P_to_T) = BLOCKED
```

## 5. Q05 — EV_T_to_P

### Exact claim

For GreenEVT scenario (s), an EV (v) associated with electrical bus (b) contributes charging demand to that bus when the EV flag is active and the simulation time lies within the vehicle charging interval.

```math
\mathcal A_v(t)
=
\mathbf1[
ev_v=1
\land
t_{start,v}\le t\le t_{end,v}
].
```

```math
N_{EV,b}^{chg}(t)
=
\sum_v
\mathbf1[bus_v=b]\mathcal A_v(t).
```

```math
\boxed{
\Delta P_b(t)
=
N_{EV,b}^{chg}(t)P_{EV}^{chg}.
}
```

### Gate findings

#### G2-M — PASS
The mechanism is direct and non-circular: active EV charging adds electrical demand at the associated distribution bus.

#### G2-C — PASS
The GreenEVT vehicle records encode `sumo_edge`, `bus_name`, EV status and charging times. The OpenDSS solver groups charging EVs by `bus_name` and modifies the corresponding bus load.

#### G2-X — PASS
The exchanged quantity is charging electrical demand, represented in kW in the OpenDSS load update.

#### G2-A — PASS
The source code explicitly defines activation using EV status, charging interval and scenario ID.

#### G2-E — PASS
The evidence portfolio includes:
1. the GreenEVT peer-reviewed testbed architecture;
2. exact upstream source code implementing the mapping and load update;
3. exact materialized GreenEVT critical source objects in the thesis audit;
4. the H1 Level-2 dependency registry marking `EV_T_to_P` EVIDENCE_SUPPORTED;
5. established EV-grid literature supporting charging demand as a T->P mechanism.

The claim is deliberately limited to the synthetic-testbed case and does not assert observed Greensboro customer-service wiring.

#### G2-V — PASS
Validity domain:

```text
system: GreenEVT/SMART-DS Greensboro realistic-synthetic testbed
transport mode: road EV
interaction: grid-connected charging demand
mapping: GreenEVT vehicle/parcel/bus association
time semantics: configured charging interval and simulation step
receiver: OpenDSS distribution-bus load
excluded: V2G/export, observed real utility wiring, charger outage response, unmanaged external charging not represented by the scenario
```

#### G2-F — PASS
The claim is falsified/revised if:
- active charging-EV records do not map to the modified bus;
- the EV/time-window query does not control charging load;
- holding baseline load fixed, changing (N_{EV,b}^{chg}) produces no specified load change;
- the bus mapping fails source-integrity checks.

### Aggregate decision

```math
\boxed{
G_2(EV\_T\_to\_P)=PASS.
}
```

The accepted case relation is:

```math
\boxed{
\mathfrak I_{EV,T\to P}
=
(\mathcal C_e,\Sigma_e,\Pi_e,S_e^\theta).
}
```

Parameter status:

```text
S_e^theta = UNESTIMATED
```

for causal-governance purposes: a scenario charging-power value can be configured, but the local mechanism parameter is not yet independently calibrated/validated.

Therefore:

```math
\boxed{
G_2=PASS
\not\Rightarrow
G_{2\to3}=PASS.
}
```

Stage-3 parameter/readiness qualification remains open.

## 6. Q06 — REPAIR_T_to_P

### Exact claim
When a damaged power asset requires a field resource, road-network state can change route feasibility/travel time and therefore the restoration trajectory.

### Gate findings
- **G2-M PASS:** strong engineering/literature mechanism.
- **G2-C BLOCKED:** no case task/access/resource crosswalk.
- **G2-X PASS:** exchanged/enabling service is physical access/travel capacity.
- **G2-A BLOCKED:** repair job, field-access requirement and resource state are not instantiated.
- **G2-E BLOCKED:** generic evidence is strong but case evidence is incomplete.
- **G2-V PASS:** validity can be restricted to field-required restoration tasks.
- **G2-F PASS:** remote restoration, pre-positioned resources, alternate routes and immaterial travel-time effects are explicit falsifiers/substitutes.

### Decision
```text
G2(REPAIR_T_to_P) = BLOCKED
```

## 7. Accepted causal set after audit

Before this audit:

```math
\mathbb I_{acc}=\varnothing.
```

After this case-specific audit:

```math
\boxed{
\mathbb I_{acc}^{case}
=
\{\mathfrak I_{EV,T\to P}\}.
}
```

This is a **synthetic-case causal acceptance** with a declared validity domain. It is not evidence that the GreenEVT bus-to-vehicle association is observed real-world Greensboro utility wiring.

Blocked set:

```math
\boxed{
\mathbb I_{blocked}^{case}
=
\{
SIGNAL_{P\to T},
EV_{P\to T},
REPAIR_{T\to P}
\}.
}
```

## 8. Stage-3 prohibition remains active

No blocked relation may enter Stage 3 as an accepted causal coupling.

For the sole G2-PASS relation, Stage-3 handoff remains conditional on parameter/readiness audit:

```math
\mathfrak I_{EV,T\to P}
\xrightarrow{G_P\ ?}
F_{\mathcal G}^{m}.
```

No missing parameter, delay, queue law or empirical validation may be manufactured by simulation.

## 9. Immediate next gates

1. `SIGNAL_P_to_T`: obtain/construct-with-explicit-synthetic-label signal -> power-source crosswalk and backup assumptions; otherwise retain BLOCKED.
2. `EV_P_to_T`: specify and verify bus/charger availability -> served charging/fulfillment response and activation.
3. `REPAIR_T_to_P`: instantiate failed asset -> field task -> access point -> route(s) -> resource origin.
4. `EV_T_to_P`: execute parameter-status and Stage-2->3 readiness audit without reopening causal status unless contradictory evidence appears.
