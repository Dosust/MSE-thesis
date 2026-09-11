<!--
DOCUMENT STATUS: CURRENT ENGINEERING CONFIRMATORY HYPOTHESIS MATRIX
SOURCE: user-supplied Pasted markdown(20260911-042927).md
SOURCE_SHA256: f24104a8be55b1f5d42b4087e32df636c72afb04ed5c3e1677ec26a5b7eef271
PRESERVATION RULE: scientific claims, methodological logic, citations, thresholds policy, and references are preserved from the supplied source.
DISPLAY-ONLY NORMALIZATION: malformed Markdown table headers/separators repaired; equation tags moved to Markdown labels to comply with repository GitHub rendering rules.
FREEZE BOUNDARY: hypothesis structure is usable for operationalization; numerical delta_1...delta_5, exact Omega_H, and final analysis procedures remain unfrozen as stated in the source.
-->

Yes. We can now build the **Engineering Confirmatory Hypothesis Matrix** for the thesis.

The matrix below combines four methodological requirements:

```math
\boxed{ \text{confirmatory science} + \text{systems engineering} + \text{physics-based modelling} + \text{VVUQ} }
```

ISO/IEC/IEEE 15288:2023 provides the systems and systems-of-systems life-cycle frame, while ISO/IEC/IEEE 29148:2018 provides requirements and traceability discipline (ISO/IEC/IEEE, 2023, 2018). ([ISO](https://www.iso.org/standard/81702.html "ISO/IEC/IEEE 15288:2023 - Systems and software engineering — System life cycle processes")) NASA-STD-7009B requires modeling and simulation credibility to be judged against intended use and explicit acceptance criteria, and ASME VVUQ emphasizes communicating verification, validation, and uncertainty evidence relative to context of use (NASA, 2024; ASME, 2022). ([Standards](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf?utm_source=chatgpt.com "NASA-STD-7009B")) IEEE 1012-2024 similarly separates conformity to requirements from satisfaction of intended use (IEEE, 2024). ([IEEE Standards Association](https://standards.ieee.org/ieee/1012/7324/?utm_source=chatgpt.com "IEEE SA - IEEE 1012-2024"))

For the confirmatory-science side, Henderson and Chambers (2022) recommend defining hypotheses and analyses prospectively; Dienes (2024) goes further by requiring the crucial test, auxiliary assumptions, outcome-neutral checks, and the ability of the design to provide evidence against an effect as well as for it. Lakens (2022) emphasizes that study informativeness and meaningful effect sizes should be justified from the actual inferential goal rather than chosen mechanically. ([PLOS](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1010571\&utm_source=chatgpt.com "Ten simple rules for writing a Registered Report | PLOS Computational Biology"))

# Engineering Confirmatory Hypothesis Matrix

## Matrix A — Scientific specification

| Specification | H1 — Dynamic interdependency | H2 — Information–organization | H3 — Controlled viability | H4 — Interface criticality | H5 — Adaptive transformation |
|---|---|---|---|---|---|
| **Scientific gap** **`G_i`** | It remains unclear how much explicit state/time/mode-dependent `P\leftrightarrow T` coupling changes propagation relative to independent or static-coupling representations. | Physical-only infrastructure models can omit information degradation and organizational feasibility even though these determine what operators know and can execute. | Conventional resilience trajectories quantify service degradation/recovery but do not necessarily reveal whether acceptable future operation remains controllably maintainable. | Static centrality identifies structurally important components but may not identify interfaces whose perturbation most changes system viability. | A fixed intervention plan may be vulnerable to deep uncertainty; the added value of adaptive trigger-based transformation must be demonstrated. |
| **Scientific premise** **`T_i`** | Interdependent-network physics shows that coupling structure can qualitatively alter cascade behavior; topology and dynamics cannot generally be separated (Buldyrev et al., 2010; Gates & Rocha, 2016). | Infrastructure resilience depends on physical, information, organizational and coordination processes, not physical topology alone (Li et al., 2019; Mohebbi et al., 2020). | Viability theory distinguishes currently acceptable states from states from which constraints can continue to be satisfied under admissible control (Béné & Doyen, 2018). | Network importance is mechanism- and dynamics-dependent; connectivity/centrality alone cannot certify resilience (Kaiser et al., 2021; Gates & Rocha, 2016). | DAPP/RDM preserve alternatives and modify action as uncertain futures unfold rather than optimizing one forecast (Haasnoot et al., 2013; Hadka et al., 2015). |
| **Mechanism** **`M_i`** | `\mathfrak I\rightarrow F_{\mathcal G}\rightarrow` altered propagation paths/times `\rightarrow` altered service trajectory. | `I\rightarrow\hat X\rightarrow O\rightarrow\mathcal U\rightarrow u\rightarrow Y`. | `Y\rightarrow\mathcal V\rightarrow(\rho,T_{\mathcal V},T_K)\rightarrow` information about future maintainability. | `\theta_{ij}\rightarrow F\rightarrow\mathcal V\rightarrow` marginal intervention benefit. | observation `\rightarrow` signpost `\rightarrow` trigger `\rightarrow a_k\rightarrow\mathcal M_{k+1}`. |
| **Confirmatory hypothesis** | **Under the prespecified disturbance/domain, explicit dynamic causal interdependency modeling will produce materially different and more benchmark-consistent propagation/service trajectories than independent or static-coupling models.** | **Information degradation and organizational constraints will materially alter feasible response, response timing, and recovery outcomes relative to models assuming perfect information and unconstrained organization.** | **Viability-based quantities will provide material prognostic information about impending loss of maintainability beyond conventional instantaneous service/recovery indicators.** | **Interventions selected using viability-based interface criticality will improve controlled viability more than equal-resource interventions selected using static structural rankings.** | **Across prespecified deeply uncertain futures, an adaptive trigger-based transformation policy will achieve a materially stronger robust resilience–sustainability–equity trade-off than the best comparable fixed pathway.** |
| **Primary** **`X_i`** | Coupling representation: independent/static/dynamic causal. | `I,O` condition: perfect versus degraded/constrained. | Predictor set: conventional metrics versus conventional + viability metrics. | Interface-ranking method. | Pathway policy: fixed versus adaptive. |
| **Primary** **`Y_i`** | `T_C`, cascade extent, service loss, propagation/recovery trajectory. | `\tau_{\rm response}`, `\mathcal U`, service loss, recovery time, viability. | future viability loss/constraint violation and warning lead time. | `\Delta\mathcal V,\Delta\rho,\Delta T_{\mathcal V}`, service improvement. | robust multiobjective performance across `\Omega`. |
| **Estimand** **`\Delta_i`** | `\Delta_1=D(Z_{\rm dyn},Z_{\rm baseline})` plus benchmark-error difference. | `\Delta_2=Z_{PTIO}-Z_{PT}`, decomposed through nested models. | `\Delta_3=\operatorname{Skill}(Q_C+Q_V)-\operatorname{Skill}(Q_C)`. | `\Delta_4=G_{\mathcal V}(R_V)-G_{\mathcal V}(R_{\rm structural})`. | `\Delta_5=\mathcal R(\pi_A)-\mathcal R(\pi_F)`. |
| **Baseline** **`B_i`** | Independent `P+T` and static-coupled `P-T`. | Perfect information + instantaneous/unconstrained organization. | service loss, recovery time, instantaneous performance. | degree, betweenness and preferably flow-based ranking. | best feasible fixed pathway using identical intervention library/resources. |
| **Strong rival** | Static coupling is sufficient; dynamic coupling adds no meaningful explanatory/predictive information. | Physical dynamics dominate, making realistic `I/O` degradation practically negligible. | Ordinary service metrics already contain essentially all useful warning information. | Static flow/centrality already identifies intervention targets as effectively as viability sensitivity. | Flexibility has insufficient value to compensate for trigger delays, coordination cost and added complexity. |

This first matrix already gives us something important: none of the five hypotheses is simply “our proposed method works.” Each has a **credible rival explanation**, which is essential for strong confirmatory inference (Dienes, 2024). ([Cambridge University Press](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-research-methods-and-statistics-for-the-social-and-behavioral-sciences/inner-workings-of-registered-reports/DE817FF7830BC127896A55932DD6F514?utm_source=chatgpt.com "The Inner Workings of Registered Reports (Chapter 14) - The Cambridge Handbook of Research Methods and Statistics for the Social and Behavioral Sciences"))

---

# Matrix B — Domain, context of use, and operationalization

NASA-STD-7009B makes intended use and acceptance criteria central to M&S credibility, while ASME VVUQ 1 emphasizes evidence supporting model application for its specific context of use (NASA, 2024; ASME, 2022). ([Standards](https://standards.nasa.gov/node/263?utm_source=chatgpt.com "Standard for Models and Simulations | Standards")) Therefore each hypothesis gets its own **Context of Use**, rather than declaring the complete model universally valid.

| Specification | H1 | H2 | H3 | H4 | H5 |
|---|---|---|---|---|---|
| **Context of use** **`C_{\rm use}`** | Determine whether explicit interdependency dynamics are necessary to reproduce cascade/service behavior in the reduced `P-T` demonstrator. | Quantify whether realistic `I/O` limitations materially change resilience conclusions. | Determine whether viability quantities improve early identification of future unacceptable trajectories. | Support equal-resource ranking of candidate cross-layer resilience interventions. | Compare transformation strategies across uncertain long-horizon futures. |
| **System of interest** | `P,T` with explicit Stage-2 interfaces. | `P,T,I,O`. | Reduced Stage-5 state `Y_V`. | Selected `P-T-I-O` interfaces. | Alternative regimes `\mathcal M_k` in `\mathbb G_{\rm ST}`. |
| **Hypothesis domain** **`\Omega_H`** | Prespecified topology, demand/loading ranges, one disturbance class, parameter ranges, initial states. | Same physical domain plus prespecified delay, information-quality and organizational-resource ranges. | States/hazards lying within validated reduced-dynamics domain. | Same `\Omega_H`, restricted to physically implementable interface perturbations. | Prespecified scenario ensemble `\Omega`, planning horizon and intervention library. |
| **Validation domain** **`\Omega_V`** | Region where power, transport and coupling models have benchmark/data support. | `\Omega_V^{PT}\cap\Omega_V^I\cap\Omega_V^O`. | Region where reduced dynamics and viability computation have been verified/benchmarked. | Domain over which perturbing `\theta_{ij}` remains physically/model-valid. | Domain covered by validated regime models and plausible transformation scenarios. |
| **Mandatory condition** | `\boxed{\Omega_{H_1}\subseteq\Omega_V}` | `\boxed{\Omega_{H_2}\subseteq\Omega_V}` | `\boxed{\Omega_{H_3}\subseteq\Omega_V}` | `\boxed{\Omega_{H_4}\subseteq\Omega_V}` | Each regime transition must remain inside documented model-use domains or be explicitly classified as extrapolation. |
| **Operational** **`X`** | Switch coupling representation while holding hazard/network/initial conditions fixed. | Manipulate `\delta_I,\Delta_I,e_X,R_O,\tau_O,\ldots` according to prespecified ranges. | Compute `Q_C` and `Q_V` from identical trajectories. | Generate ranking from each method, then implement equal-budget top-`k` interventions. | Execute fixed and trigger-based policies over identical future ensembles. |
| **Operational** **`Y`** | trajectory distance, `T_C`, failure count, service loss, recovery. | response time, estimator error, feasible-control loss, recovery/viability outcomes. | predictive/discrimination score, warning lead time, calibration. | viable-set/margin/time improvement per unit resource. | robustness, regret/satisficing, cost, service, carbon, inequity, flexibility. |

The condition

```math
\boxed{\Omega_H\subseteq\Omega_V}
```

is one of the most important safeguards in the matrix. It prevents us from claiming a hypothesis is tested in regions where the computational model itself has not been shown credible for its intended use.

---

# Matrix C — Quantitative predictions and meaningful effects

Lakens (2022) argues that the amount and precision of evidence collected should follow from the inferential goal and that a smallest effect of interest should be justified rather than mechanically chosen. ([DOI](https://doi.org/10.1525/collabra.33267?utm_source=chatgpt.com "Sample Size Justification | Collabra: Psychology | University of California Press")) We therefore **do not insert arbitrary 10%, 20%, or 30% thresholds now**.

| Hypothesis | Prespecified prediction | Meaningful threshold |
|---|---|---|
| **H1** | `\boxed{\Delta_1\ge\delta_1}`, with the dynamic model also reducing discrepancy against benchmark/observed trajectories relative to simpler models. | `\delta_1`: determined from benchmark error, engineering relevance and numerical uncertainty. |
| **H2** | `\boxed{\Delta_2\ge\delta_2}`, together with the mechanistic prediction `I/O\rightarrow\tau_{\rm response},\mathcal U\rightarrow Y`. | `\delta_2`: meaningful change in service/recovery/viability rather than merely numerical detectability. |
| **H3** | `\boxed{\operatorname{Skill}(Q_C+Q_V)-\operatorname{Skill}(Q_C)\ge\delta_3}`. | `\delta_3`: minimum useful increase in warning/discrimination/predictive value. |
| **H4** | `\boxed{G_{\mathcal V}(R_V)-G_{\mathcal V}(R_S)\ge\delta_4}` under equal intervention resources. | `\delta_4`: minimum decision-relevant improvement in viable margin/set/time. |
| **H5** | `\boxed{\mathcal R(\pi_A)-\mathcal R(\pi_F)\ge\delta_5}` or robust Pareto improvement. | `\delta_5`: minimum policy-relevant robustness benefit after accounting for added flexibility/coordination cost. |

For every `i`,

```math
\boxed{ \delta_i > U_{\mathrm{relevant},i} }
```

should normally hold. A claimed meaningful effect smaller than the model's numerical/parameter/model-form uncertainty floor would be scientifically difficult to interpret.

---

# Matrix D — Physics, verification and validation gates

The hypothesis cannot be evaluated until its model passes credibility gates. IEEE 1012-2024 explicitly treats V&V as assessing both conformance to requirements and satisfaction of intended use, while ASME VVUQ 50.1:2025 embeds V&V throughout the computational-model life cycle (IEEE, 2024; ASME, 2025). ([IEEE Standards Association](https://standards.ieee.org/ieee/1012/7324/?utm_source=chatgpt.com "IEEE SA - IEEE 1012-2024"))

| Gate | H1 | H2 | H3 | H4 | H5 |
|---|---|---|---|---|---|
| **Dimensional consistency** | required | required | required | required | required |
| **Conservation/physics** | power, traffic/vehicle flows | inherited physical laws plus valid `I/O` state transitions | inherited Stage-3/4 laws | recompute transformed dynamics | every transformed `\mathcal M_k` |
| **State bounds** | `V,f,SOC,q,k,\ldots` | plus information/resource bounds | viability-state bounds | intervention cannot create impossible parameters | all regimes/actions feasible |
| **Limiting cases** | `w_{ij}\to0\Rightarrow` uncoupled limit where applicable | perfect `I,O\Rightarrow` baseline model | simple low-dimensional cases against known viability results | `\Delta\theta\to0\Rightarrow\Delta\mathcal V\to0` where continuity applies | fixed-policy special case must be recoverable from adaptive formulation |
| **Code verification** | subsystem + coupling implementation | information/organization modules | viability solver | perturbation/ranking algorithm | pathway/optimizer/policy implementation |
| **Solution verification** | time step/grid/convergence | event synchronization sensitivity | discretization/kernel convergence | perturbation size sensitivity | optimization/scenario convergence |
| **Validation evidence** | physical/subsystem benchmark + coupling benchmark where available | literature/data for communication/decision/resource delays | benchmark against analytically/independently computable viability cases | counterfactual intervention response | historical/plausible scenario logic + validated lower-stage models |
| **Acceptance criterion** | predefined before H1 test | predefined before H2 | predefined before H3 | predefined before H4 | predefined before H5 |

This distinction matters:

```math
\boxed{ \text{code verified} \not\Rightarrow \text{physical model validated} \not\Rightarrow \text{hypothesis supported}. }
```

NASA-STD-7009B specifically requires acceptance criteria and model credibility evidence during development and use rather than treating a simulation result as self-validating (NASA, 2024). ([Standards](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf?utm_source=chatgpt.com "NASA-STD-7009B"))

---

# Matrix E — Critical confirmatory experiments

| `H_i` | Critical experiment |
|---|---|
| **H1** | Run identical initial states, hazard realizations, demand and controls under `M_{\rm independent}`, `M_{\rm static}`, and `M_{\rm dynamic}`. Compare both trajectory differences **and benchmark discrepancy**. Only coupling representation changes. |
| **H2** | Use nested ablation: `M_0=P+T` with perfect information/organization; `M_1=P+T+I`; `M_2=P+T+I+O`. Hold physical network/hazard identical. Quantify both outcome change and mediation through `\hat X,\tau_{\rm response},\mathcal U`. |
| **H3** | Generate states/scenarios with similar instantaneous service performance but different viability margins. Test whether viability quantities discriminate subsequent viability loss/constraint violation better than conventional metrics alone. |
| **H4** | Rank interfaces independently using `S_{ij}^{\mathcal V}`, degree, betweenness and flow-based metrics. Apply the same intervention budget/top-`k` count and compare post-intervention viability outcomes across common scenarios. |
| **H5** | Construct the strongest feasible fixed pathway and an adaptive pathway using the same intervention library and comparable resource constraints. Stress-test both across the identical scenario ensemble `\Omega`. |

Dienes (2024) calls for identifying the **specific crucial test** that actually distinguishes theoretical claims rather than choosing from many analyses after outcomes are known. ([Cambridge University Press](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-research-methods-and-statistics-for-the-social-and-behavioral-sciences/inner-workings-of-registered-reports/DE817FF7830BC127896A55932DD6F514?utm_source=chatgpt.com "The Inner Workings of Registered Reports (Chapter 14) - The Cambridge Handbook of Research Methods and Statistics for the Social and Behavioral Sciences")) These experiments follow that principle.

---

# Matrix F — Auxiliary assumptions and outcome-neutral checks

This is essential. A failed prediction cannot be interpreted as evidence against `H_i` if the apparatus used to test it failed.

| Hypothesis | Important auxiliary assumptions | Outcome-neutral checks before hypothesis interpretation |
|---|---|---|
| **H1** | subsystem models are adequate; coupling mapping is implemented correctly; scenario synchronization is correct | uncoupled benchmark; coupling unit tests; convergence; known limiting cases |
| **H2** | `I/O` variables represent meaningful degradation/resource processes; estimator and scheduling models work | estimator calibration; delay distribution checks; resource conservation; event-order checks |
| **H3** | reduced viability state preserves relevant failure mechanisms; kernel approximation is sufficiently accurate | dimensional reduction test; solver convergence; benchmark viability cases |
| **H4** | interface perturbations are physically meaningful and comparably costed | feasibility audit; equal-budget check; perturbation-size stability |
| **H5** | scenario ensemble is sufficiently diverse; trigger observations are available; intervention lead times/resources are credible | scenario-coverage diagnostics; policy feasibility checks; fixed-policy recovery test; optimization convergence |

This follows the Registered Report principle:

```math
\boxed{ H_i\land A_{i1}\land\cdots\land A_{im} \Rightarrow P_i }
```

rather than pretending that `P_i` follows from `H_i` alone (Dienes, 2024). ([Cambridge University Press](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-research-methods-and-statistics-for-the-social-and-behavioral-sciences/inner-workings-of-registered-reports/DE817FF7830BC127896A55932DD6F514?utm_source=chatgpt.com "The Inner Workings of Registered Reports (Chapter 14) - The Cambridge Handbook of Research Methods and Statistics for the Social and Behavioral Sciences"))

---

# Matrix G — Uncertainty architecture

For engineering use, uncertainty should be decomposed rather than represented by one generic error term:

```math
\boxed{ U_i= \{ U_{\theta}, U_{\mathrm{IC}}, U_h, U_M, U_N, U_D \} }
```

where:

```math
U_\theta=\text{parameter uncertainty}, \quad U_{\mathrm{IC}}=\text{initial-state uncertainty},
```

```math
U_h=\text{hazard/scenario uncertainty}, \quad U_M=\text{model-form uncertainty},
```

```math
U_N=\text{numerical uncertainty}, \quad U_D=\text{data/measurement uncertainty}.
```

| Hypothesis | Dominant uncertainties |
|---|---|
| H1 | coupling parameters `w,\delta,\tau`, hazard realization, model form, time discretization |
| H2 | delay/loss distributions, state-estimation error, organizational resource/decision-time distributions |
| H3 | reduced-state selection, viability approximation, uncertainty in `K_{\rm sus}`, dynamics parameters |
| H4 | perturbation magnitude, cost normalization, viability solver, ranking stability |
| H5 | future scenarios, intervention cost/lead time, institutional feasibility, model structural change |

For deep uncertainty in H5:

```math
\boxed{ \omega\in\Omega }
```

should normally be preferable to imposing unjustified precise probabilities.

---

# Matrix H — Confirmatory decision rules

A result should not be forced into a binary supported/not-supported classification.

Define:

```math
\boxed{ D_i\in \{ \text{consistent}, \text{inconsistent}, \text{inconclusive} \}. }
```

| Decision | General condition |
|---|---|
| **Consistent with** **`H_i`** | effect meets/exceeds `\delta_i`, uncertainty does not erase the effect, mechanistic prediction is also satisfied, and V&V gates pass |
| **Inconsistent with** **`H_i`** | credible effect lies below the prespecified meaningful-effect criterion or follows the rival prediction, while V&V gates pass |
| **Inconclusive** | uncertainty interval spans decision boundaries, model credibility is insufficient, validity checks fail, or scenario coverage is inadequate |

This is more defensible than interpreting every nonsignificant result as “no effect.” Henderson and Chambers (2022) and Dienes (2024) specifically emphasize making null results interpretable and planning analyses before results are observed. ([PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9612468/?utm_source=chatgpt.com "Ten simple rules for writing a Registered Report - PMC"))

---

# Matrix I — Evidence and novelty status

| Hypothesis | Established basis | Thesis-level proposition |
|---|---|---|
| **H1** | interdependency, multilayer networks, topology–dynamics interactions **[E]** | quantitative necessity/value of our dynamic `P-T` mechanism representation **[D/P]** |
| **H2** | cyber/information and organizational effects on resilience **[E]** | integrated `P-T-I-O` causal impact under our architecture **[D/P]** |
| **H3** | viability theory and controlled invariant sets **[E]** | added prognostic value of `\rho,T_{\mathcal V},T_K` in this infrastructure application **[P]** |
| **H4** | network intervention and centrality methods **[E]** | `S_{ij}^{\mathcal V}` as an interface-ranking construct and its superiority test **[P]** |
| **H5** | DAPP, RDM, real options, multiobjective optimization **[E]** | their integration with `P-T-I-O` architecture-space transformation `\mathfrak P_{\rm ST}` **[P]** |

This preserves the discipline already established in the framework:

```math
[E]\neq[D]\neq[P].
```

---

# Final traceability matrix

The final scientific trace for each hypothesis should be stored as:

**HM-1 — Confirmatory hypothesis traceability chain**

```math
\boxed{ G_i \rightarrow T_i \rightarrow M_i \rightarrow H_i \rightarrow P_i \rightarrow Q_i \rightarrow \mathcal M_i \rightarrow V\&V_i \rightarrow U_i \rightarrow C_i \rightarrow D_i. }
```

And our five thesis hypotheses map onto the framework as:

**HM-2 — Mapping of the five hypotheses onto the frozen framework**

```math
\boxed{ \begin{aligned} H_1 &: \mathfrak I \longrightarrow F_{\mathcal G}, \\ H_2 &: (I,O) \longrightarrow (\hat X,\mathcal U,u) \longrightarrow F, \\ H_3 &: (F,\mathcal U) \longrightarrow \mathcal V, \\ H_4 &: \mathfrak I \longrightarrow S_{ij}^{\mathcal V} \longrightarrow \Delta\mathcal V, \\ H_5 &: \mathcal V \longrightarrow \Phi_{\rm ST} \longrightarrow \mathfrak P_{\rm ST} \longrightarrow \mathbb M_{\rm sus}. \end{aligned} }
```

That hierarchy matches the frozen framework: Stage 7 is explicitly linked back through Stages 1–6 rather than acting as an isolated optimization layer. The final framework likewise places `\mathfrak P_{\rm ST}` after the Stage-6 transformation diagnosis while keeping the earlier stages unchanged.

## Qualification rule

I would now adopt one formal thesis rule:

```math
\boxed{ H_i\text{ becomes confirmatory only if } \mathcal Q(H_i)=1 }
```

with

```math
\boxed{ \mathcal Q(H_i) = \bigwedge_{r=1}^{12}Q_{ir} }
```

where the required gates are:

**HM-3 — Twelve confirmatory qualification gates**

```math
\boxed{ \begin{array}{lll} Q_1:&\text{documented knowledge gap},\\ Q_2:&\text{defensible mechanism},\\ Q_3:&\text{defined system/context of use},\\ Q_4:&\text{operational variables and estimand},\\ Q_5:&\text{baseline + strong rival},\\ Q_6:&\Omega_H\subseteq\Omega_V,\\ Q_7:&\text{quantitative prediction},\\ Q_8:&\text{justified }\delta_{\min},\\ Q_9:&\text{physics + verification gates passed},\\ Q_{10}:&\text{validation evidence adequate for context of use},\\ Q_{11}:&\text{uncertainty/robustness plan fixed},\\ Q_{12}:&\text{critical experiment + decision rule prespecified}. \end{array} }
```

The exact 12-gate formulation is **our derived thesis methodology [D/P]**, not an ISO/ASME standard. Its components, however, are traceable to established systems-engineering, M&S credibility, VVUQ, and confirmatory-research principles.

### Core methodological references

American Society of Mechanical Engineers. (2022). *Verification, validation, and uncertainty quantification terminology in computational modeling and simulation (ASME VVUQ 1-2022).* ([ASME](https://www.asme.org/codes-standards/find-codes-standards/verification-validation-and-uncertainty-quantification-terminology-in-computational-modeling-and-simulation?utm_source=chatgpt.com "Verification Validation and Uncertainty Quantification Terminology in Computational Modeling and Simulation - ASME"))

American Society of Mechanical Engineers. (2025). *VVUQ 50.1: Guide to a model life cycle approach that incorporates verification, validation, and uncertainty quantification.* ([ASME](https://www.asme.org/codes-standards/find-codes-standards/vvuq501-vvuq-50-1-guide-to-a-model-life-cycle-approach-that-incorporates-verification-validation-and-uncertainty-quantification?utm_source=chatgpt.com "VVUQ 50.1 Guide to a Model Life Cycle Approach That Incorporates Verification Validation and Uncertainty Quantification - ASME"))

Dienes, Z. (2024). The inner workings of Registered Reports. In J. E. Edlund & A. L. Nichols (Eds.), *The Cambridge handbook of research methods and statistics for the social and behavioral sciences*. Cambridge University Press. ([Cambridge University Press](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-research-methods-and-statistics-for-the-social-and-behavioral-sciences/inner-workings-of-registered-reports/DE817FF7830BC127896A55932DD6F514?utm_source=chatgpt.com "The Inner Workings of Registered Reports (Chapter 14) - The Cambridge Handbook of Research Methods and Statistics for the Social and Behavioral Sciences"))

Henderson, E. L., & Chambers, C. D. (2022). Ten simple rules for writing a Registered Report. *PLOS Computational Biology, 18*(10), e1010571. ([PLOS](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1010571\&utm_source=chatgpt.com "Ten simple rules for writing a Registered Report | PLOS Computational Biology"))

Institute of Electrical and Electronics Engineers. (2024). *IEEE Standard for System, Software, and Hardware Verification and Validation (IEEE 1012-2024).* ([IEEE Standards Association](https://standards.ieee.org/ieee/1012/7324/?utm_source=chatgpt.com "IEEE SA - IEEE 1012-2024"))

International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2023). *Systems and software engineering—System life cycle processes (ISO/IEC/IEEE 15288:2023).* ([ISO](https://www.iso.org/standard/81702.html "ISO/IEC/IEEE 15288:2023 - Systems and software engineering — System life cycle processes"))

International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2018). *Systems and software engineering—Life cycle processes—Requirements engineering (ISO/IEC/IEEE 29148:2018).* ([ISO](https://www.iso.org/standard/72089.html?utm_source=chatgpt.com "ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering"))

Lakens, D. (2022). Sample size justification. *Collabra: Psychology, 8*(1), 33267. ([DOI](https://doi.org/10.1525/collabra.33267?utm_source=chatgpt.com "Sample Size Justification | Collabra: Psychology | University of California Press"))

McAllister, T. P. (2015). *Community Resilience Planning Guide for Buildings and Infrastructure Systems, Volume I* (NIST SP 1190v1). National Institute of Standards and Technology. NIST's framework explicitly links infrastructure performance goals, dependencies, hazards and recovery planning. ([NIST](https://www.nist.gov/publications/community-resilience-planning-guide-buildings-and-infrastructure-systems-volume-i?utm_source=chatgpt.com "Community Resilience Planning Guide for Buildings and Infrastructure Systems, Volume I | NIST"))

National Aeronautics and Space Administration. (2024). *NASA-STD-7009B: Standard for Models and Simulations.* ([Standards](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf?utm_source=chatgpt.com "NASA-STD-7009B"))

**We should not freeze numerical** **`\delta_1,\ldots,\delta_5`****, exact** **`\Omega_H`****, or final analysis procedures yet.** Those require the next step: selecting the reduced `P-T-I-O` demonstrator and determining what physical/data/benchmark evidence is actually available. The scientific structure of the five hypotheses, however, is now sufficiently rigorous to serve as the basis for that operationalization phase.