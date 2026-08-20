# Scientific Propositions and Falsification Plan

The thesis is organized around propositions that can be tested, rejected, bounded, or qualified. These are not claims of truth before analysis.

| ID | Proposition | Mathematical object | Primary falsification / stress test |
|---|---|---|---|
| **P1** | Dynamic interfaces materially alter resilience geometry relative to static coupling. | $\mathcal V(Z(t))$ vs. $\mathcal V(\bar Z)$ | Compute $\Delta_{\mathcal V}=d_H(\mathcal V_{dyn},\mathcal V_{static})$ and test whether deformation is negligible under prespecified tolerances. |
| **P2** | Interface identifiability materially affects reliability of inferred viability. | $p(\theta,G,Z\mid\mathcal D)$ and $\mathcal V(\widehat\theta)$ | Propagate posterior/parameter uncertainty into viability-set uncertainty; compare against truth/synthetic benchmark where available. |
| **P3** | Interface/system timescale ratios govern the validity of static approximations. | $\rho_{ij}=\tau_{interface,ij}/\tau_{system}$ | Sweep $\rho_{ij}$ and compare state and boundary errors across fast, commensurate, and slow interface regimes. |
| **P4** | Sustainability and equity constraints deform the viable region beyond technical-operability constraints alone. | $K_{tech}$ vs. $K_{sus,eq}$ | Compare $\mathcal V(K_{tech})$ and $\mathcal V(K_{sus,eq})$ using boundary distance, volume/measure, and critical-state changes. |
| **P5** | Recovery geometry contains information not captured by viability alone. | $\mathcal V_R$, $\mathcal C_R$, $\tau_R$ | Identify states outside $\mathcal V_R$ that are in $\mathcal C_R$ and quantify recovery-time structure. |
| **P6** | Waste–drainage–flood feedback shifts coupled P–W–T–SW resilience boundaries. | $X_{SW}\to B_{drain}\to\eta_{flood}\to X$ | Compare otherwise identical models with and without the feedback loop; quantify service, boundary, and recovery changes. |
| **P7** | Reduced models used for decision-making must preserve or conservatively bound viability conclusions. | $\mathcal V_r$ vs. $\Pi(\mathcal V)$ | Compute approximation error and test whether reduced-model safe sets are conservative under a declared error criterion. |

## Decision discipline

A proposition is considered **supported under the tested model and data** only when:

1. the mathematical comparison is predeclared;
2. numerical tolerances are reported;
3. uncertainty is quantified where applicable;
4. alternative parameterizations/sensitivity checks do not reverse the conclusion without explanation;
5. the scope of inference is explicitly limited to the model, demonstrator, and evidence actually analyzed.

## Non-claims

The project does **not** infer global novelty from PRISMA counts, Monte Carlo paper rankings, or repository completeness. Literature ranking and mathematical falsification are separate evidence layers.
