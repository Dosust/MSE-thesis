# Public Novelty Addendum — Dependency Semantics and Evidence Provenance v1.0

**Date:** 2026-09-16  
**Status:** MATERIAL PRIOR-ART ADDENDUM / PUBLIC-WEB EVIDENCE  
**Effect:** materially narrows residual `N1'`; does not close the authenticated global-search gate

## 1. Reason for addendum

A targeted second-stage search asked whether the thesis can claim novelty for a **directed, evidence-grounded, typed and provenance-preserving infrastructure dependency representation**.

The answer is **no in that broad form**. Prior work already contains substantial portions of that idea.

## 2. Closest prior art identified

### 2.1 CIMS formal infrastructure interdependencies

Dudenhoeffer, Permann & Manic (2006), *CIMS: A Framework for Infrastructure Interdependency Modeling and Analysis*, Idaho National Laboratory.

CIMS formally represents directed cross-infrastructure dependencies with source/target entities and distinguishes physical, informational, geospatial, policy/procedural and societal interdependencies. It explicitly permits directional dependency and reciprocal/interdependent relationships.

**Consequence:** directed source–receiver dependency edges and typed infrastructure interdependency classes are prior art.

### 2.2 Dependency/interdependency distinction and mediated reciprocity

Subsequent critical-infrastructure literature explicitly distinguishes unidirectional dependency from bidirectional interdependency and recognizes direct and indirect/mediated dependencies.

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

**Consequence:** defining interface contracts and validating SoS interfaces are also prior art outside the critical-infrastructure dependency literature.

### 2.6 Composable multi-infrastructure model integration

Tasseff et al. (2023), *InfrastructureModels: Composable Multi-infrastructure Optimization in Julia*, INFORMS Journal on Computing, DOI `10.1287/ijoc.2022.0118`, provides a composable framework for integrating multiple infrastructure optimization models.

**Consequence:** composability across infrastructure models is prior art and cannot be used alone as the thesis novelty claim.

## 3. Broad claims now removed from N1 novelty space

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
composable multi-infrastructure models.
```

## 4. Further narrowed residual `N1''`

The canonical thesis object remains

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e),
```

but the object itself is not claimed as an unprecedented concept.

The narrower research question becomes:

```math
\boxed{
N_1'':
\text{Can evidence-qualified infrastructure dependency assertions be mapped into explicit executable}
\\
\text{causal operators/guards/internal states that preserve constituent physics and materially improve}
\\
\text{prediction or decisions under matched ablation in a dynamic }P\!\!-\!T\!\!-\!I\!\!-\!O\text{ system?}
}
```

The potentially differentiating combination is therefore not provenance + typing + direction. It is the validated bridge

```math
\boxed{
\text{evidence-supported dependency claim}
\rightarrow
(\Phi_e,\gamma_e,\theta_e,\zeta_e)
\rightarrow
\Xi_e
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
\Delta Q
\rightarrow
\text{matched empirical/decision test}.
}
```

Even this remains `UNRESOLVED_GLOBAL` until authenticated search and full-text comparison close the gate.

## 5. Consequence for H1

H1 is strengthened as an empirical/representation question rather than a novelty claim:

```math
M_0=\text{independent},
\qquad
M_1=\text{static/algebraic coupling},
\qquad
M_2=\text{executable dynamic causal mechanisms}.
```

The thesis earns a contribution only if `M2` adds prespecified explanatory, predictive or decision value relative to the simpler representations within the validation domain.

## 6. Formal-search consequence

The frozen F0 authenticated search must now specifically screen for prior methods connecting evidence/semantic dependency objects to executable dynamic coupling operators, guards, delay/memory states and empirical validation.

The global novelty gate remains:

```math
\boxed{G_A=\texttt{BLOCKED\_EXTERNAL\_ACCESS}.}
```
