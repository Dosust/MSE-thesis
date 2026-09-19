# Global Claim / Evidence / Result Control v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.9 CONTROL-PLANE AUTHORITY  
**Scope:** thesis-wide claim identity, evidence sufficiency, result admissibility, uncertainty, validity domain, claim ceiling, and allowed wording  
**Empirical effect:** NONE. This artifact does not create or adjudicate any H1–H5 result.

## 1. Purpose

P1.9 closes the final major control-plane gap before the P2 master workbook.

The thesis must never move directly from a scientific idea to prose. Every intended conclusion is governed by:

~~~math
\boxed{
\text{Claim}
\rightarrow
\text{RQ/SO/H}
\rightarrow
\text{Stage}
\rightarrow
\text{Required Evidence}
\rightarrow
\text{Test/Gate}
\rightarrow
\text{Result}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Validity Domain}
\rightarrow
\text{Claim Ceiling}
\rightarrow
\text{Allowed Wording}.
}
~~~

The controlling rule is:

~~~math
\boxed{
\text{strength of stated conclusion}
\le
\text{strength of qualified evidence and valid result}.
}
~~~

## 2. Claim object

Every controlled thesis claim is represented as:

~~~math
\boxed{
\mathfrak c_i =
(
CID_i,
Ver_i,
Statement_i,
Type_i,
RQ_i,
SO_i,
H_i,
Stage_i,
Scope_i,
EvidenceReq_i,
Evidence_i,
Test_i,
QOI_i,
Result_i,
U_i,
\Omega_i,
\Lambda_i,
W_i,
Status_i,
Prov_i
).
}
~~~

where:

- \`CID\`: persistent claim identifier;
- \`Ver\`: claim version;
- \`Statement\`: proposition to be established;
- \`Type\`: claim class;
- \`RQ/SO/H\`: research-question, objective, and hypothesis trace;
- \`Stage\`: producing stage(s);
- \`Scope\`: object/population/scenario/context addressed;
- \`EvidenceReq\`: evidence required before testing or wording;
- \`Evidence\`: qualified evidence actually available;
- \`Test\`: gate, comparator, benchmark, or inferential procedure;
- \`QOI\`: quantity/endpoint supporting the claim;
- \`Result\`: result identity and adjudication;
- \`U\`: uncertainty record;
- \`\Omega\`: validity domain;
- \`\Lambda\`: claim ceiling inherited from credibility;
- \`W\`: allowed wording class;
- \`Status\`: independent workflow state;
- \`Prov\`: provenance and reverse trace.

## 3. Claim classes

The permitted top-level classes are:

~~~text
STRUCTURAL
MECHANISM
MODEL_IMPLEMENTATION
PREDICTIVE_OR_EXPLANATORY
CAUSAL_EFFECT
VIABILITY_REACHABILITY
DIAGNOSTIC
INTERVENTION_PERFORMANCE
SUSTAINABILITY_CONSEQUENCE
REQUIREMENT_DERIVATION
DECISION
SYNTHESIS
~~~

A claim class controls what evidence is necessary.

~~~math
\boxed{
\text{verification evidence}
\not\Rightarrow
\text{predictive validity}
}
~~~

~~~math
\boxed{
\text{association}
\not\Rightarrow
\text{causal effect}.
}
~~~

## 4. Three independent claim-state axes

P1.9 prohibits one overloaded status field.

### 4.1 Gate state

~~~text
PASS
BLOCKED
FAIL
DEFERRED
N/A
~~~

### 4.2 Claim maturity

~~~text
DRAFT
SPECIFIED
EVIDENCE_QUALIFIED
TEST_READY
TESTED
SUPERSEDED
RETIRED
~~~

### 4.3 Result state

For H1–H5:

~~~text
SUPPORTED
NOT_SUPPORTED
NOT_TESTED
~~~

For non-hypothesis claims:

~~~text
NO_RESULT
QUALIFIED
VERIFIED
VALIDATED
PASS
FAIL
INCONCLUSIVE
~~~

A blocked prerequisite does not constitute negative evidence.

~~~math
\boxed{
BLOCKED \not\Rightarrow FAIL
}
~~~

and for H1–H5:

~~~math
\boxed{
\text{mandatory prerequisite unresolved}
\Rightarrow
\text{NOT TESTED}.
}
~~~

## 5. Global claim gate

For claim \(c_i\):

~~~math
\boxed{
G_C(c_i)
=
G_{trace}
\land
G_{evidence}
\land
G_{test}
\land
G_{result}
\land
G_U
\land
G_{\Omega}
\land
G_{\Lambda}.
}
~~~

A thesis conclusion is admissible only if the gates required by its class pass.

A \`PASS\` design-control gate does not imply an empirical claim result.

## 6. Evidence sufficiency by claim class

| Claim class | Minimum evidence obligation | Typical prohibited leap |
|---|---|---|
| STRUCTURAL | qualified system boundary/entity/service/interface evidence | ontology → real-case completeness |
| MECHANISM | directional mechanism evidence + activation/validity conditions | correlation → mechanism |
| MODEL_IMPLEMENTATION | code/algorithm/physics/numerical verification | verification → real-world accuracy |
| PREDICTIVE_OR_EXPLANATORY | matched comparator + protected evaluation + UQ/VVUQ | in-sample fit → predictive value |
| CAUSAL_EFFECT | identified intervention/exposure contrast + confounding/identification control | predictive association → causation |
| VIABILITY_REACHABILITY | qualified \(K,G_{rec},F_{unsafe},\Pi,\Omega\) + verified solver | computed set → empirically valid resilience |
| DIAGNOSTIC | defined diagnostic + comparator/reference + stability | ranking → causal importance |
| INTERVENTION_PERFORMANCE | physically admissible intervention + matched baseline + resource/performance evidence | modeled change → deployable benefit |
| SUSTAINABILITY_CONSEQUENCE | declared functional unit/boundary + qualified factors/data + UQ | partial metric → “sustainable” |
| REQUIREMENT_DERIVATION | qualified source/need + P1.8 translation/provenance | measured outcome → hard requirement |
| DECISION | admissible alternatives + qualified upstream results + uncertainty/value rules | score → universal optimum |
| SYNTHESIS | all constituent claims within their ceilings | local evidence → universal thesis generalization |

## 7. RQ/SO/H traceability firewall

The canonical research architecture is:

~~~text
RQ1/SO1 -> Stage 1 -> developmental structural conclusions
RQ2/SO2 -> Stage 2 -> mechanism/evidence conclusions
RQ3/SO3 -> Stage 3 -> H1
RQ4/SO4 -> Stage 4 -> H2
RQ5/SO5 -> Stage 5 -> H3 + separately qualified interface diagnostic
RQ6/SO6 -> Stage 6 -> H4 + requirements derivation
RQ7/SO7 -> Stage 7 -> H5
RQ0 -> bounded synthesis of RQ1–RQ7
~~~

No new H6/H7 is created.

Interface-criticality superiority is not silently treated as H3.  
Stage-6 requirement derivation is not silently treated as H4.  
A final engineering recommendation is not silently treated as H5 unless it is exactly the preregistered H5 claim.

## 8. Result identity

A result used to support a claim must be uniquely traceable to:

~~~math
\boxed{
ResultID
\leftrightarrow
(CID,Ver)
\leftrightarrow
ScenarioID/RunID
\leftrightarrow
DataVersion
\leftrightarrow
ModelVersion
\leftrightarrow
RequirementBaseline
\leftrightarrow
VVUQRecord.
}
~~~

A figure, table, or scalar without this reverse trace cannot close a claim gate.

## 9. Uncertainty and validity domain

Every empirical or computational conclusion must state the uncertainty relevant to that claim.

~~~math
\boxed{
U_{claim}
\supseteq
\{U_{measurement},U_{state},U_{parameter},U_{model},U_{numerical},U_{future}\}
}
~~~

using only applicable components.

The validity domain must identify, where relevant:

- physical network/topology;
- hazard/disturbance regime;
- operating state;
- observation architecture;
- control/policy class;
- intervention class;
- requirement baseline;
- scenario population;
- temporal/spatial scale;
- data version;
- intended use.

Extrapolation is prohibited unless separately supported.

## 10. Claim ceiling

P1.9 inherits P1.7 credibility levels \(C0\)–\(C5\).

~~~math
\boxed{
\Lambda_{claim}
=
\min_{j\in\mathcal J_i}\Lambda_j
}
~~~

over the required evidence components for claim \(i\).

The ceiling controls wording, not only publication labels.

- C0: proposed / specified / designed;
- C1: verified implementation for declared properties;
- C2: works on declared synthetic/analytic benchmark;
- C3: validated for declared subsystem QOI/domain;
- C4: validated for declared coupled intended use/domain;
- C5: hypothesis-eligible adjudication in declared domain.

## 11. Wording firewall

| Verb/phrase | Minimum semantic obligation |
|---|---|
| “defines / specifies / proposes” | C0 design authority |
| “implements / verifies” | relevant C1 verification |
| “reproduces / works on benchmark” | C2 benchmark evidence |
| “validates / is accurate for” | intended-use validation with domain/QOI/UQ |
| “predicts” | protected predictive evaluation |
| “explains incremental information” | valid comparator and frozen endpoint |
| “causes / effect of” | causal identification appropriate to the claim |
| “improves” | matched baseline + direction + materiality + uncertainty |
| “robust” | declared uncertainty domain + stability evidence |
| “sustainable” | explicit sustainability dimensions/boundaries; no universal label from a partial vector |
| “optimal / best” | explicit decision problem, feasible set, objective/value model, uncertainty; never universal |
| “generalizes” | evidence for the stated target population/domain |

Unqualified words such as “proven”, “always”, “universally”, “risk-free”, and “guaranteed in reality” are prohibited unless the exact mathematical/legal meaning and evidence justify them.

## 12. Negative, null, blocked, and inconclusive evidence

A fully admissible test that fails the frozen criterion may support \`NOT_SUPPORTED\`, \`FAIL\`, or \`NOT_VALIDATED_FOR_DECLARED_USE\`, depending on claim type.

A blocked prerequisite supports only \`NOT_TESTED\`, \`NO_RESULT\`, or \`BLOCKED\`. It may not be rewritten as evidence against the claim.

If the test executes but uncertainty or identifiability prevents the planned conclusion, preserve \`INCONCLUSIVE\` where applicable.

## 13. Post-result change control

If claim statement, endpoint, comparator, materiality rule, validity domain, evidence class, or allowed wording is materially changed after target results are inspected:

~~~math
\boxed{
\text{affected analysis}
\rightarrow
EXPLORATORY
}
~~~

unless a protected independent confirmation remains.

Every such change must be versioned and traceable to P1.3, P1.7, and P1.8 controls.

## 14. Thesis writing rule

Every major Results, Discussion, and Conclusion statement must be traceable to a \`CID\`.

~~~math
\boxed{
CID
\rightarrow
ResultID
\rightarrow
Evidence/UQ/VVUQ
\rightarrow
ValidityDomain
\rightarrow
ClaimCeiling
\rightarrow
Sentence.
}
~~~

If no \`CID\` exists, the conclusion is not yet authorized for final thesis wording.

## 15. Current pre-data state

~~~math
\boxed{
G_{P1.9}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

Current confirmatory state remains:

~~~text
H1 = NOT TESTED
H2 = NOT TESTED
H3 = NOT TESTED
H4 = NOT TESTED
H5 = NOT TESTED
~~~

No case-specific result, threshold, validation outcome, or recommendation is created by P1.9.
