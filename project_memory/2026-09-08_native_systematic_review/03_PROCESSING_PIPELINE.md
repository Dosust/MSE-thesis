# Native systematic-review processing pipeline — reproducible operating procedure

**Project:** MSE thesis  
**Current thesis:** Dynamic Physical–Organizational Resilience of Interdependent Power–Transportation Systems: Causal Events, Timescales, Critical Transitions, and Viability  
**Evidence standard:** PRISMA 2020 + PRISMA-S + PRESS-style search audit

## 1. Evidence architecture

Use three corpus families:
- `C_D`: direct Power–Transportation evidence
- `C_M`: mechanism-transfer evidence
- `C_T`: mathematical theory
- reviews/context retained separately as `C_R`

Nine frozen families per full engineering database:
`Q0, Q3, Q5, Q6A, Q6B, M1, M2, T1, T2`

TRID intentionally omits T1/T2.

## 2. Immutable run tuple

For every native run freeze:
`D,Q,t,F,Y,L,N`

where:
- `D`: database
- `Q`: exact query
- `t`: timestamp
- `F`: native search field/mode
- `Y`: year rule
- `L`: filters/limits
- `N`: native result count

Never edit the raw export. Compute SHA-256 immediately.

## 3. Eligibility before scoring

`Search -> Eligibility -> Classification -> Scoring`

Formal evidence objects can map to:
`X, Z, I, O, h, e, tau, F, J, K, V, rho_V, u, pi`.

## 4. Deterministic pilot

Default:
- development `n=30`
- validation `n=30`, disjoint
- seed `20260907`
- stable SHA-256 ranking on `seed | phase | run_id | record_key`

Small corpus amendment:
- if `N < 30`, screen all
- if `30 <= N < 60`, screen all N and report full-corpus strict proportion; do not fabricate an overlapping holdout.

## 5. Canonical record key

Prefer:
1. normalized DOI
2. otherwise normalized `title + year`

Exact duplicate removal is separate from superseded-version review. A preprint/published pair is not automatically an exact duplicate.

## 6. Precision and uncertainty

`P_hat = included / screened`

Report Wilson 95% CI. Freeze is **not** based on precision alone.

Operational freeze evidence:
- native N traceable and export complete
- predefined year rule satisfied
- prospective anchor sensitivity acceptable where defined/indexable
- development/validation estimates reasonably stable
- no systematic semantic defect
- PRESS/syntax audit passes
- retrieval manageable
- raw artifact immutable and hashed

## 7. Anchor rule

Protocol amendment `PA-ANCHOR-INDEX-01`:
`S_q = A_retrieved,indexable / A_eligible,indexable`

If the prospective anchor denominator is zero for a database, report `N/A`, never 0%.

## 8. Compendex Q0 execution deviation

Engineering Village repeatedly returned parser/system errors for the full frozen Boolean query entered as one long Expert Search.

Accepted deviation:
`RD-CPX-Q0-SET-01`

Resolution:
1. Run exact atomic keyword searches in `KY`.
2. Apply `2000-2026 WN YR` to every atom.
3. Build P, T, Z, R unions using Search History.
4. Run final `P AND T AND Z AND R`.
5. Preserve the original frozen semantics exactly.

This was an **execution-only decomposition**, not a scientific query change.

Final block counts:
- `P = 504,675`
- `T = 375,268`
- `Z = 275,522`
- `R = 1,056,435`
- `Q0 = P ∩ T ∩ Z ∩ R = 245`

## 9. Compendex Q0 native audit

- native N = 245
- export N = 245
- canonical unique N = 245
- exact DOI duplicates = 0
- exact title+same-year duplicates = 0
- publication years = 2001–2026
- outside 2000–2026 = 0
- detailed fields = 45
- missing abstract = 0
- missing DOI = 29
- superseded title/version candidates = 12
- raw SHA-256 = `2c15662b02f27a085dc39f50245d33c4f2166c63839050feb8fc2eb22f7816a8`

Pilot:
- development = 20/30 = 66.7%; Wilson 48.8–80.8%
- validation = 16/30 = 53.3%; Wilson 36.1–69.8%
- absolute difference = 13.3 pp
- prospective Q0 anchors = 3/3 = 100%
- overlap with frozen Scopus Q0 = 212; Jaccard = 0.7413
- overlap with frozen IEEE Q0 = 65; Jaccard = 0.1762
- unique exact-key contribution vs Scopus∪IEEE = 32

Decision: **FREEZE CPX-Q0 v2.2**.

## 10. Next run

Next: `CPX-Q3 v1.1`, direct P–T timescales/delays.

Canonical translated query:

```text
(((("power system*" OR "power grid*" OR "electric grid*" OR "electric power system*" OR "power distribution system*" OR "distribution network*") AND ("transportation system*" OR "transport system*" OR "transportation network*" OR "transport network*" OR "road network*" OR "traffic network*" OR "traffic system*" OR "rail network*" OR railway* OR "electric vehicle*" OR "EV charging" OR "charging station*") AND (interdepend* OR "coupled system*" OR "coupled network*" OR (coupl* NEAR/5 network*) OR (coupl* NEAR/5 system*) OR (coupl* NEAR/5 infrastructure*) OR "interconnected infrastructure*" OR multilayer OR "system of systems" OR cross-sector* OR "power-transportation" OR "power transportation" OR "power-traffic" OR "traffic-electric power" OR "transportation-electric power") AND (resilien* OR restoration OR "disaster recovery" OR "post-disaster" OR "service recovery" OR "load restoration" OR cascading OR "failure propagation" OR disruption* OR robustness) AND (timescale* OR "time scale*" OR delay* OR temporal OR "response time*" OR "repair time*" OR "restoration time*" OR "propagation time*" OR "recovery time*" OR "travel time*" OR "spatio-temporal" OR spatiotemporal OR "recovery trajector*" OR "restoration curve*" OR "service restoration" OR "scheduling horizon"))) WN KY) AND (CPX) WN DB
```

Prospective anchor:
`10.1016/j.ijepes.2022.108180`

Year rule:
`2000–2026`

### Important Compendex execution strategy for Q3
Do not assume the long query will parse in one Expert Search. Use the Q0-proven atomic/Search-History strategy if needed. Because Q3 adds a temporal block, construct:

`Q3 = P ∩ T ∩ Z_Q3 ∩ R ∩ Tau`

where `Z_Q3` includes the Q0 coupling terms plus `coupl* NEAR/5 network*`, `coupl* NEAR/5 system*`, and `coupl* NEAR/5 infrastructure*`; `Tau` is the frozen time/delay term set.

Any decomposition must preserve exact frozen semantics and be logged as an execution-only deviation.

## 11. File-handling rule

Raw database exports may contain licensed abstracts/metadata. Keep them in secure project storage. Git should contain:
- hashes/manifests
- queries/search ledgers
- screening decisions/rationales
- code/config
- derived aggregate results

Do not publish licensed full-text PDFs, unpermitted abstracts, credentials, or personal/supervisor notes.
