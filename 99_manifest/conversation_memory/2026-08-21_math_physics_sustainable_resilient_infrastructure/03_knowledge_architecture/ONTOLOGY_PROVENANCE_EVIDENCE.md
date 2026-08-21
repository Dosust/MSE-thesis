# Mathematical Knowledge Architecture: Taxonomy, Ontology, Provenance, and Formal Evidence

## 1. Core correction

The project must distinguish **taxonomy**, **ontology**, **formal mathematical dependency**, **literature evidence**, and **project hypotheses**.

An untyped arrow

\[
A\rightarrow B
\]

is scientifically ambiguous. It could mean `broader-than`, `is-a`, `part-of`, `uses`, `defines`, `computes`, `requires`, `causes`, `supports`, or `mathematically-implies`.

The upgraded representation is:

\[
\boxed{A\xrightarrow[\text{provenance/evidence/version}]{\text{typed relation}}B.}
\]

## 2. Two taxonomies with different roles

### 2.1 Duke 2002 — educational browse taxonomy

User-supplied source:
`https://sites.math.duke.edu/education/mathnsdl02/math-taxonomy-0202-1web.htm`

This is the February 2002 "Core Subject Taxonomy for Mathematical Sciences Education" final draft, designed to support cross-library educational browsing/catalog mapping.

Its top-level categories are:
1. Elementary Mathematics
2. Logic and Foundations
3. Algebra and Number Theory
4. Discrete Mathematics
5. Geometry
6. Calculus
7. Analysis
8. Differential and Difference Equations
9. Statistics and Probability
10. Applied Mathematics
11. Mathematics History

**Project role:** optional human-facing educational navigation. It is **not** the canonical modern research classification and its tree edges are not theorem/prerequisite relations.

### 2.2 MSC2020 — canonical research-literature classification

Official sources:
- `https://msc2020.org/`
- `https://mathscinet.ams.org/mathscinet/msc/msc2020.html`
- `https://zbmath.org/classification/`

MSC2020 is jointly maintained by Mathematical Reviews and zbMATH and is the current classification used for mathematical research literature.

**Project role:** canonical scholarly subject coding for literature, PRISMA, mathematical coverage, and reproducible research indexing.

**Binding rule:** do not convert MSC2020 hierarchy into a causal, prerequisite or theorem-dependency graph.

## 3. Recommended standards/knowledge stack

- **Duke 2002 educational taxonomy** — optional browse/teaching navigation only;
- **MSC2020 / MSC2020-SKOS** — canonical disciplinary research taxonomy;
- **ISO 25964 / SKOS** — controlled-vocabulary/thesaurus semantics where needed;
- **RDF / OWL 2** — formal ontology relations;
- **ISO 80000-2** — mathematical signs and symbols where relevant;
- **OpenMath** — mathematical-object semantics;
- **MathML** — mathematical web/presentation representation;
- **OMDoc/MMT** — theory/formal dependency structure;
- **MaRDI MathModDB** — applied mathematical models, formulations, quantities, research problems and computational tasks;
- **PROV-O** — provenance;
- **Lean / Isabelle / Rocq / Mizar** — theorem/formal-proof layer.

## 4. Node classes

Examples of distinct entity types:
- `EducationalSubject`;
- `MSCSubject`;
- `Theory`;
- `MathematicalObject`;
- `Definition`;
- `Assumption`;
- `MathematicalFormulation`;
- `Method`;
- `Algorithm`;
- `ComputationalTask`;
- `MathematicalModel`;
- `ResearchProblem`;
- `ApplicationDomain`;
- `Dataset/EvidenceSource`;
- `Theorem/ProofObject`;
- `InfrastructureState`;
- `InterfaceState`;
- `AdmissibleSet`;
- `ReachableSet`;
- `ViabilityKernel`;
- `ServiceMetric`;
- `DecisionVariable`.

Example:

\[
\text{Hamilton–Jacobi PDE}
\xrightarrow{\texttt{usedBy}}
\text{Reachability Analysis}
\xrightarrow{\texttt{computes/approximates}}
\text{Reachable Set}.
\]

The second edge must be qualified by solver assumptions, discretization, convergence/error status and state dimension.

## 5. Relation classes

Use typed relations, for example:
- `skos:broader` / `skos:narrower` — taxonomy only;
- `isDefinitionOf`;
- `requiresAssumption`;
- `usedBy`;
- `computes`;
- `approximates`;
- `bounds`;
- `isSpecialCaseOf`;
- `isEquivalentUnderConditionsTo`;
- `causes` — only with defensible physical/causal semantics;
- `supportsClaim`;
- `falsifiesClaim`;
- `implementedBy`;
- `validatedBy`;
- `appliedToDomain`;
- `mapsPhysicalStateToService`.

## 6. Evidence/status classes

The conversation proposed the hierarchy:

- **S0** — official taxonomy / international standard / authoritative controlled source;
- **S1** — formal ontology relation;
- **S2** — formal mathematical/theorem dependency or proved result;
- **S3** — peer-reviewed literature-supported relation;
- **S4** — project hypothesis / proposed research relation.

A thesis originality claim may begin as S4 and later be promoted only when proof or evidence justifies it.

## 7. Provenance-bearing edge object

A useful representation is:

\[
\boxed{e_{ij}=(v_i,r,v_j,P,A,C,\nu,T)}
\]

where:
- \(v_i\) = source entity;
- \(r\) = typed relation;
- \(v_j\) = target entity;
- \(P\) = provenance/source;
- \(A\) = authority/evidence class;
- \(C\) = confidence or verification status;
- \(\nu\) = source/version;
- \(T\) = conditions/assumptions/tolerance under which the edge is valid.

## 8. Three interacting problem graphs

The research program can be represented as three linked graphs:

1. **Mathematical knowledge graph** \(\mathcal G_M\): theories, objects, methods, algorithms, formal dependencies, taxonomy mappings and provenance.
2. **Physical infrastructure graph** \(\mathcal G_I\): executable P–T–W infrastructure state plus extensible additional sectors such as Solid Waste; directional dynamic interfaces \(Z_{ij}\).
3. **Human/service graph** \(\mathcal G_H\): population/service dependencies, critical facilities, service groups, deprivation, vulnerable populations and societal consequences.

The mathematical graph supplies the formal apparatus used to model \(\mathcal G_I\) and its mapping to \(\mathcal G_H\).

## 9. Thesis-specific mathematical spine

The high-value mathematical spine is:

\[
\boxed{
\text{Governing Dynamics}
\rightarrow
\text{Dynamic Interfaces}
\rightarrow
\text{Observation / Inverse Inference}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Service / Admissibility}
\rightarrow
\text{Recovery Reachability}
\rightarrow
\text{Viability}
\rightarrow
\text{Minimum Intervention / Control}
}
\]

Associated mathematics includes:
- nonlinear ODE/PDE and hybrid systems;
- network/interdependency mathematics;
- inverse problems and identifiability;
- probability, Bayesian inference and UQ;
- functional analysis/operator theory where needed for well-posedness;
- reachability, viability theory and Hamilton–Jacobi methods;
- control theory;
- optimization/Operations Research;
- numerical analysis and scientific computing;
- formal verification/certification where tractable.

## 10. Sustainability / SDG logic

SDGs should not be decorative graph nodes. The defensible chain is:

\[
\boxed{
\text{mathematical intervention}
\rightarrow
\text{physical outcome}
\rightarrow
\text{service outcome}
\rightarrow
\text{sustainability/equity outcome}
\rightarrow
\text{SDG relevance}
}
\]

Example:

\[
\text{safe recovery reachability}
\rightarrow
\text{avoid critical-service deprivation}
\rightarrow
\text{population service continuity}
\rightarrow
\text{potential SDG 9/11/13 contribution}.
\]

The SDG relation remains an evaluation/impact relation unless a quantitative causal evaluation has been established.

## 11. Consequence for OR / Monte Carlo

Future rankings should weight not only concept value but also evidence strength/provenance:

\[
S_i=\sum_k w_k q_{ik}s_{ik},
\]

with \(q_{ik}\) reflecting authority, evidence class, recency, replication/formalization and provenance quality.

Project hypotheses should receive broader uncertainty than established standards/theorems unless the data justify otherwise.

## 12. Binding anti-error rules

1. Duke 2002 and MSC2020 are not interchangeable.
2. Taxonomy edges do not imply mathematical dependency.
3. Literature co-occurrence does not imply theorem-level dependence or physical causality.
4. `P–T–W` is the executable MSE core; `Solid Waste` is an extension unless later explicitly promoted by the user.
5. Recovery reachability, acceptable recovery, hard safety and post-recovery viability are distinct mathematical objects.
6. AI outputs are never upgraded automatically to physical states or certified decisions.
