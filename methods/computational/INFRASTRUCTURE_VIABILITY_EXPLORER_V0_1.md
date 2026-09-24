# Infrastructure Viability Explorer v0.1 — computational specification

## Status

**Proposal / synthetic demonstrator.** This artifact establishes an executable research-software path from coupled dynamics to geometry, ML surrogate validation, deterministic data export, and synchronized animation. It does not introduce a declared thesis result.

## Purpose

The implementation operationalizes this chain:

mathematical model → computational experiment → reusable visual primitives → synchronized scientific visualization → testable research questions

Computation and rendering are separated. Python generates a versioned, hashed experiment record; the browser only visualizes that record.

## Reduced state and domain

The reduced state is Y(t) = [P(t), T(t), C_PT(t)] in [0,1]^3, where P is normalized power service, T is normalized transportation service, and C_PT is normalized interface health.

The synthetic hazard eta(t) is a bounded Gaussian pulse in [0,1].

## Demonstrator dynamics

dP/dt = r_P(1-P) - h_P eta P - k_TP(1-T)P

dT/dt = r_T(1-T) - h_T eta T - k_PT(1-P)T

dC_PT/dt = r_C(1-C_PT) - h_C eta C_PT - k_M |P-T| C_PT

For non-negative rates, the continuous vector field points inward on the faces of the unit cube. The implementation uses fixed-step classical RK4 and a floating-point guard to prevent numerical overshoot.

These equations are declared prototype mechanisms, not empirically calibrated laws.

## Sustainability constraint set and margin proxy

The declared threshold set K_sus requires P >= P_min, T >= T_min, and C_PT >= C_min.

For diagonal metric g = diag(w_P,w_T,w_C), the signed constraint-margin proxy is the minimum across components of sqrt(w_i) times (Y_i - Y_i,min).

A positive margin means all declared thresholds are satisfied. This is a distance-to-threshold construction. It must not be relabeled as rho_V or a viability-kernel distance until control admissibility, reachability, and invariance are explicitly solved.

## ML surrogate

The ML layer is a transparent ridge-regression surrogate for the synthetic vector field, mapping (P,T,C_PT,eta) to an estimate of dY/dt.

The feature map is declared in source code and includes direct state terms, hazard interactions, directional coupling features, and service-deficit features. Training uses a deterministic synthetic design; validation uses fixed hold-out states not used in the training grid.

Low synthetic hold-out error does not imply empirical predictive validity. The purpose is to validate the software contract for a later evidence-supported learned dynamics or residual model.

## Sensitivity diagnostic

For a selected model parameter theta_j, the demonstrator reports a forward finite-difference sensitivity of the minimum constraint margin after an additive perturbation Delta.

This is model sensitivity. It is not causal identification and not yet the thesis's final interface-criticality operator.

## Reliability controls

1. Deterministic fixed-step integration.
2. Bounded state and hazard validation.
3. Explicit numerical step-size guard.
4. Deterministic synthetic ML training design.
5. Deterministic hold-out validation.
6. Exact JSON regeneration check in CI.
7. SHA-256 fingerprint over the canonical exported payload.
8. Explicit epistemic status fields in exported data.
9. Python 3.10, 3.11, and 3.12 focused CI matrix.
10. Visualization reads generated data rather than recomputing science in JavaScript.

## Expansion gates

1. Replace the reduced graph with an explicit multilayer G_P, G_T, E_PT data model.
2. Connect hazard forcing to spatially located components.
3. Add observation and state-estimation uncertainty.
4. Introduce a physics-plus-learned-residual model with held-out scenario validation.
5. Solve controlled reachability and viability before using viability-kernel language.
6. Add uncertainty propagation and confidence or credible bands.
7. Define interface criticality against the approved thesis operator and falsification tests.
8. Keep strategic interventions a_k separate from operational controls u(t).
