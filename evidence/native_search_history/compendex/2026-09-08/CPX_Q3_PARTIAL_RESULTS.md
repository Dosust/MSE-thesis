# CPX-Q3 v1.1 partial native results — 2026-09-08

Status: **IN PROGRESS — all atomic searches complete; Z_Q3 union complete; temporal union/final combination pending**

Purpose: direct Power–Transportation timescales/delays.

Current scientific decomposition:

`Q3 = P ∩ T ∩ Z_Q3 ∩ R ∩ Tau`

Frozen Q0 blocks:
- P = 504,675
- T = 375,268
- Z0 = 275,522
- R = 1,056,435

## Q3 coupling/proximity atoms

| Atom | Search History ID | Exact Engineering Village query | Native count |
|---|---:|---|---:|
| ZN1 | #33 | `((coupl* NEAR/5 network*) WN KY) AND (2000-2026 WN YR)` | 32,465 |
| ZN2 | #34 | `((coupl* NEAR/5 system*) WN KY) AND (2000-2026 WN YR)` | 152,603 |
| ZN3 | #35 | `((coupl* NEAR/5 infrastructure*) WN KY) AND (2000-2026 WN YR)` | 1,317 |

Current old Z block: `#29`.

Executed:

```text
#29 OR #33 OR #34 OR #35
```

Result:

`Z_Q3 = 431,898 records`

This is the expanded Q3 interdependency/coupling block and is valid.

## Temporal block — complete 16/16

| Atom | Search History ID | Exact Engineering Village query | Native count |
|---|---:|---|---:|
| Tau1 | #32 | `(timescale* WN KY) AND (2000-2026 WN YR)` | 59,943 |
| Tau2 | #36 | `({time scale*} WN KY) AND (2000-2026 WN YR)` | 119,185 |
| Tau3 | #37 | `(delay* WN KY) AND (2000-2026 WN YR)` | 657,847 |
| Tau4 | #38 | `(temporal WN KY) AND (2000-2026 WN YR)` | 674,488 |
| Tau5 | #39 | `({response time*} WN KY) AND (2000-2026 WN YR)` | 102,263 |
| Tau6 | #40 | `({repair time*} WN KY) AND (2000-2026 WN YR)` | 2,826 |
| Tau7 | #41 | `({restoration time*} WN KY) AND (2000-2026 WN YR)` | 1,167 |
| Tau8 | #42 | `({propagation time*} WN KY) AND (2000-2026 WN YR)` | 3,663 |
| Tau9 | #43 | `({recovery time*} WN KY) AND (2000-2026 WN YR)` | 25,012 |
| Tau10 | #44 | `({travel time*} WN KY) AND (2000-2026 WN YR)` | 36,257 |
| Tau11 | #45 | `({spatio-temporal} WN KY) AND (2000-2026 WN YR)` | 110,053 |
| Tau12 | #46 | `(spatiotemporal WN KY) AND (2000-2026 WN YR)` | 124,769 |
| Tau13 | #47 | `({recovery trajector*} WN KY) AND (2000-2026 WN YR)` | 543 |
| Tau14 | #48 | `({restoration curve*} WN KY) AND (2000-2026 WN YR)` | 42 |
| Tau15 | #49 | `({service restoration} WN KY) AND (2000-2026 WN YR)` | 1,538 |
| Tau16 | #50 | `({scheduling horizon} WN KY) AND (2000-2026 WN YR)` | 409 |

Next construct:

```text
#32 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50
```

## Current active Q0 IDs relevant to Q3
- `#4` = correct Transportation union, N=375,268
- `#29` = old Interdependency union `Z0`, N=275,522
- `#30` = Resilience union `R`, N=1,056,435
- `#31` = frozen CPX-Q0 final, N=245

The standalone Power union is no longer visible in the 50-search history and must be recreated before final Q3.

## Safe next sequence
1. `Z_Q3` union — COMPLETE, N=431,898.
2. Create `Tau` union.
3. While `#4` is still active, create `T ∩ R ∩ Z_Q3 ∩ Tau`.
4. Recreate Power union and verify N=504,675.
5. Final `Q3 = P ∩ (T ∩ R ∩ Z_Q3 ∩ Tau)`.

Do not use `#31 AND Tau` as final Q3 because that would lock the search to `Z0` and omit papers found only through the added proximity terms.
