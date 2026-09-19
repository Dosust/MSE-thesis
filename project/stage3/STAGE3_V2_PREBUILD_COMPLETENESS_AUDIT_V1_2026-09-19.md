# Stage 3 v2 Pre-Build Completeness Audit v1

**Date:** 2026-09-19  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Branch:** `main`  
**Purpose:** determine, before writing Stage-3 v2, exactly which required scientific objects already exist, which are only fragmented/supporting, which are genuinely missing, and which case-specific items must remain deferred until data qualification.

## 1. Audit conclusion

```math
\boxed{
\text{Stage-3 scientific content is substantially developed}
\neq
\text{Stage-3 v2 constitution is complete}.
}
```

The repository contains strong Stage-3 theory and a mature H1/Level-2 experimental-control architecture, but it lacks a single active, case-independent Stage-3 constitution that compiles the current dependency contract into a clean Stage2→3→4 scientific interface.

### Decision

```math
\boxed{
G_{3,PREBUILD}=PASS
}
```

**Interpretation:** sufficient pre-existing material exists to begin the Stage-3 v2 constitution **without inspecting confirmatory outcomes or waiting for case-specific data**.

This is **not** Stage-3 empirical closure:

```math
\boxed{
G_{3,PREBUILD}=PASS
\quad\not\Rightarrow\quad
G_{3,CLOSURE}=PASS.
}
```

The current empirical/confirmatory Stage-3 state remains:

```text
NOT TESTED / BLOCKED BY PREREQUISITE EVIDENCE
```

## 2. Authorities and evidence inspected

### Current scientific authorities
- `project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`
- `project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`
- `project/CANONICAL_DEPENDENCY_CONTRACT_V1.md`
- `project/CANONICAL_NOTATION_TRANSLATION_LAYER_V1.md`
- current authority-drift cleanup under `project/global_integration/`

### Stage-3 material
- `project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md` — supporting theory only after authority cleanup
- `project/stage3/README.md`
- `project/stage3/STAGE3_EXECUTION_AND_CLOSURE_AUDIT_V1_2026-09-19.md`
- `project/stage3/STAGE3_GATE_RESULTS_V1_2026-09-19.csv`
- `project/stage3/STAGE3_SCENARIO_MATRIX_CAUSAL_COMPATIBILITY_AUDIT_V1_2026-09-19.md`
- `project/stage3/reference/Stage3_Reference_Database_v1.xlsx`

### H1 Level-2 implementation/control material
- `models/H1/level2/PROTOCOL_V1.md`
- `models/H1/level2/config/protocol_v1.json`
- `models/H1/level2/config/protocol_status_v1.json`
- `models/H1/level2/registries/dependency_registry_v1.csv`
- `models/H1/level2/registries/parameter_registry_v1.csv`
- `models/H1/level2/registries/qoi_registry_v1.csv`
- `models/H1/level2/registries/scenario_matrix_v1.csv`
- `models/H1/level2/registries/freeze_gate_register_v1.csv`
- development/held-out case manifest templates and blocked manifests
- code/test infrastructure under `models/H1/level2/`

### Downstream compatibility target
- `project/stage4/00_governance/STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md`

Stage 4 currently declares admissible input:

```math
I_4=(\mathcal G,\mathbb I^{qualified},\mathfrak M_3,Y^{phys},Q,\Lambda_3).
```

This creates a concrete target that Stage 3 v2 must satisfy.

---

# 3. Requirement-by-requirement audit

Status vocabulary:

```text
DONE    = current object exists in active/current-enough form;
PARTIAL = scientific content exists but is fragmented, legacy, or not constitutionally frozen;
MISSING = no explicit governed object/file exists;
BLOCKED = depends on case/data evidence and must remain unresolved before data;
LEGACY  = useful content exists but cannot be copied as active semantics without translation.
```

## R3-01 — Main Stage-3 scientific constitution

**Expected:** `project/stage3/STAGE3_SCIENTIFIC_CONSTITUTION_V2.md`

**Status:** **MISSING**

Evidence:
- no repository path matching `STAGE3_SCIENTIFIC_CONSTITUTION`;
- the root Stage-3 theory is now explicitly classified as supporting theory with legacy notation;
- the current `project/stage3/README.md` identifies execution status, not a data-independent constitution.

What already exists:
- RQ3/SO3;
- scientific role;
- generic hybrid-dynamics theory;
- execution gates;
- H1 protocol.

What must be created:
```math
\mathfrak S_3=
(RQ_3,SO_3,H_1,I_3,O_3,\mathcal M_3,\Theta_3,G_3,U_3,E_3,\Lambda_3)
```
or a notation-equivalent universal stage contract synchronized with the Stage-4 contract style.

**Action:** BUILD.

---

## R3-02 — Stage 2 → Stage 3 input contract

**Expected:** explicit active-notation handoff.

**Status:** **PARTIAL / NOT CANONICALLY PACKAGED**

Strong existing content:
- canonical dependency object:
  ```math
  \mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e);
  ```
- executable semantics:
  ```math
  \mathcal X:\Sigma_e\mapsto\Xi_e;
  ```
- provenance, uncertainty, validation state, guard, mechanism parameters, optional memory and delay semantics are already defined;
- Level-2 `dependency_registry_v1.csv` contains source, receiver, ports, carrier/service, `Phi_e`, `gamma_e`, `theta_e`, `zeta_e`, provenance, evidence state, uncertainty and validation pointer.

Defect:
- no explicit `STAGE2_TO_STAGE3` handoff file exists;
- root Stage-3 theory still contains four flat legacy `\mathfrak I_{ij}^{\alpha\beta}` references;
- current case readiness is stricter than causal admission: even `EV_T_to_P` is Stage2→3 BLOCKED because parameter/uncertainty readiness is incomplete.

Required v2 distinction:

```math
\boxed{
G_2(e,c)=PASS
\neq
G_{2\to3}(e,c)=PASS.
}
```

A causal mechanism can be scientifically accepted yet not simulation-ready.

**Action:** CONSOLIDATE + FREEZE schema.  
**Data values:** DEFER.

---

## R3-03 — State / input / output / QOI ontology

**Status:** **PARTIAL**

Existing theory defines:
- `Y=[x_P,x_T,z_I,z_O]^T`;
- continuous/quasi-continuous versus discrete states;
- explicit hybrid mode `m(t)`;
- power-state examples;
- road/EV/rail state examples;
- information-state and organizational-process concepts;
- event sequence and service/recovery trajectories as outputs.

Level-2 implementation already distinguishes:
- parameters;
- dependency mechanisms;
- primary/secondary QOIs;
- case manifest identifiers.

Critical unresolved issue:
the old theory's `z_I,z_O` Stage-3 state definitions must be reconciled with current Stage-4 semantics.

Stage 4 requires:
```math
Y^{phys}_t=(x_P(t),x_T(t),z_{PT}(t))
```
and separately owns observation, information actually available, estimator belief, organizational state and feasible control.

Therefore Stage 3 v2 must explicitly decide which `I/O` quantities are:
1. genuine dynamic plant/environment states needed to generate physical truth;
2. Stage-4 epistemic/organizational states that Stage 3 must **not** duplicate.

Mandatory distinctions:
```math
\text{state}
\neq
\text{algebraic variable}
\neq
\text{input}
\neq
\text{parameter}
\neq
\text{mode}
\neq
\text{event}
\neq
\text{QOI}.
```

**Action:** CONSOLIDATE + REPAIR boundary.  
This is a **design task**, not a data blocker.

---

## R3-04 — Generic mathematical dynamics contract

**Status:** **PARTIAL / STRONG SUPPORTING CONTENT**

The root theory already contains:
- continuous/quasi-continuous dynamics;
- algebraic constraints;
- discrete resets;
- mode transitions;
- topology transitions;
- delayed-history terms;
- native power and transport dynamics;
- dependency-to-dynamics translation;
- dynamic topology;
- uncertainty;
- co-simulation principles.

This is scientifically mature supporting content.

Defects:
- dependency notation must be replaced by active `\mathfrak d_e` semantics;
- the v2 constitution must separate **generic admissible equation classes** from **case-selected equations**;
- the executable bridge
  ```math
  \mathfrak d_e\rightarrow\Xi_e\rightarrow F_{\mathcal G}^{m}
  ```
  must become explicit.

**Action:** TRANSLATE + CONSOLIDATE.  
Do not re-research this from zero.

---

## R3-05 — Hybrid / event / multirate time semantics

**Status:** **PARTIAL / STRONG**

Already established:
```math
\text{event time}
\neq
\text{causal delay}
\neq
\text{characteristic timescale}.
```

The theory also supports:
- heterogeneous subsystem clocks;
- delayed terms;
- event resets;
- multirate co-simulation;
- dynamic topology.

Level-2 audit further establishes for Q05:
- charging start/end in minutes;
- audited OpenDSS workflow commonly uses 5-min updates;
- no additional empirical electrical latency is demonstrated.

Missing in the active constitution:
- a single typed timing registry distinguishing:
  ```math
  t_{event},\delta_e,\tau_e,\Delta t_{solver},\Delta t_{comm},T_{horizon};
  ```
- generic synchronization admissibility and convergence requirements.

**Action:** CONSOLIDATE.  
Case-specific time-step values remain DEFERRED.

---

## R3-06 — Model-family selection protocol

**Status:** **PARTIAL**

Existing:
- root theory explicitly allows different equation classes and warns against maximum-possible fidelity;
- power may be algebraic/QSTS/dynamic-DAE depending on RQ;
- transport may use conservation law, CTM, dynamic assignment or microscopic simulation;
- Level-2 current strong candidate is OpenDSS quasi-static/QSTS + GreenEVT/SUMO.

Current gate:
```text
G3-MC = OPEN
```

Reason:
final model class must follow QOI/resolution, case and mechanism requirements.

What is missing:
an outcome-blind, case-independent selection table:
```text
candidate family
| admissible timescale
| required states
| QOIs supported
| coupling compatibility
| data requirement
| numerical burden
| VVUQ obligation
| rejection rule.
```

**Action:** BUILD protocol from existing theory.  
**Final model choice:** DEFER.

---

## R3-07 — H1 comparator architecture

**Status:** **DONE STRUCTURALLY**

Current frozen Level-2 protocol defines:
```math
M_0=\text{independent},\qquad
M_1=\text{static/algebraic coupling},\qquad
M_2=\text{dynamic causal coupling}.
```

It also freezes:
- matched scenario logic;
- common random numbers;
- identical exogenous conditions;
- independent-reference requirement for superiority;
- divergence-only claim when reference is absent;
- outcome-neutral claim ladder.

This is high-quality reusable material.

Remaining issue:
the current scenario matrix contains causal ablations that conflict with the latest Stage-2 G2 case audit.

Therefore:
- **comparator architecture = DONE**;
- **current case-specific scenario realization = BLOCKED / requires amendment**.

**Action:** IMPORT structural comparator rules into v2; do not import blocked mechanism memberships.

---

## R3-08 — QOI registry

**Status:** **PARTIAL / MACHINE REGISTRY EXISTS**

Existing registry:
`models/H1/level2/registries/qoi_registry_v1.csv`

Primary H1 families:
- cascade;
- service loss;
- spatial propagation;
- recovery.

Secondary quantities include:
- power/transport service-loss integrals;
- ENS;
- recovery times;
- queue/access/transport consequences.

Good scientific control:
```text
model consequence != model accuracy
```
and independent reference is required for predictive-error claims.

Current gate:
```text
G3-Q = BLOCKED
```
because exact primary metrics, reference and horizons are not frozen.

Important distinction for v2:
the **QOI ontology can be frozen now**, while **exact case metric definitions/materiality thresholds remain deferred**.

**Action:** CONSOLIDATE registry schema + ownership.  
**Exact confirmatory metrics:** DEFER.

---

## R3-09 — Scenario architecture

**Status:** **PARTIAL / STRUCTURE EXISTS, CURRENT MATRIX NOT AUTHORIZED**

Existing:
- `scenario_matrix_v1.csv`;
- protocol-defined hazard levels;
- common-random-number matching;
- ablation structure;
- case-manifest template;
- development and held-out role separation.

Critical incompatibility:
current matrix includes:
- `EV_P_to_T`;
- `SIGNAL_P_to_T`;
- `REPAIR_T_to_P`;
- `FULL_DYNAMIC`;

while latest case-specific Stage-2 causal gates block those mechanisms.

Therefore:
```math
\boxed{
\text{scenario schema exists}
\neq
\text{current scenario matrix authorized}.
}
```

Stage 3 v2 should define a generic scenario object with a dynamic admitted-mechanism field:
```math
\omega_s=
(Y_0,\mathcal G_0,\eta_s,D_s,\Theta_s,m_0,
\mathbb I^{ready}_s,u_s,T_s,seed_s).
```

Case scenarios may include only mechanisms satisfying Stage2→3 readiness.

**Action:** CONSOLIDATE schema; VERSION current matrix later after case-gate changes.

---

## R3-10 — Uncertainty contract

**Status:** **PARTIAL / STRONG IMPLEMENTATION SUPPORT**

Existing:
- canonical dependency uncertainty `\mathcal U_e`;
- parameter registry with uncertainty type/evidence grade;
- explicit separation of aleatory and epistemic uncertainty;
- model uncertainty is recognized;
- UQ sequence:
  ```text
  registry → screening → global sensitivity → propagation
  ```;
- Morris/Sobol candidate methods and sample-growth sequence are defined.

Current gate:
```text
G3-U = BLOCKED
```
because bounds/distributions and convergence rule are not frozen.

What v2 still needs:
one Stage-3 taxonomy:
```math
U_3=(U_\theta,U_{IC},U_\eta,U_{\mathbb I},U_M,U_N)
```
with ownership, propagation and claim implications.

**Action:** CONSOLIDATE taxonomy now.  
**Numerical distributions/bounds:** DEFER.

---

## R3-11 — Benchmark / verification / validation architecture

**Status:** **PARTIAL / STRONG BUT NOT PACKAGED AS STAGE-3 v2**

Existing:
- code verification → solution verification → submodel validation → coupled prediction assessment;
- nested-limit requirements;
- conservation/unit checks;
- timestep/grid refinement;
- model-reference distinction;
- realistic-synthetic ≠ observational validation;
- independent reference required for predictive superiority;
- preview fixture reproduced exactly;
- tests exist under `models/H1/level2/tests/`.

Current empirical gate:
```text
G3-N = BLOCKED,
G3-V = BLOCKED.
```

Missing before data:
a constitution-level benchmark ladder, e.g.
```math
B_{3,0}\rightarrow B_{3,1}\rightarrow B_{3,2}\rightarrow B_{3,3},
```
with exact purpose and claim ceiling for:
- analytic/unit fixtures;
- independent subsystem benchmarks;
- coupled synthetic benchmark;
- qualified case.

**Action:** CONSOLIDATE + ADD benchmark ladder.  
**Execution:** DEFER.

---

## R3-12 — Stage 3 → Stage 4 handoff

**Status:** **MISSING AS STAGE-3 CONTRACT / DOWNSTREAM TARGET EXISTS**

No `STAGE3_TO_STAGE4` file exists.

However Stage 4 already freezes its admissible input:
```math
I_4=(\mathcal G,\mathbb I^{qualified},\mathfrak M_3,Y^{phys},Q,\Lambda_3).
```

This is a strong downstream contract target.

Stage 3 v2 therefore needs to output at minimum:
```math
Z_3=
(\mathfrak M_3,Y^{phys}(t),\mathcal G(t),m(t),
\mathbb I^{active}(t),Q(t),\mathbb U_3,\Lambda_3)
```
subject to reconciliation with Stage-4 notation.

Mandatory prohibition:
```math
\boxed{
\text{Stage 3 does not output }b_t,\widehat Y_t,
\mathcal I_t,\mathcal U_{feas},u_t.
}
```

Those are Stage-4 objects.

**Action:** BUILD explicit handoff.

---

## R3-13 — Claim ceiling

**Status:** **PARTIAL / STRONG RULES EXIST**

Existing Level-2 claim ladder:
- preview fixture → software/mechanism verification only;
- realistic-synthetic development → reproducible model differences;
- qualified independent reference + frozen metrics → explanatory/predictive comparison;
- all preregistration/data gates closed → confirmatory H1 test.

Existing Stage-3 audit correctly states:
```text
NOT TESTED / BLOCKED BY PREREQUISITE EVIDENCE
```
and explicitly prevents preview values from becoming thesis evidence.

Missing:
one constitution-level `\Lambda_3` object that maps each verification/validation state to allowed/prohibited thesis wording.

**Action:** CONSOLIDATE into v2.

---

## R3-14 — Stage-3 design freeze and manifest

**Status:** **MISSING**

No repository file exists matching:
- `STAGE3_DESIGN_PROTOCOL_FREEZE_V2.md`;
- Stage-3 v2 finalization manifest.

Current `STAGE3_EXECUTION_AND_CLOSURE_AUDIT...` is an empirical/execution audit, not a design freeze.

**Action:** BUILD after the v2 package passes internal consistency audit.

---

# 4. Existing gate state must not be confused with design completeness

Current execution audit reports:

```text
G3-A   PASS
G3-MC  OPEN
G3-X   OPEN
G3-T/H OPEN
G3-S   OPEN
all other execution/closure gates predominantly BLOCKED.
```

Those statuses answer:

> Can the selected realistic/confirmatory Stage-3 case be executed and closed now?

They do **not** answer:

> Can we write the case-independent Stage-3 scientific constitution now?

The audit conclusion is:

```math
\boxed{
\text{case execution blocked}
\quad\text{but}\quad
\text{constitution design is admissible now}.
}
```

This distinction prevents unnecessary data dependence in the scientific architecture.

---

# 5. What is genuinely DONE already

The following should be reused rather than reinvented:

1. **RQ3 / SO3 / H1 mapping** — current canonical authority exists.
2. **Active dependency primitive** — `\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)`.
3. **Executable dependency concept** — `\mathcal X:\Sigma_e\mapsto\Xi_e`.
4. **Native physics remain distinct** — coupling modifies receiver physics, does not replace it.
5. **Hybrid equation classes** — continuous/algebraic/discrete-event/mode/topology changes.
6. **Time distinction** — event time ≠ causal delay ≠ characteristic timescale.
7. **Multirate/co-simulation principle**.
8. **M0/M1/M2 experimental family**.
9. **Outcome-blind case selection principle**.
10. **Matched/common-random-number experiment principle**.
11. **Parameter evidence hierarchy**.
12. **Machine parameter/QOI/dependency registries**.
13. **Aleatory/epistemic separation and UQ workflow**.
14. **Verification ≠ validation ≠ hypothesis support**.
15. **Independent reference required for predictive superiority**.
16. **Strong claim ceiling for preview/realistic-synthetic/confirmatory use**.
17. **Stage-4 downstream admissible-input contract already exists**.

---

# 6. What is genuinely MISSING before Stage-3 v2 can be frozen

These are architecture/governance gaps, not data gaps:

```text
M1. one active Stage-3 v2 constitution;
M2. one explicit Stage2→3 handoff/readiness contract;
M3. one active state/input/output/QOI ontology;
M4. one model-family selection protocol;
M5. one typed hybrid/multirate timing registry;
M6. one generic scenario schema independent of currently blocked mechanisms;
M7. one consolidated Stage-3 uncertainty taxonomy;
M8. one Stage-3 benchmark/VVUQ ladder;
M9. one explicit Stage3→4 handoff contract;
M10. one formal Stage-3 claim-ceiling object;
M11. one design-freeze file;
M12. one finalization/hash manifest.
```

These can all be built **before case data inspection**.

---

# 7. What must remain DEFERRED until data/case qualification

The following must **not** be invented while writing v2:

```text
D1. development feeder ID;
D2. held-out feeder ID;
D3. final road subnetwork;
D4. final flood geometry/intensity/duration;
D5. charger power / efficiency / energy distributions;
D6. blocked Stage-2 mechanisms;
D7. final power/transport model-family selection where case evidence is required;
D8. exact numerical time steps/communication steps;
D9. exact H1 primary error metrics if independent reference is unresolved;
D10. numerical V&V tolerances;
D11. UQ convergence threshold;
D12. confirmatory delta_1/materiality rule if evidence basis is unresolved;
D13. M0/M1/M2 results;
D14. H1 support/not-support conclusion.
```

The constitution should contain **slots and rules** for these, not values.

---

# 8. Important defects the v2 constitution must resolve

## Defect A — legacy dependency notation
Root Stage-3 theory still contains four flat-object uses:
```math
\mathfrak I_{ij}^{\alpha\beta}.
```
v2 must contain zero active uses except explicit migration notes.

## Defect B — Stage-3 / Stage-4 state-boundary ambiguity
The old Stage-3 theory places information and organization states directly in `Y`, while current Stage 4 owns epistemic information, organization and feasible control.

v2 must explicitly distinguish:
```math
\text{physical/dynamic truth generated by Stage 3}
\neq
\text{information available / belief / organizational decision state in Stage 4}.
```

## Defect C — causal admission versus executable readiness
Current case:
```math
EV_{T\to P}: G_2=PASS
\quad\text{but}\quad
G_{2\to3}=BLOCKED.
```
v2 needs a formal readiness gate.

## Defect D — scenario matrix predates latest causal gate
The existing `FULL_DYNAMIC` and several mechanism ablations are currently unauthorized.
v2 must define the schema without hardcoding blocked mechanisms.

## Defect E — model family versus implementation choice
The theory names many admissible families and the Level-2 protocol has a strong candidate, but there is no frozen outcome-blind selection decision function.

## Defect F — QOI ontology versus confirmatory metric
The QOI families are structurally known; exact predictive-error metrics are not.
v2 must preserve:
```math
\text{QOI family freeze}
\neq
\text{final confirmatory distance/threshold freeze}.
```

---

# 9. Pre-build completeness matrix

| Required v2 output | Scientific content available? | Explicit governed artifact? | Case/data dependency? | Audit status |
|---|---:|---:|---:|---|
| Main constitution | substantial | no | no | **MISSING artifact** |
| Stage2→3 contract | strong fragments | no | values only | **PARTIAL** |
| State/input/output/QOI ontology | strong fragments | no | no | **PARTIAL** |
| Generic dynamics contract | strong | legacy file only | no | **PARTIAL/LEGACY** |
| Time/hybrid/multirate semantics | strong | fragmented | values only | **PARTIAL** |
| Model-family selection | moderate/strong | no dedicated protocol | final choice partly | **PARTIAL** |
| M0/M1/M2 comparator | yes | yes | execution only | **DONE structurally** |
| QOI registry | yes | yes | exact metrics partly | **PARTIAL** |
| Scenario architecture | yes | current matrix incompatible | realization yes | **PARTIAL/BLOCKED realization** |
| Uncertainty contract | strong | fragmented | distributions yes | **PARTIAL** |
| Benchmark/VVUQ | strong | no v2 benchmark protocol | execution yes | **PARTIAL** |
| Stage3→4 handoff | downstream target exists | no Stage-3 file | no | **MISSING** |
| Claim ceiling | strong | fragmented | no | **PARTIAL** |
| Design freeze/manifest | no | no | no | **MISSING** |

---

# 10. Minimum safe build sequence

The most efficient order is:

```text
1. Stage2→3 readiness/handoff contract
2. Stage-3 state/input/output/QOI ontology
3. Stage-3 scientific constitution v2
4. hybrid/time/multirate semantics normalization
5. model-family selection protocol
6. generic scenario schema
7. uncertainty + benchmark/VVUQ protocol
8. Stage3→4 handoff
9. internal contradiction audit
10. design freeze + manifest
```

The constitution can be drafted at step 3 and finalized after steps 4–8.

---

# 11. Go / no-go decision

## GO for Stage-3 v2 design

```math
\boxed{
\text{GO: build the case-independent Stage-3 v2 package now}.
}
```

Reasons:
- canonical RQ/SO/H is fixed;
- dependency semantics are fixed;
- enough physics/hybrid theory exists;
- H1 comparator architecture exists;
- machine registries exist;
- downstream Stage-4 input is known;
- the remaining architecture gaps do not require target-result inspection.

## NO-GO for realistic/confirmatory Stage-3 execution

```math
\boxed{
\text{NO-GO: do not execute/interpret realistic H1 confirmation yet}.
}
```

Reasons:
- case IDs are not frozen;
- Stage2→3 mechanism readiness incomplete;
- parameter distributions incomplete;
- QOI error metrics/reference unresolved;
- VVUQ tolerances unresolved;
- scenario matrix conflicts with current causal gates;
- confirmatory authorization is false.

---

# 12. Immediate next scientific task

The first artifact should **not** be the whole constitution in one jump.

Build first:

```text
project/stage3/STAGE3_STAGE2_TO_STAGE3_INPUT_AND_READINESS_CONTRACT_V2.md
```

because every subsequent Stage-3 object depends on what is legally/scientifically allowed to enter Stage 3.

Once that contract is internally consistent, build:

```text
STAGE3_STATE_INPUT_OUTPUT_QOI_ONTOLOGY_V2.md
```

and then compile both into:

```text
STAGE3_SCIENTIFIC_CONSTITUTION_V2.md
```

This order minimizes rework and prevents the constitution from reintroducing Stage-2 or Stage-4 objects incorrectly.
