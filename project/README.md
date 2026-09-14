# Project Mathematical Architecture

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Search](https://img.shields.io/badge/evidence%20search-DE%20NOVO-1A7F37)
![FTEE](https://img.shields.io/badge/FTEE%20v2.0-CURRENT-0969DA)
![H1](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)

This directory is the active mathematical/scientific specification of the MSE thesis. The seven-stage framework and H1–H5 logic are frozen. The named execution method is **EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method**. FTEE v2.0 remains the evidence-to-equation protocol inside EGMIV.

> **Reasoning protocol:** [`RESEARCH_REASONING_PROTOCOL.md`](RESEARCH_REASONING_PROTOCOL.md)

> **Execution method:** [`EGMIV_METHOD_V1.md`](EGMIV_METHOD_V1.md)

> **Evidence rule:** primary thesis evidence enters only through the reproducible search and frozen eligibility process. Public-support branches cannot silently replace the formal confirmatory corpus.

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
| 9 | [`MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md) | demonstrator-reduction rationale | current |
| 10 | [`FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`](FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md) | primary evidence protocol | current |
| 11 | [`H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`](H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md) | H1 formal search | frozen; authenticated execution pending |

## H1 physical experiment

The physical demonstrator boundary remains

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C.
```

Information and organization remain deferred to H2 so H1 can identify physical Power–Transportation coupling without attribution confounding.

The competing representations are

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic coupling},\quad M_2=\text{dynamic causal coupling}.}
```

### M0

[`../models/H1/M0/`](../models/H1/M0/) — **verified, 13/13**.

### M1

[`../models/H1/M1/`](../models/H1/M1/) — **verified, 13/13 M1-specific gates**.

M1 is memoryless and satisfies

```math
M_1\rightarrow M_0
```

when interface maps are removed.

### M2

[`../models/H1/M2/`](../models/H1/M2/) — **verified, full M1+M2 regression 29/29**.

M2 adds explicit interface memory and recovery dynamics:

```math
q_c(k+1)=\max\{0,q_c(k)+\Delta t[\lambda_c(k)-\mu_c(k)]\},
```

plus repair-crew path state and repair progress.

The critical nesting gate passes:

```math
\boxed{M_2\rightarrow M_1\quad\text{when queue memory is suppressed and dynamic repair is disabled}.}
```

Dynamic repair also reduces to M1 static free-flow delay under empty, unobstructed traffic.

Closed-form verification checks pass: persistent overload growth `900-720=180 veh/h` produces 324 queued vehicles over 1.8 h; a 0.2 h outage at 600 veh/h creates 120 vehicles and requires exactly 1 h to clear with 120 veh/h spare capacity. Dynamic congested repair restores at 0.19 h versus 0.14 h for the static free-flow comparator. These remain benchmark verification results, not confirmatory H1 effect sizes.

## Formal H1 evidence status

Authenticated execution of the exact frozen H1 CORE searches in Scopus, Web of Science Core Collection, Compendex and IEEE Xplore remains pending. No final H1 conclusion may substitute public-web discovery for that corpus.

## Immediate next step

Model construction is now complete at the H1 comparator level:

```math
M_0\;\checkmark\rightarrow M_1\;\checkmark\rightarrow M_2\;\checkmark.
```

The next EGMIV operation is **H1a pre-registration**, not another model:

```math
\boxed{
\Omega_H
\rightarrow
\{L_P,L_T,T_R,T_C,D_S\}
\rightarrow
\varepsilon_{repr},\varepsilon_{pred}
\rightarrow
\text{parameter/UQ plan}
\rightarrow
\text{sensitivity + held-out validation}.
}
```

Before confirmatory M0/M1/M2 runs, freeze the matched scenario universe, primary outcomes, engineering-resolution thresholds, uncertainty distributions, sensitivity method, numerical tolerances, validation split and stopping rules. Thresholds may not be chosen after observing confirmatory results.