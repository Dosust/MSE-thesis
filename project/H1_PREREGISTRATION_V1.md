# H1 Confirmatory Preregistration v1.0

**Status:** PRECONFIRMATORY STRUCTURE FROZEN — CONFIRMATORY EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-18  
**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Threshold authority:** `H1_THRESHOLD_PROVENANCE_V1.md`  
**Case authority:** `AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V2.md`

## 1. Canonical hypothesis

> **H1:** Under matched Power–Transportation disturbances and initial conditions, an evidence-grounded dynamic causal coupling representation provides measurable incremental explanatory or predictive information for preregistered cascade, service-loss, spatial-propagation, and recovery outcomes relative to corresponding static-coupling and independent-system representations.

H1 maps to RQ3/SO3 with developmental inputs from RQ1/SO1 and RQ2/SO2.

## 2. Frozen comparator architecture

```math
M_0=\text{independent }P+T,
\qquad
M_1=\text{static/algebraic }P\text{--}T\text{ coupling},
\qquad
M_2=\text{dynamic causal }P\text{--}T\text{ coupling}.
```

Primary scientific contrast:

```math
\boxed{M_2\;\text{vs}\;M_1}
```

with `M0` retained as the uncoupled reference.

The matched experiment must keep the same topology, initial state, exogenous demand, hazard realization, numerical resolution, service definitions, and non-coupling parameters across the three models. Only the coupling representation may differ for the H1 contrast.

## 3. Admissible Austin mechanisms

Until separately versioned evidence changes the case definition, H1 may use only:

1. `P→T`: electrical service affects retained traffic-signal operation/service through a reproducible semisynthetic SMART-DS-to-signal mapping;
2. `T→P`: qualified road accessibility affects repair access/restoration;
3. flood: common-cause exposure, not an interdependency edge.

No EV/V2G, charger-feedback, or other coupling enters confirmatory H1 merely because it is physically plausible.

## 4. Candidate response vector

```math
Z_1=
\begin{bmatrix}
T_C\\
N_{\rm fail}\\
L_{\rm service}\\
V_{\rm spatial}\\
T_{\rm recovery}
\end{bmatrix}.
```

The exact primary response, aggregation function `D`, orientation, and materiality threshold `delta_1` remain **OPEN** until the Austin data/threshold gates provide same-quantity provenance.

## 5. H1a — representation distinguishability

H1a asks whether the dynamic causal representation produces a reproducibly distinguishable matched response relative to `M1` without claiming engineering materiality before an engineering threshold exists.

For each matched experimental unit `omega`:

```math
\Delta Z_1(\omega)=Z_1^{M_2}(\omega)-Z_1^{M_1}(\omega).
```

H1a may be reported as `REPRESENTATION-DISTINGUISHABLE` only if the paired effect survives preregistered UQ and physical/numerical verification. It may not be upgraded to engineering support using the observed difference itself to choose `delta_1`.

## 6. H1b — held-out predictive validation

H1b is a separate external-validation claim. Calibration and validation must use independent events/cases rather than time points sampled from the same event.

A candidate held-out error is

```math
E_{PT}(M)=\frac{1}{T}\int_0^T\|\hat S_M(t)-S_{obs}(t)\|_W\,dt,
```

with

```math
\Delta E=E_{PT}(M_2)-\min\{E_{PT}(M_0),E_{PT}(M_1)\}.
```

The predictive threshold `epsilon_pred` must be frozen from the actual observation/noise architecture before the validation result is inspected. Synthetic self-generated truth is insufficient for H1b.

## 7. Frozen uncertainty rule

Paired model comparisons must reuse the same scenario/parameter draw across `M0/M1/M2`. The uncertainty registry must distinguish hazard, demand, coupling parameters, observation, repair, model-form, and numerical uncertainty. Correlated observations may not be randomly row-split.

Bootstrap/resampling units must be independent events/scenarios rather than internally correlated time rows. Effect sizes, interval estimates, scenario stratification, physical residuals, and numerical-convergence evidence are primary; p-values are secondary.

## 8. Verification gates

Confirmatory execution is prohibited until all applicable gates pass:

- **V0 model/code:** units, domains, initial/boundary conditions, conservation/physical admissibility, event/reset logic, limiting cases;
- **V1 nesting:** `M0/M1/M2` differ only by the intended coupling representation;
- **V2 numerical:** timestep/solver convergence and deterministic regression tests pass;
- **V3 Austin mechanisms:** P→T/T→P mapping gates pass;
- **V4 threshold:** primary outcome, `D`, `delta_1`/service materiality and uncertainty floor frozen independently;
- **V5 held-out validation:** independent observation architecture frozen for H1b.

## 9. Falsification/adjudication

H1 is not supported in the declared domain if `M2` fails to provide the preregistered meaningful incremental information relative to `M1` under the matched comparison and UQ rule.

Allowed adjudications:

```text
SUPPORTED
PARTIAL
NOT SUPPORTED
INCONCLUSIVE
NOT YET TESTABLE
REPRESENTATION-DISTINGUISHABLE (H1a only)
```

## 10. Current authorization state

```text
Austin final admissibility: OPEN
primary response/aggregation: OPEN
engineering materiality delta_1: OPEN
observation uncertainty: OPEN
held-out validation events: OPEN
M0/M1/M2 confirmatory run: NOT AUTHORIZED
```

The minimal demonstrator may be used for verification only; it may not be presented as confirmatory Austin evidence.
