# Stage 2 Case Uncertainty Register v1

**Status:** EXECUTED — CASE-SPECIFIC UNCERTAINTY DISAGGREGATION  
**Case:** GreenEVT/SMART-DS Greensboro H1 Level-2 realization  
**Related records:** `STAGE2_CASE_CONNECTION_REGISTER_V1.md`, `STAGE2_CASE_ACTIVATION_REGISTER_V1.md`, `STAGE2_CASE_G2_AUDIT_V1_2026-09-19.md`

## 1. Rule

Uncertainty is represented by mechanism-specific components and is never collapsed into a default confidence score:

```math
\mathcal U_e=
(U_e^{conn},
U_e^{act},
U_e^{intf},
U_e^{time},
U_e^{resp},
U_e^{resource},
U_e^{alt}).
```

The labels below are qualitative workflow states only:

```text
LOWER / MATERIAL / HIGH / NOT-APPLICABLE
```

They are not probabilities and not coupling strengths.

## 2. Register

| Relation | U_conn | U_act | U_intf | U_time | U_resp | U_resource | U_alt | Dominant uncertainty |
|---|---|---|---|---|---|---|---|---|
| SIGNAL_P_to_T / Q01 | HIGH | HIGH | MATERIAL | HIGH | MATERIAL | N/A | MATERIAL | actual signal electrical supply mapping + backup/endurance |
| EV_P_to_T / Q03 | LOWER | HIGH | MATERIAL | MATERIAL | HIGH | N/A | MATERIAL | energization/constraint -> served charging/fulfillment response |
| EV_T_to_P / Q05 | LOWER | LOWER | LOWER | MATERIAL | MATERIAL | N/A | MATERIAL | charging-power/behavioral parameterization and synthetic-to-real transfer |
| REPAIR_T_to_P / Q06 | HIGH | HIGH | MATERIAL | HIGH | MATERIAL | HIGH | HIGH | task/access/crew/resource mapping and travel/restoration timing |

## 3. Q01 — SIGNAL_P_to_T

- **Connection:** HIGH — no verified signal -> feeder/circuit/bus service record.
- **Activation:** HIGH — backup state/endurance and service threshold are unknown.
- **Interface:** MATERIAL — electrical service semantics are established, realized case service is not.
- **Timing:** HIGH — outage-to-backup-depletion and controller/fallback timing are unknown.
- **Response:** MATERIAL — exact controller fallback/capacity effect is case-dependent.
- **Alternatives:** MATERIAL — alternate supply, local UPS/generator, controller fault, communications fault, direct road damage.

No causal-strength value may be inferred from this uncertainty.

## 4. Q03 — EV_P_to_T

- **Connection:** LOWER — GreenEVT explicitly associates charging demand with distribution buses.
- **Activation:** HIGH — case-specific availability/energization threshold for reduced service is not yet qualified.
- **Interface:** MATERIAL — requested vs available vs served charging power must be separated.
- **Timing:** MATERIAL — charging interval, outage onset, queue/fulfillment delay may differ.
- **Response:** HIGH — served-rate/mobility fulfillment response is not native in the baseline GreenEVT implementation.
- **Alternatives:** MATERIAL — alternate charging, onsite storage, backup generation, driver substitution.

## 5. Q05 — EV_T_to_P

- **Connection:** LOWER — vehicle/bus mapping is explicit in the synthetic case.
- **Activation:** LOWER — EV flag and charging time-window logic are explicit.
- **Interface:** LOWER — charging demand is explicitly translated to OpenDSS load.
- **Timing:** MATERIAL — finite simulation step and assigned charging schedules affect temporal resolution.
- **Response:** MATERIAL — the direct load increment is explicit, but feeder voltage/overload response depends on the electrical model and parameters.
- **Alternatives:** MATERIAL — charging schedule/model assumptions, charger power, charging efficiency, uncontrolled external demand not represented.
- **Transfer:** MATERIAL — the GreenEVT mapping is a realistic-synthetic construction, not observed Greensboro utility service records.

Causal PASS does not reduce these parameter/model-transfer uncertainties to zero.

## 6. Q06 — REPAIR_T_to_P

- **Connection:** HIGH — failed asset/task/access/resource crosswalk is absent.
- **Activation:** HIGH — field requirement and job release are unobserved.
- **Interface:** MATERIAL — physical access/travel is interpretable but not case-realized.
- **Timing:** HIGH — mobilization, route travel, repair duration, precedence and re-energization are unknown.
- **Response:** MATERIAL — travel-time contribution to restoration time is case/task dependent.
- **Resource/task:** HIGH — depot, crew class, materials and alternatives are missing.
- **Alternatives:** HIGH — remote switching, pre-positioned resources, alternate routes/crews, repair-duration dominance.

## 7. Consequence for G2

```text
Q01 BLOCKED: uncertainty is dominated by missing case connection and activation evidence.
Q03 BLOCKED: connection exists, but activation/response uncertainty remains decisive.
Q05 PASS: residual uncertainty affects parameters/model transfer, not existence of the synthetic-case causal mechanism.
Q06 BLOCKED: case connection, activation, timing and resource uncertainty are decisive.
```

## 8. Parameter-status separation

```math
G_2(e)=PASS
\not\Rightarrow
S_e^\theta=VALIDATED.
```

In particular, Q05 remains causally accepted while its charger-power/behavioral parameters still require Stage-2->3 readiness and parameter-status qualification.
