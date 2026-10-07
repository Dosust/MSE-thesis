# Canonical Extreme-Heat State-Time Scope Amendment V1

**Status:** CANONICAL CURRENT-SCOPE AMENDMENT  
**Effective date:** 2026-10-07  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

## 1. Purpose

This amendment reconciles the active thesis scope with the research direction developed after the September 2026 broad seven-stage architecture.

It does **not** delete prior work. It changes which scientific objects are current for the active thesis workstream and which remain historical/provenance or reusable methodological resources.

## 2. Authority precedence

For questions of **current thesis scope**, use this order:

1. `CANONICAL_THESIS_TITLE_V1.md`
2. `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`
3. this file: `CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`
4. `CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
5. `RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`
6. `ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md`
7. `CONCEPTUAL_FRAMEWORK_SPEC_V3.md`
8. `MATHEMATICAL_FRAMEWORK_SPEC_V1.md`
9. `RESEARCH_REASONING_PROTOCOL.md`
10. `EGMIV_METHOD_V1.md`

ASU/SSEBE/committee requirements remain higher authority for degree, formatting, defense, and program compliance.

## 3. Current active scope

The active workstream is:

```text
Extreme heat
→ selected Power / interface / electrified-transport physical states
→ state-time evolution
→ critical transition timing
→ interdependency propagation timing
→ electricity + mobility service consequence
→ Improve / Adapt / Restore
→ Learn
```

### Physical core

```text
Power System P
↔
Physical Power–Transport Interfaces I_PT
↔
Electrified Transportation T
```

### Current transport mode

```text
Road transport
→ battery-electric road transportation
→ grid-connected EV charging
```

Status: **WORKING-FROZEN**.

### Canonical Electrified Transportation System boundary

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

Composition/boundary authority: `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`.

For the active thesis, EVSE and the physical charging connection belong to the Electrified Transportation System `T_e`. The Power–Transportation coupling/interface object represents exchanged quantities, coupling conditions, constraints, and interface states between `P` and `T_e`; it is not a third physical infrastructure system and is not synonymous with EVSE.

### Exact charging context

```text
public DC fast charging
vs
fleet/depot charging
```

Status: **OPEN**.

## 4. Current mathematical focus

State and time are the primary analytical variables.

```math
H(x,t)
\rightarrow
X(t)
\rightarrow
\{\tau_i^C,\delta_{ij},Q_P(t),Q_T(t)\}
\rightarrow
\{\text{Improve},\text{Adapt},\text{Restore}\}.
```

with

```math
X(t)=[X_P^\top,Z^\top,X_T^\top]^\top.
```

Permanent distinctions:

```text
external forcing ≠ system state
common heat exposure ≠ P–T interdependency
interface architecture ≠ interface state
state ≠ function ≠ service
transition time ≠ propagation delay ≠ recovery time
physical degradation ≠ service criticality
simulation ≠ validation
```

## 5. Physics-based mathematical engineering

The thesis uses **minimum sufficient physics**.

For selected element/interface `i`:

```math
\dot X_i=f_i(X_i,H,L_i,Z_{ji},u_i;\theta_i).
```

The model is required to preserve component-specific physics. A universal component law is not assumed merely for convenience.

## 6. Engineering resilience cycle

The current thesis-defined engineering cycle is:

```text
Improve → Adapt → Restore → Learn → Improve
```

Interpretation:

- **Improve:** modify baseline design/parameters before a future event.
- **Adapt:** modify operation while heat forcing and states evolve.
- **Restore:** recover acceptable service after unacceptable degradation.
- **Learn:** use event evidence, validation, intervention performance, and recovery to improve future models and decisions.

This is a thesis-defined engineering architecture, not a claim of a universal resilience definition.

## 7. Status of the September broad architecture

The following packages remain **retained whole** and scientifically valuable, but they no longer control the active reader-facing thesis scope where they conflict with this amendment:

- canonical seven-stage framework v2/v2.1;
- RQ0 + RQ1–RQ7 / SO1–SO7 / H1–H5 architecture;
- Chapter-I September freeze;
- P2/P3 global-integration state;
- Austin/SMART-DS candidate-case work;
- broad P+T+I+O decomposition;
- broad sustainability / Stage-6/7 decision architecture.

They may still supply:
- evidence discipline;
- VVUQ;
- requirements/provenance controls;
- model-comparison logic;
- historical mathematical development;
- reusable methods.

No legacy object is automatically active. Re-admission requires explicit consistency with this amendment.

## 8. Current research logic status

The **final narrowed RQ/SO/H set is OPEN**.

Until a new versioned RQ/SO/H authority is approved:

- old RQ/SO/H wording is historical/provenance;
- it must not be presented as the current narrowed confirmatory plan;
- no hypothesis is considered supported by this scope amendment;
- no new result is created by governance reconciliation.

## 9. Current novelty boundary

Not novelty by itself:

- P–T coupling;
- EV charging coupling;
- temperature-aware charging demand;
- dynamic coupled-network restoration;
- V2G-supported resilience;
- generic physics-based modeling;
- Improve / Adapt / Restore wording.

Current candidate unresolved handoff:

```text
heat-dependent physical state/capability
→ coupled electricity + mobility service trajectory
→ measurable consequence for engineering decisions
```

Status: **CANDIDATE / NOT YET FINAL NOVELTY CLAIM**.

## 10. Reopen conditions

This scope may be reopened only for:

1. contradictory full-text evidence;
2. implementation/data infeasibility;
3. supervisor/chair/committee instruction;
4. formal scope change;
5. conflict with higher ASU/SSEBE requirements.

## 11. Preservation rule

No superseded/historical authority is deleted.

Every replacement must preserve:
- prior complete content;
- prior blob/commit identity;
- date;
- authority status;
- superseding authority.

This amendment changes **current precedence**, not historical existence.
