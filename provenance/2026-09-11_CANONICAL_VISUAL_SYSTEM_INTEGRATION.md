# Canonical Visual System V00–V10 — Integration Record

**Date:** 2026-09-11  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Branch:** `main`  
**Visual registry:** `figures/canonical/README.md`  
**Document-integration commit:** `80029fd01c42272be1df4b2ca4f7cac607e80495`  
**Status:** INTEGRATED / SCIENTIFIC CONTENT PRESERVED

## Scope

The deterministic canonical visual family V00–V10 was integrated into its owning thesis documents. The integration changes **visual hierarchy and navigation only**; it does not redefine the frozen seven-stage scientific framework, the P–T–I–O ontology, the H1–H5 hypothesis logic, FTEE v2.0 evidence governance, or the minimal-sufficient-demonstrator methodology.

## Ownership map

| ID | Scientific owner |
|---|---|
| V00 | root `README.md`; `project/README.md` |
| V01 | `project/CANONICAL_SYSTEM_DEFINITION.md` |
| V02 | `project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md` |
| V03 | `project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md` |
| V04 | `project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md` |
| V05 | `project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md` |
| V06 | `project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md` |
| V07 | `project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md` |
| V08 | `project/RESEARCH_HYPOTHESES.md`; root/project dashboards |
| V09 | `project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`; root/project dashboards |
| V10 | `project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`; root dashboard |

## Scientific fidelity rule

Every embedded figure carries the statement that it is a **visual synopsis** and that the equations, definitions, evidence status and boundary rules in the owning Markdown document remain authoritative. This prevents compact SVG notation from silently replacing canonical mathematical notation.

The integration preserves the standing rule:

```math
\textbf{CHANGE THE VISUAL HIERARCHY, NOT THE SCIENTIFIC CONTENT.}
```

## Reproducibility

Placement is controlled by:

- `tools/integrate_canonical_visuals.py`
- `.github/workflows/canonical-visual-integration.yml`

The script is idempotent, checks insertion anchors explicitly, rejects missing anchors, and verifies exactly one visual marker for every required owner document.

## Current operational state

The visual integration does not change the evidence-workflow priority. The next scientific operation remains execution of the frozen H1 CORE v1 searches in Scopus, Web of Science Core Collection, Compendex and IEEE Xplore, followed by raw-corpus construction, deduplication and screening.
