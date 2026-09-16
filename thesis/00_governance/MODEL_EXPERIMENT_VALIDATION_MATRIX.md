# Model–Experiment–Validation Matrix

**Purpose:** enforce preregistration, rival-model comparison, physical admissibility, uncertainty quantification and falsification before scientific inference.

## Generic test object

```math
\boxed{
\mathcal T_i=(H_i,M_i,B_i,\Omega_i,D_i,\theta_i,Z_i,\delta_i,\mathcal F_i,V_i,U_i)
}
```

where:

- `H_i`: hypothesis;
- `M_i`: proposed model/representation;
- `B_i`: baseline/rival model;
- `\Omega_i`: test/scenario domain;
- `D_i`: evidence/data;
- `\theta_i`: parameters and provenance;
- `Z_i`: response vector;
- `\delta_i`: prespecified meaningful-effect threshold/decision criterion;
- `\mathcal F_i`: falsification condition;
- `V_i`: verification/validation protocol;
- `U_i`: uncertainty protocol.

## Universal EGMIV requirements

Every confirmatory experiment must satisfy:

```math
\boxed{
\text{same relevant initial conditions}
+
\text{same hazards/scenarios}
+
\text{same resource assumptions}
}
```

across rival models unless a difference is itself the treatment being tested.

No preferred model is validated alone.

### Verification gate

```math
\text{dimensions}
\rightarrow\text{conservation/physics}
\rightarrow\text{limiting cases}
\rightarrow\text{numerical convergence}
\rightarrow\text{regression/unit tests}.
```

### Validation gate

```math
\text{benchmark/observed behavior}
\rightarrow\text{independent or held-out comparison}
\rightarrow\text{declared validation domain}
\rightarrow\text{uncertainty-aware adequacy judgment}.
```

Verification and validation are not interchangeable.

## H1 matrix

| Element | H1 specification / current state |
|---|---|
| Claim | dynamic causal P–T coupling materially changes cascade/service trajectories relative to independent/static representations |
| Baselines | `M0` independent; `M1` static/algebraic |
| Proposed representation | `M2` dynamic causal coupling |
| Nested-limit requirement | `M2→M1` as dynamic memory/delay removed; `M1,M2→M0` when interface maps removed |
| Response family | cascade/service/recovery trajectory outputs as frozen by H1 preregistration |
| Current model state | M0/M1/M2 implementations verified in current project authority |
| Confirmatory design | frozen |
| Raw data | row-level retrieval/qualification pending |
| Candidate split | `D_train^{cand}={E0,E2}`, `D_test^{cand}={E1,E3,E4}`; not frozen until R1–R8 qualification passes |
| Calibration authorization | BLOCKED until raw row qualification passes |
| Confirmatory run authorization | BLOCKED until prerequisite data/activation gates pass |
| Falsification | dynamic representation fails prespecified meaningful-difference/validation criteria or violates physical/nested-limit requirements |

## H2 matrix — to be frozen before execution

| Element | Required specification |
|---|---|
| Claim | information degradation and organizational constraints alter feasible response/recovery |
| Nested models | `P+T`, `P+T+I`, `P+T+I+O` |
| Mechanisms | measurement error/availability, communication delay, estimation error, authority/coordination/resource constraints |
| Primary responses | `\mathcal U`, `\tau_response`, declared downstream service/recovery vector |
| Data/domain | NOT YET FROZEN |
| Threshold/decision rule | NOT YET FROZEN |
| V&V/UQ | MUST BE FROZEN BEFORE CONFIRMATORY EXECUTION |
| Falsification | I/O perturbations fail to produce prespecified meaningful effects over declared domain |

## H3 matrix — to be frozen before execution

| Element | Required specification |
|---|---|
| Claim | viability quantities add decision-relevant information beyond conventional service/recovery metrics |
| Baseline predictor set | conventional service/recovery metrics |
| Proposed predictor set | conventional + `\rho,T_{\mathcal V},T_K,S_{\mathcal V}` |
| Outcome | declared future maintainability/constraint-failure outcome |
| Skill metric | NOT YET FROZEN |
| Matched-state test | required where feasible |
| Falsification | no meaningful skill/decision improvement after complexity penalty/declared criterion |

## H4 matrix — to be frozen before execution

| Element | Required specification |
|---|---|
| Claim | viability-sensitive ranking improves targeting value over structural/flow rankings |
| Baselines | degree, betweenness, flow-based ranking |
| Proposed ranking | `S_{ij}^{\mathcal V}` |
| Fairness rule | equal intervention budget/resources |
| Primary scalar viability functional | NOT YET FROZEN |
| Scenario aggregation | NOT YET FROZEN |
| Falsification | baseline ranking performs equally well or better under prespecified functional/budget |

## H5 matrix — to be frozen before execution

| Element | Required specification |
|---|---|
| Claim | adaptive trigger-based pathway improves robustness/satisficing performance over fixed pathway under deep uncertainty |
| Baseline | best prespecified fixed sequence `\Pi_F` |
| Proposed policy | adaptive `\boldsymbol\pi_{ST}` |
| Objective vector | risk, service, cost, carbon, inequity, time, flexibility |
| Scenario ensemble | NOT YET FROZEN |
| Robustness/satisficing metric | NOT YET FROZEN |
| Resource comparability | MUST BE DECLARED |
| Falsification | adaptive policy fails prespecified robustness gain or imposes unacceptable burden under decision rule |

## Parameter provenance rule

```math
\boxed{
\text{measured/site data}
>
\text{peer-reviewed/full-text evidence}
>
\text{benchmark data}
>
\text{sensitivity-only assumption}.
}
```

No sensitivity-only value may later be described as empirical calibration.

## Amendment rule

Any post-freeze change to a confirmatory threshold, scenario domain, baseline, data split, primary metric or falsification rule requires a dated amendment with:

1. reason for change;
2. whether results were already observed;
3. whether the analysis becomes exploratory;
4. downstream thesis sections affected.
