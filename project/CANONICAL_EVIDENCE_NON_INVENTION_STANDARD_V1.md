# Canonical Evidence and Non-Invention Standard V1

**Status:** CANONICAL — FROZEN THESIS-WIDE EVIDENCE RULE
**Effective date:** 2026-10-08
**Repository:** `Dossiya-SE/MSE-thesis`
**Applies to:** literature review, equations, variables, states, parameters, thresholds, constitutive laws, capability laws, service definitions, resilience metrics, sustainability indicators, numerical values, figures, code, validation, and conclusions.

## 0. Mandatory AI / agent rule

This file is a **mandatory repository authority for every AI system, coding assistant, research agent, literature-review agent, visualization agent, and human contributor working on the active thesis**.

Before producing or modifying any active scientific content, the agent must load and apply this file.

This requirement applies to:
- literature searches and paper summaries;
- equations and derivations;
- standards interpretation;
- parameter and threshold selection;
- physical mechanisms;
- model architecture;
- code and simulation;
- figures and diagrams;
- validation and uncertainty claims;
- service, resilience, sustainability, and SDG interpretation;
- research questions, hypotheses, results, discussion, and conclusions.

Permanent AI behavior:

```text
Do not invent.
Do not guess a source.
Do not guess a DOI.
Do not guess a standard clause.
Do not guess a threshold.
Do not guess a parameter.
Do not promote an assumption to established fact.
Do not promote a thesis definition to a standard definition.
Do not transfer a numerical law across equipment/cases without a transferability justification.
If the evidence is unavailable or unverified, mark it OPEN / UNKNOWN / NOT YET QUALIFIED.
```

Any AI-generated scientific object must remain subordinate to verified evidence and the repository authority hierarchy.

## 1. Non-invention rule

> **No scientific object may be introduced into the active thesis as established fact, equation, parameter, threshold, limit, mechanism, standard requirement, or validated model unless it is traceable to an authoritative source appropriate to that claim.**

The thesis must never fill an evidence gap by inventing:
- a paper or citation;
- a DOI, title, author list, year, journal, or standard clause;
- an equation presented as literature-established;
- a threshold or operating limit;
- a parameter value;
- a material property;
- a transformer thermal constant;
- an EVSE derating temperature or curve;
- a battery charging-temperature limit;
- a BMS rule;
- a service requirement;
- an uncertainty bound;
- a validation result;
- a resilience or sustainability metric presented as standard;
- a numerical result.

If authoritative evidence is unavailable, the correct status is:

```text
OPEN / UNKNOWN / NOT YET QUALIFIED
```

not an estimated or convenient substitute.

## 2. Evidence hierarchy

### Tier A — Normative / official authority

Preferred when the claim concerns requirements, limits, definitions, procedures, safety, standardized test conditions, or engineering practice.

Examples:
- ISO;
- IEC;
- IEEE standards/guides;
- SAE standards;
- ASME V&V / VVUQ standards and guides;
- NIST;
- national laboratories / official government datasets;
- official utility, transit-agency, fleet, or system-operator data;
- manufacturer datasheets, technical manuals, and certified operating envelopes for the exact equipment studied.

Tier A is the default authority for:
- standard definitions;
- equipment ratings;
- standardized thermal limits/procedures;
- declared operating envelopes;
- test procedures;
- required units and reporting conventions where applicable.

### Tier B — Peer-reviewed primary research

Preferred for:
- experimentally measured thermal relationships;
- validated component models;
- field observations;
- mechanism identification;
- parameter-identification methods;
- case-specific performance;
- uncertainty/validation results.

A peer-reviewed paper does not automatically authorize parameter transfer to another technology, device, fleet, climate, or operating regime.

### Tier C — Peer-reviewed review / systematic review

Use for:
- field mapping;
- terminology;
- model families;
- identifying primary studies;
- comparing methodologies;
- identifying limitations and unresolved gaps.

A review is not the preferred final provenance for a case-specific parameter, threshold, or validated constitutive law when the underlying primary source can be traced.

### Tier D — Conference paper / preprint / technical report

May support emerging methods, preliminary findings, comparison, or discovery. It must be clearly labeled and cannot silently replace stronger available evidence.

### Tier E — Secondary web content

Blogs, summaries, search snippets, commercial pages without primary technical documentation, AI-generated summaries, and unattributed web text are not admissible scientific evidence for model freezing. They may be used only to locate the authoritative source.

## 2A. Claim-level authority classes

In addition to the broad source tiers above, every thesis quantity, equation, threshold, mechanism, or metric should carry a **claim-level provenance class** where practical:

| Class | Source | Permitted use |
|---|---|---|
| **A1** | Official standard / code / normative authority | definitions, ratings, limits, required procedures, test methods, accepted equations where explicitly specified |
| **A2** | Exact manufacturer / certified technical documentation | component-specific ratings, operating envelopes, derating curves, tolerances, parameters |
| **A3** | Peer-reviewed experiment / field measurement | observed physical relationships, measured behavior, validation evidence |
| **A4** | Peer-reviewed mathematical / physics model | governing/model equations, constitutive relations, numerical formulation, parameter-identification method |
| **A5** | Recognized textbook / engineering handbook / authoritative theory source | fundamental laws, standard derivations, dimensional and physical foundations |
| **T1** | Thesis-derived quantity / equation / metric | transparent derivation from A1–A5 evidence; must be explicitly labeled thesis-derived |
| **OPEN** | Not yet established | no verified authority sufficient for freezing |

These claim-level classes do **not** imply that all standards outrank all experiments for every claim. The claim-to-source matching rule controls which source type is authoritative for the specific scientific object.

Permanent rule:

```text
A1–A5 = externally established authority/evidence
T1 = thesis-derived from established evidence
OPEN = evidence not yet sufficient
```

A T1 object is scientifically admissible only when its source chain is explicit and its derivation is checked. It must never be described as standard-defined, manufacturer-defined, or literature-established.

## 2B. Standard information versus scientific-model information

Standards and papers have different roles.

Standards/official authorities are preferred for:

```text
terminology
+ ratings
+ operating envelopes
+ safety/thermal limits
+ test procedures
+ interface requirements
+ reporting conventions
```

Peer-reviewed primary research is preferred for:

```text
physical mechanism
+ measured constitutive behavior
+ model structure
+ parameter identification
+ validation
+ uncertainty
+ limitations
```

Therefore:

```text
standard definition ≠ physical constitutive law
standard scope ≠ validated case-specific model
```

A standard defining an EVSE, transformer loading procedure, or interface does not automatically supply a case-specific relation such as
`P_charge,max = f(T)` unless that relation is explicitly contained and applicable.

## 3. Claim-to-source matching rule

```text
Standard requirement
→ standard / official technical authority

Equipment-specific limit
→ exact manufacturer documentation or validated experiment for that equipment

Physical mechanism
→ peer-reviewed primary evidence and/or established physical theory

Model equation
→ derivation from established governing law or traceable literature source

Parameter value
→ exact case source, calibrated data, or compatible validated source

Threshold
→ standard, manufacturer, experiment, or explicitly justified operational requirement

Service requirement
→ fleet/operator/system requirement or explicitly defined research requirement

Validation claim
→ independent comparison with declared data and error metric
```

## 4. Equation admission rule

Every active equation must be classified as one of:

### E1 — Fundamental / governing law
Required: authoritative theory/reference, variables and units, assumptions, initial/boundary conditions, and domain of applicability.

### E2 — Standard model / standard procedure
Required: exact standard/guide identifier, edition/year, clause/equation reference where available, required inputs, and validity conditions.

### E3 — Literature-derived model
Required: exact primary paper, equation number or derivation location, model assumptions, parameter definitions, and validation domain.

### E4 — Thesis-derived equation
A new derivation is allowed only when explicitly labeled as **derived in this thesis**.

Required:
- derivation from cited governing laws/definitions;
- dimensional consistency;
- assumptions;
- mathematical verification;
- validation or limiting-case checks where applicable.

A thesis-derived equation must never be presented as an existing standard or literature equation.

## 4A. Equation provenance record

Every equation considered for active use must carry a provenance record containing, at minimum:

```text
equation identifier
+ provenance class (A1/A2/A3/A4/A5/T1)
+ exact source
+ standard number / DOI / permanent identifier where applicable
+ equation / clause / page / derivation location where available
+ physical meaning
+ variables
+ units
+ assumptions
+ initial conditions
+ boundary conditions
+ parameter sources
+ validity domain
+ verification status
+ validation status
+ uncertainty treatment
+ thesis-transfer decision
```

A generic relation such as

```math
C_{th}\frac{dT}{dt}
=
P_{loss}
-
\frac{T-T_a}{R_{th}}
```

must not automatically be called **the transformer model**, **the charger model**, or **the battery model**. It is only a generic lumped energy-balance form until a source, component interpretation, parameters, assumptions, boundary conditions, and validation domain are established.

## 5. Parameter and threshold admission rule

Every numerical parameter/threshold must have a provenance record:

```text
name
+ symbol
+ value
+ unit
+ source
+ equipment/system identity
+ operating conditions
+ uncertainty/tolerance
+ validity range
+ transferability decision
```

No parameter may be copied from a paper solely because the paper studies the same broad technology.

## 6. Paper metadata rule

A bibliographic record is not considered verified until at least one authoritative metadata source confirms the record, preferably:
- DOI resolver / Crossref metadata;
- publisher page;
- indexing database;
- official institutional repository linked to the published record.

For each paper record, verify title, authors, year, venue, DOI/permanent identifier, publication type, and retraction/correction status where relevant.

Unverified bibliographic slots must remain blank and labeled:

```text
TO BE VERIFIED
```

They must never be populated with guessed titles, authors, dates, or DOIs.

## 7. Standards rule

When a standard is used, record:
- organization;
- standard number;
- full title;
- edition/year;
- relevant clause/table/equation;
- whether access was direct full-text or secondary citation.

Do not claim a requirement from a standard based only on another paper's paraphrase when direct verification is needed for the thesis claim.

## 8. Full-text rule

Abstract-level evidence may support relevance screening.

It may not by itself authorize equation adoption, parameter adoption, threshold adoption, validation claims, detailed assumptions, boundary conditions, or limitations not stated in the accessible source.

Permanent distinction:

```text
relevant abstract
≠ full-text audited paper
≠ model evidence
≠ parameter evidence
```

## 9. Mathematical/physical audit required for every admitted paper

```text
Equation
→ Physical meaning
→ Variables + units
→ Governing principle
→ Assumptions
→ Initial conditions
→ Boundary conditions
→ Parameter provenance
→ Numerical method
→ Verification
→ Validation
→ Uncertainty
→ Validity domain
→ Thesis transfer decision
```

For every mechanism:

```text
Cause
→ physical mechanism
→ state
→ capability/constraint
→ cross-system exchange
→ receiver consequence
→ service consequence
→ time scale
→ supporting evidence
```

## 10. Transferability rule

A finding may be physically relevant while still being non-transferable to the thesis case.

Before transferring a result, check equipment type/model, rating, materials/chemistry, cooling architecture, ambient range, loading/duty cycle, control/BMS logic, spatial scale, time scale, measurement method, and validation domain.

Use:

```text
MECHANISM EVIDENCE ONLY
```

when the mechanism is supported but the numerical law/parameter is not transferable.

## 11. Model-development rule

The thesis may derive new models, but novelty must come from transparent synthesis or derivation, not fabricated physics.

```text
standard governing physics
+ traceable evidence
+ explicit assumptions
+ thesis derivation
+ dimensional/mathematical verification
+ validation
+ uncertainty
```

Use the phrase `derived in this thesis from ...` for a thesis derivation. Do not call a relation a standard equation unless that status is directly verified.

## 11A. Thesis-defined objects

A thesis-defined object is permitted when a standardized metric or equation does not exist, but it must be visibly labeled **T1 — THESIS-DERIVED**.

Example:

```math
Q_T(t_d)
=
\frac{N_{departure-ready}}{N_{scheduled}}
```

may be a defensible thesis-defined mobility-service metric only if its underlying quantities are independently sourced and operationally defined.

For a T1 metric, record:

```text
definition
+ purpose
+ derivation
+ source quantities
+ units
+ assumptions
+ system boundary
+ time basis
+ sensitivity
+ validation / reasonableness checks
```

Permanent distinction:

```text
thesis definition ≠ invention
thesis definition ≠ standard definition
```

A defensible thesis definition is a transparent construction from established quantities; an unsupported convenient formula is not.

## 11B. Required 200-paper extraction structure

For every paper admitted to the 200-paper reading school, extract:

```text
1. Standard / authority context
2. Physical principle
3. Governing mathematics
4. Parameters + units
5. Initial conditions + boundary conditions
6. Experimental / numerical method
7. Verification + validation
8. Limitation + validity domain
9. What remains unknown
10. Transferability to this thesis
```

Every extracted scientific claim should, where practical, carry one of:

```text
[A1] Standard-defined
[A2] Manufacturer/certified technical documentation
[A3] Experimentally observed
[A4] Peer-reviewed model
[A5] Fundamental established physics
[T1] Thesis-derived
[OPEN] Not established yet
```

## 12. Evidence-status labels

```text
VERIFIED — STANDARD/OFFICIAL
VERIFIED — PRIMARY PEER-REVIEWED
VERIFIED — REVIEW/BACKGROUND
MECHANISM EVIDENCE ONLY
CANDIDATE — FULL-TEXT AUDIT PENDING
CANDIDATE — PARAMETER VALIDATION PENDING
CANDIDATE — TRANSFERABILITY PENDING
OPEN / UNKNOWN
EXCLUDED
```

## 13. 200-paper school rule

The target of 200 papers is a coverage target, not a license to populate a bibliography artificially.

```text
200 paper positions
≠ 200 verified papers
≠ 200 admitted models
```

The final corpus reaches 200 only when 200 unique bibliographic records have verified metadata. The mathematical model may ultimately use far fewer papers if only a subset survives the evidence/admission gates.

## 14. Conflict rule

When sources disagree:
1. do not average or reconcile silently;
2. identify the disagreement;
3. compare equipment, assumptions, test conditions, scale, and uncertainty;
4. prefer the source most compatible with the selected case and strongest evidence;
5. report unresolved disagreement where it remains.

## 15. Scientific writing rule

Use calibrated statements such as:

```text
demonstrated by
measured under
validated for
reported within
derived assuming
applicable over
not established for
transferability remains unverified
```

Avoid unsupported absolutes such as `always`, `universal`, `standard threshold`, `proven`, `optimal`, or `validated` unless the evidence warrants them.

## 16. Permanent non-invention statement

```text
If it cannot be traced, it is not frozen.
If it cannot be verified, it remains open.
If it is thesis-derived, it is labeled thesis-derived.
If it is transferred, transferability must be justified.
If evidence conflicts, the conflict is reported.
```