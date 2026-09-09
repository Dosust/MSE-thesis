# Stage 1A — Structural Identification & Completeness Protocol

```text
Stage 1A — Structural Identification & Completeness Protocol
│
├── 1. Entity Ontology Ω
│   ├── Power entities
│   ├── Transportation entities
│   ├── Information entities
│   ├── Organizational entities
│   └── Interface assets
│
├── 2. Admissible Relation Universe Qadm
│   ├── Physically admissible pairs
│   ├── Information-compatible pairs
│   ├── Organizationally admissible pairs
│   └── Exclude impossible pairings
│
├── 3. Relation-Status Matrix Sij
│   ├── D — dependency
│   ├── N — non-dependency within scope
│   ├── C — conditional
│   ├── L — latent candidate
│   └── U — unknown
│
├── 4. Relation Semantics rij
│   ├── Direction
│   ├── Type
│   ├── Carrier
│   ├── Mechanism
│   ├── Activation condition
│   ├── Spatial relation
│   └── Evidence
│
├── 5. Hidden-Relation Discovery
│   ├── Literature and engineering mechanisms
│   ├── Operational plans and rules
│   ├── Event evidence
│   └── Constrained causal discovery
│
├── 6. Evidence Triangulation
│   ├── Direct engineering evidence
│   ├── Operator / official documentation
│   ├── Peer-reviewed mechanism evidence
│   ├── Empirical statistical evidence
│   └── Hypothesized only
│
├── 7. Completeness Audit
│   ├── Caudit = 1
│   ├── Cresolved
│   ├── Clatent
│   └── Cunknown
│
└── Output
    └── Frozen Stage-1 Structural Knowledge Base 𝔐₁*
```

## Formal objects

```math
\boxed{\Omega=\{V_P,E_P,V_T,E_T,V_I,E_I,V_O,E_O,V_C\}}
```

```math
\boxed{\mathcal Q_{adm}=\{(i,j):\text{cross-system interaction is engineering-admissible}\}}
```

```math
\boxed{S_{ij}\in\{D,N,C,L,U\}}
```

```math
\boxed{r_{ij}=(i,j,d_{ij},\chi_{ij},\gamma_{ij},\phi_{ij},\psi_{ij},g_{ij},S_{ij},\eta_{ij})}
```

```math
\boxed{C_{audit}=\frac{|Q_D|+|Q_N|+|Q_C|+|Q_L|+|Q_U|}{|Q_{adm}|}=1}
```

```math
\boxed{C_{resolved}=\frac{|Q_D|+|Q_N|+|Q_C|}{|Q_{adm}|}}
```

```math
\boxed{C_{latent}=\frac{|Q_L|}{|Q_{adm}|},\qquad C_{unknown}=\frac{|Q_U|}{|Q_{adm}|}}
```

## Scientific interpretation

- `D`: evidence-supported dependency.
- `N`: non-dependency only within the declared model boundary, hazard regime, operating conditions, and time horizon.
- `C`: dependency activated only under defined conditions.
- `L`: plausible hidden/latent candidate requiring mechanism verification.
- `U`: unresolved relation; insufficient evidence for inclusion or exclusion.

The key epistemic rule is:

```math
\boxed{A_{ij}=0\not\Rightarrow\text{scientifically proven non-dependency}}
```

## Frozen output

```math
\boxed{\mathfrak M_1^{*}=(\Omega,\mathcal G,\mathcal Q_{adm},\mathbf S,\mathcal R_D,\mathcal R_N,\mathcal R_C,\mathcal R_L,\mathcal R_U,\mathcal E_{prov},Y_0,\Lambda_{sus})}
```

Only after this object is audited should the study advance to Stage 2 causal mechanisms.
