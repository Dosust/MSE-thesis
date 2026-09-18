# Stage 2 Evidence Register v1

**Status:** WORKING PRIOR-EVIDENCE REGISTER — NO CAUSAL RELATION ACCEPTED YET  
**Date:** 2026-09-18

## 1. Interpretation

This register inventories the initial `P↔T` mechanism families that deserve causal qualification. `OPEN` means the mechanism family has prior evidence but the **case-specific G2 dossier is incomplete**.

| ID | Direction | Mechanism | Primary prior evidence | Interface/exchange hypothesis | Activation hypothesis | Case connection | Parameter status | Current G2 |
|---|---|---|---|---|---|---|---|---|
| `M2-PT-01` | P→T | Traffic-signal electrical service | Fotouhi et al. (2017) directly couple power needs of traffic signals to the traffic-power system | electrical supply interface; available electrical service | signal requires external supply; backup/substitute state matters | OPEN | UNESTIMATED | **OPEN** |
| `M2-PT-02` | P→T | EV charging-service availability | EV/grid interface literature; Lu et al. (2025) provides charging-station functional heterogeneity context | grid/EVSE interface; available charging power/service | EV connected/requesting charge; EVSE/grid available; operating limits active | OPEN | UNESTIMATED | **OPEN** |
| `M2-TP-01` | T→P | Repair/restoration access | Fotouhi et al. (2017); Anokhin et al. (2021) | route/access interface; crew/MPS travel-time/accessibility service | failed/target power asset requires physical intervention and mobile resource | OPEN | UNESTIMATED | **OPEN** |
| `M2-TP-02` | T→P | EV charging demand | Lu et al. (2025) and coupled EV-grid literature | EVSE electrical interface; charging demand/load | charging session active; vehicle/EVSE connected; demand not curtailed | OPEN | UNESTIMATED | **OPEN** |
| `M2-TP-03` | T→P | V2G/mobile-storage support | mobile power/V2G literature; Anokhin et al. supports mobile-resource restoration logic | bidirectional/mobile electrical interface; exported power/energy | compatible hardware/control; stored energy; dispatch/consent; grid support mode | OPEN | UNESTIMATED | **OPEN** |

## 2. Required evidence before any PASS

Each row must acquire:

~~~text
verified case source + receiver
verified interface
realized exchanged signal
mechanism evidence
activation evidence
temporal ordering where relevant
empirical/operational support where available
alternative-explanation analysis
contrary evidence
validity domain
falsification condition
parameter status
~~~

## 3. Common-cause register

Flood, heat, earthquake, or other hazards may create:

~~~math
\eta\to P,\qquad\eta\to T
~~~

These are tracked as context/exogenous causes and are not entered as `M2-PT` or `M2-TP` mechanisms without an additional qualified cross-system causal path.

## 4. Acceptance boundary

~~~math
\boxed{\text{row in this register}\neq\mathfrak I_e}
~~~

Only a completed G2 audit may create a causally qualified interdependency.