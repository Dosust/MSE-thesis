# Global Final-Case Uncertainty Template v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.5 UNCERTAINTY RECORD

## 1. Uncertainty record

For each field \(f\):

~~~math
\boxed{
U_f
=
(
ID_U,
FieldID,
Class_U,
Representation_U,
Parameters_U,
Dependence_U,
Source_U,
Propagation_U,
Validation_U,
Status_U
).
}
~~~

Required columns:

~~~text
uncertainty_id
field_id
uncertainty_class
source_or_cause
representation
parameters_or_bounds
unit
dependence_group
dependence_description
probability_semantics
propagation_method
sensitivity_method
validation_or_calibration
evidence_source
validity_domain
status
notes
~~~

## 2. Global uncertainty classes

| Class | Meaning | Typical representations | Probability permitted? |
|---|---|---|---|
| ALEATORY | irreducible/variability under declared model | distributions, empirical samples | yes, only if probability model justified |
| EPISTEMIC | knowledge/parameter/state uncertainty | intervals, distributions, sets, ensembles | conditional |
| MODEL_FORM | plausible structural/model alternatives | model ensemble, discrepancy term, scenario set | not automatically |
| NUMERICAL | discretization/solver/approximation error | convergence estimate, tolerance envelope | usually not as physical probability |
| MEASUREMENT | instrument/observation uncertainty | standard uncertainty, covariance, interval | as justified by measurement model |
| REQUIREMENT | uncertain/contested threshold/target | interval, scenarios, discrete alternatives | not automatically |
| PERFORMANCE | uncertain intervention consequence/effectiveness/resource result | distributions, intervals, ensembles | as justified |
| VALUE | preference/weight/value-model uncertainty | ranges, scenarios, distributions if elicited | only if justified |
| MIXED | multiple inseparable categories | explicit composite model | document components |
| NONE | deterministically fixed formal object | N/A | N/A |

## 3. Field expectations

| Field | Minimum uncertainty questions |
|---|---|
| \(\mathcal G\) | topology completeness? spatial accuracy? asset status/version? interface/crosswalk uncertainty? |
| \(Y_0\) | measurement vs estimate? synchronization? covariance/set/ensemble? missing state components? |
| \(\theta\) | source uncertainty? calibration/identifiability? correlation/dependence? model-form association? |
| \(\eta\) | intensity, location, timing, interpolation/grid, model/reanalysis uncertainty? |
| \(T\) | fixed design choice or uncertain requirement/response horizon? |
| \(K\) | threshold uncertainty? requirement authority? mapping from service to state? |
| \(G_{\rm rec}\) | recovery target/deadline uncertainty? |
| \(F_{\rm unsafe}\) | safety threshold/model uncertainty? |
| \(\mathcal U_{\rm feas}\) | resource availability, info latency, org response, action uncertainty? |
| \(\mathcal A\) | implementation, cost/resource, lifetime, performance/model uncertainty? |
| \(\Omega\) | domain boundaries, excluded regions, deep-uncertainty alternatives? |

## 4. Probability firewall

~~~math
\boxed{
\text{scenario frequency}
\neq
\text{probability}
}
~~~

unless a justified probability model exists.

A probability distribution requires:
- stated random quantity;
- population/process interpretation;
- source/estimation method;
- dependence assumptions;
- validation/adequacy evidence;
- validity domain.

## 5. Dependence firewall

Do not propagate marginal distributions independently when scientifically material dependence is known or plausible.

For grouped uncertain inputs:

~~~math
\boxed{
U_{joint}
\neq
\prod_i U_i
}
~~~

unless independence is justified.

## 6. Propagation

Allowed propagation approaches include:
- analytic propagation;
- Monte Carlo;
- ensemble propagation;
- interval/set propagation;
- scenario propagation;
- polynomial/surrogate methods after verification;
- sensitivity analysis.

Method choice must match uncertainty semantics. JCGM 101 may guide Monte Carlo propagation for measurement models, but it does not justify probability semantics for unrelated deep-uncertainty quantities.

## 7. Reduction versus propagation

~~~math
\boxed{
\text{uncertainty reduction}
\neq
\text{uncertainty propagation}.
}
~~~

Calibration, better observation or additional evidence may reduce epistemic uncertainty. Simulation propagates the remaining uncertainty; it does not automatically reduce it.

## 8. Pre-data state

All final numerical uncertainty models are DEFERRED unless independently qualified.

P1.5 freezes the record structure and admissibility requirements only.
