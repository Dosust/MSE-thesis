# Calibration–Validation Independence Standard V1

## 1. Rule

Where independent validation is required:

```math
\boxed{
D_{cal}\cap D_{val}=\varnothing
}
```

at the event, trajectory, temporal block, or case level appropriate to the hypothesis.

## 2. Register requirements

Every source/dataset must contain:
- `Calibration_use = YES/NO`
- `Validation_use = YES/NO`
- `Independence_flag`
- split unit: event / day / trajectory / asset / case
- split rationale
- leakage audit status

## 3. Prohibitions

Do not:
- estimate a parameter from an event and call agreement on the same event independent validation;
- tune service thresholds to maximize H3 skill;
- tune intervention factors after observing H4 confirmatory outcomes;
- use future outcome information in Stage-5 predictors;
- merge calibration and validation data because the sample is small without lowering the claim ceiling.

## 4. Permitted alternatives when data are scarce

- development-only calibration with no empirical validation claim;
- cross-event validation;
- held-out temporal blocks;
- external-case validation;
- literature-supported parameter envelope plus sensitivity analysis;
- explicit scenario analysis with claim ceiling marked SCENARIO.
