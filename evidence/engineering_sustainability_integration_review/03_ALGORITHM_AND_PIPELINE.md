# Deterministic Evidence-First Algorithm and Pipeline

## 1. Purpose

This algorithm is the direct specification for a modular Python implementation. It is designed to maximize supported information while minimizing unsupported inference.

The controlling principle is:

$$
\boxed{Extract\ first\rightarrow Interpret\ second\rightarrow Score\ third}
$$

No semantic score is allowed to generate its own supporting evidence retrospectively.

---

## 2. Inputs

For each of the 10 selected papers, require:

- Paper_ID
- Rank
- Original CSV ID
- Authors
- Exact title
- Year
- Journal/source
- DOI
- verified PDF/full text

Before analysis assert:

$$
N_{papers}=10,
$$

$$
N_{unique\ DOI}=10,
$$

$$
N_{unique\ PaperID}=10.
$$

No silent duplicate deletion.

---

## 3. PDF identity verification

For each PDF, verify DOI when available; otherwise title plus author correspondence. Outcomes are `Confirmed`, `Unresolved`, or `Mismatch`.

`Mismatch` stops processing. `Unresolved` remains unresolved; do not guess paper identity.

---

## 4. Full-text segmentation

Preserve page boundaries and, where possible, section labels such as Abstract, Introduction, Methods/Methodology, Materials/Experimental Program, Sustainability Assessment, Results, Discussion, Conclusion, References, Appendices, Tables/Figures/Equations.

A keyword hit in the Introduction or References does not prove focal implementation.

---

## 5. Four retrieval passes

### Pass P — Engineering/functional performance

Retrieve candidate passages using controlled performance families. For every verified focal-author performance item create:

$$
P_{ip}=(Family,Metric,Method,Result,Unit,Alternative,Comparator,Origin,Passage,Location).
$$

### Pass S — Sustainability

Retrieve implemented sustainability methods and actual quantitative outcomes. Create one record per outcome rather than compressing all sustainability evidence into one cell:

$$
S_{is}=(Method,Dimension,Indicator,Result,Unit,FunctionalBasis,Alternative,Origin,Passage,Location).
$$

### Pass F — Integration

Retrieve candidate passages showing normalization, weighting, thresholding, service-life transformation, functional equivalence, inventory/design modification, MCDM, value functions, causal loss chains, optimization, regression/surrogate coupling, etc.

Create:

$$
F_{if}=(SourceVariable,Transformation,TargetVariable,TA,Formula/Chain,FormulaType,Passage,Location).
$$

### Pass D — Decision

Retrieve ranking, selection, rejection, optimization, recommendation, trade-off, Pareto, robustness, and scenario-selection evidence:

$$
D_{id}=(DecisionType,Alternatives,DecisionRule,Outcome,Sensitivity/Robustness,Passage,Location).
$$

---

## 6. Evidence verification after retrieval

A keyword hit is only a retrieval cue. For each candidate passage determine:

1. Is this the focal study or background/cited work?
2. What did the focal authors actually do?
3. What variable/method/result is present?
4. What alternative does it belong to?
5. Is the passage complete enough to preserve context?
6. Is the item author-generated, author-implemented, secondary, assumed, supplier-derived, or unclear?

If unsupported, do not export a substantive claim.

---

## 7. Fifth pass — PFSD cross-link reconstruction

After the independent P, S, F, D passes, test whether the pieces form a valid analytical chain. Do not infer causality merely because items coexist in the same paper.

For each candidate chain:

$$
C_{ic}=(P_{ip},F_{if},S_{is},D_{id}).
$$

Require traceable alternative correspondence and direct evidence that F links the relevant variables.

Use `→` only for verified analytical dependence. Use `||` for parallel coexistence.

---

## 8. K–M decisions

Compute K, SM, and M from the verified evidence layer. Then:

$$
G_i^{KLM}=K_iSM_iM_i.
$$

For a generic corpus, $G_i^{KLM}=0$ stops detailed analytical extraction. For the already selected Top-10 reference set, the gate is retained as a reproducibility check rather than assumed silently.

---

## 9. N–T extraction

Create N–T only after supporting evidence exists.

- N summarizes author-generated engineering/functional effects.
- O lists assessment-method core elements in author terminology.
- P reconstructs the method workflow from supported steps only.
- Q identifies construction strategies/alternatives.
- R separates engineering, environmental, economic, social, integrated outcomes.
- S reports assessment-method validation/application status.
- T lists named sustainability evaluation methods/tools for backward snowballing.

The exact supporting passages remain stored separately and are never replaced by the summaries.

---

## 10. R1–R4 and λ classification

### R1

Use method implementation evidence. Maximum score requires operational core elements, procedure, implementation, and method-generated outputs.

### R2

Determine method family first, then evaluate method-specific essential components. Do not allow a generic percentage threshold to create R2=3.

### R3

Maximum score requires focal-author-generated quantitative engineering/functional evidence with method, metric, result, and traceable alternative; unit is required where conventionally applicable.

### R4

Maximum score requires method-generated quantitative sustainability evidence with identified indicator, result, traceable alternative, interpretable unit/scale, and functional basis where methodologically required.

### λ

1. Test valid F3 architecture first.
2. If no F3, test F2 directional coupling.
3. If no F2, test F1 matched parallel evidence.
4. Otherwise F0.

`RR` reviewer reconstruction cannot be the sole basis of λ=3.

---

## 11. Perfect status

After scoring:

$$
\Pi_i=\mathbb{1}[(R_1,R_2,R_3,R_4,\lambda)=(3,3,3,3,3)].
$$

Do not type `PERFECT` manually; derive it from scores.

---

## 12. Evidence-first Top-10 dossier structure

Do not compress the complete evidence into one row. One paper may contain many P/F/S/D records. Recommended relational tables:

- `01_Papers`
- `02_KLM_Evidence`
- `03_NT_Evidence`
- `04_P_Engineering`
- `05_F_Integration`
- `06_S_Sustainability`
- `07_D_Decision`
- `08_Method_Architecture`
- `09_Validation`
- `10_Methods_Mentioned`
- `11_Interpretation`
- `12_Scoring`

This keeps extraction separate from interpretation and scoring.

---

## 13. Derived synthesis

Only after the evidence dossier is populated and validated should downstream comparative tables be created:

$$
Evidence\ layer\rightarrow Controlled\ classification\rightarrow Narrative\ synthesis\rightarrow Visual\ matrices.
$$

Avoid independently recoding the same scientific fact in multiple sheets.

---

## 14. Integrity tests before export

The implementation must raise an error for contradictory states including:

- SM=0 with R1=3.
- M=0 with R4=3.
- R3=3 without author-generated P evidence.
- R4=3 without method-generated S evidence.
- λ>0 with TA=0.
- λ=3 without author-implemented F3 architecture.
- R2=3 while a required method-family component is missing/partial.
- Perfect status without exact `(3,3,3,3,3)`.

Scan final workbook for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, and accidental `#N/A`.

---

## 15. Deterministic orchestration

```text
START
  load frozen protocol
  load controlled vocabularies
  load 10-paper manifest
  validate unique IDs/DOIs

  FOR each paper:
      verify PDF identity
      preserve page/section structure
      PASS P: retrieve + verify engineering evidence
      PASS S: retrieve + verify sustainability evidence
      PASS F: retrieve + verify integration evidence
      PASS D: retrieve + verify decision evidence
      cross-link P/F/S/D with traceable alternatives
      compute K/SM/M and KLM gate
      extract N–T summaries from evidence
      classify R1, R2, R3, R4, lambda
      run logical assertions
      derive perfect status
      store evidence + interpretation separately
  END FOR

  build derived narrative synthesis
  build evidence-coverage matrix
  build P→F, F→S, optional S→D matrices
  run formula/data integrity tests
  export final workbook/data package
END
```

---

## 16. Accuracy policy

The system is optimized for

$$
\boxed{Maximum\ supported\ information+Minimum\ unsupported\ inference}
$$

not for filling every cell. If the full text does not support a field, preserve `NR` or `U` rather than inventing content.