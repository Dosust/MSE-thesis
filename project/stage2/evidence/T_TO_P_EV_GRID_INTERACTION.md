# Stage 2 Evidence Dossier — T→P EV–Grid Interaction

**Mechanism IDs:** `M2-TP-02` charging demand; `M2-TP-03` V2G/mobile-storage support  
**Status:** **OPEN — TWO DISTINCT MECHANISMS; MUST NOT BE COLLAPSED**

## 1. Scientific separation

EV-grid interaction contains at least two opposite functional mechanisms:

~~~math
\boxed{\text{EV charging demand}: T\rightarrow P}
~~~
where mobility/charging behavior imposes electrical demand, and

~~~math
\boxed{\text{V2G/mobile support}: T\rightarrow P}
~~~
where mobile storage exports/supports electrical service. They may share an EVSE interface but have different activation, sign, parameters, controls and evidence requirements.

## 2. Submechanism A — charging demand (`M2-TP-02`)

| Field | Working value |
|---|---|
| source | EV arrivals/charging decisions and requested charging profile |
| receiver | distribution-system loading/voltage/thermal/operating state |
| mechanism | `M-DEMAND` |
| interface | EV↔EVSE↔distribution bus |
| exchange | charging electrical demand |
| prior evidence | Lu et al. (2025) supply-demand dependency + FCS heterogeneity |
| parameter status | UNESTIMATED |
| current G2 | OPEN |

Activation requires connected compatible vehicle/EVSE, active charging request, and nonzero delivered demand. Managed charging/price/control must be modeled as mediator if it changes realized load.

## 3. Submechanism B — V2G/mobile support (`M2-TP-03`)

| Field | Working value |
|---|---|
| source | mobile storage/EV fleet available energy and dispatch state |
| receiver | grid support/restoration/operating state |
| mechanism | `M-ENERGY-SUPPORT` |
| interface | bidirectional compatible electrical/control interface |
| exchange | exported power/energy or ancillary service |
| parameter status | UNESTIMATED |
| current G2 | OPEN — DIRECT V2G EVIDENCE EXPANSION REQUIRED |

Activation requires, at minimum: compatible bidirectional hardware, stored energy, connected/available vehicles, authorization/control signal, and a grid-support mode that permits export.

## 4. Critical evidence caution

Anokhin et al. (2021) directly support **mobile power source** routing/restoration logic, not necessarily EV-based V2G. Therefore that paper may support the broader mobile-energy-support concept but **must not be cited as direct V2G proof**.

The current 11-paper core also does not provide sufficient direct V2G evidence for causal qualification. Dedicated V2G/EV aggregator/EVSE full-text evidence must be added before `G2-M` can pass for `M2-TP-03`.

## 5. Case evidence required — charging demand

- vehicle arrival/charging-demand process;
- EVSE connection and electrical crosswalk;
- delivered charging power/time series;
- charging-management/price/curtailment policy;
- distribution-system voltage/thermal/loading response;
- alternative loads and confounding demand drivers.

## 6. Case evidence required — V2G

- bidirectional EV/EVSE capability;
- aggregation/control architecture;
- state-of-charge and vehicle availability;
- export limits and efficiency;
- participation/dispatch rules;
- grid-service signal and measured response;
- counterfactual/alternative grid support sources.

## 7. Falsification examples

- charging-demand claim: no material receiver response within the declared sensitivity domain after controlling for other loads;
- V2G claim: export/support cannot occur under actual hardware/control/availability conditions, or measured grid response contradicts the proposed mechanism.

## 8. Current decision

~~~math
\boxed{G_2(M2\text{-}TP\text{-}02)=\mathrm{OPEN}}
~~~
~~~math
\boxed{G_2(M2\text{-}TP\text{-}03)=\mathrm{OPEN}}
~~~