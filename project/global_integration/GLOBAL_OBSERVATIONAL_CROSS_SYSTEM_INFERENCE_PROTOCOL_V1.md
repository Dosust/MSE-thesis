# Global Observational Interdependency / Cross-System Inference Protocol v1

**Status:** CANONICAL CROSS-STAGE INFORMATION CONTROL  
**Effective date:** 2026-09-19  
**Owner:** P1.11.4 / Stage 4  
**Empirical effect:** NONE

## 1. Relation classes

Every cross-system relation used for data analysis must be typed as one of:

~~~text
PHYSICAL_CAUSAL_DEPENDENCY
CAUSAL_INFORMATION_DEPENDENCY
OBSERVATIONAL_PREDICTIVE_RELATION
SHARED_DRIVER_ASSOCIATION
GEOGRAPHIC_COEXPOSURE
POLICY_ECONOMIC_CHANNEL
UNRESOLVED
~~~

The type determines the admissible claim class and gate.

## 2. Claim mapping

~~~text
OBSERVATIONAL_PREDICTIVE_RELATION
  -> PREDICTIVE_OR_EXPLANATORY claim only unless causal identification exists

SHARED_DRIVER_ASSOCIATION
  -> ASSOCIATION / EXPLANATORY-HYPOTHESIS claim only

PHYSICAL_CAUSAL_DEPENDENCY
  -> MECHANISM / CAUSAL_EFFECT only after Stage-2 and relevant causal gates

CAUSAL_INFORMATION_DEPENDENCY
  -> information-system mechanism only after causal qualification
~~~

## 3. Forecasting record

Required fields:

~~~text
obs_relation_id
source_domain
source_variable
source_observation_id
source_unit
source_spatial_support
source_temporal_support
target_domain
target_quantity
target_unit
target_spatial_support
target_temporal_support
alignment_id
observational_lag
candidate_shared_drivers
feature_set
estimator_id
training_window
validation_window
test_window
baseline_model
metric_ids
uncertainty_ids
leakage_check
mode_scope
regime_scope
data_version
model_code_version
validity_domain
claim_ceiling
publication_evidence_status
provenance
gate_status
~~~

## 4. Leakage firewall

Prohibited:
- using future target observations unavailable at forecast time;
- estimating lag on protected confirmatory test outcomes and reusing it as fixed;
- using post-event labels unavailable to the operational estimator;
- spatial aggregation that uses target information unavailable at inference time;
- reporting training fit as predictive validity.

## 5. Baseline requirement

Cross-system information value must be evaluated against a target-only or otherwise scientifically justified baseline under matched evaluation data.

~~~math
\boxed{
\Delta E_{info}
=
E_{baseline}
-
E_{xsys}
}
~~~

with metric direction defined prospectively.

## 6. Regime-shift claims

Claims that cross-system information is especially useful during abnormal regimes require explicit regime definition and protected evaluation across one or more relevant events/scenarios.

One historical episode is preliminary evidence, not universal proof.

## 7. Spatial/mode validity

No result may be generalized beyond:
- represented geography;
- represented time period;
- transportation mode;
- population/aggregation level;
- data resolution;
- observed regime;
without separate evidence.

## 8. Downstream resilience trace

To claim resilience benefit from information:

~~~math
\boxed{
\mathfrak o^{obs}
\rightarrow
\Delta b/\Delta\widehat q
\rightarrow
\Delta u
\rightarrow
\Delta Q
\rightarrow
\Delta\mathfrak R.
}
~~~

Every arrow needs an admissible model/test.

## 9. Evidence hierarchy

Publication/evidence status must be retained:

~~~text
PEER_REVIEWED
PREPRINT
TECHNICAL_REPORT
OPERATOR_DATA
CASE_OBSERVATION
SYNTHETIC
OTHER
~~~

Publication status affects evidence interpretation but does not by itself determine truth.
