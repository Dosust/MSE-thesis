# Decision Log and Corrections

This file records corrections made during the discussion so that future chats do not regress to superseded definitions.

## 1. Corpus-size correction

Do not say that 216 full PDFs were available. The broader K–M eligible set contained 216 records, while the later available full-text state was 202 original PDFs plus 5 additional PDFs = 207 available full texts.

Use the relevant denominator explicitly whenever reporting rates.

---

## 2. Perfect-score history

A framework-only Python run created/validated scoring logic but did not itself populate all paper-level scores. Therefore `0 perfect papers from that framework-only run` was a statement about automation, not the project evidence history.

Subsequent evidence audits established:

- 40 first-review provisional perfect-score candidates.
- 31 retained at `(3,3,3,3,3)` after second-review adjudication.
- 9 downgraded from perfect status; most lost maximum linkage because engineering influenced sustainability without satisfying the stricter explicit-integration boundary, and one lost R2 maximum because reproducibility evidence was insufficient.
- 10 papers selected from the adjudicated 31 as reference archetypes for detailed comparative analysis.

Do not revert to `0`, `40`, or `19` when referring to the final adjudicated perfect-score set unless explicitly discussing an earlier stage.

---

## 3. K/L/M versus R1/R4 duplication correction

The original K–M screen already asks whether a sustainability method is directly implemented and whether a quantitative sustainability output exists. Therefore R1 and R4 must not merely repeat those binary questions.

- Column L/SM = presence/direct implementation gate.
- R1 = depth/completeness of the implemented sustainability method.
- Column M = presence of quantified sustainability output.
- R4 = strength/completeness/traceability of the method-generated sustainability output.

---

## 4. R2 correction

Do not mechanically assign R2 from generic reporting-coverage thresholds such as 0.25/0.50/0.75. `RC` may be retained as a transparency statistic, but R2 must be method-family specific and based on essential configuration elements.

Examples:

- LCA: functional unit, system boundary, inventory, data source, impact method, procedure.
- MCDA: alternatives, criteria, weights, normalization, aggregation, decision rule.
- Optimization: variables, objectives, constraints, model, solver/search, decision rule.
- ML: dataset, predictors, target, model, training, validation.

---

## 5. Alternative-set correction

Do not require exact equality between the engineering and sustainability alternative sets. Replace exact set equality with traceable-alternative correspondence `TA`.

A subset may legitimately proceed from engineering screening into sustainability assessment if the correspondence remains traceable.

---

## 6. Lambda boundary correction

The final linkage interpretation is:

- `λ=0`: no usable relationship / domain absent / TA=0.
- `λ=1`: matched parallel evidence (`P || S`).
- `λ=2`: directional analytical coupling (`P → S`) such as service-life adjustment, functional equivalence, thresholds, design/inventory modification.
- `λ=3`: author-implemented integrated decision architecture.

`AHP`, `TOPSIS`, `MIVES`, `service life`, or `optimization` as keywords do not automatically establish λ=2 or λ=3. The engineering variable must actually enter the relevant calculation/model/decision structure.

---

## 7. Formula-type correction

Earlier `AF/RR/NF` coding was insufficient because a valid author-implemented causal/process architecture can support λ=3 even without a single algebraic formula.

Use:

- `AF` — author algebraic formula.
- `AC` — author causal/process architecture.
- `RR` — reviewer reconstruction.
- `NF` — no explicit qualifying formula/architecture.

Reviewer reconstruction alone does not justify λ=3.

---

## 8. Evidence-first correction

For the Top 10, do not reduce the papers immediately to summaries/scores. Preserve the full relevant content as written by the authors, with location, then let interpretation and scoring occur downstream.

Preferred relation:

$$
Raw\ Evidence\rightarrow Interpretation\rightarrow Scoring\rightarrow Synthesis.
$$

One paper may therefore have multiple P, F, S, and D rows.

---

## 9. Validation correction

A case study is not automatically method validation. Distinguish:

- No validation.
- Applied/demonstrated.
- Internally validated.
- Externally validated.

Do not confuse validation of engineering experiments with validation of the sustainability assessment method/tool.

---

## 10. Visual-matrix correction

The visual evidence matrix should include the entire frozen taxonomy, including categories with zero coverage. Omitting zero categories makes it impossible to distinguish `absent` from `forgotten/not coded`.

`**/*/blank` measures evidence presence/provenance, not quality.

---

## 11. Mapping-matrix correction

Downstream mapping counts should be derived from paper-level PFSD evidence/classification, not manually typed independently. A change in a paper-level classification should propagate to counts and normalized matrices.

---

## 12. Taxonomy conflict to resolve before final freeze

The mat-foundation reference uses LCSA + NAHP-G + ELECTRE IS. The current mapping vocabulary at one stage contained both `LCSA + outranking` and `Hybrid MCDM` while coding this paper only as Hybrid MCDM, leaving the more specific category empty.

Preferred resolution: classify that architecture specifically as `LCSA + outranking`, or revise the taxonomy to remove redundancy. Do not keep both without an explicit assignment rule.

---

## 13. Evidence-snippet correction

Do not retain truncated character-window snippets in the final dossier when complete-sentence/paragraph evidence is available. Extend boundaries to meaningful complete text while preserving the original wording.

---

## 14. Decision/ranking correction

The Top-10 rank is secondary reference-strength ordering. It must not be used to alter R1–R4–lambda scores or methodological eligibility.

---

## 15. Governing final principle

When in doubt, prefer `NR`/`U` and retain the source passage rather than maximizing a score. The purpose is a reproducible evidence system, not a target number of perfect papers.