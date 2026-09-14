# EGMIV H1 Threshold Provenance Study v1.0

**Status:** PARTIALLY FROZEN — numerical components frozen; observation and engineering components not yet admissible for final threshold lock.  
**Date:** 2026-09-14  
**Purpose:** establish decision-threshold provenance independently of confirmatory M0/M1/M2 effect sizes.

## 1. EGMIV decision

The threshold study was executed under the rule:

```math
\text{evidence}\rightarrow\text{native quantity}\rightarrow\text{mapping}\rightarrow\text{uncertainty}\rightarrow\text{admissibility}\rightarrow\epsilon.
```

A published standard or guideline is **not** allowed to become a thesis threshold unless its native quantity maps defensibly to the thesis service metric.

The present result is:

```math
\boxed{u_{num,P}=0.000416667,\qquad u_{num,T}=0.001281963}
```

for the current minimal H1 demonstrator at

```math
\boxed{\Delta t=0.00125\;\mathrm{h}=4.5\;\mathrm{s}}
```

with an independent refinement check at `0.000625 h = 2.25 s`.

However, `u_obs,P`, `u_eng,P`, `u_obs,T`, `u_eng,T`, and `epsilon_pred` cannot yet be frozen without the actual validation-data architecture and service-level requirements.

Therefore:

```math
\boxed{\epsilon_P\;\text{NOT YET FROZEN},\qquad\epsilon_T\;\text{NOT YET FROZEN},\qquad\epsilon_{pred}\;\text{NOT YET FROZEN}.}
```

This is a scientific result, not a failure.

## 2. Numerical uncertainty — executed

The numerical component was estimated without using M2−M1 confirmatory effect sizes.

For each verification scenario, M2 was rerun at progressively finer time steps. The service trajectories at `Delta t = 0.00125 h` were compared against `0.000625 h` using a left-hold projection onto the finer grid.

Worst time-averaged service discrepancy across verification scenarios:

```math
\boxed{u_{num,P}=0.000416667}
```

or **0.0417% of full service scale**, and

```math
\boxed{u_{num,T}=0.001281963}
```

or **0.1282% of full service scale**.

The dominant power numerical discrepancy came from the discrete restoration-time boundary in S3R. The dominant transport discrepancy came from the outage/queue-recovery scenario S2.

A further refinement to `0.0003125 h` reduced these discrepancies again, supporting convergence rather than numerical instability.

For **H1 minimal-demonstrator v1**, use `Delta t = 0.00125 h` and retain the values above as conservative verification-derived floors until the final network/data resolution changes. If demonstrator topology, CTM cell size, repair-event discretization, or solver changes materially, rerun numerical provenance.

## 3. Power observation uncertainty

IEC 62053-22:2020 specifies transformer-operated static active-energy meter accuracy classes including 0.2S and 0.5S. The standard applies to meter type testing; therefore an accuracy-class label is **not** automatically the total field uncertainty of the thesis service metric.

For a ratio `S=A/B`, if numerator and denominator each have bounded relative measurement error `b`, a conservative ratio bound is

```math
u_{ratio}^{bound}=\frac{1+b}{1-b}-1.
```

Conditional instrument-only examples:

- class 0.2S: `b=0.002` gives `u_ratio^bound = 0.004008016 ≈ 0.401%`;
- class 0.5S: `b=0.005` gives `u_ratio^bound = 0.010050251 ≈ 1.005%`.

These are not final `u_obs,P` values.

Our power-service definition is

```math
S_P(t)=\frac{\sum_i\omega_i p_i^{srv}(t)}{\sum_i\omega_i p_i^d(t)}.
```

During an outage, part of `p_i^d(t)` is counterfactual demand: the meter cannot directly observe electricity that would have been consumed if supply had remained available.

Therefore the observation uncertainty must include at least

```math
\boxed{u_{obs,P}=\mathcal U(u_{meter},u_{counterfactual\ demand},u_{aggregation},u_{temporal},\Sigma_P).}
```

Until the counterfactual-demand estimator and sensing chain are fixed, **no numeric `u_obs,P` is admissible**.

## 4. Transportation observation uncertainty

FHWA guidance provides useful native-quality evidence:

- properly functioning single inductive loops can exceed 95% count accuracy;
- a FHWA traffic-monitoring guidebook gives a rule-of-thumb that a simultaneous manual count should agree within ±2% of a permanent inductive-loop automatic count for equipment QA.

These are not the same as uncertainty in our service ratio.

Conditional bounds are:

- ±2% per count: `u_ratio^bound = 1.02/0.98 - 1 = 0.040816327 ≈ 4.082%`;
- 5% per count: `u_ratio^bound = 1.05/0.95 - 1 = 0.105263158 ≈ 10.526%`.

But our mobility service is

```math
S_T=\frac{\text{weighted completed OD flow}}{\text{weighted requested OD flow}}.
```

Thus loop-count accuracy alone is insufficient. Final observation uncertainty must include

```math
\boxed{u_{obs,T}=\mathcal U(u_{count},u_{OD},u_{coverage},u_{trajectory\ matching},u_{temporal},\Sigma_T).}
```

If validation uses probe/GPS data instead of fixed loops, rebuild this uncertainty model for that source. FHWA NPMRDS documentation also shows explicit temporal/spatial aggregation, reinforcing that temporal resolution must be carried separately from amplitude accuracy.

## 5. Engineering significance: Power

The power-resilience evidence does **not** support a universal load-service significance threshold.

NREL states that no single resilience definition or metric applies broadly; suitable metrics depend on goals, hazard/event context, scale, and stakeholder perspective. PNNL likewise notes that critical-load weighting has no one-size-fits-all solution and depends on operator/system conditions.

Therefore:

```math
\boxed{u_{eng,P}\;\text{is not universal}.}
```

It cannot be borrowed directly from voltage limits, SAIDI/SAIFI, or an arbitrary percent-load threshold because those are different quantities. A final `u_eng,P` must come from the chosen demonstrator's service requirement, such as minimum critical-load service, a utility restoration target, or another formally justified stakeholder criterion.

Until then, H1a may establish **representation distinguishability**, but not engineering materiality.

## 6. Engineering significance: Transportation

FHWA target-setting guidance treats performance targets as agency/context/data-driven quantities. It does not provide a universal target for our completed-OD/requested-OD service ratio.

LOTTR=1.5, travel-time-index thresholds, and related FHWA measures are useful transportation performance measures, but they are **not numerically interchangeable with** `S_T`.

Therefore:

```math
\boxed{u_{eng,T}\;\text{is not universal}.}
```

It must be derived from a service requirement that uses the same or a defensibly transformed quantity as `S_T`.

## 7. Predictive threshold

The pre-registration defines

```math
\epsilon_{pred}=Q_{0.95}(|\mathcal E^{noise}|).
```

ASME VVUQ distinguishes numerical, input, model-form and experimental/data uncertainty. For H1b, the predictive noise floor must be generated from the actual calibration/validation architecture.

Because no independent held-out validation events and observation-error model have yet been frozen:

```math
\boxed{\epsilon_{pred}\;\text{cannot yet be computed}.}
```

This prevents synthetic self-validation.

## 8. Threshold admissibility table

| Quantity | Result now | Status |
|---|---:|---|
| `u_num,P` | 0.000416667 | **FROZEN for minimal demonstrator v1** |
| `u_num,T` | 0.001281963 | **FROZEN for minimal demonstrator v1** |
| `u_obs,P` | conditional instrument bounds only | **PENDING measurement + counterfactual-demand architecture** |
| `u_obs,T` | conditional count bounds only | **PENDING OD observation architecture** |
| `u_eng,P` | no universal threshold supported | **PENDING case-specific service requirement** |
| `u_eng,T` | no universal threshold supported | **PENDING case-specific service requirement** |
| `epsilon_P` | — | **NOT YET FROZEN** |
| `epsilon_T` | — | **NOT YET FROZEN** |
| `epsilon_pred` | — | **NOT YET COMPUTABLE** |

## 9. Rejected shortcuts

The following are explicitly **inadmissible**:

1. using the observed M2−M1 benchmark difference to choose `epsilon`;
2. treating IEC meter class as the complete `S_P` uncertainty;
3. treating loop-detector accuracy as complete OD-service uncertainty;
4. using voltage-band limits as a direct `S_P` threshold;
5. using LOTTR/TTI thresholds as a direct `S_T` threshold;
6. choosing 5%, 10%, or another round number without a same-quantity service requirement;
7. computing `epsilon_pred` from synthetic outputs generated by the model being validated.

## 10. EGMIV gate decision

Threshold provenance is **partially complete**.

We may freeze the numerical component, but the confirmatory H1a experiment is still blocked by:

```math
\boxed{\text{Observation architecture}\rightarrow u_{obs,P},u_{obs,T}}
```

and

```math
\boxed{\text{Case-specific service requirements}\rightarrow u_{eng,P},u_{eng,T}.}
```

Only after those are established can we compute

```math
\epsilon_P=\max(u_{obs,P},u_{num,P},u_{eng,P})
```

and

```math
\epsilon_T=\max(u_{obs,T},u_{num,T},u_{eng,T}).
```

## 11. Evidence anchors

- IEC 62053-22:2020 — static AC active-energy meters, accuracy classes 0.1S/0.2S/0.5S; type-test scope.
- IEC 62053-21:2020 — active-energy meters and accuracy-class-specific requirements.
- FHWA Traffic Detector Handbook — count accuracy for properly functioning inductive-loop systems.
- FHWA Traffic Monitoring Guide / Guidebook — traffic-data QA and permanent-counter comparison guidance.
- FHWA Transportation Performance Management target-setting guidance — targets are contextual and data driven.
- NREL, *Valuing Resilience in Electricity Systems* — resilience metric choice depends on goals, context, hazards, scale, and perspective.
- PNNL, *Power System Resilience Metrics Augmentation for Critical Load Prioritization* — no one-size-fits-all critical-load weighting.
- ASME VVUQ standards portfolio — numerical, validation and uncertainty components must remain distinguishable.
