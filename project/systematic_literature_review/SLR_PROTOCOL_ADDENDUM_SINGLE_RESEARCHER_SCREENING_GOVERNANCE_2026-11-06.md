# S0 Scoping Review Protocol Addendum — Single-Researcher Screening and Supervisor Consultation

**Decision date:** 2026-11-06  
**Researcher authorization:** User stated: "I will do and my supervisor will validate but it will be to considate not to approve : the approvement should be from me 100% and from the feedback I will validate"; subsequently directed "let go."  
**Authority status:** Researcher-adopted operational change. Does not assert supervisor or institutional approval. This addendum records a deviation from the previously researcher-approved two-independent-reviewer design; original protocol v0.3 is preserved without edits.

## 1. Authority and roles

- **Thesis researcher:** Sole human screener for S0 validation; determines initial eligibility classifications, assesses supervisory feedback, and holds final decision authority over research analysis and classifications, subject to any binding university requirements.
- **Thesis supervisor:** Scientific adviser providing methodological critique, consistency checking and recommendations. Feedback is not automatically accepted. The researcher records acceptance, modification or rejection of each substantive suggestion with reasons.
- **AI research assistant:** Prepares materials and performs reproducible numerical calculations and data-quality audits. AI decisions **do not count as independent human screening** and must never be copied into human-decision fields as if performed by a person.
- **Institutional distinction:** Researcher control over research decisions does not waive formal supervisor, committee or university sign-off requirements for thesis submission/defense, if applicable.

## 2. Superseded reviewer requirement

This addendum **replaces only the reviewer-count, dual-independent-reviewer screening, reviewer agreement and adjudication workflow in §4 of** `SLR_PROTOCOL_V0_3_RESEARCHER_APPROVED_2026-11-05.md` for the S0 pilot and, unless later amended, the subsequent screening process. All SO1–SO3 objectives, eligibility codes I1–I6/E01–E07, search provenance rules, seed-candidate checks and core/supporting/context evidence boundaries remain in effect. Screening is now **single-researcher with supervisor consultation**, not dual independent. Explicitly disclose heightened selection/misclassification bias and resulting limitation. **Do not claim two-reviewer JBI methodological conformity, reviewer consensus, inter-rater agreement or Cohen's kappa** for this single-person process.

## 3. Inputs

- Original Scopus integrated S0 query: 5,662 unique S0 EIDs in original 45-field export, with query text and native count corroborated in prior records. Exact native search timestamp and active refinements remain to be archived.
- **100-record random-sample source CSV**: `S0_RANDOM100_FULL_45_FIELDS.csv` (original Drive link: https://drive.google.com/file/d/1FfHtZufQ7YM6-Mp4Y7LBpiwtED3qQP7m/view). All 100 EIDs are unique and abstracts are populated; 93 DOIs populated and 7 omitted in source. It includes `sample_id` S0-CAL-001…100, original S0 row position, and original S0 SHA-256 `4e2bfdb7d38759f3e7b6d12e1b2ea1244e7263c1901a713db1d1048640bdde50`. The random number generator/seed and implementation must be verified independently before asserting fully reproducible selection.
- **100 records are distinct from** an additional 30 targeted S0 noise/stress-test records. Never combine targeted 30 with the unbiased precision denominator.
- A local blank-screening workbook prepared from the 100-record CSV: `S0_Single_Researcher_Screening_100.xlsx` in conversation artifacts, with `START HERE`, `SCREEN 100`, `SUPERVISOR FEEDBACK`, `RESULTS`. This workbook is researcher worksheet only and must not be represented as completed human screening.

## 4. Execution

1. **Confirm provenance:** Inspect original 5,662-row S0 CSV and the 100 selected original row positions/EIDs; verify the original seed and simple-random-without-replacement procedure, and archive the extraction script or selection manifest. Preserve source files and original record ordering.
2. **Use the eligibility codebook:** Retain I1–I6 / E01–E07 definitions and decide the exact threshold for CORE vs SUPPORTING and CONTEXT role. Log treatment of retractions, conference reviews, missing full text, languages and duplicate works.
3. **Individually screen each of 100 records:** Researcher reads full title, abstract and indexed keywords, records a singular one of `INCLUDE_CORE`, `INCLUDE_SUPPORTING`, `INCLUDE_CONTEXT`, `EXCLUDE`, `UNCLEAR`; codes relevant SO1/SO2/SO3, reason, and full-text retrieval need. A keyword match alone never justifies inclusion or exclusion; record enough evidence to audit each choice.
4. **Complete unclear cases:** Retrieve original text/abstract/full text when possible. Use `UNCLEAR` and documented retrieval steps when unresolved; do not force an unsupported include/exclude.
5. **Supervisor consultation (advisory):** Supervisor may audit exclusions/unclear cases and methods, suggest category changes or stricter controls. Preserve comments and initial researcher screening.
6. **Researcher adjudication:** Researcher records for each substantive feedback item: accept / modify / decline with scientific reasons, date and final researcher category. Feedback does not silently overwrite initial decision.
7. **Quantify S0 relevance:** Tabulate mutually exclusive Core, Supporting, Context, Exclude, Unclear. Define primary technical-relevance estimator `(CORE+SUPPORTING)/100`; separately broader estimator `(CORE+SUPPORTING+CONTEXT)/100`, with appropriate confidence interval and unresolved-case sensitivity analysis. This estimates within-S0 relevance/precision, **not search recall**. Cannot compute independent-reviewer agreement.
8. **Assess additional evidence:** Evaluate 30 deliberately targeted noise records separately; test retrieval of known relevant seed papers, especially strongest coupled thermal comparators; confirm A0–F1 complementing S0; retain original native query/log details.
9. **Researcher decision:** Researcher records `ACCEPT_S0_v0.1`, `REVISE_S0_v0.2`, or `REJECT_S0_AS_PRIMARY` with scientific rationale and dated decision. This does not establish institutional/supervisor sign-off. If revised, run a new native query, preserve earlier exports and report both search versions.

## 5. Completion gate and reporting

**Current status at creation:** 100-record source structure verified; screening workbook created with **zero** recorded human screening decisions; no supervisor feedback or completed search-freeze decision reported.

The report must explicitly state:

> "The initial S0 search-quality sample was screened by one thesis researcher using predefined criteria. The supervisor was invited to provide scientific feedback; the researcher assessed and documented responses to feedback and retained final research decision authority. No independent second human reviewer screened the complete sample. This limits inter-rater verification and may increase screening selection bias."

The eventual JBI-informed scoping review must declare the single-screener deviation transparently; do not describe it as a completed dual-reviewer JBI-compliant systematic screening process.

## 6. Preserved primary sources

- `SLR_PROTOCOL_V0_3_RESEARCHER_APPROVED_2026-11-05.md`
- `SCOPUS_S0_PREFREEZE_NATIVE_AND_HUMAN_VALIDATION_DECISION_2026-11-05.md`
- Original S0 and A0–F1 search exports and provenance.
