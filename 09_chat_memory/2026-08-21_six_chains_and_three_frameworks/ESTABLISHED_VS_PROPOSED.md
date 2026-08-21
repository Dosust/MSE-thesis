# Established Literature vs Candidate Thesis Contribution

This is the anti-overclaim checkpoint for future chats.

| Scientific element | Status represented in project | Safe thesis role |
|---|---|---|
| Sector conservation/flow physics | established | choose/reduce/assemble sector models |
| Graph/multilayer representation | established | build infrastructure-specific representation |
| Infrastructure interdependency concepts | established | define mechanism-specific dynamic interfaces |
| Cascading-failure models | established | compare dynamic-interface failure mechanisms |
| Dynamic/transient cascade effects | established | study effect on viability for selected system |
| State estimation/system identification | established | apply/extend to selected interface model |
| Bayesian inverse problems | established | quantify interface uncertainty |
| Bayesian ICI topology reconstruction | already exists | **do not claim first hidden-interface inference** |
| Fragility/hazard-damage relations | established | forcing/failure layer |
| Resilience performance metrics | established | distinguish from viability geometry |
| Viability kernels/capture basins | established mathematics | apply rigorously |
| HJ/HJI reachability | established mathematics | solve/approximate selected viability problem |
| HJ viability in infrastructure | already exists | **do not claim first infrastructure HJ viability** |
| Recovery/restoration optimization | mature | comparison/downstream control |
| Sustainability-resilience integration | exists | encode sustainability constraints |
| Equity-aware resilience | exists | encode service-floor/disparity constraints |
| Multiobjective design/decision | exists | downstream implications if scope permits |

## Current candidate intersection

\[
\boxed{
\mathcal D_{\rm obs}
\rightarrow
(\hat G,\hat\theta,\Sigma_\theta)
\rightarrow
M(t)
\rightarrow
F_{\rm dyn}
\rightarrow
\mathcal V_{\rm sus,eq}
}
\]

The candidate contribution is the rigorous connection between:

1. dynamic interface identifiability;
2. interface/system timescale separation;
3. parameter/topology uncertainty;
4. viability and recoverability geometry;
5. sustainability/equity admissibility;
6. a P–W–T–SW urban-flood demonstrator.

Candidate objects:

\[
E_{\rm inv}=d_H[\mathcal V(\theta^*),\mathcal V(\hat\theta)]
\]

\[
\Pi_M=\frac{\tau_{\rm interface}}{\tau_{\rm system/hazard}}
\]

\[
E_{\rm qs}(\Pi_M)=d_H[\mathcal V_{\rm dyn},\mathcal V_{\rm qs}]
\]

\[
S_j^{\mathcal V}
=
\lim_{\delta\to0}
\frac{d_H[\mathcal V(\theta),\mathcal V(\theta+\delta e_j)]}{|\delta|}.
\]

Possible reduction theorem target retained from project work:

\[
\mathcal V_{\rm red}\subseteq\Pi(\mathcal V_{\rm full})
\]

or

\[
d_H[\mathcal V_{\rm red},\Pi(\mathcal V_{\rm full})]\le\varepsilon_R.
\]

Generic HJ decomposition/reduction precedents exist, so any final theorem must be infrastructure-specific and its assumptions must be explicit.

## Novelty status

**Candidate only; global novelty is not frozen.** Absence from an audited subset is not proof of absence from the global literature.
