# CPX-Q3 v1.1 — current Engineering Village Search History ID map

Source: user-exported Engineering Village Search History, 50 active searches, 8 Sept 2026.

## Frozen Q0 blocks still active
- `#4` = Transportation union, N=375,268
- `#29` = Interdependency union `Z0`, N=275,522
- `#30` = Resilience union `R`, N=1,056,435
- `#31` = frozen CPX-Q0 final intersection, N=245

The standalone Power union is no longer present in the current 50-search window and must be recreated before final CPX-Q3.

## Q3 coupling/proximity atoms
- `#33` = `((coupl* NEAR/5 network*) WN KY) AND (2000-2026 WN YR)` = 32,465
- `#34` = `((coupl* NEAR/5 system*) WN KY) AND (2000-2026 WN YR)` = 152,603
- `#35` = `((coupl* NEAR/5 infrastructure*) WN KY) AND (2000-2026 WN YR)` = 1,317

Therefore construct:

```text
#29 OR #33 OR #34 OR #35
```

Expected new set: `Z_Q3`.

## Q3 temporal atoms
- `#32` = timescale* = 59,943
- `#36` = time scale* = 119,185
- `#37` = delay* = 657,847
- `#38` = temporal = 674,488
- `#39` = response time* = 102,263
- `#40` = repair time* = 2,826
- `#41` = restoration time* = 1,167
- `#42` = propagation time* = 3,663
- `#43` = recovery time* = 25,012
- `#44` = travel time* = 36,257
- `#45` = spatio-temporal = 110,053
- `#46` = spatiotemporal = 124,769
- `#47` = recovery trajector* = 543
- `#48` = restoration curve* = 42
- `#49` = service restoration = 1,538
- `#50` = scheduling horizon = 409

Therefore construct:

```text
#32 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50
```

Expected new set: `Tau`.

## Safe combination sequence under the 50-search-history window

Because Engineering Village keeps 50 active searches and the oldest entries are displaced as new searches are added, use this order:

1. Create `Z_Q3` from `#29 OR #33 OR #34 OR #35`.
2. Create `Tau` from the 16 temporal IDs above.
3. Before `#4` disappears, create the non-power Q3 core:
   `#4 AND #30 AND #<Z_Q3_ID> AND #<Tau_ID>`.
4. Recreate the frozen Power union from the six exact Power atoms/terms and verify N=504,675.
5. Final Q3 = `#<non-power-core-ID> AND #<new-P-ID>`.

Do not use `#31 AND Tau` as final Q3 because `#31` contains only the old `Z0` block and would omit records retrieved solely by the added Q3 proximity terms.
