# Stage 3 — EV Charging Parameter Authority V1

**Date:** 2026-09-19  
**Case role:** `C_DEV_GREENSBORO_GREENEVT_V1`  
**Mechanism:** `EV_T_to_P` / Q05  
**Purpose:** resolve the 7.2 kW versus 7.5 kW GreenEVT source discrepancy without inventing a parameter or claiming empirical charger calibration.

## 1. Scientific question

For the accepted GreenEVT mechanism

```math
P_b^{new}(t)
=
P_b^{base}(t)
+
N_{EV,b}^{chg}(t)P_{EV}^{chg},
```

what value/status may be assigned to

```math
P_{EV}^{chg}
```

for the **C_DEV GreenEVT source-backed benchmark**?

## 2. Evidence hierarchy

### E1 — peer-reviewed GreenEVT article

Nilsson, Aquino, Coogan, and Molzahn, *GreenEVT: Greensboro Electric Vehicle Testbed*, IEEE Systems Journal, 18(1), 600–611 (2024), DOI: `10.1109/JSYST.2023.3343692`.

The paper states that the testbed's default EV charging representation uses a constant **7.2 kW per EV**, chosen to represent common Level-2 equipment.

Evidence role:

```text
SOURCE-DEFINED BENCHMARK ASSUMPTION
NOT CASE-MEASURED CHARGER POWER
```

### E2 — frozen upstream source code

Frozen upstream commit:

```text
6aff1cac48869ccfa0183643979f5f04b04e1124
```

Observed source settings:

| Source file/context | Value |
|---|---:|
| `interactive_simulator.py` | 7.2 kW |
| `custom_workflow.py` | 7.5 kW |
| `scripts/solve_opendss.py` standalone `__main__` example | 7.5 kW |
| `iteratively_solve_opendss(...)` implementation | caller-supplied parameter |

The executable function is therefore parameterized; the repository contains at least two workflow defaults.

## 3. Authority decision

For **replication of the published GreenEVT benchmark semantics**:

```math
oxed{
P_{EV,0}^{chg}=7.2 {m kW}.
}
```

Status:

```text
BENCHMARK_FIXED
SOURCE-DEFINED
PEER-REVIEWED TESTBED DEFAULT
NOT EMPIRICALLY CALIBRATED TO GREENSBORO CHARGERS
```

The 7.5 kW value is retained as a source-code variant:

```math
oxed{
P_{EV,sens}^{chg}=7.5 {m kW}.
}
```

It is **not discarded**, but it does not override the published 7.2 kW default.

## 4. Uncertainty treatment

The code discrepancy is classified as **epistemic source/implementation uncertainty**, not aleatory charging variability.

For source-sensitivity testing:

```math
oxed{
mathcal U_{P_{EV}}^{src}
=
{7.2,7.5} {m kW}.
}
```

No probability distribution or probability weight is assigned to the two values.

Differences:

```math
7.5-7.2=0.3 {m kW},
```

```math
rac{0.3}{7.2}	imes100approx4.17%,
```

and relative to their mean:

```math
rac{0.3}{7.35}	imes100approx4.08%.
```

If any declared QOI materially changes across this source variant, that sensitivity must be reported.

## 5. Parameter sufficiency for Q05

The audited GreenEVT Q05 response operator is instantaneous bus real-power addition:

```math
Delta P_b(t)
=
N_{EV,b}^{chg}(t)P_{EV}^{chg}.
```

For this exact operator, the minimum required coupling-parameter set is:

```math
oxed{
Theta_{Q05}^{min}
=
{P_{EV}^{chg}}.
}
```

Charging start/end times are state/scenario records, not a second charger-power parameter.

The existing registry rows:
- `charger_energy_per_vehicle`;
- `charger_efficiency`

remain scientifically relevant for future energy/SOC/grid-to-battery models, but they are **not required by the current GreenEVT instantaneous bus-load operator**.

Therefore they must not be used as artificial blockers for Q05 if those additional physics are not activated.

## 6. Gate decision

For `C_DEV` GreenEVT benchmark use:

```math
oxed{
G_{	heta}(Q05,C_{DEV})=PASS.
}
```

because the required parameter is prospectively fixed from the published benchmark default.

Also:

```math
oxed{
G_{mathcal U}(Q05,C_{DEV})=PASS
}
```

for the **source-discrepancy dimension**, because the 7.5 kW code variant is preserved as a nonprobabilistic sensitivity case.

This does **not** close aggregate Stage2→3 readiness:

```math
oxed{
G_{2	o3}(Q05,C_{DEV})=BLOCKED
}
```

until the exact materialized GreenEVT data and solver stack are bound in the execution environment and the executable realization passes the required runtime verification fixtures.

## 7. Case-transfer prohibition

The 7.2 kW value is authorized for the GreenEVT development/benchmark context only.

```math
oxed{
P_{EV}^{chg}=7.2 {m kW}	ext{ in }C_{DEV}

otRightarrow
P_{EV}^{chg}=7.2 {m kW}	ext{ in }C_{CONF}.
}
```

Austin or any future confirmatory case requires its own charger/interface parameter evidence or explicitly declared scenario assumption.

## 8. Claim ceiling

Allowed:

> The GreenEVT development benchmark is executed with the published testbed default of 7.2 kW per simultaneously charging EV, with 7.5 kW retained as a source-code sensitivity variant.

Not allowed:

> Greensboro EVs empirically charge at 7.2 kW.

Not allowed:

> 7.2–7.5 kW is an empirical probability distribution of charging power.
