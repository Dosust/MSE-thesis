# Stage 2 Evidence Dossier — P→T EV Charging-Service Availability

**Mechanism ID:** `M2-PT-02`  
**Status:** **OPEN — MECHANISM FAMILY PLAUSIBLE; DIRECT CASE EVIDENCE REQUIRED**

## 1. Tested causal claim

> When an EV/charging demand requires service from an electrically connected EVSE, constraints or loss of the supplying electrical service can reduce or prevent charging service, subject to EVSE ratings, local storage, control, and charging-management rules.

## 2. Causal fields

| Field | Working value |
|---|---|
| source | distribution-grid/EVSE electrical service state |
| receiver | available EV charging service / transportation-energy availability |
| direction | P→T |
| mechanism class | `M-PHYS-ELEC` with possible `M-INFO-CTRL` mediation |
| interface | grid↔EVSE electrical interface |
| `Φ_e` | charging power/energy service availability |
| parameter status | UNESTIMATED |
| current G2 | OPEN |

## 3. Prior evidence basis

Lu et al. (2025), DOI `10.1016/j.energy.2025.135330`, model P–T dependency through fast-charging-station supply-demand behavior and show that FCS functional heterogeneity materially affects quantified dependency. This supports the importance of EVSE function/context and later parameter heterogeneity, but does not by itself verify a particular case connection or charging-response law.

## 4. Activation — working conditions

~~~text
EV/transport charging request active
+ compatible EVSE physically connected
+ EVSE requires grid/local electrical source
+ service constrained by grid/EVSE operating state
+ no sufficient local substitute/storage for requested service
~~~

Managed charging/price/control may mediate the source→receiver response and must be represented rather than hidden.

## 5. Case evidence required

- EVSE-to-bus/feeder electrical crosswalk;
- EVSE rated power, connector count, operating limits;
- local storage/onsite generation if present;
- charging-session/arrival/demand data or declared demand model;
- grid service/voltage/thermal constraint data;
- charging-control/curtailment/price rules;
- transportation consequence definition: unavailable energy, waiting, range/service impact, or route response.

## 6. Alternative explanations

EVSE hardware outage, network/payment/communications outage, vehicle incompatibility, demand absence, queue saturation, pricing response, onsite storage/generation, maintenance.

## 7. Falsifier / revision condition

If verified grid-service degradation within the claimed activation domain produces no charging-service change because the EVSE is independently supplied or the assumed grid constraint is irrelevant, the causal claim/interface must be revised.

## 8. Evidence gap

The present 11-paper Stage-1 precedent set is not sufficient for final Stage-2 qualification of this mechanism. Dedicated EV/EVSE operational and power-flow evidence must be added.

~~~math
\boxed{G_2(M2\text{-}PT\text{-}02)=\mathrm{OPEN}}
~~~