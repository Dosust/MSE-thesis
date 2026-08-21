# Scope, Corpus, and Evidence Rules

## 1. Controlled corpus

The bio-inspired construction sustainability review must use the controlled Scopus workbook:

`scopus_export_bio-inspiration AND ( framework OR evaluation ) AND construction 8(1).xlsx`

A paper is eligible for substantive analysis only if it is present in that controlled corpus. The legacy coded/synthesis sheets are comparison/reference data, not primary evidence.

## 2. Focal-evidence rule

For each included paper:

- use the focal saved/admitted paper evidence;
- do not import evidence from another paper;
- do not treat cited-study results as focal-author results;
- do not promote literature-review/background mentions into implemented methods;
- do not infer missing values, units, page numbers, tool inputs, or analytical linkages;
- do not use general knowledge to fill evidence gaps;
- if the saved PDF is unavailable, use `PENDING_PDF`, `U`, `NR`, or `NA`.

## 3. Frozen research questions

### RQ1 — Assessment tool
What sustainability assessment method/tool is directly implemented by the focal authors?

### RQ2 — Tool inputs
What specific inputs are supplied to that method/tool, and where do those inputs originate?

### RQ3 — Engineering performance
What engineering/functional performance metrics are measured, calculated, simulated, or tested?

### RQ4 — Sustainability outcomes
What sustainability outcomes are generated, in which dimensions, and what specific indicators/values are reported?

### RQ5 — Engineering-to-sustainability connection
Which engineering-performance metrics actually become tool inputs, through what transformation, and with what resulting sustainability outcome?

## 4. Core distinctions

### Tool implementation
A method/tool is implemented only when the focal paper provides a study-specific operational chain such as:

`input -> procedure/model -> output`

A mention in the introduction, literature review, or references does not satisfy implementation.

### Engineering software vs sustainability assessment
Engineering simulation software is not automatically a sustainability assessment tool. For example, a daylighting, energy, structural, or thermal simulation may generate engineering/operational evidence without constituting a sustainability assessment method.

### Engineering result vs sustainability result
`engineering performance != sustainability outcome`

Examples of engineering evidence include load, displacement, thermal conductivity, heat flux, illuminance, residual indentation, durability, etc. A sustainability outcome must be generated within the declared sustainability assessment architecture and may be environmental, economic, social, or integrated.

### Arrow semantics
Use `->` only when analytical dependence is supported. Use parallel/coexistence when two evidence streams appear together but a transformation is not established.

## 5. Evidence states

- `SUPPORTED` — focal evidence directly supports the record.
- `NR` — investigated but not reported / no value located.
- `U` — unresolved or ambiguous.
- `NA` — genuinely not applicable.
- `PENDING_PDF` — claim/page/value cannot be closed until focal PDF verification.

## 6. Review states

- `FROZEN`
- `REVIEWED`
- `UNREVIEWED`
- `REQUIRES_PDF_CONFIRMATION`

## 7. Linkage states

- `L0`: no demonstrated connection.
- `L1`: engineering and sustainability evidence coexist/parallel.
- `L2`: engineering variable becomes an assessment input/modifier or otherwise directly affects the sustainability calculation/architecture.
- `L3`: integrated engineering+sustainability evidence explicitly drives ranking, selection, optimization, or another decision architecture.

Do not award a stronger linkage because a paper uses the word “integrated.” The focal evidence must establish the operation.

## 8. Validation levels

Validation target and validation level are separate.

Targets may include:
- bio-inspired mechanism;
- engineering performance;
- sustainability assessment;
- integrated architecture.

Levels:
- `No`
- `Applied`
- `Internal`
- `External`
- `U`

A case-study application is not automatically external validation.

## 9. Workflow invariant

`focal source -> raw evidence -> controlled classification -> interpretation -> cross-paper synthesis`

Never code the same fact independently in downstream synthesis tables.