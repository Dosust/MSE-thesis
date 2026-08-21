# Chat Memory — Engineering–Sustainability Integration Review

This is a compact chronological memory intended to let a future chat continue without reconstructing the project from scratch.

## Phase A — Original supervisor extraction requirements

The project began from a spreadsheet workflow in which papers are first screened on Columns K–M using title/abstract/keywords and full text if needed:

- K: built-environment/construction relevance, Yes/No.
- L: sustainability evaluation/assessment method/tool directly implemented, Yes/No.
- M: quantifiable sustainability output, Yes/No.

Only K=L=M=Yes proceeds to detailed N–T extraction:

- N: engineering/functional performance effects.
- O: core elements of the evaluation method, not the paper.
- P: evaluation-method procedure as a chain.
- Q: construction strategy/strategies being evaluated.
- R: what is evaluated, separating engineering and sustainability dimensions/outcomes.
- S: whether/how the assessment method/tool is validated.
- T: named sustainability evaluation methods/tools for backward snowballing.

The original review contained 282 broad records; 216 records had previously passed the K/L/M triple-Yes screen.

## Phase B — Evidence validation

An early `OK/NO OK` validation idea was refined into evidence-based checking:

- YES OK: fully supported.
- PARTIAL OK: substantially correct but incomplete/imprecise.
- NO OK: unsupported/incorrect.
- FULL PDF NOT AVAILABLE where necessary.

The key shift was from re-extracting everything to verifying spreadsheet statements against paper evidence, while preserving exact passages and locations.

## Phase C — R1–R4–lambda methodological scoring

A stricter methodological layer was introduced to distinguish papers that truly integrate engineering performance with sustainability assessment.

Core variables:

- R1: depth/completeness of implemented sustainability method.
- R2: methodological reproducibility.
- R3: focal-author-generated engineering/functional evidence.
- R4: method-generated quantified sustainability output.
- lambda: engineering–sustainability linkage depth.

The hard Tier-A gate was defined as:

$$
R_1=3\land R_2\ge2\land R_3=3\land R_4=3\land\lambda\ge2.
$$

Perfect status was defined as:

$$
(3,3,3,3,3).
$$

The review explicitly rejected a broad compensating total-score gate. Total score may rank papers only after route/eligibility classification.

## Phase D — Extended routes

To broaden the analytical set without weakening all requirements, explicit routes were discussed:

- B1: complete engineering + sustainability evidence for matched alternatives, but parallel (`lambda=1`).
- B2: author-generated engineering evidence under-reported (`R3=2`) with strong integration.
- B3: limited sustainability coverage (`R4=2`) with strong engineering evidence/integration.

Only one controlled limitation is allowed for an extended paper. R1 remains a hard requirement in the stronger design.

## Phase E — Corpus audit history

A first-review audit identified 40 provisional perfect-score candidates. A second-review audit retained 31 papers at `(3,3,3,3,3)`. Most downgrades were caused by the stricter lambda=3 boundary; one key downgrade concerned R2 reproducibility.

This superseded earlier claims such as `0 perfect papers` (framework-only run) or `40 final perfect papers` (first review only).

## Phase F — Top-10 archetype selection

Because all 31 perfect papers have the same score vector, R1–R4–lambda cannot rank them internally. A secondary reference-strength ranking selected 10 archetypes spanning different integration mechanisms. Their rank is not an eligibility score.

The selected CSV IDs are:

`245, 241, 232, 59, 124, 169, 282, 83, 23, 10`.

See `05_TOP10_REFERENCE_SET.md` for titles/DOIs and roles.

## Phase G — Central PFSD model

The project was reframed around:

$$
P_{engineering}\rightarrow F_{integration}\rightarrow S_{sustainability}\rightarrow D_{decision}.
$$

The fuller chain includes construction strategy Q upstream:

$$
Q\rightarrow P\rightarrow F\rightarrow S\rightarrow D.
$$

The key research question became: what physically/technically performs, how that performance is connected/transformed, what sustainability consequence is generated, and how that consequence affects a decision.

## Phase H — Keyword dictionaries

Controlled P/F/S/D dictionaries were developed. A major methodological rule was frozen:

`keyword hit != evidence`.

The correct chain is:

$$
Keyword\rightarrow Candidate\ Passage\rightarrow Focal\ Author\ Action\rightarrow Equation/Procedure\rightarrow Evidence\rightarrow Interpretation\rightarrow Score.
$$

## Phase I — Important corrections

Several earlier formulations were corrected:

1. 216 is not the same as available full PDFs; later state was 207 full texts (202+5).
2. Column L/M must not be duplicated by R1/R4; R1/R4 assess strength/depth after the binary gates.
3. R2 must be method-family specific; RC is only a supporting statistic.
4. Exact equality of engineering and sustainability alternative sets was replaced by traceable-alternative correspondence TA.
5. lambda=2 versus lambda=3 was sharpened: directional coupling versus explicit author-integrated architecture.
6. Formula types were expanded to AF/AC/RR/NF.
7. Case application was separated from internal/external validation.
8. Downstream visual/mapping matrices should be derived from the evidence layer, not independently recoded.
9. Full taxonomy should include zero-coverage categories.
10. The `LCSA + outranking` versus `Hybrid MCDM` taxonomy conflict must be resolved before freeze.

## Phase J — Python implementation

A modular Python package was produced with schemas, controlled vocabularies, PDF retrieval, four-pass candidate retrieval, scoring functions, validation assertions, coverage/mapping logic, workbook generation, JSON I/O, CLI, and tests.

A synthetic `(3,3,3,3,3)` self-test passed. A 10-record workbook smoke test produced correct `PERFECT`/`Tier A` formulas and zero tested spreadsheet errors. This is a software QA result, not a substitute for full-text scientific verification.

## Phase K — Workbook verification

A high-rigor workbook (`Top10_Engineering_Sustainability_High_Rigor.xlsx`) was inspected. Its architecture was strong, but the following improvements were identified before freeze:

- derive visual/mapping matrices from PFSD evidence;
- resolve LCSA+outranking versus Hybrid MCDM;
- include complete taxonomy including zeros;
- replace generic output phrases with specific outcomes where supported;
- structure R2 essential components explicitly;
- distinguish AF from AC;
- preserve causal arrows only when verified;
- clean truncated evidence snippets to complete sentences/paragraphs.

## Phase L — Current preference: full evidence extraction

The current preferred direction is not to force the Top-10 papers immediately into final summaries. Instead, build a structured evidence dossier that preserves the full relevant content as written by the authors, with location and multiple records per paper.

Preferred architecture:

$$
Raw\ Evidence\rightarrow Interpretation\rightarrow Scoring\rightarrow Synthesis.
$$

The user intends to read the extracted source evidence and design/validate the interpretation independently.

## Current frozen next step

Build the final Top-10 evidence-first database/workbook using the definitions, algorithms, and relational tables in this folder. Do not silently change the scientific rules during coding. Any change must first update `06_DECISION_LOG_AND_CORRECTIONS.md`.