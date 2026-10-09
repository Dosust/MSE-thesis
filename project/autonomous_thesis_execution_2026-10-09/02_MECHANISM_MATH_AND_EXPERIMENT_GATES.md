# Mechanism, minimal mathematics and experiment test contract
Status: T1 research derivation and blocked empirical admission; no installed specific equipment model.

## Research problem [T1 / OPEN novelty]
Under identical external heat forcing and baseline loading, can independently qualified, temperature-dependent P→T_e and/or T_e→P interface mechanisms change the predicted timing or adequacy of declared electricity and mobility services relative to models without these mechanisms? Closest literature must be subtracted before originality is claimed.

## Physical architecture and four-field component admission
| Component | Input | Physical transformation | Output | State-conditioned behavior / status |
|---|---|---|---|---|
| P transformer | electrical voltage/current/load; environmental forcing | electromagnetic transfer, loss heat, stored thermal energy and heat rejection | downstream electrical flow, internal thermal condition | state→permissible-power map OPEN |
| P feeder/control | upstream flow, ratings, sensed conditions | power transfer/losses, actual implemented controls | electrical capability/availability | exact voltage/protection policy OPEN |
| T_e EVSE | AC supply, vehicle request, ambient forcing | electrical conversion/losses/cooling | DC delivered power, AC demanded power, waste heat | derating shown in literature for particular hardware; own equipment law OPEN |
| T_e battery | battery-side charging power, energy state | net storage, losses/auxiliaries | battery energy and charging acceptance | temperature condition only if relevant and evidenced |
| T_e fleet requirement | vehicle readiness and duty schedule | operational service assessment, not an additional physical energy conversion component | deadline energy margin or completed mobility | actual service definition OPEN |

## Conservation-based minimum structure [T1]
A thermodynamic control-volume energy balance, if a lumped representation is admissible:
`dU_P/dt = P_loss,P - Q_reject,P`
`dU_E/dt = P_loss,E - Q_reject,E`
These describe conservation only. Identifying exact temperatures, effective heat capacitances, loss laws, cooling laws and measurement locations requires case evidence. They are **NOT the admitted transformer or charger ODEs**.

At a compatible electrical interface and appropriate sign convention:
`P_AC,in = P_DC,out + P_EVSE,loss`
is a steady-state/converter-averaged accounting relation *only if* relevant internal energy storage is negligible and auxiliaries are included in the loss term; otherwise use `P_AC,in = P_DC,out + P_loss + dU_electrical/dt` with consistent control-volume definition. AC phase/power factor and net DC/battery acceptance must be treated explicitly when applicable.

Generic coupled system [T1]:
`dot X_P = F_P(X_P,Z,H,u;theta_P)`
`dot X_T = F_T(X_T,Z,H,u;theta_T)`
`0 = G(X_P,X_T,Z,H,u;theta)`
`Q = S(X_P,X_T,Z,u)`.
Here H external forcing; Z interface flow algebraic by default; capabilities and services outputs; battery SOC an energy state, not thermal; no temperature threshold invented.

### Candidate event and effect [T1]
Critical event defined *only when* a physically justified limit exists:
`t_i^C = inf {t in [t0,tf]: g_i(X(t),H(t),t)=0}`.
If none occurs, record NO CROSSING. A candidate event-relative delay is `delta_ij = t_j^response - t_i^source` **only when** receiver change is attributable via qualified mechanism, not merely common temperature exposure.

## Model comparison contracts — DO NOT run unqualified simulation as confirmatory
- Baseline M0: P and T_e respond independently to the identical external heat forcing. Establish shared-environment effects first.
- Comparator M1: actual electrically exchanged power and fixed/basic operating constraints; no unsupported thermal limit.
- Candidate M2: *only verified* temperature-conditioned interface constraint/feedback admitted to M1; if no thermal coupling law exists, M2 is blocked.
- One intended modeling difference per matched contrast; hold weather, initial states, demand, equipment, measurements and service requirements fixed. Counterfactual necessity of thermal coupling must be tested where identifiable.
- Primary candidate QOIs: justified critical event times, source-response delay if identifiable, AC supply/energy at declared boundary, delivered battery-side energy, vehicle requirement satisfaction. Prespecify error metrics and meaningful difference thresholds from the decision context.
- Data split: calibrate on separate development sets; independently validate on held-out equipment sessions/conditions with no leakage. If no validation evidence, downgrade to unvalidated demonstration.
- Numerical verification: energy-balance residual, dimensional checks, initial/algebraic consistency, physical bounds, time-step/solver convergence, event-time interpolation tests. None is empirical validation.

## Scientific difference between matched candidate and reality
- A mathematically plausible S-shaped derating function is not an actual EVSE control curve.
- A transformer top-oil threshold is not automatically a protection trip or service reduction.
- Transformer oil/hot-spot candidates are not admitted as a final two-dimensional state.
- Correlated temperature or power trajectories do not identify propagation.
- Missing expected causal response can be informative *only after* sufficient measurement and test sensitivity.

## Decision gates
G1 primary full-text and closest-prior-art: OPEN.
G2 equipment admissibility and exact physical interface: OPEN.
G3 parameters, forced inputs and service requirements: OPEN.
G4 minimum-sufficient differential/algebraic law: OPEN.
G5 numerical verification: BLOCKED by G4.
G6 independent calibration/validation: BLOCKED by G2–G4.
G7 matched experiments/uncertainty: BLOCKED by G2–G6.
G8 publishable conclusion: BLOCKED by G1,G5–G7.

Source anchors: Hilshey et al. (2013), https://doi.org/10.1109/TSG.2012.2217385; Krama et al. (2026), https://doi.org/10.1016/j.ecmx.2026.101960; current admission and scope authorities noted in file 01.
