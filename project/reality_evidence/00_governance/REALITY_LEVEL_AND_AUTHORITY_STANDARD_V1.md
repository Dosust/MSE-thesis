# Reality Level and Evidence Authority Standard V1

## 1. Reality level

```math
RL\in\{RL0,RL1,RL2,RL3,RL4\}
```

| Level | Meaning |
|---|---|
| RL0 | mathematical/synthetic test fixture |
| RL1 | literature/model proxy |
| RL2 | authoritative static real-world evidence |
| RL3 | observed operational evidence, but external/regional |
| RL4 | case-matched, temporally aligned observed evidence |

Reality level is not a quality score. RL1 may be high-quality peer-reviewed evidence but is not case-matched observation.

## 2. Authority class

```math
AC\in\{
OFFICIAL,
STANDARD,
PEER\_REVIEWED,
RESEARCH\_DATASET,
PROJECT\_SOURCE,
THIRD\_PARTY
\}
```

Authority class and reality level are independent.

Examples:
- ERCOT hourly load: RL3, OFFICIAL.
- GreenEVT feeder: RL0/RL1, RESEARCH_DATASET/PROJECT_SOURCE.
- Austin Energy event after-action report: potentially RL4 for that event, OFFICIAL.
- NREL workplace charging dataset: RL3 external empirical evidence, RESEARCH_DATASET.

## 3. Scientific role

```math
Role(d)\in\{
STRUCTURE,
MECHANISM,
FORCING,
PARAMETER,
CALIBRATION,
VALIDATION,
THRESHOLD,
BENCHMARK,
ACCOUNTING,
DECISION
\}
```

A source may have more than one role only when justified.

## 4. Stage-4 evidence state

For measurement/information/organization quantities:

```math
ES\in\{
OBSERVED,
DOCUMENTED,
CALIBRATED,
SCENARIO,
UNKNOWN
\}.
```

No SCENARIO quantity may be described as EMPIRICAL.

## 5. Semantic firewall

```math
\boxed{RL4\not\Rightarrow\text{universal validity}}
```

```math
\boxed{OFFICIAL\not\Rightarrow\text{case match}}
```

```math
\boxed{PEER\_REVIEWED\not\Rightarrow\text{parameter validity for this case}}
```
