# Configuration Contracts

This directory contains machine-readable configuration aligned with the frozen seven-stage P–T–I–O thesis framework.

| File | Purpose | Authority |
|---|---|---|
| `scientific_propositions.yaml` | P1–P10 supporting proposition registry | synchronized with `project/SCIENTIFIC_PROPOSITIONS.md` |
| `research_hypotheses.yaml` | H1–H5 primary hypothesis registry | synchronized with `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md` |
| `research_question_mapping_v4.json` | exact RQ0 + RQ1–RQ7 + SO1–SO7 machine mapping | `project/CANONICAL_RESEARCH_QUESTIONS_V4.md` + `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md` |
| `research_question_mapping_v3.json` | superseded v3 mapping | provenance only |
| `example_model.json` | valid illustrative P–T–I–O model configuration | validated against `schemas/thesis_model.schema.json` |
| `h3_houston_power_source_v1.json` | frozen H3 Houston SMART-DS source/version/year/scenario contract and geographic-selection gates | `project/H3_SMARTDS_YEAR_QUALIFICATION_V1.md` + `project/H3_SMARTDS_HOUSTON_PREEXTRACTION_V1.md` |
| `h3_houston_transport_source_v1.json` | frozen H3 H-GAC transport source family/base-year contract and Houston-selection gates | `project/H3_HGAC_TRANSPORT_SOURCE_AND_BASEYEAR_QUALIFICATION_V1.md` |
| `h3_houston_signal_source_v1.json` | frozen City of Houston traffic-signal source, P→T interface role, materialization and mapping gates | `project/H3_HOUSTON_TRAFFIC_SIGNAL_SOURCE_AND_MATERIALIZATION_V1.md` |

These files are contracts for software/reproducibility. They do not replace the human-readable canonical stage specifications.

## Synchronization rules

- $P,T$ remain physical systems; $I,O$ remain informational/organizational layers.
- RQ0 is overarching; exact RQ0/RQ1–RQ7 wording follows `project/CANONICAL_RESEARCH_QUESTIONS_V4.md`, and SO1–SO7/H1–H5 follow `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`.
- Primary hypothesis logic $H_1$–$H_5$ is frozen; numerical thresholds are not yet frozen.
- H4 tests heterogeneity in resource requirements, resource efficiencies, or admitted sustainability consequences among resilience-effective interventions; interface criticality is a supporting diagnostic, not H4 itself.
- H5 tests the joint engineering decision effect of resource efficiency, admitted sustainability consequences, feasibility, and uncertainty relative to resilience-only evaluation; adaptive transformation pathways are a supporting extension unless separately preregistered.
- The proposition registry contains $P_1$–$P_{10}$ as subordinate falsifiable claims.
- Stage-4 operational control uses $u(t)$.
- Stage-7 strategic transformation uses $\mathbf a_k$ and regime $\mathfrak M_k$.
- Historical P–W–T–SW/waste–drainage configuration must not reappear in active contracts.
- `h3_houston_power_source_v1.json` freezes SMART-DS v0.9 / 2016 / Full_Texas / base_timeseries as the primary semisynthetic H3 power-source contract, but it does not authorize Houston asset labeling until `G_{\Omega,QA}=1`.
- `h3_houston_transport_source_v1.json` freezes H-GAC 2025 Transportation Conformity with model base year 2023 as the primary semisynthetic H3 transportation source contract, but it does not authorize Houston link selection until `G_{\Omega,QA}=1` and raw C.1/C.3/C.4 bytes are inspected.
- `h3_houston_signal_source_v1.json` freezes City of Houston Public Works `Traffic Signal` layer 26 as the location source for the P→T interface. It does not assert real utility feeder assignments, feature-level backup power, or Houston-core membership until the respective gates close.

The GitHub scientific-architecture workflow validates these invariants automatically where implemented.
