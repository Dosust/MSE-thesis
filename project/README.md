# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207%20MANDATORY-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-v2.0-1A7F37)
![Reasoning](https://img.shields.io/badge/reasoning-v1.2-0969DA)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Traceability](https://img.shields.io/badge/v2%20audit-SYNC%20REQUIRED-9A6700)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![H1 Prereg](https://img.shields.io/badge/confirmatory%20design-FROZEN-1A7F37)
![Validation](https://img.shields.io/badge/NYC%2FACN-PARTIAL%20PASS-9A6700)
![Row Audit](https://img.shields.io/badge/executor-VERIFIED%204%2F4-1A7F37)
![Raw Retrieval](https://img.shields.io/badge/event%20rows-PENDING-B42318)
![Split](https://img.shields.io/badge/train%2Ftest-CANDIDATE%20ONLY-B42318)

This directory is the active scientific/mathematical specification of the MSE thesis. **Framework v2.0** is the current framework authority. H1 and H2 remain compatible with v2.0; H3–H5 require explicit versioned synchronization before new v2 confirmatory execution. The named execution method remains **EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method**.

> Reasoning protocol: [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md) — **v1.2; mandatory adjacent APA 7 author–date citation for externally sourced scientific claims**  
> Framework authority: [`CANONICAL_7_STAGE_FRAMEWORK_V2.md`](CANONICAL_7_STAGE_FRAMEWORK_V2.md)  
> v2 traceability audit: [`../thesis/00_governance/V2_TRACEABILITY_AUDIT_2026-09-16.md`](../thesis/00_governance/V2_TRACEABILITY_AUDIT_2026-09-16.md)  
> Execution method: [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md)  
> Evidence rule: public-support evidence may develop the method but cannot replace the formal confirmatory corpus.

## Current governance state

```math
\boxed{
\text{Framework v2.0}
\rightarrow
\text{traceability audit complete}
\rightarrow
\text{H3--H5 / outline / specification synchronization required}
\rightarrow
\text{preregistration}
\rightarrow
\text{confirmatory execution}.
}
```

The v2 audit requires one-to-one traceability:

```math
\boxed{
RQ_i
\rightarrow
SO_i
\rightarrow
H_i
\rightarrow
\text{metric}
\rightarrow
\text{experiment}
\rightarrow
\text{result}
\rightarrow
\text{engineering conclusion}.
}
```

No new H3–H5 confirmatory execution is authorized until the synchronization gate closes. Existing H1 execution controls are unchanged.

## Cross-cutting canonical requirements

| File | Role | Status |
|---|---|---|
| [`CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md`](CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md) | mandatory temporal–geospatial realization rule for spatially dependent P–T cascades, recovery and intervention | **FROZEN v1.0** |
| [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md) | canonical Learn → Verify → Formulate → Derive → Test → Validate → Synthesize → Advance protocol; includes citation-quality gate | **CURRENT v1.2** |
| [`../thesis/00_governance/V2_TRACEABILITY_AUDIT_2026-09-16.md`](../thesis/00_governance/V2_TRACEABILITY_AUDIT_2026-09-16.md) | RQ → objective → hypothesis → Stage-5 metric → experiment → chapter audit | **AUDIT COMPLETE / SYNC REQUIRED** |

The spatiotemporal requirement remains mandatory:

```math
\boxed{\text{Every modeled Power--Transportation cascade must preserve both time and location whenever the physical mechanism is spatially dependent.}}
```

The v2 resilience core is

```math
\boxed{
\text{Resilience}
=
\underbrace{\text{remain acceptable}}_{\text{viability}}
+
\underbrace{\text{return to acceptable operation}}_{\text{reachability}}
+
\underbrace{\text{quantify confidence}}_{\text{probability}},
}
```

where the plus signs denote conceptual composition, not scalar addition. Performance/recovery curves remain a benchmark; incremental engineering value must be tested rather than assumed.

## H1 authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`](H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md) | M0/M1/M2 physical specification | frozen |
| 2 | [`H1_CONFIRMATORY_PREREGISTRATION_V1.md`](H1_CONFIRMATORY_PREREGISTRATION_V1.md) | H1a/H1b design, UQ and decision gates | frozen |
| 3 | [`H1_THRESHOLD_PROVENANCE_V1.md`](H1_THRESHOLD_PROVENANCE_V1.md) | threshold provenance | partially frozen |
| 4 | [`H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md`](H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md) | observation/service requirement architecture | frozen structure |
| 5 | [`H1_DEMONSTRATOR_QUALIFICATION_V1.md`](H1_DEMONSTRATOR_QUALIFICATION_V1.md) | public demonstrator qualification | frozen v1 |
| 6 | [`H1_RAW_COMPLETENESS_AUDIT_V1.md`](H1_RAW_COMPLETENESS_AUDIT_V1.md) | source-level event-family completeness | structural pass |
| 7 | [`H1_ROW_LEVEL_DATA_QUALIFICATION_STATUS_V1.md`](H1_ROW_LEVEL_DATA_QUALIFICATION_STATUS_V1.md) | current raw-data execution state | **current gate** |
| 8 | [`../evidence/H1/09_row_level_v1/`](../evidence/H1/09_row_level_v1/) | frozen row-level acquisition/audit executor | code verified 4/4; raw retrieval pending |
| 9 | [`../models/H1/M0/`](../models/H1/M0/) | independent baseline | verified 13/13 |
| 10 | [`../models/H1/M1/`](../models/H1/M1/) | static/algebraic comparator | verified |
| 11 | [`../models/H1/M2/`](../models/H1/M2/) | dynamic causal comparator | verified full 29/29 regression |

## H1 model and confirmatory state

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic coupling},\quad M_2=\text{dynamic causal coupling}.}
```

with verified nested limits

```math
M_1\rightarrow M_0,
\qquad
M_2\rightarrow M_1.
```

The primary H1a comparison remains M2 vs M1:

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

Frozen numerical floors are

```math
\boxed{u_{num,P}=0.000416667,\qquad u_{num,T}=0.001281963}
```

at

```math
\boxed{\Delta t=0.00125\;\mathrm{h}=4.5\;\mathrm{s}}.
```

`epsilon_P`, `epsilon_T` and `epsilon_pred` remain unfrozen pending real observation uncertainty and service requirements.

## Public demonstrator and event family

```math
\boxed{\mathcal D_{H1}^{public}=\mathcal D_{NYC}\cup\mathcal D_{ACN}}
```

is a **PARTIAL PASS**. NYC supports aggregate/event, power-outage, completed-TLC-OD and road-state validation. ACN supports charging-component validation only. Full system-level H1b remains blocked with current public data.

Candidate events:

```text
E0  Tropical Storm Fay — 2020-07-10
E1  Tropical Storm Isaias — 2020-08-04 onward
E2  Dec-2022 wind/rain storm
E3  Dec-2023 wind/rain storm
E4  Apr-2024 coastal wind/rain storm
```

Non-adaptive candidate split:

```math
\boxed{D_{train}^{cand}=\{E0,E2\},\qquad D_{test}^{cand}=\{E1,E3,E4\}.}
```

This split is **not frozen**.

## Current gate: row-level data qualification

The executor at `evidence/H1/09_row_level_v1/` freezes:

- event windows and candidate roles;
- official source endpoints/files;
- required fields and timezone handling;
- EAGLE-I NYC FIPS filter;
- 311 obstruction vocabulary;
- row-count/timestamp/gap/null/duplicate metrics;
- raw-file provenance hashes;
- missingness and non-adaptation rules.

Offline verification reports:

```text
4/4 offline audit tests passed
```

Actual event-window row counts/null rates are **not yet claimed** because the required raw bodies have not completed the qualification gate. This is an acquisition block, not a PASS.

Therefore:

```math
\boxed{\text{ACQUISITION PLAN FROZEN}}
```

```math
\boxed{\text{AUDIT CODE VERIFIED OFFLINE}}
```

```math
\boxed{\text{RAW ROW-LEVEL GATE PENDING}}
```

No train/test freeze, calibration, UQ, H1a confirmatory run or H1b adjudication is authorized until the required event/source roles pass R1–R8.

## Immediate next governance task

Close the v2 synchronization gate in this order:

```math
\boxed{
\text{version H3--H5}
\rightarrow
\text{v2 RQ--SO--H traceability}
\rightarrow
\text{outline/specification synchronization}
\rightarrow
\text{abstract synchronization}
\rightarrow
\text{H3--H5 preregistration}.
}
```

The H1 row-level acquisition/qualification process continues independently under its frozen controls. Authenticated Scopus, Web of Science Core Collection, Compendex and IEEE Xplore execution of the formal H1 evidence search also remains pending before final H1 confirmation.