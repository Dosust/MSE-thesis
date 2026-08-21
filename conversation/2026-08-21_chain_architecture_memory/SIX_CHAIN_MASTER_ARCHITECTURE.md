# Six-Chain Master Scientific Architecture

## A. Why six chains

The scientifically strongest architecture is not one giant arrow. Different chains answer different scientific questions and should not be collapsed.

## I. Physical-System Chain — What is the system?

Long form:

`Sector-specific physical laws & constitutive relations`
→ `Infrastructure components, spatial configuration & network topology`
→ `Cross-sector interdependencies & dynamic interface mechanisms`
→ `Coupled system states, stocks, flows & capacities`
→ `Nonlinear, hybrid & stochastic system dynamics`
→ `Disturbance propagation, feedback & cascading behaviour`

Short form:

`Physical Laws → System Structure → Interdependencies & Interfaces → States & Flows → Dynamics → Cascades`

### Layer meanings

- **Physical laws:** conservation, constitutive relations, thermodynamic/mechanical/electrical/hydraulic/transport/material-flow constraints.
- **Components/topology:** nodes, links, spatial layout, capacities, network geometry.
- **Interdependencies:** relationships of functional dependence across sectors.
- **Interfaces:** mechanisms through which interdependencies actually transmit flows, constraints, information, failures, or intervention.
- **States/stocks/flows/capacities:** physical variables needed to describe system condition.
- **Dynamics:** time evolution.
- **Cascades:** propagation and feedback after perturbation or failure.

A key conceptual distinction:

`Interdependency = relationship`  
`Interface = mechanism of the relationship`

## II. Observation–Inference–Prediction Chain — What do we know?

Long form:

`Measurement, sensing, monitoring & data acquisition`
→ `Observability, data quality & information extraction`
→ `System identification, calibration & inverse inference`
→ `State estimation & data assimilation`
→ `Parameter, structural & state UQ`
→ `Forecasting, predictive simulation & scenario projection`

Short form:

`Observe → Identify → Estimate → Quantify Uncertainty → Predict`

### Layer meanings

- **Measurement:** observations are not the hidden state itself.
- **Observability:** whether hidden states can be reconstructed from available outputs.
- **Identification:** infer unknown model structure/parameters from data.
- **State estimation:** infer current hidden state.
- **UQ:** quantify parameter/state/model uncertainty and its propagation.
- **Prediction:** forecast future states, failure, service, or recovery with uncertainty.

## III. Hazard–Failure–Consequence Chain — What happens under stress?

Long form:

`Hazard / climate / operational forcing`
→ `Spatial & temporal exposure`
→ `Component vulnerability & fragility`
→ `Physical damage, degradation & failure`
→ `Interdependent failure propagation & cascading disruption`
→ `Functional capacity loss`
→ `Critical-service degradation`
→ `Population, economic, environmental & institutional consequences`
→ `System risk & criticality`

Short form:

`Hazard → Exposure → Vulnerability → Damage → Cascades → Function Loss → Service Loss → Consequences → Risk`

Critical distinction:

`Physical state ≠ functional capacity ≠ critical service ≠ societal consequence`

Risk must not be collapsed to hazard alone.

## IV. Resilience–Viability–Recovery Chain — Can the system remain acceptable and recover?

Long form:

`Pre-disturbance system condition & preparedness`
→ `Disturbance absorption & resistance`
→ `Safe-state / viability boundary assessment`
→ `Reachability of unacceptable or recoverable states`
→ `Residual functionality & critical-service continuity`
→ `Recovery feasibility`
→ `Repair, restoration & resource allocation`
→ `Adaptive / feedback control`
→ `Recovered, adapted or transformed state`

Mathematical short form:

`State → Viability → Reachability → Resilience / Service Continuity → Recoverability → Recovery → Adaptive Control`

Important distinctions:

- viability asks whether admissibility can be maintained;
- reachability asks which states can be reached;
- recoverability asks whether an inadmissible state can return;
- recovery is an actual trajectory/process;
- control chooses interventions that influence that trajectory.

## V. Engineering Design–Operation–Adaptation Chain — What can engineers build and do?

Long form:

`Performance requirements, constraints & design objectives`
→ `Infrastructure architecture, topology, location & capacity design`
→ `Construction / deployment / commissioning`
→ `Operations, dispatch & resource allocation`
→ `Monitoring & condition assessment`
→ `Maintenance, repair & replacement`
→ `Capacity expansion, retrofit & investment planning`
→ `Climate adaptation & system transformation`
→ `Decommissioning, reuse, recycling & circularity`

Short form:

`Requirements → Design → Deploy → Operate → Monitor → Maintain → Expand/Retrofit → Adapt → Circularize`

Important rule:

**Optimization is not a lifecycle stage.** Optimization is a cross-cutting mathematical engine that can act on design, operation, recovery, maintenance, planning, and adaptation.

## VI. Sustainability–Equity–Governance–Decision Chain — What should society choose?

Long form:

`Infrastructure needs & critical-service requirements`
→ `Candidate designs, policies & intervention strategies`
→ multidimensional evaluation of:

- technical performance;
- resilience & risk;
- environmental sustainability;
- economic & financial value;
- equity, accessibility & justice;
- governance & institutional feasibility;
- human behaviour & social acceptability;

→ `Multiobjective evaluation under uncertainty`
→ `Trade-off / Pareto / robustness analysis`
→ `Decision & strategy selection`
→ `Implementation`
→ `Monitoring, learning & adaptive revision`

Short form:

`Needs → Alternatives → Evaluate → Trade Off → Decide → Implement → Learn → Adapt`

This is not a physical causal chain; it is a normative and decision chain.

## Cross-cutting mathematical spine

Do not draw these as a causal chronology. They overlap:

- Mathematical modelling
- Probability & stochastic processes
- Statistics & Bayesian inference
- Inverse problems & system identification
- Network science & graph theory
- Dynamical systems & PDEs
- Numerical analysis & scientific computing
- Uncertainty quantification
- Viability / reachability theory
- Control theory
- Optimization & operations research
- Machine learning / physics-informed AI
- Game theory & decision science

## Cross-cutting admissibility/value layer

Across the chains:

`Sustainability + Equity + Economics + Governance + Human Behaviour`

These can appear as:

- constraints;
- admissibility conditions;
- objectives;
- institutional feasibility conditions;
- evaluation criteria.

For the thesis, sustainability/equity should be considered for inclusion in the admissible state geometry rather than only post-hoc reporting.

## Whole-system feedback structure

A useful mental model is:

`I. Reality`
→ `II. Knowledge about reality`
→ `III. Disturbance/failure of reality`
→ `IV. Acceptability/recovery of reality`
→ `V. Engineering modification of reality`
→ `VI. Societal choice about modification`
→ back to `I. Reality`

Sideways feedbacks also matter:

- Chain II updates parameter/state knowledge used in Chain I;
- Chain III can change topology and modes in Chain I;
- Chain IV identifies which engineering actions are needed in Chain V;
- Chain VI selects which Chain V actions are implemented;
- implemented actions create new observations for Chain II.

## Urban-flooding demonstrator mapping

One illustrative P–W–T–SW chain:

`rainfall → waste accumulation/blockage → drainage reduction → flood depth → road disruption → constrained repair access → power/water service disruption → service consequences`

Then:

- Chain II estimates blockage/interface parameters from observations;
- Chain IV tests viability/recoverability of critical services;
- Chain V tests clearing, routing, backup power, pump protection, retrofit;
- Chain VI evaluates cost/resilience/carbon/equity/governance trade-offs.