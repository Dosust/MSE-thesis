# E-ROSETTA-UPR-001 — OMG UPR / ROSETTA v1.0 (2019)

**Status:** ADMITTED METHODOLOGICAL / SYSTEMS-ENGINEERING EVIDENCE  
**Date admitted:** 2026-10-06  
**Primary use:** relational structure, mathematical constraints, sensitivity relations, feasible design-space reasoning, and cross-domain design integration  
**Authority:** Object Management Group (OMG) formal specification  
**Thesis adoption status:** SUPPORTING METHOD ONLY — not a replacement for the thesis physics-based state-time dynamics

## 1. Source identity

Object Management Group (OMG).  
*UML Profile for Relational Oriented Systems Engineering Technology Trade-off and Analysis (ROSETTA), Version 1.0.*  
OMG Document Number: **formal/19-11-09**.  
Release date: **November 2019**.

Official specification page:

https://www.omg.org/spec/UPR/1.0

Official PDF:

https://www.omg.org/spec/UPR/1.0/PDF

### Uploaded source provenance

User-supplied filename: `formal-19-11-09.pdf`

SHA-256:

```text
915d3dd32a731c88ea3807a4ae03ce93327a37fa082a30dba728ac8bd8414f70
```

The full PDF is **not republished in this repository**. The repository stores the official source location, provenance hash, and thesis-specific analytical extraction.

## 2. What the specification establishes

The specification extends UML to support information structuring for model-based analysis, architecture optimization, system design, and constraint-driven design.

Its mathematical foundation is the ROSETTA relational-oriented framework. The specification explicitly supports:

- system elements and variables;
- mathematical constraints;
- design objectives;
- design variables;
- design ranges;
- feasible ranges and feasible design spaces;
- mathematical relations and sensitivities;
- relational structures;
- relational transformations;
- matrix representations of relations;
- cross-domain design integration.

## 3. Key mathematical concepts useful to the thesis

### 3.1 Relational structure

ROSETTA treats models through entities and mathematical relations. A relational structure can be represented graphically or by matrices.

Potential thesis translation:

```math
\mathcal G=(\mathcal V,\mathcal E),
\qquad
A=[a_{ij}]
```

where components/interfaces are represented by elements and qualified relations.

**Use:** architecture and dependency semantics.

**Boundary:** topology or relation alone does not prove physical causality.

### 3.2 Mathematical constraints

UPR distinguishes constrained design objectives and constrained design variables.

Potential thesis translation:

```math
g_i(X_i,t)\le 0
```

for physically admissible operating limits, and

```math
Q_k(t)\ge Q_k^{\min}
```

for minimum acceptable service requirements.

**Use:** formalize thermal, operational, and service constraints.

### 3.3 Design range and feasible range

UPR distinguishes a general design range from the subset that satisfies design-objective constraints.

Potential thesis translation:

```math
\mathcal D
\supseteq
\mathcal F
```

where `\mathcal D` is the available engineering design space and `\mathcal F` is the feasible subset.

This is directly useful for **IMPROVE**, where engineering design choices can be screened against heat-resilience requirements.

### 3.4 Sensitivity

UPR defines sensitivity as a mathematical relation describing how variation in one variable affects another and supports derivative/polynomial representations.

Potential thesis translations:

```math
S_{ij}=\frac{\partial X_i}{\partial X_j}
```

and

```math
S_{ki}^{Q}=\frac{\partial Q_k}{\partial X_i}.
```

**Use:** quantify state-to-state and state-to-service influence.

### 3.5 Relational transformation

ROSETTA uses transformations between relational structures to infer or preserve relations across models.

Potential thesis use:

```text
component-state relations
→ interface relations
→ service relations
```

This may support traceable propagation from lower-level physical states to higher-level service objectives.

### 3.6 Feasible-design inverse mapping

UPR describes inverse mapping from objective constraints into feasible ranges of design variables.

Potential thesis use:

```text
service requirement
→ permissible state/parameter region
→ engineering design choices
```

This can support the **IMPROVE** stage by asking which design choices keep the system inside a service-feasible region.

## 4. What ROSETTA does NOT establish for this thesis

UPR / ROSETTA does not by itself provide:

- extreme-heat governing physics;
- thermal differential equations for power or transport assets;
- dynamic state evolution;
- state-transition timing;
- propagation delays;
- hybrid state dynamics;
- service-resilience trajectories;
- viability/reachability analysis;
- adaptation control laws;
- restoration dynamics;
- empirical validation for the thesis system.

Therefore:

```text
ROSETTA relational mathematics
≠
physics-based state-time resilience model
```

The thesis must supply those dynamic physical and control layers independently.

## 5. Correct thesis role

Use ROSETTA as a **structuring and mathematical-engineering support layer**:

```text
SYSTEM ARCHITECTURE
→ relational structure
→ constraints
→ sensitivities
→ design/objective mappings
```

Then couple that structure to:

```text
PHYSICAL DYNAMICS
→ state-time evolution
→ service consequences
→ resilience interventions
```

## 6. Strong compatibility with the thesis

Candidate integration:

```math
\underbrace{(\mathcal V,\mathcal R)}_{\text{ROSETTA relational structure}}
\rightarrow
\underbrace{\dot X=F(X,H,u;\theta)}_{\text{physics-based dynamics}}
\rightarrow
\underbrace{g(X,t)\le0}_{\text{constraints}}
\rightarrow
\underbrace{Q=G(X)}_{\text{service}}
\rightarrow
\underbrace{\mathcal V_{\mathrm{safe}}(t)}_{\text{feasible / viable region}}
\rightarrow
\text{Improve / Adapt / Restore}.
```

## 7. Evidence-strength statement

This source strongly supports:

- relational architecture formalization;
- mathematical constraints;
- design-variable / design-objective separation;
- sensitivity-based relations;
- feasible design spaces;
- transformation between related model domains.

It does **not** establish the final thesis equations or prove that ROSETTA is the optimal unifying mathematical method for extreme-heat resilience.

## 8. Future-use triggers

Revisit this source when the thesis needs to:

1. formalize the component/interface relation matrix;
2. distinguish design variables from performance/service objectives;
3. build a mathematical constraint ledger;
4. map asset physics to service objectives;
5. define sensitivity relations between state variables;
6. perform cross-domain tradeoff analysis;
7. derive feasible intervention ranges;
8. create a SysML/UML-compatible mathematical architecture;
9. trace requirements to physical variables and service thresholds;
10. compare design alternatives during the **IMPROVE** stage.

## 9. Repository-use rule

Any future implementation based on ROSETTA must state whether each relation is:

- **physics-derived**;
- **data-derived**;
- **expert-estimated**;
- **mathematically implied**.

No estimated relational coefficient may be silently treated as physical law.
