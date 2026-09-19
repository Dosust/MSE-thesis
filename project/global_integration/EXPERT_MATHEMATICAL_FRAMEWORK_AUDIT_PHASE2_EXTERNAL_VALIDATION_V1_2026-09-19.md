# Expert Mathematical Framework Audit — Phase 2: External Validation and Comparison

**Date:** 2026-09-19  
**Scope:** Compare the Phase-1 repository-only findings against authoritative standards and peer-reviewed mathematical/control literature.  
**Rule:** External sources validate or constrain the thesis framework; they do not silently overwrite frozen repository authorities.

## 1. External reference set

1. ISO/IEC/IEEE 15288:2023 — Systems and software engineering — System life cycle processes.  
   https://www.iso.org/standard/81702.html

2. NASA-STD-7009B — Standard for Models and Simulations; NASA-HDBK-7009B, 2026 implementation guide.  
   https://standards.nasa.gov/node/263  
   https://standards.nasa.gov/node/198

3. Goebel, Sanfelice & Teel — Hybrid Dynamical Systems: Modeling, Stability, and Robustness; hybrid flow/jump semantics.  
   DOI: 10.23943/princeton/9780691153896.001.0001

4. Sanfelice & Teel (2010), Dynamical properties of hybrid systems simulators, Automatica 46(2), 239–248.  
   DOI: 10.1016/j.automatica.2009.09.026

5. FMI 3.0.2 — Functional Mock-up Interface, Model Exchange / Co-Simulation.  
   https://fmi-standard.org/docs/3.0.2/

6. Aubin, Bayen & Saint-Pierre (2011), Viability Theory: New Directions.  
   https://link.springer.com/book/10.1007/978-3-642-16684-6

7. Abate, Prandini, Lygeros & Sastry (2008), Probabilistic reachability and safety for controlled discrete time stochastic hybrid systems, Automatica 44(11).  
   DOI: 10.1016/j.automatica.2008.03.027

8. Summers & Lygeros (2010), Verification of discrete time stochastic hybrid systems: A stochastic reach-avoid decision problem, Automatica.  
   DOI: 10.1016/j.automatica.2010.08.006

9. Rinaldi, Peerenboom & Kelly (2001), Identifying, understanding, and analyzing critical infrastructure interdependencies, IEEE Control Systems Magazine 21(6), 11–25.  
   DOI: 10.1109/37.969131

10. Hernán & Robins, Causal Inference: What If.  
    https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf

11. JCGM 101:2008 — Propagation of distributions using a Monte Carlo method.  
    DOI: 10.59161/JCGM101-2008

12. ISO 14040:2006 and ISO 14044:2006 — LCA principles/framework and requirements/guidelines; confirmed current by ISO in 2022.  
    https://www.iso.org/standard/37456.html  
    https://www.iso.org/standard/38498.html

13. ISO/TS 14074:2022 — normalization, weighting and interpretation in LCA.  
    https://www.iso.org/standard/61117.html

14. RAND Robust Decision Making / deep-uncertainty literature, including `Shaping the Next One Hundred Years`.  
    https://www.rand.org/pubs/monograph_reports/MR1626.html

## 2. Comparison results

### A. Systems-engineering chain

**External finding:** ISO/IEC/IEEE 15288:2023 explicitly supports life-cycle process discipline for systems and systems of systems.

**Thesis implication:** the stage-gated architecture, explicit handoffs, provenance, verification and validation separation are consistent with modern systems-engineering practice.

**Decision:** VALIDATED AS A SOUND ARCHITECTURAL PRINCIPLE.

### B. Infrastructure dependency semantics

**External finding:** Rinaldi et al. distinguish dependencies/interdependencies and emphasize multidimensional, complex adaptive behavior.

**Thesis implication:** Stage 1's firewall
```math
\text{proximity/common exposure}\neq\text{dependency}
```
and Stage 2's mechanism qualification are strongly defensible.

**Decision:** SUPPORTED.

### C. Causal qualification

**External finding:** modern causal inference requires explicit assumptions to identify causal effects from observational data; consistency and exchangeability are among central identification concepts in Hernán & Robins.

**Thesis implication:** the Stage-2 engineering mechanism gate is useful, but `G2=PASS` must not be described as proof of a statistically identified causal effect magnitude unless an appropriate causal-identification design exists.

**Decision:** FRAMEWORK SUPPORTED, CLAIM CEILING MUST REMAIN RESTRICTED.

### D. Hybrid-system mathematics

**External finding:** standard hybrid-system formulations explicitly use:
- flow set;
- flow map;
- jump set;
- jump map.

Hybrid simulation results can depend on numerical discretization and must be checked for solution fidelity.

**Thesis implication:** Stage 3 should normalize the mathematical core to an explicit flow/jump representation, even when the implementation is DAE/co-simulation:

```math
\mathscr H_3=(C,F,D,J)
```

augmented by algebraic constraints and topology/mode state where required.

A guard-only expression is not enough; the domain on which flow and jump are admissible matters.

**Decision:** PHASE-1 CORRECTION R6 CONFIRMED.

### E. Co-simulation and multirate semantics

**External finding:** FMI 3.0.2 explicitly separates Model Exchange from Co-Simulation and notes that co-simulation exchanges data at communication points while subsystems evolve independently between them.

**Thesis implication:**
```math
\text{physical causal delay}
\neq
\text{solver step}
\neq
\text{co-simulation communication interval}.
```

Different subsystem timescales do not by themselves prove that a multirate algorithm is required; numerical choice must follow stability/accuracy/convergence evidence.

**Decision:** PHASE-1 STAGE-3 TIMING CORRECTION CONFIRMED.

### F. Verification, validation and credibility

**External finding:** NASA-STD-7009B and the active 2026 NASA-HDBK-7009B treat verification, validation, uncertainty, sensitivity and model-use credibility as distinct activities. NASA guidance explicitly warns against empirical validation before adequate model verification.

**Thesis implication:** the repository rule
```math
\text{verification}\neq\text{validation}\neq\text{hypothesis testing}
```
is externally supported, and the current Stage-3 runtime qualification must remain implementation verification rather than thesis validation.

**Decision:** STRONGLY SUPPORTED.

### G. Viability mathematics

**External finding:** viability theory is fundamentally state-constraint/control mathematics; viability kernels belong to a specified state space and admissible dynamics/control class.

**Thesis implication:** a physical-state viability kernel and a belief-space stochastic safety set are distinct mathematical objects.

Recommended notation:
```math
\mathcal V_T^x\subseteq\mathcal X_R
```
for physical/robust viability and
```math
\mathcal V_{\alpha,T}^{b}\subseteq\mathcal B
```
for belief-conditioned probabilistic maintainability.

**Decision:** PHASE-1 C1 STATE-SPACE CORRECTION CONFIRMED.

### H. Probabilistic reachability / reach-avoid

**External finding:** Abate et al. and Summers & Lygeros formulate finite-horizon probabilistic safety/reach-avoid using stochastic control and dynamic programming, with target and unsafe sets and control policies.

**Thesis implication:** Stage 5's reach-avoid architecture is mathematically legitimate, but policy information structure and the probability model must be explicit. Where no defensible probability model exists, robust/set/scenario formulations are preferable.

**Decision:** STAGE-5 CORE SUPPORTED WITH NONANTICIPATIVITY/PROBABILITY GATES.

### I. Uncertainty propagation

**External finding:** JCGM 101:2008 provides a rigorous Monte Carlo framework for propagation of input probability distributions through a mathematical model.

**Thesis implication:** Monte Carlo/Sobol-style propagation is valid only after the relevant distributions or uncertainty models are justified; epistemic ignorance must not be silently converted into probability.

**Decision:** REPOSITORY UNCERTAINTY FIREWALL SUPPORTED.

### J. Sustainability accounting

**External finding:** ISO 14040/14044 require explicit goal/scope, inventory, impact assessment/interpretation, limitations and critical review for LCA. ISO/TS 14074 explicitly addresses normalization/weighting and their limitations.

**Thesis implication:** Stage 6 must retain:
- functional unit;
- lifecycle/system boundary;
- inventory provenance;
- native units;
- uncertainty;
- separation of disruption/recovery horizon from lifecycle horizon.

An arbitrary sustainability budget vector is not sufficient evidence by itself.

**Decision:** CURRENT REPOSITORY STAGE-6 ARCHITECTURE IS STRONGER THAN THE SIMPLIFIED PROMPT.

### K. Multiobjective / value model

**External finding:** normalization and weighting require explicit interpretive choices; robust-decision literature under deep uncertainty emphasizes robustness, regret and vulnerability across plausible futures rather than optimizing under unsupported probabilities.

**Thesis implication:** Stage 7's existing sequence
```math
\text{feasibility}
\to\text{native units}
\to\text{Pareto}
\to\text{robustness/regret}
\to\text{preference model if justified}
```
is more defensible than the proposed weighted scalar objective.

**Decision:** PHASE-1 R5 CONFIRMED.

## 3. Externally validated correction set

| ID | Severity | External comparison result |
|---|---|---|
| E1 | C1 | Separate physical-state and belief-space viability objects. |
| E2 | C1 | Explicitly constrain Stage-5 policies by information/nonanticipativity. |
| E3 | C1 | Do not use a derivative w.r.t. undefined/noncanonical coupling strength as the default interface-criticality metric. |
| E4 | C1 | Use the canonical Stage-6 intervention → consequence → candidate-requirement chain, with lifecycle functional unit/boundary. |
| E5 | C1 | Keep Pareto/robustness/regret as Stage-7 default; scalar weights require a legitimate value model. |
| E6 | C2 | Add explicit flow/jump sets to the Stage-3 mathematical abstraction. |
| E7 | C2 | Separate physical delay, event timing, numerical step and communication interval. |
| E8 | C2 | Treat stochastic probability as conditional on a justified probability model. |
| E9 | C2 | Preserve verification-before-validation and use-specific credibility. |
| E10 | C2 | Define sustained recovery when the engineering requirement is stable restoration rather than first target entry. |

## 4. External-validation decision

```math
\boxed{
G_{framework}^{external}
=
SUPPORTED\;WITH\;TARGETED\;MAJOR\;CORRECTIONS.
}
```

No external source invalidates the seven-stage thesis architecture. The strongest external evidence instead supports its major firewalls while requiring more precise Stage-3 hybrid semantics and Stage-5 state/information semantics.

The external comparison also confirms that the current repository authorities for Stages 6 and 7 are scientifically stronger than the simplified mathematical framework drafted in the audit prompt.
