# Global Claim / Evidence / Result Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.9 CLAIM FAMILY MATRIX  
**Authority:** \`GLOBAL_CLAIM_EVIDENCE_RESULT_CONTROL_V1.md\`  
**Empirical effect:** NONE

## 1. Interpretation

This matrix freezes the intended thesis conclusion families before final case-data qualification.

~~~math
\boxed{
\text{claim family registered}
\neq
\text{claim established}.
}
~~~

## 2. Claim family matrix

| CID | Intended conclusion family | RQ/SO/H | Stage | Required evidence | Test / gate | Result state now | Uncertainty / validity obligation | Ceiling now | Allowed wording now |
|---|---|---|---:|---|---|---|---|---|---|
| C-RQ1-STRUCTURE | Declared P–T system boundary, entities, layers, services, interfaces and states are sufficient for the final case representation. | RQ1/SO1 | 1 | qualified case sources; entity/service/interface completeness evidence; source provenance | Stage-1 representation/completeness gate | NO_RESULT | final case, topology, service scope, spatial/temporal boundary | C0 | “the framework specifies…” |
| C-RQ1-INTERFACE | Candidate interaction locations/interfaces are explicitly represented without conflating possibility with active causal coupling. | RQ1/SO1 | 1 | interface inventory + location/topology provenance | interface representation audit | NO_RESULT | case topology and interface coverage | C0 | “candidate interfaces are defined…” |
| C-RQ2-MECHANISM | Each active cross-infrastructure mechanism is directional, evidence-supported, parameterized, uncertainty-bounded and validity-scoped. | RQ2/SO2; supports H1 | 2 | qualified mechanistic evidence + activation/parameter/uncertainty records | Stage-2 evidence/mechanism gate + Stage2→3 readiness | NO_RESULT | mechanism-specific conditions and applicability | C0 | “the protocol requires evidence-qualified mechanisms…” |
| C-RQ3-MODEL | The hybrid multiscale P–T implementation correctly realizes the frozen equations, flow/jump logic and coupling semantics for tested properties. | RQ3/SO3 | 3 | code/physics/unit/numerical verification + benchmark/reference evidence | Stage-3 verification/VVUQ gates | NO_RESULT | solver/model/domain/timestep/event semantics | C0 | “the model is specified…” |
| C-H1-DYNAMIC | Dynamic causal coupling provides incremental explanatory or predictive information over static coupling under matched conditions. | RQ3/SO3/H1 | 3 | matched M2 vs M1 experiment; frozen endpoint/materiality; protected evaluation; UQ/VVUQ | H1 preregistered gate | NOT_TESTED | declared scenario population, hazard, model domain, uncertainty | C0 | “H1 is NOT TESTED” |
| C-H2-INFOORG | Information availability and organizational conditions change estimation, feasible control, response timing, service or recovery under matched physical states. | RQ4/SO4/H2 | 4 | matched N0/N1/N2 contrasts; observation/organization qualification; frozen primary rule; UQ/VVUQ | H2 preregistered gate | NOT_TESTED | information topology, latency, organization/resource assumptions, physical domain | C0 | “H2 is NOT TESTED” |
| C-RQ5-VR-STATE | For the declared case and policy class, the system can/cannot remain acceptable or reach the recovery target over the stated horizon and uncertainty representation. | RQ5/SO5 | 5 | qualified \(K,G_{rec},F_{unsafe},\Pi,\Omega\); verified viability/reachability solver; state uncertainty | Stage-5 viability/reachability gate | NO_RESULT | state/policy/horizon/requirement/uncertainty domain | C0 | “the Stage-5 object is specified…” |
| C-H3-VR-VALUE | Viability–reachability information adds incremental predictive or decision-relevant information beyond conventional performance/recovery features. | RQ5/SO5/H3 | 5 | matched information-set comparison; protected labels; frozen skill metric/materiality; UQ/VVUQ | H3 preregistered gate | NOT_TESTED | outcome-label domain, data split, policy and requirement baseline | C0 | “H3 is NOT TESTED” |
| C-RQ5-INTERFACE-DIAG | Interface criticality/sensitivity meaningfully identifies influential interfaces under a declared perturbation/diagnostic definition. | RQ5/SO5; no H-number | 5 | mechanism-specific diagnostic definition; perturbation/reference; stability/sensitivity; comparator if superiority claimed | separate diagnostic validity gate | NO_RESULT | perturbation scale, operating regime, mechanism, uncertainty | C0 | “interface criticality is a proposed diagnostic…” |
| C-RQ6-PERFORMANCE | Each physically admissible intervention has traceable resilience change, effectiveness, resource efficiency and consequence outputs relative to a matched baseline. | RQ6/SO6 | 6 | admissibility; matched baseline; resource/performance accounting; UQ/VVUQ | Stage-6 intervention-performance gate | NO_RESULT | intervention/scenario/accounting boundary and uncertainty | C0 | “Stage 6 specifies separate performance outputs…” |
| C-H4-SUS-HETEROGENEITY | At least two resilience-effective interventions differ materially in declared sustainability consequences. | RQ6/SO6/H4 | 6 | >=2 qualified resilience-effective alternatives; functional unit/boundary; consequence data/factors; frozen materiality; UQ/VVUQ | H4 preregistered gate | NOT_TESTED | intervention set, scenario domain, accounting boundaries, factors | C0 | “H4 is NOT TESTED” |
| C-RQ6-REQ-DERIVATION | A sustainability or resource constraint/target is a legitimate requirement only when its source, authority, formal translation and applicability are qualified. | RQ6/SO6; no H-number | 6 | P1.8 requirement/provenance chain + Stage-6 evidence | requirement derivation/validation/compliance gates | NO_RESULT | jurisdiction/scope/effectivity/aggregation/accounting boundary | C0 | “candidate requirements must be evidence-qualified…” |
| C-H5-DECISION | Adding sustainability information materially changes the admissible/nondominated set, dominance relation, or regret under the frozen decision problem. | RQ7/SO7/H5 | 7 | identical feasible universe; qualified Stage-6 inputs; frozen endpoint/materiality; uncertainty/stability analysis | H5 preregistered gate | NOT_TESTED | candidate set, uncertainty, requirement baseline, value/normalization rules | C0 | “H5 is NOT TESTED” |
| C-RQ7-TRANSFORM | A specific infrastructure transformation or sequence is supported for the declared context of use. | RQ7/SO7 | 7 | feasible candidate; qualified upstream claims; robustness/stability; requirement compliance; decision provenance | Stage-7 decision admissibility + consequence/robustness gates | NO_RESULT | decision context, candidate set, uncertainty, preference/value model | C0 | “the decision framework is specified…” |
| C-RQ0-SYNTHESIS | The complete framework supports bounded conclusions about coupled P–T resilience and sustainable intervention decisions for the declared case/domain. | RQ0 + RQ1–RQ7/SO1–SO7/H1–H5 | 1–7 | all constituent claim families at adequate ceilings; no unresolved contradiction; final trace audit | final synthesis/claim-evidence audit | NO_RESULT | intersection of constituent validity domains | C0 | “the thesis framework is designed to test…” |

## 3. Permanent separations

~~~math
\boxed{\text{interface exists}\not\Rightarrow\text{causal mechanism active}}
~~~

~~~math
\boxed{\text{verified implementation}\not\Rightarrow\text{validated predictive model}}
~~~

~~~math
\boxed{\text{computed viability/reachability result}\neq\text{H3 incremental-information result}}
~~~

~~~math
\boxed{\text{interface criticality}\neq\text{H3 unless separately preregistered as H3 evidence}}
~~~

~~~math
\boxed{J_{sus}\neq RID_{sus}}
~~~

~~~math
\boxed{\Delta\mathfrak R,\mathcal E_{fx},\mathcal E_{fy},\Delta\mathbf J_{sus}\neq\text{H4 adjudication by themselves}}
~~~

~~~math
\boxed{\text{score/rank}\not\Rightarrow\text{deployment recommendation}}
~~~

## 4. Claim closure rule

A row may advance from \`NO_RESULT/NOT_TESTED\` only when its exact evidence/test obligations are instantiated and reverse-traceable.

For hypothesis rows:

~~~math
\boxed{
\text{H-result}
\in
\{SUPPORTED,NOT\_SUPPORTED,NOT\_TESTED\}.
}
~~~

## 5. Synthesis ceiling

~~~math
\boxed{
\Lambda_{RQ0}
\le
\min_{c_i\in\mathcal C_{essential}}\Lambda_{c_i}.
}
~~~

A strong result in one stage cannot compensate for an unqualified indispensable upstream claim.
