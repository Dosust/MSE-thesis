# Global Computational Role and Output-Claim Protocol v1

**Status:** CANONICAL P1.11.7 COMPUTATION GOVERNANCE
**Effective date:** 2026-09-19
**Purpose:** make every thesis computation traceable to a scientific object, transformation, output and claim ceiling.

## 1. Computation record

Every material computational operation shall register:

~~~text
computation_id
stage
lane
scientific_question
input_object_ids
input_object_classes
input_provenance
transformation_id
algorithm_or_equation
implementation_version
spatial_support_in
spatial_support_out
temporal_support_in
temporal_support_out
reference_state_id
normalization_id
uncertainty_ids
verification_status
validation_status
source_support_class
output_object_ids
output_object_classes
diagnostic_or_primary
allowed_claim
prohibited_inference
claim_ceiling
validity_domain
provenance
gate_status
~~~

## 2. Lane vocabulary

~~~text
MECHANISTIC
OBSERVATIONAL
DECISION
~~~

A workflow may cross lanes, but each transformation has one primary role and explicit handoff.

## 3. Role discipline

~~~math
\boxed{
\text{algorithm name}
\neq
\text{scientific role}.
}
~~~

For example, optimization may be used for:
- state estimation;
- trajectory control;
- intervention design;
- decision comparison.

The scientific role is determined by input/output semantics, not software family.

## 4. Feature-engineering gate

~~~math
G_{\rm feat}
=
G_{\rm definition}
\land
G_{\rm support}
\land
G_{\rm reference}
\land
G_{\rm units}
\land
G_{\rm leakage}
\land
G_U
\land
G_{\rm provenance}.
~~~

A derived feature is BLOCKED from confirmatory use when any required factor is unresolved.

## 5. Diagnostic-learning gate

For PCA/clustering/ML diagnostics:

~~~math
G_{\rm diag}
=
G_{\rm feat}
\land
G_{\rm verification}
\land
G_{\rm validation}
\land
G_{\rm stability}
\land
G_{\rm interpretation}.
~~~

Stability may include sensitivity to scaling, feature selection, hyperparameters, sample support and missing-data treatment as applicable.

## 6. Reference-state governance

A computational contrast must declare the reference object before confirmatory outcome inspection when the reference affects the test.

~~~math
\boxed{
\text{reference}
\neq
\text{requirement}
\neq
\text{preference}.
}
~~~

## 7. Claim ceilings by computation class

~~~text
SPATIAL_JOIN      -> representation/alignment only
FEATURE_ENGINEER  -> derived observational quantity
PCA               -> statistical dimension reduction/variance structure
CLUSTERING        -> descriptive archetype/pattern within feature space
PREDICTIVE_ML     -> predictive performance within validation domain
STATE_ESTIMATOR   -> estimated state/QOI with uncertainty
PHYSICS_SIM       -> model-implied dynamics within model/validation domain
INTERVENTION_SIM  -> model-implied intervention contrast under matched design
DECISION_ANALYSIS -> comparison under explicit objectives/constraints/preferences
VISUALIZATION     -> communication/diagnosis; no additional evidentiary status
~~~

## 8. Permanent prohibitions

~~~math
\boxed{
\begin{aligned}
\text{correlation/ML importance}&\not\Rightarrow\text{causality},\\
\text{cluster}&\not\Rightarrow\text{dynamical regime},\\
\text{index}&\not\Rightarrow\text{physical state},\\
\text{visualization}&\not\Rightarrow\text{validation},\\
\text{computation volume}&\not\Rightarrow\text{credibility}.
\end{aligned}
}
~~~

## 9. P2 integration

P2 shall normalize all computational objects using this protocol rather than storing simulation, ML or optimization as untyped generic activities.
