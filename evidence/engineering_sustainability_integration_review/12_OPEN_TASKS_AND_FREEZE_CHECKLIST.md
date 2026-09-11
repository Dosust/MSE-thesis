# Open Tasks and Freeze Checklist

This file records what remains to be done before the Top-10 evidence system should be considered final.

## A. Methodology items to resolve before freeze

1. Resolve the mapping taxonomy conflict between `LCSA + outranking` and `Hybrid MCDM`.
2. Freeze the full framework/method/output taxonomies, including zero-coverage categories.
3. Freeze the `AF / AC / RR / NF` formula/architecture coding in code and schemas.
4. Freeze method-family essential-component sets used for R2.
5. Confirm the exact rule distinguishing `Applied`, `Internal`, and `External` validation.
6. Freeze the arrow semantics: `→` only for verified analytical dependence; `||` for parallel evidence.

## B. Evidence dossier construction for the 10 papers

For each paper:

- verify PDF identity against DOI/title/authors;
- extract complete K/L/M supporting passages;
- extract complete N–T supporting passages;
- extract all relevant P engineering records;
- extract all candidate/confirmed F integration records with preceding/following context;
- extract all quantified S sustainability outputs separately;
- extract all D decision/ranking/optimization records;
- extract method architecture/R2 components explicitly;
- extract validation evidence;
- extract T/backward-snowballing methods/tools;
- retain page/section/table/figure/equation locations.

Do not summarize away the source evidence.

## C. Interpretation and scoring

Only after evidence extraction:

- construct N–T summaries;
- assign PFSD chains;
- assign R1–R4/lambda from evidence;
- run fail-closed consistency checks;
- derive perfect/Tier-A status;
- document any disagreement or ambiguity as `U` rather than forcing a maximum score.

## D. Derived comparative tables

Once the evidence layer is frozen:

- regenerate the K–T summary sheet;
- regenerate PFSD detailed synthesis;
- regenerate narrative Table 1;
- regenerate visual evidence matrix from evidence classifications;
- regenerate mapping matrices from paper-level PFSD records;
- calculate coverage/mapping formulas automatically;
- ensure zero categories remain visible.

## E. Quality assurance

Before final export:

- check 10 unique Paper IDs and 10 unique DOIs;
- check no unsupported paper-specific claim is exported;
- check no `R3=3` lacks author-generated engineering evidence;
- check no `R4=3` lacks method-generated sustainability output;
- check no `lambda>0` lacks traceable alternative correspondence;
- check no `lambda=3` lacks author-integrated F3 evidence;
- check no `R2=3` has missing/partial required components;
- check all perfect labels equal exact `(3,3,3,3,3)`;
- scan workbook for formula errors;
- verify normalized coverage/mapping values are within `[0,1]`;
- clean truncated evidence snippets to complete sentences/paragraphs.

## F. Code v0.2

Update the legacy Python scaffold to:

- relational evidence tables;
- `AC` formula type;
- complete passage extraction support;
- evidence IDs linking raw passages to interpretations/scores;
- deterministic derivation of downstream matrices;
- explicit source-of-truth hierarchy;
- schema validation for all evidence states;
- tests for the corrected taxonomies and mapping rules.

## G. Binary artifact preservation

The text methodology and key legacy source are now in GitHub. Binary XLSX/PDF/ZIP artifacts remain outside this text-only GitHub connector workflow. Commit them separately if a binary-upload-capable workflow becomes available, using the recorded filenames and hashes where available.

## Freeze criterion

The framework is ready to freeze only when:

```math
\boxed{Definitions\ frozen + Evidence\ extracted + Interpretations\ traceable + Code\ consistent + Derived\ matrices\ deterministic}
```

The target is not “all cells filled”; the target is that every exported substantive claim is explicitly supported.