# Working Thesis Research Proposal — Thermal Interdependencies (SO1–SO3)

**Official thesis title:** **Engineering of Power–Electrified Transportation Interdependencies for Resilience**  
**Program:** Master of Science in Engineering (MSE), Sustainable Engineering, Arizona State University  
**Document status:** **PROPOSED / EVIDENCE-GATED / NOT SUPERVISOR APPROVED / NOT RELEASE-READY**  
**Working version:** V1, 2026-10-16  
**Title authority:** [Canonical Thesis Title V3](../../project/CANONICAL_THESIS_TITLE_V3.md)  
**Scientific scope:** [Thermal Interdependency Scope V1](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md), [Extreme-Heat State-Time Amendment V4](../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)  
**Objectives:** [Frozen GO and SO1–SO3](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)  
**Evidence:** [Evidence and Non-Invention Standard](../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md)

> **Interpretation:** This is the active candidate proposal for scientific review, not a claim that the thesis is experimentally validated, its method is selected, the bibliography is systematically complete, or a university/chair has approved a final proposal. The title is official in repository governance only.

## Abstract (working)

Power distribution and electrified road transportation interact through charging equipment, electrical power transfers, operating limits and time-dependent demand. During extreme heat, equipment thermal states can constrain both electrical supply and charging capability. Yet two systems experiencing the same hot weather is not evidence that one caused the other's deterioration. Existing studies document transformer thermal models and their calibration, EV-charging impacts on calculated transformer aging, measured fast-charger derating under hot conditions, and joint EV–grid co-simulation (Godina et al., 2016; Blomgren et al., 2023; Balogun et al., 2024; Krama et al., 2026). The thesis will qualify the *directional, temperature-conditioned* physical interface mechanisms that can connect these phenomena, develop a minimum-sufficient physics-based state-time representation only for qualified mechanisms, and assess critical transitions, propagation timing and effects on required electricity and mobility services. Physical-only, identified grey-box and physics-informed learning methods remain conditional candidate implementations. Experimental data, model observability, uncertainty, independent holdouts and applicable operating limits will govern what can be asserted. Cross-system field validation will not be claimed unless synchronized Power and Electrified Transportation measurements actually support it.

## 1. Engineering context and problem

The **Power System (P)** supplies electrical energy to the physically distinct **Electrified Transportation System (Tₑ)**. Under the frozen full system definition, Tₑ includes electrically propelled road vehicles, rechargeable energy-storage systems, propulsion and auxiliaries, the vehicle power-supply circuit, **EV supply equipment (EVSE)**, the physical charging connection and required charging communication/control. EVSE is not a third infrastructure system. The bounded active application is grid-connected, battery-electric road transportation; public fast charging versus depot/fleet charging remains **OPEN** pending data and mechanism feasibility. These are internal scope decisions, not claims of field-tested coupling ([system-boundary authority](../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md)).

High ambient temperature is an **exogenous forcing** to both systems. Power-side loading and equipment heating may change thermal capacity or permissible supply; Tₑ-side heat may constrain charging output or demand. A direction is an interdependency only if evidence and appropriate physics support a **heat-conditioned change in one system's capability or service attributable to a state/constraint in the other through the power-transfer interface**, rather than shared ambient heating or an ordinary electrical connection alone ([thermal scope authority](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)). No unobserved direct conductive heat transfer across grid and vehicle is assumed.

**Research problem.** Under extreme heat, which specific physical state/constraint mechanisms qualify as directional P→Tₑ or Tₑ→P thermal interdependencies; how do those mechanisms evolve through state and time; and when, if at all, do their effects propagate to required electricity or mobility services? Qualified evidence is needed to discriminate thermal effects from ordinary loading, ambient confounding, nonthermal controls and model artifacts.

## 2. Established prior work and bounded unresolved questions

### 2.1 What prior studies actually establish

- **EV charging to transformer thermal consequences:** Godina et al. (2016) use measured baseline electrical input data, modeled EV charging profiles, transformer thermal equations and insulation aging calculations. Consequently, EV load→transformer heating/aging calculations are existing prior art. Their thermal outcomes are primarily **modeled**, not independently measured coupled-interface hot-spot observations ([Godina et al., 2016](https://doi.org/10.1016/j.enconman.2016.04.087), original publisher-version PDF inspected).
- **Transformer thermometry and grey-box identification:** Blomgren et al. (2023) fit and test a stochastic physically motivated transformer-temperature model using distribution-utility field measurements; reported prediction accuracy chiefly concerns **measured lid temperature**, not direct independent winding-hot-spot measurement. Field transformer modeling and grey-box methods are thus prior art ([Blomgren et al., 2023](https://doi.org/10.1016/j.segan.2023.101048), original PDF inspected).
- **Measured internal hot spots:** Villarroel et al. (2017) demonstrate the value of internal fibre-optic temperature observations and parameter calibration for predicting a transformer's hot-spot temperature under a separately tested overload event. That is **component-level** experimental evidence, not a P–Tₑ field test ([Villarroel et al., 2017](https://doi.org/10.1049/oap-cired.2017.1102), publisher-indexed article text; original PDF not acquired).
- **EVSE extreme-heat observations:** Krama et al. (2026) report a field experiment on a 50-kW DC charger in Qatar, with ambient conditions approximately 15–55°C; the charger thermally derated and charging time for the tested state-of-charge window rose from 86 to 169 minutes. This supports EVSE-side heat/charging consequences **but not a separately observed upstream distribution-transformer hot spot or actual trip completion**. Source tier: publisher abstract and institutional record, not original PDF/raw time-series audit ([Krama et al., 2026](https://doi.org/10.1016/j.ecmx.2026.101960)).
- **Coupled grid–charging simulation:** EV-EcoSim already represents charging, grid transformer thermal dynamics and distribution-network simulation (Balogun et al., 2024). A co-simulation alone is therefore not a novel scientific contribution; the inspected author manuscript explicitly did not model internal battery thermal states ([Balogun et al., 2024](https://doi.org/10.1109/TSG.2023.3339374), author-manuscript text, journal version not cross-audited).
- **Numerical vs physics-informed methods:** Bragone et al. (2022) use a simplified 1D transformer heat PDE with real operating inputs and compare a PINN with the finite-volume numerical solution; that comparison does not establish independently measured interior temperature-field accuracy or PINN superiority ([Bragone et al., 2022](https://doi.org/10.1016/j.epsr.2022.108447), original PDF inspected).

### 2.2 Proposed research gap — limited-evidence hypothesis, not confirmed absence

The present **six-stream pilot** has **15 provisional paper/dataset leads**, source audits at different confidence tiers and **no completed authenticated Scopus/Web of Science/IEEE Xplore/Compendex search or formal PRISMA count**. Its inability to locate a suitable synchronized full-system dataset **does not prove none exists**.

**Working gap hypothesis:** For extreme heat, independently measured and cross-validated *directional P–Tₑ interface* laws linking observed thermal states/constraints, physical propagation or transition timing, and both electricity and mobility-service consequences may remain insufficiently characterized—particularly when confounded by shared ambient heat, aggregate transformer loading, charging controls and equipment heterogeneity. This hypothesis remains testable/falsifiable by the completed systematic literature review, accessible experiments, or a verified prior-art counterexample.

In particular, “temperature-dependent EVSE charging-time change” is **not automatically** observed transportation trip/schedule loss; “transformer temperature forecast” is **not automatically** an independently measured winding hot spot; and “coupled simulator output” is **not** a field measurement.

### 2.3 Novelty claims that are prohibited at proposal stage

Do not claim the invention of transformer thermal ODEs, EV-charging transformer aging, grey-box estimation, PINNs for transformer heat, charger thermal derating, or EV–power co-simulation. Any distinctive thesis contribution must be established narrowly and comparatively after formal prior-art searches and matched validation—not declared novel simply because the framework combines familiar components.

## 3. Research scope, boundaries and assumptions

**Inside scope:** Qualified P→Tₑ and/or Tₑ→P **thermal-conditioned** dependencies under extreme heat; necessary Power-side and Tₑ-side thermal states, heat-conditioned capabilities, directional interface quantities, state trajectories, physically defined critical time events, electricity-service and mobility-service consequences, and recovery times **only if recovery is actually modeled**.

**Exogenous/input conditions:** ambient extreme-heat forcing; equipment electrical loading and demand; cooling or charging controls where evidenced; relevant initial/boundary conditions, parameter domains and site context. SOC is an **energy state**, not a thermal state. Degradation is an optional slow state, admitted only if it changes the proposed horizon's conclusions. Interface power/energy is a coupling quantity, **not a third infrastructure**.

**Outside independent research scope:** all nonthermal P–Tₑ interdependencies; generic information/organizational or traffic-network modeling; universal resilience optimization; all transport modes; full battery electrochemistry; complete LCA/social LCA; unbounded multi-criteria intervention rankings. Needed nonthermal quantities may be boundary conditions or constraints only ([scope](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md); [state/time](../../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)).

**Key assumptions to test, not freeze:** adequate temporal resolution; known equipment identities and ratings; documented thermal operating envelopes; sufficiently excited data for parameter identification; stable calibration instruments; and comparability of heat and reference events. If a required assumption fails, narrow the experiment or mark the associated claim **NOT ESTABLISHED**.

## 4. Frozen research goal and objectives — exact approved wording

**General Research Objective**

> To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.

**SO1 — Identify and qualify**

> Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.

**SO2 — Model state-time evolution**

> Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.

**SO3 — Quantify consequences**

> Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

These four quotations reproduce the [frozen objectives authority](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md) exactly. **No SO4 or seven-objective contract is activated.**

### 4.1 Working research questions — PROPOSED, NOT FROZEN

**W-RQ1 (SO1):** What physically and empirically qualified heat-conditioned P→Tₑ and Tₑ→P mechanisms, states, capability constraints and interface measurements are sufficient to establish directional interdependency rather than parallel heat exposure?

**W-RQ2 (SO2):** Under what explicit constitutive assumptions and data-identifiability conditions can minimum-sufficient physics-based state-time models reproduce each qualified mechanism, including delays and thermal constraints under extreme heat?

**W-RQ3 (SO3):** Which supported thermal thresholds/transition times and causal propagation intervals change the electricity and mobility-service trajectories, and how reliably can these consequences be predicted using independently verified data?

The questions clarify research logic only. **Final RQs and hypotheses remain OPEN**, pending an independently approved/versioned freeze. No new official objective has been created.

## 5. Conceptual and mathematical orientation (working, not a model freeze)

### 5.1 Physical mechanism and inference architecture

~~~text
Exogenous extreme-heat exposure H(t)
            ↓                     ↓
  Power-side thermal state   Tₑ-side thermal state
            ↓                     ↓
   Thermal capability        Thermal capability
            \                   /
             shared electrical power-transfer interface
                 ↙           ↘
             P→Tₑ?          Tₑ→P?
                 ↓           ↓
     State evolution / conditional transitions / propagation
                           ↓
                Electricity or mobility service
                           ↓
                 Service-level resilience
~~~

Each directional arrow with a question mark remains **a hypothesis requiring its own physical and empirical qualification**, not a causal fact. The arrows from ambient forcing are common-cause paths, not proof of interdependency.

### 5.2 Schematic state-time specification (T1 thesis working formulation)

Let H(t) be external heat forcing, X_P(t) and X_{Tₑ}(t) minimum-sufficient physically evolving states, Z(t) a power-transfer/interface quantity, u controls and θ parameters. Candidate equations are:

$$
\begin{aligned}
\dot X_P(t) &= f_P\bigl(X_P(t),H(t),Z(t),u_P(t);\theta_P\bigr),\\
\dot X_{T_e}(t) &= f_{T_e}\bigl(X_{T_e}(t),H(t),Z(t),u_{T_e}(t);\theta_{T_e}\bigr),\\
Z(t) &= \Gamma\bigl(X_P(t),X_{T_e}(t),H(t),D(t),u(t);\theta_I\bigr),\\
Q_P(t) &= G_P\bigl(X_P(t),Z(t),u(t)\bigr),\\
Q_T(t) &= G_T\bigl(X_{T_e}(t),Z(t),u(t)\bigr).
\end{aligned}
$$

Here f, Γ and G are **unknown functional structures**, not fitted laws. Model-specific state variables and constitutive equations may be drawn from verified physics, standard thermal models or identified input-output mechanisms only after appropriate equation/parameter/source gates. H belongs to neither physical system's endogenous state. Power-transfer quantities are coupling variables unless separately modeled dynamics require additional states.

A conditional thermal interface must carry actual electrically meaningful quantities—e.g., grid-side AC real/reactive power, voltage/current and available charging power—with specified direction, unit, sign convention and measurement location. A hypothetical **P→Tₑ** pathway is: measured power transformer/feeder thermal limit → documented supply/capability restriction → measurable EVSE input/delivered-energy consequence. A hypothetical **Tₑ→P** pathway is: heat-driven charger control/derating → measured change in grid-side draw → transformer electrical losses → future transformer thermal condition. The existence, sign, timing and size of either pathway are **OPEN**, not implied by a generic coupling equation.

For a physically qualified thermal safety/capability boundary g_j(X,H,Z,u) with a **separately sourced and applicable** threshold, a working critical transition time is

$$
\tau^{\mathrm{crit}}_j=\inf\{t\geq t_0:\ g_j(X(t),H(t),Z(t),u(t))\leq 0\}.
$$

The sign convention and threshold definition must be stated and checked before use. “Propagation delay” δ_{P→Tₑ} or δ_{Tₑ→P} is not merely a difference between any two events: it is assigned only when directionality and an attributable temperature-conditioned interface pathway have been supported by experiments, timing and a defensible alternative/common-forcing control. Counterfactual simulation alone can show **modeled sensitivity**, not automatically field causality.

Service-level resilience is interpreted using the [canonical resilience definition](../../project/CANONICAL_RESILIENCE_DEFINITION_V1.md): required electricity/mobility service Q_k^{req}(t) must be independently defined before claims of maintained/recovered service. Charging power, energy delivered or duration are charging **proxies** unless needed vehicle-trip or schedule fulfillment data support a mobility-service quantity. Recovery metrics are not obligatory if recovery has not been modeled.

**Implementation families remain conditional:** PHY (first-principles/specified physics and numerical model), GREY (data-identified physics with uncertainty), PIML (physics-informed ML including PINNs). A better score on numerical/synthetic reference data is not equivalent to better field validation.

## 6. Methodology and evidence gates

### Phase A — Literature qualification (SO1, cross-cutting)
Execute and export the prepared six conceptual streams, with a two-part L1A/L1B direct-interface search, in **Scopus, Web of Science, IEEE Xplore and Compendex** when legitimately accessible. Preserve native queries, dates, total results, DOI-level records, filters, deduplication, screening reasons and PRISMA counts. Do not equate 28 **draft/unexecuted** strings with an executed formal review. Extract equations, scope, equipment topology, measurements, source tiers, model validity, uncertainty and actual service evidence. Compare all identified counterexamples before deciding any novelty statement.

### Phase B — Mechanism admissibility (SO1)
For each P→Tₑ or Tₑ→P candidate, record **physical source → thermal variable → capability/operating constraint → carried interface quantity → receiving effect → service mapping → evidence**. Identify ambient confounding and competing causes, especially cooling controls, battery taper, nonthermal voltage limitation and aggregate electrical demand. Exclude or mark **INSUFFICIENT EVIDENCE** when temperature-conditioned direction or source/receiving states are unqualified.

### Phase C — Data and model feasibility (SO1→SO2 gate)
Require original, permitted files, identifiers and synchronized timestamps, sensor coordinates and units, extreme-heat coverage, load/excitation ranges, quality flags, uncertainty/calibration and independent time/session/site splits. Distinguish experimental measurements from modeled fields and downloaded files from merely described datasets. An EVSE-only field dataset may calibrate Tₑ, but without matched Power-side transformer observations cannot validate P–Tₑ joint field mechanisms. If datasets cannot meet the interface conditions, **do not fabricate a joint field dataset by concatenating unrelated records**; present separately qualified component validation plus clearly labeled coupled **simulation** where defensible.

### Phase D — Physics and parameterization (SO2)
Select the smallest verified thermal state set capable of representing material thresholds and timing: for example, a directly sensed P component temperature, EVSE rectifier thermal state, and any essential energy/operational state. These are **candidates**—not frozen selections. Verify component-level conservation, dimensional consistency, parameter origin, initial/boundary conditions and limiting cases before coupling. Test observability/identifiability by parameter sensitivities, profile/covariance checks and independent thermal excitation; if indistinguishable parameters produce equivalent observable predictions, do not declare separately identified transfer coefficients.

### Phase E — Matched rival-method evaluation (SO2→SO3)
Define a common observable target and identical train/test episodes for **PHY, GREY, and PIML if feasible**. Report measured-target MAE/RMSE/bias, interval calibration, physically admissible state limits, critical-time error, computation cost and held-out extreme-heat generalization. Include basic low-order RC/ODE and numerical physical references. Include PIML only if necessary data and physics justify the added model class (Bragone et al., 2022); it is not a mandatory contribution. Do not compare a model's error against field measured lid temperature with another model's error against simulated hottest-spot temperature as if the targets were equivalent.

### Phase F — Directionality, transition and service tests (SO3)
Use matched heat and control/load episodes where feasible. Separately test P→Tₑ and Tₑ→P by changing or conditioning the proposed source thermal limit/response, preserving nuisance operating factors where possible, and checking receiving-side measurements and time ordering. Report critical-time estimates only for evidence-backed thresholds; report propagation delays only if attributable and distinguish them from component thermal response lags. Define electricity-service output (delivered supply, curtailment or other actual requirement) and mobility-service output (required energy available before departure, schedule fulfillment or observed equivalent) **before** interpreting resilience. Report uncertainty and non-support results.

### Phase G — Conditional downstream resilience and sustainability interpretation
Under the [service-level resilience authority](../../project/CANONICAL_RESILIENCE_DEFINITION_V1.md), assess maintained service, duration below required service and recovery **only if trajectories and requirement thresholds exist**. Two-pathway sustainability assessment is optional and **bounded** to available measurable environmental, economic and social indicators of (1) thermal/service consequences or (2) a tested engineering response; it does not add SO4, universal optimization or unsupported SDG impact ([sustainability authority](../../project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md)).

## 7. Planned falsification and limitation tests

1. **Common forcing alternative:** If P and Tₑ respond separately to H(t) and the receiving outcome has no qualified dependence on the proposed source interface mechanism, **do not** label a directional interdependency.
2. **Baseline alternative:** If thermal-only and full coupling models make indistinguishable field predictions, report no empirical improvement rather than claim synergy.
3. **Identifiability:** If only aggregate grid load is measured and cannot separate EVSE heat-conditioned demand effects from other household demand, directional coefficient estimates remain conditional/unidentified.
4. **Benchmark superiority:** If GREY/PIML does not outperform simpler PHY on the same independently measured target and uncertainty budget, do not select it based on architectural sophistication.
5. **Threshold validity:** If a threshold is transferred from incompatible equipment/rating/climate without manufacturer/standard/experimental admissibility, its critical-time result cannot support an engineering guarantee.
6. **Service observability:** If only delivered charging energy or session length is measured, mobility trip or schedule performance must remain **UNKNOWN** without supported requirement data.
7. **Transferability:** A held-out season from one charger or one transformer's overload experiment is not automatically a multi-device or multi-site generalization guarantee.

Failed critical tests lead to a narrower admissible research claim, a documented blocker or a negative finding—not post-hoc replacement of observations.

## 8. Planned research outputs and completion conditions

| Objective | Proposed output | Evidence needed to declare completion |
| --- | --- | --- |
| SO1 | Source-anchored directional thermal mechanism register with physical states, interfaces, competing pathways, evidence tiers and exclusions | Reproducible research corpus; original-source traceability; separately qualified directions and system boundaries |
| SO2 | Minimum-sufficient thermal state-time equations / identified and verified physical parameters, with matched model-class comparison where admissible | Physical and numerical verification, sensor/parameter identification, independent holdouts and uncertainty reporting |
| SO3 | Qualified transition and propagation timing, plus electricity/mobility-service trajectories | Observed or clearly simulation-labeled scenarios, sourced operating/service thresholds, valid causal attribution, holdout predictive checks |

**Feasibility stop condition:** if linked data are unavailable, report component-level measured validation and explicitly bounded interface simulation as such; do not assert end-to-end experimental validation or complete SO3 measurements. The scholarly outcome may include a documented non-identifiability or data-readiness finding, but thesis scope or completion expectations then require chair discussion—not silent change.

**Working deliverables:** literature evidence matrix, evidence-qualified mechanism table, model equation/provenance and parameter registry, data-readiness report, matched comparison scripts with reproducible splits, service definitions, uncertainty/limitations and a concise engineering interpretation. Precise timeline and experimental site, sensing, instruments, power-transfer direction and equipment are **OPEN** until evidence and supervision support them.

## 9. Source and readiness disclosure

As of 2026-10-16, the related [systematic review pilot in draft PR #84](https://github.com/Dossiya-SE/MSE-thesis/pull/84) is not a completed systematic review. It logged 19 public-web query runs and 15 provisional leads. Four original scholarly PDF artifacts have been read in text (including one arXiv author manuscript), and Villarroel publisher-indexed article text was separately examined. Figure pixels were not generally verified. Krama's publisher-authenticated PDF and raw field records have not been obtained; its paper is verified at publisher abstract/institutional bibliography level. Scopus, Web of Science, IEEE Xplore and Compendex authenticated query executions and native record exports are absent; **PRISMA actual record counts remain UNKNOWN**. These source tiers are preserved in the audit records; the proposal is not a full systematic-review inference.

Scientific originality, a finalized model family, directly measured P↔Tₑ thermal law, site-level mobility-service observability and independent multi-equipment generalization all remain **OPEN**. No numeric parameters, temperature thresholds, population effectiveness figures or resilience guarantees are invented.

## References (primary sources used in this working proposal)

Balogun, E., Buechler, E., Bhela, S., Onori, S., & Rajagopal, R. (2024). *EV-EcoSim: A grid-aware co-simulation platform for the design and optimization of electric vehicle charging infrastructure*. IEEE Transactions on Smart Grid. https://doi.org/10.1109/TSG.2023.3339374  
[Primary article DOI; original arXiv author-manuscript text audited; journal-version equivalence not independently audited.]

Blomgren, E. M. V., et al. (2023). *Grey-box modeling for hot-spot temperature prediction of oil-immersed transformers in power distribution networks*. Sustainable Energy, Grids and Networks, 34, 101048. https://doi.org/10.1016/j.segan.2023.101048  
[Publisher-version PDF text audited; reported validation mainly targets measured lid temperature.]

Bragone, F., Morozovska, K., Hilber, P., Laneryd, T., & Luvisotto, M. (2022). *Physics-informed neural networks for modelling power transformer's dynamic thermal behaviour*. Electric Power Systems Research, 211, 108447. https://doi.org/10.1016/j.epsr.2022.108447  
[Publisher-version PDF text audited; numerical FVM used as main distributed-field reference.]

Godina, R., et al. (2016). *Innovative impact assessment of electric vehicles charging loads on distribution transformers using real data*. Energy Conversion and Management, 120, 206–216. https://doi.org/10.1016/j.enconman.2016.04.087  
[Publisher-version PDF text audited; original load input + modeled EV and transformer thermal outputs.]

Krama, A., Kamal, N., Sezer, N., & Bayhan, S. (2026). *Impact of extreme climatic conditions on fast EV charger performance: Field experimental insights from Qatar*. Energy Conversion and Management: X, 31, 101960. https://doi.org/10.1016/j.ecmx.2026.101960  
[Publisher abstract/HBKU record audited; original PDF and raw data NOT acquired.]

Villarroel, R., Liu, Q., & Wang, Z. (2017). *Experimental study of dynamic thermal behaviour of an 11 kV distribution transformer*. CIRED – Open Access Proceedings Journal. https://doi.org/10.1049/oap-cired.2017.1102  
[Publisher-indexed original text and reported experiment; original PDF/raw traces not acquired.]

**Bibliography status:** preliminary working references, not the complete systematic-review bibliography; abbreviated author lists for Blomgren and Godina require final APA-7 metadata expansion from the publisher/DOI export before formal submission. All manuscript scientific claims use adjacent author-year and DOI links, while original thesis scope/objectives cite their internal authorities.
