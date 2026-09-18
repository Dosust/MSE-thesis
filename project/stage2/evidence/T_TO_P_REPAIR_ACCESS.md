# Stage 2 Evidence Dossier — T→P Restoration / Repair-Access Dependency

**Mechanism ID:** `M2-TP-01`  
**Status:** **OPEN — STRONG DIRECT PRIOR MECHANISM EVIDENCE; CASE CONNECTION NOT YET QUALIFIED**

## 1. Tested causal claim

> When restoration of a failed/degraded power asset requires a mobile crew or mobile power resource to physically reach a target location, transportation-network accessibility and travel conditions can affect arrival time, feasible task execution, and therefore the power-restoration trajectory.

## 2. Causal fields

| Field | Working value |
|---|---|
| source | transportation route/accessibility/travel-time state |
| receiver | power restoration task/state |
| direction | T→P |
| mechanism class | `M-MOB-ACCESS` |
| path | MEDIATED: route → mobile resource/crew → repair/restoration action |
| `Φ_e` | accessibility / travel-time / route-feasibility service |
| parameter status | UNESTIMATED |
| current G2 | OPEN |

## 3. Direct prior evidence

Fotouhi et al. (2017), DOI `10.1016/j.ress.2017.01.026`, explicitly include transportation access for repair operations associated with damaged power infrastructure. Anokhin et al. (2021), DOI `10.1111/poms.13393`, coordinate mobile power sources and repair crews while accounting for transportation connectivity; disrupted routes alter routing/scheduling during distribution-system restoration.

## 4. Activation predicate

~~~math
\mathcal A_e=1
\quad\text{if}\quad
\text{power restoration task is required}
\land
\text{task requires physical mobile resource/crew}
\land
\text{target is not already reachable/served without transportation movement}.
~~~

Thus repair access is **recovery activated**, not a continuously active generic T→P coupling.

## 5. Case evidence required

- failed/target power asset ID and repair requirement;
- repair-crew/MPS depot or current location;
- admissible road-network routes to the target;
- road status, closures, capacities, travel times and vehicle restrictions;
- mobilization time and crew/resource availability;
- task precedence and repair duration;
- remote-switching/alternative-restoration possibilities;
- timestamped restoration/arrival data where available.

## 6. Alternative explanations

- remote switching/restoration without field access;
- alternative crew/resource already onsite;
- spare/material shortage dominating delay;
- safety clearance/authority delay;
- repair duration dominating travel time;
- alternate route not represented in the candidate relation.

## 7. Falsification / revision condition

A candidate route/access relation is rejected or revised if the restoration task does not require physical access, the proposed route is not actually used/necessary, or restoration timing is demonstrably independent of transportation accessibility within the declared validity domain.

## 8. Delay structure

Do not equate travel time with total restoration time. A possible decomposition is:

~~~math
T_{\rm restore}=T_{\rm detect}+T_{\rm authorize}+T_{\rm mobilize}+T_{\rm travel}+T_{\rm repair}+T_{\rm reenergize}.
~~~

Only the transportation-mediated terms belong to this mechanism unless evidence shows additional coupling.

## 9. G2 state

| Gate | Current state |
|---|---|
| G2-M | PRIOR-SUPPORTED / OPEN | two direct prior precedents |
| G2-C | OPEN | case asset↔route↔resource connection required |
| G2-X | OPEN | accessibility/travel-time service must be operationalized |
| G2-A | DRAFTED / OPEN | field-intervention activation defined; case test required |
| G2-E | OPEN | case operational/empirical evidence not assembled |
| G2-V | OPEN | vehicle/route/task validity limits needed |
| G2-F | DRAFTED | reject/revise conditions defined |

~~~math
\boxed{G_2(M2\text{-}TP\text{-}01)=\mathrm{OPEN}}
~~~