# Literature Anchors Used in the Current Chain Synthesis

## Status of this file

This is a **memory index of literature anchors already used in the current thesis discussion**. It is not a substitute for the frozen literature database, PRISMA evidence table, PDFs, or final bibliographic verification.

Before publication-quality citation, future work must verify title, year, journal, DOI and the exact proposition supported against the authoritative corpus/full text.

The role of this file is recall: it records which established literature families were already connected to which layers of the six-chain ontology.

---

# Chain I — Interdependencies, multilayer representation, physical/coupled systems

## Rinaldi, Peerenboom & Kelly (2001)

**Title:** *Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies*  
**DOI:** `10.1109/37.969131`

**Role in current synthesis:** canonical infrastructure-interdependency taxonomy and the distinction among physical, cyber, geographic and logical interdependencies.

**Use:** foundational support for treating interdependency as more than graph adjacency.

## Ouyang (2014)

**Title:** *Review on modeling and simulation of interdependent critical infrastructure systems*  
**DOI:** `10.1016/j.ress.2013.06.040`

**Role:** review of major interdependent-infrastructure modeling traditions; supports the claim that different mathematical representations capture different mechanisms/scales.

## Boccaletti et al. (2014)

**Title:** *The structure and dynamics of multilayer networks*  
**DOI:** `10.1016/j.physrep.2014.07.001`

**Role:** mathematical foundation for multilayer/network-of-networks representation and dynamics.

## Kivelä et al. (2014)

**Title:** *Multilayer networks*  
**DOI:** `10.1093/comnet/cnu016`

**Role:** formal multilayer-network terminology and representation.

## Buldyrev et al. (2010)

**Title:** *Catastrophic cascade of failures in interdependent networks*  
**DOI:** `10.1038/nature08932`

**Role:** canonical evidence that interdependency can qualitatively change cascading-failure behavior and generate abrupt collapse.

## Gao et al. / network-of-networks family

**Role in discussion:** broader theoretical basis for coupled-network robustness and network-of-networks behavior. Verify exact record and DOI from the frozen corpus before final citation.

## Ouyang & Dueñas-Osorio interface-topology work

**Role:** supports treating cross-system interface architecture/topology as an explicit engineering/design variable rather than only as an exogenous relation. Verify the exact bibliographic record from the corpus before final citation.

---

# Chain II — Inverse problems, Bayesian inference, identification

## Stuart (2010)

**Title:** *Inverse Problems: A Bayesian Perspective*  
**DOI:** `10.1017/S0962492910000061`

**Role:** mathematical foundation for Bayesian inverse problems, posterior uncertainty, and the distinction between a point estimate and a probability distribution over unknowns.

## Tarantola / inverse-problem foundation

**Role:** conceptual foundation for model–data inverse problems, likelihood/misfit, parameter inference and uncertainty. Exact edition/source must be taken from the authoritative bibliography before final citation.

## Infrastructure-specific inverse/source-identification studies

**Role:** current literature synthesis noted water-distribution source-identification, model-reduction for Bayesian inversion, system-identification and physics-informed parameter-estimation precedents in the corpus.

**Publication rule:** do not cite a generic recollection; retrieve the exact frozen-corpus record and full-text evidence anchor before thesis use.

---

# Chain III — Hazard, fragility, failure and cascades

## Buldyrev et al. (2010)

See above. Used here for cascading dependence.

## Mühlhofer et al. (2023) generalized infrastructure-failure cascade / natural-hazard risk work

**Role:** current synthesis used this literature family to connect natural hazards, infrastructure failures and cascades. Exact record/DOI must be retrieved from the authoritative corpus before final citation.

## Fragility literature

Representative mathematical family used in the discussion:

```text
P(D_i >= d_s | IM) = Phi((ln IM - ln mu_i,ds)/beta_i,ds)
```

This formula is a generic lognormal fragility form, not a claim that all infrastructure components share the same fragility model. Parameterization and citation must be sector/hazard specific.

---

# Chain IV — Resilience, viability, reachability, recovery

## Viability theory foundations

### *A Survey of Viability Theory*

Current corpus discussion associated this title with DOI `10.1137/0328045`. A prior dataset contained an identity/DOI conflict warning for a similarly named viability item, so **the final bibliographic identity must be checked directly before publication**.

### *Viability Problems for Nonautonomous Differential Inclusions*

Current discussion associated DOI: `10.1137/0329014`.

### *Approximation of the viability kernel*

DOI: `10.1007/BF01204182`

**Role:** numerical viability-kernel approximation / viability foundations.

## Mitchell, Bayen & Tomlin (2005)

**Title:** *A Time-Dependent Hamilton-Jacobi Formulation of Reachable Sets for Continuous Dynamic Games*  
**DOI:** `10.1109/TAC.2005.851439`

**Role:** Hamilton–Jacobi reachability, reachable sets, dynamic games, viscosity-solution framework.

**Important formula caveat:** the sign and min/max order in an HJ/HJI Hamiltonian depend on the declared target/disturbance/control convention; future work must derive rather than copy the generic form.

## Bruneau et al. (2003)

**DOI:** `10.1193/1.1623497`

**Role:** established infrastructure/community resilience-performance framing and recovery-curve concepts.

## Cimellaro et al. (2010)

**DOI:** `10.1016/j.engstruct.2010.08.008`

**Role:** quantitative resilience-performance formulation/recovery literature.

## Hosseini et al. (2016)

**DOI:** `10.1016/j.ress.2015.08.006`

**Role:** resilience definitions/measures review and synthesis.

## Panteli et al. / power-system resilience family

**Role:** power-system resilience assessment and restoration/performance literature; retrieve exact record from the frozen corpus for final citation.

---

# Chain V — Restoration, design, optimization and adaptation

## Nurre et al. (2012)

**DOI:** `10.1016/j.ejor.2012.07.010`

**Role:** integrated network design/scheduling/restoration optimization family.

## Cavdaroglu et al. / interdependent restoration family

**Role:** joint/interdependent infrastructure restoration and repair scheduling under dependencies/resources. Exact record should be recovered from the frozen bibliography.

## Ouyang & Wang (2015)

**DOI:** `10.1016/j.ress.2015.03.011`

**Role in current discussion:** resilience/restoration modeling of interdependent infrastructures; verify exact title from authoritative corpus before final thesis citation.

## Recent multi-timescale water–power restoration paper

**Title:** *Multi-timescale risk-averse restoration for interdependent water-power networks with joint reconfiguration and diverse uncertainties*  
**DOI:** `10.1016/j.ress.2025.111083`

**Role:** one of the strongest corpus-relative precedents for timescale-aware interdependent restoration/control/uncertainty.

---

# Chain VI — Sustainability, equity and decision

## Coleman et al. (2024)

**Title:** *Weaving equity into infrastructure resilience research: a decadal review and future directions*  
**DOI:** `10.1038/s44304-024-00022-x`

**Role:** supports treating equity as multidimensional rather than a single generic inequality score; current discussion referenced distributional-demographic, distributional-spatial, procedural and capacity dimensions.

## Sustainability/climate-resilience transport recovery paper

**Title:** *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery*  
**DOI:** `10.1016/j.trd.2023.103800`

**Role:** important corpus-relative bridge between sustainability, climate resilience, asset recovery and trade-offs.

## NIST Community Resilience Planning Guide

**Role:** connects resilience analysis to community performance goals, planning and implementation. Use the official NIST record when citing.

---

# Literature maturity interpretation preserved from the current discussion

The current synthesis treats these areas as already mature or substantially established:

- infrastructure interdependency taxonomies;
- multilayer/network representation;
- cascading network failure;
- classical resilience performance metrics;
- restoration optimization;
- general viability theory and HJ reachability;
- general inverse-problem mathematics.

The narrower integration questions identified for falsification are:

- dynamic interface identification in coupled infrastructure;
- propagation of interface-identification uncertainty into viability/recovery boundaries;
- timescale-dependent validity of static coupling;
- viability-boundary-based interface criticality;
- sustainability/equity as hard viability/admissibility constraints;
- capture/recovery geometry for coupled P–W–T–SW systems;
- waste–drainage–flood feedback inside viability analysis;
- conservative reduced-order preservation/bounding of viability decisions.

These are **candidate integration gaps**, not globally proven novelty claims.

---

# Citation discipline for future chats

Future chats must classify every literature statement as one of:

1. directly verified from full text / evidence table;
2. verified bibliographic metadata only;
3. carried forward from current literature synthesis and awaiting re-verification;
4. mathematical background/general knowledge;
5. proposed thesis interpretation.

Do not silently promote category 3–5 to category 1.