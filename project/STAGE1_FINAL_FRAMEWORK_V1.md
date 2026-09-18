# Stage 1 Final Framework v1.1 — Ready for Freeze

**Stage:** 1 — Spatiotemporal Multilayer System-of-Systems Structure  
**Status:** **PASS — READY FOR FREEZE AFTER NEW-EVIDENCE INTEGRATION**  
**Date:** 2026-09-18  
**Canonical RQ:** **RQ1: What entities exist, what layers constitute the system, and where can interactions occur?**  
**Canonical SO:** **SO1: Define the coupled Power–Transportation system boundary, entities, layers, locations, interfaces, states and service requirements, with Information and Organization as supporting domains.**  
**Evidence/ontology authority:** `STAGE1_EVIDENCE_AND_ONTOLOGY_REGISTER_V1.md`

## 1. Stage-1 scientific responsibility

Stage 1 constructs and verifies the bounded, typed, spatially embedded, provenance-controlled architecture of the coupled Power–Transportation System of Systems before causal claims are admitted.

```math
\boxed{
\text{Stage 1 = structural possibility}
\qquad
\text{Stage 2 = causal qualification}.
}
```

Stage 1 answers:

```math
\boxed{
\text{what exists}
+
\text{where it exists}
+
\text{how it is typed/organized}
+
\text{where interaction is structurally admissible}.
}
```

It does not answer whether a candidate relation is causally active, how strongly it acts, or how its effects propagate dynamically.

## 2. Mathematical provenance classes

Every Stage-1 object is labelled by provenance:

```text
[LIT]    established theory/mathematics
[ADAPT]  established theory adapted to P–T
[THESIS] thesis-defined methodological object
[ASSUMP] explicit modeling assumption
[CASE]   case-specific realization
```

```math
\boxed{
\text{literature foundation}
+
\text{engineering semantics}
+
\text{explicit assumptions}
+
\text{thesis methodology}
\rightarrow
\text{admissible Stage-1 mathematics}.
}
```

## 3. Typed System-of-Systems

```math
\boxed{
\mathcal S=\{P,T,I,O\},
\qquad
\mathcal S_{\rm phys}=\{P,T\},
\qquad
\mathcal S_{\rm sup}=\{I,O\}.
}
```

`P` and `T` are physical constituent systems. `I` and `O` are supporting information and organization domains.

## 4. Extended system boundary

```math
\boxed{
\Omega_{\rm sys}^{+}
=
(\Omega_x,\Omega_t,\Omega_{\rm infra},\Omega_{\rm service},\Omega_{\rm mode},\Omega_{\rm jur}).
}
```

where the factors encode geographic support, temporal support/vintage, retained infrastructure, service scope, operating modes, and jurisdictional/normative applicability.

## 5. Constituent graphs and spatial embedding

```math
G_P=(V_P,E_P,\lambda_P),
\qquad
G_T=(V_T,E_T,\lambda_T).
```

Electrical and transportation edges retain different engineering semantics.

```math
\boxed{
\mathcal G^{(1)}
=
(\mathcal V,\mathcal E_{\rm intra},R,\Lambda),
}
```

with:

```math
\mathcal V=V_P\cup V_T\cup V_I\cup V_O,
\qquad
\mathcal E_{\rm intra}=E_P\cup E_T\cup E_I\cup E_O.
```

Spatial geometry is denoted by:

```math
R=\{r_i\},
\qquad
r_i\in\mathbb R^2
```

when a 2-D coordinate is meaningful.

## 6. Frozen state notation

```math
Y(t)
=
\begin{bmatrix}
X_P(t)\\
X_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
```

`r_i` denotes location/geometry; `X_P,X_T,z_I,z_O` denote state blocks; `Y(t)` is the integrated system state used by later stages. Stage 1 declares state schemas, not Stage-3 trajectories.

## 7. Semantic entity representation

The Stage-1 entity is not an anonymous graph vertex. The thesis-defined semantic entity object is:

```math
\boxed{
E_i^\alpha
=
(
id_i,
type_i,
layer_i,
r_i,
f_i,
\mathcal Y_i,
o_i,
a_i,
\ell_i,
\mathcal D_i
).
}
```

It records identity/type, layer, geometry, engineering function/service roles, state schema, ownership/operator roles, authority roles, modeling resolution, and evidence/provenance.

The exact tuple is a thesis synthesis grounded in ontology/GIS, functional-dependency, multilayer-network and infrastructure-interface literature; it is not represented as a published standard formula.

## 8. Structural admissibility

A cross-layer pair enters Stage 1 only through the non-causal structural predicate:

```math
\boxed{
\Gamma_{ij}^{\rm str}
=
\Gamma(A_{ij},H_{ij},S_{ij},L_{ij},C_{ij},\Pi_{ij}).
}
```

where the inputs represent asset/crosswalk evidence, interface compatibility, spatial relation, access/connectivity geometry, geographic co-exposure, and provenance/data quality.

```math
\Gamma_{ij}^{\rm str}\in\{0,1\}.
```

```math
\boxed{
\Gamma_{ij}^{\rm str}=1
\not\Rightarrow
i\rightarrow j.
}
```

## 9. Structural candidate set

```math
\boxed{
\mathcal C_{\alpha\beta}^{(1)}
=
\left\{
(i,j)\in V_\alpha\times V_\beta:
\Gamma_{ij}^{\rm str}=1
\right\}.
}
```

This is the domain handed to Stage 2 for causal qualification.

## 10. Geographic guardrail

```math
\boxed{
\text{spatial proximity alone}
\not\Rightarrow
\text{functional/causal dependency}.
}
```

Shared local hazard exposure may justify geographic co-exposure status, but common exposure remains distinct from causal dependency.

## 11. Relation-status ontology

```math
\boxed{
\mathcal R_{\rm prior},
\qquad
\mathcal C_{\rm struct},
\qquad
\mathbb I_{\rm acc}.
}
```

```math
\boxed{
\mathcal R_{\rm prior}\not\Rightarrow\mathbb I_{\rm acc},
\qquad
\mathcal C_{\rm struct}\not\Rightarrow\mathbb I_{\rm acc}.
}
```

Stage 1 may record prior-documented and structural-candidate relations. Only Stage 2 may populate accepted causal dependencies `I_acc`.

## 12. Typed Stage-1 relation object

The structural candidate pair is represented by a richer pre-causal object:

```math
\boxed{
\mathfrak R_{ij}^{\alpha\beta,(1)}
=
(
E_i^\alpha,
E_j^\beta,
\Gamma_{ij}^{\rm str},
\gamma_{ij},
\Phi_{ij},
d_{ij},
m_{ij}^{\rm cand},
c_{ij}^{\rm cand},
b_{ij},
s_{ij},
\mathcal E_{ij},
q_{ij}^{\rm evid},
\ell_{ij},
\chi_{ij}^{\rm norm}
).
}
```

Here `gamma_ij` identifies interface semantics, `Phi_ij` identifies the exchanged function/service/resource/information, `d_ij` records direction, `m_ij^cand` and `c_ij^cand` are candidate mechanism/context descriptors, `b_ij` records the admission basis, `E_ij` records evidence/provenance, `q_ij^evid` records evidence confidence, and `ell_ij` records relation resolution.

```math
\boxed{
\text{existence status}
\neq
\text{coupling strength}
\neq
\text{evidence confidence}.
}
```

Stage 1 does not estimate functional coupling strength:

```math
\boxed{
w_{ij}=\mathrm{NOT\ ESTIMATED\ IN\ STAGE\ 1}.
}
```

Evidence confidence may be numeric only under a declared auditable scoring/calibration method; otherwise it remains categorical.

## 12A. Hard scientific separation rules

```math
\boxed{
\begin{aligned}
\text{topology} &\neq \text{function},\\
\text{proximity} &\neq \text{dependency},\\
\text{correlation} &\neq \text{causality},\\
\text{standardized interface} &\neq \text{case-specific connection},\\
\text{case connection} &\neq \text{causal mechanism},\\
\text{dependency existence} &\neq \text{dependency strength},\\
\text{dependency strength} &\neq \text{evidence confidence}.
\end{aligned}
}
```

These are mandatory Stage-1 guardrails.

## 13. Normative and jurisdictional admissibility

```math
\boxed{
\text{standard/regulatory requirement}
\neq
\text{scientific mechanism}
\neq
\text{thesis mathematical contribution}.
}
```

The authority/requirements register is:

```math
\boxed{
\mathcal N_1=\{N_k\}.
}
```

Each authority record carries jurisdiction, authority/document type, edition/version, effective period, status, clause/locator, applicability, affected object, and verification state.

Normative admissibility remains distinct:

```math
\chi_{ij}^{\rm norm}
\in
\{\mathrm{PASS},\mathrm{CONDITIONAL},\mathrm{BLOCKED},\mathrm{N/A}\}.
```

```math
\boxed{
\chi_{ij}^{\rm norm}=\mathrm{PASS}
\not\Rightarrow
i\rightarrow j.
}
```

## 14. Entity and service traceability

Every retained entity must be traceable through:

```math
\boxed{
\text{entity}
\rightarrow
\text{layer}
\rightarrow
\text{geometry/topology}
\rightarrow
\text{engineering function}
\rightarrow
\text{resolution}
\rightarrow
\text{state schema}
\rightarrow
\text{service role}
\rightarrow
\text{requirement provenance}.
}
```

Ownership, operation, regulation, electrical supply, transport authority, and jurisdiction are distinct optional roles and are not assumed identical.

## 15. Requirement provenance

```math
\boxed{
\text{Need}
\rightarrow
\text{Requirement}
\rightarrow
\text{Measure}
\rightarrow
\text{Threshold/Rule}.
}
```

Stage 1 records provenance and applicability of requirements. Stage 5 later determines viability/reachability relative to accepted service constraints.

## 16. Stage-1 assumptions

```math
\boxed{
A_k^{(1)}
=
(\text{statement},\text{reason},\text{evidence},\text{consequence},\text{sensitivity test}).
}
```

No assumption may remain hidden in code, cleaning, crosswalk construction, temporal alignment, or topology repair.

## 17. Case-independent data architecture

```math
\boxed{
\text{heterogeneous source}
\rightarrow
\text{source adapter}
\rightarrow
\text{canonical intermediate representation}
\rightarrow
\text{clean/normalize}
\rightarrow
\text{QA/provenance}
\rightarrow
Z_1^{\rm impl+}.
}
```

Data zones are:

```text
RAW -> STAGING -> CANONICAL -> DERIVED -> RELEASE
```

RAW data are immutable. No silent imputation, unit conversion, CRS transformation, geometry repair, topology repair, deduplication, temporal reinterpretation, or crosswalk construction is permitted.

## 18. Canonical intermediate representation

The CIR comprises:

```text
CIR-1  Source manifest
CIR-2  Entity table
CIR-3  Intralayer edge table
CIR-4  Geometry table
CIR-5  Attribute/value table
CIR-6  Service traceability
CIR-7  Typed structural candidate relations (interface/exchange/context/evidence/resolution; no strength estimate)
CIR-8  Assumption register
CIR-9  QA ledger
CIR-10 Authority and requirements register
```

## 19. Generic source-adapter contract

Every source adapter exposes:

```text
inspect
validate_source
parse
map_schema
normalize
emit_canonical
report_provenance
report_quality
```

Source-specific semantics stop at the CIR boundary.

## 20. Complete Stage-1 handoff

```math
\boxed{
Z_1^{\rm impl+}
=
(
\mathcal S,
\mathcal G^{(1)},
R,
\mathcal Y;
\Omega_{\rm sys}^{+},
\mathcal C_{\rm cross},
\mathfrak R_1,
\mathcal T_{\rm svc},
\mathcal A_1,
\mathcal N_1,
\Pi_1
).
}
```

`R_1` is the typed Stage-1 relation-object register. `Pi_1` contains immutable source provenance, transforms, QA results, topology/spatial checks, temporal role, data-quality state, and release status.

## 21. Framework versus case

```math
\boxed{
G_1^{\rm framework}
\neq
G_1^{\rm case}(c).
}
```

Austin, Greensboro, Singapore, synthetic benchmarks, or future P–T cases instantiate the same framework through adapters and configuration. A blocked case does not invalidate the framework.

## 22. Verification result

The revised evidence-based framework was re-audited after introducing semantic entities, typed relation objects, modeling resolution, and separation of existence, strength, and evidence confidence.

Two verification layers passed:

```math
\boxed{
42/42\ \text{exact main-branch contract/invariant checks}=\mathrm{PASS},
}
```

and:

```math
\boxed{
19/19\ \text{controlled behavioral checks}=\mathrm{PASS}.
}
```

The exact repository checks cover schema versioning, semantic entity requirements, relation semantics, no Stage-1 strength estimation, no causal promotion, candidate-only mechanism labels, evidence-confidence discipline, verified-case structural evidence, P→T and T→P semantic heterogeneity, source classes, normative metadata, runtime guards, missingness, CRS, geometry repair and authority applicability.

The controlled behavioral checks execute the corresponding deterministic normalization and runtime-guard logic under Python 3.13.5 with the required scientific Python dependencies available.

The repository Python unit suite has also been expanded from 18 to 26 tests. GitHub-hosted Actions continues to return runner ID 0 with zero executed steps; that mirror remains classified `BLOCKED-ENVIRONMENT`, not as a scientific failure.

## 23. Final Stage-1 framework gate

```math
\boxed{
\begin{gathered}
\text{boundary explicit}
\land
\text{entities/layers typed}
\land
\text{topology semantics explicit}
\\
\land
\text{spatial/temporal provenance explicit}
\land
\text{structural candidates reproducible}
\land
\text{interface/exchange semantics explicit}
\land
\text{resolution explicit}
\\
\land
\text{existence/strength/confidence separated}
\land
\text{service/requirement traceability defined}
\land
\text{normative applicability separated from causality}
\\
\land
\text{generic schemas/adapters/QA verified}
\land
\text{no Stage-2 causal promotion}.
\end{gathered}
}
```

All framework-level conditions are now satisfied.

```math
\boxed{
G_1^{\rm framework}
=
\mathrm{PASS\ —\ READY\ FOR\ FREEZE}.
}
```

## 24. Freeze boundary

Freezing this framework will freeze the Stage-1 scientific/mathematical/data contract, not any particular case dataset. The Stage-1 Evidence and Ontology Register is part of the freeze authority and provides the literature-to-mathematics traceability for the semantic entity and relation objects.

Post-freeze case activities remain allowed under `G_1^{case}(c)` so long as they instantiate the frozen contract without silently redefining it.

A framework amendment is required only if a future case reveals a genuinely missing semantic class or invalidates a frozen Stage-1 assumption/contract.