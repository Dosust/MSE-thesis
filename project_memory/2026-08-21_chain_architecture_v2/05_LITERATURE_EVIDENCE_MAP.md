# Literature Evidence Map — v2

## Purpose

This file preserves the literature families already used to explain the six chains while separating:

- bibliographic anchors that are already stable in the project;
- exact records that still require re-verification from the frozen corpus/full text;
- generic mathematical forms that must not be attributed to a paper without checking the source.

This is a **memory/evidence-routing file**, not the final bibliography.

---

# Chain I — Physical system, interdependencies, multilayer structure, interfaces

## Stable anchors already used

### Rinaldi, Peerenboom & Kelly (2001)

**Title:** *Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies*  
**DOI:** `10.1109/37.969131`

**Role:** canonical infrastructure-interdependency taxonomy; supports distinguishing different types of interdependency and treating coupled infrastructure as a system problem.

### Ouyang (2014)

**Title:** *Review on modeling and simulation of interdependent critical infrastructure systems*  
**DOI:** `10.1016/j.ress.2013.06.040`

**Role:** review of modeling paradigms for interdependent critical infrastructure; supports the claim that different mathematical representations capture different mechanisms and scales.

### Boccaletti et al. (2014)

**Title:** *The structure and dynamics of multilayer networks*  
**DOI:** `10.1016/j.physrep.2014.07.001`

**Role:** multilayer/network-of-networks structure and dynamics.

### Kivelä et al. (2014)

**Title:** *Multilayer networks*  
**DOI:** `10.1093/comnet/cnu016`

**Role:** multilayer network terminology and formal representation.

### Buldyrev et al. (2010)

**Title:** *Catastrophic cascade of failures in interdependent networks*  
**DOI:** `10.1038/nature08932`

**Role:** canonical evidence that interdependency can qualitatively change cascade/robustness behavior.

## Record requiring exact corpus lookup before final citation

- Gao et al. network-of-networks robustness family.
- Ouyang & Dueñas-Osorio interface-topology/design work.

**Memory rule:** these families were invoked in the discussion, but future thesis text must retrieve the exact frozen-corpus record/full-text evidence before citing.

---

# Chain II — Observation, inverse problems, identifiability, uncertainty

### Stuart (2010)

**Title:** *Inverse Problems: A Bayesian Perspective*  
**DOI:** `10.1017/S0962492910000061`

**Role:** Bayesian inverse-problem foundation; posterior inference and uncertainty representation.

### Tarantola / inverse-problem foundation

**Role:** general inverse-problem formulation, data-model inversion and uncertainty.

**Status:** exact edition/record must be retrieved before final citation.

### Infrastructure-specific inverse/system-identification papers

The project literature corpus contains infrastructure-specific examples such as water-network source/parameter identification, system identification, model reduction for Bayesian inversion, and physics-informed parameter estimation.

**Status:** retrieve exact records/evidence anchors from the authoritative corpus before using them to support P2/H1.

---

# Chain III — Hazard, fragility, failure, cascades, service consequences

### Buldyrev et al. (2010)

Also relevant here as a cascade precedent.

### Mühlhofer et al. (2023) hazard/failure-cascade literature family

**Role in current synthesis:** linking natural-hazard risk to infrastructure failure cascades.

**Status:** exact title/DOI must be recovered from the authoritative corpus before final citation.

### Fragility functions

Representative generic family used in the discussion:

```text
P(D_i >= d_s | IM)=Phi((ln IM-ln mu_i,ds)/beta_i,ds)
```

**Status:** mathematical template only. Final fragility equations must be tied to sector/hazard-specific empirical literature and parameter evidence.

---

# Chain IV — Viability, reachability, resilience, recovery

## Viability theory

### *Approximation of the viability kernel*

**DOI:** `10.1007/BF01204182`

**Role:** numerical viability-kernel approximation / foundational viability computation.

### *Viability Problems for Nonautonomous Differential Inclusions*

**DOI used in current project discussion:** `10.1137/0329014`

**Role:** nonautonomous/differential-inclusion viability foundations.

### *A Survey of Viability Theory*

**Status:** **IDENTITY/DOI CONFLICT — do not use a DOI from memory.**

The project history contains a conflict around `10.1137/0328044` versus `10.1137/0328045`. The correct bibliographic identity must be checked directly from the authoritative record before final citation. This was one reason the closed-corpus ranking retained an identity-warning mechanism.

## Hamilton–Jacobi reachability

### Mitchell, Bayen & Tomlin (2005)

**Title:** *A Time-Dependent Hamilton-Jacobi Formulation of Reachable Sets for Continuous Dynamic Games*  
**DOI:** `10.1109/TAC.2005.851439`

**Role:** time-dependent reachable sets, dynamic games, Hamilton–Jacobi reachability/viscosity-solution foundation.

**Formula rule:** do not copy a generic HJ/HJI sign or min/max order without deriving it from the exact target/control/disturbance convention.

## Classical resilience metrics

### Bruneau et al. (2003)

**DOI:** `10.1193/1.1623497`

**Role:** established resilience/performance/recovery-curve framing.

### Cimellaro et al. (2010)

**DOI:** `10.1016/j.engstruct.2010.08.008`

**Role:** quantitative resilience/performance-recovery formulation.

### Hosseini et al. (2016)

**DOI:** `10.1016/j.ress.2015.08.006`

**Role:** review/synthesis of resilience definitions and measures.

### Panteli et al. power-system resilience family

**Role:** power-system resilience and restoration/performance literature.

**Status:** exact record should be retrieved before final citation.

---

# Chain V — Engineering action, restoration, design, adaptation

### Nurre et al. (2012)

**DOI:** `10.1016/j.ejor.2012.07.010`

**Role:** network restoration/design/scheduling optimization family.

### Cavdaroglu et al. interdependent restoration family

**Role:** joint/interdependent infrastructure restoration under dependency/resource constraints.

**Status:** exact record must be retrieved from the frozen bibliography.

### Ouyang & Wang (2015)

**DOI used in current project discussion:** `10.1016/j.ress.2015.03.011`

**Role:** interdependent infrastructure resilience/restoration family.

**Status:** verify exact title and proposition anchor before thesis citation.

### Multi-timescale water–power restoration paper

**Title:** *Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties*  
**DOI:** `10.1016/j.ress.2025.111083`

**Role:** one of the strongest corpus-relative precedents connecting interdependent water–power restoration, uncertainty and multiple timescales.

---

# Chain VI — Sustainability, equity, tradeoffs, decision

### Coleman et al. (2024)

**Title used in current project discussion:** *Weaving equity into infrastructure resilience research: a decadal review and future directions*  
**DOI:** `10.1038/s44304-024-00022-x`

**Role:** equity dimensions in infrastructure resilience and limitations of treating equity as a single generic score.

**Status:** verify exact title metadata against the authoritative corpus before final bibliography export.

### Sustainability/climate-resilience transport recovery paper

**Title:** *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery*  
**DOI:** `10.1016/j.trd.2023.103800`

**Role:** strong bridge between sustainability, climate resilience, recovery and tradeoffs.

### NIST Community Resilience Planning Guide

**Role:** community performance goals, planning and implementation.

**Status:** cite the official NIST edition/record used in the final evidence table.

---

# Literature maturity interpretation

The present project should treat the following as **established research domains rather than thesis novelty claims**:

- infrastructure interdependency taxonomies;
- multilayer/network representation;
- cascading failures in interdependent networks;
- classical resilience metrics;
- restoration optimization;
- general viability theory;
- general Hamilton–Jacobi reachability;
- general inverse-problem/Bayesian mathematics;
- sustainability and equity as established infrastructure-research topics.

The candidate contribution lies in a narrower **integration/falsification space**, including:

- dynamic interface states/mechanisms in coupled infrastructure;
- interface-identification uncertainty propagated into viability/recovery geometry;
- timescale-dependent validity of static interface approximations;
- viability-boundary-based interface criticality;
- sustainability/equity as explicit viability admissibility constraints;
- recovery/capture geometry in the selected coupled P–W–T–SW setting;
- waste–drainage–flood and transport-access feedbacks in the demonstrator;
- reduced-order preservation/conservative bounding of viability decisions.

These are **candidate gaps to falsify**, not globally established novelty.

# Citation-state labels for future work

Use one of these labels in evidence tables:

```text
VERIFIED_FULL_TEXT
VERIFIED_METADATA
CORPUS_DERIVED
CARRIED_FORWARD_NEEDS_RECHECK
IDENTITY_CONFLICT
MATHEMATICAL_TEMPLATE
PROPOSED_INTERPRETATION
```

Do not cite this memory file as if it were the original paper.