# Approved IEEE feeder and active coupling decision — 2026-10-09

**Decision authority:** Explicit user approval, 2026-10-09.
**Status:** APPROVED benchmark choices; actual hardware configuration, model parameters and evidence admission remain OPEN.
**Thesis scope:** Physical-state-and-time mechanisms for thermally conditioned interdependencies between distinct Power (P) and Electrified Transportation (T_e) systems under extreme heat.

## Approved choices

1. **Primary reference:** IEEE 123-node distribution test feeder.
2. **Development and verification reference:** IEEE 13-node distribution test feeder.
3. **Initial active coupling configuration:** One explicitly defined transformer → grid-side AC measurement/exchange interface → EVSE → vehicle pathway. This sequence is an architecture and exchange path, **not proof of either thermally conditioned causal direction**.
4. **Component completeness:** Retain the 40-entry candidate coverage ledger (P01–P19 and T01–T21), identifying overlaps, service and environmental records, and conditional capabilities; do not force each class into a separate ODE or PDE.
5. **Benchmark limitation:** Both IEEE feeders are synthetic electrical test systems suitable for reproducible computational study; they cannot alone validate equipment thermal physics, field causal effects or mobility service outcomes.

## Required next gates before active system admission

- Verify the official feeder files and reproduce the published electrical base case for IEEE 13-node and then IEEE 123-node; report versions, unbalanced phase representation, transformers, regulator data, impedances, connections and numerical tolerances.
- Select and record a **particular** test-feeder transformer, its mineral-oil/dry-type construction, cooling method, ratings, topology and actual upstream/downstream position before choosing thermal standards or states.
- Define the grid-side AC measurement plane and phase/sign conventions; account for harmonic effects when relevant; do not substitute charger DC delivered energy for grid-side AC power.
- Define EVSE mode (AC or DC), internal conversion topology, cooling and thermal-control details, charging connection, actual permitted power and vehicle-side acceptance.
- Define vehicle/battery architecture only to the extent demanded by the chosen energy/mobility service mechanism; V2G stays conditional.
- Specify synthetic extreme-heat boundary trajectories separately from the IEEE electrical data; report data provenance or explicitly flag illustrative forcing.
- Obtain equipment-specific admissibility evidence for thermal laws, switching/derating controls and timescales; leave unknown coefficients OPEN.
- Trace both P→T_e and T_e→P individually through actual state → constraint/control → measured AC exchange → service. Shared heat forcing and network links alone do not demonstrate causal propagation.
- Register service observables and time clocks: exposure, thermal transitions, directional propagation, session/departure deadlines and recovery.
- Preserve frozen thesis objectives, scope, 13-slide presentation authority and evidence/non-invention gates. No additional research objectives authorized by this decision.

**Do not claim:** IEEE benchmark includes real EVSE temperature curves, validated transformer time constants, manufacturer trip limits, field mobility records or empirically demonstrated heat-induced cross-sector propagation.
