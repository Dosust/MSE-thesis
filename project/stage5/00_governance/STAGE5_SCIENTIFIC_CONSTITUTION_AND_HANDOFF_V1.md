# Stage 5 Scientific Constitution and Handoff v1

**Stage:** 5 — Uncertainty-Aware Viability and Reachability Resilience  
**RQ5:** Under what conditions can critical coupled services remain acceptable or recover under feasible controls and uncertainty, and what additional engineering information do viability and reachability provide?  
**SO5:** Determine uncertainty-aware service viability and recovery reachability, evaluate incremental value beyond conventional performance/recovery curves, and characterize interface criticality as a supporting diagnostic.  
**Evidence obligation:** H3.

## Governing rule

\[
Q_5 \rightarrow \mathcal C_5 \rightarrow \mathcal R_5(D) \rightarrow G_5 \rightarrow Z_5 \rightarrow \Lambda_5 \rightarrow I_{5\to6}.
\]

Available data instantiate and test Stage 5; they do not define what Stage 5 scientifically means.

## Upstream contract

\[
I_{4\to5}(t)=
\left(
b_t,\mathbb U_{\widehat Y,t},\mathcal I_t,z_I(t),z_O(t),\mathcal U_{\rm feas}(t)
\right).
\]

Permanent distinctions:

\[
Y_t^{phys}\neq \widehat Y_t\neq b_t,
\qquad
\mathcal U_{\rm phys}\neq\mathcal U_{\rm feas}\ \text{in general}.
\]

Stage 5 may use only physical mechanisms qualified upstream. It may not invent a new \(P\leftrightarrow T\) mechanism because a resilience calculation appears sensitive to it.

## Canonical constitution

\[
\boxed{
\mathcal C_5=
\left(
I_{4\to5},
x_R,
\mathcal K_{\rm req},
K,
G_{\rm rec},
F_{\rm unsafe},
T,
\mathbb U_5,
R_{\rm curve},
\mathcal V,
\mathcal R,
\mathfrak R_T,
\mathcal D_R
\right)
}
\]

with \(x_R=\Pi_R(Y^{phys})\).

## Scientific interpretation

- **Remain**: controlled viability.
- **Return**: controlled reachability/reach-avoid.
- **Confidence**: robust guarantee, scenario coverage, or probability only when justified.
- **Baseline**: conventional performance/recovery curve.
- **Contribution tested by H3**: whether viability–reachability adds predictive or decision-relevant engineering information beyond the conventional baseline.

The thesis does **not** claim to invent viability/reachability theory and does **not** assume superiority over conventional resilience metrics.
