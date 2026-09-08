# Compendex Q3 v1.1 — Native execution plan

Status: **READY TO RUN**

Purpose: direct Power–Transportation evidence with temporal/timescale/delay mechanisms.

Year rule: `2000–2026`

Prospective anchor: `10.1016/j.ijepes.2022.108180`

## Scientific definition

`Q3 = P ∩ T ∩ Z_Q3 ∩ R ∩ Tau`

Reuse the already validated Q0 blocks if the Engineering Village Search History session is still available:
- `P = #8` = 504,675
- `T = #24` = 375,268
- `Z_Q0 = #49` = 275,522
- `R = #50` = 1,056,435

Search-history numbers are session-local. If they differ, identify blocks by their query definitions/counts, not by number alone.

## Add the three Q3-only coupling proximity atoms

Run one by one in Expert Search:

```text
((coupl* NEAR/5 network*) WN KY) AND (2000-2026 WN YR)
```

```text
((coupl* NEAR/5 system*) WN KY) AND (2000-2026 WN YR)
```

```text
((coupl* NEAR/5 infrastructure*) WN KY) AND (2000-2026 WN YR)
```

Then create:

`Z_Q3 = Z_Q0 OR proximity_1 OR proximity_2 OR proximity_3`

Official Engineering Village syntax supports `WN` field restriction and `NEAR/n` proximity in Expert Search. `NEAR/5` means the terms may occur in either order with at most five indexed words between them.

## Build Tau block one atom at a time

Run exactly these 16 atomic queries:

```text
(timescale* WN KY) AND (2000-2026 WN YR)
```

```text
({time scale*} WN KY) AND (2000-2026 WN YR)
```

```text
(delay* WN KY) AND (2000-2026 WN YR)
```

```text
(temporal WN KY) AND (2000-2026 WN YR)
```

```text
({response time*} WN KY) AND (2000-2026 WN YR)
```

```text
({repair time*} WN KY) AND (2000-2026 WN YR)
```

```text
({restoration time*} WN KY) AND (2000-2026 WN YR)
```

```text
({propagation time*} WN KY) AND (2000-2026 WN YR)
```

```text
({recovery time*} WN KY) AND (2000-2026 WN YR)
```

```text
({travel time*} WN KY) AND (2000-2026 WN YR)
```

```text
({spatio-temporal} WN KY) AND (2000-2026 WN YR)
```

```text
(spatiotemporal WN KY) AND (2000-2026 WN YR)
```

```text
({recovery trajector*} WN KY) AND (2000-2026 WN YR)
```

```text
({restoration curve*} WN KY) AND (2000-2026 WN YR)
```

```text
({service restoration} WN KY) AND (2000-2026 WN YR)
```

```text
({scheduling horizon} WN KY) AND (2000-2026 WN YR)
```

Then OR-union the 16 Tau atoms in Search History.

## Final native Q3 combine

Run:

`P AND T AND Z_Q3 AND R AND Tau`

Do not add, delete, or substitute scientific terms.

## If the current Search History still ends at Q0 final #51

Expected numbering, assuming no intervening searches:
- #52–#54 = three Q3-only proximity atoms
- #55 = `#49 OR #52 OR #53 OR #54` = Z_Q3
- #56–#71 = the 16 Tau atoms in the order listed above
- #72 = Tau union
- #73 = `#8 AND #24 AND #55 AND #50 AND #72` = final CPX-Q3

Treat these IDs as convenience only; verify the actual Search History before combining.

## After final Q3 result

1. Capture final native result count.
2. Export **all records** as `My PC -> CSV -> Detailed record`.
3. Suggested raw filename:
   `2026-09-08_COMPENDEX_Q3_v1_1_RAW_N####.csv`
4. Do not open/edit/resave the raw CSV.
5. Compute SHA-256.
6. Verify N, unique N, duplicates, year range, required fields, and anchor recovery.
7. Create deterministic development/validation samples using seed `20260907`.
8. Apply the frozen Q3 screening precedent.
9. Calculate precision + Wilson 95% CI.
10. Decide FREEZE only after completeness, sensitivity, stability and syntax/semantic checks.
11. Update master controller and translation package.

## Frozen Q3 screening precedent

Include direct P–T dynamic/spatio-temporal studies even when a quantified characteristic timescale is not formally extracted. Search inclusion is broader than final `D_tau=1`.

Exclude:
- reviews
- generic infrastructure without direct P–T coupling
- power-only work
- EV/DER control where EVs are electrical resources but transportation-network dynamics are absent

Later extraction separately determines quantified timescale/delay/repair/restoration/travel/recovery properties.
