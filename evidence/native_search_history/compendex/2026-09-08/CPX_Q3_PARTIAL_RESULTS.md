# CPX-Q3 v1.1 partial native results — 2026-09-08

Status: **TEMPORAL BLOCK COMPLETE / UNION PENDING**

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

Temporal block — COMPLETE:

| Atom | Exact Engineering Village query | Native count |
|---|---|---:|
| Tau1 | `(timescale* WN KY) AND (2000-2026 WN YR)` | 59,943 |
| Tau2 | `({time scale*} WN KY) AND (2000-2026 WN YR)` | 119,185 |
| Tau3 | `(delay* WN KY) AND (2000-2026 WN YR)` | 657,847 |
| Tau4 | `(temporal WN KY) AND (2000-2026 WN YR)` | 674,488 |
| Tau5 | `({response time*} WN KY) AND (2000-2026 WN YR)` | 102,263 |
| Tau6 | `({repair time*} WN KY) AND (2000-2026 WN YR)` | 2,826 |
| Tau7 | `({restoration time*} WN KY) AND (2000-2026 WN YR)` | 1,167 |
| Tau8 | `({propagation time*} WN KY) AND (2000-2026 WN YR)` | 3,663 |
| Tau9 | `({recovery time*} WN KY) AND (2000-2026 WN YR)` | 25,012 |
| Tau10 | `({travel time*} WN KY) AND (2000-2026 WN YR)` | 36,257 |
| Tau11 | `({spatio-temporal} WN KY) AND (2000-2026 WN YR)` | 110,053 |
| Tau12 | `(spatiotemporal WN KY) AND (2000-2026 WN YR)` | 124,769 |
| Tau13 | `({recovery trajector*} WN KY) AND (2000-2026 WN YR)` | 543 |
| Tau14 | `({restoration curve*} WN KY) AND (2000-2026 WN YR)` | 42 |
| Tau15 | `({service restoration} WN KY) AND (2000-2026 WN YR)` | 1,538 |
| Tau16 | `({scheduling horizon} WN KY) AND (2000-2026 WN YR)` | 409 |

Temporal completion: **16/16 atoms**.

## Next required action

Do **not** guess Search History numbers. Obtain a current Engineering Village **Search History screenshot or export** that maps the active searches to session-local `#IDs`.

Then build:

1. `Z_Q3 = Z0 OR ZN1 OR ZN2 OR ZN3`
2. `Tau = Tau1 OR Tau2 OR ... OR Tau16`
3. Final `Q3 = P AND T AND Z_Q3 AND R AND Tau`

If Engineering Village rejects the 16-way Tau OR, stage it as smaller exact unions and then OR those staged unions. This remains an execution-only decomposition; do not change any frozen terms.

After the final native Q3 result is obtained, record native N, export the complete detailed-record CSV, hash it, run the deterministic development/validation pilot, verify the prospective anchor `10.1016/j.ijepes.2022.108180`, calculate Wilson intervals, and make the freeze decision.
