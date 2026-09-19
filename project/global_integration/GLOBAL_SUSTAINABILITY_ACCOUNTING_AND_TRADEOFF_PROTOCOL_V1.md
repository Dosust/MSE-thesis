# Global Sustainability Accounting and Trade-off Protocol v1

**Status:** CANONICAL CROSS-STAGE SUSTAINABILITY CONTROL  
**Effective date:** 2026-09-19  
**Owner:** P1.11.5 / Stage 6–7  
**Empirical effect:** NONE

## 1. Sustainability record

Every material sustainability consequence has:

~~~text
sustainability_id
component
role_class
source_stage
intervention_id
scenario_id
quantity
native_unit
direction_of_preference
spatial_domain
temporal_horizon
systems_included
processes_included
functional_unit
perspective
local_rate_definition
aggregation_rule
embodied_term
lifecycle_stage
data_sources
factor_sources
uncertainty_ids
accounting_state_id
requirement_role
requirement_id
hardness
double_counting_check
burden_shifting_check
baseline_result
intervention_result
delta_result
validity_domain
claim_ceiling
provenance
gate_status
~~~

## 2. Role classes

~~~text
HAZARD_CONTEXT
PHYSICAL_STATE
SERVICE
PERFORMANCE_QOI
SUSTAINABILITY_CONSEQUENCE
RESOURCE_INPUT
HARD_REQUIREMENT
SOFT_TARGET
DECISION_OBJECTIVE
PREFERENCE
ACCOUNTING_STATE
~~~

An item may have multiple registered roles only if each role has separate semantics.

## 3. Accounting gate

~~~math
\boxed{
G_{\rm sus}
=
G_{\rm definition}
\land
G_{\rm boundary}
\land
G_{\rm units}
\land
G_{\rm inventory/data}
\land
G_{\rm aggregation}
\land
G_U
\land
G_{\rm doublecount}
\land
G_{\rm burden}
\land
G_{\rm provenance}.
}
~~~

## 4. Hard-constraint gate

~~~math
\boxed{
G_{\rm hard-sus}
=
G_{\rm sus}
\land
G_{\rm RID}
\land
G_{\rm authority}
\land
G_{\rm threshold}
\land
G_{\rm applicability}
\land
G_{\rm effectivity}.
}
~~~

Without \(G_{\rm hard-sus}=PASS\), the quantity cannot enter \(K(t)\) as a hard sustainability constraint.

## 5. Trade-off analysis

Default:
- retain native units;
- compare signed deltas and uncertainty;
- identify nondominated sets;
- report trade-off surfaces/regions;
- perform sensitivity to scenario/accounting assumptions.

Do not infer a tipping threshold from a conceptual figure.

## 6. Burden shifting

Check at minimum:
- P versus T sector transfer;
- operational versus embodied/lifecycle transfer;
- geographic transfer;
- temporal transfer;
- stakeholder/population transfer where relevant;
- environmental-category transfer when extended environmental assessment is claimed.

## 7. Double counting

The same underlying activity cannot be counted twice within the same endpoint.

If a quantity legitimately contributes to two scientific objects (for example cost consequence and efficiency resource denominator), those result objects remain separate and must not be scalar-summed without an explicit value/accounting model.

## 8. Transformation

For transformed architectures, sustainability results are versioned by:

~~~text
architecture_version
technology_version
dependency_version
scenario_version
accounting_boundary_version
factor_version
~~~

so that long-term comparisons remain reproducible.

## 9. Claim wording

Allowed wording depends on:
- component coverage;
- accounting boundary;
- uncertainty;
- lifecycle coverage;
- comparator;
- requirement status.

A partial vector cannot support an unqualified statement that an intervention "is sustainable."
