# Global Policy–Operator–Budget–Market Feedback Protocol v1

**Status:** CANONICAL CROSS-STAGE CONTROL  
**Effective date:** 2026-09-19  
**Owner:** P1.11.3  
**Scope:** policy-, operator-, authority-, budget-, resource- and market-mediated Power–Transportation relations  
**Empirical effect:** NONE

## 1. Purpose

This protocol prevents policy/economic feedback from being confused with physical network dynamics while allowing such feedback to enter Stages 4, 6 and 7 when scientifically justified.

## 2. Channel record

Every material non-physical cross-sector channel receives a versioned record:

~~~text
channel_id
channel_class
source_actor_or_system
source_object
receiver_actor_or_system
receiver_object
mechanism_statement
variables
native_units
spatial_scope
temporal_scope
timescale_class
authority_source
budget_resource_source
market_context
policy_instrument_id
evidence
uncertainty_ids
model_form
calibration_status
validation_status
scenario_ids
stage_owner
consumer_stages
gate_status
validity_domain
claim_ceiling
provenance
~~~

## 3. Admission rule

A policy/economic channel may affect confirmatory analysis only if:

~~~math
\boxed{
G_{PE}
=
G_{\rm mechanism}
\land
G_{\rm authority}
\land
G_{\rm units}
\land
G_{\rm time}
\land
G_{\rm data}
\land
G_U
\land
G_{\rm calibration}
\land
G_{\rm validity}
\land
G_{\rm provenance}.
}
~~~

A field may be N/A only when scientifically inapplicable.

## 4. Stage allocation

### Stage 3
Admit only channels needed for declared dynamic QOIs and satisfying Stage2→3 readiness.

### Stage 4
Represent operator/authority/resource constraints affecting feasible operational control.

### Stage 6
Represent intervention resources, effectiveness targets, efficiency accounting and cross-sector consequences.

### Stage 7
Represent strategic feasibility, actor objectives, public-policy/investment context, path dependence and architecture transformation.

## 5. Public policy nomenclature

Use:

~~~math
p_k^{pol}\in\mathcal P^{pol}
~~~

for public-policy instruments.

Do not reuse:
- \(\Pi_e\): dependency provenance;
- \(\Pi^{NA}\): nonanticipative operational-policy class.

## 6. Budget/resource rule

A budget variable becomes an operative constraint only if a trace exists:

~~~math
\boxed{
B
\rightarrow
\text{available resource/action}
\rightarrow
\mathcal U_{\rm feas}\ \text{or}\ \mathcal A_{\rm feas}^{strat}.
}
~~~

A reported cost is not automatically a budget constraint.

## 7. Market rule

A market variable becomes a causal channel only if its mechanism and calibration are defensible.

~~~math
\boxed{
\text{market correlation}
\neq
\text{causal market mechanism}.
}
~~~

## 8. Equilibrium rule

If an equilibrium model is used, record:
- equilibrium concept;
- actors/markets included;
- objective/behavior assumptions;
- constraints;
- calibration;
- horizon;
- whether the output is used as scenario input, transformed-state estimate or decision context.

Never relabel equilibrium output as a transient dynamic trajectory.

## 9. Actor/objective rule

For each decision actor used in Stage 7, record:

~~~text
actor_id
role
authority
controlled actions
objectives
requirements
resource/budget constraints
information available
decision horizon
value/preference evidence
uncertainty
~~~

Scientific evidence may define consequence models; it may not invent actor preferences.

## 10. Validation rule

A conceptual policy/economic loop remains DEFERRED/BLOCKED for empirical claims until the required elasticities, response functions, network cost/capacity functions or other parameters are qualified for the case and intended use.

## 11. Reverse trace

A decision/transformation claim using such a channel must be traceable:

~~~math
\boxed{
Claim
\leftrightarrow
Result
\leftrightarrow
Scenario
\leftrightarrow
Policy/Actor/ChannelID
\leftrightarrow
Model/DataVersion
\leftrightarrow
Calibration/VVUQ
\leftrightarrow
Evidence/Validity.
}
~~~
