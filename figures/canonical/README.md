# Canonical Thesis Visual System

![Status](https://img.shields.io/badge/visual%20family-V00--V10-0969DA)
![Scientific Authority](https://img.shields.io/badge/content-frozen%20framework%20aligned-1A7F37)
![Format](https://img.shields.io/badge/format-deterministic%20SVG-8250DF)

This directory contains the canonical visual family for the MSE thesis. Each figure is a **visual synopsis** of an authoritative scientific document. The equations and definitions in the owning Markdown document remain the mathematical authority whenever a compact visual label is necessarily shorter than the canonical notation.

## Placement registry

| ID | Canonical SVG | Owning scientific document | Function |
|---|---|---|---|
| **V00** | [`00_master_seven_stage_architecture.svg`](00_master_seven_stage_architecture.svg) | root `README.md`, `project/README.md` | whole-thesis seven-stage architecture |
| **V01** | [`01_multilayer_PTIO_system.svg`](01_multilayer_PTIO_system.svg) | `project/CANONICAL_SYSTEM_DEFINITION.md` | P–T–I–O ontology and multilayer system identity |
| **V02** | [`02_causal_interdependency_object.svg`](02_causal_interdependency_object.svg) | `project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md` | causal interdependency object and directed scope |
| **V03** | [`03_hybrid_multiscale_dynamics.svg`](03_hybrid_multiscale_dynamics.svg) | `project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md` | hybrid, delayed, event-driven, multiscale propagation |
| **V04** | [`04_observation_organization_control.svg`](04_observation_organization_control.svg) | `project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md` | observation–information–organization–control loop |
| **V05** | [`05_controlled_viability_geometry.svg`](05_controlled_viability_geometry.svg) | `project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md` | acceptability vs controlled maintainability |
| **V06** | [`06_resilience_sustainability_interface.svg`](06_resilience_sustainability_interface.svg) | `project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md` | WHY/WHAT/HOW-DEEP transformation diagnosis |
| **V07** | [`07_transformation_pathways.svg`](07_transformation_pathways.svg) | `project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md` | graph of regimes, adaptive actions and target-regime reachability |
| **V08** | [`08_hypothesis_test_architecture.svg`](08_hypothesis_test_architecture.svg) | `project/RESEARCH_HYPOTHESES.md` | H1–H5 confirmatory architecture |
| **V09** | [`09_FTEE_evidence_pipeline.svg`](09_FTEE_evidence_pipeline.svg) | `project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md` | de novo search → eligibility → FTEE → model qualification |
| **V10** | [`10_minimal_experimental_realization.svg`](10_minimal_experimental_realization.svg) | `project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md` | minimal sufficient P–T–I–O demonstrator concept |

## Fidelity rules

1. **Scientific ownership:** every figure is subordinate to its owning canonical Markdown document.
2. **No silent scientific edits:** changing visual content that changes meaning requires a versioned scientific revision first.
3. **Notation separation:** Stage-4 operational control $u(t)$, Stage-7 strategic action $a_k$, and Stage-2 activation $a_{ij}$ must remain distinct.
4. **Ontology lock:** $P,T$ are physical infrastructure systems; $I,O$ are informational and organizational layers.
5. **Evidence status:** visual compression does not convert a proposed `[P]` construct into established evidence.
6. **Rendering:** deterministic SVG is preferred for conceptual architecture; numerical/computed figures will use Python/Julia/TikZ as appropriate.
7. **Accessibility:** color is not the sole information carrier; labels, line patterns, shapes and captions carry meaning independently.

## Visual grammar

| Semantic object | Primary visual role |
|---|---|
| $P$ | power-system structure/dynamics |
| $T$ | transportation-system structure/dynamics |
| $I$ | information/observation |
| $O$ | organization/coordination |
| viability | feasible-maintainability geometry |
| hazard/violation | disruption, loss or invalidity |
| strategic transformation | regime-level structural change |

The visual family is designed so that

```math
V_{00}
\rightarrow
\{V_{01},\ldots,V_{07}\}
\rightarrow
\{V_{08},V_{09},V_{10}\},
```

meaning that V00 supplies the common hierarchy and visual grammar, V01–V07 are stage-level scientific zooms, and V08–V10 describe testing, evidence and experimental realization.
