# arXiv-to-Journal Verification and Critical Evidence Audit — Stage 1 Structure

**Status:** ACTIVE / VERIFIED EVIDENCE AUDIT  
**Date:** 2026-09-18  
**Stage:** 1 — Spatiotemporal Multilayer System-of-Systems Structure  
**Canonical RQ1:** What entities exist, what layers constitute the system, and where can interactions occur?

## 1. Critical conclusion

The literature strongly supports a multilayer/System-of-Systems structural representation, explicit system context and boundaries, distinct constituent-system semantics, spatial embedding, and explicit cross-layer interfaces. It does **not** establish the thesis's exact Stage-1 tuple, candidate-pair notation, or Stage-1→Stage-2 gate as universal standards.

The strongest defensible statement is:

`established structural/network/SoS foundations + thesis-specific evidence governance -> Stage-1 structural architecture`.

Stage 1 should therefore be presented as an **evidence-grounded structural ontology and handoff**, while Stage 2 remains responsible for causal qualification.

## 2. arXiv-to-journal verification

| Source | arXiv status | Verified journal status | Admission |
|---|---|---|---|
| Kivelä et al., arXiv:1309.7233 | arXiv review | Journal of Complex Networks 2(3), 203–271 (2014), DOI [10.1093/comnet/cnu016](https://doi.org/10.1093/comnet/cnu016) | [ARX-J][FND][MATH] |
| De Domenico et al., arXiv:1307.4977 | arXiv manuscript | Physical Review X 3, 041022 (2013), DOI [10.1103/PhysRevX.3.041022](https://doi.org/10.1103/PhysRevX.3.041022) | [ARX-J][FND][MATH] |
| Mahabadi, Varga, & Dolan, arXiv:2105.12701 | arXiv systematic review | IEEE Access 9, 135755–135773 (2021), DOI [10.1109/ACCESS.2021.3116868](https://doi.org/10.1109/ACCESS.2021.3116868) | [ARX-J][SR][DIR-CI] |
| Danziger et al., arXiv:1505.01688 | arXiv paper | no peer-reviewed journal version verified in this audit | [ARX-P][MATH/CI]; discovery only |
| Vaknin et al., arXiv:2106.14084 | arXiv manuscript | New Journal of Physics 23, 113001 (2021), DOI [10.1088/1367-2630/ac2e3c](https://doi.org/10.1088/1367-2630/ac2e3c) | [ARX-J][MATH/CI] |

## 3. Claim-by-claim Stage-1 audit

### S1.1 — Canonical RQ1

**Status: PASS / SCIENTIFICALLY WELL-POSED.**

RQ1 asks for entities, layers, and locations of possible interaction. This is consistent with systems engineering's use of system context and boundaries and with multilayer-network theory's separation of entities, layers, and relation types. ISO/IEC/IEEE 15288:2023 explicitly applies systems-engineering processes to systems of interest, system elements, and systems of systems, while SEBoK treats system context as the system-of-interest plus its environment and relationships.

**Primary sources:** [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html); [SEBoK — Engineered System Context](https://sebokwiki.org/wiki/Engineered_System_Context); [Kivelä et al., 2014](https://doi.org/10.1093/comnet/cnu016).

### S1.2 — Stage 1 as structure before causality

**Status: STRONGLY DEFENSIBLE AS THESIS GOVERNANCE; NOT A UNIVERSAL PUBLISHED STAGING RULE.**

Kivelä et al. and De Domenico et al. establish mathematical representations for multilayer structure. Ouyang and Zhang–Peeta show that infrastructure systems may have disparate physical/operational characteristics and that additional mechanisms are required to represent cross-system interdependencies. Mahabadi et al. further show that much multilayer-infrastructure literature relies on simplified synthetic interlayer relations, with directed links, feedback conditions, and real-world data comparatively rare.

Therefore the thesis separation

`Stage 1 = structural possibility`

`Stage 2 = causal qualification`

is a rigorous **research-design rule**. It should not be attributed to one paper as a standard two-stage infrastructure methodology.

**Primary sources:** [Kivelä et al., 2014](https://doi.org/10.1093/comnet/cnu016); [De Domenico et al., 2013](https://doi.org/10.1103/PhysRevX.3.041022); [Zhang & Peeta, 2011](https://doi.org/10.1016/j.trb.2010.10.001); [Mahabadi et al., 2021](https://doi.org/10.1109/ACCESS.2021.3116868).

### S1.3 — Explicit system boundary

**Status: ESTABLISHED SYSTEMS-ENGINEERING FOUNDATION.**

SEBoK defines engineered-system context around a selected system of interest and distinguishes narrower/wider systems of interest and their environment. ISO/IEC/IEEE 15288 provides the formal systems-engineering life-cycle context. This supports making the geographic, infrastructure, service, and modeling boundary explicit before cross-system claims are evaluated.

**Critical qualification:** the exact Stage-1 boundary object `Omega_sys` is thesis notation, not an ISO variable.

### S1.4 — Power and Transportation as constituent systems; Information and Organization as supporting domains

**Status: THESIS ONTOLOGY WITH LITERATURE SUPPORT, NOT A UNIVERSAL TAXONOMY.**

Critical-infrastructure and SoS literature supports treating power and transportation as autonomous infrastructure systems and recognizes cyber/information and organizational/social relationships as distinct dimensions. Eusgeld et al. explicitly analyze infrastructure together with SCADA/control systems as a SoS, while Mohebbi et al. support cyber-physical-social/organizational resilience reasoning.

The exact ontology

`S = {P,T,I,O}`

with `P,T` physical and `I,O` supporting, is therefore a defensible thesis modeling decision rather than an established four-layer standard.

**Primary sources:** [Eusgeld, Nan, & Dietz, 2011](https://doi.org/10.1016/j.ress.2010.12.010); [Mohebbi et al., 2020](https://doi.org/10.1016/j.scs.2020.102327); [Grafius, Varga, & Jude, 2020](https://doi.org/10.1061/(ASCE)IS.1943-555X.0000575).

### S1.5 — Constituent entities and layer-specific semantics

**Status: STRONG FOUNDATION.**

Multilayer theory explicitly allows different relation types and layer structures, while infrastructure models preserve domain-specific topology and flow semantics. Zhang and Peeta model individual infrastructures as distinct networks with disparate physical and operational characteristics; Fotouhi et al. use a two-layer power/traffic representation with cross-system linking variables rather than collapsing both systems into one homogeneous graph.

Thus power edges and transport edges should retain distinct meanings.

**Primary sources:** [Zhang & Peeta, 2011](https://doi.org/10.1016/j.trb.2010.10.001); [Fotouhi et al., 2017](https://doi.org/10.1016/j.ress.2017.01.026).

### S1.6 — Spatial embedding

**Status: STRONGLY SUPPORTED.**

Spatially embedded infrastructure-network studies explicitly represent geographic position and spatially constrained links. Danziger et al. model interdependent multiplex infrastructure in two-dimensional space, and Vaknin et al. show that anisotropy and spatial modularity materially affect cascading behavior. Mahabadi et al.'s review also identifies geographic/spatial network properties as important but notes widespread simplification and limited real-data use.

Therefore a mapping such as `x_i in R^2` is mathematically and engineeringly defensible for physical assets with meaningful coordinates.

**Primary sources:** [Danziger et al., arXiv:1505.01688](https://arxiv.org/abs/1505.01688) — preprint-only in this audit; [Vaknin et al., 2021](https://doi.org/10.1088/1367-2630/ac2e3c); [Mahabadi et al., 2021](https://doi.org/10.1109/ACCESS.2021.3116868).

### S1.7 — Critical correction: spatial proximity versus interdependency

**Status: ORIGINAL WORDING REQUIRES CORRECTION.**

The statement `spatial proximity != interdependency` is too absolute because the Rinaldi taxonomy includes **geographic interdependency**, in which proximate infrastructures can experience correlated state changes under the same local environmental event. Later infrastructure literature retains this interpretation.

The safer Stage-1 rule is:

`proximity alone != functional/causal dependency`

and:

`proximity + a defensible shared local hazard pathway -> geographic co-exposure/interdependency candidate`.

This also remains consistent with the canonical Stage-2 rule:

`common exposure or correlation != causal dependency`.

**Primary sources:** [Rinaldi et al., 2001](https://doi.org/10.1109/37.969131); [Ganguly & Mukherjee, 2023](https://doi.org/10.1111/mice.12999).

### S1.8 — Candidate cross-layer interaction set

**Status: MATHEMATICALLY SOUND THESIS CONSTRUCTION; NOT AN ESTABLISHED STANDARD NOTATION.**

The proposed object

`C_PT^(1) subseteq V_P x V_T`

is compatible with multilayer-network mathematics: cross-layer relations are subsets of Cartesian products of node sets. However, the notation and its interpretation as a **pre-causal candidate set** are thesis-specific.

A more explicit definition is recommended:

`C_ab^(1) = {(i,j) in V_a x V_b : Gamma_ij^struct = 1}`

where `Gamma_ij^struct` is a structural-admissibility predicate based only on documented asset mapping, interface hardware, geographic/co-exposure criteria, access geometry, or other non-causal structural evidence.

Stage 2 then applies causal qualification to this candidate set.

### S1.9 — Known relationships versus potentially qualifying relationships

**Status: HIGH-VALUE THESIS DISTINCTION, BUT TERMINOLOGY MUST AVOID PREJUDGING STAGE 2.**

Do not call a Stage-1 relation an 'accepted interdependency' merely because prior literature reports the mechanism class. Separate:

- `R_prior`: prior literature or operator documentation reports a relation/mechanism class;
- `C_struct`: structurally admissible candidate relation in the study system;
- `I_acc`: Stage-2 accepted causal dependency after provenance, mechanism, activation, validity, and uncertainty checks.

A clean relation is:

`I_acc subseteq (R_prior union C_struct)`.

For example, literature can establish that traffic signals generally require electric power, but a particular signal-to-feeder mapping in the study network still requires case-specific asset mapping and Stage-2 qualification.

### S1.10 — Graph notation and state notation

**Status: CONCEPTUALLY VALID; NOTATION NEEDS DISCIPLINE.**

The canonical framework currently writes `G=(V,E,X)` with `X={x_i}` for locations and separately uses dynamic state symbols inside `Y`. This is workable but risks confusing spatial coordinates with dynamical state vectors.

For implementation, preserve the canonical object but document the types explicitly:

- `x_i`: spatial coordinate/location of entity i;
- `Y_i`: state-variable schema/value attached to entity i;
- `Y(t)`: integrated system state at time t.

Stage 1 defines the **state schema/state space**, not the Stage-3 trajectory.

### S1.11 — Rich Stage-1 output

**Status: USEFUL IMPLEMENTATION EXTENSION; DO NOT SILENTLY REPLACE THE CANONICAL OUTPUT.**

The canonical Stage-1 output is `S, G, X, Y`. The richer tuple

`(Omega_sys, S, V, E_intra, X, Y, C_cross)`

is scientifically useful, but it should be described as the **implementation package or expanded handoff metadata**, not as a replacement for the frozen canonical output unless the canonical framework is formally amended.

A safe form is:

`Z1_impl = (S,G,X,Y ; Omega_sys, C_cross, Pi1)`

where `Pi1` stores provenance, data quality, coordinate reference system, entity typing, and topology-validation metadata.

### S1.12 — Stage-1 acceptance gate

**Status: THESIS GOVERNANCE WITH STRONG SYSTEMS-ENGINEERING SUPPORT.**

Checking boundary clarity, entity/layer semantics, interface definition, data adequacy, and avoidance of premature causal claims is consistent with systems-engineering architecture/context practice. The exact PASS/FAIL/BLOCKED gate is the thesis's scientific-control mechanism, not a published universal Stage-1 gate.

## 4. Evidence-strength summary

| Stage-1 proposition | Evidence status | Writing label |
|---|---|---|
| Explicit system context/boundary | strong systems-engineering foundation | ESTABLISHED BASIS |
| SoS architecture for interdependent infrastructure | strong peer-reviewed foundation | ESTABLISHED BASIS |
| Multilayer representation | strong mathematical foundation | ESTABLISHED BASIS |
| Layer-specific topology semantics | strong direct/general infrastructure evidence | ESTABLISHED BASIS |
| Spatial embedding | strong network/infrastructure evidence | ESTABLISHED BASIS |
| Proximity alone implies causal dependency | not supported | REJECT |
| Proximity can indicate geographic co-exposure | supported | ESTABLISHED TAXONOMIC BASIS |
| Stage 1 structure before Stage 2 causality | defensible integration rule | THESIS GOVERNANCE |
| `S={P,T,I,O}` with I/O supporting | defensible but thesis-specific | THESIS ONTOLOGY |
| `C_PT^(1)` candidate set | mathematically sound | THESIS STRUCTURAL OBJECT |
| prior-known vs structurally-candidate vs accepted-causal relation classes | not standard terminology | THESIS EVIDENCE ONTOLOGY |
| rich `Z1` handoff | useful but noncanonical extension | IMPLEMENTATION OBJECT |
| PASS/FAIL/BLOCKED Stage-1 gate | thesis-specific scientific control | THESIS GOVERNANCE |

## 5. High-confidence references for Stage 1

1. Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D
2. Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131
3. Eusgeld, I., Nan, C., & Dietz, S. (2011). System-of-systems approach for interdependent critical infrastructures. *Reliability Engineering & System Safety, 96*(6), 679–686. https://doi.org/10.1016/j.ress.2010.12.010
4. Zhang, P., & Peeta, S. (2011). A generalized modeling framework to analyze interdependencies among infrastructure systems. *Transportation Research Part B: Methodological, 45*(3), 553–579. https://doi.org/10.1016/j.trb.2010.10.001
5. De Domenico, M., et al. (2013). Mathematical formulation of multilayer networks. *Physical Review X, 3*, 041022. https://doi.org/10.1103/PhysRevX.3.041022
6. Kivelä, M., et al. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016
7. Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026
8. Grafius, D. R., Varga, L., & Jude, S. (2020). Infrastructure interdependencies: Opportunities from complexity. *Journal of Infrastructure Systems, 26*(4), 04020036. https://doi.org/10.1061/(ASCE)IS.1943-555X.0000575
9. Mahabadi, Z., Varga, L., & Dolan, T. (2021). Network properties for robust multilayer infrastructure systems: A percolation theory review. *IEEE Access, 9*, 135755–135773. https://doi.org/10.1109/ACCESS.2021.3116868
10. Vaknin, D., Bashan, A., Braunstein, L. A., Buldyrev, S. V., & Havlin, S. (2021). Cascading failures in anisotropic interdependent networks of spatial modular structures. *New Journal of Physics, 23*, 113001. https://doi.org/10.1088/1367-2630/ac2e3c
11. Ganguly, P., & Mukherjee, S. (2023). A simulation-based generalized framework to model vulnerability of interdependent critical infrastructure systems under incomplete information. *Computer-Aided Civil and Infrastructure Engineering, 38*(18), 2537–2559. https://doi.org/10.1111/mice.12999
12. ISO/IEC/IEEE 15288:2023. Systems and software engineering — System life cycle processes. https://www.iso.org/standard/81702.html

## 6. arXiv records retained for provenance/discovery

- [Kivelä et al., arXiv:1309.7233](https://arxiv.org/abs/1309.7233) — journal version verified; do not count separately.
- [De Domenico et al., arXiv:1307.4977](https://arxiv.org/abs/1307.4977) — journal version verified; do not count separately.
- [Mahabadi et al., arXiv:2105.12701](https://arxiv.org/abs/2105.12701) — journal version verified; do not count separately.
- [Danziger et al., arXiv:1505.01688](https://arxiv.org/abs/1505.01688) — preprint-only in this audit; discovery/support only.
- [Vaknin et al., arXiv:2106.14084](https://arxiv.org/abs/2106.14084) — journal version verified; do not count separately.

## 7. Revised Stage-1 critical formulation

The most defensible Stage-1 statement is:

> Stage 1 constructs and verifies the bounded, typed, spatially embedded multilayer architecture and identifies structurally admissible cross-layer relation candidates. It may record prior evidence that a relation class is known in the literature, but it does not promote a study-specific relation to an accepted causal dependency. Stage 2 performs that causal qualification.

The key guardrail should be written as:

`structural compatibility or proximity != functional/causal dependency`

while geographic co-exposure is retained separately as a recognized infrastructure relation class.

This formulation preserves RQ1, strengthens the Stage-1/Stage-2 boundary, and avoids contradicting the established geographic-interdependency literature.