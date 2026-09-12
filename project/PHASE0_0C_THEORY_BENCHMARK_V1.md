# Phase 0 — 0C Existing-Representation Theory Benchmark v1.0

**Status:** CORE BENCHMARK PASS COMPLETE — diagnostic scoring frozen for inspected sources; literature saturation not yet established.  
**Gate:** Theoretical Decision Gate v1.0  
**Inputs:** `INTERDEPENDENCY_DEFINITION_REGISTER.md`, `REPRESENTATION_REQUIREMENTS_MATRIX.md`, `PHASE0_0C_SOURCE_REGISTER.md`  
**Date:** 2026-09-12

> **Interpretation rule:** A score of `0` means **not explicitly supported by the source evidence inspected in this pass**, not proof that the broader method can never represent that feature. Scores are conservative evidence codes, not universal judgments.

---

## 1. Frozen requirements

The benchmark uses the already frozen requirements:

```math
\mathcal R=\{R_1,\ldots,R_{12}\}.
```

| ID | Requirement |
|---|---|
| `R1` | constituent-system identity |
| `R2` | mechanism semantics |
| `R3` | directionality / reciprocity |
| `R4` | information/control relations |
| `R5` | organizational/human/authority relations |
| `R6` | state dependence |
| `R7` | time variation / delay / sequence |
| `R8` | feedback / mediated interdependency |
| `R9` | uncertainty / evidence status |
| `R10` | service/capability consequence |
| `R11` | preservation of domain-specific physics |
| `R12` | extensibility / cross-domain reuse |

Scoring:

```math
B_{jk}=\begin{cases}
0,&\text{not explicitly supported in inspected evidence},\\
1,&\text{indirect / partial / externally supplied},\\
2,&\text{explicit first-class support}.
\end{cases}
```

No weighted total is used for the ontology decision.

---

# 2. Representation families

| ID | Representation family / anchor source |
|---|---|
| `M01` | Maier — SoS architecting |
| `M02` | Rinaldi et al. — infrastructure interdependency conceptual framework |
| `M03` | Johansson & Hassel — structural + functional interdependency model |
| `M04` | Kivelä et al. — multilayer-network framework |
| `M05` | Nan & Sansavini — multilayer hybrid physical/control/human-organizational model |
| `M06` | ontology-based infrastructure-interdependency representations |
| `M07` | NIST CPS framework |
| `M08` | ISO/IEC/IEEE 42010 architecture-description framework |
| `M09` | temporal-network infrastructure-interdependency model |
| `M10` | dynamic coupled Power–Transportation equilibrium model |

---

# 3. Benchmark matrix

| Model | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `M01` SoS architecting | 2 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 0 | 1 | 1 | 2 |
| `M02` Rinaldi framework | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 2 |
| `M03` Johansson–Hassel | 2 | 2 | 2 | 1 | 0 | 1 | 1 | 2 | 0 | 2 | 1 | 2 |
| `M04` Multilayer networks | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 0 | 1 | 1 | 2 |
| `M05` Nan–Sansavini hybrid | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 |
| `M06` Ontology approaches | 2 | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 2 | 2 |
| `M07` NIST CPS | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 |
| `M08` ISO 42010 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 |
| `M09` Temporal networks | 1 | 1 | 2 | 0 | 0 | 2 | 2 | 2 | 2 | 1 | 0 | 2 |
| `M10` Dynamic P–T model | 2 | 2 | 2 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | 2 | 0 |

### Important warning

The matrix is **not** an ordinal ranking of scientific quality. Each model solves a different problem. A `0` for organization in a P–T equilibrium model, for example, means organization is not explicit in the inspected formulation; it does not imply the model is scientifically deficient for its intended purpose.

---

# 4. Requirement-by-requirement synthesis

## R1 — Constituent-system identity

**Finding [E/D]:** already strongly covered by SoS theory, infrastructure frameworks, architecture standards and most domain models.

```math
\boxed{R_1\text{ is not a residual novelty opportunity.}}
```

Any candidate thesis representation must preserve it.

---

## R2 — Mechanism semantics

**Finding [E/D]:** Rinaldi, Johansson–Hassel, Nan–Sansavini, ontology approaches and detailed P–T models all move beyond untyped adjacency. However, they encode mechanisms differently: taxonomy, functional link, subsystem interaction, ontology relation, or domain equation.

**Residual issue [H]:** semantic interoperability among those mechanism forms may remain unresolved.

---

## R3 — Directionality / reciprocity

**Finding [E/D]:** direction and reciprocal propagation are already representable in dependency/network/domain models.

```math
\boxed{\text{Directed }P\rightarrow T\text{ versus }T\rightarrow P\text{ is necessary but not novel.}}
```

---

## R4 — Information/control

**Finding [E]:** explicitly strong in Rinaldi, Nan–Sansavini and NIST CPS; also represented operationally in detailed coupled-system models.

**Residual issue [H]:** a common relation contract spanning information/control and physical dependencies without collapsing their semantics may still be useful.

---

## R5 — Organization/human/authority

**Finding [E]:** organization/human factors are already explicit in SoS managerial independence, Nan–Sansavini's human-organizational layer, NIST human/business aspects, and architecture viewpoints.

```math
\boxed{\text{Adding an organizational layer is not sufficient novelty.}}
```

**Residual issue [H]:** explicit organizational dependencies at the same relation-contract level as physical/informational dependencies remain to be checked against broader literature.

---

## R6 — State dependence

**Finding [E/D]:** multilayer dynamic processes, hybrid infrastructure models, temporal networks and dynamic P–T models all support changing system state; not all make *dependency influence itself* an explicit state-dependent object.

**Residual issue [H]:** distinguish

```math
\text{system state }X(t),\qquad
\text{dependency state }z_e(t),\qquad
\text{dependency influence }w_e(t).
```

This separation must be tested, not assumed novel.

---

## R7 — Time / delay / sequence

**Finding [E]:** strongly represented by temporal networks, hybrid models, NIST timing concerns and dynamic P–T models.

Therefore:

```math
\boxed{\text{time-varying coupling alone is not novelty.}}
```

The remaining question is semantic integration of different time objects:

```math
\text{event time}\neq\text{causal delay}\neq\text{response latency}\neq\text{characteristic timescale}.
```

---

## R8 — Feedback / mediated interdependency

**Finding [E]:** return propagation and cross-system feedback already appear in infrastructure-interdependency models and detailed P–T coupling.

The thesis may still contribute a **formal composition rule** distinguishing direct reciprocal dependency from mediated system-level interdependency, but this must survive 0C saturation and 0F ablation.

---

## R9 — Uncertainty / evidence status

**Finding [E/D]:** uncertainty itself is widely modeled probabilistically, through trustworthiness/assurance, or through scenario/stochastic models.

**Current strongest candidate residual issue:** the benchmark has not yet identified a widely adopted infrastructure dependency representation in which every relation carries a first-class **epistemic/evidence status** distinct from physical uncertainty.

This is **not yet a novelty claim**.

Required distinction:

```math
\boxed{
\underbrace{\text{aleatory/parametric uncertainty}}_{\text{uncertainty in the system/model}}
\neq
\underbrace{\text{epistemic relation status}}_{\text{uncertainty that the dependency itself is known/correct}}
}
```

---

## R10 — Service/capability consequence

**Finding [E]:** many predecessors evaluate function, vulnerability, resilience, traffic performance, power losses, or SoS purpose.

What remains important for Phase 0 is enforcing a traceable relation-to-service chain:

```math
\mathfrak d_e\rightarrow\Delta X\rightarrow\Delta Q.
```

The chain is an acceptance criterion, not presumed novelty.

---

## R11 — Preservation of domain physics

**Finding [E]:** Nan–Sansavini explicitly permit subsystem-specific models; NIST integrates physics and logic; ISO supports multiple model kinds; Song et al. retain traffic and power equations separately.

Therefore:

```math
\boxed{F_P\neq F_T\text{ is a design requirement, not a new discovery.}}
```

---

## R12 — Extensibility

**Finding [E/D]:** SoS, multilayer networks, ontologies, NIST CPS and ISO architecture descriptions are explicitly general/reusable. Detailed P–T models are naturally less general because their purpose is domain fidelity.

**Residual issue [H]:** whether a *single minimal dependency contract* can connect reusable architecture to high-fidelity domain models without redesign when a new infrastructure domain is introduced.

---

# 5. Coverage envelope

Define the evidence-supported coverage set of representation family `M_j` as

```math
\Gamma_j=\{R_k:B_{jk}=2\}.
```

The benchmark shows that no inspected model should be dismissed as globally inadequate. Instead:

```math
\boxed{
\bigcup_j\Gamma_j\approx\mathcal R
}
```

at the **family level**: collectively, the literature already covers nearly all requirements.

The unresolved issue is therefore not simply missing capability, but **integration without semantic loss or unnecessary complexity**.

This substantially narrows the Phase-0 thesis claim.

---

# 6. Strongest predecessor challenge

Among the inspected sources, `M05` (Nan–Sansavini) is the strongest direct challenge to Phase 0 because it already provides:

```math
\text{physical/process}
+
\text{operational control}
+
\text{human-organizational}
+
\text{hybrid dynamics}
+
\text{subsystem-specific models}
+
\text{performance/resilience evaluation}.
```

Therefore any Phase-0 proposal must demonstrate added value **against this predecessor**, not only against a simple binary multilayer graph.

A defensible future baseline set should therefore include at minimum:

```math
\boxed{
\begin{aligned}
B_0&=\text{simple directed multilayer graph},\\
B_1&=\text{functional infrastructure interdependency model},\\
B_2&=\text{Nan--Sansavini-type multilayer hybrid model},\\
B_3&=\text{ontology/architecture representation},\\
B_4&=\text{high-fidelity dynamic P--T domain model}.
\end{aligned}}
```

---

# 7. Current candidate residual problem

The benchmark supports the following **candidate** problem statement:

```math
\boxed{
\begin{minipage}{0.86\textwidth}
Existing approaches already represent constituent systems, multiple relation types, physical/control/human dimensions, temporal behavior, uncertainty, and detailed Power--Transportation physics. The remaining theoretical question is whether these heterogeneous representations can be connected through a minimum typed dependency contract that preserves mechanism and domain physics while making relation state, evidence status, and service consequence explicit and composable.
\end{minipage}}
```

Status:

```math
[P/H]\quad\text{candidate residual problem; not yet established as a literature gap.}
```

---

# 8. Falsification of the candidate residual problem

The candidate residual problem is **closed** if 0C saturation identifies an existing representation that simultaneously and explicitly provides:

```math
\boxed{
R_1\land R_2\land\cdots\land R_{12}
}
```

or provides an equivalent interoperable relation object with no material loss for V1–V5.

If such a predecessor exists:

```math
\boxed{\text{do not invent a new dependency grammar.}}
```

Instead, adopt/extend that framework and move the thesis contribution downstream to hypothesis testing, viability, or intervention.

---

# 9. 0C status

```math
\boxed{
\text{CORE BENCHMARK PASS COMPLETE}
\quad\land\quad
\text{SATURATION NOT YET ESTABLISHED}
}
```

The next substep inside 0C is a **saturation/contrary-framework search**, not 0D yet.

Required search targets:

1. `shared-state` system-of-systems models;
2. infrastructure `reference architecture` and interoperability frameworks;
3. typed dependency / dependency grammar formalisms;
4. knowledge-graph/semantic representations with temporal and uncertainty annotations;
5. federated co-simulation standards/frameworks for heterogeneous infrastructures;
6. models explicitly integrating physical + cyber/information + organization + service + uncertainty;
7. recent 2025–2026 reviews for predecessor frameworks omitted by the core anchors.

Only when new searches cease changing the taxonomy or identify no dominating predecessor can 0C be closed.
