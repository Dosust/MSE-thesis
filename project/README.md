# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![H1 Prereg](https://img.shields.io/badge/confirmatory%20design-FROZEN-1A7F37)
![Validation](https://img.shields.io/badge/NYC%2FACN-PARTIAL%20PASS-9A6700)

This directory is the active scientific/mathematical specification of the MSE thesis. The seven-stage framework and H1–H5 logic are frozen. The named execution method is **EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method**.

> Reasoning protocol: [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md)  
> Execution method: [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md)  
> Evidence rule: public-support evidence may develop the method but cannot replace the formal confirmatory corpus.

## H1 authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`](H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md) | M0/M1/M2 physical specification | frozen |
| 2 | [`H1_CONFIRMATORY_PREREGISTRATION_V1.md`](H1_CONFIRMATORY_PREREGISTRATION_V1.md) | H1a/H1b design, UQ and decision gates | frozen |
| 3 | [`H1_THRESHOLD_PROVENANCE_V1.md`](H1_THRESHOLD_PROVENANCE_V1.md) | numerical/observation/engineering threshold provenance | partially frozen |
| 4 | [`H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md`](H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md) | observation and service-requirement architecture | frozen structure |
| 5 | [`H1_DEMONSTRATOR_QUALIFICATION_V1.md`](H1_DEMONSTRATOR_QUALIFICATION_V1.md) | demonstrator qualification and hard gates | **current** |
| 6 | [`../models/H1/M0/`](../models/H1/M0/) | independent baseline | verified 13/13 |
| 7 | [`../models/H1/M1/`](../models/H1/M1/) | static/algebraic coupling | verified |
| 8 | [`../models/H1/M2/`](../models/H1/M2/) | dynamic causal coupling | verified full 29/29 regression |
| 9 | [`../evidence/H1/08_demonstrator/`](../evidence/H1/08_demonstrator/) | machine-readable demonstrator audit | current |

## H1 model state

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic coupling},\quad M_2=\text{dynamic causal coupling}.}
```

Nested limits pass:

```math
M_1\rightarrow M_0,
\qquad
M_2\rightarrow M_1.
```

Benchmark effects remain verification-only.

## Confirmatory statistic

Primary H1a comparison is M2 vs M1.

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

Thresholds cannot be selected from observed M2−M1 effects.

Frozen numerical floors for the current minimal demonstrator are

```math
\boxed{u_{num,P}=0.000416667,\qquad u_{num,T}=0.001281963}
```

at

```math
\boxed{\Delta t=0.00125\;\mathrm{h}=4.5\;\mathrm{s}}.
```

`epsilon_P`, `epsilon_T` and `epsilon_pred` remain unfrozen pending real observation uncertainty and service requirements.

## Validation observation architecture

Power validation uses interval served energy divided by independently reconstructed requested energy. Transportation validation uses completed OD flow divided by independently reconstructed requested OD demand. Missing telemetry is never equivalent to physical zero.

All model outputs must be passed through the same temporal/spatial observation operator as the data.

## Qualified public demonstrator

```math
\boxed{\mathcal D_{H1}^{public}=\mathcal D_{NYC}\cup\mathcal D_{ACN}}
```

with status

```math
\boxed{\textbf{PARTIAL PASS}}.
```

### NYC system arm

Audited public sources:
- NYISO P-58B actual load;
- EAGLE-I 15-minute county outages;
- NYC TLC trip records;
- NYC DOT Traffic Speeds;
- NYC 311;
- Con Edison / NY DPS event and restoration evidence.

Tropical Storm Isaias passes the structural temporal-overlap gate. Candidate common validation clock: **15 minutes**, pending final raw timestamp inspection.

The arm supports aggregate load/outage/restoration validation, TLC-subsystem completed OD behavior, road-state validation, obstruction evidence and restoration milestones.

It does **not** fully support microscopic road→crew→repair validation or exact fine-scale P–T spatial co-validation because public data do not provide individual geolocated crew/job trajectories and the NYISO Zone-J power geography does not map exactly to fine transport geography.

### ACN charging arm

ACN-Data is admissible for charging-component calibration/validation but is not NYC same-event system truth.

```math
\boxed{\text{ACN}\not\Rightarrow\text{system-level H1b validation}.}
```

## Candidate event family

The wind/tree mechanism family currently contains:

```text
E0  Tropical Storm Fay — 2020-07-10
E1  Tropical Storm Isaias — 2020-08-04 to 2020-08-12
E2  Dec 2022 wind/rain storm
E3  Dec 2023 wind/rain storm
E4  Apr 2024 coastal wind/rain storm
```

Train/test membership is deliberately **not frozen** until raw completeness and missingness are quantified.

Required:

```math
D_{train}\cap D_{test}=\varnothing
```

with at least two independent held-out events for any mechanism class claimed confirmatory.

## H1b status

```math
\boxed{\textbf{BLOCKED WITH PUBLIC DATA AT THE STRONGEST PRE-REGISTERED LEVEL}}.
```

This does not block H1a matched representation testing, aggregate/event validation, road-state validation or charging-component validation.

To upgrade H1b, additional independent data are required: geolocated crew/job logs, finer electrical service/outage truth coextensive with the transport domain, and stronger requested-mobility truth.

## Formal literature evidence

Authenticated Scopus, Web of Science Core Collection, Compendex and IEEE Xplore execution of the frozen H1 CORE search remains pending. Final H1 confirmation is prohibited until the formal corpus is completed and reconciled.

## Immediate next step

```math
\boxed{E0\ldots E4\rightarrow\textbf{raw completeness audit}\rightarrow\textbf{freeze train/test split}\rightarrow\mathcal O_P,\mathcal O_T\rightarrow u_{obs}\rightarrow\epsilon\rightarrow\text{H1a/UQ}.}
```

Run the public-data track and H1b data-escalation track in parallel. Do not upgrade H1b from component/aggregate evidence without the missing independent truth.