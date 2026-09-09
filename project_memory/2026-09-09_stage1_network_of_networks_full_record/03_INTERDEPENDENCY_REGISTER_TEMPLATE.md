# Component-Level Interdependency Register Template

## Evidence hierarchy

```text
E3 Direct       - utility/GIS/operator/official technical evidence
E2 Mechanistic  - peer-reviewed mechanism + defensible mapping
E1 Hypothesized - sensitivity/scenario analysis only
E0 Unsupported  - exclude
```

## Domain completeness

```math
\boxed{C_{domain}=N_{audited}/12}
```

Require `C_domain = 1`, meaning all 12 directed domain pairs were audited.

## Register schema

| Field | Description |
|---|---|
| ID | unique dependency identifier |
| Source layer | P/T/I/O |
| Source object | real component/actor/interface |
| Source geometry | node/link/agent/interface |
| Target layer | P/T/I/O |
| Target object | real component/actor/interface |
| Target geometry | node/link/agent/interface |
| Direction | alpha -> beta |
| Dependency class | physical/cyber/geographic/logical |
| Mechanism | exact causal/functional mechanism |
| Carrier | electricity/information/mobility/command/resource/etc. |
| Spatial mapping | feeder/service area/road path/control map/etc. |
| Baseline state | availability/capacity/strength |
| Evidence level | E3/E2/E1/E0 |
| Literature evidence | DOI/reference |
| Empirical data evidence | utility/GIS/operator/source |
| Inclusion status | included/excluded/unresolved/scenario |
| Stage-2 event relevance | what event can activate/degrade relation |
| Stage-3 dynamic object | future z_ij(t), tau_ij, g_ij(.) mapping |
| Stage-6 metadata | sustainability descriptors retained for later translation |

## Illustrative rows

| ID | Source | Target | Direction | Type | Mechanism | Carrier | Evidence | Status |
|---|---|---|---|---|---|---|---|---|
| D001 | Feeder P17 | EVCS C04 | P -> T | Physical | electrical supply to charger | electricity | E3/E2 | Include |
| D002 | Road R28 | Repair Crew O12 | T -> O | Physical/functional | road accessibility controls crew travel | mobility | E3/E2 | Include |
| D003 | Repair Crew O12 | Line P09 | O -> P | Organizational/physical | crew performs repair | resource/action | E3/E2 | Include |
| D004 | SCADA I04 | Switch P22 | I -> P | Cyber | remote status/control | information/command | E3/E2 | Include |
| D005 | Dispatcher O02 | Crew O12 | O -> O | Logical | task assignment | authority/resource | E3/E2 | Include |

## Inclusion rule

```math
\boxed{\text{Direction + mechanism + mapping + type + evidence are mandatory.}}
```
