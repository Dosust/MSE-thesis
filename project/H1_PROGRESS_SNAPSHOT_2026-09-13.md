# H1 EGMIV Progress Snapshot — 2026-09-13

## Scientific state

H1 has progressed from search design to an implementable competing-model experiment.

```math
\boxed{
\mathfrak I_{PT}
\rightarrow
\{M_0,M_1,M_2\}
\rightarrow
F_{\mathcal G}^{(0,1,2)}
\rightarrow
\text{matched experiment}
}
```

The physical H1 boundary is:

```math
\boxed{
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C
}
```

with a radial distribution system, a dynamic road network, and charging interfaces. Information and organization are deliberately excluded from H1 to preserve attribution and enter H2 later.

## Instantiated physical interdependencies

1. `P→T`: grid power limits charging service, producing queue/waiting and mobility effects.
2. `T→P`: EV arrivals and charging demand become electrical nodal load.
3. `T→P`: road accessibility and travel time delay power-repair crews/resources.

## Competing representations

- `M0`: independent/uncoordinated baseline.
- `M1`: static/algebraic coupling without dynamic interface memory.
- `M2`: explicit dynamic causal coupling with queue state, time/state dependence, and delayed repair-resource transport.

## Public evidence branch

The public H1 evidence branch is complete as a **provisional/supportive branch**, not a replacement for the frozen four-database confirmatory search.

Current public-branch judgment:

```math
\boxed{\text{H1 = provisionally supported, not confirmed}.}
```

## M0 implementation and verification

`M0` is implemented and verified before any coupling is added.

Verification result:

```text
13 tests passed, 0 failed
```

Verified gates include:

- radial-tree topology validation;
- power-balance residual audit;
- voltage/thermal checks;
- CTM CFL enforcement;
- global and commodity-wise vehicle conservation;
- nonnegative traffic states;
- power invariance to transport demand;
- transport invariance to power demand;
- exogenous power outage cannot affect M0 transport;
- stepwise mobility-service definition;
- multi-commodity consistency;
- time-step refinement.

Deterministic benchmark residuals:

- maximum power-balance residual: `0`;
- maximum traffic-conservation residual: `3.553e-15 vehicles`;
- voltage violations: `0`;
- thermal violations: `0`.

Finite-horizon traffic accounting is exact:

```math
720=700+20,
```

where 700 trips complete and 20 vehicles remain in-network at the horizon.

## Interpretation boundary

M0 verification means only that the independent baseline satisfies its frozen numerical and physical checks. It does **not** validate H1, calibrate real infrastructure, or prove the final adequacy of LinDistFlow/CTM.

All numerical values in the M0 harness remain `BENCHMARK_TEST_HARNESS_ONLY`.

## Next EGMIV gate

```math
\boxed{
M_0\;\checkmark
\rightarrow
\text{verification}\;\checkmark
\rightarrow
\mathbf{M_1}
\rightarrow
M_2
}
```

M1 must introduce only static/algebraic Power–Transportation coupling. It must not contain charger queue memory or time-varying repair delay. M2 remains prohibited until M1 passes its own dimensional, decoupling, and physical checks.