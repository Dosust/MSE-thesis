# Stage 2 Case-Connection Register v1

**Status:** EXECUTED — FOUR CURRENT CASE CANDIDATES  
**Case:** GreenEVT/SMART-DS Greensboro H1 Level-2 realization  
**Authority:** `STAGE2_CASE_PRESENCE_AUDIT_V1_2026-09-19.md`

## 1. Purpose

Resolve the G2-C case-connection question for the four mechanism families instantiated in the current Level-2 dependency registry:

```math
\mathcal M_{case}^{cand}=\{Q01,Q03,Q05,Q06\}.
```

Case-connection PASS requires an auditable source -> interface -> receiver mapping. Spatial proximity, common geography, or a generic literature mechanism is insufficient.

## 2. Register

| Relation | Parent | Direction | Source | Interface / crosswalk | Receiver | Case evidence | G2-C |
|---|---|---|---|---|---|---|---|
| `SIGNAL_P_to_T` | Q01 | P->T | SMART-DS distribution bus/feeder candidate | required: signal/controller -> actual electrical supply circuit/feeder/bus; backup configuration | SUMO/Greensboro signalized junction/controller | 914 SUMO tlLogic controllers exist; power network exists; no verified electrical service mapping exists | **BLOCKED** |
| `EV_P_to_T` | Q03 | P->T | distribution bus / charging electrical connection | GreenEVT vehicle/parcel-to-bus charging association | EV charging service | GreenEVT explicitly links EV charging to distribution buses; H1 registry marks relation ACTIVE / EVIDENCE_SUPPORTED | **PASS** |
| `EV_T_to_P` | Q05 | T->P | EV/vehicle charging state associated with SUMO edge/parcel | vehicle `bus_name` -> OpenDSS load bus | distribution bus electrical load | `generatevehicles.py` stores vehicle SUMO edge, bus, EV flag and charging times; `solve_opendss.py` groups charging EVs by bus and modifies that bus load | **PASS** |
| `REPAIR_T_to_P` | Q06 | T->P | SUMO road-network state | required: failed asset -> field task -> access point -> route(s) -> crew/resource origin | damaged power component / repair progress | power assets and road topology exist, but no verified task/access/depot/crew crosswalk exists | **BLOCKED** |

## 3. Q01 signal-power connection

Required chain:

```math
bus/feeder/circuit
\rightarrow
signal\ electrical\ service
\rightarrow
controller
\rightarrow
signalized\ junction.
```

Available:
- SMART-DS buses/feeders;
- 914 SUMO `tlLogic` controllers;
- Greensboro signal GIS is an assigned construction source but is not currently materialized in the canonical source registry;
- UDS bus/parcel-to-SUMO-edge interface-opportunity geometry.

Missing:
- actual or explicitly constructed signal-controller electrical supply mapping;
- controller electrical requirement;
- backup source/type/endurance;
- protection/fallback configuration.

### Prohibited shortcut

```math
\boxed{
\text{nearest bus / same road edge / UDS interface opportunity}
\neq
\text{verified signal electrical supply}.
}
```

Therefore:

```text
SIGNAL_P_to_T : G2-C = BLOCKED
```

A later synthetic benchmark may explicitly construct a signal-to-bus mapping, but it must be labeled SYNTHETIC CASE DESIGN and cannot be represented as observed Greensboro utility wiring.

## 4. Q03 charging-service connection

GreenEVT's defining architecture links EV charging to the distribution grid at vehicle/parcel locations. The source testbed contains:
- vehicle/parcel spatial association;
- distribution-bus association;
- EV charging schedules;
- OpenDSS charging-load injection.

This is sufficient to establish that the synthetic case contains a grid-connected EV charging interface.

Therefore:

```text
EV_P_to_T : G2-C = PASS
```

Boundary: this passes the **connection** gate only. It does not yet prove the thesis-specific bus energization/outage -> served charging rate -> mobility-service response.

## 5. Q05 charging-demand connection

The exact upstream code provides a deterministic crosswalk:

```text
vehicle
 -> sumo_edge / parcel
 -> bus_name
 -> charging state
 -> OpenDSS bus load
```

`scripts/generatevehicles.py` writes `sumo_edge`, `bus_name`, `ev`, `charging_start`, `charging_end`.

`scripts/solve_opendss.py` queries active charging EVs by `bus_name` and updates the corresponding OpenDSS load.

Therefore:

```text
EV_T_to_P : G2-C = PASS
```

The mapping is a GreenEVT synthetic-testbed connection, not an observed utility customer-service mapping.

## 6. Q06 repair-access connection

Required chain:

```math
failed\ power\ asset
\rightarrow
required\ field\ task
\rightarrow
physical\ access\ point
\rightarrow
road\ route(s)
\rightarrow
crew/resource\ origin.
```

Available:
- SMART-DS geolocated power topology;
- SUMO Greensboro road topology.

Missing:
- failure-specific task classification;
- whether field access is required versus remote operation;
- access point;
- crew/resource depot;
- vehicle class;
- route set;
- alternative crew/resource;
- task precedence.

Therefore:

```text
REPAIR_T_to_P : G2-C = BLOCKED
```

Nearest-road or nearest-node assignment cannot be called an observed case connection. If used later, it must be an explicit synthetic-case construction with sensitivity analysis.

## 7. G2-C conclusion

```text
Q01 SIGNAL_P_to_T  BLOCKED
Q03 EV_P_to_T      PASS
Q05 EV_T_to_P      PASS
Q06 REPAIR_T_to_P  BLOCKED
```

No G2-C decision is made for Q02,Q04,Q07-Q13 because no current case relation instance exists for those families.

## 8. Evidence pointers

Thesis repository:
- `models/H1/level2/registries/dependency_registry_v1.csv`
- `models/H1/level2/artifacts/uploaded_source_audit_v1.json`
- `models/H1/level2/artifacts/feeder_features_source_v1_1.csv`
- `models/H1/level2/FEEDER_FEATURE_SPECIFICATION_V1_1.md`

GreenEVT upstream commit `6aff1cac48869ccfa0183643979f5f04b04e1124`:
- `scripts/generatevehicles.py`
- `scripts/solve_opendss.py`
