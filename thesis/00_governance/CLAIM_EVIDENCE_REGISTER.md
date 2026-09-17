# Claim–Evidence Register

**Status:** CURRENT / SYNCHRONIZED WITH RQ–SO–H v3  
**Effective date:** 2026-09-17  
**Purpose:** prevent unsupported claims, hidden assumptions, retrospective evidence selection, and drift between research questions, experiments and conclusions.

**Scientific authorities:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`, `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`, `../../project/CANONICAL_INTERVENTION_PERFORMANCE_AMENDMENT_V2_1.md`  
**Writing/inference authority:** `SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

---

## Governing chain

```math
\boxed{
\text{Claim}
\rightarrow
\text{Evidence}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Mathematics}
\rightarrow
\text{Assumptions}
\rightarrow
\text{Comparator / developmental criterion}
\rightarrow
\text{Test}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Result}
\rightarrow
\text{Validity domain}
\rightarrow
\text{Engineering implication}.
}
```

---

## Epistemic status

| Label | Meaning |
|---|---|
| `[E]` | established by admissible external evidence |
| `[D]` | derived mathematically/logically from stated premises |
| `[H]` | hypothesis to be tested |
| `[P]` | thesis proposal/construct |
| `[A]` | explicit assumption |
| `[U]` | unresolved/uncertain |
| `[R]` | result produced by a frozen/declared experiment |

### Final-state rule

Mixed labels such as `[D/H]` and `[P/H]` are not accepted in frozen thesis prose. If a sentence contains both a derivation/proposal and a hypothesis, split it into separate registered claims.

At proposal stage, `[R]` is restricted to already executed, clearly identified method-development or verification results. A result claim must carry an experiment/artifact ID, uncertainty statement and validity domain.

---

## Required fields

| Field | Description |
|---|---|
| Claim ID | stable identifier `C###` |
| Exact claim | wording that may appear in the thesis |
| Status | one of `[E]/[D]/[H]/[P]/[A]/[U]/[R]` |
| Claim type | theoretical / physical / empirical / computational / sustainability / decision / design |
| Source/evidence | source IDs, evidence objects, or thesis derivation |
| Mechanism | causal/physical/logical warrant |
| Mathematical object | equation/model/set/metric if applicable |
| Assumptions | explicit conditions |
| Validity domain | where the claim applies |
| Rival/alternative | competing explanation/model/definition |
| Test/falsification | what would challenge the claim |
| Uncertainty | evidence/model/data uncertainty |
| RQ / SO / H | traceability |
| Thesis location | chapter/section |
| Artifact links | figure/table/equation/code/data/result IDs |
| Status date | last review date |

---

## Canonical claim set

| ID | Claim | Status | Primary authority/evidence | Mathematical object | Test / gate | Traceability |
|---|---|---|---|---|---|---|
| C001 | Power and transportation can exhibit directional cross-system dependencies whose mechanisms must be distinguished from common exposure or correlation. | `[E]` | qualified interdependency and P–T literature; Stage-2 evidence program | `\mathfrak d_e`, `\mathbb I` | evidence admissibility + mechanism mapping | RQ2/SO2; Ch.2–3 |
| C002 | The thesis can represent coupled P–T infrastructure as an interdependent System of Systems while preserving constituent physical laws and explicit information/organizational support domains. | `[P]` | framework authority + evidence-qualified ontology | `\mathcal S=\{P,T,I,O\}`, `\mathcal G` | structural/ontology verification | RQ1/SO1; Ch.3 |
| C003 | Under matched disturbances and initial conditions, dynamic causal P–T coupling may provide measurable incremental explanatory or predictive information relative to static coupling and independent-system representations. | `[H]` | H1 | `M_0,M_1,M_2` | H1 preregistered comparison | RQ3/SO3/H1; Ch.4.5–5.1 |
| C004 | Under matched physical conditions, changes in information availability and organizational constraints may alter state-estimation quality, feasible actions, response timing, recovery trajectories and Stage-5 resilience outcomes. | `[H]` | H2 | `P+T`, `P+T+I`, `P+T+I+O`, `\mathcal U_t` | H2 preregistered nested comparison | RQ4/SO4/H2; Ch.4.6–5.2 |
| C005 | Uncertainty-aware viability and reachability quantities may provide incremental engineering information beyond conventional performance/recovery curves for declared maintainability/recovery tasks. | `[H]` | H3 + viability/reachability theory | `R_{\rm curve}`, `\mathfrak R_T` | H3 preregistered skill/decision comparison | RQ5/SO5/H3; Ch.4.7–5.3 |
| C006 | Interface criticality is a supporting diagnostic whose engineering value must be separately qualified; ranking superiority is not assumed and is not silently treated as H4. | `[P]` | Stage-5/6 framework + v3 boundary | declared `C_{ij}`/`S_{ij}` diagnostic | separate diagnostic test if promoted | RQ5–RQ6; Ch.3.10/4.10 |
| C007 | Resilience-effective interventions can have materially different resource-efficiency and sustainability consequence profiles within declared accounting boundaries. | `[H]` | H4 + intervention-performance amendment | `\mathcal E_{\rm fx}`, `\mathcal E_{\rm fy}`, `\mathbf J_{\rm sus}` | H4 preregistered consequence/materiality test | RQ6/SO6/H4; Ch.4.8–5.4 |
| C008 | Incorporating sustainability consequences, with effectiveness and efficiency obligations enforced, may change the feasible/nondominated engineering intervention set relative to resilience-only evaluation. | `[H]` | H5 + intervention-performance amendment | `\mathcal A_R^{\star}`, `\mathcal A_{R,S}^{\star}` | H5 preregistered set/regret comparison | RQ7/SO7/H5; Ch.4.9–5.5 |
| C009 | Resilience, intervention effectiveness, resource efficiency and sustainability are distinct engineering concepts and must not be used as synonyms. | `[D]` | canonical intervention-performance definitions | `\mathfrak R_T`, `\mathcal E_{\rm fx}`, `\mathcal E_{\rm fy}`, `\mathbf J_{\rm sus}` | definition/operationalization consistency | RQ5–RQ7; Ch.1–7 |
| C010 | The seven-stage sequence is a thesis synthesis used to organize the research program; it is not presented as an already established literature framework. | `[P]` | project synthesis + qualified foundations | Stages 1–7 | Chapter-II synthesis + framework consistency | RQ0; Ch.2–3 |
| C011 | Adaptive/sequential transformation pathways are a conditional Stage-7 extension and cannot be presented as a demonstrated H5 contribution unless separately operationalized, preregistered and tested. | `[P]` | v3 scope + Stage-7 authority | `a_{0:H}` / adaptive policy if activated | separate activation/preregistration gate | RQ7; Ch.3/4/7 |
| C012 | A quantitative statement becomes a thesis result only when it is produced by a declared experiment or verification procedure with recoverable provenance, uncertainty and validity domain. | `[D]` | writing/inference standard | result object / artifact IDs | result-registration gate | cross-cutting |

---

## Claim promotion rule

A statement may be promoted:

```math
[P/H/U]\rightarrow[R]
```

only when its declared evidence/test chain closes. A citation alone cannot convert a proposal or hypothesis into an established result.

Likewise

```math
[H]\not\rightarrow\text{falsified}
```

when a prerequisite evidence, data, solver or preregistration gate fails. The correct status is **NOT TESTED**.

---

## Registration rule

Before a major new statement is promoted into Chapter I, II, III, VI or VII, it must receive a Claim ID or be traceable to an existing registered claim.

A literature citation does not automatically promote a claim to `[E]`. Source relevance, evidence type, system/population, mechanism, validity domain and limitations must be checked.

Before Chapter V result prose is frozen, every `[R]` statement must identify:

```math
\boxed{
\text{experiment/result ID}
+\text{estimate}
+\text{uncertainty}
+\text{decision rule}
+\text{validity domain}.
}
```
