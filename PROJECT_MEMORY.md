# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![Prereg](https://img.shields.io/badge/H1%20confirmatory%20design-FROZEN-1A7F37)
![Validation](https://img.shields.io/badge/NYC%2FACN-PARTIAL%20PASS-9A6700)
![Raw Completeness](https://img.shields.io/badge/raw%20completeness-STRUCTURAL%20PASS-9A6700)
![Row Audit](https://img.shields.io/badge/acquisition%20plan-FROZEN-0969DA)
![Audit Code](https://img.shields.io/badge/offline%20tests-4%2F4%20PASS-1A7F37)
![Raw Retrieval](https://img.shields.io/badge/event%20rows-PENDING-B42318)
![Split](https://img.shields.io/badge/train%2Ftest-CANDIDATE%20ONLY-B42318)
![H1b](https://img.shields.io/badge/full%20public%20H1b-BLOCKED-B42318)

## Repository authority — updated 2026-09-14

The sole active repository is `Dossiya-SE/MSE-thesis`. Thesis-wide citation standard: APA 7. Canonical reasoning protocol: `project/RESEARCH_REASONING_PROTOCOL.md`. Canonical execution method: `project/EGMIV_METHOD_V1.md`.

## Active H1 authority

1. `project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`
2. `project/H1_CONFIRMATORY_PREREGISTRATION_V1.md`
3. `project/H1_THRESHOLD_PROVENANCE_V1.md`
4. `project/H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md`
5. `project/H1_DEMONSTRATOR_QUALIFICATION_V1.md`
6. `project/H1_RAW_COMPLETENESS_AUDIT_V1.md`
7. `project/H1_ROW_LEVEL_DATA_QUALIFICATION_STATUS_V1.md` — **current data gate**
8. `evidence/H1/09_row_level_v1/` — frozen executable acquisition/audit protocol
9. `models/H1/M0/`, `models/H1/M1/`, `models/H1/M2/`
10. `project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`

## Canonical H1 model state

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C,
```

```math
\boxed{M_0=\text{independent},\qquad M_1=\text{static/algebraic coupling},\qquad M_2=\text{dynamic causal coupling}.}
```

Verification:
- M0: 13/13 passed.
- M1: 13/13 M1-specific passed.
- M2: 29/29 full M1+M2 regression passed.

Nested limits:

```math
M_1\rightarrow M_0,
\qquad
M_2\rightarrow M_1.
```

All benchmark effect sizes remain verification-only and `BENCHMARK_TEST_HARNESS_ONLY`.

## H1 confirmatory design — frozen

Primary H1a comparison is **M2 vs M1**. M2 vs M0 is secondary.

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

Thresholds may not be selected from observed M2−M1 effects.

Frozen numerical floors for minimal-demonstrator v1:

```math
\boxed{u_{num,P}=0.000416667,\qquad u_{num,T}=0.001281963}
```

at

```math
\boxed{\Delta t=0.00125\;\mathrm{h}=4.5\;\mathrm{s}}.
```

Observation and engineering thresholds remain case/data dependent:

```math
\boxed{\epsilon_P\;\text{NOT YET FROZEN},\quad\epsilon_T\;\text{NOT YET FROZEN},\quad\epsilon_{pred}\;\text{NOT YET COMPUTABLE}.}
```

## Qualified public demonstrator

```math
\boxed{\mathcal D_{H1}^{public}=\mathcal D_{NYC}\cup\mathcal D_{ACN}}
```

with status **PARTIAL PASS**.

NYC system-arm sources: NYISO P-58B, EAGLE-I, TLC HVFHV, DOT Traffic Speeds, NYC 311 and Con Edison/NY DPS event records. ACN is restricted to charging-component validation and is not same-event NYC system truth.

Full-public-H1b gaps remain: no public geolocated crew/job trajectories; aggregate NYISO Zone-J geography does not exactly match fine TLC/DOT geography; EAGLE customer-outage fraction is not identical to demand-weighted `S_P`; and public trip records do not enumerate all latent/unserved mobility requests.

## Candidate event family

- E0 — Tropical Storm Fay, 2020-07-10;
- E1 — Tropical Storm Isaias, 2020-08-04 onward;
- E2 — Dec 2022 wind/rain storm;
- E3 — Dec 2023 wind/rain storm;
- E4 — Apr 2024 coastal wind/rain storm.

A non-adaptive candidate split, recorded before model-result inspection, is:

```math
\boxed{D_{train}^{cand}=\{E0,E2\},\qquad D_{test}^{cand}=\{E1,E3,E4\}.}
```

This split is **not frozen**.

## Raw-completeness audit

The source-level audit is a PARTIAL / STRUCTURAL PASS. Key safeguards remain:

1. absent EAGLE-I county-time rows are never equated with zero outage;
2. TLC completed HVFHV trips are never equated with the entire requested-demand population;
3. DOT link speeds are road-state observations, not OD-demand truth;
4. 311 is supporting/reporting evidence, not a complete obstruction inventory;
5. publisher quality caveats remain part of uncertainty;
6. public Con Edison/DPS reports provide event/restoration truth but not individual crew-route/job trajectories.

## Row-level acquisition/audit executor — current gate

Executable package:

`evidence/H1/09_row_level_v1/`

Frozen items:
- E0–E4 audit windows and candidate roles;
- source endpoint/file templates;
- required native fields and timezone rules;
- NYC EAGLE-I county FIPS set;
- frozen 311 obstruction vocabulary;
- deterministic row-level metrics;
- missingness interpretation rules;
- provenance hashing.

The executor computes, where raw data are retrievable:

```math
N_{rows},\quad t_{min},\quad t_{max},\quad
\Delta t_{median},\quad \Delta t_{95},\quad \Delta t_{max},\quad
r_{null},\quad r_{dup}
```

plus rule flags and raw-file SHA-256 hashes.

Offline audit-code verification:

```text
4/4 offline audit tests passed
```

The tests cover timestamp/gap computation, duplicate detection, required-field failure and the EAGLE-I `missing != zero` gate.

### Retrieval state

Actual event-window row counts/null rates are **not yet claimed**. The current chat runtime cannot retrieve the large ZIP/Parquet/raw bodies required for the full audit. This is an acquisition block, not a scientific PASS.

Therefore:

```math
\boxed{\text{ACQUISITION PLAN = FROZEN}}
```

```math
\boxed{\text{AUDIT CODE = VERIFIED OFFLINE}}
```

```math
\boxed{\text{RAW ROW-LEVEL QUALIFICATION = PENDING}}
```

and

```math
\boxed{D_{train},D_{test}\text{ remain UNFROZEN}.}
```

## R1–R8 activation rule

The candidate split may activate only when every required event/source role passes the predeclared row-level gates:
- R1 timestamp/timezone integrity;
- R2 pre-event/impact/recovery support;
- R3 missingness interpretability;
- R4 declared spatial support;
- R5 native quantity/units validity;
- R6 no held-out repair using model residuals;
- R7 publisher quality flags retained;
- R8 non-adaptive exclusion.

No held-out event may move into training because model performance is poor.

## Full H1b status

```math
\boxed{\textbf{BLOCKED WITH PUBLIC DATA AT THE STRONGEST PRE-REGISTERED LEVEL}}.
```

This does not block H1a matched representation testing, aggregate/event validation, road-state validation or charging-component validation once the data gates are passed.

## Formal evidence status

Authenticated Scopus, Web of Science Core Collection, Compendex and IEEE Xplore execution of the frozen H1 CORE search remains pending. Public evidence remains supportive/provisional and cannot replace the formal corpus.

## Immediate next task

```math
\boxed{\text{execute frozen raw-data acquisition}\rightarrow\text{row metrics}\rightarrow R1{:}R8\rightarrow\textbf{freeze or reject candidate split}.}
```

No calibration, UQ or confirmatory H1 run is authorized before this gate passes.