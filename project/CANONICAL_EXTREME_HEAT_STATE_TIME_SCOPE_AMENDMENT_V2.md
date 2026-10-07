# Canonical Extreme-Heat State-Time Scope Amendment V2

**Status:** CANONICAL CURRENT-SCOPE AMENDMENT  
**Effective date:** 2026-10-07  
**Supersedes for active scope:** `CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

## 1. Purpose

This amendment preserves the extreme-heat/state-time thesis direction while aligning the active system boundary with `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`.

V1 is retained for provenance and is not deleted.

## 2. Current active scope

The active thesis workstream is:

`Extreme heat → selected physical states → state-time evolution → qualified Power ↔ Electrified Transportation propagation → electricity + mobility service consequences → Improve / Adapt / Restore → Learn`

### Physical core

**Power System P ↔ Electrified Transportation System T_e**

The Power System and Electrified Transportation System are distinct coupled physical systems. Mathematical coupling/interface variables may represent exchanged quantities, constraints, communication, and bidirectional transfer without constituting a third physical infrastructure system.

## 3. Canonical Electrified Transportation System definition

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

Status: **FROZEN — CANONICAL**.

Use the system name **Electrified Transportation System**. Do not use “standards-defined” as part of the system name.

## 4. Current bounded application subset

Battery-electric road transportation with grid-connected charging remains a **WORKING-FROZEN application subset** for current extreme-heat investigation.

The exact charging context remains **OPEN**:

- public DC fast charging; or
- fleet/depot charging.

A selected bus/fleet/depot or fast-charging case does not redefine the thesis-wide Electrified Transportation System composition.

## 5. State-time mathematical spine

`H(x,t) → X(t) → {critical transition timing, propagation timing, Q_P(t), Q_T(t)} → {Improve, Adapt, Restore}`

with structural state container:

`X(t) = [X_P^T(t), Z_PT^T(t), X_Te^T(t)]^T`.

`Z_PT` is a coupling/interface object, not a third physical system.

Permanent distinctions:

- external forcing ≠ system state;
- common heat exposure ≠ Power–Transportation interdependency;
- system-scope membership ≠ mandatory detailed model;
- physical connection ≠ functional dependency;
- state ≠ function ≠ service;
- transition time ≠ propagation delay ≠ recovery time;
- physical degradation ≠ service criticality;
- simulation ≠ validation.

## 6. Minimum-sufficient-physics rule

The canonical scope identifies what belongs to the Electrified Transportation System. The mathematical model activates only those component states, constitutive laws, constraints, and coupling quantities needed to change a threshold, service prediction, validation result, intervention assessment, or engineering decision.

## 7. Engineering resilience cycle

The thesis operational cycle remains:

**Improve → Adapt → Restore → Learn → Improve**.

This is a thesis-defined engineering architecture, not a universal resilience definition.

## 8. Service boundary

The Electrified Transportation System is distinct from mobility service. Mobility-service definitions, thresholds, fleet availability, routes, schedules, travel time, traffic flow, accessibility, and passenger/service-demand quantities require separate operational definitions and evidence when used.

## 9. Research-logic status

The final narrowed RQ/SO/H set remains **OPEN** until separately frozen by a versioned authority. This amendment creates no empirical result and no novelty claim.

## 10. Reopen conditions

This scope may be reopened only for contradictory evidence, implementation/data infeasibility, explicit supervisor/chair/committee direction, conflict with higher ASU/SSEBE requirements, or a formally authorized scope change.
