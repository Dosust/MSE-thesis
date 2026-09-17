# Austin Service Threshold Protocol v1.0

**Date:** 2026-09-18  
**Case:** `AUS-P5U-2018-V1`  
**Status:** PRIORITY SEMANTICS FROZEN / NUMERICAL SERVICE THRESHOLDS OPEN

## 1. Evidence result

Austin Energy publishes a phased restoration policy:

```text
Phase 1: critical life-safety services and backbone transmission/substation/main distribution equipment;
Phase 2: outages affecting the largest customer groups;
Phase 3: remaining smaller outages.
```

Its Critical Load Registry prioritizes approved public-safety and critical-infrastructure locations, including hospitals, police/fire and water/wastewater functions, to the extent conditions permit. Austin Energy also states that widespread restoration can require hours or days and that estimated restoration times depend on field conditions and crew availability.

These sources define **priority semantics**, not a universal numerical minimum service fraction or fixed recovery deadline.

Therefore:

```math
\boxed{
s_P^{min},\;s_T^{min},\;s_{P,rec},\;s_{T,rec},\;T_V,\;T_R
\text{ are not inferable from Austin Energy policy alone.}
}
```

## 2. Physical versus service thresholds

Physical limits in `K_phys` must be taken from the selected OpenDSS/transport realization and applicable engineering rules in their native quantities.

Service requirements in `K_svc` must not be copied from unrelated quantities. In particular:

```text
voltage limits != S_P threshold;
traffic-count accuracy != S_T threshold;
LOTTR/TTI thresholds != completed-OD/requested-OD threshold;
restoration priority != universal T_R deadline.
```

## 3. Confirmatory rule when no same-quantity authority exists

If no same-quantity operator/standard requirement can be qualified for a normalized service metric, the thesis may not label a selected numerical value as an empirical Austin requirement.

Instead, before confirmatory outcomes are inspected, the analysis must choose one of two declared branches:

### Branch A -- authority-backed native constraint

Use a native critical-service constraint with direct engineering meaning, for example a mapped critical facility/corridor requirement, provided the underlying location and synthetic mapping are qualified.

### Branch B -- assumption/sensitivity family

Treat the service threshold as an explicit thesis assumption:

```math
s\in\mathcal S_{pre},
```

where `S_pre` is frozen from development/design considerations before test outcomes. Report H3 conclusions conditionally across `S_pre`; do not collapse them to a single “Austin threshold.” A result is threshold-robust only if its adjudication is unchanged over the declared sensitivity family.

The numerical members of `S_pre` remain OPEN until final data resolution, observation uncertainty and engineering interpretation are available. They may not be chosen from the confirmatory H3 effect.

## 4. Recovery target

`G_rec` must satisfy

```math
G_{rec}\subseteq K.
```

Recovery need not equal the pre-event state. If Austin priority classes are represented, critical life-safety restoration must be evaluated explicitly rather than hidden inside an arbitrary weighted average.

## 5. Recovery horizon

Because Austin Energy does not publish one universal restoration deadline for severe events, `T_R` must come from the declared engineering decision use, an event-specific requirement, or an explicitly preregistered sensitivity horizon. The same applies to `T_V`.

## 6. Decision

```text
Austin critical-service priority semantics: PASS / FROZEN
universal Austin S_P threshold: NOT SUPPORTED
universal Austin S_T threshold: NOT SUPPORTED
universal Austin T_R: NOT SUPPORTED
numerical K_svc/G_rec/T_V/T_R: OPEN
post-hoc threshold selection from H3 outcomes: PROHIBITED
```

This OPEN status is intentional scientific control, not an implementation defect.

## Evidence

- Austin Energy, *How We Restore Power* — phased restoration and crew travel requirements.
- Austin Energy, *Critical Load Registry* — priority service/restoration for public safety and critical infrastructure.
- Austin Energy, *Field Service Centers* — two dispatch centers and restoration/repair responsibilities.
- Poulin & Kane (2021), *Reliability Engineering & System Safety*, 216, 107926 — resilience-curve interpretation depends on declared performance measures and targets.
