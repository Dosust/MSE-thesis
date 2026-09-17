# Concept Definition and Operationalization Register

**Status:** CURRENT GOVERNANCE REGISTER  
**Effective date:** 2026-09-17  
**Purpose:** prevent conceptual drift between literature review, mathematical framework, experiments, results and discussion.

## Governing chain

```math
\boxed{
\text{Literature meanings}
\rightarrow
\text{thesis-adopted definition}
\rightarrow
\text{operational representation}
\rightarrow
\text{unit/domain}
\rightarrow
\text{evidence/data}
\rightarrow
\text{validity boundary}.
}
```

No concept is allowed to change meaning silently between chapters.

## Required fields

| Field | Meaning |
|---|---|
| Concept ID | stable ID `D###` |
| Concept | term used in thesis |
| Literature definition(s) | evidence-supported meanings and disagreements |
| Adopted thesis definition | exact meaning used in this thesis |
| Operational representation | variable/set/function/metric/model object |
| Units/domain | units and admissible domain where applicable |
| Evidence/provenance | supporting sources/data |
| Assumptions | conditions imposed by thesis |
| Validity boundary | where the definition/measure applies |
| RQ/Stage | research role |
| Status | OPEN / QUALIFIED / FROZEN |

## Initial canonical concepts

| ID | Concept | Adopted thesis definition / role | Operational representation | RQ / Stage | Status |
|---|---|---|---|---|---|
| D001 | Dependency | directional relation in which a source supplies/changes a resource, service or condition required by a receiver | `\mathfrak d_e` | RQ2 / Stage 2 | QUALIFIED STRUCTURE |
| D002 | Interdependency | reciprocal or coupled composition of directional dependencies whose effects can feed across constituent systems; exact composition must be stated | `\mathbb I`, dependency pair/composition | RQ2 / Stage 2 | QUALIFIED STRUCTURE |
| D003 | Interface | component-to-component or layer-to-layer locus through which a declared mechanism acts; not merely geographic proximity | source–mechanism–receiver object | RQ1–RQ2 | QUALIFIED STRUCTURE |
| D004 | Critical service | electricity, mobility or coupled service quantity with declared acceptable bounds over space/time | `Q(Y,t)`, `K(t)` | RQ1/RQ5 | OPEN VALUES |
| D005 | Resilience | ability to maintain acceptable service, recover acceptable service, and quantify confidence under uncertainty | `\mathfrak R_T=(\mathcal V,\mathcal R,\rho_{\mathcal V},T_{\mathcal V},T_{\rm rec},P_{\rm viable},P_{\rm recover})` | RQ5 / Stage 5 | STRUCTURE FROZEN / VALUES OPEN |
| D006 | Viability | existence of feasible control/policy keeping service within the acceptable set over the maintainability horizon under declared uncertainty semantics | `\mathcal V_{\alpha,T}` | RQ5 | STRUCTURE FROZEN |
| D007 | Reachability / recovery | existence of feasible control/policy reaching the recovery target before unacceptable failure within the recovery horizon | `\mathcal R_{\beta,T}` | RQ5 | STRUCTURE FROZEN |
| D008 | Effectiveness | whether an intervention achieves its preregistered resilience/service target | `\mathcal E_{\rm fx}(a_k)` or declared target vector | RQ6 / Stage 6 | CONCEPT FROZEN / METRIC OPEN |
| D009 | Efficiency | resources required relative to achieved intervention outcome; not assumed scalar | `\mathcal E_{\rm fy}(a_k)`, resource vector `\mathbf C_{\rm res}^{a_k}` | RQ6 / Stage 6 | CONCEPT FROZEN / METRIC OPEN |
| D010 | Sustainability consequence | evidence-supported accessibility, energy, carbon, cost and other declared consequences of the intervention-induced trajectory within stated accounting boundaries | `\mathbf J_{\rm sus}^{a_k}` | RQ6 / Stage 6 | CORE VECTOR FROZEN / DETAILS OPEN |
| D011 | Interface criticality | supporting diagnostic measuring how an interface affects declared resilience/decision quantities; not a primary H4 claim unless separately preregistered | declared `C_{ij}`/`S_{ij}` diagnostic | RQ5–RQ6 | SUPPORTING / TEST OPEN |
| D012 | Operational control | feasible action applied to operate the current system without redefining its strategic architecture | `u(t)\in\mathcal U_t` | RQ4 | QUALIFIED STRUCTURE |
| D013 | Strategic intervention | action that changes system structure, mechanism, resources, control capability or service design | `a_k\in\mathcal A` | RQ6–RQ7 | QUALIFIED STRUCTURE |
| D014 | Transformation pathway | conditional sequence/policy of strategic interventions; active only if justified by scope, data and preregistration | `a_{0:H}` or declared adaptive policy | RQ7 / Stage 7 | CONDITIONAL EXTENSION |
| D015 | Uncertainty | declared lack of knowledge/variability represented by evidence-supported probability, interval, scenario or other admissible semantics | `U_i`, distributions/sets/scenarios | cross-cutting | OPEN BY EXPERIMENT |

## Operationalization rule

A term may enter confirmatory analysis only after the following are fixed or explicitly declared open under a preregistration gate:

```math
\boxed{
\text{definition}
+\text{representation}
+\text{units/domain}
+\text{data/provenance}
+\text{threshold/decision role}
+\text{uncertainty}
+\text{validity boundary}.
}
```

## Chapter use

- **Chapter II:** compare literature definitions and disagreements.
- **Chapter III:** state the adopted thesis definition and mathematical object.
- **Chapter IV:** operationalize measurement/model/test rules.
- **Chapter V:** report only quantities whose operationalization is frozen for that experiment.
- **Chapter VI:** discuss interpretation limits and alternative definitions where relevant.
- **Chapter VII:** preserve the same meaning used in the tested result.

## Change control

Changing an adopted definition after confirmatory results are visible requires a dated amendment stating:

1. the original definition;
2. the revised definition;
3. reason for change;
4. whether results had been observed;
5. which experiments and conclusions become exploratory or require re-execution.
