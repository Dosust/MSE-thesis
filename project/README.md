# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![H1 Prereg](https://img.shields.io/badge/confirmatory%20design-FROZEN-1A7F37)
![Validation](https://img.shields.io/badge/NYC%2FACN-PARTIAL%20PASS-9A6700)
![Row Audit](https://img.shields.io/badge/executor-VERIFIED%204%2F4-1A7F37)
![Raw Retrieval](https://img.shields.io/badge/event%20rows-PENDING-B42318)
![Split](https://img.shields.io/badge/train%2Ftest-CANDIDATE%20ONLY-B42318)

This directory is the active scientific/mathematical specification of the MSE thesis. The seven-stage framework and H1–H5 logic are frozen. The named execution method is **EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method**.

> Reasoning protocol: [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md)  
> Execution method: [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md)  
> Evidence rule: public-support evidence may develop the method but cannot replace the formal confirmatory corpus.

## Cross-cutting canonical requirements

| File | Role | Status |
|---|---|---|
| [`CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md`](CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md) | mandatory temporal–geospatial realization rule for spatially dependent P–T cascades, recovery and intervention | **FROZEN v1.0** |

The spatiotemporal requirement supplements the frozen seven-stage framework without changing its sequence or the canonical dependency primitive. Its governing rule is:

```math
\boxed{\text{Every modeled Power--Transportation cascade must preserve both time and location whenever the physical mechanism is spatially dependent.}}
```

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

The tests cover timestamp/gap computation, duplicate detection, missing-required-field failure and the EAGLE-I rule that an absent record is not automatically zero outage.

Actual event-window row counts/null rates are **not yet claimed** because the current chat runtime cannot retrieve the required large ZIP/Parquet/raw bodies. This is an acquisition block, not a PASS.

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

## Immediate next step

```math
\boxed{\text{execute frozen acquisition}\rightarrow(N,t_{min},t_{max},\Delta t,\text{nulls},\text{duplicates},\text{coverage})\rightarrow R1{:}R8\rightarrow\textbf{freeze or reject split}.}
```

Authenticated Scopus, Web of Science Core Collection, Compendex and IEEE Xplore execution of the formal H1 evidence search also remains pending before final H1 confirmation.