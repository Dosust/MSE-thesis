# Stage 4 Measurement, Identification, and Estimation Amendment v1.4

**Status:** CANONICAL ADDITIVE STAGE-4 INFERENCE AMENDMENT
**Effective date:** 2026-09-19
**Parents:** STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md; STAGE4_FEATURE_ENGINEERING_AND_REFERENCE_STATE_AMENDMENT_V1_3.md
**Cross-stage authority:** P1.11.8
**H2 status:** NOT TESTED

## 1. Measurement model remains primary

~~~math
\boxed{
y_k
=
\Gamma_k h^{m_k}(Y_k^{phys};\theta_H)
+
\nu_k.
}
~~~

Every estimator consumes a declared measurement model or an explicitly documented empirical observation model.

## 2. Identification precedes estimator selection

For unknown \(\vartheta\) inferred from \(\mathcal I_t\):

~~~math
\boxed{
\mathcal M_{\rm sci}
\rightarrow
\mathcal M_{\rm meas}
\rightarrow
G_{\rm ID}(\vartheta)
\rightarrow
G_{\rm EST}
\rightarrow
\widehat\vartheta
\rightarrow
\mathbb U_{\widehat\vartheta}.
}
~~~

This is an inference pipeline, not a new thesis stage.

## 3. Identification record

Every material empirically inferred parameter/state/QOI records:

~~~text
estimand_id
scientific_model_id
measurement_model_id
observed_variables
latent_variables
identification_assumptions
identification_method
rank_or_variation_condition
identification_strength_method
identification_strength_result
identification_status
falsifier_or_failure_condition
validity_domain
provenance
~~~

## 4. Estimator record

~~~text
estimator_id
estimand_id
estimator_family
required_assumptions
identification_link
data_support
regularization_or_prior
numerical_method
convergence_status
uncertainty_representation
verification
validation
weak_identification_robustness
claim_ceiling
~~~

## 5. Distinctions

~~~math
\boxed{
\text{observability}
\neq
\text{identifiability}
\neq
\text{estimability in finite data}
\neq
\text{numerical convergence}.
}
~~~

Observability addresses state reconstruction under a dynamic/measurement model. Identification addresses uniqueness/recoverability of the unknown scientific quantity under the declared statistical/model assumptions.

## 6. Method selection

Regression, IV/2SLS, GMM, Bayesian inference, filtering and ML remain candidates. No family is preferred generically.

~~~math
\boxed{
\text{estimator family}
=
f(
\text{scientific model},
\text{measurement model},
\text{identification assumptions},
\text{data},
\text{intended claim}
).
}
~~~

## 7. Cross-system coefficient firewall

~~~math
\boxed{
\widehat\beta_{P\to T}\neq0
\not\Rightarrow
P\to T.
}
~~~

No Stage-4 statistical estimate can promote a Stage-2 BLOCKED causal dependency.

## 8. H2 compatibility

Any estimated/learned information object used in H2 must preserve measurement-model provenance, identification status when inferential, estimator-admission status, uncertainty, held-out/prospective validation where required, no leakage, and claim ceiling.

A better prediction does not imply physically causal coupling.
