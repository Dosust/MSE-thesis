# Global Computational Role and Output-Claim Protocol v1.1

**Status:** CANONICAL SUCCESSOR TO V1
**Effective date:** 2026-09-19
**Parent:** GLOBAL_COMPUTATIONAL_ROLE_AND_OUTPUT_CLAIM_PROTOCOL_V1.md
**Correction authority:** P1.11.8.1

All v1 computation-role semantics remain in force except where refined below.

## 1. Additional computation classes

The claim-ceiling table is extended by:

~~~text
MONTE_CARLO_METHOD_TEST
UNCERTAINTY_PROPAGATION
~~~

### MONTE_CARLO_METHOD_TEST

Scientific role:

~~~math
\boxed{
\text{controlled/known DGP}
\rightarrow
\text{sampling behavior of a method}.
}
~~~

Allowed claims may include, within the declared DGP/design:
- bias;
- variance;
- coverage;
- finite-sample estimator behavior;
- method sensitivity.

Prohibited inference:
- empirical P–T validation;
- new causal mechanism evidence;
- real-case parameter truth without independent validation.

### UNCERTAINTY_PROPAGATION

Scientific role:

~~~math
\boxed{
\mathbb U_{\rm input}
\rightarrow
\mathbb U_{\rm output}.
}
~~~

Allowed claims:
- propagated uncertainty conditional on the declared input uncertainty, dependence assumptions, model and validity domain.

Prohibited inference:
- uncertainty propagation as evidence that the model is empirically valid;
- propagation as new causal evidence.

## 2. Monte Carlo firewall

~~~math
\boxed{
\text{MONTE_CARLO_METHOD_TEST}
\neq
\text{UNCERTAINTY_PROPAGATION}
\neq
\text{CASE_VALIDATION}.
}
~~~

The same Monte Carlo engine may implement both classes in different tasks; the scientific role must be recorded per computation.

## 3. Computation-record extension

Add:

~~~text
monte_carlo_class
dgp_status
identification_type
identification_struct_status
identification_strength_status
estimator_admission_status
result_validation_status
case_validation_status
~~~

where applicable.

## 4. Updated claim-ceiling summary

~~~text
SPATIAL_JOIN             -> representation/alignment only
FEATURE_ENGINEER         -> derived observational quantity
PCA                      -> statistical dimension reduction/variance structure
CLUSTERING               -> descriptive archetype/pattern within feature space
PREDICTIVE_ML            -> predictive performance within validation domain
STATE_ESTIMATOR          -> estimated state/QOI with uncertainty
PHYSICS_SIM              -> model-implied dynamics within model/validation domain
INTERVENTION_SIM         -> model-implied intervention contrast under matched design
MONTE_CARLO_METHOD_TEST  -> method behavior under declared controlled DGP
UNCERTAINTY_PROPAGATION  -> propagated output uncertainty under qualified input uncertainty/model
DECISION_ANALYSIS        -> comparison under explicit objectives/constraints/preferences
VISUALIZATION            -> communication/diagnosis; no additional evidentiary status
~~~
