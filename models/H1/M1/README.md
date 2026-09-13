# EGMIV H1 — M1 Static/Algebraic Coupling v1.0

M1 preserves the verified M0 power and CTM solvers and adds only memoryless interface maps.

- T→P: same-step transport demand maps to EV charging arrivals and nodal electrical load.
- P→T: bus energization and charger rating limit same-step charging service.
- T→P repair: a snapshot road-availability map yields a fixed repair-access delay.

No charger queue state, evolving interface state, or time-varying repair-resource delay is allowed in M1.

All numeric values in the included example are `BENCHMARK_TEST_HARNESS_ONLY`.

Verification status: **13 passed, 0 failed**. See `reports/M1_VERIFICATION.md`.