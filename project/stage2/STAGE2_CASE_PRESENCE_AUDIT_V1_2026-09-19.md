# Stage 2 Case-Presence Audit v1 — 2026-09-19

**Status:** EXECUTED — PRE-G2 CASE-PRESENCE AUDIT  
**Case authority:** H1 Level-2 GreenEVT/SMART-DS Greensboro realization  
**Mechanism-taxonomy authority:** `STAGE2_QUALIFIED_MECHANISM_UNIVERSE_FREEZE_2026-09-19.md`  
**Purpose:** determine which frozen parent mechanism families Q01–Q13 are actually instantiated, partially instantiated, or not instantiated in the current thesis case. This audit does not treat absence from the current case as falsification of a mechanism family.

## 1. Case identity

The current H1 Level-2 construction is the GreenEVT Greensboro realistic-synthetic testbed:

- power: GreenEVT / SMART-DS OpenDSS;
- transportation: GreenEVT SUMO Greensboro road network;
- interface opportunities: GreenEVT UDS bus/parcel-to-SUMO-edge mappings;
- observed transport-control geometry: Greensboro signal GIS is assigned as a construction source but is not yet materialized;
- exact GreenEVT critical objects are materialized and audited.

Frozen source identities:

```text
GreenEVT upstream commit:
6aff1cac48869ccfa0183643979f5f04b04e1124

UDS.db SHA-256:
74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724

greensboro.net.xml SHA-256:
f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06
```

Audited transport invariants:

```text
non-internal SUMO edges = 118,289
tlLogic controllers     = 914
road length             = 28,216.37782 km
lane length             = 30,625.43639 km
```

The source-only feeder matrix contains 61 SMART-DS feeders. Sixty have at least one UDS-derived bus/parcel-to-SUMO-edge interface opportunity; one has N_I=0. This is structural/interface-opportunity evidence only, not observed utility wiring.

## 2. Case-presence semantics

Use four pre-G2 states:

- **NATIVE-EXPLICIT:** the source case directly encodes the mechanism-relevant source/interface/receiver relation.
- **PARTIAL:** relevant source/receiver/interface objects exist, but at least one relation or activation element is not verified.
- **NOT-INSTANTIATED:** the frozen parent family is scientifically qualified, but the current H1 Level-2 case contains no candidate relation instance for it.
- **OUTSIDE-CURRENT-MODE:** the family applies to a transport mode absent from the current road-focused realization.

These are not G2 decisions.

## 3. Q01–Q13 audit

| ID | Parent mechanism | Case-presence result | Direct case evidence | Scientific limitation |
|---|---|---|---|---|
| Q01 | Electrical service to transport operational assets | **PARTIAL** | SUMO contains 914 traffic-light logic controllers; SMART-DS power buses/feeders exist; `SIGNAL_P_to_T` is registered as an active pending-evidence relation | no verified signal/controller -> supplying circuit/feeder/bus mapping; backup/endurance is unknown; proximity or UDS edge opportunity cannot substitute for service records |
| Q02 | Traction/propulsion electrical supply | **OUTSIDE-CURRENT-MODE** | current D_T realization is a road/SUMO passenger network | no rail/trolley traction-power system is instantiated |
| Q03 | Charging-service availability and grid constraints | **PARTIAL / CASE CONNECTION PRESENT** | GreenEVT links EV charging to distribution buses; `EV_P_to_T` is ACTIVE and evidence-supported in the H1 dependency registry | native GreenEVT code does not establish the thesis outage/energization -> served-charging-rate response; outage-state/fulfillment activation remains to be qualified |
| Q04 | Power-asset physical obstruction of transportation | **NOT-INSTANTIATED** | power and road geometries exist | no downed-line/pole/work-zone -> road-capacity relation is registered in the H1 Level-2 case |
| Q05 | Mobility-derived charging demand and redistribution | **NATIVE-EXPLICIT** | GreenEVT vehicle records carry bus, SUMO edge, EV flag, charging start/end; `solve_opendss.py` counts charging EVs by bus and adds charging kW to OpenDSS loads; `EV_T_to_P` is ACTIVE and evidence-supported | charging-power magnitude and behavioral assumptions are parameter/model choices; native GreenEVT primarily implements demand injection rather than all possible queue/redistribution behavior |
| Q06 | Transport access for power field intervention | **PARTIAL** | SUMO road network and SMART-DS power assets exist; `REPAIR_T_to_P` is registered ACTIVE_PENDING_EVIDENCE | no verified failed-asset -> field task -> access point -> route set -> crew/resource origin crosswalk; local depot/task/repair data are absent |
| Q07 | Restoration logistics | **NOT-INSTANTIATED** | none in active dependency registry | no material/fuel/spare-part logistics object or supply-chain relation is instantiated |
| Q08 | Mobile power-resource positioning | **NOT-INSTANTIATED** | none in active dependency registry | no MEG/MESS/mobile-transformer fleet, origin, route, hookup, or target mapping is instantiated |
| Q09 | Bidirectional/mobile stored-energy export | **NOT-INSTANTIATED** | GreenEVT search and source code expose EV charging demand; no V2G relation is registered | charging load must not be reinterpreted as export; no bidirectional hardware/SOC/export/authorization path is instantiated |
| Q10 | Transport-induced physical damage to power assets | **NOT-INSTANTIATED** | none in active dependency registry | no collision/excavation/road-work -> power-asset failure event is instantiated |
| Q11 | Information/control-mediated coupling | **NOT-INSTANTIATED AS INFRASTRUCTURE MECHANISM** | GreenEVT uses shared software/database orchestration | simulation orchestration is not evidence of a real case information infrastructure or operator control mechanism |
| Q12 | Communication/cyber-state coupling | **NOT-INSTANTIATED** | none in active dependency registry | no communication network, latency, availability, integrity, or cyber-failure state is modeled as a case dependency |
| Q13 | Organizational/rule/pricing/dispatch coupling | **NOT-INSTANTIATED** | none in active dependency registry | scenario scripts/assumptions are not evidence of an actual organizational authority, tariff, dispatch, or restoration-priority relation |

## 4. Case-candidate set

The current Level-2 dependency registry contains four case candidates:

```math
\boxed{
\mathcal M_{case}^{cand}
=
\{Q01,Q03,Q05,Q06\}.
}
```

with current evidence classes:

```text
Q01 / SIGNAL_P_to_T   = INFERRED_PENDING_VERIFICATION
Q03 / EV_P_to_T       = EVIDENCE_SUPPORTED
Q05 / EV_T_to_P       = EVIDENCE_SUPPORTED
Q06 / REPAIR_T_to_P   = INFERRED_PENDING_VERIFICATION
```

The remaining Q02,Q04,Q07–Q13 are retained in the frozen conceptual universe but are not current case relations. Their absence is not a G2 FAIL because no case relation instance has been opened for them.

## 5. Strongest native case relation

Q05 is directly encoded by GreenEVT:

```math
\text{vehicle mobility / EV assignment}
\rightarrow
\{bus\_name,charging\_start,charging\_end\}
\rightarrow
N_{EV}^{charging}(b,t)
\rightarrow
\Delta P_b(t).
```

The upstream solver implements:

```math
\Delta P_b(t)
=
N_{EV}^{charging}(b,t)\,P_{EV}^{charge}
```

for the configured scenario charging power.

This establishes a synthetic-case mechanism and case connection. It does not establish that the synthetic bus/vehicle mapping is an observed Greensboro utility-service record.

## 6. Anti-overclaiming rules

1. UDS bus/parcel-to-SUMO-edge mappings are case-construction/interface evidence, not observed utility wiring.
2. SUMO traffic-light presence does not establish which feeder supplies a signal.
3. GreenEVT EV charging does not establish V2G.
4. Shared simulation code/database does not establish a real information/organizational dependency.
5. Absence from the current case realization does not falsify the parent mechanism family.
6. No unregistered Q-family may enter Stage 3 merely because it is literature-supported.

## 7. Pre-G2 conclusion

```math
\boxed{
\mathcal M_{PT}^{Q1}
\rightarrow
\mathcal M_{case}^{cand}
=
\{Q01,Q03,Q05,Q06\}
}
```

The next operation is case-connection qualification for these four relations, followed by activation evidence and component-wise G2 audit.

## 8. Evidence pointers

Repository:
- `models/H1/level2/config/protocol_status_v1.json`
- `models/H1/level2/data/CANONICAL_DATA_ARCHITECTURE_V1.md`
- `models/H1/level2/artifacts/uploaded_source_audit_v1.json`
- `models/H1/level2/artifacts/feeder_features_source_v1_1.csv`
- `models/H1/level2/registries/dependency_registry_v1.csv`

Upstream GreenEVT commit `6aff1cac48869ccfa0183643979f5f04b04e1124`:
- `scripts/generatevehicles.py`
- `scripts/solve_opendss.py`
- `scripts/assign_charging_times_to_vehicles.py`
- `data/sumo_network/greensboro.netccfg`

Literature anchor:
- Nilsson, Aquino, Coogan & Molzahn, *GreenEVT: Greensboro Electric Vehicle Testbed*, IEEE Systems Journal, DOI 10.1109/JSYST.2023.3343692.
