# EGMIV H1 — M1 Static/Algebraic Coupling Verification Report

**Status:** PASS  
**Tests:** 13 passed, 0 failed  
**Scientific role:** static/algebraic coupled comparator for H1; no dynamic interface memory.

## Frozen M1 definition

M1 keeps the verified M0 radial power and CTM transport solvers unchanged and adds only same-step algebraic interfaces.

For charger c:

- transport demand creates same-step EV arrival rate λ_c;
- requested charger electrical demand is p_req,c = min(pmax,c, E_c λ_c / η_c);
- served charger power is p_ch,c = p_req,c g_b(c), where g is bus energization;
- charging service is μ_c = η_c p_ch,c / E_c;
- fulfillment is φ_c = μ_c / λ_c for λ_c>0.

There is deliberately no q_c(k), no evolving z_c(k), and no delayed repair-resource state in M1.

## EGMIV correction before freeze

The first implementation used served charger power inside the electrical-demand denominator. EGMIV rejected this because an outage would erase unmet EV electrical demand and inflate power service. The final implementation distinguishes requested charger power from served charger power. Requested EV electricity remains in p_i^d even when the charger bus is de-energized.

In the deterministic outage benchmark, this correction changes the minimum power-service ratio from the invalid 0.60 accounting value to 0.4736842105263158.

## Passed verification gates

1. Charging-service dimensional identity: μ = ηp/E.
2. Exact EV-load mapping: charger request enters the mapped power buses exactly once.
3. Monotonicity: losing grid availability cannot increase charger power or service.
4. Decoupling: with charger interfaces removed, M1 reproduces M0.
5. Zero-demand limit: zero transport/EV demand makes charging coupling vanish and M1 reproduces M0.
6. Sufficient-capacity limit: when charger/grid capacity is sufficient, M1 transport service equals base CTM service.
7. Feeder outage reduces M1 charging/mobility service algebraically without queue state.
8. Higher transport demand increases or saturates same-step requested/served charger power.
9. Static repair-access map returns a fixed snapshot travel delay or infinity if the path is blocked.
10. Time-step refinement preserves terminal service and integrated mapped charging energy in the benchmark.
11. Charger demand-share sums above one are rejected to prevent hidden double counting.
12. Requested EV demand remains in the power-service denominator during outage.
13. Memorylessness: after electrical availability returns, same-step charging fulfillment returns immediately to the same value regardless of the previous outage state.

## Matched M0–M1 scenarios

| Scenario | Meaning | Key result |
|---|---|---|
| S0 | normal demand, no outage | M1 changes electrical loading/voltage but not P/T service; fulfillment = 1 |
| S1 | higher EV/transport demand | charger hardware saturates; mean fulfillment = 0.8; M1 mobility service differs from M0 without queue accumulation |
| S2 | charger-feeder outage halfway through horizon | mean fulfillment = 0.5; post-outage fulfillment = 0; M1 power and transport service diverge from M0 |
| S6 | coupling removed | M1 and M0 trajectories and electrical states agree numerically |

Exact machine-readable values are stored beside this report.

## Scientific decision

M1 is **verified as a static/algebraic comparator** and progression to M2 is permitted.

This does not confirm H1. The current benchmark only shows that the algebraic coupling implementation is physically coherent, nested with M0, and capable of producing controlled representation differences. No engineering-materiality threshold has been evaluated and no benchmark parameter is admissible as final thesis calibration.

## Next EGMIV gate

M2 may now introduce the dynamic objects that M1 explicitly forbids:

- charger queue state q_c(k+1)=q_c(k)+Δt[λ_c(k)-μ_c(k)];
- state/time-dependent road travel delay;
- delayed repair-resource transport and repair progress;
- interface state z_ij(k+1)=H_ij(Y_{k-ℓ},z_ij(k),m_k).

M2 must pass the limiting test M2→M1 when queue memory and delay are removed.