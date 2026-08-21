# Literature Anchors from the Uploaded 207-Paper Corpus

This file records chain-specific anchors drawn from `High_Rigor_Thesis_Paper_Corpus_207.csv` supplied in the session. The title/year/DOI/relevance/evidence fields are corpus metadata; detailed paper claims still require full-text verification before final thesis use.

## Chain I — Physical system / mathematical physics

| Paper ID | Title | Year | DOI | Corpus role |
|---|---|---:|---|---|
| `P_758de5df9157` | Identifying, understanding, and analyzing critical infrastructure interdependencies | 2001 | `10.1109/37.969131` | STRONG_APPLIED; Evidence A |
| `P_8807d9b8c8c2` | Review on modeling and simulation of interdependent critical infrastructure systems | 2014 | `10.1016/j.ress.2013.06.040` | CORE; H2/H3; Evidence A |
| `P_3167cf61f309` | Catastrophic cascade of failures in interdependent networks | 2010 | `10.1038/nature08932` | STRONG_APPLIED; H3; Evidence A |
| `WEB_9ee41da52abe` | Dynamically induced cascading failures in power grids | 2018 | `10.1038/s41467-018-04287-5` | STRONG_APPLIED; H2; Evidence A/B |
| `P_6f7647563d62` | The structure and dynamics of multilayer networks | — | — | FOUNDATION; H2/H3; Evidence A |

**Use:** interdependency taxonomy, representation, cascade mechanisms, and evidence that transient dynamics can matter. These papers prevent novelty claims based merely on “coupled networks,” “interdependencies,” or “dynamic cascades.”

## Chain II — Observation / identification / inference / prediction

| Paper ID | Title | Year | DOI | Corpus role |
|---|---|---:|---|---|
| `WEB_ce8c4d327b69` | Bayesian approach for the network reconstruction of interdependent critical infrastructure systems from cascading failures | 2026 | `10.1103/vswp-h4hx` | CORE; H1/H3; Evidence A/B |
| `P_dde48856721e` | Model order reduction for Bayesian approach to inverse problems | 2014 | `10.1186/2196-1166-1-2` | CORE; H1/T1 |
| `P_d9d970cb958c` | A Bayesian model updating approach for detection-related problems in water distribution networks | 2019 | `10.1016/j.ress.2018.12.014` | CORE; H1/H5 |
| `P_8b6ae007f63c` | Resilience evaluation for water distribution system based on partial nodes’ hydraulic information | 2023 | `10.1016/j.watres.2023.120148` | CORE; H1/T1 |

**Critical novelty guardrail:** uncertain ICI network reconstruction already exists. The thesis cannot claim “first inference of hidden infrastructure interdependencies.” The sharper question is how interface-identification uncertainty deforms downstream viability/recovery geometry.

## Chain III — Hazard / failure / consequence

| Paper ID | Title | Year | DOI | Corpus role |
|---|---|---:|---|---|
| `P_d1c9beeb5e03` | A Co-Simulation Approach for Time-Varying Damage Propagation in Interdependent Power and Wastewater Systems During Flood Events | 2025 | `10.1016/j.ijdrr.2024.105155` | CORE; H2/H4/H6 |
| `P_d0100f989f04` | Modest flooding can trigger catastrophic road network collapse due to compound failure | 2022 | — | CORE; H3/H6 |
| `WEB_2f29b5d5ba48` | Urban Flood Drifters (UFDs): identification, classification and characterisation | 2023 | — | FOUNDATION; H2/H6 |
| `WEB_9ee41da52abe` | Dynamically induced cascading failures in power grids | 2018 | `10.1038/s41467-018-04287-5` | STRONG_APPLIED; H2 |
| `P_3167cf61f309` | Catastrophic cascade of failures in interdependent networks | 2010 | `10.1038/nature08932` | STRONG_APPLIED; H3 |

**Use:** preserve the causal sequence forcing → hazard → damage/failure → cascade → functionality/service consequence. Flooding is a demonstrator, not the mathematical novelty by itself.

## Chain IV — Resilience / viability / recovery

| Paper ID | Title | Year | DOI | Corpus role |
|---|---|---:|---|---|
| `P_53655f583742` | Hamilton-Jacobi Reachability for Viability Analysis of Constrained Waste-to-Energy Systems under Adversarial Uncertainty | 2026 | `10.1016/j.ejcon.2026.101501` | CORE; H2/H4/H6; Evidence A |
| `P_27a58a16aab2` | Viability Problems for Nonautonomous Differential Inclusions | 1990 | `10.1137/0329014` | CORE; H5/H7; Evidence B |
| `P_3d7da872a7dd` | Equitable Resilience in Infrastructure Systems: Empirical Assessment of Disparities in Service Disruptions and Recovery | 2020 | `10.1061/(ASCE)NH.1527-6996.0000401` | CORE; H4/H5/H6; Evidence A |
| `P_f6f696d2afb0` | Novel methodology for resilience assessment of critical infrastructure considering the interdependencies: A case study in water, transportation and electricity sector | 2025 | `10.1016/j.ijdrr.2025.105271` | CORE; H2/H3; Evidence A |
| `P_375f20cdf434` | A resilience enhancement approach for interdependent networks incorporating recovery coupling mechanisms | 2026 | `10.1016/j.ress.2026.112375` | CORE; H2/H5 |

**Critical novelty guardrail:** HJ viability has already been used for an infrastructure system. The current thesis must not claim first infrastructure HJ viability. The candidate contribution is viability-boundary sensitivity to uncertain/dynamic interfaces.

## Chain V — Design / operation / adaptation

| Paper ID | Title | Year | DOI | Corpus role |
|---|---|---:|---|---|
| `P_097f37548705` | Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties | — | — | CORE; H2/H5 |
| `P_c55cc0f18ddf` | The interdependent network design problem for optimal infrastructure system restoration | — | — | CORE; H3/H5 |
| `P_203336fe17bf` | Coordinated emergency resource allocation for resilience enhancement in post-disaster electrified transportation networks | 2026 | `10.1016/j.jtrangeo.2025.104503` | CORE; H2/H5 |
| `P_f42847fad7a6` | Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards | 2026 | `10.1016/j.apenergy.2025.127004` | CORE; H2/H5/H6 |
| `P_4bf77c7fdfee` | Protection-interdiction-restoration: Tri-level optimization for enhancing interdependent network resilience | — | — | CORE; H3/H5 |

**Use:** restoration, dispatch, and network-design optimization are already developed. They are downstream applications/comparators unless the thesis deliberately changes to Type III.

## Chain VI — Sustainability / equity / decision

| Paper ID | Title | Year | DOI | Corpus role |
|---|---|---:|---|---|
| `P_2fd820854d1a` | Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery | — | — | CORE; H3/H4/H5/H6; Evidence A |
| `P_3d7da872a7dd` | Equitable Resilience in Infrastructure Systems: Empirical Assessment of Disparities in Service Disruptions and Recovery | 2020 | `10.1061/(ASCE)NH.1527-6996.0000401` | CORE; H4/H5/H6 |
| `P_9d3bbe2db836` | Weaving equity into infrastructure resilience research: a decadal review and future directions | — | — | CORE; H3/H4/H6/T1 |
| `P_58ffda062d1b` | Resilience and sustainability of civil infrastructure: Toward a unified approach | — | — | CORE; H4/T1 |
| `WEB_ac8934d0d859` | A data framework for assessing social inequality and equity in multi-sector urban systems | 2022 | `10.1111/jiec.13222` | STRONG_APPLIED; H4 |

**Use:** sustainability and equity are already established concerns. In the preferred architecture they enter primarily through admissible-state/service constraints and downstream decision trade-offs.

## Future citation discipline

1. Use the canonical `Paper_ID` to locate the record.
2. Treat missing year/author/DOI as missing; do not fill from memory.
3. Before equation-level or detailed-method claims, inspect the actual full paper.
4. Distinguish literature equations from integrating thesis equations.
5. Never convert absence in this 207-record corpus into a global novelty claim.
