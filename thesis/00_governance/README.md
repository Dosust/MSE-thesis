# Thesis Governance and Control Plane

This folder converts the ASU MSE thesis into a traceable scientific system rather than a loose writing project.

## Governing rule

```math
\boxed{
\text{Every claim, equation, figure, experiment, result and conclusion must have}
\\
\text{a defined place, epistemic status, evidence/test path, uncertainty treatment and ASU-compliant destination.}
}
```

## Current control artifacts

| File | Function |
|---|---|
| `ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md` | top-level specification joining ASU/SSEBE compliance and scientific control |
| `ASU_REQUIREMENTS_MATRIX.md` | separates verified ASU/SSEBE rules from chair/GSC decisions and internal standards |
| `THESIS_MASTER_OUTLINE.md` | current seven-chapter architecture and chapter deliverables |
| `RQ_SO_H_TRACEABILITY_V3.md` | current RQ0/RQ1–RQ7 → SO1–SO7 → H1–H5 → method/result/conclusion traceability |
| `SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md` | thesis-wide evidence, definition, assumption, mathematical-writing, inference and validity-domain standard |
| `CLAIM_EVIDENCE_REGISTER.md` | claim status, source, mechanism, assumptions, uncertainty, experiment/result and thesis-location ledger |
| `MODEL_EXPERIMENT_VALIDATION_MATRIX.md` | model, baseline, held constants, treatment, data, V&V, UQ, thresholds and falsification control |
| `SUSTAINABILITY_DIMENSION_ADMISSION_AND_ACCOUNTING_STANDARD_V1.md` | thesis-wide Stage-6/7 authority for admitting, typing, bounding, comparing and validating sustainability/resource dimensions |
| `SUSTAINABILITY_DIMENSION_REGISTER_V1.md` | live admission matrix and status register for every proposed resilience/resource/sustainability/transformation quantity |
| `FIGURE_TABLE_EQUATION_REGISTER.md` | scientific purpose and provenance registry for formal artifacts |
| `THESIS_COMPLETION_GATES.md` | formal conditions for declaring sections scientifically complete/frozen |

`RESEARCH_QUESTIONS_HYPOTHESES_TRACEABILITY.md` and `RQ_SO_H_TRACEABILITY_V2.md` are superseded provenance stubs. They must not override `RQ_SO_H_TRACEABILITY_V3.md`.

For all Stage-6/7 work and any thesis use of the terms **sustainability**, **sustainable transformation**, **resource efficiency**, **carbon**, **energy consequence**, **accessibility consequence**, **economic consequence**, or **joint resilience–sustainability decision**, the sustainability admission standard and live register are mandatory controls. No new sustainability dimension may enter confirmatory H4/H5 analysis outside that governance chain.

## External scientific authorities

- `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`
- `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`
- `../../project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md`
- `../../project/RESEARCH_REASONING_PROTOCOL.md`
- `../../project/EGMIV_METHOD_V1.md`

## Epistemic labels

```math
[E]=\text{established external evidence},\quad
[D]=\text{thesis derivation},\quad
[H]=\text{hypothesis},\quad
[P]=\text{proposal/construct},
```

```math
[A]=\text{assumption},\quad
[U]=\text{uncertain/unresolved},\quad
[R]=\text{declared result}.
```

Final prose need not display these labels, but it must preserve their meaning. At proposal stage, `[R]` is restricted to already executed, explicitly identified verification or method-development results.

## Scientific gate

For any substantive section `S_j`:

```math
\boxed{G(S_j)=C\land E\land M\land T\land R\land U\land V}
```

where:

- `C`: conceptually complete;
- `E`: evidence complete/qualified for the declared scope;
- `M`: mathematically/physically consistent;
- `T`: traceable to RQ/objective/hypothesis or developmental obligation;
- `R`: reproducible/auditable;
- `U`: uncertainty/limitations addressed where relevant;
- `V`: validity domain stated.

Only when all required gates pass may a section be marked scientifically frozen.

For an admitted sustainability dimension `j`, the additional non-compensatory gate is:

```math
\boxed{
G_{\rm sus}(j)
=
M_j\land Q_j\land X_j\land D_j\land U_j\land B_j\land K_j\land V_j\land S_j.
}
```

All applicable terms must pass before the dimension enters confirmatory H4/H5 inference.

## Current hypothesis semantics

```math
H_1:\ M_2\ \text{vs}\ M_1\ \text{vs}\ M_0,
```

```math
H_2:\ P+T\ \text{vs}\ P+T+I\ \text{vs}\ P+T+I+O,
```

```math
H_3:\ R_{\rm curve}\ \text{vs}\ R_{\rm curve}+\mathfrak R_T,
```

```math
H_4:\ a_k\rightarrow(\Delta\mathfrak R^{a_k},\Delta\mathbf J_{\rm sus}^{a_k}),
```

```math
H_5:\ \mathcal A_R^{\star}\ \text{vs}\ \mathcal A_{R,S}^{\star}.
```

Interface criticality is a supporting diagnostic. Adaptive/sequential transformation is a supporting Stage-7 extension unless separately activated and preregistered.
