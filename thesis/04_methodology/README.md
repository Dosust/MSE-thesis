# Chapter 4 — Methodology and Experimental Design

**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Current-scope authority:** [`../../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`](../../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md)  
**Status:** CURRENT WORKING METHODOLOGY  
**Date:** 2026-10-06

## Purpose

Test whether explicitly modeling heat-dependent physical states and state-time evolution changes predicted Power–Transportation service consequences and the engineering value of Improve, Adapt, and Restore actions.

---

## Methodological chain

```text
Evidence qualification
→ scope qualification
→ component/interface selection
→ minimum-sufficient physics
→ state + constraint definition
→ matched heat scenarios
→ state-time simulation / estimation
→ transition / propagation / service extraction
→ intervention comparison
→ verification
→ validation
→ uncertainty quantification
→ engineering inference
```

---

## Scope gate

A candidate mechanism enters the active model only if it passes:

```text
research relevance
+ service relevance
+ physical measurability
+ data/model feasibility
+ Master's tractability
```

The road-over-rail decision is **WORKING-FROZEN**.

Next scope decision:

```text
public DC fast charging
vs
fleet/depot charging
```

---

## Candidate matched model hierarchy

```text
M0 — nominal/static baseline
M1 — heat-dependent component/interface physics
M2 — M1 + coupled P–T interface/service propagation
M3 — M2 + Improve/Adapt/Restore interventions
```

This hierarchy is a **current candidate methodology**, not an established standard. It must be frozen before confirmatory use.

Matched conditions should preserve, where applicable:

- topology;
- demand;
- component inventory;
- heat event;
- initial state;
- service requirements;
- simulation horizon.

---

## Physics layer

For selected component/interface `i`:

```math
\dot X_i=f_i(X_i,H,L_i,Z_{ji},u_i;\theta_i).
```

Do not force heterogeneous assets into one universal component equation.

---

## State-time outputs

Primary candidate outputs:

```math
X_i(t),\qquad
\tau_i^C,\qquad
\delta_{ij},\qquad
Q_P(t),Q_T(t).
```

Possible service deficit:

```math
D_k=\int [Q_k^{req}-Q_k(t)]_+\,dt.
```

Any confirmatory metric must be defined before inspection of confirmatory results.

---

## Intervention experiments

### Improve
Compare a declared design/parameter change with a matched baseline.

### Adapt
Compare a declared operational control with a matched no-adaptation/reference policy.

### Restore
Compare a declared recovery action/policy after service degradation.

Evaluate interventions through physical and service consequences, not model complexity.

---

## Data roles

Data may have distinct roles:

```text
forcing
parameterization
initialization
calibration
validation
service observation
```

Do not reuse one evidence object across incompatible roles without justification.

---

## VVUQ

### Verification
Check equations/code against analytical limits, standards, conservation laws, or known cases.

### Validation
Compare modeled quantities against independent empirical/experimental/operator evidence appropriate to the context of use.

### Uncertainty quantification
Propagate uncertainty in:
- heat forcing;
- operating load;
- physical parameters;
- threshold values;
- demand;
- initial conditions.

### Decision/ranking stability
If plausible uncertainty reverses a ranking, do not claim a definitive ranking.

---

## Prohibited practices

- simulation presented as validation;
- post hoc confirmatory thresholds;
- assumed values presented as measurements;
- causality inferred from topology/correlation alone;
- state variables with no physical semantics;
- cascade claims without sequential dependent mechanisms;
- instability claims without stability analysis;
- resilience rankings based only on raw temperature when service is the objective;
- model complexity treated as engineering improvement.

---

## Exit gate

Confirmatory execution is authorized only after:

- exact charging context is frozen;
- selected states are defined;
- state equations/parameters have admissible evidence;
- interface exchanges are qualified;
- service metrics are operationalized;
- matched baselines are frozen;
- validation evidence is identified;
- uncertainty plan is frozen;
- intervention definitions are frozen;
- non-support/falsification logic is declared;
- narrowed RQ/SO/H is frozen.
