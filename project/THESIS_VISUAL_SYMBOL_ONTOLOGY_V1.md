# Thesis Visual Symbol Ontology — v1.0

![Authority](https://img.shields.io/badge/authority-CANONICAL%20VISUAL%20ONTOLOGY-0969DA)
![Scope](https://img.shields.io/badge/scope-P--T--I--O%20%2B%20hazard-1D4ED8)
![Version](https://img.shields.io/badge/version-v1.0-1A7F37)

**Ontology ID:** `TVSO-V1`  
**Status:** `CANONICAL-VISUAL-ONTOLOGY`  
**Repository role:** normative visual vocabulary for thesis figures, legends, diagrams, dashboards, and multilayer-network schematics  
**Scientific authority:** [`CANONICAL_7_STAGE_FRAMEWORK_V2.md`](CANONICAL_7_STAGE_FRAMEWORK_V2.md)  
**Interdependency authority:** [`INTERDEPENDENCY_UNIVERSE_CLASSIFICATION_V1.md`](INTERDEPENDENCY_UNIVERSE_CLASSIFICATION_V1.md)  
**Primary figure family:** Class I physical P–T network and Class II augmented P–T–I–O network  

> **Normative rule.** One canonical symbol represents one canonical meaning. Different meanings must not reuse the same symbol, color, line style, or arrow semantics. Color is never the sole discriminator: shape, line style, direction, and label must remain interpretable in grayscale.

---

# 1. Ontology purpose

The ontology separates four visual-semantic families:

```math
\boxed{
\text{engineering assets}
\neq
\text{network abstractions}
\neq
\text{functional-support icons}
\neq
\text{cross-layer relation symbols}
}
```

A fifth family represents external forcing:

```math
\boxed{
\text{hazard field}
\neq
\text{network layer}
\neq
\text{interdependency}
}
```

This ontology does **not** claim that every thesis glyph is an IEC/FHWA standardized symbol. It deliberately combines:

1. engineering-conventional symbols where appropriate;
2. graph/network abstractions for infrastructure topology;
3. thesis-defined functional icons for Information and Organization;
4. thesis-defined relation encodings for interdependencies and control/observation flows.

---

# 2. Ontology schema

Every visual object is defined by

```math
\boxed{
\mathcal O_v
=
(
ID,
Class,
Layer,
Meaning,
Glyph,
Color,
Stroke,
Direction,
LegendLabel,
Status
)
}
```

where:

- `ID` = unique ontology identifier;
- `Class` = `engineering_asset`, `network_object`, `support_function`, `relation`, or `hazard`;
- `Layer` = `P`, `T`, `I`, `O`, `PT`, or `H`;
- `Meaning` = scientific/engineering semantics;
- `Glyph` = normalized shape/icon;
- `Color` = canonical hexadecimal color;
- `Stroke` = solid/dashed and nominal line weight;
- `Direction` = arrow direction where applicable;
- `LegendLabel` = exact wording permitted in legends;
- `Status` = `REQUIRED`, `OPTIONAL`, or `RESERVED`.

---

# 3. Canonical layer palette

| Layer | Canonical color | Hex | Use |
|---|---|---:|---|
| Organization `O` | Gold / ochre | `#A66F00` | organization icons and layer boundary |
| Information `I` | Engineering blue | `#1D4ED8` | information functions and layer boundary |
| Power `P` | Engineering red | `#C8102E` | electrical network objects |
| Transportation `T` | Infrastructure green | `#16823A` | transport access/repair semantics and layer boundary |
| Transportation neutral topology | Neutral gray | `#6B7280` | roads and ordinary intersections |
| Hazard `H` | Hazard blue | `#2F80ED` | external hazard field / exposure only |

**Rule:** layer colors identify domains. Relation colors are defined separately and must not be inferred from source-layer color.

---

# 4. Power-network ontology — `P`

## 4.1 Normalized symbols

| ID | Class | Normalized glyph | Canonical meaning | Color | Exact legend label | Status |
|---|---|---|---|---|---|---|
| `P.SUBSTATION_NODE` | network_object | large filled circle | graph node representing a substation / major electrical node | `#C8102E` | `Substation node` | REQUIRED |
| `P.BUS_NODE` | network_object | small hollow circle | graph abstraction of an electrical bus/node | `#C8102E` | `Power bus node` | REQUIRED |
| `P.LINE` | engineering_asset | solid line | power line / feeder connectivity | `#C8102E` | `Power line / feeder` | REQUIRED |
| `P.TRANSFORMER` | engineering_asset | two interlinked/overlapping circles | power transformer | `#C8102E` | `Power transformer` | REQUIRED |
| `P.SWITCH` | engineering_asset | explicit open-contact / blade symbol | switch/disconnector | `#C8102E` | `Switch / disconnector` | REQUIRED |
| `P.LOAD` | engineering_asset | short downward stem ending in arrowhead | electrical load / demand | `#C8102E` | `Load` | REQUIRED |
| `P.GENERATOR` | engineering_asset | circle containing `G` | generator | `#C8102E` | `Generator` | REQUIRED |
| `P.AC_SOURCE` | engineering_asset | circle containing sine-wave mark | AC source | `#C8102E` | `AC source` | OPTIONAL |
| `P.DER` | engineering_asset | dedicated resource-specific symbol only | DER when its technology is explicitly modeled | domain-specific | technology-specific label | RESERVED |

## 4.2 Prohibited power-symbol ambiguities

- `Transformer` and `Switch / disconnector` shall never share a glyph.
- A square-with-diagonal glyph shall not be used as a generic switch in thesis figures.
- `Generator` shall not be labeled `DER`.
- Filled/hollow circles are **graph abstractions**, not claims of IEC-standard substation/bus symbols.

---

# 5. Transportation-network ontology — `T`

| ID | Class | Normalized glyph | Canonical meaning | Color | Exact legend label | Status |
|---|---|---|---|---|---|---|
| `T.ROAD_LINK` | network_object | double gray road line with center marking | road-network edge | `#6B7280` | `Road link` | REQUIRED |
| `T.INTERSECTION` | network_object | filled gray circle | ordinary road intersection node | `#6B7280` | `Intersection node` | REQUIRED |
| `T.REPAIR_ACCESS_NODE` | network_object | hollow green circle | road node explicitly used by repair-access mechanism | `#16823A` | `Repair-access node` | REQUIRED |
| `T.TRAFFIC_SIGNAL` | engineering_asset | standard three-aspect traffic-light pictogram | signalized intersection device | signal colors with dark body | `Traffic signal` | REQUIRED |
| `T.REPAIR_ROUTE` | relation/path | green dashed path over road topology | path used by repair crew to reach power asset | `#16823A` | `Repair route` | REQUIRED |
| `T.REPAIR_CREW` | engineering_asset | service/repair truck pictogram | mobile repair crew represented by service vehicle | `#16823A` | `Repair crew` | REQUIRED |
| `T.CRITICAL_FACILITY` | network_object | building/facility pictogram | optional critical destination/facility | neutral dark | `Critical facility` | OPTIONAL |

**Mechanism rule:** `T.REPAIR_ACCESS_NODE` does not itself constitute the `T→P` dependency. The dependency is path-based and is represented by the repair route plus an upward cross-layer relation to a repairable power asset.

---

# 6. Information-layer ontology — `I`

Information is a **functional support layer** unless an empirical communication topology is explicitly introduced. No generic information-network nodes or internal graph links shall be drawn in the baseline Class II figure.

| ID | Class | Normalized icon | Canonical meaning | Color | Exact legend label | Status |
|---|---|---|---|---|---|---|
| `I.SENSING` | support_function | dedicated sensor/radar icon with sensing arcs | acquisition / monitoring of physical-system observations | `#1D4ED8` | `Sensors / monitoring` | REQUIRED |
| `I.COMMUNICATION` | support_function | radio/communication tower | communication / message transmission | `#1D4ED8` | `Communication` | REQUIRED |
| `I.MEASUREMENT` | support_function | waveform / sampled-data / gauge icon | measured data, not storage | `#1D4ED8` | `Measurements` | REQUIRED |
| `I.STATE_ESTIMATION` | support_function | target/estimate icon or estimator dashboard distinct from monitoring | estimated system state / belief | `#1D4ED8` | `State estimation` | REQUIRED |
| `I.SITUATIONAL_AWARENESS` | support_function | map/dashboard/operational-picture icon | integrated operational awareness | `#1D4ED8` | `Situational awareness` | REQUIRED |
| `I.UNCERTAINTY` | support_function | probability distribution / uncertainty-band icon | quantified uncertainty | `#1D4ED8` | `Uncertainty` | REQUIRED |
| `I.DATA_STORAGE` | support_function | database cylinder | persistent data storage | `#1D4ED8` | `Data storage` | OPTIONAL |

## 6.1 Prohibited information-symbol ambiguities

- Database cylinder shall not mean `Measurements`.
- People/group icon shall not mean `Situational awareness`.
- Bar chart shall not be the canonical symbol for `Uncertainty`.
- Monitoring and state estimation shall not reuse the same icon.
- Generic `information node` and `information link` shall not appear unless an explicit `G_I=(V_I,E_I)` topology is modeled.

---

# 7. Organization-layer ontology — `O`

Organization is a **functional support layer** unless an empirical organizational topology is explicitly introduced. The baseline figure shall use function icons without invented node-edge topology.

| ID | Class | Normalized icon | Canonical meaning | Color | Exact legend label | Status |
|---|---|---|---|---|---|---|
| `O.AUTHORITY` | support_function | institutional/governance building | authority / formal decision rights | `#A66F00` | `Authority` | REQUIRED |
| `O.COORDINATION` | support_function | group/team icon | inter-actor coordination | `#A66F00` | `Coordination` | REQUIRED |
| `O.CREWS_RESOURCES` | support_function | worker/hardhat + resource cue | crews and deployable resources | `#A66F00` | `Crews / resources` | REQUIRED |
| `O.PRIORITIES` | support_function | clipboard/checklist | priority rules / task ordering | `#A66F00` | `Priorities` | REQUIRED |
| `O.RESPONSE_TIMING` | support_function | clock | response delay / timing | `#A66F00` | `Response timing` | REQUIRED |
| `O.DECISION_CONTROL` | support_function | gear/control icon | operational decision / command | `#A66F00` | `Decision / control` | REQUIRED |

## 7.1 Prohibited organization-symbol ambiguities

- Generic `organizational node` and `organizational link` shall not appear in the baseline figure.
- Functional icons shall not be connected by a network topology unless `G_O=(V_O,E_O)` is empirically defined.
- Coordination and situational awareness shall use different icons.

---

# 8. Cross-layer relation ontology

## 8.1 Hard visual-semantic rule

```math
\boxed{
\text{one relation meaning}
\Longleftrightarrow
\text{one color + one line style + one direction convention}
}
```

The same color may be reused only when the semantic relation is identical and only the source/target instance changes.

| ID | Source → Target | Canonical meaning | Color | Line | Arrow | Exact legend label | Status |
|---|---|---|---:|---|---|---|---|
| `R.PT.SIGNAL_POWER` | `P→T` | electrical supply to traffic signal / signalized intersection | `#F28C00` | dashed | downward | `Signal-power dependency` | REQUIRED |
| `R.TP.REPAIR_ACCESS` | `T→P` | repair route/access enabling crew arrival at repairable power asset | `#008A3B` | dashed | upward | `Repair-access dependency` | REQUIRED |
| `R.PI.OBSERVATION` | `P→I` | power-system measurements / observations | `#0097A7` | solid | upward | `Measurements / observations` | REQUIRED |
| `R.TI.OBSERVATION` | `T→I` | transportation-system measurements / observations | `#0097A7` | solid | upward | `Measurements / observations` | REQUIRED |
| `R.IO.STATE_INFORMATION` | `I→O` | estimated/processed state information supplied to organization | `#7C3AED` | solid | upward | `State information` | REQUIRED |
| `R.OI.INFORMATION_PRIORITIES` | `O→I` | organizational priorities affecting sensing/information attention | `#C026D3` | solid | downward | `Information priorities` | REQUIRED |
| `R.OP.CONTROL_RESOURCE` | `O→P` | organizational control / resource deployment acting on power system | `#8B5E00` | solid | downward | `Control / resource deployment` | REQUIRED |
| `R.OT.CONTROL_RESOURCE` | `O→T` | organizational control / resource deployment acting on transportation system | `#8B5E00` | solid | downward | `Control / resource deployment` | REQUIRED |

## 8.2 Geometry rules

### Signal-power dependency

The visual arrow must originate at the supplying electrical asset or feeder and terminate at the traffic-signal object:

```math
E_P\rightarrow N_T^{signal}
\quad\text{or}\quad
N_P\rightarrow N_T^{signal}.
```

### Repair-access dependency

The visual relation must originate from a highlighted repair route/path and terminate at a repairable power asset:

```math
\boxed{\text{Path}_T\rightarrow N_P\text{ or }E_P.}
```

Do not depict repair access as an unexplained green node-to-node vertical line.

### Observation relations

Power and Transportation independently feed the Information layer:

```math
P\rightarrow I,
\qquad
T\rightarrow I.
```

### Organizational action

Organization acts independently on both physical systems when applicable:

```math
O\rightarrow P,
\qquad
O\rightarrow T.
```

---

# 9. Hazard ontology — `H`

| ID | Class | Normalized glyph | Canonical meaning | Color | Exact legend label | Status |
|---|---|---|---|---|---|---|
| `H.FIELD` | hazard | irregular translucent contour/raster field | external spatial hazard field | light-to-dark `#90CAF9` → `#2F80ED` | `Hazard field` | REQUIRED |
| `H.EXPOSURE_P` | relation | solid blue exposure arrow | hazard forcing/exposure acting on power assets | `#2F80ED` | `Hazard forcing / exposure` | REQUIRED |
| `H.EXPOSURE_T` | relation | solid blue exposure arrow | hazard forcing/exposure acting on transportation assets | `#2F80ED` | `Hazard forcing / exposure` | REQUIRED |

**Mandatory rule:**

```math
\boxed{
\text{hazard exposure}\neq\text{interdependency}.
}
```

The hazard field must remain visually external to the multilayer stack and must show independent exposure to both `P` and `T`.

---

# 10. Class-I ontology subset

Class I shall use only:

```math
\boxed{
P+T+R.PT.SIGNAL\_POWER+R.TP.REPAIR\_ACCESS+H
}
```

Required visual objects:

- Power-network symbols from Section 4;
- Transportation-network symbols from Section 5;
- `R.PT.SIGNAL_POWER`;
- `R.TP.REPAIR_ACCESS`;
- `H.FIELD`, `H.EXPOSURE_P`, `H.EXPOSURE_T`.

No `I` or `O` symbols are allowed in Class I.

---

# 11. Class-II ontology subset

Class II is defined as a strict augmentation:

```math
\boxed{
\text{Class II}
=
\text{Class I}
+
I
+
O
+
\{R.PI,R.TI,R.IO,R.OI,R.OP,R.OT\}.
}
```

The Class-I physical core shall not be redefined when moving to Class II.

Required additional objects:

- all six Information functions in Section 6;
- all six Organization functions in Section 7;
- observation relations from `P` and `T` to `I`;
- state information from `I` to `O`;
- information priorities from `O` to `I`;
- control/resource deployment from `O` to both `P` and `T` where shown.

---

# 12. Canonical legend protocol

Legends contain **only symbol → meaning**. No explanatory sentences, mathematical interpretation, or methodological notes are permitted inside the legend.

## 12.1 Class-I legend order

1. `Power network`
2. `Transportation network`
3. `Interdependencies`
4. `Hazard`

## 12.2 Class-II legend order

1. `Organization`
2. `Information`
3. `Power network`
4. `Transportation network`
5. `Cross-layer relations`
6. `Hazard`

## 12.3 Exact legend vocabulary

### Organization

- Authority
- Coordination
- Crews / resources
- Priorities
- Response timing
- Decision / control

### Information

- Sensors / monitoring
- Communication
- Measurements
- State estimation
- Situational awareness
- Uncertainty

### Power network

- Substation node
- Power bus node
- Power line / feeder
- Power transformer
- Switch / disconnector
- Load
- Generator

### Transportation network

- Road link
- Intersection node
- Repair-access node
- Traffic signal
- Repair route
- Repair crew

### Cross-layer relations

- Signal-power dependency
- Repair-access dependency
- Measurements / observations
- State information
- Information priorities
- Control / resource deployment

### Hazard

- Hazard field
- Hazard forcing / exposure

---

# 13. Accessibility and reproduction rules

1. Meaning shall never depend on color alone.
2. Every relation uses a unique combination of color, line style, and arrow direction.
3. Text contrast must remain readable on white backgrounds and in exported PNG/PDF.
4. Layer fill colors shall remain pale; boundary and icon colors carry the semantics.
5. Hazard contours shall remain translucent so they cannot be mistaken for a network layer.
6. All legend symbols must visually match the actual figure glyphs exactly.
7. The same ontology ID must retain the same meaning across all thesis figures.
8. New symbols require a versioned ontology update before figure use.

---

# 14. Forbidden representations

The following are prohibited unless the ontology is explicitly revised:

- same color/line semantics for two different relation meanings;
- unlabeled cross-layer arrows;
- generic `DER` label attached to generator glyph;
- combined transformer/switch legend entry;
- database cylinder used for measurements;
- generic organization/information graph topology without evidence;
- hazard drawn as a fifth infrastructure layer;
- repair-access dependency shown only as node-to-node when the modeled mechanism is path-based;
- hazard exposure labeled as `impact` when the arrow denotes forcing/exposure.

---

# 15. Change-control rule

This file is the visual authority for the Class-I and Class-II figure family.

Any future symbol change requires:

```math
\boxed{
\text{proposed symbol change}
\rightarrow
\text{semantic audit}
\rightarrow
\text{ontology version update}
\rightarrow
\text{figure regeneration}
}
```

Figures must not silently introduce new symbols or change the meaning of an existing ontology ID.
