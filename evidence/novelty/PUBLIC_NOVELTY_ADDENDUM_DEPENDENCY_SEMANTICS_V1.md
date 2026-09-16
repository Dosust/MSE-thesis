# Public Novelty Addendum — Dependency Semantics and Evidence Provenance v1.1

**Date:** 2026-09-16  
**Status:** MATERIAL PRIOR-ART ADDENDUM / PUBLIC-WEB EVIDENCE  
**Effect:** materially narrows residual `N1`; does not close the authenticated global-search gate

## 1. Reason for addendum

A targeted second-stage search asked whether the thesis can claim novelty for a **directed, evidence-grounded, typed and provenance-preserving infrastructure dependency representation**, and then whether semantic dependency models linked to executable/federated simulation are already prior art.

The answer is **yes, substantial prior art exists for both layers of that broad claim**.

## 2. Closest prior art identified

### 2.1 CIMS formal infrastructure interdependencies

Dudenhoeffer, Permann & Manic (2006), *CIMS: A Framework for Infrastructure Interdependency Modeling and Analysis*, Idaho National Laboratory.

CIMS formally represents directed cross-infrastructure dependencies with source/target entities and distinguishes physical, informational, geospatial, policy/procedural and societal interdependencies. It explicitly permits directional dependency and reciprocal/interdependent relationships.

**Consequence:** directed source–receiver dependency edges and typed infrastructure interdependency classes are prior art.

### 2.2 Dependency/interdependency distinction and mediated reciprocity

Critical-infrastructure literature explicitly distinguishes unidirectional dependency from bidirectional interdependency and recognizes direct and indirect/mediated dependencies.

**Consequence:** the thesis cannot claim novelty merely for distinguishing dependency from interdependency or for allowing mediated `A -> ... -> B -> ... -> A` reciprocal influence.

### 2.3 Ontology-based interdependency representation

McNally et al. (2007), *Learning the Critical Infrastructure Interdependencies through an Ontology-Based Information System*, Environment and Planning B 34(6), DOI `10.1068/b32078`, and later semantic-web infrastructure work represent cross-domain infrastructure knowledge through ontologies and machine-readable relationships.

Dao et al. (2021), *Semantic framework for interdependent infrastructure resilience decision support*, Automation in Construction 130, 103852, develops cross-domain ontologies, heterogeneous data integration and rule-based logical reasoning for interdependency identification.

**Consequence:** ontology-grounded cross-domain semantics, interoperability and machine reasoning for infrastructure dependencies are prior art.

### 2.4 Evidence-first auditable dependency graphs

Nurjahan et al. (2026), *An Evidence-First Multi-LLM Framework for Auditable Critical-Infrastructure Dependency Modeling*, arXiv:2609.12360, provides a particularly close precedent.

Its framework separates:

```text
raw evidence;
entity/dependency extraction;
ontology grounding;
evidence verification;
entity resolution;
dependency endpoint alignment;
validation/fusion;
human review;
final infrastructure dependency graph.
```

It explicitly preserves provenance and unresolved cases. Its Infrastructure Knowledge Base represents dependencies with project identity, source entity, target entity, relationship and dependency type, while provenance links assertions to evidence.

**Consequence:** evidence-grounded directional dependencies, explicit endpoint resolution, ontology grounding, validation state and provenance cannot be claimed as new in isolation.

### 2.5 Contract-based interface validation in systems of systems

Waschle et al. (2021), *Contract-based methods and activities in the validation of interfaces for System of Systems*, IEEE SoSE, DOI `10.1109/SOSE52739.2021.9497476`, applies contract-based methods to define and validate interfaces between vehicle and infrastructure systems.

**Consequence:** defining interface contracts and validating SoS interfaces are prior art outside the critical-infrastructure dependency literature.

### 2.6 Composable multi-infrastructure model integration

Tasseff et al. (2023), *InfrastructureModels: Composable Multi-infrastructure Optimization in Julia*, INFORMS Journal on Computing, DOI `10.1287/ijoc.2022.0118`, provides a composable framework for integrating multiple infrastructure optimization models.

**Consequence:** composability across infrastructure models is prior art and cannot be used alone as the thesis novelty claim.

### 2.7 Ontology-to-federated-simulation integration

Older European critical-infrastructure simulation work is even closer to the semantics-to-execution bridge:

- Tofani et al. (2010), *Using Ontologies for the Federated Simulation of Critical Infrastructures*, Procedia Computer Science 1(1):2301–2309, DOI `10.1016/j.procs.2010.04.258`, uses an ontology-based knowledge base to represent domain properties, relations and cross-domain dependencies inside a federated critical-infrastructure simulation framework.
- DIESIS/IRRIIS ontology-based simulation work uses semantic infrastructure/dependency models to integrate heterogeneous critical-infrastructure simulators, dynamically bind models, exchange state information and test interdependency assumptions.
- Related ontology-based critical-infrastructure modeling and simulation work explicitly describes ontology/rule systems as a semantic foundation for federated simulation and for identifying latent dependencies.

**Consequence:** the broad bridge

```math
\text{semantic dependency representation}
\rightarrow
\text{federated/executable simulation}
```

is also prior art.

### 2.8 Semantic CPS modeling and executable numerical behavior

NIST work on semantic frameworks for CPS modeling and simulation integrates component semantics, requirements traceability, rules and analysis of discrete/continuous behavior.

**Consequence:** semantic descriptions connected to executable physical/cyber simulation are not unique to infrastructure-interdependency research.

## 3. Broad claims removed from N1 novelty space

The thesis shall not claim originality merely for:

```text
directed dependency edges;
dependency vs interdependency distinction;
mediated interdependency loops;
typed dependency classes;
ontology-grounded infrastructure relationships;
evidence-linked dependency assertions;
provenance-preserving dependency graphs;
interface contracts in systems of systems;
composable multi-infrastructure models;
semantic infrastructure dependency models linked to federated simulation;
dynamic binding/interoperability of heterogeneous infrastructure simulators.
```

## 4. Residual `N1*` after deeper falsification

The canonical thesis object remains

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e),
```

but neither that object nor a semantics-to-simulation bridge should be presented as globally unprecedented.

The remaining scientifically defensible question is now primarily **empirical and methodological**:

```math
\boxed{
N_1^{*}:
\text{Does the canonical evidence-to-mechanism contract produce a sufficiently explicit, reproducible and}
\\
\text{validated mapping from real P--T dependency evidence to executable dynamic coupling such that it}
\\
\text{adds measurable predictive/decision value over independent and static-coupling representations?}
}
```

The working chain is

```math
\boxed{
\text{qualified evidence}
\rightarrow
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)
\rightarrow
\Xi_e
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
\Delta Q
\rightarrow
\{M_0,M_1,M_2\}\text{ matched test}.
}
```

The possible thesis contribution is therefore **not the existence of this family of modeling ideas**. It is conditional on demonstrating a rigorous, traceable and useful implementation for the selected P–T–I–O problem under the thesis validation gates.

## 5. Consequence for H1

H1 remains scientifically valuable even if `N1*` is not globally novel, because H1 is a falsifiable engineering test:

```math
M_0=\text{independent},
\qquad
M_1=\text{static/algebraic coupling},
\qquad
M_2=\text{dynamic causal coupling under the canonical dependency contract}.
```

The thesis earns a substantive contribution only if `M2` adds prespecified explanatory, predictive or decision value relative to simpler representations within a declared validation domain.

## 6. Formal-search consequence

The authenticated F0 search must screen explicitly for prior methods that jointly contain:

```text
evidence/provenance;
typed dependency semantics;
model-to-simulator mapping;
dynamic operators/guards/delays/internal relation states;
preservation of constituent physics;
matched model ablation;
empirical validation against observed cross-system behavior.
```

This is an extraction/screening refinement, not permission to alter search results after inspection.

The global novelty gate remains:

```math
\boxed{G_A=\texttt{BLOCKED\_EXTERNAL\_ACCESS}.}
```
