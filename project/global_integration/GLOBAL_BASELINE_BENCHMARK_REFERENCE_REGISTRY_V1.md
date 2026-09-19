# Global Baseline / Benchmark / Reference Registry v1

**Date:** 2026-09-19  
**Status:** CANONICAL GLOBAL PRE-DATA CLASSIFICATION REGISTRY  
**Scope:** Stage 1→7 experimental baselines, comparators, benchmark problems, verification fixtures, reference solutions/calculations, validation evidence/references, synthetic truth, ground truth, oracles, and external practice/factor references.  
**Empirical effect:** none. This registry classifies existing and deferred credibility objects; it does not create validation.

## 1. Governing firewall

~~~math
\boxed{
\text{baseline}
\neq
\text{benchmark}
\neq
\text{reference solution/calculation}
\neq
\text{validation evidence/reference}
\neq
\text{ground truth}.
}
~~~

Additional permanent distinctions:

~~~math
\boxed{
\text{synthetic truth}
\neq
\text{empirical ground truth},
}
~~~

~~~math
\boxed{
\text{oracle}
\neq
\text{validation reference},
}
~~~

~~~math
\boxed{
\text{external standard/factor/source}
\neq
\text{validation evidence by default},
}
~~~

~~~math
\boxed{
\text{requirement threshold}
\neq
\text{baseline}
\neq
\text{reference}.
}
~~~

The same object may participate in more than one workflow only when each role is separately declared and independence is not violated.

## 2. Canonical registry object

Every registered credibility/comparison object is represented as:

~~~math
\boxed{
\mathfrak C_j
=
(
ID_j,
\kappa_j,
\kappa_j^{sub},
S_j,
H_j,
O_j,
R_j,
Src_j,
Ind_j,
Truth_j,
Use_j^{allow},
Use_j^{prohibit},
\Lambda_j,
Status_j,
Prov_j
).
}
~~~

where:
- \(ID_j\): immutable registry identifier;
- \(\kappa_j\): global class;
- \(\kappa_j^{sub}\): subtype;
- \(S_j\): owning stage;
- \(H_j\): hypothesis/test link if applicable;
- \(O_j\): object being compared/checked;
- \(R_j\): scientific role;
- \(Src_j\): source/data/model origin;
- \(Ind_j\): independence relative to calibration/treatment;
- \(Truth_j\): truth semantics;
- \(Use_j^{allow}\): allowed use;
- \(Use_j^{prohibit}\): prohibited use;
- \(\Lambda_j\): claim ceiling;
- \(Status_j\): ACTIVE / DEFERRED / CONDITIONAL / PROVENANCE / NOT AUTHORIZED;
- \(Prov_j\): exact authority/provenance.

## 3. Global class ontology

### 3.1 BASELINE

A baseline is the declared comparison/counterfactual/information arm against which incremental change is measured.

Subtypes:

~~~text
RIVAL_MODEL_BASELINE
UNCOUPLED_REFERENCE_COMPARATOR
INFORMATION_BASELINE
COUNTERFACTUAL_INTERVENTION_BASELINE
BUSINESS_AS_USUAL_BASELINE
DECISION_BASELINE
~~~

A baseline is not presumed correct and is not a truth source merely because it is the comparator.

### 3.2 COMPARATOR

A comparator is a rival method/model/intervention/decision construction used for contrast.

A baseline may be one comparator, but not every comparator is the primary baseline.

### 3.3 BENCHMARK_PROBLEM

A benchmark problem is a standardized, reproducible problem/scenario used to test implementation, numerical behavior, method logic, or controlled performance.

Benchmark success does not automatically validate real-system claims.

### 3.4 VERIFICATION_FIXTURE

A verification fixture is a small hand-checkable/analytic/synthetic case with known expected behavior used to test code, dimensions, signs, limiting cases, event logic, or arithmetic.

~~~math
\boxed{
\text{verification fixture PASS}
\not\Rightarrow
\text{physical validation}.
}
~~~

### 3.5 REFERENCE_SOLUTION

A reference solution is a sufficiently trusted analytic or high-accuracy numerical solution of the same mathematical problem, used for verification/convergence/algorithm comparison.

It does not become physical ground truth merely by high numerical accuracy.

### 3.6 REFERENCE_CALCULATION

A reference calculation is an independently reproduced hand/analytic calculation for the same reported quantity, e.g. present value, Pareto membership, Jaccard distance, activity × factor accounting.

### 3.7 VALIDATION_EVIDENCE / VALIDATION_REFERENCE

Validation evidence is independent or appropriately reserved evidence used to assess whether a model/method is adequate for the intended real-system use.

A validation reference is the specific observable/reference target derived from that evidence.

Preferred hierarchy when scientifically appropriate:

~~~math
\boxed{
\text{independent empirical observation}
>
\text{qualified independent higher-fidelity reference}
>
\text{synthetic/analytic truth for verification only}.
}
~~~

The ordering is a claim-strength hierarchy, not a statement that every empirical dataset is automatically high quality.

### 3.8 SYNTHETIC_TRUTH

Synthetic truth is known because the benchmark was constructed to have a known answer/state.

Allowed: verification, controlled synthetic validation, algorithm discrimination.

Prohibited: describing it as observed real-world ground truth.

### 3.9 GROUND_TRUTH

Ground truth means the relevant physical truth is genuinely known to sufficient accuracy for the stated purpose.

This label is used conservatively.

~~~math
\boxed{
\text{observed data}
\not\equiv
\text{ground truth}
}
~~~

when measurement, reconstruction, coverage, or counterfactual uncertainty remains material.

### 3.10 ORACLE

An oracle is an ideal-information/control upper-bound diagnostic.

It is not an achievable baseline or validation target unless separately justified.

### 3.11 EXTERNAL_PRACTICE / FACTOR REFERENCE

Standards, authoritative factors, engineering guides, literature values, emission factors, cost references, etc. provide method/provenance/parameter support.

They are not model-validation evidence unless the validation role is explicitly qualified.

### 3.12 REQUIREMENT_THRESHOLD

A requirement/target/limit is normative, regulatory, stakeholder, contractual or engineering design information.

It is not a benchmark/reference simply because a model is tested against it.

### 3.13 QUALIFIED_CASE

A qualified case is the real or realistic thesis case used after its data/model/provenance gates close.

A protocol may place a qualified case at the top of a benchmark ladder (for example (B_{k,3})), but the global class remains QUALIFIED_CASE rather than BENCHMARK_PROBLEM.

### 3.14 TREATMENT

A treatment is the declared changed model/information/intervention/decision block in a matched comparison.

Treatment status gives no truth privilege.

### 3.15 EVIDENCE_SOURCE_REFERENCE

An evidence-source reference is literature, authoritative documentation, or case evidence used to support existence, mechanism, parameter, or provenance claims.

It is distinct from VALIDATION_EVIDENCE unless it is independently qualified for the specific validation role.

### 3.16 AUXILIARY_COUNTERFACTUAL_MODEL

An auxiliary counterfactual model reconstructs an unobserved or counterfactual quantity required by a metric, such as requested demand during disruption.

It must be validated for that reconstruction task and is neither the experimental baseline nor ground truth.

---

# 4. Stage 1 registry

| ID | Class / subtype | Object | Role | Allowed use | Prohibited use | Claim ceiling | Status | Authority |
|---|---|---|---|---|---|---|---|---|
| GCBR-S1-01 | VERIFICATION_FIXTURE / generic ontology fixture | Stage-1 semantic/entity/relation fixtures | verify schemas, runtime guards, noncausal semantics, provenance | framework verification | real-case validation; causal proof; H1–H5 evidence | Stage-1 framework verification only | ACTIVE | STAGE1_GENERIC_FIXTURE_VERIFICATION_REPORT_2026-09-18.md @ def61787... |
| GCBR-S1-02 | VALIDATION_REFERENCE / CASE_STRUCTURE | case-specific structure/geometry/source evidence | assess Stage-1 case materialization | case QA/validation when independently qualified | infer causality from structural match | case-specific structure only | DEFERRED | Stage-1 v2 case gates |

Stage-1 fixture PASS therefore means:

~~~math
\boxed{
G_1^{framework}=PASS
\not\Rightarrow
G_1^{case}(c)=PASS.
}
~~~

---

# 5. Stage 2 registry

Stage 2 primarily uses causal evidence/provenance, not a generic numerical benchmark ladder.

| ID | Class / subtype | Object | Role | Allowed use | Prohibited use | Claim ceiling | Status | Authority |
|---|---|---|---|---|---|---|---|---|
| GCBR-S2-01 | EVIDENCE_SOURCE_REFERENCE / mechanism evidence | peer-reviewed/authoritative mechanism evidence | support/qualify directional mechanism claims | G2 evidence qualification within validity domain | treat literature existence as case-specific causal truth | evidence-supported mechanism candidacy/qualification | ACTIVE | Stage-2 evidence/governance package |
| GCBR-S2-02 | CASE_CAUSAL_REFERENCE / future | case-specific observations/evidence for mechanism activation/response | case causal qualification | support PASS/BLOCKED/FAIL status | globalize case result to all P–T systems | declared case/domain only | CONDITIONAL/DEFERRED | Stage-2 case evidence gates |

Permanent:

~~~math
\boxed{
\text{common exposure/correlation}
\neq
\text{causal validation reference}.
}
~~~

---

# 6. Stage 3 / H1 registry

## 6.1 Experimental baselines/comparators

| ID | Class / subtype | Object | Role | Independence/truth | Allowed use | Prohibited use | Status | Authority |
|---|---|---|---|---|---|---|---|---|
| GCBR-H1-01 | BASELINE / RIVAL_MODEL_BASELINE | \(M_1\) static/algebraic P–T coupling | primary H1 rival | not truth; matched rival model | primary M2 incremental comparison | call M1 ground truth | ACTIVE | H1 preregistration + global H1–H5 registry |
| GCBR-H1-02 | COMPARATOR / UNCOUPLED_REFERENCE_COMPARATOR | \(M_0\) independent P+T | uncoupled reference/context + nested limit | not truth | contextual/secondary contrast, nested-limit test | use as sole H1 primary rival | ACTIVE | H1 preregistration |
| GCBR-H1-03 | TREATMENT / MODEL | \(M_2\) dynamic causal coupling | H1 treatment | not truth | matched dynamic-coupling test | validate M2 against itself | ACTIVE DESIGN / EXECUTION GATED | Stage-3 v2 |

## 6.2 Stage-3 benchmark ladder

| ID | Global class | Stage label | Purpose | Truth semantics | Claim ceiling | Status |
|---|---|---|---|---|---|---|
| GCBR-S3-B0 | VERIFICATION_FIXTURE | \(B_{3,0}\) | dimensions, conservation, exact simple solutions, resets, nested limits, regression | analytic/constructed truth | CODE / MECHANISM VERIFICATION ONLY | ACTIVE |
| GCBR-S3-B1 | BENCHMARK_PROBLEM / subsystem | \(B_{3,1}\) | P/T subsystem credibility | may use independent subsystem evidence/reference | SUBSYSTEM CREDIBILITY ONLY | ACTIVE DESIGN |
| GCBR-S3-B2 | BENCHMARK_PROBLEM / coupled synthetic | \(B_{3,2}\) | controlled ready-interface execution | SYNTHETIC_TRUTH | COUPLED IMPLEMENTATION / SYNTHETIC VALIDATION | ACTIVE DESIGN |
| GCBR-S3-B3 | QUALIFIED_CASE | \(B_{3,3}\) ladder position | final qualified Stage-3 thesis case | empirical/realistic status depends on qualified evidence | predictive/explanatory or H1 only after gates | DEFERRED |

The symbol \(B_{3,3}\) is a ladder position in the Stage-3 protocol; its global class is QUALIFIED_CASE, not a synthetic benchmark.

## 6.3 H1 validation/reference objects

| ID | Class / subtype | Object | Role | Allowed use | Prohibited use | Status |
|---|---|---|---|---|---|---|
| GCBR-H1-V01 | VALIDATION_EVIDENCE | independently reserved empirical P/T observations/events | H1b predictive adequacy | held-out predictive comparison | calibration/refit using test events | DEFERRED / qualification required |
| GCBR-H1-V02 | VALIDATION_REFERENCE | observed/reconstructed \(S_P^{obs},S_T^{obs}\) with uncertainty | common comparison target after observation operator | quantify held-out service error | call uncertain reconstruction exact ground truth | DEFERRED |
| GCBR-H1-V03 | REFERENCE_SOLUTION | independent higher-fidelity/reference model \(y^R\) where justified | alternative predictive/explanatory comparison | compute \(E_q^{(M)}\) within validity domain | treat higher fidelity as automatically true | CONDITIONAL |
| GCBR-H1-V04 | SYNTHETIC_TRUTH | controlled benchmark truth | verify sign/memory/events/nested limits | synthetic benchmark discrimination | empirical validation language | ACTIVE for benchmark only |

## 6.4 Counterfactual observation baselines

The H1 validation architecture also uses baseline-demand reconstruction models:

~~~math
\widehat E_{i,m}^d=\mathcal B_i(Z_m;\widehat\beta_i),
\qquad
\widehat N_{w,m}^{req}=\mathcal D_w(X_m;\widehat\gamma_w).
~~~

These are classified as AUXILIARY_COUNTERFACTUAL_MODEL, not H1 experimental baselines and not ground truth.

They must be validated on intact/non-held-out periods with residual uncertainty propagated into service reconstruction.

Model-generated OD is explicitly not admissible as independent H1b truth.

---

# 7. Stage 4 / H2 registry

## 7.1 Comparator architecture

| ID | Class / subtype | Object | Role | Truth semantics | Status |
|---|---|---|---|---|---|
| GCBR-H2-01 | BASELINE / INFORMATION_BASELINE | \(\mathscr N_0=P+T\) | idealized reference knowledge-control architecture | not a claim that real systems have no information | ACTIVE DESIGN |
| GCBR-H2-02 | TREATMENT / INFORMATION | \(\mathscr N_1=P+T+I\) | information-effect arm | not truth | ACTIVE DESIGN |
| GCBR-H2-03 | TREATMENT / ORGANIZATION | \(\mathscr N_2=P+T+I+O\) | organizational-effect arm | not truth | ACTIVE DESIGN |

## 7.2 Estimation validation

| ID | Class | Object | Allowed use | Claim ceiling | Status |
|---|---|---|---|---|---|
| GCBR-S4-V01 | VALIDATION_REFERENCE | point/state truth/reference where independently available | estimator state-error validation | declared state/observation domain | DEFERRED |
| GCBR-S4-V02 | VALIDATION_EVIDENCE | held-out observations + missing/delay stress evidence | estimator coverage/calibration/robustness | estimator adequacy only | DEFERRED |
| GCBR-S4-B01 | BENCHMARK_PROBLEM | estimator benchmark/stress tests | numerical/algorithm verification | method verification | DEFERRED |

No estimator is currently selected; no Stage-4 validation result is claimed.

---

# 8. Stage 5 / H3 registry

## 8.1 H3 baseline

~~~math
\boxed{
R_{curve}
=
(Q(t),L_{svc},Q_{min},T_{rec})
}
~~~

is classified BASELINE / INFORMATION_BASELINE for H3.

It is a legitimate conventional comparison representation, not ground truth.

## 8.2 Stage-5 benchmark/reference ladder

| ID | Global class | Stage label | Role | Truth semantics | Claim ceiling | Status |
|---|---|---|---|---|---|---|
| GCBR-S5-B0 | VERIFICATION_FIXTURE / BENCHMARK_PROBLEM | \(B_0\) | low-dimensional analytic/high-resolution verification | analytic/reference solution | algorithm/math verification | ACTIVE |
| GCBR-S5-B1 | BENCHMARK_PROBLEM / subsystem | \(B_1\) | reduced P/T constituent systems | controlled/subsystem | subsystem method credibility | ACTIVE DESIGN |
| GCBR-S5-B2 | BENCHMARK_PROBLEM / coupled synthetic | \(B_2\) | coupled P–T viability/reachability benchmark | SYNTHETIC_TRUTH if constructed | coupled method verification/synthetic evidence | ACTIVE DESIGN |
| GCBR-S5-B3 | QUALIFIED_CASE | \(B_3\) ladder position | final qualified thesis case | depends on qualified case evidence | H3 only after confirmatory gates | DEFERRED |

## 8.3 Stage-5 reference types

| ID | Class | Object | Role | Allowed use | Prohibited use |
|---|---|---|---|---|---|
| GCBR-S5-R01 | REFERENCE_SOLUTION | \(R_{ref}\) analytic/high-resolution numerical solution | set/probability convergence | numerical verification | call physical ground truth absent evidence |
| GCBR-S5-R02 | VALIDATION_REFERENCE | held-out trajectories / empirical evidence | intended-use validation | adequacy assessment | benchmark agreement alone |
| GCBR-S5-R03 | VALIDATION_REFERENCE / higher-fidelity | qualified higher-fidelity model/data | validation where empirical truth limited | bounded adequacy comparison | automatic truth status |
| GCBR-S5-O01 | ORACLE | ideal-information/control upper bound | diagnostic ceiling | upper-bound comparison | achievable baseline or validation evidence |

Permanent:

~~~math
\boxed{
\text{benchmark agreement alone}
\neq
\text{Stage-5 validation}.
}
~~~

---

# 9. Stage 6 / H4 registry

## 9.1 Intervention baselines/comparators

| ID | Class / subtype | Object | Role | Status |
|---|---|---|---|---|
| GCBR-S6-01 | BASELINE / COUNTERFACTUAL_INTERVENTION_BASELINE | \(a_0\) status quo / no additional strategic intervention | primary incremental consequence counterfactual | ACTIVE |
| GCBR-S6-02 | BASELINE / BUSINESS_AS_USUAL_BASELINE | \(a_{BAU}\) | conditional current-practice/minimum-required lifecycle counterfactual | CONDITIONAL |
| GCBR-S6-03 | COMPARATOR_SET | \(\mathcal A_R^+\) | H4 resilience-effective alternatives | ACTIVE DESIGN / membership deferred |
| GCBR-S6-04 | COMPARATOR_SET / MATCHED_EFFECT | similar-resilience alternatives | reduce intervention-strength confounding | CONDITIONAL |
| GCBR-S6-05 | COMPARATOR / CURRENT_PRACTICE | real current-practice/code/agency intervention | external engineering comparator | CONDITIONAL; cannot be invented |

Only one primary counterfactual (\(a_0\) or \(a_{BAU}\)) may govern a declared analysis, prospectively frozen.

## 9.2 Stage-6 benchmark ladder

| ID | Global class | Stage label | Role | Claim ceiling | Status |
|---|---|---|---|---|---|
| GCBR-S6-B0 | VERIFICATION_FIXTURE | \(B_{6,0}\) | units/signs/PV/activity×factor/accessibility/EFX/EFY fixtures | implementation/accounting verification | ACTIVE |
| GCBR-S6-B1 | BENCHMARK_PROBLEM / subsystem | \(B_{6,1}\) | P/T intervention consequences independently | subsystem consequence credibility | ACTIVE DESIGN |
| GCBR-S6-B2 | BENCHMARK_PROBLEM / coupled synthetic | \(B_{6,2}\) | coupled intervention propagation + no-double-counting | coupled method verification/synthetic evidence | ACTIVE DESIGN |
| GCBR-S6-B3 | QUALIFIED_CASE | \(B_{6,3}\) ladder position | final H4 case + Stage6→7 handoff | H4 only after gates | DEFERRED |

## 9.3 Stage-6 references

| ID | Class | Example | Role | Allowed use | Prohibited use |
|---|---|---|---|---|---|
| GCBR-S6-R01 | REFERENCE_CALCULATION | \(I=\sum_r A_rEF_r\) hand check | accounting arithmetic verification | fixture comparison | empirical intervention validation |
| GCBR-S6-R02 | REFERENCE_CALCULATION | \(PV=C_0+\sum_y C_y/(1+r)^y\) | lifecycle-cost arithmetic verification | fixture comparison | cost-effectiveness proof |
| GCBR-S6-R03 | REFERENCE_CALCULATION | small-graph accessibility/path calculation | accessibility algorithm verification | hand verification | full-case accessibility validation |
| GCBR-S6-R04 | EXTERNAL_PRACTICE/FACTOR_REFERENCE | ISO/NIST/EPA/TRACI/factor source | method/factor/boundary provenance | qualified accounting inputs/guidance | treat standard/factor as observed system outcome |
| GCBR-S6-V01 | VALIDATION_EVIDENCE | independent resource/cost/time/material/energy estimates | Stage-6 input/consequence validation | intended-use adequacy | benchmark self-reproduction |

Passing \(G_{B6}\) does not prove a real intervention effective, efficient or sustainable.

---

# 10. Stage 7 / H5 registry

## 10.1 Decision baseline/comparator

| ID | Class / subtype | Object | Role | Truth semantics | Status |
|---|---|---|---|---|---|
| GCBR-H5-01 | BASELINE / DECISION_BASELINE | \(\mathcal X_R\rightarrow\mathcal A_R^\star\) | resilience-only H5 decision arm | not truth/preference | ACTIVE DESIGN |
| GCBR-H5-02 | TREATMENT / DECISION_AUGMENTATION | \(\mathcal X_{R,S}\rightarrow\mathcal A_{R,S}^\star\) | resilience+sustainability arm | not truth/preference | ACTIVE DESIGN |

Both use the same admissible candidate set and common decision machinery.

## 10.2 Stage-7 benchmark ladder

| ID | Global class | Stage label | Role | Claim ceiling | Status |
|---|---|---|---|---|---|
| GCBR-S7-B0 | VERIFICATION_FIXTURE | \(B_{7,0}\) | feasibility/Pareto/Jaccard/regret/robustness arithmetic | implementation verification only | ACTIVE |
| GCBR-S7-B1 | BENCHMARK_PROBLEM / synthetic table | \(B_{7,1}\) | known feasible/dominated/set-change/regret structure | decision-engine verification/synthetic validation | ACTIVE |
| GCBR-S7-B2 | BENCHMARK_PROBLEM / synthetic handoff | \(B_{7,2}\) | full synthetic \(I_{6\to7}^{v2}\) consumption | integrated decision-engine verification | ACTIVE |
| GCBR-S7-B3 | QUALIFIED_CASE | \(B_{7,3}\) ladder position | final H5 case | H5 only after all upstream + decision gates | DEFERRED |

## 10.3 Stage-7 references

| ID | Class | Object | Role | Claim ceiling |
|---|---|---|---|---|
| GCBR-S7-R01 | REFERENCE_CALCULATION | hand Pareto fixture | verify dominance/Pareto implementation | algorithm only |
| GCBR-S7-R02 | REFERENCE_CALCULATION | Jaccard fixture | verify H5 set-distance arithmetic | algorithm only |
| GCBR-S7-R03 | REFERENCE_CALCULATION | regret fixture | verify regret calculation | algorithm only |
| GCBR-S7-R04 | REFERENCE_CALCULATION | robustness-coverage fixture | verify robustness calculation | algorithm only |
| GCBR-S7-R05 | REFERENCE_CALCULATION | weight/normalization sensitivity fixture if activated | verify value-model implementation | algorithm/value implementation only |

Permanent inheritance rule:

~~~math
\boxed{
\Lambda_7
\le
\min(
\Lambda_3,
\Lambda_4,
\Lambda_5,
\Lambda_6
)
}
~~~

for claims depending on those stages.

A Stage-7 decision over synthetic benchmark inputs remains a synthetic benchmark decision.

---

# 11. Ground-truth policy

The label GROUND_TRUTH is authorized only when the physical truth needed for the stated comparison is genuinely known or defensibly observable at the required resolution.

Allowed:
- exact analytic truth for a mathematical fixture, classified primarily as analytic/synthetic truth rather than empirical ground truth;
- physically measured state/event with uncertainty small enough and independently demonstrated for the intended validation purpose.

Not automatically allowed:
- a higher-fidelity model;
- a calibrated model;
- a model-generated OD matrix;
- an imputed/reconstructed service trajectory;
- a literature value;
- an agency standard;
- a benchmark that reproduces itself;
- a held-out dataset with unresolved measurement/coverage error.

Therefore the default status of empirical truth objects is VALIDATION_EVIDENCE / VALIDATION_REFERENCE with uncertainty, unless the stronger ground-truth label is explicitly justified.

---

# 12. Independence and data-role rules

## 12.1 Calibration versus validation

~~~math
\boxed{
D_{cal}\cap D_{val}=\varnothing
}
~~~

where independence is required by the declared validation design.

Held-out/reference data may not be used to:
- refit treatment-specific parameters;
- select the preferred model;
- choose materiality thresholds from target effects;
- choose scenario membership based on outcomes.

## 12.2 Benchmark versus validation

~~~math
\boxed{
\text{benchmark reproduction}
\not\Rightarrow
\text{validation}.
}
~~~

## 12.3 Reference solution versus validation evidence

~~~math
\boxed{
\text{numerically trusted solution}
\not\Rightarrow
\text{real-system evidence}.
}
~~~

## 12.4 External reference versus requirement

~~~math
\boxed{
\text{published/standard value}
\not\Rightarrow
\text{applicable requirement}.
}
~~~

Applicability, jurisdiction, scope and authority must be separately established.

---

# 13. Claim-ceiling rules by class

| Global class | Maximum default claim |
|---|---|
| VERIFICATION_FIXTURE | implementation/math/code correctness for tested property |
| BENCHMARK_PROBLEM | method behavior on declared benchmark |
| SYNTHETIC_TRUTH | synthetic/controlled discrimination only |
| REFERENCE_SOLUTION | numerical/mathematical accuracy for same problem |
| REFERENCE_CALCULATION | arithmetic/algorithm reproduction |
| VALIDATION_EVIDENCE / REFERENCE | intended-use adequacy within declared validation domain |
| GROUND_TRUTH | only the specifically known physical quantity/domain |
| ORACLE | ideal upper-bound diagnostic |
| BASELINE / COMPARATOR | relative difference only; no truth privilege |
| EXTERNAL_PRACTICE/FACTOR_REFERENCE | provenance/method/input support only |
| REQUIREMENT_THRESHOLD | constraint/target applicability only |
| QUALIFIED_CASE | case-specific evidence/claims only after case gates |
| TREATMENT | relative effect under matched comparison only |
| EVIDENCE_SOURCE_REFERENCE | evidence/provenance support within cited validity domain |
| AUXILIARY_COUNTERFACTUAL_MODEL | reconstruction-task adequacy only |

Downstream claims cannot exceed the weakest required upstream claim ceiling.

---

# 14. Required global registry fields for future additions

Every new object added after this freeze must record:

~~~text
registry_id
global_class
subtype
stage
hypothesis
object_name
scientific_role
source_or_generator
data_role = calibration / validation / held-out / benchmark / confirmatory / none
independence_status
truth_semantics
units_or_quantity
scenario/case domain
allowed_use
prohibited_use
claim_ceiling
uncertainty
validity_domain
authority_path
authority_git_blob
version/date
status
~~~

No unnamed “reference” is permitted in confirmatory documentation after P1.4. Its subtype must be explicit.

---

# 15. Cross-hypothesis baseline map

| Hypothesis | Primary baseline/reference arm | Treatment | Baseline type |
|---|---|---|---|
| H1 | \(M_1\); \(M_0\) secondary uncoupled reference | \(M_2\) | rival-model baseline |
| H2 | \(\mathscr N_0=P+T\) | \(\mathscr N_1,\mathscr N_2\) | information/organization architecture baseline |
| H3 | \(Q_{conv}\) / \(R_{curve}\) | \(Q_{VRR}=Q_{conv}+\mathfrak R_T\) | information baseline |
| H4 | \(a_0\) or prospectively authorized \(a_{BAU}\) for deltas; pairwise alternatives within \(\mathcal A_R^+\) | \(a_k\) | intervention counterfactual + comparator set |
| H5 | \(\mathcal X_R\rightarrow\mathcal A_R^\star\) | \(\mathcal X_{R,S}\rightarrow\mathcal A_{R,S}^\star\) | decision baseline |

This map is subordinate to GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md and may not change hypothesis meaning.

---

# 16. Current P1.4 status

~~~math
\boxed{
G_{P1.4}^{design}=PASS
}
~~~

if and only if:
- all active cross-stage baseline/comparator roles are typed;
- benchmark ladders are separated from qualified final cases;
- reference subtypes are explicit;
- validation evidence is separated from verification/reference arithmetic;
- ground-truth language is conservative;
- no benchmark or self-generated output is promoted to empirical validation;
- no requirement threshold is misclassified as a reference.

This is a classification/design gate, not a validation result.


---

# 17. Source authority snapshot

| Role | Authority | Git blob SHA |
|---|---|---|
| global model/experiment/validation governance | thesis/00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md | 662439d04ec4297a1c5cbba047fc40c46d17db57 |
| Stage-1 verification fixture evidence | project/STAGE1_GENERIC_FIXTURE_VERIFICATION_REPORT_2026-09-18.md | def6178742d4bca3f4616267a23a0838b555b187 |
| H1 observation/validation architecture | project/H1_VALIDATION_OBSERVATION_SERVICE_REQUIREMENT_ARCHITECTURE_V1.md | 20f47ce3eeefe68c143b97e2ee4c660314b919ea |
| Stage-3 benchmark/VVUQ authority | project/stage3/STAGE3_UNCERTAINTY_BENCHMARK_VVUQ_PROTOCOL_V2.md | 83abc66ff5f5d0f66c421847fa789832ac94ab24 |
| Stage-4 estimation validation state | project/stage4/03_cases/greensboro_greenevt_smartds/02_estimation/STAGE4_ESTIMATION_VALIDATION_V1.md | 864b7a9687d24a680669f08f68a5ae7235815238 |
| Stage-5 benchmark/reference authority | project/stage5/04_benchmark/STAGE5_BENCHMARK_AND_REFERENCE_PROTOCOL_V1.md | 48fe92dda9bc819b6769c9e7263734df7461b26f |
| Stage-5 VVUQ authority | project/stage5/08_VVUQ/STAGE5_VVUQ_PROTOCOL_V1.md | 2c62b12bece9d4ab041255c63c040c9efa407639 |
| Stage-6 baseline/comparator support | project/stage6/02_interventions/STAGE6_INTERVENTION_BASELINE_AND_COMPARATOR_PROTOCOL_V1.md | 95e7ce3c9119d5e10fc4d700c541dbb807ca9032 |
| Stage-6 active benchmark/reference authority | project/stage6/05_benchmark/STAGE6_BENCHMARK_AND_REFERENCE_PROTOCOL_V2.md | 41bf51dde8c651d46425d9ac037734c70fcb8657 |
| Stage-6 VVUQ authority | project/stage6/07_vvuq/STAGE6_VVUQ_PROTOCOL_V2.md | f050d5d334f2e2a6587785241b30c9ae5606db55 |
| Stage-7 benchmark/reference authority | project/stage7/STAGE7_BENCHMARK_AND_REFERENCE_PROTOCOL_V2.md | c262d81d217f47bf5d51200324335e6b72fbd724 |
| Stage-7 VVUQ/decision-stability authority | project/stage7/STAGE7_VVUQ_AND_DECISION_STABILITY_PROTOCOL_V2.md | dad9344f78260587a2177954c0dee4d033e33a1b |
| H1–H5 global preregistration | project/global_integration/GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md | 9b80cb8a2bbb882b53ed5dd3f86d007596e0e9f6 |

## 18. Supersession note

Stage-6 benchmark protocol v1 remains useful only for detailed provenance such as examples of reference calculations and external practice/factor references.

Its active benchmark governance is superseded by Stage-6 benchmark protocol v2.

This registry therefore:
- takes benchmark-ladder semantics from v2;
- reuses non-conflicting reference-calculation provenance from v1;
- does not reactivate superseded v1 intervention-performance semantics.
