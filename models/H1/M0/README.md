# EGMIV H1 — M0 Independent Baseline v1.0

This package executes the next frozen EGMIV step for H1: implement and verify the independent baseline **before** adding any P↔T coupling.

## Scientific boundary

M0 is deliberately decoupled:

\[
x_{P,k+1}=f_P(x_{P,k},u_{P,k},\eta_{P,k}),\qquad
x_{T,k+1}=f_T(x_{T,k},u_{T,k},\eta_{T,k}).
\]

There is no endogenous charger queue, no road-dependent power restoration, and no transport-derived electrical load. Those enter M1/M2 only after M0 passes verification.

## Implemented physics

### Power
- radial topology validation;
- lossless LinDistFlow baseline in per-unit;
- exogenous line availability;
- downstream load aggregation;
- voltage and thermal violation reporting;
- weighted electricity-service ratio;
- branch power-balance residual audit.

### Transportation
- multi-commodity Cell Transmission Model;
- sending/receiving constraints;
- fixed commodity-specific turning fractions;
- boundary source demand and sink completion;
- road/cell availability;
- CFL check;
- global vehicle-conservation residual audit.

The traffic formulation follows the CTM family introduced by Daganzo (1994) and extended to multi-commodity network traffic in Daganzo (1995). The power model uses the radial DistFlow family introduced by Baran & Wu (1989), here in a lossless linearized baseline form.

## EGMIV verification gates implemented now

1. **Power balance:** every energized child branch must equal local served load plus downstream branch flow.
2. **Traffic conservation:** initial vehicles + admitted boundary flow − completed sink flow = next total vehicles.
3. **CFL:** the explicit CTM time step cannot exceed cell length divided by the larger wave/free-flow speed.
4. **Physical bounds:** no negative vehicle occupancy; jam capacity monitored; voltage/thermal violations reported.
5. **Structural decoupling:** changing traffic demand cannot alter M0 power trajectories, and changing power demand cannot alter M0 transport trajectories.
6. **Exogenous-outage behavior:** a power outage can reduce M0 power service but cannot alter M0 traffic service.

## Critical interpretation rule

All numerical values in `examples/run_m0.py` are **benchmark test-harness values only**. They are not thesis calibration, empirical evidence, or accepted parameter values under EGMIV.

## Run

```bash
python -m pip install -e '.[test]'
pytest -q
python examples/run_m0.py
```

## Next gate

Only after every M0 verification test passes do we implement **M1 static/algebraic coupling**. M2 remains prohibited until M1 itself passes its decoupling and dimensional checks.