# Stage 5 H3 Experiment Protocol v1

## H3

For the declared P–T test domain, the combined uncertainty-aware viability–reachability object must provide measurable incremental predictive or decision-relevant information beyond prespecified conventional performance/recovery-curve metrics.

## Primary confirmatory comparison

\[
A_0=R_{\rm curve}
\]

versus

\[
A_4=R_{\rm curve}+\mathfrak R_T.
\]

## Diagnostic ablations

\[
\begin{aligned}
A_1&=R_{\rm curve}+\mathcal V,\\
A_2&=R_{\rm curve}+\mathcal R,\\
A_3&=R_{\rm curve}+\mathcal V+\mathcal R,\\
A_4&=R_{\rm curve}+\mathfrak R_T.
\end{aligned}
\]

## Matched conditions

Freeze and share across arms:

\[
\mathcal G,\ 
\mathbb I^{qualified},\
F_{\mathcal G}^{m},\
Y_0,\
\eta,\
\mathcal U_{\rm feas},\
K,\
T,\
ScenarioID.
\]

Use common random numbers where stochastic simulation permits.

## Outcomes

Remain event:
\[
Z^{remain}=1[\text{service remains in }K\text{ over the horizon}].
\]

Recovery event:
\[
Z^{recover}=1[\tau_{G_{\rm rec}}\le T\text{ without forbidden-set violation}].
\]

## Predictive incremental information

\[
\Delta Skill=
Skill(A_4)-Skill(A_0).
\]

Use a preregistered proper probabilistic score when outputs are probabilities; use preregistered classification/regression metrics otherwise.

## Decision value

\[
\Delta V_{\rm decision}
=
V_{\rm decision}(A_4)-V_{\rm decision}(A_0).
\]

Stage 5 tests decision information; strategic intervention optimization remains Stage 6/7.

## Falsification

H3 is not supported in the declared domain if the augmented representation fails to meet the preregistered meaningful incremental-information criterion under the frozen evaluation protocol.

No effect threshold is invented in this v1; it must be set from pilot/reference performance and engineering significance before confirmatory execution.
