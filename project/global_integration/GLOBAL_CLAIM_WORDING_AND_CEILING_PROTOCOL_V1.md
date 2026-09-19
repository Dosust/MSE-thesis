# Global Claim Wording and Ceiling Protocol v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.9 WRITING CONTROL

## 1. Purpose

~~~math
\boxed{
Evidence + Test + UQ + Validity
\rightarrow
ClaimCeiling
\rightarrow
AllowedSentence.
}
~~~

## 2. Wording ladder

| Ceiling | Default allowed verbs | Required qualifier |
|---|---|---|
| C0 | define, specify, propose, design | identify object/protocol only |
| C1 | implement, verify, reproduce tested property | state verified property/fixture |
| C2 | reproduce benchmark, work on declared synthetic/analytic case | name benchmark/domain |
| C3 | validate for declared subsystem use/QOI | name QOI/domain/reference/UQ |
| C4 | validate for declared coupled intended use | name coupled domain/context/UQ |
| C5 | support / not support / not test preregistered hypothesis | name declared domain and preregistered rule |

## 3. Protected scientific verbs

### “Predicts”
Allowed only when the claimed predictive target is evaluated on protected data/scenarios not used to fit or select the model/endpoint in a way that invalidates the test.

### “Explains”
If used as “incremental explanatory information,” the comparator, metric and tested domain must be explicit. It does not imply causality.

### “Causes”
Requires a causal claim design and identification argument appropriate to the data/model. Mechanistic plausibility alone is insufficient.

### “Improves”
Requires explicit baseline, direction, frozen endpoint, materiality rule where relevant, uncertainty, and validity domain.

### “Robust”
Requires a declared uncertainty/adversarial domain and stability/sensitivity evidence.

### “Sustainable”
A partial vector such as carbon alone cannot justify an unqualified “sustainable intervention.” State the dimensions and accounting boundaries actually evaluated.

### “Optimal / best”
Requires a fully specified decision problem: feasible set, objective/value model, and uncertainty assumptions. Universal “best” is prohibited.

## 4. Hypothesis templates

### Supported
Within the declared domain and under the frozen preregistered comparison and VVUQ protocol, H# was supported because the primary criterion was satisfied with the stated uncertainty result.

### Not supported
Within the declared domain, the valid preregistered H# comparison executed, but the frozen primary criterion was not satisfied; H# was not supported.

### Not tested
H# was not tested because a mandatory prerequisite remained unresolved or failed; this is not evidence against H#.

## 5. Validation rule

Validation wording must state the object/model, intended use, QOI, domain, qualified reference/evidence, uncertainty, and acceptance condition.

## 6. Prohibited claim inflation patterns

- protocol exists -> validated;
- code runs -> accurate;
- benchmark passes -> real-world proven;
- mechanism evidence -> observed causal proof;
- one scenario -> general behavior;
- mean benefit -> robust benefit;
- carbon reduction -> sustainable;
- ranking -> best;
- blocked test -> hypothesis failed;
- statistical significance -> engineering materiality unless independently established;
- no observed failure -> safe;
- local validity -> universal generalization.

## 7. Discussion and conclusion rule

~~~math
\boxed{
\Lambda_{Discussion}
\le
\Lambda_{Result},
\qquad
\Lambda_{Conclusion}
\le
\Lambda_{Result}.
}
~~~

Speculation must be explicitly labeled as interpretation, implication, or future work.
