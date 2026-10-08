# Thermal 200-Paper School V3.1 — Evidence-Controlled

**Status:** ACTIVE SCREENING ARCHITECTURE — NO UNVERIFIED BIBLIOGRAPHIC CONTENT  
**Effective date:** 2026-10-08  
**Evidence authority:** `CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`  
**State-time authority:** `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`

## 1. Purpose

The target of 200 papers is a literature-coverage target.

It is not a license to invent bibliographic records or to treat relevant papers as model evidence.

```text
200 screening positions
≠ 200 verified papers
≠ 200 full-text audits
≠ 200 model-admissible sources
```

## 2. Permanent non-invention rule

No title, authors, year, DOI, standard clause, equation, parameter, threshold, material property, operating limit, validation result, or numerical law may be guessed to fill a corpus slot.

Unverified fields remain:

```text
TO BE VERIFIED
```

## 3. Twenty screening modules

These modules are **thesis-designed screening strata**, not claims that the literature is formally partitioned in this exact way.

Each module contains 10 paper positions.

1. Transformer thermal-state physics — 10
2. Transformer thermal parameter identification and state estimation — 10
3. Transformer insulation aging / degradation states — 10
4. EV charging demand → transformer electro-thermal consequence — 10
5. EVSE thermal derating and charging capability — 10
6. EVSE converter electro-thermal physics — 10
7. Power-semiconductor junction-temperature modeling and observability — 10
8. Power-electronics thermal cycling / degradation — 10
9. Battery heat generation and electro-thermal modeling — 10
10. Battery thermal parameter identification and uncertainty — 10
11. Battery thermal-management and cooling physics — 10
12. Battery multiscale / spatial thermal modeling — 10
13. Battery thermal degradation / health-state dynamics — 10
14. Thermal-constrained charging, state estimation, and control — 10
15. Vehicle/cabin/HVAC thermal-energy demand under extreme heat — 10
16. Battery-electric fleet/bus energy and mobility-service translation — 10
17. Fleet/depot charging windows and departure constraints — 10
18. Coupled Power–Electrified Transportation interdependency mathematics — 10
19. Service trajectories, resilience metrics, and temporal definitions — 10
20. Verification, validation, uncertainty quantification, and model credibility — 10

Total:

```text
20 modules × 10 verified-paper targets = 200 verified-paper target
```

## 3A. Active Module 01 execution checkpoint

Module 01 is now actively being executed at:

`project/module_01_transformer_thermal_state_physics/`

Current checkpoint:

~~~text
P01–P10 = audited at declared, unequal evidence depths
P10 = Garelli et al. (2021); winding validation discrepancy identified; state sufficiency still OPEN
standards spine = mapped; clause-level freeze still partly OPEN
final Power thermal model = NOT FROZEN; post-P10 outcome B
~~~

Current Module 01 control files:

- `README.md`
- `MODULE_01_STANDARDS_SPINE_V1.md`
- `MODULE_01_PAPER_AUDITS_P01_P05_V1.md`
- `MODULE_01_PAPER_AUDITS_P06_P07_V1.md`
- `MODULE_01_PAPER_AUDIT_P08_V1.md`
- `MODULE_01_PAPER_AUDIT_P09_V1.md`
- `MODULE_01_PAPER_AUDIT_P10_V1.md`
- `MODULE_01_CROSS_PAPER_SYNTHESIS_P01_P05_V1.md`
- `MODULE_01_MODEL_ADMISSION_LEDGER_V1.md`
- `MODULE_01_OPEN_GAPS_V1.md`

The working candidate reduced Power thermal state vector is:

~~~math
X_P,th = [theta_TO, theta_HS]^T
~~~

with status:

~~~text
CANDIDATE — NOT FROZEN
~~~

No parameter, threshold, exact ODE, or state-to-capability law has been frozen.

## 4. Evidence hierarchy

```text
Tier A — Standards / official technical authorities / exact manufacturer or system documentation
Tier B — Peer-reviewed primary research
Tier C — Peer-reviewed review / systematic review
Tier D — Conference / preprint / technical report, clearly labeled
Tier E — Secondary web content, discovery only
```

## 4A. Claim-level provenance classes

Every extracted scientific claim, quantity, equation, threshold, or metric should be tagged where practical:

```text
[A1] Official standard / code / normative authority
[A2] Exact manufacturer / certified technical documentation
[A3] Peer-reviewed experiment / field measurement
[A4] Peer-reviewed mathematical / physics model
[A5] Recognized textbook / engineering handbook / authoritative theory
[T1] Thesis-derived from A1–A5 evidence
[OPEN] Not yet established
```

A T1 object is admissible only when its derivation is transparent and all source quantities are traceable.

```text
thesis definition ≠ invention
thesis definition ≠ standard definition
```

## 4B. Required extraction record

For each admitted paper:

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

No equation, parameter, or threshold is admitted from abstract-level evidence alone.

## 5. Module search order

For each module:

```text
standards / official technical authority
→ peer-reviewed reviews
→ trace primary studies
→ verify metadata
→ lawful full-text acquisition
→ equation/physics audit
→ parameter/threshold provenance
→ VVUQ
→ transferability test
→ thesis-admission decision
```

## 6. Bibliographic verification gate

A paper record is not verified until title, authors, year, venue, DOI/permanent identifier, publication type, and retraction/correction status are checked against authoritative metadata.

Preferred metadata authorities include:
- publisher record;
- DOI resolver / Crossref;
- recognized indexing database;
- official institutional repository linked to the publication.

## 7. Full-text mathematical/physics gate

For every model/equation considered for use:

```text
Equation
→ physical meaning
→ variables + units
→ governing principle
→ assumptions
→ initial conditions
→ boundary conditions
→ parameter provenance
→ numerical method
→ verification
→ validation
→ uncertainty
→ validity domain
→ thesis transfer decision
```

## 8. Equation classification

```text
E1 — Fundamental governing law
E2 — Standard model / procedure
E3 — Literature-derived model
E4 — Thesis-derived equation
```

E4 is allowed only when explicitly labeled as thesis-derived and traced to cited governing laws/definitions.

## 9. Parameter / threshold gate

Every numerical value requires:

```text
symbol
+ value
+ unit
+ source
+ equipment/system identity
+ operating conditions
+ uncertainty/tolerance
+ validity range
+ transferability decision
```

## 10. Admission labels

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

## 11. Supersession rule

Any earlier 200-paper draft or registry containing bibliographic metadata that has not been independently verified must be treated as a planning scaffold only.

This V3.1 evidence-controlled architecture supersedes such drafts for future corpus construction.

## 12. Governing sentence

```text
No invention fills an evidence gap.
The gap stays open until a standard, official source, or verified scientific source closes it.
```
