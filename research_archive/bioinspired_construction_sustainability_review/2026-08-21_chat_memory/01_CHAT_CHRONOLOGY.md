# Chat Chronology and Decision History

This file records the substantive trajectory of the current chat so future work can recover not only the final schema but why it exists.

## A. Presentation-template context

The chat began with an NUS Cognition X Lab PowerPoint template. The user asked what content could fill the template, then requested the template background be white. A white-background version was produced. This presentation context is peripheral to the scientific extraction workflow but belongs to the same chat and is preserved in `08_PRESENTATION_CONTEXT.md`.

## B. Return to the 10-paper engineering-sustainability reference set

The discussion then returned to a previously selected set of 10 engineering-sustainability papers. The user asked:

- where the 10-paper work stood;
- the titles of the 10 papers;
- JavaScript to identify them in Zotero and place them in a subcollection;
- how to assess each paper fairly for strengths and weaknesses.

The core fairness principle was reaffirmed:

`evidence first -> paper-level assessment -> strengths/weaknesses -> later cross-paper comparison`

Scientific quality and usefulness for the review question were to be kept separate.

The top-10 reference set is preserved in `06_TOP10_REFERENCE_SET.md`. It is **not automatically part of the bio-inspired corpus**.

## C. Shift to the bio-inspired construction workbook

The user supplied the controlled workbook:

`scopus_export_bio-inspiration AND ( framework OR evaluation ) AND construction 8(1).xlsx`

The user clarified that papers used in the bio-inspired review must come from this workbook/corpus and that the prior template should be adapted to the actual study rather than changing the research rules to fit the template.

The central evidence questions were narrowed to:

1. sustainability assessment tool implemented;
2. inputs to the tool;
3. engineering-performance metrics measured;
4. sustainability outcomes assessed, specifically;
5. engineering-performance-to-sustainability linkage.

## D. Frozen conceptual chain

The working chain became:

`Assessment tool -> Tool inputs -> Engineering performance -> Sustainability outcomes`

with a separate evidence question for:

`Engineering performance -> sustainability assessment -> sustainability outcome`

The main methodological insight was that a paper may contain technical performance and sustainability language without an implemented sustainability assessment. Therefore engineering simulation, experimental performance, sustainability claims, and sustainability-method outputs must remain separate evidence objects.

## E. Evidence-first workbook architecture

A 10-sheet workbook architecture was designed:

1. `00_Control`
2. `01_Papers`
3. `02_Assessment_Tools`
4. `03_Tool_Inputs`
5. `04_Engineering_Performance`
6. `05_Sustainability_Outcomes`
7. `06_Performance_Tool_Linkage`
8. `07_Validation`
9. `08_Paper_Interpretation`
10. `09_Audit_Log`

The architecture deliberately separates raw/controlled evidence from interpretation.

## F. BIO58 chosen as calibration paper

BIO58:

Horn, Dahy, Gantner, Speck & Leistner (2018), `Bio-inspired sustainability assessment for building product development - Concept and case study`, DOI `10.3390/su10010130`.

It was chosen because the focal paper explicitly develops/applies a sustainability assessment architecture for building-product development and is therefore a useful calibration case for distinguishing:

- assessment architecture;
- tool/model inputs;
- engineering/functional evidence;
- sustainability outcomes;
- integration/linkage;
- validation.

## G. Initial Version 1.0 freeze

A Version 1.0 workbook was created and the schema frozen. The initial audit was conservative and explicitly left page-level and case-specific fields unresolved because the focal PDF binary was not located in the available uploaded sources.

Important initial frozen findings included:

- BiSA as the focal integrated sustainability assessment/decision-support method;
- environmental LCA as an embedded assessment component;
- a GaBi-based life-cycle inventory/model backbone;
- environmental/economic/social function-and-burden architecture;
- direct representation of the intended building-physical function within the BiSA social-function component;
- case/application validation rather than automatically calling it external validation.

## H. Later high-rigor BIO58 re-audits

Subsequent high-rigor audit artifacts in the File Library strengthened and corrected the BIO58 state while retaining the frozen schema.

The strongest later audit records report:

- assessment tool: BiSA;
- embedded methods: environmental LCA plus an economic/process-immanent costing component;
- S-LCA status: discussed only, not implemented as a separate focal tool;
- engineering metrics confirmed from reviewer-extracted focal evidence:
  - residual indentation = 0.14 mm;
  - permanent thickness change = 0.02 mm;
- environmental results discussed include overall normalized environmental burden, GWP improvement, and end-of-life recycling/composting effects, but exact direct numeric focal sustainability outputs remain unresolved in the accessible evidence;
- metric-specific linkage remains unresolved: the two engineering metrics are confirmed as performance evidence but are not proven to enter BiSA;
- direct engineering-to-sustainability linkage remains L2 only for the intended building-physical function -> BiSA social-function component;
- the M/sustainability-output gate remains `U / PROVISIONAL HOLD` because a page-anchored direct numeric focal sustainability result has not been closed in the accessible evidence set.

## I. High-rigor corpus re-audit context

A later 26-paper high-rigor re-audit found that, under the stricter KLM implementation/output boundary:

- many legacy papers were engineering-performance or review papers rather than focal sustainability-assessment implementations;
- BIO55 was a confirmed KLM PASS;
- BIO58 remained a priority/provisional hold pending a direct numeric focal sustainability result;
- BIO65 remained a full-text hold.

This is important because it shows why the old synthesis workbook cannot be treated as ground truth.

## J. Current request

The user requested a full GitHub memory folder containing all information needed for future chats with high rigor, recall, and reproducibility, and asked for errors to be double-checked rather than propagated.

This archive is the response to that request.