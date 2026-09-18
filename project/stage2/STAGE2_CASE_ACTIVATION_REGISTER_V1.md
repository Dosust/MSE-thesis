# Stage 2 Activation Evidence Register v1

**Status:** EXECUTED — FOUR CURRENT CASE CANDIDATES  
**Case:** GreenEVT/SMART-DS Greensboro H1 Level-2 realization  
**Case-connection authority:** `STAGE2_CASE_CONNECTION_REGISTER_V1.md`

## 1. Principle

A case connection may exist while the mechanism is inactive:

```math
\boxed{
G_{2-C}=PASS
\not\Rightarrow
\mathcal A_e(t)=1.
}
```

Activation must be stated as an explicit predicate supported by the case representation.

## 2. Activation register

| Relation | Parent | Activation predicate | Evidence available | Missing evidence | G2-A |
|---|---|---|---|---|---|
| `SIGNAL_P_to_T` | Q01 | mapped signal depends on mapped power source AND source service insufficient AND backup unavailable/exhausted | signal controllers exist; generic mechanism literature supports power dependence | signal-to-source mapping; controller demand; backup type/endurance; outage/fallback state | **BLOCKED** |
| `EV_P_to_T` | Q03 | charging demand exists AND grid/charger service is unavailable or constrained enough to reduce served charging | grid-connected charging interface exists; charging demand schedules exist | native case lacks verified energization/availability -> served-rate/fulfillment response law and outage activation state | **BLOCKED** |
| `EV_T_to_P` | Q05 | scenario vehicle is EV AND `charging_start <= t <= charging_end` | directly encoded in GreenEVT query logic and vehicle table | local charger-power parameter is scenario-specified rather than independently validated | **PASS** |
| `REPAIR_T_to_P` | Q06 | repair job is released AND field access is required AND road state changes feasible route/travel time to required resource | generic mechanism evidence; road and power topologies exist | repair job/task; field-vs-remote requirement; crew/resource origin; route set; time-varying access state | **BLOCKED** |

## 3. Q01 activation

Candidate predicate:

```math
\mathcal A_{Q01}(t)
=
\mathbf 1[
C_{sig\leftrightarrow P}=1
\land
\phi_P(t)<\phi_{req}
\land
B_{eff}(t)=0
].
```

where:
- (C_{sig\leftrightarrow P}): verified signal-to-power connection;
- (phi_P(t)): realized electrical service;
- (phi_{req}): controller electrical-service requirement;
- (B_{eff}(t)): effective backup-service indicator.

Current case does not observe all required terms.

```text
G2-A(Q01) = BLOCKED
```

## 4. Q03 activation

Candidate predicate:

```math
\mathcal A_{Q03}(t)
=
\mathbf 1[
D_{chg}(t)>0
\land
P_{avail}(t)<P_{req}(t)
].
```

Possible receiver response:

```math
P_{served}(t)
=
\min\{P_{req}(t),P_{avail}(t),P_{EVSE}^{max}\}.
```

GreenEVT establishes charging demand and bus association, but the upstream baseline does not by itself establish the thesis-specific (P_{avail}\rightarrow P_{served}\rightarrow) mobility-service response under outages/constraints.

```text
G2-A(Q03) = BLOCKED
```

This block is not evidence against the mechanism. It means the required activation state is not yet case-qualified.

## 5. Q05 activation

The exact GreenEVT implementation defines:

```math
\mathcal A_{Q05,v}(t)
=
\mathbf 1[
ev_v=1
\land
t_{start,v}\le t\le t_{end,v}
].
```

For bus (b):

```math
N_{EV,b}^{chg}(t)
=
\sum_v
\mathbf 1[
bus_v=b
]
\mathcal A_{Q05,v}(t).
```

The resulting load increment is:

```math
\Delta P_b(t)
=
N_{EV,b}^{chg}(t)P_{EV}^{chg}.
```

The upstream `query_charging_evs_per_bus_by_time()` query implements the activation logic by requiring:
- `charging_start <= timestamp`;
- `charging_end >= timestamp`;
- `ev == 1`;
- matching scenario ID.

Therefore:

```text
G2-A(Q05) = PASS
```

Parameter note: a configured charger-power value is sufficient to execute a scenario but is not automatically a calibrated/validated mechanism parameter.

## 6. Q06 activation

Candidate predicate:

```math
\mathcal A_{Q06}(t)
=
\mathbf 1[
D_P=1
\land
F_{field}=1
\land
R_{resource}=1
].
```

where:
- (D_P): power asset requires restoration action;
- (F_{field}): task requires physical field intervention;
- (R_{resource}): crew/mobile resource must reach the target.

The road-network state then affects:
- route feasibility;
- travel time;
- resource arrival;
- repair start;
- restoration time.

These task/resource objects are not instantiated in the current case.

```text
G2-A(Q06) = BLOCKED
```

## 7. Activation conclusion

```text
Q01 SIGNAL_P_to_T  BLOCKED
Q03 EV_P_to_T      BLOCKED
Q05 EV_T_to_P      PASS
Q06 REPAIR_T_to_P  BLOCKED
```

Only Q05 presently has a case-native, machine-auditable activation predicate.

## 8. Falsification hooks carried to G2

### Q01
- verified source loses required service beyond backup endurance but signal control remains normal without alternate supply;
- asserted supply mapping is wrong;
- signal failure is caused by an independent controller/communication fault.

### Q03
- grid/charger available power falls below demand but served charging remains unchanged because an unmodeled alternate source fully supplies it;
- mobility/charging outcome changes for an independent station fault rather than power availability;
- proposed fulfillment relation fails conservation or limit tests.

### Q05
- with all other states held fixed, changing active charging-EV count does not change the corresponding OpenDSS bus load as specified;
- EV flag/time-window logic does not match the load modification;
- bus mapping used by charging records does not resolve to the modified electrical load.

### Q06
- restoration task is fully remote;
- pre-positioned/on-site resource removes road dependence;
- route/access changes do not alter arrival/intervention timing at the selected resolution;
- repair/material/authorization time dominates such that transportation state has no identifiable contribution.

## 9. Evidence pointers

GreenEVT upstream commit `6aff1cac48869ccfa0183643979f5f04b04e1124`:
- `scripts/generatevehicles.py`
- `scripts/assign_charging_times_to_vehicles.py`
- `scripts/solve_opendss.py`

Thesis repository:
- `models/H1/level2/registries/dependency_registry_v1.csv`
- `project/stage2/STAGE2_CAUSAL_QUALIFICATION_FRAMEWORK_V1.md`
- `project/stage2/STAGE2_G2_GATE_SPECIFICATION_V1.md`
