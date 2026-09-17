# Thesis Governance and Control Plane

**Status:** CURRENT / SYNCHRONIZED 2026-09-17

This folder treats the ASU Sustainable Engineering MSE thesis as a traceable scientific system rather than a loose writing project.

## Governing rule

```math
\boxed{
\text{Every material claim, definition, equation, figure, experiment and result must have}
\\
\text{a declared scientific role, evidence status, validity boundary and thesis destination.}
}
```

## Authority hierarchy

```math
\boxed{
\text{ASU Graduate College}
>
\text{SSEBE Sustainable Engineering MSE requirements}
>
\text{chair/GSC decisions}
>
\text{approved style guide}
>
\text{internal thesis governance}.
}
```

Internal files never convert a project preference into an ASU requirement.

## Current control artifacts

| File | Function |
|---|---|
| `ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md` | joins verified ASU/SSEBE compliance with scientific architecture |
| `ASU_REQUIREMENTS_MATRIX.md` | separates institutional requirements, chair decisions and internal standards |
| `THESIS_MASTER_OUTLINE.md` | controls chapter/subchapter architecture and chapter gates |
| `RQ_SO_H_TRACEABILITY_V3.md` | **current** RQ0/RQ1–RQ7 → SO1–SO7 → H1–H5/evidence → chapter closure mapping |
| `CLAIM_EVIDENCE_REGISTER.md` | claim status, mechanism, uncertainty, validity and result ledger |
| `CONCEPT_DEFINITION_OPERATIONALIZATION_REGISTER.md` | prevents concept/metric definition drift across chapters |
| `SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md` | thesis-wide writing, inference, citation, limitation and conclusion standard |
| `MODEL_EXPERIMENT_VALIDATION_MATRIX.md` | model/baseline/treatment/held-condition/data-role/V&V/UQ/falsification control |
| `FIGURE_TABLE_EQUATION_REGISTER.md` | scientific purpose and provenance registry for formal artifacts |
| `THESIS_COMPLETION_GATES.md` | conditions for declaring sections scientifically complete/frozen |

`RESEARCH_QUESTIONS_HYPOTHESES_TRACEABILITY.md` and `RQ_SO_H_TRACEABILITY_V2.md` are superseded stubs retained only to redirect historical links to v3.

## External scientific authorities

The governance layer must remain consistent with:

- `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`;
- `../../project/CANONICAL_INTERVENTION_PERFORMANCE_AMENDMENT_V2_1.md`;
- `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`;
- `../../project/RESEARCH_REASONING_PROTOCOL.md`;
- `../../project/EGMIV_METHOD_V1.md`;
- `../../project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md` for Chapter I.

Where framework v2 and the v2.1 intervention amendment interact, the amendment controls Stages 6–7 on effectiveness/efficiency/decision semantics; Stage 5 remains viability + reachability + probability.

## Epistemic labels

```math
[E]=\text{external evidence},\quad
[D]=\text{derived},\quad
[H]=\text{hypothesis},\quad
[P]=\text{proposal},\quad
[A]=\text{assumption},\quad
[U]=\text{unresolved},\quad
[R]=\text{registered result}.
```

A final thesis sentence should have one primary epistemic role. Mixed draft labels must be decomposed before freeze.

## Scientific section gate

For section `S_j`:

```math
\boxed{
G(S_j)=
C\land E\land M\land T\land U\land R
}
```

where:

- `C`: conceptually complete for declared scope;
- `E`: evidence complete/qualified for declared claims;
- `M`: mathematically and physically consistent where applicable;
- `T`: traceable to RQ/SO/H or developmental obligation;
- `U`: uncertainty and validity boundaries declared;
- `R`: reproducible/auditable.

Only when all required gates pass may a section be labeled scientifically frozen.

## Core anti-drift rule

```math
\boxed{
\text{question wording}
\rightarrow
\text{objective}
\rightarrow
\text{test/evidence obligation}
\rightarrow
\text{result}
\rightarrow
\text{conclusion}
}
```

must remain synchronized across `project/`, `thesis/`, proposal material, presentation material and final manuscript text.
