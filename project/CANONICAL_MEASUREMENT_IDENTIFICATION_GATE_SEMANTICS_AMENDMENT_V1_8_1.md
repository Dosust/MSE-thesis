# Canonical Measurement / Identification Gate-Semantics Amendment v1.8.1

**Status:** NARROW CANONICAL CORRECTION TO P1.11.8
**Effective date:** 2026-09-19
**Parent:** CANONICAL_MEASUREMENT_ERROR_IDENTIFICATION_AMENDMENT_V1_8.md
**Scope:** gate semantics only
**Seven-stage architecture / RQ / SO / H:** UNCHANGED
**P–T mechanism set:** UNCHANGED
**Sustainability authority:** UNCHANGED
**Empirical effect:** NONE

## 1. Purpose

This amendment closes four logical inconsistencies without reopening the scientific content of P1.11.8:

1. estimator admission versus post-estimation result validation;
2. structural identification versus identification strength;
3. point versus set/partial identification and the proper meaning of N/A;
4. repository/source/case evidence status as three independent axes.

It also types Monte Carlo method testing separately from uncertainty propagation.

## 2. Estimator admission is not result validation

The pre-estimation gate is:

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

For factors that are genuinely not applicable, a justified N/A satisfies the corresponding requiredness rule.

After estimation/computation, the result-level credibility gate is:

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

Permanent:

~~~math
\boxed{
\text{admissible estimator}
\neq
\text{validated estimated result}.
}
~~~

The parent P1.11.8 expression in which estimator admission contained validation is superseded by this section.

## 3. Structural identification is not identification strength

Define:

~~~math
\boxed{
G_{\rm ID}^{struct}
=
\text{whether the estimand or identified set is recoverable under the declared model and measurement assumptions}.
}
~~~

Define separately:

~~~math
\boxed{
G_{\rm ID}^{strength}
=
\text{whether the available information is strong enough for the intended finite-sample claim}.
}
~~~

Therefore the following state is valid:

~~~math
\boxed{
G_{\rm ID}^{struct}=PASS,
\qquad
G_{\rm ID}^{strength}=BLOCKED.
}
~~~

Permanent:

~~~math
\boxed{
\text{structural identification}
\neq
\text{identification strength}.
}
~~~

The source's weak-moment/weak-instrument warning is interpreted on the strength axis, not by redefining structural identification.

## 4. Identification type

Every inferential estimand records:

~~~text
identification_type =
POINT
SET_PARTIAL
N_A_NONINFERENTIAL
~~~

with an independent structural status:

~~~text
identification_struct_status =
PASS
BLOCKED
FAIL
N/A
~~~

### POINT

The parameter/estimand is point identified under the declared assumptions.

### SET_PARTIAL

The identified set is characterized under the declared assumptions, but the estimand is not point identified.

~~~math
\boxed{
\text{no point estimate}
\not\Rightarrow
\text{no identification problem}.
}
~~~

A data-derived interval/set may therefore require:

~~~text
identification_type = SET_PARTIAL
identification_struct_status = PASS/BLOCKED/FAIL
~~~

depending on whether that set is identified.

### N_A_NONINFERENTIAL

N/A is allowed only where the quantity/bound is supplied through a non-inferential qualified route, such as:
- authoritative specification;
- externally qualified engineering bound;
- controlled/synthetic truth;
- declared nonprobabilistic scenario bound;
- another independent source not estimated from the observations under analysis.

An interval/set inferred from observational data is not N/A merely because no point estimate is reported.

## 5. Normalized identification status object

For inferential quantity \(\vartheta\):

~~~math
\boxed{
\mathfrak I\!D_\vartheta
=
(
Type_\vartheta,
G_{{\rm ID},\vartheta}^{struct},
G_{{\rm ID},\vartheta}^{strength},
A_\vartheta,
C_\vartheta,
V_\vartheta,
P_\vartheta
).
}
~~~

Where:
- Type is POINT / SET_PARTIAL / N_A_NONINFERENTIAL;
- structural gate records identification existence/type;
- strength gate records finite-sample/information strength where applicable;
- A records assumptions;
- C records rank/exclusion/variation or method-specific conditions;
- V records validity domain;
- P records provenance.

## 6. Stage-3 parameter semantics

For empirically inferred Stage-3 parameter \(\theta_e\), estimator admission is a prerequisite to estimation, while result validation is downstream.

Pre-estimation:

~~~math
\boxed{
G_{\theta,e}^{pre}
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

Post-estimation readiness for intended Stage-3 use additionally requires:

~~~math
\boxed{
G_{\theta,e}^{ready}
=
G_{\theta,e}^{pre}
\land
G_{\rm EST-run}
\land
G_{\mathcal U}
\land
G_{\rm VAL}^{result}
\land
G_{\rm domain}.
}
~~~

This preserves the parent Stage2→3 rule that an empirically estimated parameter cannot be considered ready merely because an optimizer returned a value.

## 7. Three-axis evidence status

Every source-integration claim item now records:

~~~math
\boxed{
STATUS_i
=
(
REPO_i,
SOURCE_i,
CASE_i
).
}
~~~

These axes are independent.

### REPO

~~~text
PASS
BLOCKED
FAIL
DEFERRED
N/A
~~~

### SOURCE

~~~text
DIRECT
CONCEPTUAL
METHOD_PRECEDENT
THESIS_DERIVED_COMPATIBLE
THESIS_AUTHORITY_CONSISTENT
OTHER_QUALIFIED_SOURCE
NONE
BLOCKED
~~~

CASE_VALIDATED is removed from SOURCE because validation is not a source-support class.

### CASE

~~~text
VALIDATED
PARTIALLY_VALIDATED
NOT_TESTED
BLOCKED
FAIL
N/A
~~~

Example:

~~~text
REPO   = PASS
SOURCE = METHOD_PRECEDENT
CASE   = NOT_TESTED
~~~

Permanent:

~~~math
\boxed{
REPO
\neq
SOURCE
\neq
CASE.
}
~~~

## 8. Monte Carlo computation classes

Two different computational roles are now explicit.

### MONTE_CARLO_METHOD_TEST

~~~math
\boxed{
\text{known/controlled DGP}
\rightarrow
\text{bias, variance, coverage, finite-sample method behavior}.
}
~~~

Claim ceiling:
- method behavior under the declared DGP/design;
- no empirical infrastructure validation.

### UNCERTAINTY_PROPAGATION

~~~math
\boxed{
\mathbb U_{\rm inputs}
\rightarrow
\mathbb U_{\rm outputs}.
}
~~~

Claim ceiling:
- propagated output uncertainty under qualified input uncertainty, dependence assumptions and model validity;
- no new causal evidence;
- no case validation by propagation alone.

Permanent:

~~~math
\boxed{
\text{Monte Carlo method test}
\neq
\text{uncertainty propagation}
\neq
\text{case validation}.
}
~~~

## 9. Current sustainability authority unchanged

This amendment does not modify:

~~~math
\boxed{
\mathbf r_{\rm core}
\subseteq
(C_{\rm direct},E_{\rm op})
}
~~~

or:

~~~math
\boxed{
\mathbf J_{\rm sus,core}
\subseteq
(CO_{2e})
}
~~~

with distributional accessibility conditional.

## 10. P2 normalized fields

P2 shall use at least:

~~~text
IDENTIFICATION_TYPE
IDENTIFICATION_STRUCT_STATUS
IDENTIFICATION_STRENGTH_METHOD
IDENTIFICATION_STRENGTH_STATUS
ESTIMATOR_ADMISSION_STATUS
ESTIMATOR_RUN_STATUS
RESULT_VERIFICATION_STATUS
RESULT_VALIDATION_STATUS
RESULT_VALIDITY_DOMAIN
REPOSITORY_STATUS
SOURCE_SUPPORT_STATUS
CASE_VALIDATION_STATUS
MONTE_CARLO_CLASS
~~~

These extend rather than duplicate P1.11.7/P1.11.8 computation fields.

## 11. Final chain

~~~math
\boxed{
\text{REPRESENT}
\rightarrow
\text{QUALIFY CAUSALITY}
\rightarrow
\text{IDENTIFY}
\rightarrow
\text{ADMIT ESTIMATOR}
\rightarrow
\text{ESTIMATE/SIMULATE}
\rightarrow
\text{VALIDATE}
\rightarrow
\text{RESILIENCE}
\rightarrow
\text{CONSEQUENCES}
\rightarrow
\text{DECISION}.
}
~~~

Identification and uncertainty remain transversal and may recur whenever a downstream quantity is inferred from imperfect observations.

## 12. Empirical firewall

~~~math
\boxed{
G_{P1.11.8.1}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~
