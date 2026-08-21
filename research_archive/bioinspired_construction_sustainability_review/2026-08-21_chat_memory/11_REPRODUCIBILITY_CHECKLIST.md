# Reproducibility Checklist

Use this checklist before accepting any future paper-level extraction or corpus-level synthesis.

## Corpus identity

- [ ] Paper is present in the controlled bio-inspired corpus.
- [ ] Paper_ID is unique.
- [ ] DOI is normalized and matches the focal source.
- [ ] Title/author/year identity is confirmed.
- [ ] Focal PDF/source file hash is recorded where available.

## Focal evidence

- [ ] Every substantive record comes from the focal admitted source.
- [ ] No cited-study result is attributed to focal authors.
- [ ] No background method mention is coded as implementation.
- [ ] Exact passage/table/figure/equation locator is stored.
- [ ] Page number is never fabricated.
- [ ] Missing evidence is coded `NR`, `U`, `NA`, or `PENDING_PDF`.

## Assessment tool

- [ ] Tool/method name preserved as written.
- [ ] Direct implementation established by input -> procedure -> output evidence.
- [ ] Software/database infrastructure is distinguished from the assessment architecture.
- [ ] Embedded methods are distinguished from separately implemented methods.

## Tool inputs

- [ ] Each input is a separate record.
- [ ] Input origin/source is recorded.
- [ ] Value/unit preserved exactly where reported.
- [ ] `Author_Generated` assessed separately.
- [ ] `Engineering_Performance_Input` is not assumed.

## Engineering performance

- [ ] Metric preserved as written.
- [ ] Controlled performance family added separately.
- [ ] Measurement/simulation/calculation method recorded.
- [ ] Exact result/value/unit recorded.
- [ ] Alternative/comparator recorded.
- [ ] Author-generated status supported.
- [ ] Engineering evidence is not counted as sustainability evidence.

## Sustainability outcomes

- [ ] Dimension classified Environmental/Economic/Social/Integrated.
- [ ] Indicator preserved as written.
- [ ] Exact value/unit or scale recorded.
- [ ] Method-generated status established.
- [ ] Functional basis recorded where required.
- [ ] Alternative/reference traceability retained.

## Engineering -> sustainability linkage

- [ ] `->` used only with focal evidence of analytical dependence.
- [ ] Parallel evidence coded L1 rather than forced into L2/L3.
- [ ] L2 identifies the actual input/modifier/transformation.
- [ ] L3 requires explicit integrated evidence-to-decision architecture.
- [ ] Metric-specific linkage is not inferred from the existence of an integrated framework.

## Validation

- [ ] Validation target identified.
- [ ] Validation level coded separately.
- [ ] Case application not automatically called external validation.

## Interpretation

- [ ] Paper-level interpretation derives from Sheets 02–07 only.
- [ ] Strengths are evidence-supported.
- [ ] Weaknesses distinguish paper limitations from review-specific limitations.
- [ ] Unresolved evidence remains visible.

## Workbook QA

- [ ] Frozen schema version unchanged unless a documented protocol revision exists.
- [ ] Controlled dropdown values respected.
- [ ] No formula errors.
- [ ] No silent unit conversions or rounding.
- [ ] Audit log updated for every correction/conflict.

## Corpus synthesis QA

- [ ] Only eligible/frozen paper records enter synthesis.
- [ ] Counts derive from paper-level records rather than manual re-entry.
- [ ] Gap statements are calculated from evidence coverage, not assumed in advance.
- [ ] SDG mapping, if used later, distinguishes author-explicit from reviewer-derived mapping.
- [ ] Presentation/visualization is downstream of the frozen evidence, never a source of scientific classification.