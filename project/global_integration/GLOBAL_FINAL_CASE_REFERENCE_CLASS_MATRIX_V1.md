# Global Final-Case Reference-Class Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.5 ↔ P1.4 BINDING

## 1. Rule

Every bound source/reference role must use an explicit P1.4 class.

~~~math
\boxed{
\text{unnamed reference}=\text{NOT ADMISSIBLE}.
}
~~~

## 2. Field matrix

| Field | Normally admissible classes | Conditional classes | Prohibited/misuse examples |
|---|---|---|---|
| \(\mathcal G\) | VALIDATION_EVIDENCE; VALIDATION_REFERENCE; EVIDENCE_SOURCE_REFERENCE; QUALIFIED_CASE | GROUND_TRUTH only for specifically verified geometry/topology quantities | synthetic topology labeled empirical ground truth; proximity labeled causal evidence |
| \(Y_0\) | VALIDATION_EVIDENCE; VALIDATION_REFERENCE; QUALIFIED_CASE | AUXILIARY_COUNTERFACTUAL_MODEL for reconstructed components; GROUND_TRUTH only when defensible | estimated state labeled directly measured truth |
| \(\theta\) | EVIDENCE_SOURCE_REFERENCE; VALIDATION_EVIDENCE; VALIDATION_REFERENCE | EXTERNAL_PRACTICE_FACTOR_REFERENCE; REFERENCE_SOLUTION for mathematical/numerical parameter verification | literature/default value labeled calibrated; sensitivity value labeled validated |
| \(\eta\) | VALIDATION_EVIDENCE; VALIDATION_REFERENCE; EVIDENCE_SOURCE_REFERENCE | SYNTHETIC_TRUTH for constructed benchmarks; GROUND_TRUTH only where physical hazard field is known at required resolution | synthetic hazard labeled observed event |
| \(T\) | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE; NONE | VALIDATION_EVIDENCE when empirical recovery/time evidence informs horizon | arbitrary simulation duration labeled regulatory threshold |
| \(K\) | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE | VALIDATION_EVIDENCE when requirement mapping derives from empirical service evidence | research assumption promoted to regulation/standard |
| \(G_{\rm rec}\) | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE | VALIDATION_EVIDENCE for empirically justified recovery target | benchmark threshold labeled stakeholder requirement |
| \(F_{\rm unsafe}\) | REQUIREMENT_THRESHOLD; EVIDENCE_SOURCE_REFERENCE | VALIDATION_EVIDENCE if empirical safety evidence defines a boundary | arbitrary numerical failure cutoff labeled authoritative |
| \(\mathcal U_{\rm feas}\) | VALIDATION_EVIDENCE; EVIDENCE_SOURCE_REFERENCE; REQUIREMENT_THRESHOLD | EXTERNAL_PRACTICE_FACTOR_REFERENCE for resource/action limits | physical upper bound treated as organizational availability |
| \(\mathcal A\) | EVIDENCE_SOURCE_REFERENCE; EXTERNAL_PRACTICE_FACTOR_REFERENCE; VALIDATION_EVIDENCE; QUALIFIED_CASE | REFERENCE_CALCULATION for implementation/accounting verification | hypothetical intervention labeled current practice; fixture labeled field validation |
| \(\Omega\) | EVIDENCE_SOURCE_REFERENCE; REQUIREMENT_THRESHOLD; NONE | VALIDATION_EVIDENCE when domain limits are empirical | scenario frequency labeled probability; sampled scenarios treated as full domain |

## 3. Truth hierarchy

~~~math
\boxed{
\text{SYNTHETIC_TRUTH}
\neq
\text{GROUND_TRUTH}.
}
~~~

~~~math
\boxed{
\text{HIGHER_FIDELITY_MODEL}
\not\Rightarrow
\text{GROUND_TRUTH}.
}
~~~

~~~math
\boxed{
\text{VALIDATION_REFERENCE}
\not\Rightarrow
\text{exact truth}.
}
~~~

Validation references retain uncertainty and intended-use scope.

## 4. Role/independence rule

A single dataset/source may serve multiple roles only if role compatibility is explicitly justified.

Where confirmatory validation requires independence:

~~~math
\boxed{
D_{cal}\cap D_{val}=\varnothing.
}
~~~

A dataset used to choose the treatment structure, tune treatment-specific parameters, or select a materiality threshold cannot silently be relabeled held-out validation evidence.

## 5. Claim ceiling

The P1.4 class constrains \(\Lambda_f\). A stronger label requires stronger evidence and a versioned provenance change.
