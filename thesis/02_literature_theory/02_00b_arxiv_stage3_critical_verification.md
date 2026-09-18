# arXiv-to-Journal Verification and Critical Evidence Audit — Stage 3 Dynamics

**Status:** ACTIVE / VERIFIED EVIDENCE AUDIT  
**Date:** 2026-09-18  
**Purpose:** verify the scientific basis of the Stage-3 critical viewpoint against arXiv records and peer-reviewed journal versions, while separating established evidence from thesis-proposed mathematics.

## 1. Critical conclusion

The literature strongly supports the need for **dynamic, spatial, uncertainty-aware Power–Transportation modeling**, but it does **not** support treating the complete Stage-3 formulation as an already-established standard model.

Established dynamic P–T mechanisms + established hybrid/control mathematics ≠ already validated unified Stage-3 model.

Stage 3 should therefore be presented as an **evidence-grounded integration and testable mathematical construction**, not as a direct reproduction of one prior framework.

## 2. arXiv verification corrections

| Record | arXiv status | Verified journal status | Admission |
|---|---|---|---|
| Qian et al., V2Sim, arXiv:2412.09808 | preprint posted 2024 | **Published:** IEEE Transactions on Smart Grid 16(4), 3167–3178 (2025), DOI [10.1109/TSG.2025.3560976](https://doi.org/10.1109/TSG.2025.3560976) | [ARX-J][DIR-PT]; count journal article once |
| Li et al., Dynamic Flow Equilibrium, arXiv:2112.04683 | preprint posted 2021 | **Peer-reviewed:** CSEE Journal of Power and Energy Systems, DOI [10.17775/CSEEJPES.2022.04810](https://doi.org/10.17775/CSEEJPES.2022.04810) | [ARX-J][DIR-PT]; count journal article once |
| Doyen & De Lara, arXiv:1002.1140 | preprint | **Published:** Systems & Control Letters 59(10), 629–634 (2010), DOI [10.1016/j.sysconle.2010.07.008](https://doi.org/10.1016/j.sysconle.2010.07.008) | [ARX-J][MATH]; journal authority |
| Vinod & Oishi, arXiv:1810.05217 | preprint/accepted version | **Published:** Automatica 125, 109458 (2021), DOI [10.1016/j.automatica.2020.109458](https://doi.org/10.1016/j.automatica.2020.109458) | [ARX-J][MATH]; journal authority |
| Qiu et al., arXiv:2510.10914 | arXiv 2025 | no peer-reviewed version verified in this audit | [ARX-P][DIR-PT]; discovery/support only |
| Ghose et al., arXiv:2511.00941 | arXiv 2025 | no peer-reviewed version verified in this audit | [ARX-P][DIR-PT]; discovery/support only |
| Li et al., arXiv:2407.16796 | arXiv 2024 | no peer-reviewed version verified in this audit | [ARX-P][DIR-CI]; discovery/support only |
| Odunlami, Netto, & Susuki, arXiv:2509.02822 | arXiv 2025 | no peer-reviewed version verified in this audit | [ARX-P][POWER]; hybrid-model discovery only |
| Yuan et al., arXiv:2402.01547 | arXiv 2024 | no peer-reviewed version verified in this audit | [ARX-P][POWER]; stochastic-hybrid discovery only |

**Rule:** when a journal version is verified, the arXiv copy is an access/provenance aid, not a second independent evidence item.

## 3. Critical audit of Stage-3 claims

### C3.1 — Stage 3 should receive qualified mechanisms rather than arbitrary graph edges

**Status: SUPPORTABLE AS THESIS GOVERNANCE, NOT A LITERATURE STANDARD.**

Infrastructure literature distinguishes structural representation from functional dependency, while direct P–T studies specify explicit mechanisms such as signal power, repair access, EV charging demand, charging-station failure, and V2G. The exact rule that Stage 3 may only use mechanisms admitted by Stage 2 is, however, the thesis's research-governance architecture rather than a published universal convention.

### C3.2 — Dynamic P–T coupling is scientifically justified

**Status: STRONG DIRECT SUPPORT.**

Zou and Chen (2019) use dynamic traffic assignment rather than static assignment in an interdependent traffic–power resilience problem ([DOI](https://doi.org/10.1016/j.ress.2019.106557)). Li et al. model dynamic traffic assignment, departure-time/route choices, fast-charging queues, power-network voltage effects, and uncertain travel demand ([DOI](https://doi.org/10.17775/CSEEJPES.2022.04810)). Qian et al.'s peer-reviewed V2Sim platform integrates microscopic urban transportation simulation with a distribution-network model and resolves individual EV charging/V2G behavior and spatiotemporal charging loads ([DOI](https://doi.org/10.1109/TSG.2025.3560976)).

The literature therefore supports Y=Y(x,t) as potentially necessary for P–T interaction, but does not prove that the dynamic representation will outperform the static comparator in the thesis case; that remains H1.

### C3.3 — Spatial propagation is directly supported

**Status: STRONG DIRECT SUPPORT.**

Qian et al. resolve spatial–temporal EV charging loads across the coupled network ([DOI](https://doi.org/10.1109/TSG.2025.3560976)). Li et al. jointly model route/departure choices and voltage effects ([DOI](https://doi.org/10.17775/CSEEJPES.2022.04810)). Ghose et al. link road-segment speed, density, dwell time, and charging-zone demand to AC power-flow planning, but remain preprint-only in this audit ([arXiv:2511.00941](https://arxiv.org/abs/2511.00941)).

### C3.4 — Cascading Power→Transportation effects are directly supported

**Status: STRONG FOR P→T; PARTIAL FOR COMPLETE P→T→P LOOPS.**

Zhu et al. (2021) model power outage causing traffic-signal loss and roadway-capacity degradation during hurricane evacuation ([DOI](https://doi.org/10.1155/2021/5599073)). Fotouhi et al. (2017) model the reverse operational dependence in which transportation access is required for repair of damaged power infrastructure, while traffic signals themselves depend on power ([DOI](https://doi.org/10.1016/j.ress.2017.01.026)).

Together these establish the plausibility of P→T→P feedback. The exact chain flood → power failure → signal outage → congestion → repair-access delay → delayed restoration should nevertheless be labelled a **literature-grounded composite causal hypothesis** unless a single study validates the entire closed loop end-to-end.

### C3.5 — Charging-station failure and recovery create dynamic service effects

**Status: STRONG DIRECT SUPPORT.**

Wang et al. (2022) use dynamic traffic assignment with stochastic fast-charging-station failures and explicit failure/recovery phases ([DOI](https://doi.org/10.1111/mice.12736)).

### C3.6 — Continuous dynamics alone may be insufficient

**Status: STRONG MATHEMATICAL/POWER-SYSTEM SUPPORT; PARTIAL DIRECT P–T SUPPORT.**

Hybrid-system theory provides a rigorous language for continuous evolution combined with discrete switching, guards, and resets. Recent power-system preprints apply this explicitly to power-system switching and contingencies ([Odunlami et al., arXiv:2509.02822](https://arxiv.org/abs/2509.02822); [Yuan et al., arXiv:2402.01547](https://arxiv.org/abs/2402.01547)). A unified stochastic-hybrid P–T resilience model with the thesis's exact state/reset definitions has not been established by the reviewed evidence.

### C3.7 — Event-centric guards and reset maps

**Status: MATHEMATICALLY ESTABLISHED; P–T PARAMETERIZATION NOT YET ESTABLISHED.**

The event tuple used by the thesis is a reasonable hybrid-system formalization, but its exact fields are a thesis representation and require operational definition and validation.

### C3.8 — The competing-event race

**Status: CONCEPTUALLY PLAUSIBLE, CURRENTLY UNDER-SOURCED FOR THIS THESIS.**

The rule k*=argmin(T_k) is consistent with event-scheduling/competing-process ideas, but this audit did not establish it as a standard model for coupled P–T infrastructure cascades. It should therefore be presented as a proposed event-scheduling mechanism requiring explicit provenance or derivation, not as settled Stage-3 theory.

### C3.9 — Event time, propagation delay, mechanism timescale, and recovery time

**Status: CONCEPTUALLY STRONG; EXACT NOTATION IS THESIS-PROPOSED.**

The distinction among event timestamp, causal delay, characteristic mechanism timescale, and recovery duration is scientifically sound. The exact four-way notation is a thesis temporal ontology, not a verified universal taxonomy.

### C3.10 — Multiscale dynamics

**Status: SUPPORTED IN PRINCIPLE; THESIS DESCRIPTORS REQUIRE JUSTIFICATION.**

Coupled P–T literature spans electrical response, traffic flow, charging queues, user decisions, repair, and restoration over different timescales. However, the proposed ratios tau_a/tau_b, log(tau_a/tau_b), and normalized timescale contrast were not verified as standard infrastructure-resilience quantities and should remain candidate thesis descriptors.

### C3.11 — State-to-service mapping

**Status: STRONGLY JUSTIFIED; EXACT SERVICE FUNCTIONS ARE CASE-SPECIFIC.**

Direct P–T resilience studies quantify functional consequences of physical/cross-system disruption. A mapping Q_P=h_P(Y), Q_T=h_T(Y) is defensible, but exact service ratios must be frozen from service requirements, aggregation rules, and data availability.

### C3.12 — Stage-3 output object and acceptance gate

**Status: THESIS GOVERNANCE, NOT PRIOR-LITERATURE FACT.**

The proposed rich Stage-3 handoff and PASS/FAIL/BLOCKED gate synthesize established dynamics, V&V, causal-consistency, numerical-credibility, and uncertainty practices. Their exact packaging is a thesis governance object.

## 4. Evidence-strength summary

| Proposition | Evidence status | Final writing label |
|---|---|---|
| Dynamic P–T coupling | strong direct peer-reviewed | ESTABLISHED BASIS |
| Spatially varying P–T interaction | strong direct peer-reviewed | ESTABLISHED BASIS |
| P→T signal-power cascade | strong direct peer-reviewed | ESTABLISHED BASIS |
| T→P repair-access dependency | strong direct peer-reviewed | ESTABLISHED BASIS |
| Closed P→T→P cascade | mechanisms supported separately | COMPOSITE / TESTABLE |
| Dynamic traffic assignment | strong direct peer-reviewed | ESTABLISHED METHOD |
| Microscopic EV/V2G dynamics | strong direct peer-reviewed | ESTABLISHED METHOD FAMILY |
| Continuous + discrete hybrid representation | strong generic/power support | TRANSFERABLE FOUNDATION |
| Stochastic-hybrid P–T resilience model | limited direct evidence | THESIS CONSTRUCTION |
| Guard/reset event tuple | strong mathematical basis | THESIS PARAMETERIZATION |
| Competing-event argmin race | insufficient direct support | PROPOSED / NEEDS PROVENANCE |
| Four-time taxonomy | conceptually justified | THESIS TEMPORAL ONTOLOGY |
| Multiscale timescale ratios | no standard provenance verified | CANDIDATE DESCRIPTORS |
| State→service mapping | strong infrastructure basis | ESTABLISHED ABSTRACTION / CASE-SPECIFIC FUNCTION |
| Rich Stage-3 handoff | thesis-specific | THESIS GOVERNANCE OBJECT |
| PASS/FAIL/BLOCKED gate | thesis-specific | THESIS GOVERNANCE OBJECT |

## 5. High-confidence journal references

1. Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026
2. Zou, Q., & Chen, S. (2019). Enhancing resilience of interdependent traffic-electric power system. *Reliability Engineering & System Safety, 191*, 106557. https://doi.org/10.1016/j.ress.2019.106557
3. Zhu, Y., Ozbay, K., Yang, H., Zuo, F., Sha, D., & Ghosh, I. (2021). Modeling and simulation of cascading failures in transportation systems during hurricane evacuations. *Journal of Advanced Transportation, 2021*, 5599073. https://doi.org/10.1155/2021/5599073
4. Wang, H., Abdin, A. F., Fang, Y.-P., & Zio, E. (2022). Resilience assessment of electrified road networks subject to charging station failures. *Computer-Aided Civil and Infrastructure Engineering, 37*(3), 300–316. https://doi.org/10.1111/mice.12736
5. Li, J., Xu, X., Yan, Z., Wang, H., & Chen, Y. (2024). Dynamic flow equilibrium of transportation and power distribution networks considering flexible traveling choices and voltage quality improvement. *CSEE Journal of Power and Energy Systems*. https://doi.org/10.17775/CSEEJPES.2022.04810
6. Qian, T., Fang, M., Hu, Q., Shao, C., & Zheng, J. (2025). V2Sim: An open-source microscopic V2G simulation platform in urban power and transportation network. *IEEE Transactions on Smart Grid, 16*(4), 3167–3178. https://doi.org/10.1109/TSG.2025.3560976
7. Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008
8. Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

## 6. arXiv discovery references retained with caution

- Qiu, J., Thompson, D., Youcef-Toumi, K., & Farid, A. M. (2025). *Optimal multi-modal transportation and electric power flow: The value of coordinated dynamic operation*. arXiv:2510.10914. https://arxiv.org/abs/2510.10914
- Ghose, D., Sivaranjani, S., & Qin, J. (2025). *Traffic-aware grid planning for dynamic wireless electric vehicle charging*. arXiv:2511.00941. https://arxiv.org/abs/2511.00941
- Li, Y., Kim, K., Leyffer, S., Menickelly, M., Lewis, L. P., & Bergerson, J. (2024). *Modeling and solving cascading failures across interdependent infrastructure systems*. arXiv:2407.16796. https://arxiv.org/abs/2407.16796
- Odunlami, B. G., Netto, M., & Susuki, Y. (2025). *Hybrid dynamical systems modeling of power systems*. arXiv:2509.02822. https://arxiv.org/abs/2509.02822
- Yuan, S., Wang, L. Y., Yin, G., & Nazari, M. H. (2024). *Contingency detection in modern power systems: A stochastic hybrid system method*. arXiv:2402.01547. https://arxiv.org/abs/2402.01547

## 7. Revised critical viewpoint

Peer-reviewed P–T literature establishes dynamic, spatial, failure/recovery, charging, and bidirectional dependency mechanisms. Hybrid/control literature supplies rigorous continuous–discrete and stochastic mathematical foundations. The unified causal stochastic-hybrid P–T propagation object used by this thesis remains a proposed integration that must be verified, validated, and tested against simpler comparators.

This wording supports RQ3/H1 without prejudging H1 and prevents established component theories from being misrepresented as an already validated unified thesis model.