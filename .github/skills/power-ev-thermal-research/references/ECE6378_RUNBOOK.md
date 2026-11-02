# Short start-to-finish runbook

1. Read orchestrator and active canon. Read verified lecture map and lab transfer protocol. Record whether material is outline-only, released recording or independently inspected original code.
2. Perform `S1` source audit (primary data, checksum, measurement identity, rights).
3. Perform `S2` topology/meter boundary test (one-line and actual device IDs). Mark UNKNOWN, not reconstructed, when a connection is unproved.
4. Perform `S3` measured channel and interpolation QA, time alignment, train-only feature transforms.
5. `S4/S5` derive qualified loss and thermal models, power flow algebra and coupling edges separately; dimensional/limiting checks.
6. `S6` identify parameters with independent group/time splits, confidence bounds, boundary diagnostics and confounders.
7. `S7`: preregister M0/M1/M2, fixed information set/horizon, report baselines, feasibility, OOD exposure and UQ; run both checkers.
8. `S8` service/consequence inference only when G8 sources and thermal capability relation are defensible. If G7 blocked, report provisional component outcomes and precisely which connected measurements are missing.

First applied student experiment: reproduce a baseline DistFlow/EV-load scenario on the **lab's documented synthetic benchmark** with voltage/current residuals. In parallel, independently evaluate measured OPSD EV/grid series and SINTEF thermal data without joining unrelated installations. Only then consider hybrid ML; reject it if simple model remains superior or the physical constraints cannot be maintained.
