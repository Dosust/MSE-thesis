# EGMIV H1 — M0 Verification Report

**Status:** PASS  
**Tests:** 13 passed, 0 failed  
**Scientific role:** independent/uncoordinated H1 baseline only.

## Verified gates

- radial-tree topology validation;
- exact branch active/reactive load aggregation for the lossless LinDistFlow baseline;
- power-balance residual audit;
- voltage and thermal-limit reporting;
- CTM CFL enforcement;
- global and commodity-wise vehicle conservation;
- nonnegative traffic states and jam-capacity monitoring;
- power invariance to transportation inputs;
- transportation invariance to power inputs;
- exogenous power outage cannot cross into M0 transportation;
- frozen stepwise mobility-service definition;
- numerical time-step refinement of the deterministic benchmark.

## Benchmark verification result

The deterministic test harness gives maximum power-balance residual **0**, maximum traffic-conservation residual **3.553e-15 vehicles**, zero voltage/thermal violations, final stepwise transport service **1.0**, and power service **1.0**.

The finite horizon requests 720 trips and completes 700; the remaining 20 are exactly the end-of-horizon in-network vehicle inventory. This is not treated as a conservation loss.

## Refinement audit

Across Δt = 0.01, 0.005, 0.0025, 0.00125 h, the benchmark completes 700/720 requested trips and preserves the same final stepwise mobility service. Conservation residual stays at floating-point scale.

## EGMIV decision

**M0 is verified for progression to M1.** This statement means only that the independent baseline implementation satisfies its frozen numerical/physical checks. It does **not** validate the thesis hypothesis, calibrate real infrastructure, or establish that LinDistFlow/CTM are sufficient for the final case study.

## Primary mathematical foundations

- Baran & Wu (1989), DistFlow for radial distribution systems, DOI 10.1109/61.19266.
- Daganzo (1994), Cell Transmission Model, DOI 10.1016/0191-2615(94)90002-7.
- Daganzo (1995), multi-commodity network CTM, DOI 10.1016/0191-2615(94)00022-R.