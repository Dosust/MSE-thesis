# Global Identification, Measurement-Error, and Estimator-Admission Protocol v1.1

**Status:** CANONICAL SUCCESSOR TO V1
**Effective date:** 2026-09-19
**Parent:** GLOBAL_IDENTIFICATION_MEASUREMENT_ERROR_AND_ESTIMATOR_ADMISSION_PROTOCOL_V1.md
**Correction authority:** CANONICAL_MEASUREMENT_IDENTIFICATION_GATE_SEMANTICS_AMENDMENT_V1_8_1.md

## 1. Identification has type, structural status, and strength status

~~~text
identification_type =
POINT
SET_PARTIAL
N_A_NONINFERENTIAL

identification_struct_status =
PASS
BLOCKED
FAIL
N/A

identification_strength_status =
PASS
BLOCKED
FAIL
N/A
~~~

Structural identification and finite-sample/information strength are independent.

## 2. Structural gate

~~~math
\boxed{
G_{\rm ID}^{struct}
=
PASS
}
~~~

means the point estimand or identified set is recoverable under the declared structural/measurement assumptions.

It does not state that finite-sample information is sufficiently strong.

## 3. Strength gate

~~~math
\boxed{
G_{\rm ID}^{strength}
}
~~~

records method-appropriate strength, such as weak-instrument/moment robustness where applicable.

A valid state is:

~~~math
\boxed{
G_{\rm ID}^{struct}=PASS,
\quad
G_{\rm ID}^{strength}=BLOCKED.
}
~~~

## 4. Partial/set identification

A data-derived interval/set does not bypass identification.

For partial identification:

~~~text
identification_type = SET_PARTIAL
~~~

and the identified-set conditions/provenance must be recorded.

N_A_NONINFERENTIAL is reserved for qualified quantities/bounds that do not depend on inferential recovery from the observations under analysis.

## 5. Estimator admission

~~~math
\boxed{
G_{\rm EST}^{admit}
=
G_{\rm estimand}
\land
G_{\rm assumptions}
\land
G_{\rm ID}^{struct}
\land
G_{\rm ID}^{strength}
\land
G_{\rm numerical-plan}
\land
G_{\rm uncertainty-plan}.
}
~~~

A justified N/A is accepted only for a factor that is genuinely not required by the method/intended claim.

Estimator admission is evaluated before estimator execution.

## 6. Result validation

After estimation/computation:

~~~math
\boxed{
G_{\rm VAL}^{result}
=
G_{\rm verification}
\land
G_{\rm empirical/model\ validation}
\land
G_{\rm domain}.
}
~~~

~~~math
\boxed{
G_{\rm EST}^{admit}
\neq
G_{\rm VAL}^{result}.
}
~~~

An estimator may be scientifically admissible while a particular estimated result remains unvalidated.

## 7. Cross-stage use

For an empirically inferred parameter:

~~~math
\boxed{
G_{\theta}^{pre}
=
G_{\rm origin}
\land
G_{\rm meas}
\land
G_{\rm ID}^{struct}
\land
G_{\rm ID}^{strength}
\land
G_{\rm EST}^{admit}.
}
~~~

Post-estimation readiness additionally requires estimator execution, uncertainty characterization, result validation and validity-domain compatibility.

## 8. Required register fields

~~~text
estimand_id
measurement_model_id
identification_type
identification_struct_status
identification_assumptions
identification_condition
identification_strength_method
identification_strength_status
estimator_id
estimator_admission_status
estimator_run_status
uncertainty_plan_id
uncertainty_result_id
result_verification_status
result_validation_status
result_validity_domain
claim_ceiling
provenance
~~~

## 9. Permanent ceiling

~~~math
\boxed{
\text{fitted value}
\neq
\text{identified quantity}
\neq
\text{validated result}
\neq
\text{causal mechanism}.
}
~~~
