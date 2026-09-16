# ASU Prior-Work FTEE/EGMIV Audit v1.0

**Date:** 2026-09-16  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Status:** PARTIAL EVIDENCE-QUALIFIED AUDIT; full-text access remains incomplete for several dissertations  
**Question:** What has ASU already established, implemented, tested, or validated—and exactly what mathematical integration remains for this MSE thesis?

## 1. Audit rule

This file separates four evidence levels:

- `FT` — full text or extended full-text manuscript available to the audit.
- `EX` — extended official ASU/author/publisher description with methods/results detail, but full text not fully retrievable in the active runtime.
- `AB` — abstract-level only.
- `PRJ` — official ASU project/tool documentation.

No `EX`, `AB`, or `PRJ` source is treated as if every equation or implementation detail had been checked in full text.

The extraction target is

```math
\boxed{
\text{source}
\rightarrow
\text{system/layers}
\rightarrow
\text{mechanism}
\rightarrow
\text{mathematical representation}
\rightarrow
\text{data}
\rightarrow
\text{test/validation}
\rightarrow
\text{established result}
\rightarrow
\text{reusable object}
\rightarrow
\text{remaining gap}.
}
```

## 2. FTEE/EGMIV extraction matrix

| ID | ASU work | Access | Systems/layers | Mechanism/model object | Test/validation | What ASU has already established | Reuse for this thesis | Remaining integration |
|---|---|---:|---|---|---|---|---|---|
| A01 | Hoff, R. M. (2023), *A Proposal for Infrastructure Adaptation and Cascading Failures for Black Swans* | FT/EX | multi-infrastructure | synthetic networks + interdependencies + cascading-failure model; dynamic criticality appears elsewhere in dissertation lineage | synthetic/cascade demonstrations and structured evidence synthesis | infrastructure adaptation can be studied by composing synthetic topology, interdependency and cascade models; data gaps and surprise/perfect-storm behavior are central | Chapter 2 precedent; benchmark for synthetic-network/cascade architecture | no demonstrated `P-T-I-O -> controlled viability -> geometric interface sensitivity` chain identified |
| A02 | Hoff & Chester (2023), *Preparing infrastructure for surprise: fusing synthetic network, interdependency, and cascading failure models* | FT | generic multi-infrastructure | conceptual integration of synthetic network generation, interdependency modeling, cascading-failure modeling | literature-grounded framework, not a held-out empirical validation of our proposed chain | integration of topology + dependency + cascade modeling is already established as a research architecture | do not claim novelty for combining these three ingredients | need explicit causal interface semantics, dynamic state coupling, posterior uncertainty, viability, and interface ranking |
| A03 | Gorman (2020), *Contingency Analysis for Coupled Power-Water Networks* | EX | power-water | steady-state co-simulation with OpenDSS + EPANET; coupled contingency analysis; cross-system failure propagation | Phoenix-scale generated networks; scenario/contingency results; N-1 reserve violations | quantitative coupled-infrastructure contingency analysis and cross-boundary propagation are already implemented at ASU | graph-to-physics comparator; scenario design precedent | not a dynamic `P<->T` feedback model with queue/memory/delay, nor controlled viability |
| A04 | RISE project, Metis/LEAPS | PRJ | power-water + human/operator coordination | OpenDSS + EPANET + interdependency wizard + real-time operation + post-scenario diagnostics + resiliency parameterization | operational simulation environment and operator studies | real-time coupled infrastructure simulation, control interaction, and explicit interdependency configuration already exist at ASU | software-architecture comparator; observation/control separation; operator-layer precedent | no evidence here of our proposed mathematical interface tuple, posterior-to-viability propagation, or geometric interface sensitivity |
| A05 | REFIT / ASU Resilient Infrastructure Toolkit | PRJ | power + water/stormwater + other infrastructure impacts | synthetic infrastructure model + physical interdependency model + probabilistic cascading-failure model + impact model | Monte Carlo / millions of iterations; impact propagation across infrastructures | geographically realistic synthetic infrastructure and stochastic cascade experimentation already exist | synthetic verification corpus; benchmark ranking/cascade workflow | not equivalent to dynamic `P-T-I-O` controlled viability or `S_ij^V` |
| A06 | Roy (2022), *Vulnerability Analysis and Protective Measures for the Design of a Secure, Resilient and Cost-Effective Smart Grid System* | FT/EX | power-communication | MIIM and Multi-State IIM; multi-valued logic; data dependency; secure routing/topology design | tested on Arizona substation-location data | information/communication interdependency and cascading failure are already modeled and tested at ASU | H2 information-layer comparator; discrete-state baseline | need joint continuous/hybrid `P,T,I,O` state dynamics and quantitative ablation of omitting `I,O` |
| A07 | Helmrich et al. (2021), *Centralization and decentralization for resilient infrastructure and complexity* | FT | network + governance + information | network-governance framing; information as mediator; central/decentral/distributed configurations | cross-sector literature synthesis | governance configuration and information mediation are already established resilience dimensions | theoretical basis for `Z_I, Z_O`; defines what must not be claimed as novel | still need measurable state variables, transition laws, control map `U(z_I,z_O)`, and validation |
| A08 | Hoff et al. (2023), *Dynamic criticality for infrastructure prioritization in complex environments* | FT/EX | infrastructure + organization | dynamic criticality as flexible reprioritization; adaptive capacity via goals, structures, sensemaking, strategies | inductive thematic analysis across sectors | static criticality is insufficient under changing disturbances; organizational adaptive capacity drives reprioritization | comparator for H4 and organization layer | our proposed `S_ij^V` must remain mathematically distinct: sensitivity of viability margin to interface parameter, not organizational reprioritization |
| A09 | Kim (2018) + Kim et al. (2022), safe-to-fail / SETS | EX/FT | social-ecological-technological + infrastructure | safe-to-fail; failure-consequence management; SETS interdependence and resilience capabilities | dissertation decision tools/case applications; peer-reviewed SETS synthesis | resilience should manage beyond-design failure consequences and embed nontechnical systems rather than treat them only as exogenous conditions | foundation for `K_sus`, service constraints, and inclusion of organization/information | safe-to-fail is not a viability kernel; formal controlled invariance and state-space viability remain to be built/tested |
| A10 | Moslehi (2018), *Sustainability Assessment of Community Scale Integrated Energy Systems* | EX | integrated energy + environmental/economic/resilience | quantitative sustainability indices; LCA; penalty-cost resilience; performance-based assessment | whole-year university-campus operational data | sustainability/resilience can be translated into quantitative engineering indices and trade-offs | provenance model for sustainability constraints and service-loss metrics | aggregate indices do not provide dynamic viable-set geometry or interface sensitivity |
| A11 | Markolf et al. (2022), efficiency-resilience transformations | FT/EX | infrastructure systems | efficiency-resilience trade-off; exploratory models/stakeholder coproduction | review/synthesis | resilience and efficiency can conflict; sustainable transformation requires dynamic balance | H5 objective/trade-off framing | no controlled viability optimization or interface-sensitive control law established |
| A12 | Kazemtarghi (2024), EV charging systems | EX | transportation-energy interface / EV-grid | bidirectional EV support, dynamic charging pricing, stochastic charging-station procurement | technical dissertation studies and optimization experiments | EVs are both grid loads and controllable grid resources; charging allocation and procurement can be optimized | H1 `T->P` load and optional V2G mechanism provenance | road-network state, charging queue/backlog, crew accessibility, and closed `P<->T` feedback are not jointly modeled here |
| A13 | Srivastava et al. (2026), PSI-Cascade | FT/EX | power-stormwater | spatially explicit coupled models; wind fragility -> power outage -> pump outage -> flooding | Phoenix city-scale storm; comparison with documented flooding patterns | hazard field -> fragility -> component failure -> cross-infrastructure cascade -> empirical pattern validation is already implemented at ASU | strongest comparator for H1 validation architecture | different sectors; one-way power-to-stormwater dependency; no `P-T-I-O` controlled viability chain |
| A14 | Sparks et al. (2023), synthetic power cascading whitepaper | EX | power | contingency analysis on synthetic transmission networks; repeated initial failures | repeated cascade simulations | synthetic networks are admissible for method development when real network data are restricted | numerical verification and cascade stress-testing precedent | synthetic evidence cannot substitute for held-out empirical H1b validation |
| A15 | LEAPS resilient infrastructure / synthetic power-water projects | PRJ | power, water, cyber, roads/transport | coupled infrastructure simulation; geographically realistic synthetic networks using OpenStreetMap, census/population, power-flow and water-demand assignments | laboratory/testbed and simulation program | ASU already treats power, roads/transport, cyber and other infrastructure as a coupled resilience problem and has synthetic-data methods | benchmark for synthetic model construction and testbed logic | thesis contribution cannot be “consider multiple infrastructures”; it must be the specific mathematical integration and its validation |

## 3. Canonical source URLs used in this audit

1. Hoff dissertation: `https://d1rbsgppyrdqq4.cloudfront.net/.../Hoff_asu_0010E_23035.pdf` (indexed full-text result; signed direct download expired in active runtime).
2. Hoff & Chester 2023: `https://doi.org/10.1088/2634-4505/acd07d`
3. Gorman 2020 KEEP: `https://keep.lib.asu.edu/items/158483`
4. RISE / Resilient Infrastructure Lab: `https://metis.asu.edu/resilience/`
5. REFIT: `https://refit.resilientinfrastructure.org/`
6. Roy 2022 KEEP: `https://keep.lib.asu.edu/items/171903`
7. Helmrich et al. 2021: `https://doi.org/10.1088/2634-4505/ac0a4f`
8. Hoff et al. 2023 dynamic criticality: `https://doi.org/10.1088/2634-4505/acbe15`
9. Kim 2018 KEEP: `https://keep.lib.asu.edu/items/156772`
10. Kim et al. 2022 SETS: `https://doi.org/10.1016/j.cosust.2022.101153`
11. Moslehi 2018 KEEP: `https://keep.lib.asu.edu/items/156680`
12. Markolf et al. 2022: `https://doi.org/10.1016/j.cosust.2022.101181`
13. Kazemtarghi 2024 KEEP: `https://keep.lib.asu.edu/items/193547`
14. Srivastava et al. 2026: `https://doi.org/10.1016/j.envsoft.2026.106980`
15. Synthetic power cascading whitepaper: `https://keep.lib.asu.edu/items/188186`
16. LEAPS projects: `https://leaps.asu.edu/projects/`

## 4. ASU-established boundary

Within the audited ASU corpus, the following are **not thesis novelty claims**:

```math
\boxed{
\begin{aligned}
&\text{interdependent-infrastructure simulation},\\
&\text{synthetic infrastructure networks},\\
&\text{cascading-failure modeling},\\
&\text{power-water coupling},\\
&\text{power-communication dependency},\\
&\text{EV-grid optimization},\\
&\text{governance/information relevance},\\
&\text{dynamic organizational criticality},\\
&\text{safe-to-fail resilience},\\
&\text{SETS interdependence},\\
&\text{quantitative resilience/sustainability trade-offs},\\
&\text{hazard->fragility->cascade->empirical comparison}.
\end{aligned}
}
```

## 5. Candidate mathematical integration that remains after ASU subtraction

The ASU-local residual is not “coupled infrastructure” in general. The candidate residual is the **specific composition**

```math
\boxed{
\mathcal G_{PTIO}
\rightarrow
\mathfrak I_{ij}^{\alpha\beta}
\rightarrow
F_{\mathcal G}
\rightarrow
p(Y\mid D)
\rightarrow
K_{\rm sus}
\rightarrow
\mathcal V_{\rm sus}
\rightarrow
\rho_g
\rightarrow
S_{ij}^{\mathcal V}
\rightarrow
u^\star
}
```

subject to evidence provenance and VVUQ.

This residual is **ASU-local and provisional**. It is not a global novelty claim.

## 6. Hypothesis-specific implications

### H1
ASU already recognizes the two mechanisms central to H1: electricity disruption can inhibit EV-enabled mobility, and transportation disruption can delay repair crews. ASU also has coupled physical co-simulation and empirical cascade-validation precedents. Therefore H1 must test the narrower claim:

```math
\boxed{
M_2^{PT,\,dynamic}
\text{ produces representation-distinguishable and, where data permit, more predictive service trajectories than }
M_0,M_1.
}
```

### H2
Information and organizational relevance is established conceptually and, for power-communication, mathematically. H2 must therefore be an **ablation/incremental-value** claim:

```math
\boxed{
M_{PTIO}\;\text{vs}\;M_{PT}
}
```

with measurable error/service/decision consequences.

### H3
Safe-to-fail and sustainability metrics are antecedents. Novelty cannot be “resilience + sustainability.” The candidate addition is controlled viability with evidence-grounded constraints:

```math
K_{\rm sus}\rightarrow\mathcal V_{\rm sus}.
```

### H4
Dynamic criticality already exists at ASU. Our candidate object must be explicitly distinct:

```math
S_{ij}^{\mathcal V}
=-\frac{\partial \rho_g}{\partial w_{ij}},
```

or a rigorously justified generalized sensitivity if differentiability fails.

### H5
ASU already performs resilience intervention selection and EV optimization. H5 must test whether **viability-informed** intervention outperforms matched simpler baselines under equal budgets/constraints.

## 7. Blockers

The audit is not marked fully complete because the active runtime did not retrieve publisher-original/full dissertation bytes for all priority works. In particular, full PDFs for Gorman 2020, Kim 2018, Moslehi 2018, and Kazemtarghi 2024 were not fully materialized even though official KEEP metadata and detailed descriptions were available. Signed CloudFront URLs surfaced by search were expired or non-materializable.

Therefore:

```math
\boxed{\text{Task 1 = substantial partial completion, but full-text closure remains BLOCKED_EXTERNAL_ACCESS.}}
```

No equation-level claim from those incompletely accessed dissertations is upgraded beyond what official ASU descriptions support.
