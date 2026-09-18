# Stage 1 Mathematical and Ontology Contract v1.2

**Status:** REVISED FINAL CANDIDATE — NEW EVIDENCE INTEGRATED; REVERIFICATION REQUIRED  
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
\Omega_{\rm sys}^{+}
=
(\Omega_x,\Omega_t,\Omega_{\rm infra},\Omega_{\rm service},\Omega_{\rm mode},\Omega_{\rm jur}).
```

where the factors specify geographic support, temporal support/vintage, retained infrastructure scope, service scope, admitted operating modes, and jurisdictional/normative applicability.

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

## 7. Thesis entity representation

`[THESIS-SYNTHESIS]`

Ontology/GIS and functional-dependency literature support semantic infrastructure entities, but the exact thesis tuple below is a thesis construction:

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

where:

```math
\begin{aligned}
r_i &= \text{location/geometry reference},\\
f_i &= \text{engineering function/service roles},\\
\mathcal Y_i &= \text{declared state schema},\\
o_i &= \text{ownership/operator roles},\\
a_i &= \text{authority/regulatory roles},\\
\ell_i &= \text{modeling resolution level},\\
\mathcal D_i &= \text{evidence/data/provenance references}.
\end{aligned}
```

This retains the thesis-wide use of `r_i` for geometry rather than reusing `x_i`, which is reserved from state notation.

## 8. Structural-admissibility predicate

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

## 9. Structural candidate set

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

## 10. Geographic co-exposure guardrail

The frozen wording is:

```math
\boxed{
\text{spatial proximity alone}
\not\Rightarrow
\text{functional/causal dependency}.
}
```

A shared local hazard pathway may justify a geographic co-exposure candidate but still does not establish a functional causal dependency.

## 11. Relation-status ontology

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

## 12. Stage-1 relation representation

`[THESIS-SYNTHESIS]`

Stage 1 represents more than a node pair while remaining explicitly pre-causal:

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

where:

```math
\begin{aligned}
\gamma_{ij} &= \text{interface semantics / interface class},\\
\Phi_{ij} &= \text{exchanged function/service/resource/information semantics},\\
d_{ij} &= \text{declared direction of the candidate relation},\\
m_{ij}^{\rm cand} &= \text{candidate mechanism family},\\
c_{ij}^{\rm cand} &= \text{candidate operating/activation context},\\
b_{ij} &= \text{basis for structural admission},\\
s_{ij} &= \text{Stage-1 relation/evidence status},\\
\mathcal E_{ij} &= \text{evidence/provenance references},\\
q_{ij}^{\rm evid} &= \text{evidence-confidence representation},\\
\ell_{ij} &= \text{relation modeling resolution},\\
\chi_{ij}^{\rm norm} &= \text{normative/jurisdictional admissibility}.
\end{aligned}
```

The candidate mechanism and operating context are descriptors inherited from prior evidence; they are not accepted Stage-2 mechanisms.

The following quantities are frozen as distinct:

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

Evidence confidence may be represented numerically only under a declared, auditable calibration/scoring rule; otherwise a categorical confidence class plus method/provenance is required.

## 13. Entity-to-service traceability schema

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
| engineering_function | engineering function/role of the entity |
| state_schema | later state variables associated with the entity |
| service_roles | service quantities the entity may contribute to |
| resolution_level | component/facility/network/agent/aggregate or other declared modeling level |
| evidence_refs | evidence/provenance references supporting semantics and inclusion |
| provenance_status | source/vintage/license/hash/QC state |
| inclusion_rule | why retained |
| exclusion_rule | why excluded, if applicable |

The service-role field is structural traceability only. It does not assert causal effect magnitude.

## 13A. Hard scientific separation rules

`[THESIS-SYNTHESIS]`

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

These distinctions are mandatory Stage-1 guardrails.

## 14. Normative and jurisdictional admissibility

`[THESIS]`

Standards, codes, statutes, regulations, utility procedures, and local engineering rules constrain what is permissible, required, or conformant, but they do not establish scientific causality.

```math
\boxed{
\text{standard/regulatory requirement}
\neq
\text{scientific mechanism}
\neq
\text{thesis mathematical contribution}.
}
```

Define the normative register

```math
\boxed{
\mathcal N_1
=
\{N_k\}_{k=1}^{n_N},
}
```

with

```math
N_k
=
(
ID_k,
A_k^{\rm auth},
J_k,
V_k^{\rm ed},
S_k^{\rm status},
T_k^{\rm eff},
C_k^{\rm clause},
\chi_k^{\rm app},
O_k^{\rm affected}
).
```

where the fields identify the authority/document, jurisdiction, edition/version, publication/status state, effective period, clause or requirement locator, applicability decision, and affected Stage-1 object.

Normative admissibility for a structural relation is kept distinct from structural admissibility:

```math
\chi_{ij}^{\rm norm}
\in
\{
\mathrm{PASS},
\mathrm{CONDITIONAL},
\mathrm{BLOCKED},
\mathrm{N/A}
\}.
```

Therefore:

```math
\boxed{
\Gamma_{ij}^{\rm str}=1
\not\Rightarrow
\chi_{ij}^{\rm norm}=\mathrm{PASS}
}
```

and:

```math
\boxed{
\chi_{ij}^{\rm norm}=\mathrm{PASS}
\not\Rightarrow
i\rightarrow j.
}
```

The first rule separates structural compatibility from legal/standards applicability. The second prevents normative conformity from being misrepresented as a causal mechanism.

Entity records may also distinguish, where relevant:

```text
owner
operator
regulator
electrical_supplier
transport_authority
jurisdiction
```

because ownership, operating authority, regulatory authority, and physical/electrical supply roles are not assumed identical.

## 15. Requirement provenance

`[THESIS]`

Service requirements may originate from engineering needs, standards, regulations, utility procedures, agency requirements, or thesis-declared analytical thresholds. Stage 1 records the provenance without deciding Stage-5 viability.

Each requirement trace should contain:

```text
requirement_id
service_id
requirement_source
authority_id
authority_level
measure
unit
threshold_or_rule
effective_period
applicability
verification_status
```

This establishes the trace:

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

A requirement may constrain later service or intervention definitions, but Stage 1 does not infer dynamic performance from the requirement itself.

## 16. Stage-1 assumptions

`[ASSUMP]`

Stage-1 assumptions must be registered as:

```math
A_k^{(1)}
=
(\text{statement},\text{reason},\text{evidence},\text{consequence},\text{sensitivity test}).
```

At minimum, the case must explicitly state assumptions concerning boundary vintage, coordinate consistency, asset persistence through the study period, semisynthetic crosswalks, road-network cleaning/snap tolerances, and any retrospective signal/sensor filtering.

## 17. Stage-1 implementation handoff

`[THESIS]`

The canonical Stage-1 output remains `S,G,X,Y` in the framework authority. The implementation package extends that output without replacing it:

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

where:

- `R` = spatial embedding;
- `Y`/`mathcal Y` = state schema/state-space declaration, not Stage-3 trajectory;
- `C_cross` = structural candidate pair set;
- `R_1` = typed Stage-1 relation-object register `mathfrak R_{ij}^{alpha beta,(1)}`;
- `T_svc` = entity-to-service traceability table;
- `A_1` = Stage-1 assumption register;
- `N_1` = normative/authority and requirement-provenance register;
- `Pi_1` = provenance/QC bundle.

## 18. Stage-1 verification obligations

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
\text{interface/exchange semantics explicit}
\land
\text{resolution declared}
\land
\text{existence/strength/confidence separated}
\land
\text{service traceability complete}
\land
\text{normative applicability resolved where relevant}
\\
\land
\text{provenance complete}
\land
\text{no Stage-2 causal promotion in Stage 1}.
\end{gathered}
}
```

The gate is developmental verification supporting H1; it is not itself H1.

## 19. What literature must and need not justify

Literature is required for the scientific legitimacy of SoS reasoning, multilayer/network representation, infrastructure dependency concepts, spatial/geographic relations, and domain-specific entity/interface semantics.

Literature is **not** required to contain the exact thesis notation `Gamma^str`, the thesis entity tuple `E_i^alpha`, the Stage-1 relation tuple `mathfrak R_ij^(1)`, `C_struct`, `T_svc`, `Z1_impl+`, or the PASS/FAIL/BLOCKED packaging. These are thesis-defined methodological objects and are valid if internally coherent, physically interpretable, explicitly declared, and verified against case data.

## 20. Freeze state

The **Stage-1 mathematical/ontology contract has been revised using the Stage-1 Evidence and Ontology Register**. Framework freeze requires successful re-verification of the revised machine/data contracts and fixtures. Case-specific instantiations remain governed by separate `G_1^{case}` gates and do not control framework validity.