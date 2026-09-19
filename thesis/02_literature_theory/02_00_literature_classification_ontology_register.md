# Chapter 2 Literature Classification and Ontology Register — v1.0

**Status:** ACTIVE / CONTROLLED EVIDENCE REGISTER  
**Date:** 2026-09-18  
**Chapter:** 2 — Literature Review and Theoretical Foundations  
**Scientific contract:** frozen Chapter I  
**RQ–SO–H authority:** project/CANONICAL_RQ_SO_HYPOTHESES_V3.md  
**Framework authority:** project/CANONICAL_7_STAGE_FRAMEWORK_V2.md

## 1. Purpose

This register controls how literature enters Chapter 2. It prevents author-by-author accumulation by requiring every source to be classified by evidence type, system role, network representation, dependency direction, mechanism, dynamic character, model family, information/organization role, resilience construct, uncertainty treatment, intervention type, sustainability consequence, validation maturity, and thesis traceability.

The governing review grammar is:

$Concept → Evidence → Mechanism → Method → Assumptions → Validation → Limitations → Thesis\ Need.$

No single established ontology covers the complete thesis domain. Infrastructure dependency classifications remain fragmented and sometimes lose directionality, while multilayer-network science provides a stronger mathematical vocabulary but does not by itself encode physical mechanism, organizational feasibility, resilience semantics, or sustainability consequences ([Dasuni et al., 2024](https://doi.org/10.1080/23789689.2024.2403885); [Kivelä et al., 2014](https://doi.org/10.1093/comnet/cnu016); [Ouyang, 2014](https://doi.org/10.1016/j.ress.2013.06.040)).

## 2. Controlled composite ontology

The literature object is classified by:

$\mathfrak O_{lit}=(E,S,N,R,D,M,\Tau,F,K,Q,U,A,J,V,T)$

| Code | Axis | Meaning |
|---|---|---|
| E | Evidence class | provenance and publication status |
| S | System/SoS role | constituent system, supporting domain, organization, service |
| N | Network representation | monoplex, multilayer, multiplex, network-of-networks, temporal |
| R | Dependency class | physical, cyber/information, geographic, logical, social/organizational |
| D | Direction | source→target, target→source, reciprocal, indirect |
| M | Mechanism | physically or operationally interpretable dependency mechanism |
| Tau | Dynamic character | static, steady-state, discrete/continuous dynamic, event-driven, hybrid, stochastic, multiscale |
| F | Model family | empirical, network, physics, ABM, system dynamics, optimization, probabilistic, data-driven, hybrid |
| K | Knowledge/action | observation, communication, estimation, authority, coordination, resources, feasible control |
| Q | Resilience object | performance, recovery, robustness, viability, reachability, confidence/probability |
| U | Uncertainty | aleatory, epistemic, deep uncertainty and source |
| A | Intervention | hardening, repair, reconfiguration, DER, V2G, charging, information, organization, pricing |
| J | Sustainability consequence | cost, energy, GHG, accessibility, equity, material, water, service |
| V | Validation maturity | conceptual through field/operational validation |
| T | Thesis traceability | Chapter-2 section, gap, RQ, SO, H |

## 3. Controlled evidence labels

| Label | Definition |
|---|---|
| [STD] | standard or formal engineering guidance |
| [FND] | foundational theory / seminal paper |
| [SR] | systematic review |
| [CR] | critical or comprehensive review |
| [DIR-PT] | direct Power–Transportation evidence |
| [DIR-CI] | direct interdependent-critical-infrastructure evidence |
| [ADJ] | adjacent transferable evidence; not direct P–T evidence |
| [MATH] | mathematical/control-theory foundation |
| [EMP] | empirical observational evidence |
| [SIM] | simulation/computational evidence |
| [ARX-P] | arXiv preprint only; not counted as peer-reviewed evidence |
| [ARX-J] | arXiv version tied to a verified/accepted journal paper; count once |

**Rule:** arXiv is a dissemination source, not an independent evidence-quality category. A preprint and its journal version are one scientific source, not two.

## 4. System, network, dependency, and direction codes

For the thesis:

- S1:P = Power, constituent physical infrastructure.
- S1:T = Transportation, constituent physical infrastructure.
- S2:I = Information, supporting domain.
- S2:O = Organization, supporting domain.
- S3:PT = coupled Power–Transportation System of Systems.

Maier's SoS formulation supports the architectural distinction between constituent systems and a larger SoS, but it does not prescribe one universal infrastructure coupling model ([Maier, 1998](https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D)).

Network labels:

- N0 monoplex
- N1 multilayer
- N2 multiplex
- N3 network of networks
- N4 interdependent network
- N5 temporal network
- N6 spatial network
- N7 multilayer-temporal
- N8 supra-adjacency
- N9 tensorial multilayer representation

Kivelä et al. (2014) provide a general multilayer-network framework and terminology dictionary, while De Domenico et al. (2013) provide a tensorial mathematical representation ([Kivelä et al., 2014](https://doi.org/10.1093/comnet/cnu016); [De Domenico et al., 2013](https://doi.org/10.1103/PhysRevX.3.041022)).

$multilayer\ representation \neq causal\ interdependency\ model.$

Dependency labels:

- R-PHY physical
- R-CYB cyber/informational
- R-GEO geographic/spatial
- R-LOG logical/rule-mediated
- R-SOC social/organizational

Direction labels:

- D-ST source→target
- D-TS target→source
- D-BI reciprocal
- D-IND indirect/mediated
- D-P2T Power→Transportation
- D-T2P Transportation→Power

Rinaldi et al. (2001) remain a foundational source for infrastructure-interdependency dimensions, while Dasuni et al. (2024) show systematically that dependency/interdependency classifications remain fragmented and that dependency direction is often obscured ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131); [Dasuni et al., 2024](https://doi.org/10.1080/23789689.2024.2403885)).

$connection \neq directional\ dependency \neq reciprocal\ interdependency.$

## 5. Mechanism and dynamic codes

Every accepted cross-system relation must identify a source, receiver, mechanism, trigger/activation condition, effect, timing/delay where relevant, evidence source, and validity boundary.

Controlled P–T mechanism labels include:

- M-ENERGY-SUPPLY
- M-EV-CHARGE-LOAD
- M-V2G
- M-SIGNAL-POWER
- M-CHARGER-AVAILABILITY
- M-TRAFFIC-ACCESS
- M-REPAIR-ACCESS
- M-MOBILE-ENERGY
- M-PRICE-RESPONSE
- M-INFORMATION
- M-COMMUNICATION
- M-AUTHORITY
- M-RESOURCE

Direct P–T studies support explicit traffic–power linking, signal/power dependencies, stochastic disruption, mitigation/repair decisions, and dynamic traffic assignment ([Fotouhi et al., 2017](https://doi.org/10.1016/j.ress.2017.01.026); [Zou & Chen, 2019](https://doi.org/10.1016/j.ress.2019.106557)). EV-focused reviews identify charging/discharging, navigation, charging-station planning, user behavior, pricing, V2G, DER/mobile-energy coordination, and uncertainty as major P–T coupling mechanisms ([Hu et al., 2024](https://doi.org/10.3390/en17194775); [Oladigbolu et al., 2025](https://doi.org/10.1016/j.est.2025.118419)).

Dynamic labels:

- T0 static
- T1 steady-state
- T2 quasi-static
- T3 discrete-time dynamic
- T4 continuous-time dynamic
- T5 event-driven
- T6 hybrid continuous/discrete
- T7 stochastic dynamic
- T8 temporal network
- T9 multiscale

Ouyang (2014) shows that interdependent-infrastructure analysis spans multiple model families, while Zou and Chen (2019) explicitly adopt dynamic rather than static traffic assignment for disrupted traffic–power systems ([Ouyang, 2014](https://doi.org/10.1016/j.ress.2013.06.040); [Zou & Chen, 2019](https://doi.org/10.1016/j.ress.2019.106557)).

$greater\ complexity \not\Rightarrow greater\ explanatory\ or\ predictive\ value.$

That incremental value remains H1.

## 6. Model-family codes

- F-EMP empirical
- F-ABM agent-based
- F-SD system dynamics
- F-ECO economic/input-output
- F-NET network-based
- F-PHY physics-based
- F-OPT mathematical optimization
- F-PROB probabilistic/Bayesian
- F-ML data-driven/machine learning
- F-HYB hybrid/co-simulation

Ouyang (2014) is the principal broad classification source for empirical, agent-based, system-dynamics, economic, network and other interdependent-infrastructure modeling approaches ([Ouyang, 2014](https://doi.org/10.1016/j.ress.2013.06.040)).

## 7. Information, organization, and feasible-action codes

- K-OBS observation/sensing
- K-COM communication
- K-EST state estimation
- K-INF information availability
- K-SA situation awareness
- K-AUT authority
- K-COO coordination
- K-RES personnel/resources
- K-ACC physical access
- K-DEC decision rule
- K-CTRL feasible control

Cyber-physical-social infrastructure research supports physical, cyber, and social/organizational interdependencies and identifies design, operational, and managerial strategies as distinct resilience contributors ([Mohebbi et al., 2020](https://doi.org/10.1016/j.scs.2020.102327)). Integrated state-estimation research in adjacent water–energy systems shows that cross-system measurements can change estimation and bad-data detection, but this is coded [ADJ] rather than direct P–T evidence ([Moazeni et al., 2020](https://doi.org/10.1016/j.jhydrol.2020.125393)). Ganguly and Mukherjee (2023) explicitly model incomplete topology/flow information and time-dependent vulnerability under physical, spatial, and informational uncertainty ([Ganguly & Mukherjee, 2023](https://doi.org/10.1111/mice.12999)).

## 8. Resilience, viability, reachability, and uncertainty codes

Resilience labels:

- Q-ROB robustness
- Q-RED redundancy
- Q-RESO resourcefulness
- Q-RAP rapidity
- Q-PERF performance trajectory
- Q-REC recovery/restoration
- Q-VIA viability
- Q-REA reachability
- Q-RAV reach-avoid
- Q-ADP adaptation
- Q-CONF confidence/probability

Bruneau et al. (2003) establish the robustness–redundancy–resourcefulness–rapidity framework across technical, organizational, social, and economic dimensions ([Bruneau et al., 2003](https://doi.org/10.1193/1.1623497)). Poulin and Kane (2021) show from a 273-publication critical review that resilience-curve interpretation depends on the selected performance measure, target, milestones, and summary metric ([Poulin & Kane, 2021](https://doi.org/10.1016/j.ress.2021.107926)).

$performance\ trajectory \neq viability\ set \neq reachable\ set.$

Viability/reachability sublabels:

- Q-VIA-D deterministic viability
- Q-VIA-S stochastic viability
- Q-REA-T target reachability
- Q-REA-TT target-tube reachability
- Q-RAV reach-avoid
- Q-ROB-R robust reachability

Doyen and De Lara (2010) define stochastic viability kernels and viable feedbacks for uncertain constrained nonlinear systems using chance constraints and dynamic programming ([Doyen & De Lara, 2010](https://doi.org/10.1016/j.sysconle.2010.07.008)). Vinod and Oishi's target-tube formulation contains stochastic viability and terminal reach-avoid as special cases; the arXiv record reports acceptance in Automatica, so it is coded [ARX-J] and counted once ([Vinod & Oishi, arXiv v3](https://arxiv.org/abs/1810.05217)).

Uncertainty labels:

- U-ALE aleatory/stochastic
- U-EPI epistemic/knowledge
- U-DU deep uncertainty
- U-H hazard
- U-I interdependency
- U-M model form
- U-P parameter
- U-O observation
- U-A intervention/resource
- U-S sustainability accounting

Infrastructure DMDU literature supports robust and adaptive approaches when a single predictive future is not defensible, while also showing that organizational and institutional contexts are often incompletely represented ([Bonjean Stanton & Roelich, 2021](https://doi.org/10.1016/j.techfore.2021.120939)). Dynamic Adaptive Policy Pathways is therefore retained only as a conditional Stage-7 extension ([Haasnoot et al., 2013](https://doi.org/10.1016/j.gloenvcha.2012.12.006)).

## 9. Intervention and sustainability codes

Intervention labels:

- A-HARD hardening
- A-RED redundancy
- A-REP repair/restoration
- A-REC reconfiguration
- A-DER distributed energy resource
- A-MER mobile energy resource
- A-V2G vehicle-to-grid
- A-CHG charging control
- A-CS charging-station siting/capacity
- A-EXP network expansion
- A-INFO sensing/information improvement
- A-ORG organizational/coordination change
- A-PRICE pricing/incentive

Sustainability consequence labels:

- J-COST
- J-ENERGY
- J-GHG
- J-ACCESS
- J-EQUITY
- J-MATERIAL
- J-WATER
- J-LCA
- J-SERVICE

Every consequence must declare an accounting boundary: operational, partial life cycle, or full life cycle.

Integrated resilience–sustainability reviews show that sustainability assessment often emphasizes life-cycle, carbon, energy, and economic indicators while social dimensions are less consistently operationalized ([Salgado et al., 2025](https://doi.org/10.1080/23789689.2025.2471119); [Kumar & Hashem Mehany, 2026](https://doi.org/10.1007/s43621-026-02973-9)). Faber et al. frame resilience and sustainability as related but distinct infrastructure decision-analysis dimensions ([Faber et al., 2020](https://doi.org/10.1080/23789689.2017.1417348)).

$effectiveness \neq resource\ efficiency \neq sustainability\ consequence.$

## 10. Validation-maturity codes

- V0 conceptual only
- V1 analytical/theoretical proof
- V2 toy numerical example
- V3 synthetic benchmark
- V4 calibrated synthetic/semi-synthetic
- V5 empirical historical data
- V6 real-network case study
- V7 cross-case/external validation
- V8 field/pilot/operational demonstration

$model\ exists \not\Rightarrow model\ is\ empirically\ validated.$

## 11. Verified core article register

The following sources are the verified core references used in the current Chapter-2 ontology and synthesis. This is not yet the completed systematic-review corpus.

| ID | Source | Evidence class | Primary use | Directness | Thesis traceability |
|---|---|---|---|---|---|
| LIT-001 | [Maier (1998)](https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D) | [FND] | SoS architecture | foundational | 2.2; RQ1 |
| LIT-002 | [Rinaldi, Peerenboom, & Kelly (2001)](https://doi.org/10.1109/37.969131) | [FND][DIR-CI] | dependency/interdependency dimensions | CI-general | 2.2; RQ1–RQ2 |
| LIT-003 | [Bruneau et al. (2003)](https://doi.org/10.1193/1.1623497) | [FND] | resilience dimensions, organization | infrastructure/community | 2.4, 2.7 |
| LIT-004 | [Doyen & De Lara (2010)](https://doi.org/10.1016/j.sysconle.2010.07.008) | [MATH] | stochastic viability | mathematical | 2.7; H3 |
| LIT-005 | [De Domenico et al. (2013)](https://doi.org/10.1103/PhysRevX.3.041022) | [FND][MATH] | tensorial multilayer networks | generic networks | 2.2; RQ1 |
| LIT-006 | [Haasnoot et al. (2013)](https://doi.org/10.1016/j.gloenvcha.2012.12.006) | [FND][ADJ] | adaptive pathways under deep uncertainty | adjacent planning | 2.8; conditional Stage 7 |
| LIT-007 | [Ouyang (2014)](https://doi.org/10.1016/j.ress.2013.06.040) | [CR][DIR-CI] | infrastructure model-family taxonomy | CI-general | 2.2, 2.5 |
| LIT-008 | [Kivelä et al. (2014)](https://doi.org/10.1093/comnet/cnu016) | [FND][CR][MATH] | multilayer-network terminology | generic networks | 2.2; RQ1 |
| LIT-009 | [Fotouhi, Moryadee, & Miller-Hooks (2017)](https://doi.org/10.1016/j.ress.2017.01.026) | [DIR-PT][SIM] | explicit traffic–power coupling, resilience | direct P–T | 2.3, 2.5; H1 |
| LIT-010 | [Faber, Miraglia, Qin, & Stewart (2020)](https://doi.org/10.1080/23789689.2017.1417348) | [FND][ADJ] | resilience–sustainability decision analysis | infrastructure-general | 2.8; H4–H5 |
| LIT-011 | [Zou & Chen (2019)](https://doi.org/10.1016/j.ress.2019.106557) | [DIR-PT][SIM] | DTA, mitigation/repair decision | direct P–T | 2.3, 2.5, 2.8; H1/H4 |
| LIT-012 | [Moazeni, Khazaei, & Mitra (2020)](https://doi.org/10.1016/j.jhydrol.2020.125393) | [ADJ][SIM] | integrated state estimation | water–energy adjacent | 2.6; H2 support only |
| LIT-013 | [Mohebbi et al. (2020)](https://doi.org/10.1016/j.scs.2020.102327) | [SR][DIR-CI] | cyber-physical-social/organizational resilience | CI-general | 2.4; H2 |
| LIT-014 | [Poulin & Kane (2021)](https://doi.org/10.1016/j.ress.2021.107926) | [CR][ARX-J] | resilience-curve taxonomy | infrastructure-general | 2.7; H3 comparator |
| LIT-015 | [Bonjean Stanton & Roelich (2021)](https://doi.org/10.1016/j.techfore.2021.120939) | [SR][ADJ] | DMDU, robust/adaptive decisions | infrastructure-general | 2.8; H5 |
| LIT-016 | [Ganguly & Mukherjee (2023)](https://doi.org/10.1111/mice.12999) | [DIR-CI][SIM] | incomplete information; hybrid/Bayesian dynamics | CI-general | 2.4–2.6; H1/H2 |
| LIT-017 | [Dasuni et al. (2024)](https://doi.org/10.1080/23789689.2024.2403885) | [SR][DIR-CI] | dependency classification/directionality | CI-general | 2.2; RQ2 |
| LIT-018 | [Wang, Zhao, & Zhang (2024)](https://doi.org/10.1016/j.ress.2024.110300) | [SR][DIR-CI] | multiplex CI resilience, data/UQ gaps | CI-general | 2.2, 2.5, 2.7 |
| LIT-019 | [Hu, Wang, & Tan (2024)](https://doi.org/10.3390/en17194775) | [CR][DIR-PT] | EV coupling mechanisms | direct P–T | 2.3; H1/H4 |
| LIT-020 | [Salgado, Günther, & Mechtcherine (2025)](https://doi.org/10.1080/23789689.2025.2471119) | [SR][ADJ] | integrated resilience–sustainability assessment | adjacent civil infrastructure | 2.8; H4/H5 |
| LIT-021 | [Oladigbolu et al. (2025)](https://doi.org/10.1016/j.est.2025.118419) | [CR][DIR-PT] | coupled P–T planning/operation, EV/DER/mobile energy | direct P–T | 2.3, 2.8; H1/H4 |
| LIT-022 | [Kumar & Hashem Mehany (2026)](https://doi.org/10.1007/s43621-026-02973-9) | [CR][ADJ] | infrastructure sustainability/resilience definitions | infrastructure-general | 2.8 |
| LIT-023 | [Vinod & Oishi (2021)](https://doi.org/10.1016/j.automatica.2020.109458) | [MATH][ARX-J] | stochastic target-tube reachability; viability/reach-avoid relation | mathematical | 2.7; H3 |
| LIT-024 | [Qian et al. (2025)](https://doi.org/10.1109/TSG.2025.3560976) | [DIR-PT][SIM][ARX-J] | microscopic P–T/V2G co-simulation; spatiotemporal EV charging load; charging-station fault sensing | direct P–T | 2.3, 2.5, 2.6; H1/H2 |
| LIT-025 | [Li et al. (2024)](https://doi.org/10.17775/CSEEJPES.2022.04810) | [DIR-PT][SIM][ARX-J] | dynamic traffic assignment, EV queuing, voltage-quality feedback, uncertain travel demand | direct P–T | 2.3, 2.5; H1 |
| LIT-026 | [Wang et al. (2022)](https://doi.org/10.1111/mice.12736) | [DIR-PT][SIM] | dynamic traffic assignment under stochastic charging-station failure/recovery | direct P–T | 2.3, 2.5, 2.7; H1/H3 |
| LIT-027 | [Zhu et al. (2021)](https://doi.org/10.1155/2021/5599073) | [DIR-PT][SIM] | power-outage → traffic-signal loss → transportation-capacity degradation/cascade | direct P→T | 2.3, 2.5; H1 |

## 12. arXiv discovery lane

These records inform discovery but are not promoted to peer-reviewed evidence unless a journal publication is independently verified.

| ID | Preprint | Label | Relevance | Status |
|---|---|---|---|---|
| ARX-001 | [Qiu, Thompson, Youcef-Toumi, & Farid (2025)](https://arxiv.org/abs/2510.10914) | [ARX-P][DIR-PT] | dynamic multimodal P–T coordination, charging, queuing, V2G | discovery only |
| ARX-002 | [Qian, Fang, Hu, Shao, & Zheng (2024 arXiv; 2025 journal)](https://arxiv.org/abs/2412.09808) | [ARX-J][DIR-PT] | open preprint of LIT-024; microscopic P–T/V2G co-simulation | do not count separately |
| ARX-003 | [Ghose, Sivaranjani, & Qin (2025)](https://arxiv.org/abs/2511.00941) | [ARX-P][DIR-PT] | traffic-aware dynamic wireless charging and grid planning | discovery only |
| ARX-004 | [Poulin & Kane (2021)](https://arxiv.org/abs/2102.01009) | [ARX-J] | open version of LIT-014 | do not count separately |
| ARX-005 | [Vinod & Oishi](https://arxiv.org/abs/1810.05217) | [ARX-J] | open/accepted version of LIT-023 | do not count separately |

## 13. Evidence-admission rules

1. **Directness:** for P–T-specific claims, [DIR-PT] has higher transferability than [DIR-CI], which has higher transferability than [ADJ]. This is a transferability hierarchy, not a journal-quality ranking.
2. **Causality:** a graph link is not a causal coupling law unless a source/receiver/mechanism/effect chain and validity conditions are supported.
3. **Validation:** conceptual model, verified implementation, and validated representation are distinct.
4. **Novelty:** literature silence is not proof of novelty.
5. **Hypothesis non-prejudgment:** literature may justify H1–H5 but cannot be written as if it already proves them.

In particular, the present literature does not establish:

$M_2>M_1,$

$(P+T+I+O)>(P+T),$

$R_{curve}+\mathfrak R_T>R_{curve},$

or

$\mathcal A_R^\star \neq \mathcal A_{R,S}^\star.$

These remain thesis tests.

## 14. Section-level routing

| Section | Core ontology axes | Primary evidence IDs |
|---|---|---|
| 2.1 Review Method and Evidence Scope | E, V, T | protocol + full corpus |
| 2.2 Interdependent Infrastructure Systems and Multilayer SoS | S, N, R, D | 001, 002, 005, 007, 008, 017, 018 |
| 2.3 Coupled Power–Transportation Systems | S, D, M, Tau, F | 009, 011, 019, 021; ARX-001–003 discovery only |
| 2.4 Information and Organizational Dependencies | R, K, U | 003, 012, 013, 016 |
| 2.5 Cascading, Hybrid, and Spatiotemporal Dynamics | M, Tau, F, U | 007, 009, 011, 016, 018 |
| 2.6 Observation, State Estimation, and Control | K, F, U | 012, 013, 016 |
| 2.7 Resilience, Viability, Reachability, and Uncertainty | Q, U, V | 003, 004, 014, 018, 023 |
| 2.8 Intervention, Sustainability, and Engineering Decision | A, J, U, V | 006, 010, 011, 015, 019, 020, 021, 022 |
| 2.9 Critical Synthesis and Research Gap | all | synthesis of qualified corpus |

## 15. Minimum extraction row for every future paper

Every paper entering the final corpus must record: immutable paper ID; verified author–year citation; DOI or persistent URL; publication status; evidence class; system domain; network representation; dependency class; direction; mechanism; activation condition; dynamic character; model family; information/organization role; resilience construct; uncertainty; intervention; sustainability consequence and accounting boundary; data source/geography/period; validation maturity; supporting evidence; contrary/rival evidence; assumptions; limitations; transferability; Chapter-2 section; RQ/SO/H traceability; and admission status PASS / CONDITIONAL / BLOCKED / EXCLUDE.

## 16. Verified references used in this register

Bonjean Stanton, M. C., & Roelich, K. (2021). Decision making under deep uncertainties: A review of the applicability of methods in practice. *Technological Forecasting and Social Change, 171*, 120939. https://doi.org/10.1016/j.techfore.2021.120939

Bruneau, M., Chang, S. E., Eguchi, R. T., Lee, G. C., O'Rourke, T. D., Reinhorn, A. M., Shinozuka, M., Tierney, K., Wallace, W. A., & von Winterfeldt, D. (2003). A framework to quantitatively assess and enhance the seismic resilience of communities. *Earthquake Spectra, 19*(4), 733–752. https://doi.org/10.1193/1.1623497

Dasuni, K. A. L., Palliyaguru, R., Amaratunga, D., & Liyanawatta, T. N. (2024). Redefining ‘dependencies/interdependencies’ of critical infrastructure: A systematic review of the existing knowledgebase. *Sustainable and Resilient Infrastructure, 10*(2), 202–222. https://doi.org/10.1080/23789689.2024.2403885

De Domenico, M., Solé-Ribalta, A., Cozzo, E., Kivelä, M., Moreno, Y., Porter, M. A., Gómez, S., & Arenas, A. (2013). Mathematical formulation of multilayer networks. *Physical Review X, 3*, 041022. https://doi.org/10.1103/PhysRevX.3.041022

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Faber, M. H., Miraglia, S., Qin, J., & Stewart, M. G. (2020). Bridging resilience and sustainability—Decision analysis for design and management of infrastructure systems. *Sustainable and Resilient Infrastructure, 5*(1–2), 102–124. https://doi.org/10.1080/23789689.2017.1417348

Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026

Ganguly, P., & Mukherjee, S. (2023). A simulation-based generalized framework to model vulnerability of interdependent critical infrastructure systems under incomplete information. *Computer-Aided Civil and Infrastructure Engineering, 38*(18), 2537–2559. https://doi.org/10.1111/mice.12999

Haasnoot, M., Kwakkel, J. H., Walker, W. E., & ter Maat, J. (2013). Dynamic adaptive policy pathways: A new method for crafting robust decisions for a deeply uncertain world. *Global Environmental Change, 23*(2), 485–498. https://doi.org/10.1016/j.gloenvcha.2012.12.006

Hu, J., Wang, X., & Tan, S. (2024). Electric vehicle integration in coupled power distribution and transportation networks: A review. *Energies, 17*(19), 4775. https://doi.org/10.3390/en17194775

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016

Kumar, S., & Hashem Mehany, M. (2026). A comprehensive review of infrastructure sustainability and resilience. *Discover Sustainability, 7*, 903. https://doi.org/10.1007/s43621-026-02973-9

Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D

Moazeni, F., Khazaei, J., & Mitra, P. (2020). An integrated state-estimation framework for interdependent water and energy systems. *Journal of Hydrology, 590*, 125393. https://doi.org/10.1016/j.jhydrol.2020.125393

Mohebbi, S., Zhang, Q., Wells, E. C., Zhao, T., Nguyen, H., Li, M., Abdel-Mottaleb, N., Uddin, S., Lu, Q., Wakhungu, M. J., Wu, Z., Zhang, Y., Tuladhar, A., & Ou, X. (2020). Cyber-physical-social interdependencies and organizational resilience: A review of water, transportation, and cyber infrastructure systems and processes. *Sustainable Cities and Society, 62*, 102327. https://doi.org/10.1016/j.scs.2020.102327

Oladigbolu, J., Bakare, M. S., Ghanbari Motlagh, S., Mujeeb, A., & Li, L. (2025). A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources. *Journal of Energy Storage, 135*, 118419. https://doi.org/10.1016/j.est.2025.118419

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131

Salgado, I. de P., Günther, E., & Mechtcherine, V. (2025). Integrated sustainability and resilience assessments of concrete infrastructures subjected to hazards: A systematic literature review. *Sustainable and Resilient Infrastructure, 10*(5), 450–471. https://doi.org/10.1080/23789689.2025.2471119

Wang, Y., Zhao, O., & Zhang, L. (2024). Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review. *Reliability Engineering & System Safety, 250*, 110300. https://doi.org/10.1016/j.ress.2024.110300

Zou, Q., & Chen, S. (2019). Enhancing resilience of interdependent traffic-electric power system. *Reliability Engineering & System Safety, 191*, 106557. https://doi.org/10.1016/j.ress.2019.106557

Qian, T., Fang, M., Hu, Q., Shao, C., & Zheng, J. (2025). V2Sim: An open-source microscopic V2G simulation platform in urban power and transportation network. *IEEE Transactions on Smart Grid, 16*(4), 3167–3178. https://doi.org/10.1109/TSG.2025.3560976

Li, J., Xu, X., Yan, Z., Wang, H., & Chen, Y. (2024). Dynamic flow equilibrium of transportation and power distribution networks considering flexible traveling choices and voltage quality improvement. *CSEE Journal of Power and Energy Systems*. https://doi.org/10.17775/CSEEJPES.2022.04810

Wang, H., Abdin, A. F., Fang, Y.-P., & Zio, E. (2022). Resilience assessment of electrified road networks subject to charging station failures. *Computer-Aided Civil and Infrastructure Engineering, 37*(3), 300–316. https://doi.org/10.1111/mice.12736

Zhu, Y., Ozbay, K., Yang, H., Zuo, F., Sha, D., & Ghosh, I. (2021). Modeling and simulation of cascading failures in transportation systems during hurricane evacuations. *Journal of Advanced Transportation, 2021*, 5599073. https://doi.org/10.1155/2021/5599073

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

### arXiv discovery references

Ghose, D., Sivaranjani, S., & Qin, J. (2025). *Traffic-aware grid planning for dynamic wireless electric vehicle charging* [Preprint]. arXiv. https://arxiv.org/abs/2511.00941

Qian, T., Fang, M., Hu, Q., Shao, C., & Zheng, J. (2024). *V2Sim: An open-source microscopic V2G simulation platform in urban power and transportation network* [Preprint]. arXiv. https://arxiv.org/abs/2412.09808

Qiu, J., Thompson, D., Youcef-Toumi, K., & Farid, A. M. (2025). *Optimal multi-modal transportation and electric power flow: The value of coordinated dynamic operation* [Preprint]. arXiv. https://arxiv.org/abs/2510.10914

Vinod, A. P., & Oishi, M. M. K. (2020). *Stochastic reachability of a target tube: Theory and computation* (arXiv:1810.05217, v3; arXiv record reports acceptance in *Automatica*). https://arxiv.org/abs/1810.05217

## 17. Current evidence boundary

The current verified literature establishes the scientific legitimacy of the thesis components: SoS architecture, critical-infrastructure dependencies, multilayer representations, direct P–T coupling, dynamic traffic/power interaction, information/organizational dependence, resilience curves, stochastic viability/reachability mathematics, resilience–sustainability consequence analysis, and robust/adaptive decision methods.

It does not establish H1–H5 outcomes. The defensible current research boundary is:

$established\ components + fragmented\ handoffs → integration/validation\ research\ need.$

This register remains ACTIVE until the de novo database searches, screening, extraction, contrary-evidence retention, and reference-verification gates close.

## Hall–Ibáñez controlled ontology addendum — 2026-09-19

Two accepted sources add controlled distinctions that are now mandatory in Chapter-2 synthesis:

### Service-centered SoS distinction

```math
\boxed{
\text{asset topology}
\neq
\text{infrastructure service}
\neq
\text{resilience}.
}
```

Hall et al. (2016) are coded [FND]/[DIR-CI] for service-centered infrastructure and system-of-systems reasoning. They do not validate a specific P–T coupling law.

### Energy–transport interaction role

For accepted P–T literature, add derived interaction-role metadata

```math
\kappa_e^{role}
\in
\{\mathrm{OPERATION},\mathrm{RECOVERY},\mathrm{PLANNING}\}.
```

Ibáñez et al. (2010) are coded [DIR-PT]/[FND]/[SIM] and support explicit operational and investment/planning coupling between separate energy and transportation networks.

### Transport representation detail

Where relevant, distinguish

```math
T=(G_T,F_T,D_T,C_T)
```

as conceptual categories for transport infrastructure, fleet/agents, mobility demand, and control. This does not force every study into the same state vector.

### Effect class

An interdependency consequence need not be binary failure. Literature coding may distinguish:

```text
capacity | flow | demand | delay | accessibility | service | recovery | cost | other
```

with multiple classes allowed.

### Novelty boundary

Neither P–T interdependence, separate-but-coupled energy/transport networks, nor SoS framing may be claimed as thesis novelty. Novelty assessment must target the specific integrated method/result and remain evidence-gated.


## 17. P1.11.6 later-source classification reconciliation

Additional controlled evidence labels:

| Label | Definition |
|---|---|
| [BOOK-CH] | identified edited-book chapter |
| [TR] | technical/research-center report |
| [PREPRINT] | non-peer-reviewed preprint outside the arXiv-specific labels |
| [CONCEPT] | conceptual framework/evidence; no case validation implied |
| [SUPPLIED-MANUSCRIPT] | exact supplied source bytes are pinned, but publication venue/year may remain unresolved |
| [METHOD] | method/information-architecture precedent |

| ID | E | S / R / D | Tau / F / K / J | Validation maturity | Controlled thesis interpretation |
|---|---|---|---|---|---|
| A-033 Pant Ch.12 | [BOOK-CH][DIR-CI] | spatial CI SoS; physical/geographic dependencies; directional cascades | spatial-risk/network method; service disruption; risk | published chapter / source method | common cause != cascade; graph path != functional pathway; C^V remains thesis-derived |
| A-034 Barr Ch.13 | [BOOK-CH][DIR-CI][METHOD] | hierarchical SoS + horizontal relations | database/orchestration; spatial-temporal data; visualization | published chapter / implemented NISMOD-DB precedent | information architecture != physical coupling/validation |
| A-035 NEXTRANS | [TR][DIR-PT][CONCEPT] | T–Energy policy/economic/operator channels | equilibrium/CGE; operator/budget/market context | conceptual framework; report states no computational experiments | downstream context by default; Y* != Y(t) |
| A-036 Acosta-Sequeda | [PREPRINT][DIR-PT][EMP] | cross-system observational relation, not physical dependency | data-driven forecasting; Stage-4 observation/estimation | empirical preprint | rightsquigarrow != causal arrow; mode/geography validity retained |
| A-037 Kays–Sadri | [SUPPLIED-MANUSCRIPT][ADJ][CONCEPT] | transportation sustainability/resilience conceptual overlap | indicators/trade-offs; J conceptual | conceptual; calibration/validation requested by source | supports multidimensionality/trade-offs, not thesis-specific sustainability equations |

For all five sources:

~~~math
\boxed{
REPO\_CONSISTENCY
\neq
SOURCE\_SUPPORT
\neq
CASE\_VALIDATION.
}
~~~


## 18. P1.11.7 computational-method classification

Additional evidence label:

| Label | Definition |
|---|---|
| [ML] | machine-learning/data-driven analytical method; predictive/diagnostic status does not imply causal identification |

| ID | E | S / R / D | Tau / F / K / Q / J | Validation maturity | Controlled thesis interpretation |
|---|---|---|---|---|---|
| A-038 Li & Mostafavi (2025) | [ADJ][EMP][METHOD][ML] | coupled human–infrastructure post-event assessment; not P–T mechanism evidence | observational big data; feature engineering; PCA; clustering; recovery duration; risk/resilience diagnostics | peer-reviewed empirical case in Harris County/Hurricane Harvey | supports typed observational/diagnostic computation; does not replace Stage-3 physics, formal Stage-5 resilience, sustainability admission or causal intervention evaluation |

Permanent:

~~~math
\boxed{
\text{statistical pattern}
\neq
\text{physical mechanism}
\neq
\text{formal resilience guarantee}.
}
~~~
