# Phase 1 — General Evidence -> Thesis Application Map

**Status:** EVIDENCE/APPLICATION AUDIT v1.0  
**Date:** 2026-09-12  
**Purpose:** distinguish what external standards/literature establish from what this thesis proposes for its bounded Power–Transportation experiment.  
**Governing rule:** a citation supports only the claim actually established by its source; it does not automatically validate the thesis-specific implementation.

---

## 1. Evidence translation rule

For every methodological choice, use

```math
\boxed{
\text{GENERAL EVIDENCE}
\rightarrow
\text{SCOPE MATCH}
\rightarrow
\text{THESIS APPLICATION}
\rightarrow
\text{WHY}
\rightarrow
\text{TEST}.
}
```

Claim status:

```text
[E] externally established;
[P] thesis-specific proposal;
[D] derived rationale;
[A] assumption;
[U] unresolved.
```

---

## 2. V&V and model credibility

### General evidence `[E]`

NASA-STD-7009B establishes common requirements/recommendations for model-and-simulation credibility, lifecycle use and acceptance criteria. ASME V&V 20 distinguishes numerical verification from validation against experimental data for declared variables/points and explicitly incorporates uncertainty in the comparison (NASA, 2024; ASME, 2009/2021).

### Our application `[P]`

Phase 1 is ordered as

```math
\text{specify}
\rightarrow
\text{verify}
\rightarrow
\text{identify}
\rightarrow
\text{calibrate}
\rightarrow
\text{validate}
\rightarrow
\text{compare}.
```

### Why `[D]`

Our thesis contains several opportunities for model flexibility: P physics, T physics, information delay, organizational delay, dependency operators and service mappings. Freezing these before confirmatory runs reduces post-hoc explanation and makes failure interpretable.

### What the citation does NOT prove

NASA/ASME do not prove that our chosen 33-bus/Sioux-Falls/ACN demonstrator is valid. They justify the **discipline of purpose-specific V&V and acceptance criteria**. The demonstrator must earn its own credibility through the declared tests.

---

## 3. Separate physical systems from common representation

### General evidence `[E]`

NIST characterizes cyber-physical systems as interacting physical, digital and human components and organizes analysis around concerns including timing, data, composition, boundaries and human aspects (Griffor et al., 2017; Wollman et al., 2017).

### Our application `[P]`

We keep

```math
F_P\neq F_T
```

and use the common dependency contract only for the **coupling**, not as a replacement for sector physics.

### Why `[D]`

This directly implements the thesis principle:

```math
\boxed{\text{common dependency language}\neq\text{common physical law}.}
```

The power network obeys radial electrical equations; the road/access system obeys transportation/routing equations; information and organization enter through their own causal operators/guards.

### What the citation does NOT prove

NIST does not prescribe our exact P–T–I–O ontology or our three-part dependency contract. Those are thesis decisions established through Phase 0.

---

## 4. Power benchmark

### General evidence `[E]`

Baran and Wu provide radial-distribution formulations used widely in distribution-system analysis. MATPOWER `case33bw` explicitly implements a 33-bus system derived from that source (Baran & Wu, 1989; MATPOWER).

### Our application `[P]`

Use `case33bw`; connect the charging site to bus 24 and use branch 23->24 as the controlled fault/restoration branch.

### Why `[D]`

The benchmark is small enough for repeated V&V/UQ while preserving voltage drop, real/reactive flow and radial network physics. Bus 24 is selected by a preregistered rule from the benchmark’s own load table rather than after observing coupled outcomes.

### What the citation does NOT prove

The 33-bus system is not an empirical representation of the Caltech feeder or Sioux Falls. Therefore it supports **benchmark physics**, not location-specific prediction.

---

## 5. Transportation benchmark

### General evidence `[E]`

LeBlanc, Morlok and Pierskalla (1975) introduced the well-known 24-node/76-arc traffic assignment test problem now distributed in the TNTP benchmark collection. TNTP supplies link capacity, free-flow time and BPR parameters.

### Our application `[P]`

Use Sioux Falls for accessibility and crew-routing mechanics; fix node 1 as the depot and node 10 as the charging/repair access node; close the 9–10 link pair in the controlled disruption.

### Why `[D]`

The road network is used to test the causal mechanism

```math
\text{accessibility}\rightarrow\text{crew travel}\rightarrow\text{restoration},
```

not to claim realistic Sioux Falls disaster prediction.

### What the citation does NOT prove

The original network does not establish that node 10 is a real charging hub, that the 9–10 link is hazard-prone, or that the benchmark is a realistic modern city network. Those are controlled experimental choices.

---

## 6. EV charging data and simulator

### General evidence `[E]`

ACN-Data provides observed EV charging sessions, including timestamps, delivered energy and charging-current/pilot time series. ACN-Sim is a data-driven simulator designed to replay realistic charging scenarios and represent charging-network constraints (Lee, Li, & Low, 2019; Lee et al., 2021).

### Our application `[P]`

Use Caltech ACN data as empirical charging forcing and ACN-Sim as the charging-system executable realization at a 5-minute interval.

### Why `[D]`

This avoids inventing synthetic EV arrival/energy distributions when measured charging behavior is publicly available. It also gives the Phase-1 information pathway an actual time series for calibration/holdout validation.

### What the citation does NOT prove

ACN data do not validate the IEEE 33-bus feeder, Sioux Falls road network, or our synthetic cross-domain mapping. They support the **charging-demand side** only.

---

## 7. EV/EVSE communication and information timing

### General evidence `[E]`

ISO 15118-20:2022 specifies EV–EVSE communication messages/sequences supporting electricity transfer and bidirectional power transfer. NIST treats timing/latency and data as first-order CPS concerns (ISO, 2022; Wollman et al., 2017).

### Our application `[P]`

Represent the information dependency through a delayed/noisy charging-demand signal

```math
\widetilde P_{ch}(t)
=
\widehat P_{ch}(t-\delta_I)+\varepsilon_I(t)
```

and test declared latency levels.

### Why `[D]`

The experiment needs a measurable information mechanism that can be removed/degraded without changing P or T physics. Delay/error provides that controlled treatment.

### What the citation does NOT prove

ISO/NIST do not prescribe our seasonal forecast, our `delta_I={0,5,15,30}` minute levels or our test-controller equation. Those are `[P]` experimental choices.

---

## 8. Organizational/access dependency

### General evidence `[E]`

Infrastructure restoration literature explicitly integrates restoration-crew routing with transportation networks, and coupled transportation–crew–grid work shows degraded road accessibility can delay repair-resource deployment and restoration (e.g., Transportation Research Part B, 2018; Wang et al., 2026).

### Our application `[P]`

Represent

```math
T_{restoration}
=
\tau_{decision}
+\tau_{mobilization}
+T_{crew}
+\tau_{repair}.
```

Road accessibility determines `T_crew`, which controls when the failed feeder branch may be re-energized.

### Why `[D]`

This makes the organizational dependency operational: it changes a restoration event time and therefore changes physical state/service trajectories.

### What the citation does NOT prove

The literature does not justify our chosen 15/15/60-minute organizational/repair values. Those are controlled assumptions `[A/P]` and remain epistemically uncertain in `Pi_e`.

---

## 9. Identifiability

### General evidence `[E]`

Identifiability analysis determines whether parameters can be inferred uniquely or practically from available observations. Profile likelihood can expose structural/practical non-identifiability and support experimental planning/model reduction (Raue et al., 2009).

### Our application `[P]`

Keep benchmark physical parameters fixed and estimate only explicitly declared information statistics. Use normalized sensitivities/SVD as a pre-screen; require stronger identifiability analysis if additional free continuous parameters are introduced.

### Why `[D]`

The thesis seeks causal-mechanism tests. Allowing many freely calibrated dependency parameters would weaken mechanism attribution because multiple parameter combinations could mimic the same service trajectory.

### What the citation does NOT prove

Raue et al. do not prescribe our singular-value ratio threshold `1e-8`; that is a numerical diagnostic `[P]`, not a universal identifiability criterion.

---

## 10. Uncertainty and sensitivity analysis

### General evidence `[E]`

JCGM provides established measurement-uncertainty principles. Morris (1991) provides an elementary-effects screening design for computational models; Sobol (2001) provides variance-based global sensitivity indices.

### Our application `[P]`

Use

```math
\text{Morris screening}
\rightarrow
\text{reduced active inputs}
\rightarrow
\text{Sobol analysis}
```

rather than applying expensive global UQ to every possible parameter.

### Why `[D]`

Phase 1 is deliberately small, but organizational times, information error and scenario assumptions remain uncertain. Screening protects computational effort while preserving an audit of excluded factors.

### What the citations do NOT prove

The literature does not mandate `p=4`, `r=20`, `N=1024/2048`. Those are preregistered thesis settings `[P]` whose convergence must be checked.

---

## 11. FMI and executable coupling

### General evidence `[E]`

FMI 3.0.2 standardizes containers/interfaces for model exchange, co-simulation and exposed model-variable dependencies (Modelica Association, 2024).

### Our application `[P]`

If FMI is used later, represent it as

```math
\Xi_e=\mathcal X(\Sigma_e),
```

an executable realization of an already-declared dependency mechanism.

### Why `[D]`

This preserves the Phase-0 distinction

```math
\boxed{\text{real-world dependency}\neq\text{runtime model connection}.}
```

### What the citation does NOT prove

An FMI variable dependency does not prove that the corresponding infrastructure relation is physically causal. Physical/organizational evidence still belongs in `Pi_e`.

---

## 12. Why the experiment is semi-empirical, not a digital twin

### Evidence `[E]`

The selected sources provide separately credible benchmark/data elements: a distribution feeder benchmark, a traffic benchmark and observed charging sessions.

### Thesis synthesis `[D/P]`

They do **not** describe one common real city or asset system. Therefore the mapping

```math
\text{IEEE bus 24}
\leftrightarrow
\text{Sioux Falls node 10}
\leftrightarrow
\text{Caltech ACN charging demand}
```

is a synthetic experimental interface.

The correct label is:

```text
benchmark-calibrated semi-empirical demonstrator
```

not:

```text
digital twin of a real Power–Transportation system.
```

### Why this is acceptable `[D]`

Phase 1 is designed to test executable causal structure and model credibility under controlled contrasts. Geographic transferability is a later empirical question, not something to assume during the first mechanism test.

---

# 13. Final evidence/application principle

The framework now follows the hierarchy

```math
\boxed{
\text{external theory/standard}
\rightarrow
\text{what it actually establishes}
\rightarrow
\text{our bounded engineering choice}
\rightarrow
\text{explicit assumption}
\rightarrow
\text{critical test}
\rightarrow
\text{bounded claim}.
}
```

This prevents three common reasoning errors:

```text
1. citing a standard as if it validates our specific model;
2. citing prior literature as if using the same concept is novel;
3. presenting a thesis-specific parameter/threshold as an established universal constant.
```

---

# References

See the full reference list in `PHASE1_EXPERIMENT_SPECIFICATION_V1.md`. Principal sources are NASA-STD-7009B; ASME V&V 20; NIST SP 1500-201/203; ISO 15118-20:2022; Baran & Wu (1989); LeBlanc et al. (1975); Lee et al. (2019, 2021); Raue et al. (2009); Morris (1991); Sobol (2001); JCGM 100:2008; FMI 3.0.2; and work-crew routing/restoration literature.
