# Thesis QA Tools

This folder contains deterministic repository-quality checks. These tools do not decide whether a scientific claim is true; they detect presentation, configuration and ontology inconsistencies that can be tested automatically.

## `thesis_display_lint.py`

The linter checks active thesis Markdown and authority files for:

- fenced ` ```math ` blocks that should be GitHub display math;
- `\tag{...}` use inside Markdown;
- legacy display delimiters;
- unbalanced `$$` blocks and code fences;
- malformed Markdown table column counts;
- stale P–W–T–SW / waste–drainage tokens in active authority/configuration paths;
- incorrect `MSc` degree wording in active thesis authority text;
- presence and integrity of P1–P10 and H1–H5 machine-readable registries;
- parseability of active JSON configuration/schema files.

Historical/provenance directories are intentionally excluded from ontology rewriting. The goal is to protect **active scientific authority** while preserving the history of earlier research stages.

## Continuous integration

`.github/workflows/scientific-architecture-qa.yml` runs the linter together with Python numerical tests, YAML/JSON checks, SVG validation and a Julia P–T–I–O smoke test.

A passing QA workflow means the repository satisfies these machine-checkable contracts. It does **not** mean the scientific model has been empirically validated.
