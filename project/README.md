# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![H1 Prereg](https://img.shields.io/badge/confirmatory%20design-FROZEN-1A7F37)

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
| 9 | [`H1_CONFIRMATORY_PREREGISTRATION_V1.md`](H1_CONFIRMATORY_PREREGISTRATION_V1.md) | H1a/H1b confirmatory design, thresholds, UQ and decision gates | **frozen v1.0** |
| 10 | [`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction rationale | current |
| 11 | [`FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`](FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md) | primary evidence protocol | current |
| 12 | [`H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`](H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md) | H1 formal search | frozen; authenticated execution pending |

## H1 physical experiment

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C.
```

Information and organization remain deferred to H2.

The competing representations are

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic coupling},\quad M_2=\text{dynamic causal coupling}.}
```

- [`../models/H1/M0/`](../models/H1/M0/) — verified 13/13.
- [`../models/H1/M1/`](../models/H1/M1/) — verified 13/13 M1-specific gates.
- [`../models/H1/M2/`](../models/H1/M2/) — verified full M1+M2 regression 29/29.

Nested limits pass:

```math
M_1\rightarrow M_0
```

when interface maps are removed, and

```math
\boxed{M_2\rightarrow M_1}
```

when dynamic memory and repair delay are removed.

Benchmark queue/recovery effects remain analytical verification only and cannot be used as confirmatory H1 effect sizes.

## H1 confirmatory pre-registration v1.0

The decisive H1a comparison is **M2 vs M1**. M2 vs M0 is secondary context.

The predeclared scenario universe is

```math
\Omega_H=
\Omega_0\cup\Omega_C\cup\Omega_O\cup\Omega_R\cup\Omega_J\cup\Omega_D,
```

covering null/intact, charging stress, charger-feeder outage, road-to-repair stress, joint disruption and decoupling/zero-memory controls.

The primary H1a endpoint is the threshold-normalized trajectory discrepancy

```math
D_{PT}^{2,1}(\omega)=
\frac1T\int_0^T
\left[
\left(\frac{S_P^{M_2}-S_P^{M_1}}{\epsilon_P}\right)^2+
\left(\frac{S_T^{M_2}-S_T^{M_1}}{\epsilon_T}\right)^2
\right]^{1/2}dt,
```

with

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

Thresholds are not allowed to depend on observed M2−M1 effects. For service s,

```math
\epsilon_s^{det}=\max(u_{obs,s},u_{num,s}),
```

and, when independently documented engineering tolerance exists,

```math
\boxed{\epsilon_s=\max(u_{eng,s},u_{obs,s},u_{num,s}).}
```

Without a defensible engineering tolerance, the strongest allowed positive conclusion is **representation-distinguishable**, not engineering-material.

### H1a frozen decision gates

A0 verification/physics; A1 independently frozen thresholds; A2 95% paired interval for \(\Theta_{repr}\) wholly above 1; A3 predeclared-UQ robustness; A4 no advantage obtained by greater physical/numerical violation.

### UQ/statistics lock

- identical uncertain draws for M0/M1/M2;
- Tier A/B parameters eligible for confirmatory UQ; Tier C sensitivity-only;
- sampling error must be ≤ `0.1 × frozen decision scale` in interval half-width;
- variance-based sensitivity only after dependence audit;
- 5,000 paired bootstrap resamples; 95% intervals;
- P-values secondary to effect size, uncertainty and threshold comparison.

### H1b shell

H1b requires independent event/case truth. Synthetic self-generated truth alone is insufficient. No held-out observations may enter calibration, threshold derivation, model revision or scenario selection. If independent truth is absent, H1b is **NOT YET TESTABLE**.

## Formal H1 evidence status

Authenticated execution of the exact frozen H1 CORE searches in Scopus, Web of Science Core Collection, Compendex and IEEE Xplore remains pending. Final H1 confirmation is prohibited until that corpus is completed and reconciled.

## Immediate next step

Model construction and pre-registration are complete:

```math
\boxed{
M_0,M_1,M_2\;\checkmark
\rightarrow
\text{pre-registration}\;\checkmark
\rightarrow
\mathbf{threshold\ provenance}
\rightarrow
\text{scenario/parameter freeze}
\rightarrow
\text{confirmatory UQ}.
}
```

Populate and freeze `../evidence/H1/08_preregistration/threshold_provenance_template.csv` using independent evidence for observation uncertainty, numerical uncertainty and engineering/service tolerances. **Do not run the final H1a confirmatory comparison before this gate is complete.**