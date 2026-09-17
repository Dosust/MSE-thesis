# H2 Confirmatory Preregistration v1.0

**Status:** PRECONFIRMATORY STRUCTURE FROZEN — CONFIRMATORY EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-18  
**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Case authority:** `AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V2.md`

## 1. Canonical hypothesis

> **H2:** Under matched physical states and disturbances, changes in information availability and organizational conditions produce measurable differences in state-estimation quality, feasible control actions, response timing, recovery trajectories, and Stage-5 resilience outcomes.

H2 maps to RQ4/SO4.

## 2. Frozen nested comparison

```math
\mathscr N_0=P+T,
\qquad
\mathscr N_1=P+T+I,
\qquad
\mathscr N_2=P+T+I+O.
```

The intended contrasts are

```math
\mathscr N_1-\mathscr N_0=\text{information effect},
```

```math
\mathscr N_2-\mathscr N_1=\text{organizational effect}.
```

The physical trajectory generator, hazard draw, initial state, physical coupling, solver, and non-I/O parameters must be matched. A comparison is invalid if adding `I` or `O` also changes the physical model by construction.

## 3. Stage-4 objects

H2 may manipulate only explicitly defined Stage-4 objects such as

```math
(y,H,\mathcal E_{est},\hat X,I,O,\pi,u),
\qquad
u(t)=\pi(\hat X,I,O),
```

subject to the thesis distinction that `I` and `O` are supporting domains and are not automatically graph layers unless explicit topology is modeled.

## 4. Candidate response family

The confirmatory response family may include:

```text
state-estimation error;
observation latency/completeness;
control-action feasibility;
response delay;
service-loss trajectory;
recovery time/probability;
Stage-5 viability/reachability outcome.
```

The primary outcome, orientation, aggregation rule and H2 materiality threshold `delta_2` remain **OPEN** until observation and organizational evidence support them. No numerical I/O advantage may be chosen after inspecting H2 results.

## 5. Information intervention rules

An information condition must specify at minimum:

```text
observed variable(s);
sampling/latency;
missingness/error model;
estimator;
what decision receives the information;
what physical quantity is unchanged.
```

If the Austin data cannot support an empirical information architecture, H2 may remain a controlled sensitivity study and must be labeled accordingly rather than validated empirically.

## 6. Organizational intervention rules

An organizational condition must specify at minimum:

```text
authority/decision right;
resource or crew constraint;
communication/coordination delay;
feasible action set;
priority/dispatch rule;
evidence or declared scenario basis.
```

Organization may constrain feasible controls; it may not be represented by an unexplained scalar multiplier merely to create an effect.

## 7. Matched experiment and uncertainty

For experimental unit `omega`, evaluate

```math
Z_2^{(0)}(\omega),\quad Z_2^{(I)}(\omega),\quad Z_2^{(I+O)}(\omega)
```

under the same physical disturbance and parameter draw. Uncertainty attributable to sensing, estimation, organization, demand/hazard, model form and numerics must remain separately identifiable.

No random row-level splitting of temporally correlated observations is allowed for confirmatory calibration/validation.

## 8. Verification gates

Confirmatory H2 execution requires:

- Austin physical/coupling case admissibility for the physical baseline;
- qualified observation variables and errors/latencies;
- estimator verification and identifiability check where estimation is used;
- explicit organizational action/resource semantics;
- nested-comparator test showing the physical model is unchanged across `N0/N1/N2` except I/O conditions;
- independently frozen primary metric and `delta_2`;
- UQ and numerical verification.

## 9. Falsification/adjudication

H2 is not supported in the declared domain if the matched I or O changes fail to produce the preregistered meaningful response under the frozen metric and uncertainty rule.

Allowed states:

```text
SUPPORTED
PARTIAL
NOT SUPPORTED
INCONCLUSIVE
NOT YET TESTABLE
EXPLORATORY
```

## 10. Current authorization state

```text
Austin final admissibility: OPEN
observation architecture: OPEN
organizational case evidence: OPEN
primary H2 metric: OPEN
delta_2: OPEN
confirmatory execution: NOT AUTHORIZED
```
