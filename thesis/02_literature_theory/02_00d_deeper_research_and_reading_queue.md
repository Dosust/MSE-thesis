# Deeper Research and Reading Queue — Chapter 2 v1.0

**Status:** OPEN / REQUIRES FURTHER RESEARCH  
**Date:** 2026-09-18  
**Purpose:** preserve literature issues that are promising but not yet rigorous enough for unrestricted Chapter-2 use.

## 1. Priority coding

| Priority | Meaning |
|---|---|
| P0 | must be resolved before the corresponding Chapter-2 subsection is frozen |
| P1 | important for Chapter 3–4 model design; Chapter-2 prose may proceed with explicit qualification |
| P2 | useful extension; does not block the core thesis |
| P3 | exploratory only |

## 2. P0 — Must research/read before Chapter-2 freeze

### P0-1 — Competing-event race

Current thesis idea: `k* = argmin_k T_k`.

**Problem:** plausible as an event-scheduling/competing-process rule, but not yet established in the current audit as a standard coupled-infrastructure/P–T formulation.

**Research needed:** discrete-event simulation; competing risks/hazards; generalized stochastic Petri nets; piecewise-deterministic Markov processes; stochastic hybrid automata.

**Gate:** either identify formal provenance or explicitly derive and validate it as a thesis-proposed scheduler.

### P0-2 — Exact stochastic-hybrid P–T formulation

**Supported:** hybrid continuous/discrete systems are established mathematically; dynamic P–T interactions are established directly.

**Missing:** a peer-reviewed P–T resilience model matching the thesis's complete continuous + jump/reset + uncertainty architecture.

**Research needed:** hybrid automata for infrastructure; stochastic hybrid power systems; hybrid traffic/incident models; power–traffic co-simulation; guard/reset semantics.

### P0-3 — Closed P→T→P restoration feedback

Known pieces: Zhu et al. support P→T signal effects; Fotouhi et al. support T→P repair-access dependence.

**Missing:** end-to-end validation or quantitative parameterization of `hazard → power failure → signal outage → congestion → repair-access delay → delayed restoration`.

**Research needed:** disaster repair logistics; utility crew travel-time models; congestion/restoration interaction; empirical outage/road-access data.

### P0-4 — Direct P–T observation/state-estimation literature

Current direct evidence is weak relative to adjacent water–energy evidence.

**Research needed:** joint traffic-grid state estimation; EV charging-load estimation conditioned on traffic state; distribution-grid estimation using mobility data; co-simulation observability; sensor-placement/observability for coupled energy-mobility systems.

### P0-5 — Direct P–T organizational/coordination evidence

Current organizational evidence is mainly infrastructure-wide.

**Research needed:** utility–transport agency emergency coordination; signal/grid restoration governance; charging emergency management; authority/resource constraints; mutual-aid and incident-command arrangements.

### P0-6 — Direct infrastructure viability/reachability applications

Mathematical foundations are strong, but direct coupled-infrastructure use remains thin.

**Research needed:** viability kernels in power systems; reachability in energy systems; reach-avoid infrastructure safety; viability/reachability in transportation; coupled-infrastructure applications.

## 3. P1 — Important for mathematical/model design

### P1-1 — Temporal ontology

Current distinction: `t_e != delta_ij != tau_ij != T_rec`.

**Research needed:** propagation delay definitions; characteristic timescales; time-delay hybrid systems; repair/restoration duration models; cascade timing.

### P1-2 — Multiscale timescale descriptors

Candidate descriptors: `tau_a/tau_b`, `ln(tau_a/tau_b)`, and normalized timescale contrast.

**Problem:** no established infrastructure-resilience provenance verified yet.

**Research needed:** singular perturbation; timescale separation; multirate systems; dimensionless temporal ratios; synchronization/desynchronization metrics.

### P1-3 — Event ontology and reset-map design

Current event object is compatible with hybrid-system theory but not verified as an established infrastructure ontology.

**Research needed:** hybrid automata; timed automata; stochastic hybrid automata; event-log ontologies.

### P1-4 — State-to-service functions

Candidate form: `Q_P=h_P(Y), Q_T=h_T(Y)`.

**Research needed:** served-load definitions; mobility-service/accessibility metrics; critical-service weighting; normalization; spatial aggregation; threshold selection.

### P1-5 — H1 spatial-propagation metric

Need one preregistered spatial outcome able to distinguish static and dynamic coupling.

**Research needed:** propagation radius/speed; network-distance propagation; affected-service area; spatial autocorrelation; cascade-front metrics; space-time service loss.

### P1-6 — Interface delay and activation laws

Need evidence for propagation delays, characteristic timescales, and activation conditions.

**Research needed:** signal outage response; charger outage behavior; charging-demand response; repair-access delay; protection/switching delays; activation thresholds.

## 4. P1 — Sustainability / decision evidence requiring more direct P–T grounding

### P1-7 — Accessibility as sustainability consequence

**Research needed:** accessibility effects of outages/interventions; restoration-scenario accessibility metrics; distributional accessibility/equity; population weighting and accounting boundary.

### P1-8 — Operational energy and carbon consequences of resilience actions

**Research needed:** mobile generation/DER operation; restoration energy; V2G cycling; intervention-induced losses; emergency-supply emissions; marginal vs average emissions accounting.

### P1-9 — Resilience-only vs joint resilience–sustainability decisions

**Research needed:** Pareto-front changes; robust multiobjective infrastructure planning; regret; constrained resilience optimization; examples where adding sustainability changes admissible/nondominated actions.

## 5. P2 — arXiv/preprint reading queue

| ID | Preprint | Read for | Remaining verification |
|---|---|---|---|
| P2-1 | [Qiu et al. (2025)](https://arxiv.org/abs/2510.10914) | dynamic P–T operation, charging queues, V2G | peer-reviewed publication status |
| P2-2 | [Ghose et al. (2025)](https://arxiv.org/abs/2511.00941) | traffic-state → charging demand → grid planning | journal status; validation depth |
| P2-3 | [Li et al. (2024)](https://arxiv.org/abs/2407.16796) | cascading interdependent infrastructure optimization | publication status; P–T transferability |
| P2-4 | [Odunlami et al. (2025)](https://arxiv.org/abs/2509.02822) | hybrid power-system guards/switching | publication status; transferable event semantics |
| P2-5 | [Yuan et al. (2024)](https://arxiv.org/abs/2402.01547) | stochastic hybrid contingencies | publication status; formal event structure |

## 6. Broader systematic-search topics

1. dynamic traffic–power co-simulation;
2. physical P–T mechanisms beyond EV charging;
3. empirical infrastructure cascade datasets;
4. organizational constraints on restoration;
5. viability/reachability applications in infrastructure;
6. resilience intervention resource efficiency;
7. carbon consequences of resilience actions;
8. accessibility/equity in P–T disruption;
9. uncertainty propagation from mechanisms to viability boundaries;
10. validation standards for coupled-infrastructure digital twins/co-simulation.

## 7. Required deep-reading output for every P0/P1 paper

Record: exact supported claim; mechanism; mathematical object/equation; data/case; assumptions; calibration; verification; validation; uncertainty; main result; contrary/limiting result; transferability to this thesis; RQ/SO/H relevance; what the paper does **not** support; and final admission status PASS / CONDITIONAL / BLOCKED / EXCLUDE.

## 8. Current reading priority

1. competing-event / hybrid-event formalism;
2. direct P–T state estimation and observability;
3. closed P→T→P restoration feedback;
4. infrastructure viability/reachability applications;
5. temporal delays and multiscale modeling;
6. direct P–T organizational constraints;
7. service-function definitions;
8. sustainability consequence quantification;
9. joint resilience–sustainability decision evidence.

This queue remains OPEN until each item is either promoted to the accepted-core register or explicitly rejected.