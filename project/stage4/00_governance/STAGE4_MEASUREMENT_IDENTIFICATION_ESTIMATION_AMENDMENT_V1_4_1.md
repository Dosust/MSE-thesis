# Stage 4 Measurement, Identification, and Estimation Amendment v1.4.1

**Status:** NARROW CORRECTION TO V1.4
**Effective date:** 2026-09-19
**Parent:** STAGE4_MEASUREMENT_IDENTIFICATION_ESTIMATION_AMENDMENT_V1_4.md
**Cross-stage authority:** P1.11.8.1
**H2 status:** NOT TESTED

## 1. Correct inference sequence

~~~math
\boxed{
\mathcal M_{\rm sci}
\rightarrow
\mathcal M_{\rm meas}
\rightarrow
G_{\rm ID}^{struct}
\rightarrow
G_{\rm ID}^{strength}
\rightarrow
G_{\rm EST}^{admit}
\rightarrow
\widehat\vartheta
\rightarrow
\mathbb U_{\widehat\vartheta}
\rightarrow
G_{\rm VAL}^{result}.
}
~~~

## 2. Identification record extension

Every inferential object records:

~~~text
identification_type
identification_struct_status
identification_strength_method
identification_strength_status
~~~

in addition to the v1.4 fields.

## 3. Estimator record correction

Replace generic estimator-admission dependence on post-result validation with:

~~~text
estimator_admission_status
estimator_run_status
result_verification_status
result_validation_status
result_validity_domain
~~~

These are independent fields.

## 4. Permanent distinctions

~~~math
\boxed{
\text{observability}
\neq
\text{structural identification}
\neq
\text{identification strength}
\neq
\text{estimator admission}
\neq
\text{result validation}.
}
~~~

## 5. Partial identification

An observationally inferred interval/set retains identification obligations:

~~~math
\boxed{
\text{set-valued estimate}
\not\Rightarrow
G_{\rm ID}=N/A.
}
~~~

Use SET_PARTIAL where appropriate.

## 6. H2 protection

Prediction/estimation improvements remain bounded by their inferential and validation status and cannot promote blocked physical causal dependencies.
