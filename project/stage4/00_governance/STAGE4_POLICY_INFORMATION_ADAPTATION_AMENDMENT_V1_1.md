# Stage 4 Policy Information-Adaptation Amendment — v1.1

**Date:** 2026-09-19  
**Status:** CANONICAL STAGE-4 MATHEMATICAL AMENDMENT — DESIGN/PROTOCOL ONLY  
**Parent authority:** `STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md`  
**Scientific effect:** adds explicit information/adaptation semantics; does not alter H2, case data, policy values, or empirical results.

## 1. Purpose

Stage 4 already distinguishes physical truth, observation, information, belief/state estimate, organization, and feasible control. This amendment makes explicit that an operational policy may use only information available up to the action time.

## 2. Available-information filtration

From the Stage-4 available-information object

~~~math
\mathcal I_t
=
\{y_{0:t},\text{messages},\text{forecasts},\text{reports}\},
~~~

define the information filtration

~~~math
\boxed{
\mathcal F_t^{I}
=
\sigma(\mathcal I_s:s\le t).
}
~~~

When a discrete-time implementation is used, the corresponding filtration is (mathcal F_k^{I}).

## 3. Admissible operational policy class

Define

~~~math
\boxed{
\Pi^{NA}
=
\{
\pi:
\pi_t
\text{ is }
\mathcal F_t^{I}\text{-adapted}
\}.
}
~~~

The superscript (NA) denotes **nonanticipative / information-adapted** operation.

The Stage-4 policy is therefore interpreted as

~~~math
\boxed{
u_t
=
\pi_t(b_t,z_I(t),z_O(t)),
\qquad
\pi\in\Pi^{NA},
\qquad
u_t\in\mathcal U_{feas}(t).
}
~~~

## 4. Nonanticipativity firewall

~~~math
\boxed{
u_t
\text{ may not depend on future unobserved }
Y_{s>t},
\eta_{s>t},
y_{s>t},
\text{or future realized outcomes}.
}
~~~

A forecast that is legitimately available at time (t) is part of (mathcal I_t) and is therefore admissible. Future realized truth is not.

## 5. Feasible-control semantics retained

The parent authority remains:

~~~math
\boxed{
\mathcal U_{feas}(t)
=
\mathcal U_{phys}(t)
\cap
\mathcal U_{info}(t)
\cap
\mathcal U_{org}(t)
\cap
\mathcal U_{resource}(t).
}
~~~

Information adaptation does not waive physical, informational, organizational, or resource constraints.

## 6. Stage-5 inheritance

Whenever Stage 5 quantifies over admissible policies, the operational policy set inherits (Pi^{NA}) unless a stricter stage-specific policy class is declared.

This prevents a viability/reachability calculation from using future disturbance or future measurement realization implicitly.

## 7. Verification obligations

Applicable checks include:

- timestamp ordering;
- message/measurement availability at decision time;
- forecast vintage;
- actuator/decision latency;
- absence of future-state leakage;
- absence of validation/confirmatory outcome leakage;
- reproducibility of policy inputs.

## 8. Claim boundary

~~~math
\boxed{
\text{policy nonanticipativity specified}
\neq
\text{policy effectiveness validated}
\neq
\text{H2 supported}.
}
~~~

All other Stage-4 v1 semantics remain unchanged.
