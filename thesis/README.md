# ASU MSE Thesis Document Architecture

> **Current question authority (2026-09-17):** [CANONICAL_RQ_SO_HYPOTHESES_V3.md](../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md). RQ0 is overarching; RQ1–RQ7 correspond to SO1–SO7. H1–H5 retain their identifiers. RQ1/SO1 and RQ2/SO2 supply developmental evidence to H1; RQ3/SO3 → H1; RQ4/SO4 → H2; RQ5/SO5 → H3; RQ6/SO6 → H4; RQ7/SO7 → H5, with H4 intervention-performance inputs.


**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository role:** document-facing thesis architecture  
**Status:** CURRENT CONTROL STRUCTURE / content evolves under scientific gates  
**Scientific architecture:** maintained in `../project/`  
**Execution method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method

## Governing distinction

```math
\boxed{\text{Scientific architecture}\neq\text{Document architecture}.}
```

The seven-stage framework defines the scientific system architecture. This `thesis/` directory defines how the research argument is organized, audited, written, verified, and prepared for ASU Graduate College review.

The controlling chain is

```math
\boxed{
\text{ASU requirement}
\rightarrow\text{scientific claim}
\rightarrow\text{evidence}
\rightarrow\text{method}
\rightarrow\text{result}
\rightarrow\text{thesis location}
\rightarrow\text{verification}.
}
```

## Authority hierarchy

```math
\boxed{
\text{ASU Graduate College}
>
\text{SSEBE Sustainable Engineering MSE handbook}
>
\text{chair/GSC decisions}
>
\text{approved style guide}
>
\text{internal thesis conventions}.
}
```

Internal conventions never override ASU, SSEBE, or committee requirements.

## Directory structure

```text
thesis/
├── README.md
├── 00_front_matter/
│   └── README.md
├── 00_governance/
│   ├── README.md
│   ├── ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md
│   ├── ASU_REQUIREMENTS_MATRIX.md
│   ├── THESIS_MASTER_OUTLINE.md
│   ├── CLAIM_EVIDENCE_REGISTER.md
│   ├── RESEARCH_QUESTIONS_HYPOTHESES_TRACEABILITY.md
│   ├── MODEL_EXPERIMENT_VALIDATION_MATRIX.md
│   ├── FIGURE_TABLE_EQUATION_REGISTER.md
│   └── THESIS_COMPLETION_GATES.md
├── proposal/
│   ├── README.md
│   └── PROPOSAL_RELEASE_CHECKLIST.md
├── 01_introduction/
│   └── README.md
├── 02_literature_theory/
│   └── README.md
├── 03_framework/
│   └── README.md
├── 04_methodology/
│   └── README.md
├── 05_results/
│   └── README.md
├── 06_discussion/
│   └── README.md
├── 07_conclusion/
│   └── README.md
└── appendices/
    └── README.md
```

## Control entry points

| File | Role |
|---|---|
| [`00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md`](00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md) | master ASU + scientific control specification |
| [`00_governance/ASU_REQUIREMENTS_MATRIX.md`](00_governance/ASU_REQUIREMENTS_MATRIX.md) | verified ASU/SSEBE requirements vs chair/internal decisions |
| [`00_governance/THESIS_MASTER_OUTLINE.md`](00_governance/THESIS_MASTER_OUTLINE.md) | chapter architecture and chapter gates |
| [`00_governance/CLAIM_EVIDENCE_REGISTER.md`](00_governance/CLAIM_EVIDENCE_REGISTER.md) | claim/evidence/epistemic ledger |
| [`00_governance/RESEARCH_QUESTIONS_HYPOTHESES_TRACEABILITY.md`](00_governance/RESEARCH_QUESTIONS_HYPOTHESES_TRACEABILITY.md) | RQ → H → method → result → conclusion traceability |
| [`00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`](00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md) | model/baseline/data/V&V/UQ/falsification control |
| [`00_governance/FIGURE_TABLE_EQUATION_REGISTER.md`](00_governance/FIGURE_TABLE_EQUATION_REGISTER.md) | artifact purpose/provenance registry |
| [`00_governance/THESIS_COMPLETION_GATES.md`](00_governance/THESIS_COMPLETION_GATES.md) | scientific completion/freeze criteria |
| [`proposal/PROPOSAL_RELEASE_CHECKLIST.md`](proposal/PROPOSAL_RELEASE_CHECKLIST.md) | first-release proposal qualification checklist |

## Thesis chapter architecture

```math
\boxed{
\text{Problem}
\rightarrow\text{Evidence/Theory}
\rightarrow\text{Framework}
\rightarrow\text{Method}
\rightarrow\text{Results}
\rightarrow\text{Discussion}
\rightarrow\text{Conclusion}.
}
```

| Chapter | Required scientific output |
|---|---|
| 1 — Introduction | problem, significance, scope, RQs, objectives, hypotheses, proposed contribution |
| 2 — Literature Review & Theoretical Foundations | qualified evidence synthesis and verified gap |
| 3 — Conceptual & Mathematical Framework | definitions, ontology, dependency/interdependency mathematics, seven-stage framework |
| 4 — Methodology & Experimental Design | evidence/data qualification, models, baselines, experiments, V&V, UQ, falsification |
| 5 — Results | frozen-experiment outputs with uncertainty and no interpretation inflation |
| 6 — Discussion | mechanisms, literature comparison, sustainability implications, limitations |
| 7 — Conclusions & Future Work | RQ closure, supported contribution, unresolved questions |

## Scientific control rule

```math
\boxed{
\textbf{The thesis grows from verified evidence into mathematics,}
\\
\textbf{from mathematics into experiments, and from experiments into conclusions.}
}
```

No conclusion may be reverse-engineered into its evidence base.

## Current execution state

The H1 scientific implementation is governed by `../project/` authority files. Current repository state records M0/M1/M2 as implemented/verified and the H1 confirmatory design as frozen, while row-level raw-data retrieval/qualification remains the active blocking gate before calibration or confirmatory execution.

## Official ASU sources tracked

- ASU Graduate College Format Manual: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/asu-graduate-college
- ASU thesis/dissertation formatting process: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation
- ASU Format Checklist: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/format-checklist
- ASU defense process: https://graduate.asu.edu/current-students/completing-your-degree/about-your-defense
- SSEBE Sustainable Engineering MSE Handbook 2026–2027: https://ssebe.engineering.asu.edu/wp-content/uploads/sites/28/2026/07/MSE-Sustainable-Engineering-Handbook-2026-2027.pdf
- SSEBE graduate advising: https://ssebe.engineering.asu.edu/advising/graduate/

**Verification date:** 2026-09-16

