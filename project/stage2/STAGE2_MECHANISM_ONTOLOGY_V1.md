# Stage 2 Mechanism Ontology v1

**Status:** WORKING CONTROLLED ONTOLOGY — NOT FROZEN

## 1. Purpose

This ontology classifies **causal mechanism families** for Stage-2 qualification. It is a thesis-controlled synthesis informed by prior literature; it is not claimed as any one author's taxonomy.

## 2. Controlled mechanism families

| Code | Mechanism family | Meaning | Typical P↔T example |
|---|---|---|---|
| `M-PHYS-ELEC` | Physical electrical-service dependency | Receiver function requires electrical service delivered through a verified electrical interface. | feeder/bus → traffic signal or EVSE availability |
| `M-MOB-ACCESS` | Mobility/access dependency | Receiver action requires physical movement/access through the transportation network. | road route → repair-crew/MPS access → power restoration |
| `M-DEMAND` | Demand/load dependency | Transportation behavior creates electrical demand that changes power-system operating conditions. | EV charging demand → distribution loading |
| `M-ENERGY-SUPPORT` | Mobile/bidirectional energy-support dependency | Transportation-side mobile storage or generation supplies power-system service when compatible control/interface conditions hold. | V2G / mobile storage → grid support |
| `M-INFO-CTRL` | Information/control-mediated dependency | State/action transfer is mediated by sensing, communication, control or coordination. | power-state/price signal → charging control |
| `M-ORG-RULE` | Organizational/rule-mediated dependency | Human decisions, authority or formal/informal rules mediate infrastructure effects. | restoration priority/dispatch rule → P/T action sequence |
| `M-CONTEXT` | Common-cause/environmental context | Shared hazard/environment affects multiple systems without one causing the other. | flood → P and flood → T |

`M-CONTEXT` is **not eligible for promotion to a P→T or T→P causal dependency** unless an additional genuine cross-system mechanism is separately qualified.

## 3. Direction is independent of mechanism class

Mechanism family and direction must be stored separately. For example `M-PHYS-ELEC` can describe P→T electrical service, while `M-ENERGY-SUPPORT` can describe T→P electrical support. An undirected mechanism label must never replace the tested causal direction.

## 4. Direct versus mediated

~~~math
\pi_e\in\{\mathrm{DIRECT},\mathrm{MEDIATED}\}
~~~

Examples:

~~~text
P -> T signal power                    DIRECT physical/electrical
T -> repair crew mobility -> P repair  MEDIATED mobility/access
O -> dispatch rule -> I/control -> P/T MEDIATED organizational/information
~~~

## 5. Activation ontology

Activation context is not a prose afterthought. At minimum it should identify:

- operating mode: normal / stressed / disrupted / recovery;
- trigger condition;
- required interface availability;
- required resource/actor availability;
- backup/substitute state;
- relevant hazard or exogenous context;
- temporal persistence/minimum duration if applicable.

## 6. Mechanism statement template

A mechanism statement should be written as:

> When `[activation condition]`, a change in `[source state/service]` changes `[realized interface signal φ_e]` through `[mechanism]`, producing `[receiver response]` within `[validity domain]`, subject to `[uncertainty/alternatives]`.

## 7. Separation from strength

~~~math
\boxed{\text{mechanism identity}\neq\text{effect magnitude}\neq\text{evidence confidence}}
~~~

A mechanism code cannot be converted into a universal coupling coefficient.