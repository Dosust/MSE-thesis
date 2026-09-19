# Global Credibility / Claim-Ceiling Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.7 CLAIM CONTROL

## 1. Purpose

Credibility evidence constrains wording.

~~~math
\boxed{
\text{claim strength}
\le
\text{credibility/evidence strength}.
}
~~~

The following levels are thesis governance labels, not ASME/NASA standard levels.

## 2. Global credibility/claim ladder

| Level | Minimum evidence state | Allowed default wording | Prohibited overclaim |
|---|---|---|---|
| C0 — SPECIFICATION | equations/schema/protocol defined | "specified", "proposed", "designed" | implemented/verified/validated |
| C1 — VERIFIED IMPLEMENTATION | code/data/algorithm verification relevant to claim | "verified implementation for tested properties" | real-system accurate/validated |
| C2 — CONTROLLED SYNTHETIC | C1 + controlled synthetic/analytic benchmark evidence | "works on declared synthetic/analytic benchmark" | empirical validation/general real-world accuracy |
| C3 — SUBSYSTEM VALIDATED | C1/C2 + independent subsystem intended-use validation | "validated for declared subsystem QOI/domain" | coupled-system validation |
| C4 — COUPLED INTENDED-USE VALIDATED | coupled QOI/domain validation + UQ + convergence | "validated for declared coupled use/domain" | universal validity/out-of-domain validity |
| C5 — CONFIRMATORY HYPOTHESIS ELIGIBLE | C4 or hypothesis-appropriate credibility target + preregistered hypothesis gates | SUPPORTED / NOT SUPPORTED / NOT TESTED for the declared domain | universal causal/engineering generalization |

## 3. Claim inheritance

For result \(R\):

~~~math
\boxed{
\Lambda_R
=
\min(
\Lambda_{data},
\Lambda_{model},
\Lambda_{reference},
\Lambda_{numerical},
\Lambda_{requirements},
\Lambda_{decision}
)
}
~~~

over required components.

A component marked N/A is excluded only with explicit justification.

## 4. Stage-specific ceiling examples

### Stage 3
- fixture only → C1/C2 maximum;
- subsystem validation only → C3 maximum;
- coupled qualified-case validation → potentially C4;
- H1 adjudication → C5 only if H1 preregistration/VVUQ gates pass.

### Stage 4
- estimator fixture only → C1/C2;
- held-out estimator validation for declared state/QOI/domain → C3/C4 depending scope;
- H2 adjudication requires upstream physical adequacy plus Stage-4 H2 gates.

### Stage 5
- analytic viability/reachability benchmark → C2;
- qualified case/event validation → C3/C4;
- H3 adjudication requires independently evaluable outcome and frozen metric/materiality.

### Stage 6
- accounting arithmetic fixture → C1/C2;
- qualified resource/consequence evidence → C3/C4 for declared consequence model;
- H4 adjudication requires complete H4/VVUQ gates and comparable interventions.

### Stage 7
- decision algorithm fixtures → C1/C2;
- decision over synthetic inputs remains C2-style evidence;
- decision over C4-quality inputs inherits no more than C4 for engineering decision claims;
- H5 adjudication requires complete H5 preregistration and stability gates.

## 5. Verification wording

Allowed:
- "code verification passed for declared fixtures";
- "solution convergence met the frozen tolerance for QOI X";
- "algorithm arithmetic reproduced the reference calculation".

Not allowed from verification alone:
- "the model is accurate";
- "the model is validated";
- "the intervention will work in reality".

## 6. Validation wording

Validation wording must include:
- object/model;
- context of use;
- QOI;
- domain;
- reference/evidence class;
- uncertainty/acceptance status.

Preferred pattern:

~~~text
Validated for [declared use/QOI/domain] against [qualified reference],
under [uncertainty/acceptance conditions].
~~~

Avoid unqualified "validated model".

## 7. Negative/null evidence wording

A valid test that fails a frozen criterion may support:
- NOT VALIDATED FOR DECLARED USE;
- hypothesis NOT SUPPORTED.

A blocked prerequisite supports:
- NOT TESTED.

Permanent:

~~~math
\boxed{
\text{BLOCKED}
\not\Rightarrow
\text{negative evidence}.
}
~~~

## 8. Stability wording

Allowed:
- "decision membership was stable over the declared uncertainty domain";
- "H5 conclusion was sensitive to normalization/value assumptions".

Not allowed:
- "robust under all uncertainty";
- "optimal universally";
- "risk-free".

## 9. Extrapolation rule

~~~math
\boxed{
\Lambda(\Omega_{new})
\le
\Lambda(\Omega_{validated})
}
~~~

unless new evidence justifies extension.

No validation/credibility label automatically transfers to:
- new hazard regime;
- new network topology;
- new intervention class;
- new observation architecture;
- new requirement set;
- new decision/value model.

## 10. Hypothesis wording firewall

Final H1–H5 wording must remain domain-bounded:

~~~text
Within the declared case/scenario/domain and under the frozen VVUQ protocol...
~~~

unless the evidence explicitly supports a broader population/generalization.
