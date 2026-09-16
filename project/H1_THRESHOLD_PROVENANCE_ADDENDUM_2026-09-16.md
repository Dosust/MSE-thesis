# H1 Threshold Provenance Addendum — 2026-09-16

**Method:** EGMIV  
**Purpose:** targeted search for case-specific engineering requirements that can legitimately map to the frozen H1 service quantities.  
**Parent authority:** `H1_THRESHOLD_PROVENANCE_V1.md`  
**Decision:** engineering-significance thresholds remain unfrozen because available authoritative targets are not the same quantities as `S_P` and `S_T`.

## 1. Quantity-preservation rule

A threshold `c` is admissible only if the evidence quantity `q_e` and thesis quantity `q_t` are identical or connected by an independently justified transformation:

```math
\boxed{
q_e=q_t
\quad\text{or}\quad
q_t=T(q_e)\text{ with validated }T.
}
```

Otherwise

```math
\boxed{c_e\not\Rightarrow c_t.}
```

This protects the confirmatory threshold from construct substitution.

---

## 2. Power engineering significance

The frozen thesis power-service quantity is

```math
S_P(t)=
\frac{\sum_i\omega_i p_i^{srv}(t)}
{\sum_i\omega_i p_i^d(t)}.
```

Authoritative Con Edison evidence confirms two operational rules:

1. restoration prioritizes critical facilities such as mass transit, hospitals, police/fire stations, and water/sewage pumping;
2. event-specific restoration communications may declare targets such as restoring 95% of affected **customers** by a specified time.

These are valuable operational constraints but they are not numerically identical to `S_P`:

```math
\frac{N_{customers\ restored}}{N_{customers\ affected}}
\neq
\frac{\sum_i\omega_i p_i^{srv}}{\sum_i\omega_i p_i^d}
```

in general.

The difference can arise from heterogeneous customer loads, critical-load weights, outage timing, counterfactual demand and aggregation.

Therefore a `95% customers restored` target cannot be inserted as

```math
S_P\ge0.95
```

without a validated customer-to-load transformation.

### Decision

```math
\boxed{u_{eng,P}\;\text{REMAINS UNFROZEN}.}
```

The Con Edison evidence may instead constrain restoration ordering or supply an auxiliary event-level validation observable.

---

## 3. Transportation engineering significance

The frozen mobility-service quantity is

```math
S_T(t)=
\frac{\text{weighted completed OD flow}}
{\text{weighted requested OD flow}}.
```

The targeted authoritative search identified NYSDOT/FHWA measures for safety, incident management, travel-time operations and other performance objectives, but no authoritative universal or NYC-event-specific threshold was found for this exact completed-OD/requested-OD service ratio.

Safety-performance targets such as fatality rates, out-of-service rates, incident-clearance expectations, LOTTR/TTI-type measures, or link speed/travel-time targets are not numerically interchangeable with `S_T`.

Hence no threshold may be borrowed by analogy.

### Decision

```math
\boxed{u_{eng,T}\;\text{REMAINS UNFROZEN}.}
```

A valid threshold would require a service requirement stated in the same OD-service quantity or a separately validated mapping from an authoritative operational target.

---

## 4. Confirmatory consequence

The numerical uncertainty floors remain valid for minimal demonstrator v1:

```math
u_{num,P}=0.000416667,
\qquad
u_{num,T}=0.001281963.
```

But the final representation-resolution thresholds remain

```math
\epsilon_P=\max(u_{obs,P},u_{num,P},u_{eng,P}),
```

```math
\epsilon_T=\max(u_{obs,T},u_{num,T},u_{eng,T}),
```

with `u_obs,*` and `u_eng,*` not yet frozen.

Therefore:

```math
\boxed{\epsilon_P,\epsilon_T\;\text{remain NOT YET FROZEN}.}
```

This means H1a can eventually test representation distinguishability once observation uncertainty is qualified, but an engineering-materiality claim requires same-quantity service requirements.

---

## 5. Evidence anchors checked in this pass

- Con Edison restoration communications, including explicit priority for critical customer facilities and event-specific 95%-customer restoration times.
- New York State DOT performance-target and ITS/incident-management materials.
- FHWA emergency transportation / operations material.

## 6. Scientific gate

```math
\boxed{
\text{authoritative target exists}
\not\Rightarrow
\text{threshold is admissible for a different service metric}.
}
```

The threshold block is therefore a **construct-validity requirement**, not a missing-search shortcut.
