# Claim–Evidence Register

**Status:** CURRENT / SYNCHRONIZED WITH RQ–SO–H v4.0  
**Scientific authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Writing/inference authority:** `SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

**Purpose:** prevent unsupported claims, hidden assumptions, retrospective evidence selection, and claims stronger than the evidence or validation domain permits.

## Governing chain

```math
\boxed{
\text{Claim}
\rightarrow\text{Evidence}
\rightarrow\text{Mechanism}
\rightarrow\text{Mathematics}
\rightarrow\text{Assumptions}
\rightarrow\text{Comparator/Test}
\rightarrow\text{Uncertainty}
\rightarrow\text{Result}
\rightarrow\text{Validity domain}
\rightarrow\text{Engineering implication}.
}
```

## Epistemic status

| Label | Meaning |
|---|---|
| `[E]` | established by admissible external evidence within a declared domain |
| `[D]` | derived mathematically/logically in the thesis from declared premises |
| `[H]` | hypothesis to be tested |
| `[P]` | proposed thesis construct or contribution not yet demonstrated |
| `[A]` | explicit assumption |
| `[U]` | unresolved/uncertain |
| `[R]` | result produced by a declared experiment, with uncertainty and validity domain |

Mixed labels such as `[D/H]` or `[P/H]` may be used during development only. Final thesis prose must separate the established/derived statement from the hypothesis or proposal being tested.

At proposal stage, `[R]` is restricted to already executed and explicitly identified verification or method-development results. A confirmatory `[R]` requires an experiment ID, frozen or declared protocol, uncertainty statement, and validity domain.

## Required fields

| Field | Description |
|---|---|
| Claim ID | stable identifier `C###` |
| Claim | exact wording |
| Status | `[E]/[D]/[H]/[P]/[A]/[U]/[R]` |
| Claim type | theoretical / physical / empirical / computational / sustainability / design |
| Source/evidence | source IDs or repository evidence objects |
| Mechanism | causal/physical/logical warrant |
| Mathematical object | equation/model if applicable |
| Assumptions | explicit conditions |
| Validity domain | where the claim applies |
| Rival/alternative | competing explanation/model |
| Test/falsification | what would challenge it |
| Uncertainty | evidence/model/data uncertainty |
| Experiment/result IDs | required for `[R]` claims |
| Thesis location | chapter/section |
| Artifact links | figure/table/equation/code/data IDs |
| Status date | last review date |

## Current canonical claims

| ID | Claim | Status | Evidence / authority | Mathematical object | Test / gate | Thesis location |
|---|---|---|---|---|---|---|
| C001 | Power and transportation can exhibit directional cross-system dependencies through physically interpretable mechanisms | `[E]` | qualified P–T/interdependency literature; Stage-2 evidence program | `\mathbb I_{P\to T},\mathbb I_{T\to P}` | evidence admissibility and mechanism qualification | Ch.2–3 |
| C002 | The thesis represents the physical core as `P+T` and Information/Organization as supporting domains that affect knowledge and feasible action | `[P/D]` during development; separate in final prose | framework v2 + evidence synthesis | `\mathcal S=\{P,T,I,O\}` | ontology/representation verification | Ch.1–3 |
| C003 | Dynamic causal P–T coupling may provide incremental explanatory or predictive information relative to static and independent representations | `[H]` | H1 | `M_0,M_1,M_2` | H1 matched comparator experiment | Ch.3–5 |
| C004 | Information availability and organizational conditions may alter state-estimation quality, feasible control, response timing and recovery | `[H]` | H2 | `p(Y_t\mid\mathcal I_t),\mathcal U(z_I,z_O),u_t` | H2 nested comparison | Ch.3–5 |
| C005 | Current service performance, future maintainability and recoverability are distinct; viability/reachability quantities may add decision-relevant information beyond conventional performance/recovery curves | `[D]` for distinction; `[H]` for incremental-value claim | viability/reachability theory + H3 | `\mathfrak R_T=(\mathcal V,\mathcal R,\rho_{\mathcal V},T_{\mathcal V},T_{\rm rec},P_{\rm viable},P_{\rm recover})` | H3 comparator experiment | Ch.2–5 |
| C006 | Interface criticality is a supporting diagnostic and is not itself the primary H4 claim unless separately preregistered | `[D/P]` | framework v2 + v4 traceability | `C_{ij}^{\mathcal V}` or current approved diagnostic notation | separate diagnostic qualification | Ch.3–6 |
| C007 | Resilience-effective interventions can differ materially in resource requirements, resource efficiencies, or admitted sustainability consequences | `[H]` | H4 | `a_k\rightarrow(\Delta\mathfrak R^{a_k},\mathbf r^{a_k},\mathcal E_{\rm fy}^{a_k},\Delta\mathbf J_{\rm sus}^{a_k})` | H4 intervention-performance experiment | Ch.4–6 |
| C008 | Adding qualified resource efficiency and admitted sustainability consequences under common feasibility and uncertainty governance may materially change the admissible/nondominated engineering decision set, dominance relations, or regret | `[H]` | H5 | `\mathcal A_R^{\star}` vs `\mathcal A_{\rm joint}^{\star}` | H5 joint-decision experiment | Ch.4–7 |
| C009 | Adaptive or sequential transformation pathways are a Stage-7 supporting extension unless separately activated by scope, evidence and preregistration | `[P]` | framework v2 | pathway/policy object if activated | separate activation and validation gate | Ch.3–4 / future work |
| C010 | The seven-stage framework is a thesis synthesis, not an already established literature framework | `[D/P]` | evidence synthesis + canonical framework | stages 1–7 | Chapter-2 synthesis and framework derivation | Ch.2–3 |
| C011 | The framework must preserve constituent-system physics while standardizing cross-system interdependency representation and handoffs | `[P]` | theoretical-foundation work | subsystem physics + `\mathbb I` + `F_{\mathcal G}^{m}` | theoretical consistency + demonstrator verification | Ch.3–4 |
| C012 | Effectiveness, efficiency and sustainability are distinct intervention-performance concepts | `[D]` once definitions/accounting boundaries are fixed | engineering definitions + thesis operationalization | declared `E_fx`, `E_fy`, `\mathbf J_{sus}` objects | operational-definition and accounting-boundary gate | Ch.1, Ch.3–6 |

## Registration rule

Before a major new statement is promoted into Chapters 1, 2, 3, 6, or 7, it must receive a Claim ID or be traceable to an existing registered claim.

A literature citation alone does not promote a statement to `[E]`. Relevance, evidence type, system/population, mechanism, validity domain, and limitations must be checked. A mathematical derivation does not promote an empirical proposition to `[E]`, and a simulated result does not establish validity outside the declared model and validation domain.
