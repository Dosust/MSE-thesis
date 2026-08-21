# Errors, Corrections, and Conflicts

This file is mandatory reading before future edits. It records known failure modes and corrections from this chat and later high-rigor audits.

## Error 1 — Treating legacy workbook coding as primary evidence

### Problem
Older synthesis/coding cells contained classifications such as generated sustainability dimensions, framework labels, performance effects, or tool names.

### Correction
Legacy cells are comparison data only. Focal source evidence controls the final record.

`legacy coding != focal evidence`

## Error 2 — Cross-paper contamination risk

A legacy BIO58 row was previously associated with content that appears to belong to a different graded-concrete case. This showed that cells copied/extended across rows could contaminate paper-level interpretation.

### Correction
Every focal record must carry:
- Paper_ID;
- focal DOI;
- focal source locator;
- exact evidence status.

Never transfer a strategy, metric, method, result, or validation statement from one paper to another because the subject matter is similar.

## Error 3 — Overstating BIO58 engineering evidence

Earlier coding listed properties such as flexibility/indentation/recyclability/compostability as if all were confirmed engineering metrics.

### Correction
The later evidence-rigor audit confirms two specific engineering metrics:
- residual indentation = 0.14 mm;
- permanent thickness change = 0.02 mm.

Recyclability/compostability are not automatically engineering-performance metrics. Their classification depends on the focal method/context.

## Error 4 — Engineering numeric result treated as sustainability output

### Problem
A numerical performance result can look “quantitative” and be mistakenly used to satisfy a sustainability-output gate.

### Correction
`engineering numeric output != sustainability-method-generated numeric output`

BIO58's 0.14 mm and 0.02 mm values do not close the sustainability-output gate.

## Error 5 — Over-promoting S-LCA

### Problem
Legacy wording listed S-LCA as if it were directly implemented in BIO58.

### Correction
Latest high-rigor audit status:

**S-LCA = discussed only; not implemented as a separate focal tool.**

Do not restore the stronger classification without explicit focal evidence.

## Error 6 — Ambiguous treatment of economic assessment

### Problem
Earlier snapshots either omitted or over-separated LCC/economic costing.

### Correction
Latest audit supports an embedded economic/process-immanent costing component within the BiSA architecture. Preserve the focal method description. Do not label it a standalone full LCC implementation unless the focal evidence supports that exact claim.

## Error 7 — Inferring engineering-to-sustainability linkage from coexistence

### Problem
A paper can contain engineering metrics and sustainability assessment in the same article without the metrics entering the sustainability model.

### Correction
The confirmed BIO58 linkage is:

`intended building-physical function -> BiSA social-function component` = L2

The two specific indentation/thickness-change metrics remain:

`metric-specific linkage = U`

until a focal passage/equation/table establishes the transformation.

## Error 8 — Treating application as external validation

### Correction
Case application/demonstration is coded `Applied` unless independent external validation is demonstrated.

## Error 9 — Fabricating PDF page numbers

The focal BIO58 PDF binary/page map was not found in the accessible uploaded evidence set during the audit. Exact PDF page numbers must remain `PENDING_PDF` until the actual focal PDF is admitted and checked.

## Error 10 — Using outside web evidence against the declared closed-corpus evidence rule

Some earlier assistant responses referenced publisher/web pages while the user's operating rule for this work was to rely on the controlled corpus and saved/admitted focal files/PDFs.

### Correction
Future substantive coding must respect the user's closed evidence rule. External web can be used only if the user explicitly authorizes it for verification/retrieval, and any such use must be clearly separated from corpus-derived evidence.

For this archive, web-derived statements are not promoted into corpus truth merely because they appeared in an earlier assistant response.

## Error 11 — Confusing assessment architecture with software/tool infrastructure

Examples:
- GaBi can be a modeling/database basis;
- BiSA is the focal integrated assessment architecture.

Do not automatically call every software/database used by the study a sustainability assessment tool.

## Error 12 — Confusing design/engineering framework with sustainability assessment

Many bio-inspired papers contain:
- biomimicry design processes;
- performance simulation;
- structural analysis;
- thermal/daylight tools;
- review taxonomies.

These do not satisfy a sustainability-assessment implementation gate unless the focal authors actually implement a sustainability assessment method.

## Error 13 — Old 26-paper synthesis overcounting sustainability implementation

A later high-rigor re-audit found that most of the 26 synthesis papers fail the stricter implementation/output gate because they are reviews or engineering-performance studies rather than focal sustainability-assessment implementations.

Latest Stage 3 summary preserved in the archive:
- 26 legacy Table-1 studies re-audited;
- confirmed KLM PASS: 1 (BIO55);
- definitive FAIL: 23;
- provisional HOLD: 2 (BIO58 and BIO65);
- BIO58 remains held on direct quantified focal sustainability output;
- BIO65 remains held on focal full-text retrieval.

This result must be treated as a later high-rigor audit state, not overwritten by older visual-matrix labels.

## Error 14 — Forcing the evidence to match the workbook/template

### Correction
The workbook is an instrument, not the research question. The frozen schema should represent the evidence faithfully. If a paper has no sustainability assessment tool or no quantified sustainability outcome, record the absence; do not redefine an engineering tool as sustainability assessment to populate a field.

## Error 15 — Allowing previous “perfect” 10-paper scores to bias this bio-inspired review

The earlier 10-paper engineering-sustainability set used a different corpus and prior scoring architecture. It is retained only as a methodological/reference history.

No paper from that set enters the bio-inspired review unless it is independently present in the controlled bio-inspired corpus.

## Fail-closed rule

When evidence conflicts:

1. focal admitted PDF/source evidence;
2. exact table/figure/equation/passages;
3. controlled extraction;
4. interpretation;
5. legacy workbook;

with unresolved conflicts coded `U` or `PENDING_PDF` rather than resolved by intuition.