# EGMIV–TSP Thesis Scientific Operating Protocol v1.0

**Status:** CURRENT THESIS-ONLY OPERATING PROTOCOL  
**Effective date:** 2026-09-16  
**Research method:** EGMIV  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Framework authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**RQ–SO–H authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Document architecture:** `../thesis/00_governance/THESIS_MASTER_OUTLINE.md`  
**Page-control authority:** `../thesis/00_governance/THESIS_PAGE_BUDGET_160_V1.md`

> EGMIV–TSP does not replace EGMIV. It governs how every thesis prompt, search, derivation, learning request, evidence review, model question, figure, table, code task, and writing task is routed into the thesis.

## 1. Governing rule

```math
\boxed{
\text{Prompt}\rightarrow\text{Thesis destination}\rightarrow\text{Scientific question}\rightarrow\text{Evidence}\rightarrow\text{Mathematics}\rightarrow\text{Test}\rightarrow\text{Citation}\rightarrow\text{Thesis-ready output}.
}
```

```math
\boxed{\text{No thesis destination}\Rightarrow\text{No thesis research action}.}
```

A task may proceed without a chapter destination only when it is a necessary governance, formatting, reproducibility, or data-integrity task.

## 2. Mandatory routing

Every substantive request must map to:

```math
\boxed{
\text{Chapter}\rightarrow\text{Section}\rightarrow\text{Stage}\rightarrow RQ_i\rightarrow SO_i\rightarrow \mathcal H(i)\rightarrow\text{scientific object}\rightarrow\text{output}.
}
```

Before execution, determine:
1. where the result enters the thesis;
2. which RQ/SO/H or governance obligation it supports;
3. what evidence/model/equation/parameter/data object is missing;
4. what artifact will be produced;
5. what condition terminates the task.

## 3. Operating cycle

```math
\boxed{
\text{ROUTE}\rightarrow\text{DEFINE}\rightarrow\text{DECOMPOSE}\rightarrow\text{SEARCH}\rightarrow\text{QUALIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}\rightarrow\text{TEST}\rightarrow\text{CITE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{BOUND}\rightarrow\text{ADVANCE}.
}
```

- **ROUTE:** locate the task in the thesis.
- **DEFINE:** convert the request into a precise scientific question.
- **DECOMPOSE:** identify system, states, mechanisms, constraints, uncertainty, observables.
- **SEARCH:** search only for a declared evidence deficit.
- **QUALIFY:** apply the source gate below.
- **FORMULATE:** translate mechanism into mathematics.
- **DERIVE:** check logic, physics, dimensions, and limiting behavior.
- **TEST:** connect to H1–H5, a benchmark, or explicit verification/validation test.
- **CITE:** attach verified APA 7 author–date citations to externally sourced claims.
- **SYNTHESIZE:** establish agreement, contradiction, limitation, and thesis implication.
- **BOUND:** state uncertainty, assumptions, and validity domain.
- **ADVANCE:** identify only the next admissible dependency.

## 4. Online research rule

Research follows:

```math
\boxed{
\text{missing thesis claim/object}\rightarrow\text{targeted search}\rightarrow\text{qualified source}\rightarrow\text{extraction}\rightarrow\text{thesis insertion}\rightarrow\text{STOP}.
}
```

Searches must declare the target section, missing object, source class, extraction fields, and stopping condition. Additional papers are not collected merely because they are interesting.

Preferred evidence order:

```math
\boxed{
\text{primary peer-reviewed/official standard/government/operator source}
>
\text{authoritative technical report}
>
\text{high-quality review}
>
\text{secondary source}.
}
```

For engineering thresholds:

```math
\boxed{
\text{standard/regulation/operator requirement}
>
\text{empirical evidence}
>
\text{case-specific requirement}
>
\text{explicit thesis assumption}.
}
```

## 5. Source qualification gate

```math
\boxed{G_S=G_I\land G_R\land G_C\land G_Q\land G_M\land G_V}
```

where:
- `G_I`: identity verified;
- `G_R`: relevant to the thesis object;
- `G_C`: actually supports the claim;
- `G_Q`: appropriate scientific authority;
- `G_M`: metadata verified;
- `G_V`: validity domain compatible.

If `G_S=0`, the source may inform exploration but is not qualified thesis evidence.

## 6. Evidence status

| Label | Meaning |
|---|---|
| `[E]` | established external evidence |
| `[D]` | thesis-derived result |
| `[H]` | hypothesis |
| `[P]` | proposed construct |
| `[A]` | assumption |
| `[U]` | unresolved |

No status changes without evidence or derivation.

## 7. APA 7 rule

> **No externally sourced scientific claim enters the thesis without an adjacent, verified APA 7 author–date citation.**

This includes facts, theory, definitions, adopted equations/algorithms, numerical parameters, thresholds, standards, datasets, and literature-based gap/consensus claims. Thesis-defined notation, hypotheses, transparent derivations, assumptions, and thesis results do not receive fabricated citations; their premises are cited where needed.

## 8. Mathematical mindset

For mathematical tasks identify, where applicable:

```math
\boxed{\mathcal X,\mathcal U,\Theta,\eta,F,K,\mathcal Y_{obs},\mathcal M.}
```

Every major equation must pass checks for definitions, units, physical mechanism, boundary/initial conditions, limiting behavior, identifiability, computability, uncertainty, and validity domain.

Use the minimum mathematics necessary to add explanatory, predictive, control, uncertainty, falsification, or decision value.

## 9. Physics and engineering rule

```math
\boxed{
\text{mathematical term}\leftrightarrow\text{physical/organizational mechanism}\leftrightarrow\text{measurable or defensibly parameterized quantity}.
}
```

Generic coupling coefficients without physical meaning, units, evidence, or validity limits are not thesis-ready.

## 10. Model-selection rule

```math
\boxed{\text{Framework stage}>\text{model family}>\text{algorithm}.}
```

A method is activated only when justified by scientific necessity, data support, assumption compatibility, identifiability, computational feasibility, and incremental scientific/decision value. SCM, POMDP, MPC, HJ, Monte Carlo, GNN, RL, DRO, and surrogates remain conditional tools.

## 11. Hypothesis protocol

Every primary claim must trace through:

```math
\boxed{H_i\rightarrow\text{mechanism}\rightarrow\text{baseline}\rightarrow\text{metric}\rightarrow\text{experiment}\rightarrow\text{uncertainty}\rightarrow\text{falsification}\rightarrow\text{result}.}
```

Frozen contrasts remain:

```math
H_1:M_2\text{ vs }M_1\text{ vs }M_0,
```
```math
H_2:P+T\text{ vs }P+T+I\text{ vs }P+T+I+O,
```
```math
H_3:R_{\rm curve}\text{ vs }R_{\rm curve}+\mathfrak R_T,
```
```math
H_4:a_k\rightarrow(\Delta\mathfrak R^{a_k},\Delta\mathbf J_{\rm sus}^{a_k}),
```
```math
H_5:\mathcal A_R^\star\text{ vs }\mathcal A_{R,S}^\star.
```

## 12. VVUQ rule

```math
\boxed{\text{Verification}\neq\text{Validation}\neq\text{Uncertainty Quantification}.}
```

Verification checks whether the equations/code were solved correctly. Validation checks adequacy for intended real-system use. UQ quantifies uncertainty in state, parameter, prediction, resilience, and decision quantities.

## 13. Thesis-learning mode

Learning requests follow:

```math
\boxed{
\text{Intuition}\rightarrow\text{Formal definition}\rightarrow\text{Equation}\rightarrow\text{Derivation/mechanism}\rightarrow\text{Physical meaning}\rightarrow\text{Assumptions/limits}\rightarrow\text{Exact thesis application}.
}
```

General tutorials stop once the thesis application is established.

## 14. Thesis-response contract

A substantive response should satisfy the applicable parts of:
1. thesis location;
2. direct scientific answer;
3. minimum necessary mathematics;
4. qualified evidence with adjacent APA 7 citations;
5. assumptions/uncertainty/limits;
6. exact thesis artifact or insertion;
7. next admissible step only.

## 15. Thesis-only skill library

| Skill | Function |
|---|---|
| TSP-S1 Thesis Routing | map task to chapter/stage/RQ/SO/H |
| TSP-S2 Problem Formulation | convert prompt to a testable problem |
| TSP-S3 Targeted Evidence Search | search only for declared deficits |
| TSP-S4 Source Qualification | qualify evidence before use |
| TSP-S5 APA 7 Citation | verified adjacent citations |
| TSP-S6 Mathematical Reasoning | define/derive/check/bound models |
| TSP-S7 Physical Interpretation | connect math to P–T–I–O mechanisms |
| TSP-S8 Interdependency Modeling | preserve dependency semantics |
| TSP-S9 Hypothesis Design | preserve H1–H5 comparators/tests |
| TSP-S10 VVUQ | verification/validation/UQ/sensitivity |
| TSP-S11 Scientific Writing | compact thesis-ready argument |
| TSP-S12 Literature Synthesis | evidence→limitation→thesis need |
| TSP-S13 Reproducibility | data/code/version/provenance control |
| TSP-S14 Thesis Compression | enforce 160-page cap without deleting science |
| TSP-S15 Scientific Visualization | only figures/tables with scientific function |

## 16. Prohibited thesis drift

Do not browse without a defined evidence need; collect papers without extraction purpose; redesign the framework casually; add AI/ML because it is fashionable; choose algorithms before gates pass; invent parameters/probabilities/thresholds; treat correlation as causation; cite unchecked sources; use literature as proof of novelty; hide contradictory evidence; suppress uncertainty/limits; generate equations for visual sophistication; or perform work that cannot be mapped to an approved thesis or governance destination.

## 17. Current routed task

The immediate active task remains:

```math
\boxed{
\text{qualify evidence for }\{s_P^{\min},s_T^{\min},s_{P,\rm rec},s_{T,\rm rec},F,T_V,T_R\}.
}
```

Routing:

```text
Chapter:   3 and 4
Stage:     5
RQ/H:      RQ5 / H3
Output:    qualified threshold-and-horizon evidence registry
Stop when: each required quantity is evidence-supported, explicit assumption, rejected, or documented open with uncertainty and validity metadata
```

Then proceed only through:

```math
\boxed{(K,G_{\rm rec},F,T_V,T_R)\rightarrow\text{uncertainty qualification}\rightarrow\Pi_{\rm adm}\rightarrow\mathcal C_{H3}\rightarrow\text{solver selection/reference verification}.}
```

Parallel work remains limited to already-authorized H1/H2 qualification tasks.

## 18. Master quality condition

A thesis output is admissible only when the applicable elements of

```math
\boxed{
\text{Definition}+\text{Mechanism}+\text{Evidence}+\text{Mathematics}+\text{Assumptions}+\text{Test}+\text{Uncertainty}+\text{VVUQ}+\text{Citation}+\text{Validity domain}
}
```

are explicit and internally consistent.

```math
\boxed{\textbf{No thesis purpose = no research action.}}
```



**Question-to-hypothesis mapping convention:** `i=1,…,7` indexes RQ/SO; `j=1,…,5` indexes hypotheses. `\mathcal H(i)` denotes the declared mapping in `CANONICAL_RQ_SO_HYPOTHESES_V3.md`, including developmental qualification for RQ1/RQ2. It does not assert a one-to-one RQ–H correspondence.
