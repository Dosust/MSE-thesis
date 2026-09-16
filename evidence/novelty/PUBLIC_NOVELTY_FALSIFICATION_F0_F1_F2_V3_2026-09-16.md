# Public Novelty Falsification F0/F1/F2 v3 — 2026-09-16

**Status:** PUBLIC-WEB FALSIFICATION STRENGTHENED; AUTHENTICATED DATABASE CLOSURE STILL BLOCKED  
**Scope:** targeted third-pass falsification after ASU subtraction and canonical-notation reconciliation  
**Authority:** this file narrows candidate claims; it does **not** certify global novelty.

## 1. Scientific rule

```math
\boxed{\text{Search to falsify the proposed contribution before searching to support it.}}
```

The admissible inference is one-way:

```math
\text{public prior art found}\Rightarrow\text{broad novelty claim is rejected/narrowed},
```

but

```math
\text{public prior art not found}\not\Rightarrow\text{global novelty}.
```

Final novelty closure still requires the frozen Scopus, Web of Science Core Collection, Compendex and IEEE Xplore searches in `FORMAL_NOVELTY_SEARCH_PROTOCOL_F0_F1_F2_V1.md`.

---

## 2. F0 — dependency semantics, dynamics and executable coupling

### Broad claim

> Directed, typed, dynamic or ontology-supported infrastructure dependency representation is novel.

### Decision

```math
\boxed{\text{FALSIFIED}.}
```

Representative prior art now includes:

1. Rinaldi, Peerenboom & Kelly (2001), *Identifying, understanding, and analyzing critical infrastructure interdependencies*, IEEE Control Systems Magazine, DOI `10.1109/37.969131` — dependency/interdependency distinctions and interdependency dimensions.
2. Masucci et al. (2009), *Ontology-Based Critical Infrastructure Modeling and Simulation* — ontology/rule semantics supporting federated CI simulation and dynamic binding of heterogeneous infrastructure models.
3. Tofani et al. (2010), *Using Ontologies for the Federated Simulation of Critical Infrastructures*, DOI `10.1016/j.procs.2010.04.258` — ontology-based dependency relations translated into auxiliary structures for federated simulators.
4. Galbusera, Trucco & Giannopoulos (2020), *Modeling interdependencies in multi-sectoral critical infrastructure systems: Evolving the DMCI approach*, DOI `10.1016/j.ress.2020.107072` — dynamic, network-centric, service-level multi-sector dependency modelling that can federate with sector-specific models.

Therefore the thesis must not claim novelty for directionality, typing, dynamic interdependency, semantic dependency representation, ontology grounding, or coupling of heterogeneous simulators.

### Residual after third-pass subtraction

```math
\boxed{
N_1^*:
\text{qualified mechanism evidence}
\rightarrow\mathfrak d_e
\rightarrow\Xi_e
\rightarrow F_{\mathcal G}^{m}
\rightarrow\Delta Q
\rightarrow\{M_0,M_1,M_2\}
\rightarrow\text{matched empirical/decision value}.
}
```

The candidate contribution is thus primarily **implementation + falsifiable validation of a particular evidence-to-dynamics chain**, not invention of a dependency representation.

Status: `UNRESOLVED_GLOBAL / VALIDATION-DEPENDENT`.

---

## 3. F1 — partial observation, belief states and viability/safety

### Broad claims

> Stochastic viability under uncertainty is novel.  
> Mapping observations to a belief/posterior and using that belief for constrained safe control is novel.  
> Belief-space unsafe/safe-region computation is novel.

### Decision

```math
\boxed{\text{FALSIFIED}.}
```

Representative prior art:

1. Doyen & De Lara (2010), *Stochastic viability and dynamic programming*, Systems & Control Letters 59(10):629–634, DOI `10.1016/j.sysconle.2010.07.008` — stochastic viability kernels and viable feedbacks under chance constraints.
2. Wang, Chaudhuri & Kavraki (2018), *Bounded Policy Synthesis for POMDPs with Safe-Reachability Objectives*, arXiv:1801.09780 — safe-reachability synthesis over constrained belief spaces.
3. Hoerger et al. (2025), *Anytime Probabilistically Constrained Provably Convergent Online Belief Space Planning*, IEEE Transactions on Robotics, DOI `10.1109/TRO.2025.3610176` — probabilistically constrained control/planning under partial observability with convergence guarantees.
4. Yildiz et al. (2026), *Backward Monte Carlo Tree Search: Charting Unsafe Regions in the Belief-Space*, Journal of Artificial Intelligence Research 85, DOI `10.1613/JAIR.1.18011` — backward belief-space search identifying unsafe regions under partial observation.
5. Vahs, Verhagen & Tumova (2026), *Safety-critical Control Under Partial Observability: Reach-Avoid POMDP meets Belief Space Control*, arXiv:2603.10572 — certificate-based belief-space safety and information-gathering control.

Hence the abstract chain

```math
D_{0:t}\rightarrow b_t(Y)\rightarrow\text{safe/viable decision}
```

is established prior art at the control-theory level.

### Residual after third-pass subtraction

```math
\boxed{
N_2':
\text{heterogeneous }P,T,I,O\text{ observations}
\rightarrow b_t(Y)
\rightarrow F_{\mathcal G}^{m}
\rightarrow\mathcal U(z_I,z_O)
\rightarrow K_{\rm sus}
\rightarrow\mathcal V_{\rm sus}
\rightarrow\text{decision value}.
}
```

The thesis must test whether this **infrastructure-specific composition** improves prediction, viable-control characterization, or intervention choice relative to declared point-estimate / physical-only / reduced-information baselines.

Status: `UNRESOLVED_GLOBAL / VALIDATION-DEPENDENT`.

---

## 4. F2 — viability geometry and interface/component prioritization

### Broad claims

> Distance to the viability boundary is novel.  
> Geometric robustness of viability kernels is novel.  
> Parameter sensitivity of viability is novel.  
> Ranking interdependent infrastructure assets/interfaces for resilience is novel.

### Decision

```math
\boxed{\text{FALSIFIED}.}
```

The subtraction is now stronger than v2.

1. Alvarez & Martin (2011), *Geometric Robustness of Viability Kernels and Resilience Basins*, DOI `10.1007/978-3-642-20423-4_8`, explicitly studies viability-kernel geometry, parameter/boundary sensitivity, and state robustness as distance to the viability-kernel boundary.
2. Balakrishnan & Zhang (2020), *Criticality and Susceptibility Indexes for Resilience-Based Ranking and Prioritization of Components in Interdependent Infrastructure Networks*, DOI `10.1061/(ASCE)ME.1943-5479.0000769`, ranks nodes and links in interdependent infrastructure networks for resilience decision support.
3. A 2026 review, *Criticality, resilience and prioritization of components in interdependent infrastructure systems*, DOI `10.1016/j.rcns.2026.02.003`, documents an established field of component criticality/prioritization and identifies remaining socio-technical, full-resilience-cycle, calibration, validation and uncertainty gaps.
4. The September 2026 paper *A multiplex network-based framework to assess interdependent infrastructure asset criticality and priority under natural hazard scenarios*, DOI `10.1016/j.ijdrr.2026.106319`, already provides asset-level ranking in a node-weighted directed multiplex interdependent-infrastructure model, accounts for multiple interaction types and cascading effects, and demonstrates hazard-priority ranking in an urban-flood case study.

Therefore the thesis must not claim novelty for generic infrastructure asset/interface ranking, multiplex criticality, hazard-priority ranking, viability-boundary distance, or generic viability sensitivity.

### Surviving narrow residual

The current candidate object is mechanism-specific and decision-tested:

```math
\rho_g(Y;\Theta)=d_g\!\left(Y,\partial\mathcal V_{\rm sus}(\Theta)\right).
```

For a smooth declared mechanism parameter direction `v`,

```math
\boxed{
S_{e,v}^{\mathcal V}(Y)
=-D_{\theta_e}\rho_g(Y;\Theta)[v].
}
```

For nonsmooth, hybrid or topological changes, use a predeclared finite/actual intervention contrast:

```math
\boxed{
\Delta_e\mathcal M_{\mathcal V}
=
\mathcal M_{\mathcal V}(\Theta+\Delta_e)
-
\mathcal M_{\mathcal V}(\Theta).
}
```

The residual is therefore

```math
\boxed{
N_3':
\text{evidence-qualified dependency mechanism perturbation}
\rightarrow
\Delta\mathcal M_{\mathcal V}
\rightarrow
\text{mechanism/interface ranking}
\rightarrow
\text{equal-budget matched intervention validation}.
}
```

This is narrower than “criticality ranking.” The result is only scientifically useful if the viability-based ranking is prospectively compared with justified structural, flow/load, static-dependency and other baseline rankings under the same intervention budget and uncertainty treatment.

Status: `UNRESOLVED_GLOBAL / VALIDATION-DEPENDENT`.

---

## 5. Third-pass contribution boundary

The public-web subtraction now gives

```math
\boxed{
\mathcal C_{proposed}-\mathcal C_{public\ prior\ art}
=
\{N_1^*,N_2',N_3'\}_{\rm unresolved}.
}
```

The common structure is no longer “new mathematics in isolation.” It is:

```math
\boxed{
\text{evidence-qualified integration}
+\text{matched falsification}
+\text{VVUQ}
+\text{demonstrated engineering decision value}.
}
```

Accordingly, the thesis contribution should be promoted only if the chain survives the relevant hypothesis tests. A mathematically elegant pipeline with no incremental predictive or intervention value remains a negative/null result, not a validated contribution.

---

## 6. Falsification firewall

The following statements remain prohibited before authenticated closure and confirmatory validation:

- “the first dynamic infrastructure interdependency representation”;
- “the first belief-space/uncertainty-aware viability method”;
- “the first geometric viability resilience metric”;
- “the first criticality ranking for interdependent infrastructure”;
- “the first viability-based infrastructure intervention ranking” unless formal database closure and matched experimental evidence directly support that exact statement.

Admissible language is:

> `No work identified in the current ASU + public-web audit has yet been shown to establish the complete evidence-qualified P–T–I–O mechanism-to-belief-to-controlled-viability-to-matched-intervention chain. This residual remains provisional until authenticated database closure.`

---

## 7. Evidence sources added/confirmed in this pass

- Rinaldi et al. (2001), DOI `10.1109/37.969131`.
- Tofani et al. (2010), DOI `10.1016/j.procs.2010.04.258`.
- Galbusera et al. (2020), DOI `10.1016/j.ress.2020.107072`.
- Doyen & De Lara (2010), DOI `10.1016/j.sysconle.2010.07.008`.
- Hoerger et al. (2025), DOI `10.1109/TRO.2025.3610176`.
- Yildiz et al. (2026), DOI `10.1613/JAIR.1.18011`.
- Alvarez & Martin (2011), DOI `10.1007/978-3-642-20423-4_8`.
- Balakrishnan & Zhang (2020), DOI `10.1061/(ASCE)ME.1943-5479.0000769`.
- *Criticality, resilience and prioritization of components in interdependent infrastructure systems* (2026), DOI `10.1016/j.rcns.2026.02.003`.
- *A multiplex network-based framework to assess interdependent infrastructure asset criticality and priority under natural hazard scenarios* (2026), DOI `10.1016/j.ijdrr.2026.106319`.

## 8. Gate decision

```math
\boxed{\text{PUBLIC FALSIFICATION: STRENGTHENED}}
```

```math
\boxed{\text{GLOBAL NOVELTY CERTIFICATION: BLOCKED\_EXTERNAL\_ACCESS}}
```

No task is upgraded to global-novelty `PASS` by this file.
