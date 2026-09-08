# CPX-Q3 v1.1 partial native results — 2026-09-08

Status: **IN PROGRESS**

Purpose: direct Power–Transportation timescales/delays.

Current scientific decomposition:

`Q3 = P ∩ T ∩ Z_Q3 ∩ R ∩ Tau`

Frozen Q0 blocks remain unchanged:
- P = 504,675
- T = 375,268
- Z0 = 275,522
- R = 1,056,435

New Q3 coupling/proximity atoms completed:

| Atom | Exact Engineering Village query | Native count |
|---|---|---:|
| ZN1 | `((coupl* NEAR/5 network*) WN KY) AND (2000-2026 WN YR)` | 32,465 |
| ZN2 | `((coupl* NEAR/5 system*) WN KY) AND (2000-2026 WN YR)` | 152,603 |
| ZN3 | `((coupl* NEAR/5 infrastructure*) WN KY) AND (2000-2026 WN YR)` | 1,317 |

Temporal block progress:

| Atom | Exact Engineering Village query | Native count |
|---|---|---:|
| Tau1 | `(timescale* WN KY) AND (2000-2026 WN YR)` | 59,943 |
| Tau2 | `({time scale*} WN KY) AND (2000-2026 WN YR)` | 119,185 |
| Tau3 | `(delay* WN KY) AND (2000-2026 WN YR)` | 657,847 |
| Tau4 | `(temporal WN KY) AND (2000-2026 WN YR)` | 674,488 |
| Tau5 | `({response time*} WN KY) AND (2000-2026 WN YR)` | 102,263 |

Do not infer Search History numbers from this file. The user has not yet supplied a current Search History screenshot/export mapping these atoms to session-local #IDs.

Next required temporal atoms, in order:

1. `({repair time*} WN KY) AND (2000-2026 WN YR)`
2. `({restoration time*} WN KY) AND (2000-2026 WN YR)`
3. `({propagation time*} WN KY) AND (2000-2026 WN YR)`
4. `({recovery time*} WN KY) AND (2000-2026 WN YR)`
5. `({travel time*} WN KY) AND (2000-2026 WN YR)`
6. `({spatio-temporal} WN KY) AND (2000-2026 WN YR)`
7. `(spatiotemporal WN KY) AND (2000-2026 WN YR)`
8. `({recovery trajector*} WN KY) AND (2000-2026 WN YR)`
9. `({restoration curve*} WN KY) AND (2000-2026 WN YR)`
10. `({service restoration} WN KY) AND (2000-2026 WN YR)`
11. `({scheduling horizon} WN KY) AND (2000-2026 WN YR)`

After all 16 temporal atoms are complete, create the Tau union and only then form final `Q3 = P ∩ T ∩ Z_Q3 ∩ R ∩ Tau` using the actual current Search History IDs.
