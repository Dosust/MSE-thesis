# Phase 0 — Representation Benchmark for Infrastructure Interdependency

**Status:** ACTIVE BENCHMARK — supports but does not yet revise the canonical ontology.  
**Purpose:** test whether the proposed Phase-0 dependency grammar adds value beyond established representation families.

## 1. Benchmark question

```math
\boxed{\text{What can existing infrastructure-interdependency representations express, and what residual capability is still missing for the thesis problem?}}
```

The benchmark compares representation families against the requirements of a dynamic Power–Transportation–Information–Organization system-of-systems.

---

## 2. Requirements matrix

The candidate representation requirements are:

```math
\mathcal R=
\{\text{direction},\text{mechanism},\text{physics},\text{service},\text{state},\text{time},\text{delay},\text{context},\text{feedback},\text{organization},\text{uncertainty},\text{evidence},\text{composability}\}.
```

Each representation family is evaluated for whether these are first-class, possible with extension, or largely external to the method.

| Representation family | Primary strength | Main limitation for this thesis | Phase-0 implication |
|---|---|---|---|
| Binary dependency graph | simple direction/topology | mechanism, state, evidence and physics are mostly absent | baseline only |
| Multilayer/multiplex network | heterogeneous layers and cross-layer structure | edge semantics may remain generic | structural host, not sufficient complete semantics |
| Network-of-networks / interdependent network | reciprocal structural dependency and cascades | often abstract dependency rules, limited organizational semantics | useful structural baseline |
| Infrastructure ontology | semantic typing, reusable domain knowledge | may not provide executable dynamics or service consequences | strong semantic predecessor |
| System dynamics | feedback and temporal behavior | structural asset/interface granularity can be coarse | useful causal/dynamic comparator |
| Agent-based model | heterogeneous actors and decisions | expensive validation; physical laws may be simplified | useful organizational/behavioral comparator |
| Bayesian / probabilistic network | uncertainty and conditional dependence | causal/physical semantics depend on model construction | uncertainty layer, not complete SoS grammar |
| Temporal network | time-respecting paths and evolving relations | physical mechanism and authority may remain generic | important dynamic comparator |
| Hybrid dynamical system | continuous + discrete physical/operational evolution | cross-domain semantics are not automatically encoded | dynamic engine, not ontology |
| Cyber-physical / socio-technical architecture | physical, information/control, human/organization integration | usually domain architecture, not necessarily reusable cross-infrastructure dependency contract | strong conceptual predecessor |
| Shared-state SoS formulation | decisions, resources, stakeholders and time | may not expose every typed cross-domain dependency as a reusable object | major SoS predecessor |
| Coupled P–T equilibrium / co-simulation | high domain fidelity for selected mechanisms | often tailored to specific P–T mechanisms and not intended as general interdependency grammar | important domain benchmark |

---

## 3. What is already solved [E]

The following must not be claimed as thesis novelty without stronger evidence:

1. representing multiple infrastructure systems as multiple network layers;
2. distinguishing dependency from reciprocal interdependency;
3. modeling cascades across interdependent networks;
4. incorporating physical, informational/control, and organizational/human dimensions;
5. representing time-varying infrastructure interactions;
6. integrating uncertainty into infrastructure models;
7. coupling Power and Transportation through EV charging, V2G, traction power, or restoration access;
8. using ontologies to organize cross-domain infrastructure knowledge.

---

## 4. Candidate residual gap [P]

The current candidate residual gap is not "absence of a unified framework" in the universal sense.

The defensible candidate question is:

```math
\boxed{\begin{minipage}{0.84\textwidth}
Can a minimal typed dependency contract make structural, physical, informational, organizational, temporal and epistemic representations interoperable while preserving sector-specific physics and measurable service consequence?
\end{minipage}}
```

This gap must be narrowed or rejected if an existing representation already provides the same capabilities with comparable or lower complexity and validated engineering benefit.

---

## 5. Competing models for Phase-0 testing

### Baseline B0 — binary directed edge

```math
B_0=(s,r).
```

### Baseline B1 — weighted multilayer edge

```math
B_1=(s,r,w).
```

### Baseline B2 — temporal weighted edge

```math
B_2=(s,r,w(t),\delta(t)).
```

### Baseline B3 — typed mechanism edge

```math
B_3=(s,r,\rho,m,q,w(t),\delta(t)).
```

### Proposed candidate P0 — evidence-aware dynamic dependency contract

```math
P_0=(s,r,\rho,m,q,M,z(t),w(t),\delta(t),c(t),U,\mathcal H_t).
```

The experiment is not to prove that `P0` is richer. That is obvious by construction. The experiment is to test whether its added fields change a scientifically or engineering-relevant result.

---

## 6. Engineering verification cases

### Case A — normal EV charging

Question:

```math
\text{Can the representation explain how transportation demand changes electrical loading and how power availability changes mobility?}
```

Expected critical fields: direction, mechanism, transferred quantity, dynamic strength.

### Case B — outage and charging/routing cascade

Question:

```math
\text{Can the representation explain time-dependent }P\rightarrow T\rightarrow P\text{ feedback?}
```

Expected critical fields: functional state, time, delay, context, feedback path.

### Case C — restoration access and organizational authority

Question:

```math
\text{Can the representation distinguish physical road access from organizational permission, crew availability and decision latency?}
```

Expected critical fields: mechanism class, organizational semantics, delay, evidence state.

### Case D — inferred/hidden dependency

Question:

```math
\text{Can the model distinguish an observed statistical association from a physically verified dependency?}
```

Expected critical fields: epistemic/evidence status and mechanism.

### Case E — third-domain extension

Add Water without changing the grammar:

```math
\mathcal D_{PT}\rightarrow\mathcal D_{PTW}=\{P,T,W\}.
```

Question: does the representation remain structurally unchanged except for new entities and dependencies?

---

## 7. Metrics

The Phase-0 benchmark should not use only representational richness. Use at least:

### M1 — representation completeness
Fraction of required relation semantics represented without ad hoc external annotation.

### M2 — explanation fidelity
Whether the model reproduces the correct directed mechanism and feedback path for a verification case.

### M3 — dynamic prediction error
Where numerical models exist, compare predicted service/state trajectories under the same disturbance.

### M4 — decision divergence

```math
D_{decision}=\mathbf 1\{u^*(M_a)\neq u^*(M_b)\}
```

or an appropriate distance between intervention portfolios.

### M5 — model complexity
Number of fields, parameters, calibration requirements, and unavailable inputs.

### M6 — evidence traceability
Fraction of load-bearing dependency claims linked to explicit source/mechanism/confidence status.

### M7 — extensibility cost
Number of ontology/schema changes required to add a new infrastructure domain.

---

## 8. Decision rule

The proposed contract is retained only if its additional complexity is justified by measurable gain.

```math
\boxed{\Delta V_{engineering}>\Delta C_{model}}
```

where `Delta V_engineering` denotes added explanatory, predictive, or decision value and `Delta C_model` denotes added complexity/data burden.

If the richer representation does not alter engineering inference or decision quality over the selected test cases, simplify it.

---

## 9. Immediate Phase-0 research task

The next formal task is **field-ablation plus source verification**:

1. construct B0–B3 and P0 for Cases A–D;
2. identify which fields each case actually requires;
3. remove any field that never changes explanation, prediction, decision or evidence validity;
4. verify every retained field against high-rigor literature or engineering need;
5. test Case E for domain extensibility;
6. only then decide whether the canonical `P–T–I–O` ontology should be revised to the domain × aspect ontology.

---

## 10. Relationship to current canonical thesis files

This benchmark is subordinate to the currently frozen thesis files until formal revision:

- `CANONICAL_SYSTEM_DEFINITION.md`
- `FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`
- `CANONICAL_7_STAGE_FRAMEWORK.md`
- `RESEARCH_HYPOTHESES.md`

A future ontology revision must explicitly compare the frozen `S={P,T,I,O}` formulation against the tested domain × aspect formulation and record the reason for adoption or rejection.
