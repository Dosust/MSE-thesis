# Mathematical Knowledge Architecture: Ontology, Provenance, and Evidence Levels

## Why this changed the project

The six scientific chains remain valid, but the project no longer treats every node or arrow as semantically equivalent.

An untyped arrow

\[
A\rightarrow B
\]

is ambiguous: it could mean `is-a`, `part-of`, `uses`, `defines`, `computes`, `is-required-by`, `empirically-supports`, `causes`, or `mathematically-implies`.

The upgraded representation is therefore:

\[
\boxed{A\xrightarrow[\text{provenance/evidence}]{\text{typed relation}}B.}
\]

## Recommended standards/knowledge stack

- **MSC2020 / SKOS** — disciplinary taxonomy / controlled concept scheme;
- **OWL 2** — formal ontology relations;
- **OpenMath** — mathematical-object semantics;
- **MathML** — web/presentation representation;
- **OMDoc/MMT** — theory/formal dependency structure;
- **MaRDI MathModDB** — applied mathematical models, formulations, quantities, research problems, computational tasks;
- **PROV-O** — provenance;
- **Lean / Isabelle / Rocq / Mizar** — theorem/formal-proof layer.

## Node classes

Examples of distinct entity types:
- `MSCSubject`;
- `Theory`;
- `MathematicalObject`;
- `MathematicalFormulation`;
- `Method`;
- `Algorithm`;
- `ComputationalTask`;
- `MathematicalModel`;
- `ResearchProblem`;
- `ApplicationDomain`;
- `Dataset/EvidenceSource`;
- `Theorem/ProofObject`.

Example:

\[
\text{Hamilton–Jacobi PDE}
\xrightarrow{\texttt{usedBy}}
\text{Reachability Analysis}
\xrightarrow{\texttt{computes}}
\text{Reachable Set}.
\]

## Evidence classes

The conversation proposed the hierarchy:

- **S0** — official taxonomy / international standard;
- **S1** — formal ontology relation;
- **S2** — formal mathematical/theorem dependency;
- **S3** — peer-reviewed literature-supported relation;
- **S4** — project hypothesis / proposed research relation.

This makes thesis originality explicit: a candidate research contribution may begin as an S4 relation and, after proof/validation, be promoted to S2 or S3 as appropriate.

## Provenance-bearing edge object

A useful representation is:

\[
\boxed{e_{ij}=(v_i,r,v_j,P,A,C,\nu)}
\]

where:
- \(v_i\) = source entity;
- \(r\) = relation type;
- \(v_j\) = target entity;
- \(P\) = provenance;
- \(A\) = authority/evidence status;
- \(C\) = confidence;
- \(\nu\) = source/version.

## Three interacting graphs

The program can be represented as three linked graphs:

1. **Mathematical knowledge graph** \(\mathcal G_M\): theories, objects, methods, algorithms, relations, provenance.
2. **Physical infrastructure graph** \(\mathcal G_I\): P–W–T–SW assets and interfaces.
3. **Human/service graph** \(\mathcal G_H\): population/service dependencies, critical facilities, vulnerable groups and service consequences.

The mathematical graph supplies the formal apparatus used to model \(\mathcal G_I\) and its mapping to \(\mathcal G_H\).

## SDG/sustainability logic

SDGs should not be decorative graph nodes. The intended chain is:

\[
\boxed{
\text{mathematical intervention}
\rightarrow
\text{physical outcome}
\rightarrow
\text{service outcome}
\rightarrow
\text{sustainability outcome}
}
\]

Example:

\[
\text{HJ viability}
\rightarrow
\text{avoid critical-service failure}
\rightarrow
\text{population service continuity}
\rightarrow
\text{SDG 9/11/13 contribution}.
\]

## Consequence for OR / Monte Carlo

Future rankings should weight not only concept value but also evidence strength/provenance:

\[
S_i=\sum_kw_kq_{ik}s_{ik},
\]

with \(q_{ik}\) reflecting authority, evidence class, recency, replication/formalization and provenance quality.

Uncertainty widths can also depend on evidence level, with project hypotheses receiving broader uncertainty than standards/formal theorems.
