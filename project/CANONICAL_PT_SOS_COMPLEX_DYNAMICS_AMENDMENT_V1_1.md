# Canonical Power–Transportation SoS and Complex-Dynamics Amendment v1.1

**Date:** 2026-09-19  
**Status:** CANONICAL NARROW AMENDMENT — SYSTEM/INTERDEPENDENCY INTERPRETATION  
**Parent authorities:** `CANONICAL_SYSTEM_DEFINITION.md`; `CANONICAL_DEPENDENCY_CONTRACT_V1.md`; `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Evidence basis:** Hall et al. (2016); Ibáñez et al. (2010)  
**Empirical effect:** none.

## 1. Purpose

This amendment makes the thesis's Power–Transportation interpretation explicitly consistent with two established foundations:

1. infrastructure should be interpreted through the **services produced by coordinated systems**, not as an asset inventory alone;
2. energy/power and transportation should remain **separate constituent systems** whose interactions are modeled explicitly rather than homogenizing their native physics.

It does not reopen RQ1–RQ7, H1–H5, the seven-stage architecture, or the canonical dependency primitive.

## 2. Typed physical SoS

The four-domain shorthand remains

```math
\mathcal S=\{P,T,I,O\},
```

but it must not be interpreted as four physically equivalent constituent infrastructures.

For explicit SoS reasoning use

```math
\boxed{
\mathscr S_{PT}
=
(\mathcal S_P,\mathcal S_T,\mathbb I_{P\to T},\mathbb I_{T\to P})
}
```

where \(\mathcal S_P\) and \(\mathcal S_T\) retain independent physical laws, topology, operators, controls, failure modes and service semantics. Information and Organization remain supporting domains unless a declared experiment promotes a specific information/organizational infrastructure to explicit physical-network status.

Permanent:

```math
\boxed{
\text{SoS architecture}
\neq
\text{homogeneous network model}.
}
```

## 3. Service-centered interpretation

Power and Transportation matter because they provide services.

```math
\boxed{
\mathbf Q_{PT}(t)
=
\begin{bmatrix}
Q_P(t)\\
Q_T(t)
\end{bmatrix}.
}
```

Therefore

```math
\boxed{
\text{topology}
\neq
\text{physics}
\neq
\text{service}
\neq
\text{resilience}.
}
```

A graph-theoretic change is not by itself a service-loss or resilience result.

## 4. Transportation representation

For mechanism reasoning, Transportation may be decomposed conceptually as

```math
\boxed{
T=(G_T,F_T,D_T,C_T),
}
```

where:

- \(G_T\): physical transportation infrastructure/topology;
- \(F_T\): fleet, vehicles, repair crews or other mobile agents;
- \(D_T\): passenger/freight/OD/service demand;
- \(C_T\): traffic/operational control.

This is an ontology decomposition, not a universal state vector. Stage 3 determines which quantities are states, algebraic variables, inputs, parameters or outputs for the selected model family.

For repair-access reasoning:

```math
\boxed{
\text{road existence}
\neq
\text{repair accessibility}.
}
```

A defensible recovery-access mechanism may require road state, traffic state, route feasibility, mobile-resource state and task/access requirements.

## 5. Directed interaction is primary

```math
P\to T
\neq
T\to P.
```

Reciprocal interdependency exists only when both directed mechanisms are independently qualified in the declared case. They may differ in mechanism, units, sign, delay, timescale, uncertainty and dynamic state dimension.

## 6. Interaction role is multi-level

Ibáñez et al. motivate three interpretation roles:

```math
\boxed{
\kappa_e^{role}
\in
\{\mathrm{OPERATION},\mathrm{RECOVERY},\mathrm{PLANNING}\}.
}
```

These are **derived metadata**, not new dependency primitives.

- OPERATION: current service/flow/control interaction;
- RECOVERY: one system conditions restoration/support of another;
- PLANNING: capacity/investment/long-term configuration interaction.

The thesis's H1 physical dynamic core prioritizes OPERATION and qualified RECOVERY mechanisms. PLANNING coupling enters later intervention/transformation analysis unless explicitly activated by a research question.

## 7. Interdependency consequences are not binary by default

A dependency may transmit or alter one or more of:

```text
capacity
flow
demand
delay
accessibility
service
recovery
cost
other declared quantity
```

Therefore a binary edge/failure variable is used only when mechanism physics and context justify it.

## 8. Coupling sign is not fixed

```math
\boxed{
\text{dependency}
\neq
\text{vulnerability}.
}
```

Electrified transport may increase power demand, reduce mobility when power is unavailable, or provide support through qualified bidirectional/mobile-energy mechanisms. The sign of the resilience consequence is therefore scenario-, control-, state- and mechanism-dependent.

No thesis result may assume

```math
\text{stronger coupling}\Rightarrow\text{lower resilience}.
```

## 9. Architecture-to-dynamics bridge

The controlled chain is

```math
\boxed{
\mathscr S_{PT}
\rightarrow
\mathbb I^{qualified}
\rightarrow
\mathbb I_3^{ready}
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y^{phys}(t)
\rightarrow
\mathbf Q_{PT}(t)
\rightarrow
\mathfrak R_T.
}
```

The graph identifies structural possibilities. Stage 2 qualifies mechanisms. Stage 3 determines time evolution. Stage 5 evaluates remain/return/confidence.

## 10. Novelty firewall

The thesis does **not** claim novelty for:

- infrastructure SoS reasoning;
- P–T / energy–transport interdependence;
- separate-but-coupled energy and transport networks;
- EV charging/V2G as interaction families;
- integrated long-term energy–transport planning;
- network-flow, optimization, contingency or sensitivity analysis by themselves.

Candidate novelty must be stated only for the specific evidence-qualified, readiness-gated and validated integration actually demonstrated by the thesis.

## 11. Evidence boundary

Hall et al. (2016) support service-centered infrastructure and SoS reasoning. Ibáñez et al. (2010) support explicit energy–transport operational/investment coupling and separate network representation. Neither source by itself establishes the thesis Stage-2 causal gate, Stage-3 hybrid law, Stage-5 viability geometry, or a novelty claim.

## References

Hall, J. W., Nicholls, R. J., Hickford, A. J., & Tran, M. (2016). Introducing national infrastructure assessment. In J. W. Hall, M. Tran, A. J. Hickford, & R. J. Nicholls (Eds.), *The Future of National Infrastructure: A System-of-Systems Approach* (pp. 3–11). Cambridge University Press. https://doi.org/10.1017/CBO9781107588745.002

Ibáñez, E., Gkritza, K., McCalley, J., Aliprantis, D., Brown, R., Somani, A., & Wang, L. (2010). Interdependencies between energy and transportation systems for national long term planning. In *Sustainable and Resilient Critical Infrastructure Systems: Simulation, Modeling, and Intelligent Engineering* (pp. 53–76). Springer. https://doi.org/10.1007/978-3-642-11405-2_2
