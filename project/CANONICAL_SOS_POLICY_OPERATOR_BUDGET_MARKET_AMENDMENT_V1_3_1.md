# Canonical SoS Policy–Operator–Budget–Market Amendment v1.3.1 — Scope Correction

**Status:** CANONICAL CORRECTION TO v1.3  
**Effective date:** 2026-09-19  
**Parent:** project/CANONICAL_SOS_POLICY_OPERATOR_BUDGET_MARKET_AMENDMENT_V1_3.md  
**Empirical effect:** NONE

## 1. Default scope

Budget, market and public-policy variables are not default Stage-3 states.

Unless explicitly activated by an RQ/case and admitted by the relevant gates:

~~~text
B          = DEFERRED / STAGE-7 CONTEXT
M          = DEFERRED / STAGE-7 CONTEXT
p_pol      = DEFERRED / STAGE-7 CONTEXT
~~~

They may enter Stage 4 only when they causally constrain current feasible operational action, and Stage 6 only when they are required for intervention resource/consequence accounting.

## 2. Stage-3 admission

A policy/economic channel enters Stage 3 only when all are true:
- it materially affects a declared Stage-3 QOI;
- the mechanism is causally qualified;
- Stage2→3 readiness passes;
- its characteristic time is compatible with the modeled horizon;
- parameters/uncertainty are defensible.

Otherwise it remains scenario/context/downstream information.

## 3. Characteristic horizons

No universal claim is made that

~~~math
\tau_{\rm op}\ll\tau_{\rm rec}\ll\tau_{\rm trans}.
~~~

Instead:

~~~math
\boxed{
\tau_{\rm op},\tau_{\rm rec},\tau_{\rm trans}
\text{ are distinct characteristic horizons with case-dependent separation}.
}
~~~

Strict scale separation may be used only after case-specific support.

## 4. Equilibrium firewall retained

~~~math
\boxed{
Y^\ast\neq Y(t).
}
~~~

NEXTRANS equilibrium outputs cannot be relabeled as transient Stage-3 hybrid dynamics.

## 5. Evidence ceiling

The NEXTRANS report provides conceptual/methodological precedent for policy/operator/budget/market channels and explicitly reports unresolved data/calibration/computational issues.

Thus:

~~~math
\boxed{
\text{conceptual channel}
\neq
\text{qualified executable thesis mechanism}.
}
~~~
