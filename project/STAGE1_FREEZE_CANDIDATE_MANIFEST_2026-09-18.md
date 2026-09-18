> **STATUS: SUPERSEDED — RETAINED FOR PROVENANCE.**
> Active Stage-1 authority is `STAGE1_FREEZE_MANIFEST_V2_2026-09-18.md`.
> Do not use this file for new Stage-1 scientific, mathematical, schema, or freeze decisions.
# Stage 1 Freeze-Candidate Manifest — 2026-09-18

**Status:** READY FOR FREEZE — NEW EVIDENCE INTEGRATED — NOT YET FROZEN  
**Scope:** generic Stage-1 framework only; case-specific instantiations excluded

## Freeze candidate statement

```math
\boxed{
G_1^{\rm framework}
=
\mathrm{PASS\ —\ READY\ FOR\ FREEZE}.
}
```

The new literature synthesis has been integrated before freeze. The exact repository blobs below now constitute the Stage-1 freeze candidate.

| Artifact | Blob SHA |
|---|---|
| `project/STAGE1_FINAL_FRAMEWORK_V1.md` | `be43670289f69d0a659cdf712f057a61fd6157c6` |
| `project/STAGE1_EVIDENCE_AND_ONTOLOGY_REGISTER_V1.md` | `cf03417dc4dab917e7e32758a2f83f65944757ce` |
| `project/STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V1.md` | `7ad5fc08b9195aa10af1aea6b3270ef0ea1397f5` |
| `project/STAGE1_DATA_ABSTRACTION_AND_INGESTION_STANDARD_V1.md` | `2db9360b375d28c29c03ee7064416836caecea11` |
| `project/STAGE1_GENERIC_FIXTURE_VERIFICATION_REPORT_2026-09-18.md` | `def6178742d4bca3f4616267a23a0838b555b187` |
| `project/STAGE1_EXIT_GATE_AUDIT_2026-09-18.md` | `9970b2e128ba9d03367a889c6b30e81bac1dc924` |
| `schemas/stage1_structure.schema.json` | `c511ad82be39e05210463438b42a665b196d7f6c` |
| `schemas/stage1_source_manifest.schema.json` | `af70743a9487f69f38f323a29d6bfdf853be027c` |
| `methods/stage1_data/adapter_contract.py` | `cdab216ef303f857026a9bfb15dafff5908524ef` |
| `methods/stage1_data/normalization.py` | `2cdbc0900a26472fb82dd55429be41a9a7e7707e` |
| `tests/stage1_data/test_stage1_framework.py` | `36489809ca3ea9c1cbe613cb05715fd1606d834c` |
| `tests/stage1_data/fixtures/source_manifests.json` | `028eefd15d095b7b4d8fcf0a54f10fb6f2a84a0f` |
| `tests/stage1_data/fixtures/stage1_structure_valid.json` | `dbd038bcfb8343aa713ff221a2dd32b6573bf83a` |
| `.github/workflows/stage1-framework-verification.yml` | `d0a87090897b9dd60be98051e5cc95d7bb69a36d` |

## New-evidence additions now inside the freeze candidate

The freeze candidate now explicitly contains:

- semantic entity object `E_i^alpha` rather than anonymous vertices;
- typed Stage-1 relation object `mathfrak R_ij^(1)`;
- interface semantics and exchanged function/service/resource/information semantics;
- candidate mechanism/context descriptors that remain pre-causal;
- entity and relation modeling resolution;
- evidence/provenance references and evidence-confidence representation;
- machine-enforced separation of dependency existence/status, coupling strength and evidence confidence;
- machine-enforced `strength_status=NOT_ESTIMATED_STAGE1`;
- distinction between known/standardized interface and verified case-specific connection;
- direct semantic fixtures for P→T signal power and T→P repair access;
- literature-to-mathematics traceability through `STAGE1_EVIDENCE_AND_ONTOLOGY_REGISTER_V1.md`.

## Verification status

```math
\boxed{
42/42\ \text{exact repository invariant checks}=\mathrm{PASS}
}
```

```math
\boxed{
19/19\ \text{controlled behavioral checks}=\mathrm{PASS}.
}
```

The repository Python suite now contains 26 generic Stage-1 tests. GitHub-hosted Actions remains `BLOCKED-ENVIRONMENT` because the hosted job obtains runner ID `0` and executes zero steps; this is not classified as a test failure.

## Freeze effect if approved

Freezing Stage 1 will freeze the generic scientific, evidence-ontology, mathematical, data-contract and machine-schema meaning represented by the blob SHAs above.

It will **not** freeze:

- Austin, Greensboro, Singapore or another case dataset;
- case-specific entity inventories;
- case crosswalks;
- case-specific provenance or QA outcomes;
- `G_1^{case}(c)` results;
- Stage-2 accepted causal dependencies;
- Stage-3 dynamic coupling laws or strengths.

Case-specific work may continue under the frozen framework.

Any later semantic change to the Stage-1 entity object, `Gamma^str`, `mathfrak R_ij^(1)`, relation-status logic, existence/strength/confidence separation, normative/causal separation, CIR semantics, source schema, structural schema or framework verification obligations requires an explicit Stage-1 amendment or unfreeze.

Formatting, references, comments, documentation links and nonsemantic software refactoring may be maintained under controlled change so long as the frozen scientific and machine-contract meaning is unchanged.