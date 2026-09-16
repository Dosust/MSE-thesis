# ASU MSE Thesis Document Architecture

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
├── 01_introduction/
├── 02_literature_theory/
├── 03_framework/
├── 04_methodology/
├── 05_results/
├── 06_discussion/
├── 07_conclusion/
└── appendices/
```

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
- SSEBE Sustainable Engineering MSE Handbook 2026–2027: https://ssebe.engineering.asu.edu/wp-content/uploads/sites/28/2026/07/MSE-Sustainable-Engineering-Handbook-2026-2027.pdf

**Verification date:** 2026-09-16
