# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![Prereg](https://img.shields.io/badge/H1%20confirmatory%20design-FROZEN-1A7F37)
![Validation](https://img.shields.io/badge/NYC%2FACN-PARTIAL%20PASS-9A6700)
![Raw Completeness](https://img.shields.io/badge/raw%20completeness-STRUCTURAL%20PASS-9A6700)
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
6. `project/H1_RAW_COMPLETENESS_AUDIT_V1.md` — **current public-data gate**
7. `models/H1/M0/`, `models/H1/M1/`, `models/H1/M2/`
8. `evidence/H1/08_demonstrator/`
9. `project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`

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

Primary H1a comparison: **M2 vs M1**. M2 vs M0 is secondary.

```math
\Omega_H=\Omega_0\cup\Omega_C\cup\Omega_O\cup\Omega_R\cup\Omega_J\cup\Omega_D.
```

Primary statistic:

```math
D_{PT}^{2,1}(\omega)=\frac1T\int_0^T\left[\left(\frac{S_P^{M_2}-S_P^{M_1}}{\epsilon_P}\right)^2+\left(\frac{S_T^{M_2}-S_T^{M_1}}{\epsilon_T}\right)^2\right]^{1/2}dt,
```

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

Thresholds may not be selected from observed M2−M1 effects.

## Threshold provenance

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

## Validation-observation architecture — frozen structure

Power service must be reconstructed from interval served energy and independently validated counterfactual requested demand. Transportation service must use completed OD flow and independently validated requested OD demand. Missing telemetry is never silently equivalent to physical zero.

```math
\Delta_{val}\ge\max(\Delta_P^{obs},\Delta_T^{obs}).
```

No model value may be compared to field data before applying the same temporal/spatial observation operator.

## Demonstrator qualification

```math
\boxed{\mathcal D_{H1}^{public}=\mathcal D_{NYC}\cup\mathcal D_{ACN}}
```

with

```math
\boxed{\textbf{PARTIAL PASS}}.
```

### NYC system arm

Audited sources:
- NYISO P-58B Real-Time Actual Load;
- EAGLE-I county outage trajectories;
- NYC TLC trip records;
- NYC DOT Traffic Speeds;
- NYC 311;
- Con Edison / NY DPS event/restoration evidence.

This arm supports aggregate event/load/outage/restoration validation, TLC-subsystem completed OD behavior, road-state dynamics, obstruction evidence and restoration milestones.

Full-H1b gaps remain: no public geolocated crew/job trajectories; aggregate NYISO Zone-J geography does not exactly match fine TLC/DOT geography; EAGLE customer-outage fraction is not identical to demand-weighted `S_P`; and public trip records do not enumerate all latent/unserved mobility requests.

### ACN charging arm

ACN-Data is **PASS for component validation** subject to access-token registration, but is not NYC same-event system truth:

```math
\boxed{\text{ACN}\not\Rightarrow\text{system-level H1b validation}.}
```

## Candidate event family

- E0 — Tropical Storm Fay, 2020-07-10;
- E1 — Tropical Storm Isaias, 2020-08-04 onward;
- E2 — Dec 2022 wind/rain storm;
- E3 — Dec 2023 wind/rain storm;
- E4 — Apr 2024 coastal wind/rain storm.

## Raw-completeness audit — current

The source-level audit confirms event-period archives/schemas but also identifies intrinsic missingness limitations.

Key findings:

1. NYISO monthly archives exist for all candidate event months.
2. TLC publishes event-month HVFHV data, but TLC does not guarantee submitted-record completeness and gives a specific 2020 COVID-era submission caveat.
3. DOT Traffic Speeds supplies link-level speed/travel-time state, not OD demand.
4. NYC 311 is reporting-driven and cannot be treated as a complete obstruction inventory.
5. EAGLE-I omits zero-outage rows and explicitly does not distinguish true zero outage from a collection gap when a county-time row is absent.
6. EAGLE-I public data extend through 2024, but the peer-reviewed technical-validation characterization used here covers the 2014–2022 release; E3/E4 therefore retain an additional quality-provenance flag.
7. Official Con Edison/DPS reports provide strong event/restoration truth but not individual crew-route/job trajectories.

Therefore:

```math
\boxed{\textbf{RAW COMPLETENESS = PARTIAL / STRUCTURAL PASS}}
```

and the train/test split remains **unfrozen**.

A non-adaptive candidate split, recorded before model-result inspection, is:

```math
\boxed{D_{train}^{cand}=\{E0,E2\},\qquad D_{test}^{cand}=\{E1,E3,E4\}.}
```

This candidate activates only if event-window data pass the frozen R1–R8 row-level gates. Held-out events cannot move to training or be replaced because of model performance.

### Row-level R1–R8 gates

- R1 timestamp integrity and timezone;
- R2 pre-event/impact/recovery support;
- R3 missingness interpretability;
- R4 declared spatial support;
- R5 native quantity/units validity;
- R6 no held-out repair using model residuals;
- R7 publisher quality flags retained in uncertainty;
- R8 non-adaptive exclusion.

## Full H1b status

```math
\boxed{\textbf{BLOCKED WITH PUBLIC DATA AT THE STRONGEST PRE-REGISTERED LEVEL}}.
```

This does not block H1a matched representation testing, aggregate/event validation, road-state validation or charging-component validation.

To upgrade H1b, seek restricted/partner data for geolocated repair-job/crew logs, finer power-service/outage observations coextensive with transport geography, mobility request/completion truth and ideally event-linked EV charging observations.

## Formal evidence status

Authenticated Scopus, Web of Science Core Collection, Compendex and IEEE Xplore execution of the frozen H1 CORE search remains pending. Public evidence remains supportive/provisional and cannot replace the formal corpus.

## Immediate next task

```math
\boxed{\text{event-window row-level extraction}\rightarrow(N,t_{min},t_{max},\Delta t,\text{nulls},\text{duplicates},\text{spatial coverage})\rightarrow R1{:}R8\rightarrow\textbf{freeze or reject split}.}
```

No calibration or confirmatory H1 run is authorized before this gate passes.