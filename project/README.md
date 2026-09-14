# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![H1 Prereg](https://img.shields.io/badge/confirmatory%20design-FROZEN-1A7F37)
![Thresholds](https://img.shields.io/badge/threshold%20provenance-PARTIAL-9A6700)

This directory is the active mathematical/scientific specification of the MSE thesis. The seven-stage framework and H1–H5 logic are frozen. The named execution method is **EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method**.

> **Reasoning protocol:** [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md)

> **Execution method:** [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md)

> **Evidence rule:** primary evidence enters only through the reproducible search and frozen eligibility process. Public-support branches cannot replace the formal confirmatory corpus.

## Authority map

| Priority | File | Role | Status |
|---:|---|---|---|
| 1 | [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md) | reasoning, V&V, falsification and synthesis | canonical/current |
| 2 | [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md) | evidence→mechanism→model→validation execution | canonical/current |
| 3 | [`THESIS_SCOPE.md`](THESIS_SCOPE.md) | scope and stage boundaries | frozen |
| 4 | [`CANONICAL_7_STAGE_FRAMEWORK.md`](CANONICAL_7_STAGE_FRAMEWORK.md) | seven-stage architecture | frozen |
| 5 | [`CANONICAL_SYSTEM_DEFINITION.md`](CANONICAL_SYSTEM_DEFINITION.md) | P–T–I–O system identity | canonical |
| 6 | [`RESEARCH_HYPOTHESES.md`](RESEARCH_HYPOTHESES.md) | H1–H5 | logic frozen |
| 7 | [`ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md) | confirmatory operationalization | current |
| 8 | [`H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`](H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md) | H1 M0/M1/M2 specification | frozen structure |
| 9 | [`H1_CONFIRMATORY_PREREGISTRATION_V1.md`](H1_CONFIRMATORY_PREREGISTRATION_V1.md) | H1a/H1b confirmatory design, UQ and decision gates | frozen v1.0 |
| 10 | [`H1_THRESHOLD_PROVENANCE_V1.md`](H1_THRESHOLD_PROVENANCE_V1.md) | threshold evidence, numerical floor, admissibility boundary | **current / partially frozen** |
| 11 | [`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction rationale | current |
| 12 | [`FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`](FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md) | primary evidence protocol | current |
| 13 | [`H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`](H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md) | H1 formal search | frozen; authenticated execution pending |

## H1 physical experiment

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C.
```

Information and organization remain deferred to H2.

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic coupling},\quad M_2=\text{dynamic causal coupling}.}
```

- [`../models/H1/M0/`](../models/H1/M0/) — verified 13/13.
- [`../models/H1/M1/`](../models/H1/M1/) — verified 13/13 M1-specific gates.
- [`../models/H1/M2/`](../models/H1/M2/) — verified full M1+M2 regression 29/29.

Nested limits pass:

```math
M_1\rightarrow M_0,
\qquad
M_2\rightarrow M_1.
```

Benchmark queue/recovery effects remain verification only and cannot be used as confirmatory H1 effect sizes.

## H1 confirmatory pre-registration v1.0

The decisive H1a comparison is **M2 vs M1**. M2 vs M0 is secondary context.

```math
\Omega_H=\Omega_0\cup\Omega_C\cup\Omega_O\cup\Omega_R\cup\Omega_J\cup\Omega_D.
```

The primary H1a endpoint is

```math
D_{PT}^{2,1}(\omega)=\frac1T\int_0^T\left[\left(\frac{S_P^{M_2}-S_P^{M_1}}{\epsilon_P}\right)^2+\left(\frac{S_T^{M_2}-S_T^{M_1}}{\epsilon_T}\right)^2\right]^{1/2}dt,
```

with

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

Thresholds may not depend on observed M2−M1 effects.

## H1 threshold provenance v1.0

The threshold study has now been executed under

```math
\text{evidence}\rightarrow\text{native quantity}\rightarrow\text{mapping}\rightarrow\text{uncertainty}\rightarrow\text{admissibility}\rightarrow\epsilon.
```

### Numerical component — frozen

For the current minimal H1 demonstrator:

```math
\boxed{\Delta t=0.00125\;\mathrm{h}=4.5\;\mathrm{s}}
```

with an independent refinement at `0.000625 h` gives

```math
\boxed{u_{num,P}=0.000416667,\qquad u_{num,T}=0.001281963.}
```

These are worst verification-scenario time-averaged service discrepancies and are independent of M2−M1 confirmatory effect sizes.

### Observation component — not yet frozen

Meter/detector standards are native measurement-quality evidence, not direct service-ratio thresholds.

Power observation uncertainty must include

```math
u_{obs,P}=\mathcal U(u_{meter},u_{counterfactual\ demand},u_{aggregation},u_{temporal},\Sigma_P),
```

because outage-period demand is partly counterfactual.

Transportation observation uncertainty must include

```math
u_{obs,T}=\mathcal U(u_{count},u_{OD},u_{coverage},u_{trajectory\ matching},u_{temporal},\Sigma_T),
```

because `S_T` is a requested/completed OD-service ratio rather than a single detector count.

### Engineering component — not universal

The evidence does not support universal `u_eng,P` or `u_eng,T` values. Power-resilience metrics depend on goals, event context, scale and stakeholder/operator priorities; FHWA transportation targets are likewise context and agency dependent.

Therefore

```math
\boxed{\epsilon_P\;\text{NOT YET FROZEN},\qquad\epsilon_T\;\text{NOT YET FROZEN}.}
```

H1b predictive threshold `epsilon_pred` also remains unfrozen until independent validation events and their observation/calibration noise model exist.

Detailed machine-readable provenance is stored under [`../evidence/H1/07_audit/`](../evidence/H1/07_audit/).

## Formal H1 evidence status

Authenticated execution of the exact frozen H1 CORE searches in Scopus, Web of Science Core Collection, Compendex and IEEE Xplore remains pending. Final H1 confirmation is prohibited until that corpus is completed and reconciled.

## Immediate next step

Model construction, verification, pre-registration and the numerical part of threshold provenance are complete:

```math
\boxed{M_0,M_1,M_2\;\checkmark\rightarrow\text{pre-registration}\;\checkmark\rightarrow\text{numerical threshold provenance}\;\checkmark\rightarrow\mathbf{observation\ architecture+service\ requirements}.}
```

The next admissible task is to freeze the **validation observation architecture** for Power and Transportation and the **case-specific engineering service requirements**. Only then can `u_obs,P`, `u_obs,T`, `u_eng,P`, `u_eng,T`, `epsilon_P`, `epsilon_T`, and eventually `epsilon_pred` be computed. **Do not run the final H1a confirmatory comparison before this gate is complete.**