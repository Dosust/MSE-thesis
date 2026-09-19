# P1.5 Final-Case Schema Audit v1 — 2026-09-19

**Status:** EXECUTED — PASS  
**Scope:** complete P1.5 pre-data case-contract package  
**Empirical effect:** NONE

## 1. Result

~~~math
\boxed{
G_{P1.5}^{design}=PASS
}
~~~

~~~text
58 PASS
0 FAIL
~~~

## 2. Audited artifacts

1. GLOBAL_FINAL_CASE_SCHEMA_V1.md
2. GLOBAL_FINAL_CASE_SCHEMA_V1.schema.json
3. GLOBAL_FINAL_CASE_FIELD_DICTIONARY_V1.md
4. GLOBAL_FINAL_CASE_SOURCE_PROVENANCE_TEMPLATE_V1.csv
5. GLOBAL_FINAL_CASE_ADMISSIBILITY_GATE_MATRIX_V1.md
6. GLOBAL_FINAL_CASE_REFERENCE_CLASS_MATRIX_V1.md
7. GLOBAL_FINAL_CASE_UNCERTAINTY_TEMPLATE_V1.md

## 3. Machine-structure checks

PASS:
- JSON Schema parses as valid JSON;
- Draft 2020-12 identifier present;
- exactly eleven core fields required;
- all eleven core field keys individually required;
- top-level additional properties prohibited;
- field statuses restricted to PASS/BLOCKED/FAIL/DEFERRED/N/A;
- case statuses restricted to declared qualification states;
- source classes distinguish CALIBRATED from SENSITIVITY_ONLY;
- P1.4 reference/validation classes machine-bound;
- global uncertainty classes machine-bound;
- status PASS requires a bound value;
- every core field requires provenance, UQ and admissibility records.

## 4. Core-field coverage

All required fields PASS schema coverage:

~~~text
graph
initial_state
parameters
hazard
dynamic_horizon
viability_set
recovery_target
unsafe_set
feasible_controls
interventions
validity_domain
~~~

## 5. Scientific-semantic checks

PASS:
- core case object and wrapped case package both defined;
- field-level metadata object frozen;
- entity→activity→entity provenance chain explicit;
- no silent unit conversion;
- spatial/temporal metadata explicit;
- sensor/location/observed-property/feature-of-interest/observation separated;
- generic uncertainty flag prohibited;
- measured data quality separated from required quality threshold;
- unnamed reference prohibited;
- SENSITIVITY_ONLY ≠ CALIBRATED ≠ VALIDATED;
- graph proximity cannot create causality;
- measured/estimated/assumed initial state separated;
- hazard is explicitly spatiotemporal;
- dynamic horizon separated from lifecycle horizon;
- research assumption separated from authoritative requirement;
- feasible-control intersection preserved;
- strategic intervention distinct from operational control;
- case domain separated from scenario sample;
- twelve-part field admissibility gate defined;
- case qualification state separated from hypothesis outcome;
- case claim ceiling bounded by required field ceilings.

## 6. Standards/version checks

PASS:
- ISO 19115-1:2014 correctly described as current published edition with replacement under development;
- ISO 19157-1:2023 used for data-quality architecture;
- OGC WKT-CRS and SensorThings semantics included;
- latest released CF version 1.13 reflected;
- BIPM SI 9th edition updated 2026 referenced;
- JCGM uncertainty guidance referenced;
- NASA-STD-7009B / NASA-HDBK-7009B credibility guidance referenced;
- JSON Schema Draft 2020-12 referenced.

## 7. Template/completeness checks

PASS:
- field dictionary contains all eleven case IDs;
- provenance CSV contains one header plus eleven initialized rows;
- admissibility applicability matrix defined;
- PASS/BLOCKED/FAIL/DEFERRED semantics explicit;
- reference matrix protects SYNTHETIC_TRUTH versus GROUND_TRUTH;
- calibration/validation independence rule explicit;
- uncertainty template preserves scenario-frequency/probability firewall;
- uncertainty dependence cannot be silently factorized;
- uncertainty reduction separated from propagation;
- no final case/scenario numerical value is invented;
- no H1–H5 support result is asserted.

## 8. Key scientific conclusions

### 8.1 P1.5 is a schema gate, not case selection

~~~math
\boxed{
G_{P1.5}^{design}=PASS
\not\Rightarrow
G_{case,exec}=PASS.
}
~~~

### 8.2 Case domain is not scenario sample

~~~math
\boxed{
\Omega_{case}
\neq
\{\omega_s\}_{s=1}^{N}.
}
~~~

P1.6 owns scenario identity/realization.

### 8.3 Presence is not qualification

~~~math
\boxed{
\text{present}
\not\Rightarrow
\text{qualified}
\not\Rightarrow
\text{validated}.
}
~~~

### 8.4 Claim ceilings propagate

~~~math
\boxed{
\Lambda_{case}
\le
\min_{f\in F_{required}}\Lambda_f.
}
~~~

## 9. Protected DEFERRED state

The audit confirms that P1.5 does not bind:
- location/city;
- feeder/road IDs;
- crosswalks;
- hazard event/intensity;
- initial state values;
- parameter values/distributions;
- thresholds;
- controls;
- interventions;
- scenario IDs/probabilities;
- any H1–H5 result.

## 10. Closure

~~~math
\boxed{
P1.5=PASS.
}
~~~

Next:

~~~math
\boxed{
P1.6=\text{GLOBAL SCENARIO ID AND PROPAGATION SCHEMA}.
}
~~~
