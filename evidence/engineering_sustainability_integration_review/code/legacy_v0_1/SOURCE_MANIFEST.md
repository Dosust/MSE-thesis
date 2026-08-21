# Legacy v0.1 Source Manifest

This manifest records the generated modular package state from the chat.

## Local generated binary artifacts and hashes

- `engineering_sustainability_review_modular_python.zip`
  - SHA-256: `7fd58ae60c7ffacad3069db15b403a870517c9d9460f4f612cc2840a76c36e45`
- `es_review_smoke_test.xlsx`
  - SHA-256: `4a55410e2d4e3970d00d8eea6b7c5c93053c3faf91dd154ccc2535a76127ba9b`

The GitHub connector used in this chat did not expose a generic local binary-upload action, so these hashes are retained for provenance while the critical text source is archived here.

## Original generated package file list

```text
README.md
pyproject.toml
tests.py
example_records.json
example_evidence_symbols.json
example_performance_mapping.json
example_outcome_mapping.json
es_review/__init__.py
es_review/cli.py
es_review/config.py
es_review/coverage.py
es_review/dictionaries.py
es_review/enums.py
es_review/io_json.py
es_review/mapping.py
es_review/models.py
es_review/pdf_io.py
es_review/pipeline.py
es_review/retrieval.py
es_review/rules.py
es_review/scoring.py
es_review/validation.py
es_review/workbook_builder.py
```

## QA state recorded in chat

- Python syntax compilation passed after patching.
- Synthetic perfect-vector self-test passed: `(3,3,3,3,3)`.
- 10-paper synthetic workbook smoke test created successfully.
- Formula error scan over the tested workbook range returned zero matches for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`.

## Superseded aspects

The v0.1 code should not be treated as the final implementation because later methodological refinements require:

- `AC` author causal/process formula-type state;
- multiple evidence rows per P/F/S/D domain;
- complete source passages rather than only summary rows;
- downstream derivation of matrices from the evidence dossier;
- explicit resolution of the mapping taxonomy conflict documented in the parent decision log.

The parent methodological specification overrides the legacy code whenever they differ.