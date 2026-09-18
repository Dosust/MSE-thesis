# Stage 1 Evidence and Ontology Register v1.0

**Status:** ACTIVE FREEZE AUTHORITY — literature-to-mathematics bridge  
**Date:** 2026-09-18  
**Stage:** 1 — Spatiotemporal Multilayer System-of-Systems Structure  
**Purpose:** map established literature objects to Stage-1 thesis objects without converting literature support into case-specific causal claims.

## 1. Evidence-to-ontology principle

The evidence base supports the following hierarchy:

```math
\boxed{
\text{Entity}
\rightarrow
\text{Relation/interface}
\rightarrow
\text{candidate dependency}
\rightarrow
\text{causally qualified dependency}
\rightarrow
\text{dynamic interdependent system}.
}
```

The hierarchy is used as a thesis synthesis. It prevents multilayer structure, interface evidence, causal qualification, and dynamic behavior from being collapsed into one generic cross-layer edge.

## 2. Evidence labels

| Label | Meaning |
|---|---|
| ESTABLISHED | broadly established concept/theory/method family |
| DIRECT | directly demonstrated in peer-reviewed P–T literature |
| SCREENING | accepted as a candidate-generation method, not causal proof |
| NOT-JUSTIFIED | literature does not support the stronger inference |
| THESIS-SYNTHESIS | thesis object constructed from literature-supported ingredients |

## 3. Concept-to-thesis-object register

| ID | Concept | Evidence status | Principal evidence | What literature supports | What it does not prove | Stage-1 thesis object |
|---|---|---|---|---|---|---|
| E01 | dependency vs interdependency | ESTABLISHED | Rinaldi et al. (2001), DOI `10.1109/37.969131` | directional dependency and reciprocal interdependency are distinct conceptual relations | case-specific causal connection | `R_prior`, Stage-2 `I_acc` |
| E02 | physical/cyber/geographic/logical classes | ESTABLISHED conceptual taxonomy | Rinaldi et al. (2001); Ouyang (2014); Yu et al. (2025) | heterogeneous mechanism classes exist | taxonomy alone identifies a causal link | candidate `mechanism_class` + supporting P/T/I/O roles |
| E03 | semantic infrastructure entities | ESTABLISHED method family | McNally et al. (2007), DOI `10.1068/b32078` | infrastructure objects need semantic and geographic representation | exact thesis entity tuple | `E_i^alpha` |
| E04 | functional dependency | ESTABLISHED method family | Hruska et al. (2021), DOI `10.18278/jcip.2.2.6` | dependency should be tied to function/service rather than adjacency alone | a generic graph edge is dependency | entity `function_roles`, relation `exchange_semantics` |
| E05 | multilayer representation | ESTABLISHED mathematical foundation | De Domenico et al. (2013), DOI `10.1103/PhysRevX.3.041022`; Kivela et al. (2014), DOI `10.1093/comnet/cnu016`; Boccaletti et al. (2014), DOI `10.1016/j.physrep.2014.07.001` | typed multilayer/node-layer relations can be represented mathematically | a multilayer edge is causally validated | `G^(1)`, typed layers and candidate relations |
| E06 | dependency-driven cascades | ESTABLISHED theoretical foundation | Buldyrev et al. (2010), DOI `10.1038/nature08932`; Gao et al. (2012), DOI `10.1038/nphys2180` | dependency links can qualitatively change failure behavior | binary dependency is sufficient for engineering P–T systems | motivation for later Stage-3 dynamics only |
| E07 | heterogeneous model interfaces | ESTABLISHED method family | Zhou et al. (2020), DOI `10.1016/j.ijcip.2020.100391` | interfaces/variables can link heterogeneous physics-based and data-driven models | exact thesis relation tuple | `interface_semantics`, `exchange_semantics`, `operating_context` |
| E08 | multilayer functional/service flows | ESTABLISHED method family | Ahangar et al. (2020), DOI `10.1016/j.cor.2019.104883` | cross-layer edges can carry heterogeneous commodities/services/functions | interface existence fixes service magnitude | `exchange_semantics`; strength deferred |
| E09 | P→T signal power | DIRECT | Fotouhi et al. (2017), DOI `10.1016/j.ress.2017.01.026`; Zou & Chen (2019), DOI `10.1016/j.ress.2019.106557` | electricity-to-signal functionality is an established P–T mechanism family | a specific feeder-to-signal case mapping | `R_prior` mechanism family + case `C_struct` |
| E10 | T→P repair access | DIRECT | Fotouhi et al. (2017), DOI `10.1016/j.ress.2017.01.026` | road accessibility can affect repair feasibility/time | specific asset/access dependency in a new case | `R_prior` mechanism family + case structural-access candidate |
| E11 | EV charging T→P | DIRECT | coupled PDN–TN literature; network-equilibrium literature | routing/charging decisions create spatial-temporal electrical demand | every charger/EV pair has equal coupling | candidate charging interface semantics |
| E12 | P→T charging/routing constraints | DIRECT | coupled transportation–distribution equilibrium literature | price/availability/voltage constraints can influence charging/routing | case-specific effect size | prior mechanism class; Stage 2/3 quantify |
| E13 | spatiotemporal P–T coupling | DIRECT | Li et al. (2024), DOI `10.17775/CSEEJPES.2022.04810`; related dynamic P–T studies | P–T interaction can be time-, state-, and location-dependent | Stage 1 should estimate dynamic coupling | Stage-1 `operating_context`; dynamic law deferred |
| E14 | microscopic/aggregate resolution | ESTABLISHED modeling alternatives | Qian et al. (2025), DOI `10.1109/TSG.2025.3560976` | coupling can be represented at different resolutions | one resolution is universally correct | `resolution_level` on entity/relation |
| E15 | functional heterogeneity of same entity type | ESTABLISHED recent direction | recent coupled P–T supply–demand literature | same entity class can differ in role/capacity/redundancy/connectivity | type alone determines coupling strength | no type-derived `w_ij`; retain attributes/provenance |
| E16 | proximity-based candidate generation | SCREENING | GIS interdependency literature | proximity thresholds can generate spatial candidates with sensitivity/engineering judgment | proximity proves dependency | `Gamma_ij^str` screening evidence |
| E17 | correlation/data association | SCREENING only | data-driven/physics-based interface literature | association can nominate evidence candidates | correlation establishes causality | evidence basis only; Stage 2 qualification required |
| E18 | logical/organizational interdependency | ESTABLISHED/refined | Yu et al. (2025), DOI `10.1111/risa.16555` | rules, institutions, planned tasks and decisions mediate logical relations | organization is a physical P/T edge | supporting `O` domain |

## 4. Thesis entity representation

The literature supports semantic infrastructure entities but not the exact following tuple. The tuple is therefore explicitly classified `THESIS-SYNTHESIS`:

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

`r_i` is retained instead of the source review's `x_i` notation to preserve the thesis-wide coordinate/state notation freeze.

## 5. Thesis Stage-1 relation representation

Stage 1 requires more than a pair `(i,j)` but must still remain non-causal. The final Stage-1 relation object is:

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

with:

```math
\begin{aligned}
\gamma_{ij} &= \text{interface semantics / interface class},\\
\Phi_{ij} &= \text{exchanged function/service/resource/information semantics},\\
d_{ij} &= \text{declared direction of the candidate relation},\\
m_{ij}^{\rm cand} &= \text{candidate mechanism family from prior evidence},\\
c_{ij}^{\rm cand} &= \text{candidate operating/activation context},\\
b_{ij} &= \text{basis for structural admission},\\
s_{ij} &= \text{Stage-1 relation/evidence status},\\
\mathcal E_{ij} &= \text{evidence/provenance references},\\
q_{ij}^{\rm evid} &= \text{evidence-confidence representation},\\
\ell_{ij} &= \text{relation modeling resolution},\\
\chi_{ij}^{\rm norm} &= \text{normative/jurisdictional admissibility}.
\end{aligned}
```

`m_ij^cand` and `c_ij^cand` are candidate descriptors only. They do not constitute Stage-2 mechanism acceptance.

## 6. Existence, strength and confidence are separate

Stage 1 freezes:

```math
\boxed{
\text{existence status}
\neq
\text{coupling strength}
\neq
\text{evidence confidence}.
}
```

At Stage 1:

```math
s_{ij}^{\rm exist}
\in
\{
\mathrm{PRIOR\_DOCUMENTED},
\mathrm{STRUCTURAL\_CANDIDATE},
\mathrm{UNRESOLVED},
\mathrm{EXCLUDED}
\}.
```

No functional coupling strength `w_ij` is estimated by Stage 1.

```math
\boxed{
w_{ij}=\mathrm{NOT\ ESTIMATED\ IN\ STAGE\ 1}.
}
```

`q_ij^evid` may be numeric only if a declared and auditable calibration/scoring procedure exists. Otherwise a categorical confidence class with method/provenance is required. Confidence never changes a structural candidate into an accepted causal dependency.

## 7. Interface semantics are heterogeneous

```math
\boxed{
\text{interface existence}
\neq
\text{amount/type of service transferred}.
}
```

Examples of Stage-1 semantics include:

```math
P_i\rightarrow T_j:\quad
\Phi_{ij}=\text{electrical supply to traffic-control equipment},
```

and:

```math
T_k\rightarrow P_l:\quad
\Phi_{kl}=\text{repair accessibility/travel-time service},
```

which is not a physical commodity flow. The relation schema must therefore preserve semantic heterogeneity.

## 8. Hard Stage-1 scientific guardrails

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

## 9. Stage-1 to Stage-2 handoff

```math
\boxed{
\mathfrak R_{ij}^{\alpha\beta,(1)}
\xrightarrow[
\text{mechanism evidence + activation qualification + falsification}
]{G_2}
\mathfrak I_{ij}^{\alpha\beta}.
}
```

Stage 1 asks:

```math
\boxed{
\text{What exists and what deserves causal investigation?}
}
```

Stage 2 asks:

```math
\boxed{
\text{Which candidate relations are genuine causal dependencies, and why?}
}
```

## 10. Core references

1. Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). *Identifying, understanding, and analyzing critical infrastructure interdependencies*. IEEE Control Systems, 21(6), 11–25. DOI: https://doi.org/10.1109/37.969131
2. Ouyang, M. (2014). *Review on modeling and simulation of interdependent critical infrastructure systems*. Reliability Engineering & System Safety, 121, 43–60. DOI: https://doi.org/10.1016/j.ress.2013.06.040
3. McNally, R. K., Lee, S.-W., Yavagal, D., & Xiang, W.-N. (2007). *Learning the Critical Infrastructure Interdependencies through an Ontology-Based Information System*. Environment and Planning B, 34(6), 1103–1124. DOI: https://doi.org/10.1068/b32078
4. De Domenico, M. et al. (2013). *Mathematical Formulation of Multilayer Networks*. Physical Review X, 3, 041022. DOI: https://doi.org/10.1103/PhysRevX.3.041022
5. Kivela, M. et al. (2014). *Multilayer Networks*. Journal of Complex Networks, 2, 203–271. DOI: https://doi.org/10.1093/comnet/cnu016
6. Boccaletti, S. et al. (2014). *The structure and dynamics of multilayer networks*. Physics Reports, 544, 1–122. DOI: https://doi.org/10.1016/j.physrep.2014.07.001
7. Buldyrev, S. V. et al. (2010). *Catastrophic cascade of failures in interdependent networks*. Nature, 464, 1025–1028. DOI: https://doi.org/10.1038/nature08932
8. Gao, J. et al. (2012). *Networks formed from interdependent networks*. Nature Physics, 8, 40–48. DOI: https://doi.org/10.1038/nphys2180
9. Hruska, R., McGillivary, K., & Edsall, R. (2021). *A Functional All-Hazard Approach to Critical Infrastructure Dependency Analysis*. Journal of Critical Infrastructure Policy, 2(2), 103–123. DOI: https://doi.org/10.18278/jcip.2.2.6
10. Zhou, S. et al. (2020). *Integrating data-driven and physics-based approaches to characterize failures of interdependent infrastructures*. International Journal of Critical Infrastructure Protection, 31, 100391. DOI: https://doi.org/10.1016/j.ijcip.2020.100391
11. Ahangar, N. E., Sullivan, K. M., & Nurre, S. G. (2020). *Modeling interdependencies in infrastructure systems using multi-layered network flows*. Computers & Operations Research, 117, 104883. DOI: https://doi.org/10.1016/j.cor.2019.104883
12. Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). *Quantifying the resilience of an urban traffic-electric power coupled system*. Reliability Engineering & System Safety, 163, 79–94. DOI: https://doi.org/10.1016/j.ress.2017.01.026
13. Zou, Q., & Chen, S. (2019). *Enhancing resilience of interdependent traffic-electric power system*. Reliability Engineering & System Safety, 191, 106557. DOI: https://doi.org/10.1016/j.ress.2019.106557
14. Li, J. et al. (2024). *Dynamic flow equilibrium of transportation and power distribution networks considering flexible traveling choices and voltage quality improvement*. DOI: https://doi.org/10.17775/CSEEJPES.2022.04810
15. Qian, T. et al. (2025). *V2Sim: An Open-Source Microscopic V2G Simulation Platform in Urban Power and Transportation Network*. IEEE Transactions on Smart Grid, 16(4), 3167–3178. DOI: https://doi.org/10.1109/TSG.2025.3560976
16. Yu, D. J. et al. (2025). *Logical interdependencies in infrastructure: What are they, how to identify them, and what do they mean for infrastructure risk analysis?* Risk Analysis, 45, 356–375. DOI: https://doi.org/10.1111/risa.16555

## 11. Freeze implication

This register is now part of the Stage-1 framework authority. A Stage-1 freeze is not admissible until the mathematical contract, structural schema, CIR relation schema, generic fixtures, and final framework all conform to this register.