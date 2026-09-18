# Stage 1 Mathematical and Ontology Contract v1.0

**Status:** FROZEN METHODOLOGICAL CONTRACT  
**Date:** 2026-09-18  
**Stage:** 1 — Spatiotemporal Multilayer System-of-Systems Structure  
**Canonical authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md` + `CANONICAL_RQ_SO_HYPOTHESES_V3.md`

## 1. Provenance rule for mathematics

Stage-1 mathematics is not required to be copied equation-by-equation from the literature. Every mathematical object is instead assigned one provenance class:

| Label | Meaning |
|---|---|
| `[LIT]` | established mathematical/theoretical object used substantially as published |
| `[ADAPT]` | established object adapted to the P–T thesis |
| `[THESIS]` | object defined by the thesis methodology to answer RQ1/SO1 |
| `[ASSUMP]` | explicit modeling assumption requiring sensitivity/validity treatment |
| `[CASE]` | case-specific instantiation/data realization |

The admissibility rule is:

`literature foundation + engineering semantics + explicit assumptions + thesis methodology -> admissible Stage-1 mathematics`.

No thesis-defined object is represented as a published standard unless a source establishes it.

## 2. Stage-1 question and responsibility

**RQ1:** What entities exist, what layers constitute the system, and where can interactions occur?

Stage 1 answers only structural/spatial questions. It does not promote a structural relation to a causal dependency.

```math
\boxed{\text{Stage 1 = structural possibility}\qquad\text{Stage 2 = causal qualification}.}
```

## 3. System scope and typed layers

`[ADAPT/THESIS]`

```math
\mathcal S=\{P,T,I,O\},
\qquad
\mathcal S_{\rm phys}=\{P,T\},
\qquad
\mathcal S_{\rm sup}=\{I,O\}.
```

`P,T` are physical constituent infrastructure systems. `I,O` are supporting information and organization domains.

## 4. System boundary

`[THESIS]`

```math
\Omega_{\rm sys}
=
(\Omega_x,\Omega_t,\Omega_{\rm infra},\Omega_{\rm service},\Omega_{\rm mode}).
```

where the factors specify geographic support, temporal support/vintage, retained infrastructure scope, service scope, and admitted operating modes.

Boundary membership is a modeling decision and must be provenance-controlled.

## 5. Typed constituent graphs

`[LIT/ADAPT]`

```math
G_P=(V_P,E_P,\lambda_P),
\qquad
G_T=(V_T,E_T,\lambda_T),
```

where `lambda_P` and `lambda_T` type node/edge semantics. Electrical edges and traversable-road edges remain semantically distinct.

The structural multilayer graph is:

```math
\mathcal G^{(1)}
=
(\mathcal V,\mathcal E_{\rm intra},R,\Lambda),
```

with:

```math
\mathcal V=V_P\cup V_T\cup V_I\cup V_O,
\qquad
\mathcal E_{\rm intra}=E_P\cup E_T\cup E_I\cup E_O.
```

`R={r_i}` is the spatial embedding and `Lambda` stores entity/layer/edge types.

## 6. Coordinate and state notation freeze

The following notation is frozen to remove the `x_i` ambiguity:

| Symbol | Meaning |
|---|---|
| `r_i` | spatial coordinate/geometry reference of entity `i` |
| `X_P(t)` | physical Power-system state vector |
| `X_T(t)` | physical Transportation-system state vector |
| `z_I(t)` | Information-domain state |
| `z_O(t)` | Organization-domain state |
| `Y(t)` | integrated state `[X_P,X_T,z_I,z_O]^T` |
| `Y_i` | state schema/value associated with entity `i`, where applicable |

Thus:

```math
r_i\in\mathbb R^2
```

for point-like physical assets where a 2-D coordinate is meaningful, while dynamic state variables are never denoted by the same symbol.

## 7. Structural-admissibility predicate

`[THESIS]`

A cross-layer pair may enter the Stage-1 candidate set only through the non-causal structural predicate:

```math
\Gamma_{ij}^{\rm str}
=
\Gamma(
A_{ij},
H_{ij},
S_{ij},
L_{ij},
C_{ij},
\Pi_{ij}
),
```

where:

- `A_ij` = asset-identity/crosswalk evidence;
- `H_ij` = documented interface hardware or service-port compatibility;
- `S_ij` = spatial relation / geometry;
- `L_ij` = access/connectivity geometry relevant to possible interaction;
- `C_ij` = common local co-exposure/geographic relation, if applicable;
- `Pi_ij` = provenance and data-quality metadata.

`Gamma_ij^str` is Boolean at Stage 1:

```math
\Gamma_{ij}^{\rm str}\in\{0,1\}.
```

It may not use Stage-2 mechanism strength, causal-effect estimates, activation probabilities, or H1 outcomes.

## 8. Structural candidate set

`[THESIS]`

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

Therefore:

```math
\Gamma_{ij}^{\rm str}=1
\not\Rightarrow
i\rightarrow j.
```

Stage 1 identifies where a relation is structurally admissible for investigation; Stage 2 determines whether a causal dependency exists.

## 9. Geographic co-exposure guardrail

The frozen wording is:

```math
\boxed{
\text{spatial proximity alone}
\not\Rightarrow
\text{functional/causal dependency}.
}
```

A shared local hazard pathway may justify a geographic co-exposure candidate but still does not establish a functional causal dependency.

## 10. Relation-status ontology

`[THESIS]`

Three relation classes are frozen:

```math
\mathcal R_{\rm prior},
\qquad
\mathcal C_{\rm struct},
\qquad
\mathbb I_{\rm acc}.
```

- `R_prior`: literature/operator/data documentation reports that a relationship or mechanism class can exist;
- `C_struct`: a relation is structurally admissible in the declared study system under `Gamma^str`;
- `I_acc`: Stage-2 accepted causal dependency after mechanism/provenance/activation/uncertainty qualification.

Mandatory guardrails:

```math
\mathcal R_{\rm prior}\not\Rightarrow\mathbb I_{\rm acc},
```

```math
\mathcal C_{\rm struct}\not\Rightarrow\mathbb I_{\rm acc}.
```

Stage 1 is prohibited from assigning `I_acc`.

## 11. Entity-to-service traceability schema

`[THESIS]`

Every retained Stage-1 entity type must have a traceability row with:

| Field | Meaning |
|---|---|
| entity_id | immutable case identifier |
| entity_type | typed asset/entity class |
| layer | P/T/I/O |
| source_dataset | evidence/data source |
| geometry | coordinate/line/polygon/reference |
| intra_edge_semantics | meaning of same-layer connectivity |
| state_schema | later state variables associated with the entity |
| service_roles | service quantities the entity may contribute to |
| provenance_status | source/vintage/license/hash/QC state |
| inclusion_rule | why retained |
| exclusion_rule | why excluded, if applicable |

The service-role field is structural traceability only. It does not assert causal effect magnitude.

## 12. Stage-1 assumptions

`[ASSUMP]`

Stage-1 assumptions must be registered as:

```math
A_k^{(1)}
=
(\text{statement},\text{reason},\text{evidence},\text{consequence},\text{sensitivity test}).
```

At minimum, the case must explicitly state assumptions concerning boundary vintage, coordinate consistency, asset persistence through the study period, semisynthetic crosswalks, road-network cleaning/snap tolerances, and any retrospective signal/sensor filtering.

## 13. Stage-1 implementation handoff

`[THESIS]`

The canonical Stage-1 output remains `S,G,X,Y` in the framework authority. The implementation package extends that output without replacing it:

```math
\boxed{
Z_1^{\rm impl}
=
(
\mathcal S,
\mathcal G^{(1)},
R,
\mathcal Y;
\Omega_{\rm sys},
\mathcal C_{\rm cross},
\mathcal T_{\rm svc},
\mathcal A_1,
\Pi_1
).
}
```

where:

- `R` = spatial embedding;
- `Y`/`mathcal Y` = state schema/state-space declaration, not Stage-3 trajectory;
- `C_cross` = structural candidate relation register;
- `T_svc` = entity-to-service traceability table;
- `A_1` = Stage-1 assumption register;
- `Pi_1` = provenance/QC bundle.

## 14. Stage-1 verification obligations

`[THESIS/METHODOLOGY]`

Stage 1 passes only if:

```math
\boxed{
\begin{gathered}
\text{boundary explicit}
\land
\text{entities typed}
\land
\text{intralayer topology verified}
\\
\land
\text{spatial support verified}
\land
\text{candidate relations reproducible}
\land
\text{service traceability complete}
\\
\land
\text{provenance complete}
\land
\text{no Stage-2 causal promotion in Stage 1}.
\end{gathered}
}
```

The gate is developmental verification supporting H1; it is not itself H1.

## 15. What literature must and need not justify

Literature is required for the scientific legitimacy of SoS reasoning, multilayer/network representation, infrastructure dependency concepts, spatial/geographic relations, and domain-specific entity/interface semantics.

Literature is **not** required to contain the exact thesis notation `Gamma^str`, `C_struct`, `T_svc`, `Z1_impl`, or the PASS/FAIL/BLOCKED packaging. These are thesis-defined methodological objects and are valid if internally coherent, physically interpretable, explicitly declared, and verified against case data.

## 16. Freeze state

The **Stage-1 mathematical/ontology contract is frozen** by this file.

This does not freeze the case-specific Stage-1 instantiation. The case remains OPEN until the required Austin structural-data and provenance gates pass.