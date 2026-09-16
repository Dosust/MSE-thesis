# Public Novelty Falsification Search F0/F1/F2 v1.0

**Date:** 2026-09-16  
**Status:** PUBLIC-WEB PROXY ONLY — not a substitute for authenticated Scopus/WoS/Compendex/IEEE execution  
**Purpose:** attempt to falsify the strongest candidate novelty objects before mathematical freeze.

## 1. Search rule

```math
\boxed{\text{Find the closest prior art first; narrow novelty rather than defend it.}}
```

Public web discovery can disprove a broad novelty claim. It cannot certify global novelty.

---

# F0 — causal/dynamic dependency grammar

## Candidate claim before search

A generic claim such as “dynamic infrastructure interdependency modeling is novel” was tested and **falsified**.

## High-relevance prior art found

1. Zhang & Peeta (2014), *Dynamic and disequilibrium analysis of interdependent infrastructure systems*, Transportation Research Part B 67:357–381.  
   DOI: `10.1016/j.trb.2014.04.008`  
   Evidence: explicitly develops within-period and multi-period dynamic infrastructure-interdependency models, disturbance propagation, cascading effects, recovery and coordinated decision-making.

2. Liu et al. (2026), *Vulnerability analyses of power-water interdependent infrastructure networks by using load-functional dependency coupled cascading failure model*.  
   DOI: `10.1016/j.ress.2026.113092`  
   Evidence: explicitly couples load dynamics and progressive functional dependency with bidirectional feedback.

3. Hoff & Chester (2023), ASU, synthetic network + interdependency + cascading-failure fusion.

4. RISE/REFIT/PSI-Cascade, ASU, implemented coupled-infrastructure and cascading-failure architectures.

## F0 adjudication

```math
\boxed{\text{Broad N1 is falsified.}}
```

Novelty cannot be:

- dynamic interdependency modeling;
- cascading propagation across infrastructures;
- bidirectional functional dependency;
- combining multilayer/synthetic networks with cascade models.

### Narrowed N1 candidate

The candidate residual requiring formal search is:

```math
\boxed{
N_1^{\prime}:
\text{an evidence-grounded interface object }
\mathfrak I_{ij}^{\alpha\beta}
=(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t)
}
```

whose fields have explicit semantics/provenance and are composed into a hybrid `P-T-I-O` dynamical model, with nested ablation against independent/static representations.

**Status:** `UNRESOLVED_GLOBAL`; authenticated database search still required.

---

# F1 — uncertainty-aware viability

## Candidate claim before search

A broad claim such as “incorporating uncertainty into viability/resilience is novel” was tested and **falsified**.

## High-relevance prior art found

1. Doyen & De Lara (2010), *Stochastic viability and dynamic programming*, Systems & Control Letters 59(10):629–634.  
   DOI: `10.1016/j.sysconle.2010.07.008`  
   Establishes stochastic viability kernels and chance-constrained viable feedbacks through dynamic programming.

2. Rougé, Mathias & Deffuant lineage (2013), *Extending the viability theory framework of resilience to uncertain dynamics...*, Ecological Indicators 29:420–433.  
   DOI: `10.1016/j.ecolind.2012.12.032`  
   Defines stochastic viability kernels, probability of resilience, restoration-time distributions, and dynamic-programming management strategies.

3. Chu et al. (2018), resilience and environmental water releases, uses stochastic viability to define recovery probability and resilience against shocks.

4. Modern stochastic/robust viability and reachability literature already addresses uncertainty in controlled systems.

## F1 adjudication

```math
\boxed{\text{Broad N2 is falsified.}}
```

Novelty cannot be “stochastic viability,” “uncertainty-aware viability,” or “probabilistic resilience” in general.

### Narrowed N2 candidate

```math
\boxed{
N_2^{\prime}:
D_{0:t}
\rightarrow
p(Y_t\mid D_{0:t})
\rightarrow
\mathcal V_{\rm sus}(t)
}
```

where heterogeneous power/transport/information/organization observations are mapped to a posterior state distribution and that **observation/posterior uncertainty is propagated into service-constrained infrastructure viability boundaries and decisions**.

The distinctive candidate is therefore the end-to-end inference-to-viability composition in a coupled infrastructure setting, not stochastic viability itself.

**Status:** `UNRESOLVED_GLOBAL`; authenticated search required.

---

# F2 — viability-sensitive criticality

## Candidate claim before search

A broad claim such as “distance to a viability boundary is a new resilience measure” was tested and **falsified**.

## High-relevance prior art found

1. Deffuant/Mathias viability-resilience lineage: geometric robustness using distance to the viability-kernel boundary already exists; published material explicitly uses distance maps and minimal sensitive disturbances.

2. *Viability and Resilience of Languages in Competition* (PLOS ONE, 2010) uses proximity to the viability-kernel boundary to guide control and discusses distance-to-boundary behavior.

3. Viability applications already conduct sensitivity analysis of the kernel with respect to thresholds/model parameters (e.g., epidemiological and ecological applications).

4. Viability theory and reachability literature already studies boundary geometry, robust/safe sets and sensitivity-related questions.

## F2 adjudication

```math
\boxed{\text{Broad N3 is falsified.}}
```

Novelty cannot be:

- distance to a viability boundary;
- geometric robustness of a viability kernel;
- sensitivity analysis of a viability kernel;
- using viability proximity to trigger control.

### Narrowed N3 candidate

The unresolved object is much more specific:

```math
\boxed{
N_3^{\prime}:
S_{ij}^{\mathcal V}
=-\frac{\partial}{\partial w_{ij}}
\rho_g(Y),
\qquad
\rho_g(Y)=d_{g_\psi}(Y,\partial\mathcal V_{\rm sus})
}
```

with all of the following required:

1. `w_ij` is a mechanistically/evidence-defined infrastructure-interface parameter, not a generic state coordinate;
2. `g_psi` is justified rather than decorative;
3. nondifferentiable cases use a justified generalized derivative/finite perturbation definition;
4. ranking is benchmarked against degree, betweenness, flow/load, static dependency, and conventional criticality baselines;
5. equal intervention budgets are used;
6. the ranking is tested by actual perturbation/intervention effects on viability/service outcomes.

**Status:** `UNRESOLVED_GLOBAL`; authenticated search required.

---

# 2. Provisional novelty subtraction after public falsification

The public search materially narrows the thesis contribution set:

```math
\boxed{
\mathcal C_{\rm proposed}^{broad}
-\mathcal C_{\rm prior\,art}^{public}
=\{N_1',N_2',N_3'\}_{\rm unresolved}.
}
```

The thesis must **not** claim novelty for dynamic interdependency, stochastic viability, or distance-to-viability-boundary concepts in isolation.

# 3. Search provenance

Representative public-web query families executed on 2026-09-16:

### F0
- `"interdependent infrastructure" dynamic causal dependency delay mechanism coupling model`
- `"multilayer infrastructure" causal interdependency dynamic model delays`
- `"infrastructure interdependency" functional dependency dynamic coupling delay`
- `"interdependent infrastructure" "hybrid system" resilience`

### F1
- `"stochastic viability" infrastructure resilience`
- `"viability kernel" infrastructure resilience power transportation`
- `"Bayesian" "viability kernel" state estimation uncertainty`
- `"probabilistic viability" "viability kernel" uncertainty`

### F2
- `"distance to viability boundary" criticality`
- `"viability kernel" sensitivity criticality network`
- `"viability margin" infrastructure resilience`
- `"distance to boundary" viability control resilience`
- `"viability kernel" sensitivity parameter derivative`
- `"distance to viability kernel boundary" resilience`
- `"network criticality" viability infrastructure`

# 4. Formal-search blocker

The frozen evidence protocol requires authenticated execution in Scopus, Web of Science Core Collection, Compendex and/or IEEE Xplore where specified. Those authenticated searches were not executed in this public-web run.

Therefore Tasks F0/F1/F2 are **not PASS for global novelty**. Public falsification succeeded in narrowing the claims, but formal closure remains:

```math
\boxed{
F0=F1=F2=\texttt{BLOCKED_EXTERNAL_ACCESS}
\quad\text{for novelty certification.}
}
```

This block prevents freezing the final novelty boundary but does not invalidate the narrower working hypotheses above.
