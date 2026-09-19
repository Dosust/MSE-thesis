# Global VVUQ Gate Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.7 CREDIBILITY GATES

## 1. Global gate chain

~~~math
\boxed{
G_{VVUQ}
=
G_{CoU}
\land
G_{code}
\land
G_{solution}
\land
G_{data}
\land
G_{cal}
\land
G_{val}
\land
G_{UQ}
\land
G_{sens}
\land
G_{conv}
\land
G_{stability}
\land
G_{claim}.
}
~~~

Not every subgate applies to every object. N/A requires explicit justification.

## 2. Gate semantics

| Gate | PASS | BLOCKED | FAIL |
|---|---|---|---|
| \(G_{CoU}\) | intended use/QOI/domain/decision/credibility target explicit | context incomplete | declared use incompatible with object/evidence |
| \(G_{code}\) | applicable implementation fixtures pass | required test unavailable | implementation error/fixture failure |
| \(G_{solution}\) | numerical error/convergence acceptable for QOI/use | refinement not completed | frozen acceptance rule violated |
| \(G_{data}\) | transformations/version/unit/CRS/time/provenance verified | data-pipeline evidence incomplete | transformation/source integrity failure |
| \(G_{cal}\) | calibration protocol/evidence/identifiability adequate | calibration unresolved | protocol violates frozen data role/identifiability criterion |
| \(G_{val}\) | independent/qualified reference comparison meets criterion | reference/metric/threshold unresolved | valid test executes and criterion fails |
| \(G_{UQ}\) | material uncertainties represented/propagated appropriately | material source unresolved | representation/probability/dependence contradicts evidence |
| \(G_{sens}\) | influential factors/interactions assessed sufficiently | analysis incomplete | frozen sensitivity adequacy rule fails |
| \(G_{conv}\) | numerical/sampling/set/statistic stability meets rule | convergence unresolved | stopping/tolerance criterion fails |
| \(G_{stability}\) | classification/decision conclusion stable as required | stability unresolved | conclusion fails frozen stability criterion |
| \(G_{claim}\) | wording within evidence/validation ceiling | ceiling unresolved | proposed claim exceeds ceiling |

## 3. Verification levels

### V0 — specification/static checks
- type/unit/schema;
- configuration;
- exact identities;
- dimensional consistency.

### V1 — code/algorithm verification
- analytic/unit fixtures;
- conservation/sign/reset/limit tests;
- algorithm arithmetic.

### V2 — solution verification
- discretization/tolerance/refinement;
- sampling convergence;
- emulator/surrogate error if used.

Verification PASS does not imply validation.

## 4. Validation levels

### L0 — no validation
Specification/fixture only.

### L1 — synthetic/analytic controlled validation
Known constructed truth only.

### L2 — subsystem validation
Independent/held-out evidence for component/subsystem.

### L3 — coupled intended-use validation
Qualified evidence for coupled QOI/domain/use.

### L4 — confirmatory intended-use evidence
Validation plus frozen confirmatory comparison and hypothesis-specific gates.

These are thesis claim-ceiling labels, not universal ASME/NASA levels.

## 5. Stage gate matrix

| Stage | Code | Solution | Data | Calibration | Validation | UQ | Sensitivity | Convergence | Stability |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| S3 | M | M | M | C | M | M | M | M | M |
| S4 | M | M | M | C | M | M | M | M | M |
| S5 | M | M | C | N | M | M | M | M | M |
| S6 | M | M | M | C | M | M | M | M | M |
| S7 | M | M | M | N | inherited + method adequacy | M | M | M | M |

M = mandatory as applicable; C = conditional; N = normally not a calibration activity.

## 6. H1 gate

~~~math
\boxed{
G_{H1}^{VVUQ}
=
G_{3,code}
\land
G_{3,solution}
\land
G_{3,calibration\ fairness}
\land
G_{3,validation/materiality}
\land
G_{3,UQ}
\land
G_{3,convergence}.
}
~~~

If any mandatory gate is BLOCKED, H1 = NOT TESTED.

## 7. H2 gate

Requires:
- Stage-3 intended-use adequacy;
- observation/data verification;
- estimator verification/validation;
- uncertainty representation;
- information/organization assumption sensitivity;
- feasible-control classification stability;
- frozen H2 primary endpoint/materiality.

## 8. H3 gate

Requires:
- qualified upstream model/state information;
- \(K,G_{rec},F_{unsafe}\) requirement validity;
- selected algorithm verification;
- set/probability convergence;
- held-out/qualified reference or independently evaluable outcomes;
- frozen H3 metric/materiality;
- data-split firewall.

## 9. H4 gate

Requires:
- qualified upstream resilience diagnosis;
- intervention physical admissibility;
- effectiveness/efficiency verification;
- resource/accounting boundary/factor validation;
- sustainability UQ;
- double-counting audit;
- at least two qualified resilience-effective interventions;
- frozen materiality thresholds.

## 10. H5 gate

Requires:
- complete Stage6→7 handoff;
- decision-algorithm verification;
- uncertainty semantics;
- admissible/Pareto/regret/set-distance stability;
- requirement/model/numerical/normalization sensitivity;
- value sensitivity if used;
- frozen primary H5 endpoint/materiality.

## 11. Claim gate

Permanent:

~~~math
\boxed{
\text{more decimal places}
\not\Rightarrow
\text{more credibility}.
}
~~~

A result may be numerically converged but remain NOT VALIDATED for the intended use.

## 12. Gate inheritance

~~~math
\boxed{
G_{downstream}
\le
\bigwedge
G_{required\ upstream}.
}
~~~

A downstream PASS cannot overwrite an upstream BLOCKED/FAIL without new evidence and a versioned upstream change.
