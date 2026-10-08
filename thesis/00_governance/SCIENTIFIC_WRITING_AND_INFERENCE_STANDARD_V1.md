# Scientific Writing and Inference Standard — v1.0

**Status:** CURRENT THESIS-WIDE WRITING / INFERENCE AUTHORITY  
**Effective date:** 2026-09-17  
**Degree:** MSE Sustainable Engineering, Arizona State University  
**Scientific authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Method authority:** `../../project/EGMIV_METHOD_V1.md`

## 0A. Current citation-precedence amendment — 2026-10-08

**MANDATORY for all thesis-facing scientific content:** `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md` §0A requires adjacent, visible, verified in-text citations on every externally sourced substantive claim in manuscripts, chapter drafts, slide presentations, scientific explanations, figures, tables, and mathematical content. References-only lists do not satisfy citation rigor. Thesis-defined frozen wording must be preserved and attributed to canonical repository authority where presented as an internal definition; original hypotheses/objectives/assumptions/derivations are not falsely assigned to external authors. Unverifiable source-dependent claims remain `[OPEN — source verification required]` and must not be asserted as fact. For scope and chapter structure, current October 2026 canonical authorities supersede any historical seven-stage or RQ/SO/H references in the earlier sections of this document. No change to title/objectives/scope.

## 1. Purpose

This standard governs how scientific claims are written, supported, qualified and closed across Chapters 1–7. It operationalizes the thesis requirement that research be objective, reproducible, measurable, evidence-grounded and bounded by declared assumptions and validation domains.

The controlling chain is

```math
\boxed{
\text{Question}
\rightarrow\text{Objective}
\rightarrow\text{Object}
\rightarrow\text{Assumptions}
\rightarrow\text{Method}
\rightarrow\text{Comparator}
\rightarrow\text{Evidence}
\rightarrow\text{Uncertainty}
\rightarrow\text{Result}
\rightarrow\text{Inference}
\rightarrow\text{Validity domain}.
}
```

A thesis section is not rigorous because it is mathematically dense. It is rigorous when its claims are traceable, testable where appropriate, reproducible and no stronger than the evidence permits.

## 2. ASU/SSEBE precedence

Repository conventions remain subordinate to current ASU Graduate College, SSEBE program, committee/chair and approved style-guide requirements.

Internal scientific rules do not override official formatting or degree requirements.

## 3. Epistemic classes

During drafting, every major statement must be mentally or explicitly classified as:

| Label | Meaning |
|---|---|
| `[E]` | established by admissible external evidence within a declared domain |
| `[D]` | derived mathematically/logically by this thesis |
| `[H]` | hypothesis to be tested |
| `[P]` | proposed thesis construct, method or contribution |
| `[A]` | explicit assumption |
| `[U]` | unresolved or uncertain |
| `[R]` | result from a declared experiment with uncertainty and validity domain |

These labels are development controls and need not appear in final prose. Final prose must nevertheless preserve the distinction.

```math
\boxed{
\text{literature evidence}
\neq
\text{assumption}
\neq
\text{thesis derivation}
\neq
\text{hypothesis}
\neq
\text{result}.
}
```

## 4. Claim rule

Every substantive scientific claim must expose, directly or through the governance registers:

1. exact claim wording;
2. evidence or derivation basis;
3. mechanism or logical warrant;
4. assumptions;
5. validity domain;
6. rival/alternative where relevant;
7. test or verification route;
8. uncertainty;
9. thesis location;
10. result/conclusion linkage where applicable.

Externally sourced scientific claims require adjacent verified APA 7 author–date support unless document conventions require the evidence to be carried through a linked ledger.

A citation must support the exact proposition, population/system, method and time/domain claimed. Citation quantity does not compensate for evidentiary mismatch.

## 5. Definition and operationalization rule

Every important concept must have:

```math
\boxed{
\text{literature meaning}
\rightarrow
\text{competing definitions}
\rightarrow
\text{adopted thesis definition}
\rightarrow
\text{operational/mathematical representation}.
}
```

This applies particularly to:

- dependency / interdependency;
- interface;
- service requirement;
- resilience;
- viability;
- reachability / recovery;
- probability/confidence;
- criticality;
- effectiveness;
- efficiency;
- sustainability;
- feasibility;
- transformation.

If a concept cannot be operationalized for the declared experiment, it must not be treated as a measured quantity.

## 6. Mathematical writing rule

Every mathematical object must state, as applicable:

- symbol and name;
- type/set/domain;
- units/dimensions;
- physical or engineering meaning;
- inputs and outputs;
- assumptions;
- boundary/initial conditions;
- parameter provenance;
- limiting cases;
- validity domain.

Externally adopted or adapted equations, algorithms, thresholds, parameters and datasets require adjacent attribution.

No equation may be introduced only for visual sophistication.

## 7. Model rule

Every model must state:

```math
\boxed{
\text{purpose}
+
\text{assumptions}
+
\text{state/input/output semantics}
+
\text{parameter provenance}
+
\text{verification}
+
\text{validation domain}.
}
```

A model may be useful without being empirically complete. Such limitations must be stated explicitly.

## 8. Hypothesis rule

Every confirmatory hypothesis must specify before execution:

- comparator/baseline;
- held-constant conditions;
- treatment/change;
- response variable(s);
- practical/engineering significance criterion;
- uncertainty treatment;
- scenario/domain;
- falsification/non-support condition.

```math
\boxed{
\text{hypothesis}
\rightarrow
\text{comparator}
\rightarrow
\text{metric}
\rightarrow
\delta
\rightarrow
\text{falsification}.
}
```

A failed prerequisite or data-quality gate means `NOT TESTED`, not hypothesis falsification.

## 9. Verification, validation and uncertainty rule

Verification asks whether the model was implemented/solved correctly. Validation asks whether the model is adequate for its declared real-system use/domain.

```math
\boxed{\text{verification}\neq\text{validation}.}
```

Every primary result must include uncertainty or explain why a deterministic statement is appropriate. Sensitivity must target assumptions or parameters capable of changing the engineering conclusion, not merely generate additional plots.

## 10. Results rule

Results report what the declared experiment produced. They do not contain inflated interpretation.

Required chain:

```math
\boxed{
\text{experiment ID}
\rightarrow
\text{estimate/output}
\rightarrow
\text{uncertainty}
\rightarrow
\text{decision criterion}
\rightarrow
\text{hypothesis status}.
}
```

Null and negative outcomes must be retained. Exploratory outputs must be labeled exploratory.

## 11. Discussion rule

Discussion may interpret only registered results and qualified evidence. Each major interpretation must answer:

- what mechanism is supported or challenged?
- under what conditions?
- with what uncertainty?
- what rival explanation remains?
- which assumptions materially affect the inference?
- what engineering decision changes?
- what remains unvalidated?

If failure of assumption `A_i` would alter the conclusion, that dependence must be stated.

## 12. Conclusion rule

Chapter 7 must close the chain:

```math
\boxed{
RQ_i
\rightarrow
\text{result IDs}
\rightarrow
\text{supported answer}
\rightarrow
\text{validity domain}
\rightarrow
\text{unresolved remainder}.
}
```

A proposed contribution becomes a demonstrated contribution only when its evidence, experiment, uncertainty and validation chain closes.

## 13. Novelty rule

```math
\boxed{\text{literature support}\neq\text{novelty proof}.}
```

Novelty claims require a separate reproducible search and boundary audit. Absence from a selected corpus is not proof of absence from the field.

## 14. Chapter-specific writing contract

### Chapter 1
Defines the research contract: context, problem, gap, scope, framework, questions, objectives, hypotheses and proposed contributions. It does not prove the thesis.

### Chapter 2
Defines, compares, critiques and synthesizes evidence and theory. It does not become an author-by-author bibliography.

### Chapter 3
Derives the conceptual/mathematical framework with complete semantics, assumptions and stage-to-stage handoffs.

### Chapter 4
Converts hypotheses into reproducible experiments with baselines, data qualification, VVUQ, decision rules and falsification.

### Chapter 5
Reports outputs and uncertainty without interpretation inflation.

### Chapter 6
Interprets mechanisms, rival explanations, sustainability implications, limitations and transferability.

### Chapter 7
Answers every research question and states contribution only at the level supported by the results.

## 15. Scientific writing completion test

For any substantive section `S`:

```math
\boxed{
G_{write}(S)
=
C\land E\land D\land A\land M\land U\land T\land V
}
```

where:

- `C`: claims are explicit;
- `E`: evidence is admissible and adjacent/traceable;
- `D`: definitions are operationalized;
- `A`: assumptions are explicit;
- `M`: mathematics/method is semantically complete;
- `U`: uncertainty/limitations are addressed;
- `T`: RQ/SO/H traceability is intact;
- `V`: validity domain is stated.

A polished paragraph that fails one of these controls is not scientifically complete.
