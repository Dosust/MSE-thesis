# Stage 2 Evidence Dossier — P→T Traffic-Signal Electrical-Service Dependency

**Mechanism ID:** `M2-PT-01`  
**Status:** **OPEN — PRIOR MECHANISM EVIDENCE PRESENT; CASE CAUSAL QUALIFICATION NOT YET PERFORMED**

## 1. Tested causal claim

> When a traffic-signal controller depends on an external electrical supply and no adequate substitute/backup source maintains its required service, degradation or loss of the supplying electrical service can degrade or interrupt signal functionality.

## 2. Causal object fields

| Field | Working value |
|---|---|
| source | supplying power bus/feeder/service state |
| receiver | traffic-signal/controller operating state |
| direction | P→T |
| mechanism class | `M-PHYS-ELEC` |
| interface | electrical service connection to signal/control equipment |
| exchange semantic `Φ_e` | electrical service availability / required voltage-power service |
| realized signal `φ_e(t)` | verified supply/service state at the signal interface |
| parameter status | `UNESTIMATED` |
| current G2 | `OPEN` |

## 3. Prior literature evidence

Fotouhi, Moryadee & Miller-Hooks (2017), DOI `10.1016/j.ress.2017.01.026`, explicitly model a coupled traffic-electric-power system and state that coupling arises in part from **power needs of traffic signals**. This provides direct prior mechanism-family evidence, not a thesis-case connection.

## 4. Activation predicate — working form

~~~math
\mathcal A_e=1
\quad\text{if}\quad
\text{signal requires external supply}
\land
\text{supply state is below required service}
\land
\text{backup/substitute is absent, unavailable, or exhausted}.
~~~

The exact electrical threshold and backup logic remain case/equipment specific.

## 5. Case evidence required

- signal/controller asset ID and geometry;
- verified supply bus/feeder/electrical circuit crosswalk;
- controller electrical requirements and acceptable service envelope;
- backup battery/generator/UPS presence, capacity, switching logic and endurance;
- timestamped electrical outage/degradation state;
- timestamped signal operating state where available;
- maintenance/communication/controller fault records for alternative-explanation control.

## 6. Alternative explanations

- controller/device failure unrelated to upstream power;
- communication/control failure;
- maintenance outage;
- local backup supply;
- local protection/device trip;
- deliberate flashing/dark operating mode.

## 7. Falsification / revision condition

A strong falsifier would be repeated verified loss of the declared electrical service beyond the documented backup endurance while the signal remains normally functional, with no alternative supply path. Such evidence would force revision of the assumed interface, activation threshold, or mechanism.

## 8. Validity domain to declare

Controller technology, supply architecture, backup configuration, voltage/service limits, operating mode, jurisdictional equipment standard, and time horizon.

## 9. G2 state

| Gate | Current state | Reason |
|---|---|---|
| G2-M | PRIOR-SUPPORTED / OPEN | direct literature mechanism precedent exists; thesis case not yet qualified |
| G2-C | OPEN | case bus/feeder↔signal crosswalk required |
| G2-X | OPEN | interface/service must be verified for case equipment |
| G2-A | OPEN | backup and threshold conditions case-specific |
| G2-E | OPEN | empirical/operational evidence not assembled |
| G2-V | OPEN | case validity limits not declared |
| G2-F | DRAFTED | falsifier defined but not tested |

~~~math
\boxed{G_2(M2\text{-}PT\text{-}01)=\mathrm{OPEN}}
~~~