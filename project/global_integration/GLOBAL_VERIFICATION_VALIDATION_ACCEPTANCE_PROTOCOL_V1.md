# Global Verification / Validation / Acceptance Protocol v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.7 VALIDATION / CREDIBILITY CONTROL

## 1. Context of use first

No validation exercise is defined before a context of use.

~~~math
\boxed{
CoU
=
(
DecisionOrClaim,
QOI,
Domain,
Consequence,
ModelInfluence,
CredibilityTarget
).
}
~~~

This follows the intended-use orientation of NASA-STD-7009B and the risk-informed credibility logic of ASME V&V 40.

## 2. Verification questions

Code verification:
> Is the intended mathematical/algorithmic model implemented correctly?

Solution verification:
> How large are the numerical/algorithmic approximation errors for the target QOIs?

Data-pipeline verification:
> Were source data transformed, aligned and materialized correctly?

None answers:
> Is the model an adequate representation of the real system for this use?

That is validation.

## 3. Calibration protocol

Calibration is a parameter/model-identification activity, not validation.

Before calibration freeze:
- calibrated objects/parameters;
- calibration dataset;
- role of priors/constraints;
- objective/likelihood/loss;
- optimization/inference method;
- identifiability diagnostics;
- holdout policy;
- uncertainty representation.

Permanent:

~~~math
\boxed{
\text{fit quality}
\neq
\text{predictive validity}.
}
~~~

## 4. Validation plan

Every planned validation record contains:

~~~text
validation_id
context_of_use_id
model/object
QOI
validation_reference_id
reference_class
reference_uncertainty
model_output_uncertainty
metric
aggregation_rule
acceptance_rule
independence_status
validation_domain
data_split
freeze_version
status
claim_ceiling
~~~

## 5. Reference rule

Use the P1.4 classes.

Preferred claim-strength order when scientifically available:

~~~math
\boxed{
\text{independent empirical observation}
>
\text{qualified independent higher-fidelity reference}
>
\text{synthetic/analytic truth for controlled verification}.
}
~~~

This is not an assertion that every empirical dataset is accurate. Reference uncertainty and quality remain explicit.

## 6. Validation discrepancy

For QOI \(q\):

~~~math
\boxed{
e_q
=
d_q(
Q_q^{model},
Q_q^{ref}
).
}
~~~

The validation comparison must account for:
- reference uncertainty;
- model/input uncertainty;
- numerical uncertainty;
- temporal/spatial aggregation;
- observation operator if model and measurement spaces differ.

A pointwise state error is not automatically the correct validation metric for a service/cascade/recovery claim.

## 7. Acceptance rule

Acceptance must be prospectively frozen.

Generic form:

~~~math
\boxed{
A_{val}
=
\mathbf 1[
\mathcal M_{val}(e,U_{ref},U_{model},U_N)
\in
\mathcal C_{accept}
].
}
~~~

P1.7 does not invent \(\mathcal C_{accept}\).

The acceptance basis may come from:
- engineering significance;
- measurement/reference resolution;
- numerical accuracy;
- independent pilot/reference performance;
- regulatory/operator criteria where applicable.

It cannot be selected from the final confirmatory validation error.

## 8. Validation result taxonomy

~~~text
VALIDATED_FOR_DECLARED_USE
NOT_VALIDATED_FOR_DECLARED_USE
NOT_TESTED
~~~

NOT_TESTED applies when required evidence/metric/acceptance/reference is unavailable.

NOT_VALIDATED_FOR_DECLARED_USE requires a scientifically valid validation test that fails the frozen criterion.

## 9. Domain and extrapolation

Validation is local to its declared domain.

~~~math
\boxed{
Validated(M;CoU,\Omega_{val})
\not\Rightarrow
Validated(M;\Omega\supset\Omega_{val}).
}
~~~

Any extrapolation beyond validation conditions requires:
- explicit distance/domain argument;
- additional model-form/UQ treatment;
- reduced claim ceiling;
- or new validation evidence.

## 10. Validation hierarchy by thesis stage

### Stage 3
Validate subsystem/coupled physical outputs relevant to H1/QOIs.

### Stage 4
Validate observation/estimation behavior and uncertainty representation where independent truth/reference exists.

### Stage 5
Validate reduced-state projection and future-event information against independently evaluable outcomes/reference trajectories.

### Stage 6
Validate physical intervention/resource/accounting quantities and consequence models within declared boundaries.

### Stage 7
Stage 7 mostly verifies decision logic and inherits upstream validation; it validates empirical decision claims only insofar as required input/decision evidence exists.

## 11. Credibility target

The credibility target is not a universal scalar score.

It records what evidence is required for the context of use.

Example structure:

~~~text
code_verification_required = yes/no
solution_verification_required = yes/no
empirical_validation_level = L0-L4 thesis label
UQ_required = yes/no
decision_stability_required = yes/no
claim_ceiling_if_met
claim_ceiling_if_unmet
~~~

## 12. Risk-informed rigor

When model influence and consequence of incorrect use are high, the required credibility target should not be lower than for a low-consequence exploratory use.

P1.7 uses this as a qualitative rigor principle, not as a fabricated numerical model-risk score.

## 13. No self-validation

Prohibited:
- calibrate and validate on the same evidence without justified resampling/independence design;
- use a model-generated target as independent validation truth for the same model family;
- validate an algorithm solely by reproducing its own output;
- call benchmark reproduction real-system validation;
- select the validation metric/threshold after observing the target result.

## 14. Acceptance versus hypothesis

~~~math
\boxed{
\text{model accepted for use}
\neq
H_i\text{ supported}.
}
~~~

Credibility acceptance is a prerequisite for some hypothesis tests; it is not the hypothesis result itself.
