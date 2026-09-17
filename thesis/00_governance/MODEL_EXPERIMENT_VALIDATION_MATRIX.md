# Model–Experiment–Validation Matrix

**Status:** CURRENT / SYNCHRONIZED WITH RQ–SO–H v3  
**Effective date:** 2026-09-17  
**Purpose:** enforce preregistration, rival-model comparison, physical admissibility, uncertainty quantification, validity limits and falsification before scientific inference.

**Authorities:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`, `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`, `../../project/CANONICAL_INTERVENTION_PERFORMANCE_AMENDMENT_V2_1.md`, `SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`

---

## 1. Generic confirmatory test object

```math
\boxed{
\mathcal T_i=
(H_i,M_i,B_i,\Omega_i,D_i,\theta_i,Z_i,\delta_i,\mathcal F_i,V_i,U_i,C_i,X_i,R_i)
}
```

where:

- `H_i`: hypothesis;
- `M_i`: proposed model/representation/decision rule;
- `B_i`: baseline/rival model or developmental comparator;
- `\Omega_i`: declared test/scenario domain;
- `D_i`: evidence/data;
- `\theta_i`: parameters and provenance;
- `Z_i`: response vector;
- `\delta_i`: prespecified meaningful-effect threshold or decision criterion;
- `\mathcal F_i`: falsification/non-support condition;
- `V_i`: verification and validation protocol;
- `U_i`: uncertainty protocol;
- `C_i`: held constants / matched conditions;
- `X_i`: treatment, representation, intervention or decision difference intentionally changed;
- `R_i`: role of each dataset or evidence object (development / calibration / training / validation / held-out test).

A confirmatory result is interpretable only when the changed factor and held conditions are explicit.

---

## 2. Universal EGMIV requirements

Across rival models or interventions, hold constant all conditions not intentionally under test, including where applicable:

```math
\boxed{
\text{initial state}
+\text{hazard/scenario realization}
+\text{service requirements}
+\text{resource assumptions}
+\text{observation window}
+\text{evaluation metric}
}
```

unless one of these is itself the declared treatment.

No preferred model is validated alone.

### Verification gate

```math
\text{definitions}
\rightarrow
\text{dimensions/units}
\rightarrow
\text{conservation/physics}
\rightarrow
\text{limiting/nested cases}
\rightarrow
\text{numerical convergence}
\rightarrow
\text{regression/unit tests}.
```

### Validation gate

```math
\text{observed/benchmark behavior}
\rightarrow
\text{independent or held-out comparison where available}
\rightarrow
\text{declared validation metric}
\rightarrow
\text{uncertainty-aware adequacy criterion}
\rightarrow
\text{validation domain}.
```

```math
\boxed{\text{verification}\neq\text{validation}.}
```

A failed prerequisite gate gives **NOT TESTED**, not hypothesis falsification.

---

# 3. H1 — Dynamic causal interdependency

| Element | H1 specification / current state |
|---|---|
| RQ / SO | RQ3 / SO3, with RQ1/SO1 and RQ2/SO2 developmental inputs |
| Claim | dynamic causal P–T coupling may provide measurable incremental information relative to static/independent representations |
| Baselines | `M0` independent; `M1` static/algebraic coupling |
| Proposed representation | `M2` dynamic causal coupling |
| Primary contrast | `M2` vs `M1`; `M2` vs `M0` secondary as preregistered |
| Nested limits | `M2→M1` as dynamic memory/delay/state dependence is removed; `M1,M2→M0` when interface maps are removed |
| Held conditions | matched initial states, hazards, service requirements, exogenous conditions and evaluation windows |
| Treatment | coupling representation only |
| Candidate responses | cascade timing, failures, service loss, spatial propagation, recovery timing as frozen by H1 authority |
| Current model state | M0/M1/M2 implementations verified under current project authority |
| Confirmatory design | frozen |
| Raw data | row-level retrieval/qualification pending |
| Candidate split | `D_train^{cand}={E0,E2}`, `D_test^{cand}={E1,E3,E4}`; not frozen until R1–R8 pass |
| Calibration authorization | BLOCKED until raw row qualification passes |
| Confirmatory authorization | BLOCKED until prerequisite data gates pass |
| Falsification / non-support | M2 fails prespecified meaningful incremental-information/validation criterion or violates physical/nested-limit requirements |

---

# 4. H2 — Information, organization and feasible control

| Element | Required H2 specification |
|---|---|
| RQ / SO | RQ4 / SO4 |
| Claim | information availability and organizational conditions may alter estimation, feasible action, response timing, recovery and Stage-5 resilience |
| Nested models | `N0=P+T`, `N1=P+T+I`, `N2=P+T+I+O` |
| Mechanisms | measurement quality/availability, communication delay, estimation error, authority, coordination, resources, response delay |
| Held conditions | matched physical initial states, hazards and subsystem physics |
| Treatments | `N1−N0`: information-layer effect; `N2−N1`: organizational-layer effect |
| Candidate responses | estimation quality, feasible-control set, response delay, service/recovery trajectory, downstream `\mathfrak R_T` quantities |
| Data/domain | NOT YET FROZEN |
| Primary metric / threshold | NOT YET FROZEN |
| Calibration/validation roles | MUST BE DECLARED BEFORE EXECUTION |
| V&V/UQ | MUST BE FROZEN BEFORE CONFIRMATORY EXECUTION |
| Falsification / non-support | declared I/O perturbations fail to produce the prespecified meaningful effect over the declared domain |

---

# 5. H3 — Viability–reachability incremental information

| Element | Required H3 specification |
|---|---|
| RQ / SO | RQ5 / SO5 |
| Claim | uncertainty-aware viability/reachability quantities may add predictive or decision-relevant information beyond conventional performance/recovery curves |
| Baseline | `R_curve`: conventional service/performance/recovery information |
| Proposed information set | `R_curve + \mathfrak R_T` |
| Resilience object | `\mathfrak R_T=(\mathcal V_{\alpha,T_V},\mathcal R_{\beta,T_R},\rho_{\mathcal V},T_{\mathcal V},T_{\rm rec},P_{\rm viable},P_{\rm recover})` |
| Held conditions | matched system state, scenario information and prediction/decision target |
| Treatment | addition of preregistered viability/reachability information, not arbitrary additional features |
| Outcome | future maintainability/recovery/constraint-failure or declared decision task |
| Acceptable set | `K=K_phys∩K_svc∩K_op`; exact thresholds evidence-qualified |
| Recovery target / failure set | `G_rec⊆K`; `F` separately defined |
| Horizons | `T_V` maintainability horizon and `T_R` recovery horizon kept distinct |
| Uncertainty semantics | probability only if evidentially justified; otherwise appropriate deterministic/interval/scenario semantics |
| Primary skill/decision metric | NOT YET FROZEN |
| Meaningful threshold `delta_3` | NOT YET FROZEN |
| Solver | NOT YET SELECTED; must pass algorithm-selection/verification gate |
| Falsification / non-support | no prespecified incremental skill/decision value after declared complexity/adequacy criterion |

### Interface-criticality boundary

Interface criticality is a **supporting diagnostic**. It may be reported descriptively or tested under a separately declared analysis. Ranking superiority is **not** silently substituted for H3 or H4.

---

# 6. H4 — Intervention performance and sustainability consequences

| Element | Required H4 specification |
|---|---|
| RQ / SO | RQ6 / SO6 |
| Claim | resilience-effective interventions can have materially different resource-efficiency and sustainability consequence profiles |
| Candidate intervention set | `\mathcal A`; MUST BE FROZEN/QUALIFIED before confirmatory comparison |
| Resilience outcome | `\Delta\mathfrak R^{a_k}` and declared service/resilience target |
| Effectiveness | `\mathcal E_fx(a_k)` = preregistered target attainment; exact rule NOT YET FROZEN |
| Efficiency | `\mathcal E_fy(a_k)` based on evidence-supported resource vector `\mathbf C_res^{a_k}`; scalar form not assumed |
| Sustainability vector | current core: accessibility, operational energy, carbon, cost; additions require evidence/accounting boundary |
| Held conditions | matched hazard/scenario ensemble, initial conditions, accounting boundaries and evaluation horizons |
| Fair comparison | where claims compare interventions, resources/targets must be normalized or explicitly controlled by preregistered rule |
| Materiality metric | consequence-distance / Pareto / componentwise criterion `D_J`; NOT YET FROZEN |
| Threshold `delta_4` | NOT YET FROZEN |
| Uncertainty | intervention performance, resource and sustainability uncertainty must be propagated/declared |
| Falsification / non-support | resilience-effective interventions do not exhibit the preregistered material difference in efficiency/sustainability consequence profile over the declared domain |

### Required H4 sequence

```math
\boxed{
a_k
\rightarrow
Y^{a_k}
\rightarrow
\Delta\mathfrak R^{a_k}
\rightarrow
\mathcal E_{\rm fx}^{a_k}
\rightarrow
\mathcal E_{\rm fy}^{a_k}
\rightarrow
\Delta\mathbf J_{\rm sus}^{a_k}.
}
```

Effectiveness, efficiency and sustainability must not be collapsed into one score without a separately justified weighting/aggregation rule.

---

# 7. H5 — Joint resilience–sustainability engineering decision

| Element | Required H5 specification |
|---|---|
| RQ / SO | RQ7 / SO7 |
| Claim | joint resilience–sustainability evaluation may materially change the feasible/nondominated intervention set relative to resilience-only evaluation |
| Baseline decision set | `\mathcal A_R^{\star}` |
| Joint decision set | `\mathcal A_{R,S}^{\star}` |
| v2.1 construction rule | effectiveness and efficiency must be explicit performance/admissibility inputs to the joint decision; H5 label remains unchanged |
| Candidate actions | same qualified intervention set across compared decision formulations |
| Feasibility | technical, operational, resource and other declared constraints |
| Uncertainty ensemble | `\Omega`; NOT YET FROZEN |
| Decision comparison | set distance, membership change, Pareto change or regret metric; NOT YET FROZEN |
| Threshold `delta_5` | NOT YET FROZEN |
| Held conditions | same interventions, scenario ensemble, physical model, accounting boundaries and evaluation horizon |
| Falsification / non-support | joint evaluation fails the preregistered material-change/regret criterion within the declared domain |

### Sequencing boundary

Adaptive or multi-period transformation pathways are a Stage-7 extension. They may be activated only after action semantics, state-transition logic, uncertainty treatment, resource constraints and decision rules are separately specified. They are not automatically implied by H5.

---

# 8. Supporting interface-criticality analysis

If activated, define a separate analysis object with:

- diagnostic definition and units;
- perturbation semantics;
- baseline structural/flow diagnostics if comparative claims are made;
- equal-budget/fairness rule where ranking interventions are compared;
- scenario aggregation;
- uncertainty;
- falsification or descriptive-only status.

Do not infer “critical” from network centrality alone unless criticality is explicitly defined as a structural centrality property.

---

# 9. Parameter provenance rule

```math
\boxed{
\text{measured/site data}
>\text{peer-reviewed/full-text evidence}
>\text{qualified benchmark data}
>\text{sensitivity-only assumption}.
}
```

This is a provenance preference, not an automatic quality ranking independent of relevance. Every parameter must retain source, units, domain and uncertainty.

No sensitivity-only value may later be described as empirical calibration.

---

# 10. Amendment rule

Any post-freeze change to a confirmatory:

- hypothesis wording;
- treatment or held conditions;
- baseline/rival;
- scenario domain;
- data role/split;
- primary outcome/metric;
- threshold/decision criterion;
- uncertainty model;
- falsification rule;
- accounting boundary;

requires a dated amendment stating:

1. reason for change;
2. whether results were already observed;
3. whether the affected analysis becomes exploratory;
4. downstream chapters/artifacts affected;
5. whether re-execution is required.

---

# 11. Current execution summary

| Hypothesis | Current high-level state |
|---|---|
| H1 | model verification and confirmatory design advanced/frozen; raw row-level qualification remains blocking |
| H2 | mechanism architecture exists; empirical/domain/metric qualification remains open |
| H3 | mathematical preparation active; acceptability, uncertainty, policy, solver, metric, threshold and data gates remain open |
| H4 | conceptual sequence frozen by intervention-performance amendment; effectiveness/efficiency/sustainability operationalization and thresholds remain open |
| H5 | joint-decision logic frozen; action set, decision metric, uncertainty ensemble and threshold remain open |

No blocked hypothesis is treated as failed.
