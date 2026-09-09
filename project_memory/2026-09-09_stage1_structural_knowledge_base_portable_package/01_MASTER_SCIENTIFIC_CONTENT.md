# Master Scientific Content — Stage 1 Structural Knowledge Base

## 1. Scientific position

Stage 1 is not only a network diagram. It is an **auditable structural knowledge base** for the coupled Power–Transportation–Information–Organization system.

A heterogeneous network-of-networks is necessary because the four subsystems contain different entity types and link semantics. However, ordinary graph topology alone cannot distinguish a true non-dependency from an unobserved, conditional, latent, or unresolved relation.

The Stage-1 representation is therefore:

```math
\boxed{
\mathfrak M_1=
(\mathcal G,\mathcal R,\mathcal U,\mathcal H,\mathcal E,Y_0)
}
```

with:

- `\mathcal G`: heterogeneous network-of-networks structure;
- `\mathcal R`: known relations/dependencies;
- `\mathcal U`: non-relations and unresolved relations;
- `\mathcal H`: hidden or latent candidate relations;
- `\mathcal E`: evidence/provenance;
- `Y_0`: initial system state.

## 2. Structural skeleton

```math
\boxed{\mathcal G=\{\mathcal G_P,\mathcal G_T,\mathcal G_I,\mathcal G_O,E_\times\}}
```

where:

- `\mathcal G_P`: electrical topology;
- `\mathcal G_T`: transportation topology;
- `\mathcal G_I`: information/communication topology when explicitly represented;
- `\mathcal G_O`: actor/coordination topology when explicitly represented;
- `E_\times`: directed cross-system relations.

The network-of-networks answers:

```math
\boxed{\text{What exists and how is it structurally connected?}}
```

It does **not** by itself answer whether an absent edge is a true non-dependency, a conditional dependency, or a hidden relation.

## 3. Object classes

Use four distinct object classes:

```math
\boxed{\text{Node}\neq\text{Link}\neq\text{Interface asset}\neq\text{Agent}}
```

### Node
A state-holding, injection/withdrawal, junction, observation, or decision entity.

Examples: electrical bus, road junction, RTU, control center, utility operator.

### Link
A connector that transfers electricity, mobility, information, authority, or resources.

Examples: feeder, road segment, communication channel, task-assignment relation.

### Interface asset
A cross-system object that converts or transfers service between subsystems.

Examples: EV charging station, V2G connection point.

### Agent
A mobile or decision entity that acts on a network without defining its fixed topology.

Examples: EV, repair crew, mobile battery, emergency vehicle.

## 4. Subsystem entities

### Power

Recommended detailed boundary: urban/distribution electricity system with upstream transmission treated as a boundary condition.

Nodes and devices include buses, substations, transformers, DER/BESS connection points, loads, and P–T interface ports. Links include feeders, lines, transformers, and switchable branches.

### Transportation

Nodes include intersections, origin/destination points, depots, charging access points, and critical destinations. Links are directed road segments/corridors. EVs and repair vehicles are modeled as agents moving on the transport graph.

### Information

When explicit topology is needed, nodes include sensors, RTUs/IEDs, routers/gateways, data centers, SCADA, and traffic-management centers. Links include telemetry, communication, and command channels.

### Organization

Nodes are decision-capable actors, not buildings: utility operations, distribution operator, traffic management center, emergency management, EV/fleet operator, repair crews. Relations include authority, coordination, task assignment, resource transfer, and information-sharing.

## 5. Interface assets and ports

A charging station should not be duplicated as unrelated power and transportation nodes. Use a single interface object:

```math
\boxed{c_k^{EVCS}=(\pi_k^P,\pi_k^T,X_k^C,\Theta_k^C)}
```

with one port connected to a power bus and one port connected to a transportation access node.

## 6. Dependency-status architecture

For every admissible candidate relation, assign:

```math
\boxed{S_{ij}\in\{D,N,C,L,U\}}
```

where:

- `D`: confirmed dependency;
- `N`: scope-qualified non-dependency;
- `C`: conditional dependency;
- `L`: latent/hidden candidate;
- `U`: unknown/unresolved.

Critical rule:

```math
\boxed{\text{absence of evidence}\neq\text{evidence of absence}}
```

Therefore an ordinary zero in an adjacency matrix must not automatically be interpreted as a scientifically established non-dependency.

## 7. Typed relation record

Every retained or audited relation should be represented by:

```math
\boxed{
r_{ij}=
(i,j,d_{ij},\chi_{ij},\gamma_{ij},\phi_{ij},\psi_{ij},g_{ij},S_{ij},\eta_{ij})
}
```

where:

- `i,j`: source and target entities;
- `d_{ij}`: direction;
- `\chi_{ij}`: dependency type;
- `\gamma_{ij}`: carrier/service;
- `\phi_{ij}`: mechanism;
- `\psi_{ij}`: activation condition;
- `g_{ij}`: geographic relation;
- `S_{ij}`: relation status;
- `\eta_{ij}`: evidence/provenance.

Use the Rinaldi taxonomy as a primary classification: physical, cyber/informational, geographic, and logical. Logical relations should be tied to explicit human decisions, rules, procedures, or institutional constraints when possible.

## 8. Distinguish relation classes

The model must keep the following distinct:

```math
\boxed{\text{Connectivity}\neq\text{Dependency}\neq\text{Co-exposure}\neq\text{Causality}}
```

Examples:

- a power bus electrically connected to an EVCS is structural connectivity and likely a physical dependency;
- a substation and nearby road flooded simultaneously may be geographically co-exposed without either causing the other to fail;
- an absent observed relation may still be conditional or latent;
- causal propagation is handled in Stage 2, not inferred automatically from Stage-1 connectivity.

## 9. Hidden and latent relations

Hidden-relation discovery should use multiple evidence routes:

1. peer-reviewed literature and engineering mechanisms;
2. operating procedures, emergency plans, institutional rules, regulations;
3. historical event evidence;
4. constrained causal-discovery methods where adequate multivariate time-series data exist.

Causal discovery is a candidate-generation and validation aid, not a substitute for engineering mechanisms.

## 10. Evidence architecture

Every included, excluded, conditional, latent, or unresolved relation should have provenance.

Recommended evidence hierarchy:

- Direct engineering/asset/operator evidence;
- Official documentation and procedures;
- Peer-reviewed mechanism evidence;
- Empirical statistical evidence;
- Hypothesized/scenario-only.

A relation should not enter the baseline model without direction, mechanism, status, and evidence.

## 11. Stage-1A completeness protocol

Define the complete entity ontology:

```math
\boxed{\Omega=\{V_P,E_P,V_T,E_T,V_I,E_I,V_O,E_O,V_C\}}
```

Then define an engineering-admissible candidate relation universe:

```math
\boxed{\mathcal Q_{adm}=\{(i,j):\text{cross-system interaction is physically, informationally, or organizationally admissible}\}}
```

Do not use the unrestricted Cartesian product as the candidate universe.

Every candidate receives one status `D,N,C,L,U`.

## 12. Completeness audit

Define:

```math
\boxed{C_{audit}=\frac{|Q_D|+|Q_N|+|Q_C|+|Q_L|+|Q_U|}{|Q_{adm}|}}
```

Require:

```math
\boxed{C_{audit}=1}
```

This means every admissible candidate has been audited, not that every relation is resolved.

Additional diagnostics:

```math
\boxed{C_{resolved}=\frac{|Q_D|+|Q_N|+|Q_C|}{|Q_{adm}|}}
```

```math
\boxed{C_{latent}=\frac{|Q_L|}{|Q_{adm}|},\qquad C_{unknown}=\frac{|Q_U|}{|Q_{adm}|}}
```

These are thesis-specific completeness metrics, not claimed universal standards.

## 13. Operationalized canonical object

```math
\boxed{
\mathfrak M_1^{*}=
(\Omega,\mathcal G,\mathcal Q_{adm},\mathbf S,\mathcal R_D,\mathcal R_N,\mathcal R_C,\mathcal R_L,\mathcal R_U,\mathcal E_{prov},Y_0,\Lambda_{sus})
}
```

with:

- `\mathcal R_D`: confirmed dependencies;
- `\mathcal R_N`: scope-qualified non-dependencies;
- `\mathcal R_C`: conditional dependencies;
- `\mathcal R_L`: latent candidates;
- `\mathcal R_U`: unresolved relations;
- `\Lambda_{sus}`: sustainability-traceable metadata only.

## 14. Sustainability governance

Sustainability is not represented as another network layer in Stage 1.

Stage 1 stores asset-level metadata such as technology, energy carrier, material class, ownership, service zone, and resource characteristics.

Later:

```math
\boxed{\text{Stages 1–5 resilience outputs}+\Lambda_{sus}\xrightarrow{\Phi_{sus}}\text{Stage 6 transformation requirements}\rightarrow\text{Stage 7 pathways}}
```

## 15. Boundary to later stages

```math
\boxed{\text{Stage 1: What can interact?}}
```

```math
\boxed{\text{Stage 2: What causes what, and why?}}
```

```math
\boxed{\text{Stage 3: How strongly, how fast, and how does state evolve?}}
```

Stage 1 therefore ends with a frozen, evidence-audited structural knowledge base `\mathfrak M_1^*`, not with causal conclusions.
