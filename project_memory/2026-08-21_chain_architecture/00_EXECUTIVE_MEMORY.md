# Executive Memory Snapshot

## Thesis identity

**Working title:** Mathematical Physics of Sustainable Infrastructure Resilience.

**Current precise formulation:** *Equity-Constrained Viability of Coupled Power–Water–Transportation–Solid-Waste Systems with Dynamic Interfaces under Climate Stress*.

**Physical system:** Power (P), Water/drainage (W), Transportation (T), Solid Waste (SW).

**Primary demonstrator:** urban flooding with endogenous drainage–waste feedback and cross-sector consequences.

## Current scientific center

The thesis is centered on the transition

```text
observe → identify coupling → model dynamics → define admissibility → compute viability → compute recoverability → determine admissible intervention
```

Mathematically:

```text
D_obs → (G_hat, theta_hat, Sigma_theta) → F_dyn → K_R → V_R → C_R → U_recovery
```

with the central geometric object

`∂V_R` = the viability boundary.

The three governing questions are:

1. **What moves the viability boundary?**
2. **How uncertain is that boundary?**
3. **What interventions or designs move it in a favorable direction?**

## Six-chain ontology

The project now distinguishes six interacting scientific chains:

1. **Physical-system chain:** physical laws → structure → interdependencies → interfaces → states/flows → dynamics/cascades.
2. **Observation–inference–prediction chain:** observe → observability → identify → estimate → assimilate → uncertainty → predict.
3. **Hazard–failure–consequence chain:** hazard → exposure → vulnerability → damage → cascades → functionality/service loss → consequence/risk.
4. **Resilience–viability–recovery chain:** state → admissibility → viability → reachability → service continuity → recoverability → recovery → control.
5. **Engineering lifecycle chain:** requirements → design → deploy → operate → monitor → maintain → retrofit → restore/adapt/circularize.
6. **Societal decision chain:** needs → alternatives → evaluate → trade off → decide → implement → learn → revise.

These are **not one linear causal chain**. They answer different classes of scientific questions and interact through feedback.

## Mathematical core

A general reduced hybrid multiscale model is

```text
X_dot = F(X,Z,m,u,eta;theta)
epsilon Z_dot = G(X,Z,m,eta;theta)
m+ = Phi(X,Z,m,eta)
Y = H(X,Z;theta) + epsilon_Y
```

The admissible region is

`K_R = K_phys ∩ K_service ∩ K_sus ∩ K_eq`.

The viability kernel is the set of states from which an admissible control can keep the system inside `K_R`.

The recovery/capture set contains states from which `V_R` can be reached in finite time. Recovery time is represented by `tau_R(x0)`.

Dynamic versus static coupling is tested through

`Delta_V = d_H(V_dynamic, V_static)`

and a timescale ratio

`rho_ij = tau_interface,ij / tau_system`.

## Frozen proposition family

- P1 / H0: dynamic interfaces materially alter viability/recovery geometry relative to static coupling.
- P2 / H1: interface identifiability controls the reliability of inferred viability.
- P3 / H2: interface/system timescale ratios govern static-coupling approximation validity.
- P4 / H4: sustainability/equity constraints deform the viable region beyond technical constraints.
- P5 / H5: recovery/capture geometry contains information not captured by viability alone.
- P6 / H6: waste–drainage–flood feedback shifts coupled P–W–T–SW resilience boundaries.
- P7 / T1: reduced models used for decisions must preserve or conservatively bound projected full-order viability geometry.
- H3 remains the interface-criticality proposition: viability-boundary deformation defines a different criticality concept from conventional topological/flow importance.
- H7 remains an optional extension for time-varying admissible regions / nonanticipative recovery.

## Three end-to-end thesis alternatives

- **Type I — Theory-first:** physics → coupled dynamics → viability/recovery theory → control → design/decision. Question: *What is mathematically possible?*
- **Type II — Digital Twin:** observations → inverse identification/UQ → dynamic twin → forecast → probabilistic viability → adaptive control/design. Question: *What is happening, what will happen, and what should be done now?*
- **Type III — Resilience-by-Design:** requirements → candidate design → design-dependent dynamics → viability/recovery constraints → optimization → investment/planning decision. Question: *What should be built so acceptable behavior remains possible?*

Current MSE recommendation: keep **resilience/viability as the center**, use identification and dynamics upstream, include control as an enabling layer, and treat full optimal design/policy as downstream extension unless scope permits a small demonstration.

## Evidence state

The project maintains two separate evidence tracks:

- **PRISMA / literature evidence** for precedent, gaps, and falsification.
- **Mathematical development** for model definition, well-posedness, identification, viability/reachability, recovery, UQ, control and numerical analysis.

Evidence has authority over the starting architecture: finding a direct precedent is a successful falsification result, not a failure.

The locked 325-record Monte Carlo exercise ranks papers **within that dataset only**. It does not establish global novelty or global literature completeness.

## Repository state

The repository has already been converted from a simple archive into a scientific portal with:

- mathematical landing page;
- formal mathematical foundation;
- machine-readable propositions and model schema;
- Python and Julia reference implementations;
- SVG mathematical art;
- Type I/II/III framework images;
- automated scientific QA;
- transcript/provenance/archive material;
- PRISMA/Monte Carlo prompt and final-run records.

## Critical epistemic rule

Always distinguish:

- **verified literature precedent**;
- **mathematical definition**;
- **proposed thesis hypothesis**;
- **synthetic/QA computation**;
- **empirical/calibrated result**;
- **pending systematic-search result**.

Do not collapse these categories.