# Stage 4 Feature Engineering, Analysis Support, and Reference-State Amendment v1.3

**Status:** CANONICAL ADDITIVE STAGE-4 AMENDMENT
**Effective date:** 2026-09-19
**Parent:** STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md
**Cross-stage authority:** P1.11.7
**H2 status:** NOT TESTED

## 1. Dataset, observation, feature and estimate are distinct

~~~math
\boxed{
\mathcal D_{\rm raw}
\neq
y
\neq
Z^{obs}
\neq
\widehat Y
\neq
b_t.
}
~~~

\(\mathcal D_{\rm raw}\) denotes data collections/files/tables/streams.

The existing \(D_i\) demand/use notation is not reused for raw data.

## 2. Extended Stage-4 observational pipeline

~~~math
\boxed{
\mathcal D_{\rm raw}
\rightarrow
\mathcal M^{align}
\rightarrow
\Phi_{\rm feat}
\rightarrow
Z^{obs}
\rightarrow
\mathcal E
\rightarrow
(b_t,\widehat Y,\widehat q).
}
~~~

The pipeline may omit a step only with a declared reason.

## 3. Analysis support

Every derived feature records:

~~~text
native_support
target_analysis_support
crosswalk/alignment method
coverage
aggregation rule
uncertainty
resolution loss
validity domain
~~~

No proximity or aggregation operation establishes a Stage-2 dependency.

## 4. Reference-state features

If a feature is defined relative to normal/pre-event behavior:

~~~math
Z_i^{obs}(t)
=
\phi_i
\left(
y_i(t),
R_i^{ref}
\right).
~~~

The reference object records:
- source;
- period;
- sampling rule;
- seasonality/time-of-day treatment;
- scenario;
- uncertainty;
- validity.

## 5. Feature-role register

Every feature receives a role:

~~~text
OBSERVATION_TRANSFORM
PERFORMANCE_QOI
ESTIMATOR_INPUT
DIAGNOSTIC
CONTROL_INPUT
CONTEXT
~~~

A feature cannot silently migrate between roles.

## 6. Statistical-learning firewall

Feature importance, PCA loadings, embeddings and cluster labels are statistical products.

They do not create:
- causal dependencies;
- physical parameters;
- control authority;
- requirements;
- resilience guarantees.

## 7. H2 compatibility

Cross-system features may enter an H2 information ablation only when:
- feature definitions are preregistered;
- no future leakage exists;
- spatial/temporal support is aligned;
- target-only comparator is retained;
- uncertainty/validation is reported.

## 8. Stage-4 handoff extension

Where observational diagnostics are needed downstream, Stage 4 may hand off:

~~~text
feature_id
definition
support
reference_id
value/distribution
uncertainty
validation
provenance
allowed downstream role
claim ceiling
~~~

This is additive to the existing Stage4→5 contract and does not replace \(b_t\) or physical-truth lineage.
