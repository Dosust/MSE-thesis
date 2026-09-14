# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![Prereg](https://img.shields.io/badge/H1%20confirmatory%20design-FROZEN-1A7F37)
![Validation](https://img.shields.io/badge/NYC%2FACN-PARTIAL%20PASS-9A6700)
![H1b](https://img.shields.io/badge/full%20public%20H1b-BLOCKED-B42318)

## Repository authority — updated 2026-09-14

The sole active repository is `Dossiya-SE/MSE-thesis`. Thesis-wide citation standard: APA 7. Canonical reasoning protocol: `project/RESEARCH_REASONING_PROTOCOL.md`. Canonical execution method: `project/EGMIV_METHOD_V1.md`.

## Active H1 authority

1. `project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`
2. `project/H1_CONFIRMATORY_PREREGISTRATION_V1.md`
3. `project/H1_THRESHOLD_PROVENANCE_V1.md`
4. `project/H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md`
5. `project/H1_DEMONSTRATOR_QUALIFICATION_V1.md` — **current demonstrator authority**
6. `models/H1/M0/`, `models/H1/M1/`, `models/H1/M2/`
7. `evidence/H1/08_demonstrator/`
8. `project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`

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

A common observation clock must satisfy

```math
\Delta_{val}\ge\max(\Delta_P^{obs},\Delta_T^{obs}).
```

No model value may be compared to field data before applying the same temporal/spatial observation operator.

## Demonstrator qualification — current

The public H1 demonstrator is now

```math
\boxed{\mathcal D_{H1}^{public}=\mathcal D_{NYC}\cup\mathcal D_{ACN}}
```

with qualification

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
- Con Edison / NY DPS storm and restoration evidence.

For Tropical Storm Isaias the structural temporal-overlap gate passes. Candidate validation clock: 15 minutes, pending raw timestamp inspection.

The arm is admissible for aggregate event/load/outage/restoration validation, TLC-subsystem completed OD behavior, road-state dynamics, obstruction evidence and restoration milestones.

The following full-H1b gaps remain:
1. no verified public geolocated crew/job trajectory dataset;
2. NYISO Zone J aggregate is not exactly coextensive with fine TLC/DOT geography and parts of the upper Bronx lie in Zone I;
3. EAGLE customer-outage fraction is not identical to demand-weighted `S_P`;
4. public TLC trip data do not directly enumerate all latent/unserved/cancelled mobility requests.

Thus microscopic road→crew→repair validation and exact fine-scale P–T co-validation are not supported by the audited public data.

### ACN charging arm

ACN-Data is **PASS for component validation**, subject to registration/token access. It provides charging-session timing, delivered energy, measured-current/pilot time series and optional user-request information.

It may validate charging-interface physics/parameters but is not a NYC same-event system dataset:

```math
\boxed{\text{ACN}\not\Rightarrow\text{system-level H1b validation}.}
```

## Candidate event family

Current wind/tree mechanism candidates:
- E0 — Tropical Storm Fay, 2020-07-10;
- E1 — Tropical Storm Isaias, 2020-08-04 to 2020-08-12;
- E2 — Dec 2022 wind/rain storm;
- E3 — Dec 2023 wind/rain storm;
- E4 — Apr 2024 coastal wind/rain storm.

Train/test membership is **not frozen**. It must be determined only after raw completeness, missingness and observation coverage are quantified for E0–E4.

Required rule:

```math
D_{train}\cap D_{test}=\varnothing,
```

with at least two independent held-out validation events for each mechanism class claimed confirmatory.

## Full H1b status

```math
\boxed{\textbf{BLOCKED WITH PUBLIC DATA AT THE STRONGEST PRE-REGISTERED LEVEL}}.
```

This does not block H1a matched representation testing, aggregate/event validation, road-state validation or charging-component validation.

To upgrade H1b, seek restricted/partner data for:
- geolocated repair-job/crew logs with timestamps;
- finer power-service/outage observations coextensive with the transport domain;
- mobility request/completion truth;
- event-linked EV charging data if charging is claimed at system-event scale.

## Formal evidence status

Authenticated Scopus, Web of Science Core Collection, Compendex and IEEE Xplore execution of the frozen H1 CORE search remains pending. Public evidence remains supportive/provisional and cannot replace the formal corpus.

## Immediate next task

The next EGMIV gate is

```math
\boxed{E0\ldots E4\rightarrow\textbf{raw completeness audit}\rightarrow\textbf{freeze train/test split}\rightarrow\mathcal O_P,\mathcal O_T\rightarrow u_{obs}\rightarrow\epsilon\rightarrow\text{H1a/UQ}.}
```

Parallel H1b data escalation should proceed, but final H1b support is prohibited unless the missing independent truth is actually obtained.