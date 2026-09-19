# Real-Data Admissibility Gates V1

Before a datum/source enters calibration, validation, or a confirmatory experiment:

```math
\boxed{
G_{RW}
=
G_A\land G_S\land G_T\land G_U\land G_P\land G_L\land G_I
}
```

| Gate | Required question |
|---|---|
| G_A | Are authority, ownership and provenance known? |
| G_S | Are spatial meaning, CRS, geographic support and case relationship known? |
| G_T | Are timestamp, timezone, sampling interval and coverage known? |
| G_U | Are units, sign conventions and variable semantics explicit? |
| G_P | Is every transformation reproducible and documented? |
| G_L | Are license, access and redistribution rules known? |
| G_I | Is independence preserved when independent validation is required? |

## Decision states

```math
PASS\Rightarrow\text{admissible for declared role}
```

```math
FAIL\Rightarrow\text{exclude from that role}
```

```math
BLOCKED\Rightarrow\text{obtain missing metadata/evidence}
```

No silent rescue, hidden unit conversion, undocumented timezone reinterpretation, or confirmatory imputation is permitted.

## Additional experiment-level gates

A case-matched operational source additionally requires:
- entity/interface crosswalk;
- temporal alignment with experiment;
- measurement/support compatibility;
- declared missing-data rule;
- uncertainty representation;
- claim ceiling.

For event replay:

```math
G_{event}
=
G_{hazard}\land G_P\land G_T\land G_{time-align}.
```

A full coupled event replay remains BLOCKED if any required constituent trajectory is unavailable.
