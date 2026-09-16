# Public Novelty Falsification F0/F1/F2 v2.0

**Date:** 2026-09-16  
**Status:** PUBLIC-WEB FALSIFICATION / FORMAL DATABASE CLOSURE BLOCKED  
**Supersedes for active interpretation:** `PUBLIC_NOVELTY_FALSIFICATION_F0_F1_F2_V1.md`  
**Canonical dependency authority:** `project/CANONICAL_DEPENDENCY_CONTRACT_V1.md`

## 1. Purpose and rule

```math
\boxed{\text{Search for the closest prior art first; narrow the claim rather than defend it.}}
```

Public discovery can falsify broad novelty. It cannot certify global novelty. Final novelty closure still requires the formal Scopus/Web of Science/Compendex/IEEE execution defined by the thesis evidence protocol.

---

# F0 — mechanistic dependency/interdependency representation

## Broad claim tested

> Dynamic or causal infrastructure interdependency modeling is novel.

### Adjudication

```math
\boxed{\text{FALSIFIED}.}
```

Relevant prior art already includes dynamic and disequilibrium interdependent-infrastructure models, bidirectional functional dependencies, cascading propagation, synthetic-network/interdependency integration, and multiple infrastructure-modeling paradigms.

Representative anchors include:

- Zhang & Peeta (2014), *Dynamic and disequilibrium analysis of interdependent infrastructure systems*, Transportation Research Part B 67:357–381, DOI `10.1016/j.trb.2014.04.008`.
- Ouyang (2014), *Review on modeling and simulation of interdependent critical infrastructure systems*, Reliability Engineering & System Safety 121:43–60, DOI `10.1016/j.ress.2013.06.040`.
- ASU RISE/REFIT/PSI-Cascade and Hoff & Chester synthetic-network/interdependency/cascade work.

## Canonically reconciled residual N1'

The active thesis dependency object is

```math
\boxed{\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)}
```

with

```math
\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e),
```

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e),
```

```math
\Pi_e=(\mathcal P_e,V_e,\mathcal U_e).
```

Therefore the unresolved candidate is not a new tuple per se. It is:

```math
\boxed{
N_1':
\text{evidence-qualified typed interfaces}
\rightarrow
\text{explicit causal semantics}
\rightarrow
\text{executable heterogeneous }P\!\!-\!T\!\!-\!I\!\!-\!O\text{ dynamics}
\rightarrow
\text{matched ablation/validation}.
}
```

This remains `UNRESOLVED_GLOBAL`. The canonical contract is an internal thesis decision, not a certified global invention.

---

# F1 — partial observation / uncertainty to viability

## Broad claims tested

> Stochastic viability is novel.  
> Using state-estimation uncertainty in safety/viability control is novel.  
> Belief/posterior states linked to constrained safe operation are novel.

### Adjudication

```math
\boxed{\text{FALSIFIED}.}
```

Prior art includes:

- Doyen & De Lara (2010), *Stochastic viability and dynamic programming*, Systems & Control Letters 59(10):629–634, DOI `10.1016/j.sysconle.2010.07.008`.
- Jahanshahi, Jagtap & Zamani (2020), *Synthesis of Stochastic Systems with Partial Information via Control Barrier Functions*, DOI `10.1016/j.ifacol.2020.12.187`.
- Clark (2021), *Control barrier functions for stochastic systems*, Automatica 130, 109688, DOI `10.1016/j.automatica.2021.109688`, including incomplete-information systems with state estimation and probabilistic safety bounds.
- *Conformal Prediction in the Loop: Risk-Aware Control Barrier Functions for Stochastic Systems With Data-Driven State Estimators* (IEEE Control Systems Letters, 2025), DOI `10.1109/LCSYS.2025.3571828`.
- Vahs, Verhagen & Tumova (2026), *Safety-critical Control Under Partial Observability: Reach-Avoid POMDP meets Belief Space Control*, arXiv:2603.10572.
- Jahanshahi & Chen (2026), *Control Barrier–Value Functions under Partial Observability: Safety Guarantees via Conformal Prediction*, arXiv:2608.13819.

Thus even the abstract chain

```math
D_{0:t}\rightarrow p(Y_t\mid D_{0:t})\rightarrow\text{safe/viable decision}
```

is not globally novel in control theory.

## Narrower residual N2'

The thesis-specific unresolved question is:

```math
\boxed{
N_2':
\text{heterogeneous }P,T,I,O\text{ observations}
\rightarrow
b_t(Y)
\rightarrow
\text{validated coupled infrastructure prediction}
\rightarrow
\mathcal U(z_I,z_O)
\rightarrow
K_{\rm sus}
\rightarrow
\mathcal V_{\rm sus}
\rightarrow
\text{decision diagnostics}.
}
```

A minimum derived diagnostic is posterior viable mass

```math
\pi_{\mathcal V,t}
=
\Pr(Y_t\in\mathcal V_{\rm sus}\mid D_{0:t}),
```

but neither this probability nor belief-space safety is claimed as mathematically novel in isolation.

The unresolved contribution, if any, is the **validated infrastructure-specific composition** and its demonstrated decision value relative to point-estimate/physical-only baselines.

Status: `UNRESOLVED_GLOBAL`.

---

# F2 — viability geometry and interface criticality

## Broad claims tested

> Distance to the viability-kernel boundary is novel.  
> Geometric robustness of viability is novel.  
> Parameter sensitivity of a viability kernel is novel.

### Adjudication

```math
\boxed{\text{FALSIFIED}.}
```

Relevant prior art includes:

- Alvarez & Martin (2011), *Geometric Robustness of Viability Kernels and Resilience Basins*, in *Viability and Resilience of Complex Systems*.
- Alvarez, Martin and related work on robustness maps / sensitive disturbances.
- *Anticipating Shocks in the State Space: Characterizing Robustness and Building Increasingly Robust Evolutions*, SIAM Journal on Control and Optimization, DOI `10.1137/16M1061175`.
- application literature that performs viability-kernel sensitivity to thresholds/model parameters.

Therefore neither

```math
\rho(Y)=d(Y,\partial\mathcal V)
```

nor generic sensitivity of `V` can be claimed as original.

## Canonically reconciled residual N3'

Because the canonical dependency contract does not define a universal primitive `w_e`, the active candidate is not `partial rho / partial w_e`.

Let

```math
\Theta
=(\vartheta_P,\vartheta_T,\{\Sigma_e\},\Theta_I,\Theta_O),
```

and

```math
\rho_g(Y;\Theta)
=
d_g(Y,\partial\mathcal V_{\rm sus}(\Theta)).
```

For a differentiable mechanism parameterization, the local diagnostic is

```math
\boxed{
S_{e,v}^{\mathcal V}(Y)
=
- D_{\theta_e}\rho_g(Y;\Theta)[v].
}
```

For nonsmooth/hybrid mechanisms use finite perturbation or actual intervention contrasts.

The unresolved candidate is therefore:

```math
\boxed{
N_3':
\text{canonical infrastructure dependency perturbation}
\rightarrow
\Delta\mathcal M_{\mathcal V}
\rightarrow
\text{interface ranking}
\rightarrow
\text{matched intervention validation}.
}
```

The ranking must be compared under equal budgets against simpler degree, betweenness, flow/load, static-dependency and other justified baselines.

Status: `UNRESOLVED_GLOBAL`.

---

# 2. Second-pass subtraction

After the second public falsification pass:

```math
\boxed{
\mathcal C_{broad}
-
\mathcal C_{prior\,art}^{public}
=
\{N_1',N_2',N_3'\}_{UNRESOLVED\_GLOBAL}.
}
```

The residuals are integration-and-validation claims, not claims that their constituent mathematical ideas are unprecedented.

# 3. Search provenance added in v2

Additional query families executed 2026-09-16 included:

### F0
- `typed directed interface causal infrastructure dependency provenance uncertainty hybrid systems interdependency`
- `infrastructure dependency provenance causal interface model uncertainty`
- `functional dependency infrastructure hybrid causal operator delay uncertainty`

### F1
- `partial observability viability kernel posterior belief safety infrastructure`
- `belief space viability kernel partial observation safety control`
- `state estimation viability kernel infrastructure`
- `belief control barrier function partial observability`
- `observer-based probabilistic safety controller synthesis partial observation`

### F2
- `viability kernel sensitivity parameter derivative robustness control`
- `directional derivative viability kernel parameter`
- `viability kernel sensitivity infrastructure network`
- `distance to viability kernel boundary parameter sensitivity`

# 4. Formal-search blocker

Authenticated execution of the frozen Scopus/Web of Science/Compendex/IEEE protocols remains unavailable in this active runtime.

Therefore:

```math
\boxed{
G_A=\texttt{BLOCKED\_EXTERNAL\_ACCESS}
}
```

for **global novelty certification**.

The public search is sufficient to reject the broad claims and to narrow the research program, but not to declare N1', N2' or N3' globally novel.
