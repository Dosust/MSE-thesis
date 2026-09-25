# ASU MSE Thesis Document Architecture

**Canonical thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Title authority:** `../project/CANONICAL_THESIS_TITLE_V1.md`

> **Current question authority (2026-09-17):** [CANONICAL_RQ_SO_HYPOTHESES_V3.md](../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md). RQ0 is overarching; RQ1–RQ7 correspond to SO1–SO7. H1–H5 retain their identifiers. RQ1/SO1 and RQ2/SO2 supply developmental evidence to H1; RQ3/SO3 → H1; RQ4/SO4 → H2; RQ5/SO5 → H3; RQ6/SO6 → H4; RQ7/SO7 → H5.

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

## Current scientific authorities

| File | Role |
|---|---|
| [`../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`](../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md) | seven-stage scientific architecture |
| [`../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`](../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md) | RQ0 + RQ1–RQ7 + SO1–SO7 + H1–H5 |
| [`../project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md`](../project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md) | Chapter-I content, page allocation and flow authority |
| [`../project/CANONICAL_PT_SOS_COMPLEX_DYNAMICS_AMENDMENT_V1_1.md`](../project/CANONICAL_PT_SOS_COMPLEX_DYNAMICS_AMENDMENT_V1_1.md) | source-grounded P–T SoS/service/dynamics interpretation |
| [`00_governance/RQ_SO_H_TRACEABILITY_V3.md`](00_governance/RQ_SO_H_TRACEABILITY_V3.md) | thesis-facing question/objective/hypothesis traceability |
| [`00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`](00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md) | thesis-wide claim/evidence/inference writing standard |
| [`00_governance/CLAIM_EVIDENCE_REGISTER.md`](00_governance/CLAIM_EVIDENCE_REGISTER.md) | claim/evidence/epistemic ledger |
| [`00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`](00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md) | model/baseline/data/V&V/UQ/falsification control |

Older traceability or Chapter-I files are provenance unless explicitly reactivated by a versioned amendment.

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
│   ├── RQ_SO_H_TRACEABILITY_V3.md
│   ├── SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md
│   ├── MODEL_EXPERIMENT_VALIDATION_MATRIX.md
│   ├── FIGURE_TABLE_EQUATION_REGISTER.md
│   └── THESIS_COMPLETION_GATES.md
├── proposal/
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
| 1 — Introduction | context, problem, gap, significance, scope, framework logic, RQ0/RQ1–RQ7, SO1–SO7, H1–H5, proposed contributions |
| 2 — Literature Review & Theoretical Foundations | qualified evidence synthesis, operational definitions and evidence-supported gap |
| 3 — Conceptual & Mathematical Framework | definitions, ontology, interdependency mathematics, seven-stage v2 framework and stage handoffs |
| 4 — Methodology & Experimental Design | evidence/data qualification, baselines, held constants, treatments, experiments, V&V, UQ, practical significance and falsification |
| 5 — Results | declared-experiment outputs with uncertainty, decision criteria and no interpretation inflation |
| 6 — Discussion | mechanisms, rival explanations, assumption sensitivity, literature comparison, effectiveness/efficiency/sustainability implications, limitations |
| 7 — Conclusions & Future Work | RQ0/RQ1–RQ7 closure, H1–H5 status, supported contributions, validity limits and unresolved remainder |

## Scientific control rule

```math
\boxed{
\textbf{The thesis grows from verified evidence into mathematics,}
\\
\textbf{from mathematics into experiments, and from experiments into conclusions.}
}
```

No conclusion may be reverse-engineered into its evidence base.

## ASU format controls currently tracked

Current official Graduate College guidance requires use of the ASU Format Wizard for documents undergoing format review; the Graduate College Format Manual supersedes internal style conventions. Current controls tracked in governance include 1.25-inch left/right margins, 1-inch top/bottom margins, consistent approved TrueType font, double-spaced main text with stated exceptions, abstract length not exceeding 350 words, correct preliminary-page sequence/pagination, and a complete defense-ready document submission through iPOS on the required timeline. Program-specific thesis requirements remain governed by the current SSEBE Sustainable Engineering MSE handbook and chair/GSC decisions.

## Current execution state

Chapter 1 scientific content remains **PASS — FROZEN** under [`00_governance/CHAPTER_I_FREEZE_2026-09-18.md`](00_governance/CHAPTER_I_FREEZE_2026-09-18.md), with the bounded source-grounding changes to Sections 1.1, 1.2, and 1.12 authorized by [`00_governance/CHAPTER_I_SOURCE_ALIGNMENT_AMENDMENT_V1_2026-09-19.md`](00_governance/CHAPTER_I_SOURCE_ALIGNMENT_AMENDMENT_V1_2026-09-19.md). The amendment changes source grounding and interpretive precision only; it does not alter RQ0/RQ1–RQ7, SO1–SO7, H1–H5, or the seven-stage flow.

The H1 scientific implementation is governed by `../project/` authority files. M0/M1/M2 software fixtures are verified at their declared benchmark level, but accepted case M2 execution remains blocked because no current dependency has Stage2→3 PASS. `EV_T_to_P` is causally accepted for the declared synthetic case but remains Stage2→3 BLOCKED; the other instantiated P–T case relations remain causally BLOCKED. H2–H5 remain subject to their hypothesis-specific evidence, metric, accounting-boundary, VVUQ and preregistration gates.

## Official ASU sources tracked

- ASU Graduate College Format Manual: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/asu-graduate-college
- ASU thesis/dissertation formatting process: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation
- ASU Format Checklist: https://graduate.asu.edu/current-students/completing-your-degree/formatting-your-thesis-or-dissertation/format-checklist
- ASU defense process: https://graduate.asu.edu/current-students/completing-your-degree/about-your-defense
- SSEBE Sustainable Engineering MSE Handbook 2026–2027: https://ssebe.engineering.asu.edu/wp-content/uploads/sites/28/2026/07/MSE-Sustainable-Engineering-Handbook-2026-2027.pdf
- SSEBE graduate advising: https://ssebe.engineering.asu.edu/advising/graduate/

**Requirements verification date:** 2026-09-17
