# Python Implementation and QA Notes

## 1. Implementation philosophy

The Python program should not attempt to fill every paper-specific field automatically. It should support an evidence-first workflow: validate paper identity; preserve full-text/page structure; retrieve candidate passages in P/S/F/D passes; store exact passages and locations; allow controlled evidence coding; compute deterministic gates/scores/consistency checks; and build derived workbooks only after the evidence layer is populated.

The substantive accuracy target is:

```math
\frac{|SourceSupportedClaims|}{|ExportedSubstantiveClaims|}=1.
```

Uncertain claims should be withheld or marked `U`/`NR`, not inferred.

## 2. Modular package created during the chat

A modular package was generated and self-tested with modules for controlled vocabularies, frozen configuration, data models, P/F/S/D dictionaries, PDF extraction, four-pass retrieval, method-family rules, R1–R4/lambda scoring, validation, evidence coverage, mapping, workbook generation, pipeline orchestration, JSON I/O, CLI execution, and tests.

A synthetic perfect record passed the self-test at `(3,3,3,3,3)`. A 10-paper workbook smoke test ran successfully and the spreadsheet error scan found zero tested formula errors (`#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`). This proves software-logic consistency, not the scientific correctness of real-paper scores.

## 3. Required fail-closed assertions

Reject contradictory states including:

- `SM=No` with `R1=3`.
- `M=No` with `R4=3`.
- `R3=3` without focal-author-generated engineering evidence.
- `R4=3` without method-generated sustainability evidence.
- `lambda>0` without traceable alternative correspondence.
- `lambda=3` without author-implemented F3 architecture.
- reviewer-reconstructed formula as sole basis of `lambda=3`.
- `R2=3` while an essential method-family component is missing/unclear/materially partial.
- `PERFECT` unless the exact vector is `(3,3,3,3,3)`.

## 4. Python versus Excel responsibility

Python handles PDF/page extraction, retrieval, evidence objects, controlled classification after evidence review, R1–R4/lambda rules, logical assertions, category assignment, and deterministic downstream datasets.

Excel formulas handle transparent arithmetic such as KLM gate, perfect/Tier-A labels, evidence coverage, group coverage, and mapping normalizations. Excel should not perform semantic interpretation.

## 5. Exact-passage rules

Automated retrieval may initially use character windows, but final evidence should be expanded to complete sentence/paragraph boundaries. Preserve exact wording and page/section/table/figure/equation location. Table/figure evidence must be inspected where critical values or weighting matrices are absent from prose.

## 6. Formula/architecture coding

Use `AF` author algebraic formula, `AC` author causal/process architecture, `RR` reviewer reconstruction, and `NF` no explicit qualifying formula/architecture.

An author causal architecture can support lambda=3 without one algebraic equation if the engineering variable is explicitly transformed through the implemented sustainability/decision architecture.

## 7. Suggested evidence object

```python
Evidence(
    paper_id,
    domain,
    claim,
    verbatim_passage,
    page,
    section,
    table_or_figure,
    evidence_status,
    provenance,
    author_generated,
    method_generated,
    formula_type,
)
```

Raw evidence tables are persistent. Narrative/synthesis cells are downstream derivatives.

## 8. Recommended tests

Unit tests should cover KLM truth tables, R1 implementation depth, R2 method-family essentials, R3 author-generated versus secondary evidence, R4 method-generated versus qualitative output, lambda F0/F1/F2/F3 cases, reviewer-reconstruction guard, traceable-alternative subset correspondence, perfect/Tier-A conjunctions, and coverage/mapping bounds.

Integration tests should include one synthetic perfect paper, one parallel paper (`lambda=1`), one directional-coupling paper (`lambda=2`), one TA=0 case, one missing-R2-essential case, and a 10-record workbook smoke test.

## 9. Reproducibility rule for code edits

Do not change thresholds, essential method sets, integration definitions, evidence coding, or taxonomies silently inside code. Methodological changes must first update the specification/decision log, then code and tests.

Recommended sequence:

`protocol specification → decision log → code → tests → generated workbook`.

## 10. Next implementation priority

Shift from one-summary-row-per-paper toward the evidence-dossier model with multiple P/F/S/D rows per paper, then derive summary sheets from those tables. This matches the preference to preserve the full content as written and interpret it independently later.