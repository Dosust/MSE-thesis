# I7 — Electricity Price-Informed Charging Decision: Supporting Operational/Economic Interface V2

**Date:** 2026-10-12  
**Authority:** Explicit researcher's decision to add an **I7** label for the electricity-pricing decision and to retain bounded sustainability and resilience interpretation.  
**Status:** **APPROVED LABEL AND RESEARCH ROLE; PHYSICAL/BEHAVIORAL RESPONSE NOT EMPIRICALLY QUALIFIED.** This is a versioned supporting interface designation, not an amendment to frozen GO/SO1–SO3, conceptual V5, mathematical V3, the eight-component roster, or the constitutive model.  
**Supersedes:** `ELECTRICITY_PRICING_SUPPORTING_INPUT_AND_SUSTAINABILITY_DECISION_V1.md` *only* on its former prohibition against assigning a separate interface ID; all its scientific evidence restrictions continue to apply unless explicitly replaced here.

## 1. Exact I7 definition

**I7 — Electricity price-informed charging decision (supporting informational/economic interface, conditional).**

- **Signal source:** Actual externally posted/contracted electricity/charging price from the applicable tariff, provider, utility or market mechanism. Do **not** assume the local distribution power-flow model produces an LMP or that P3 generates price signals.
- **Signal:** Observed price `π(t)` with unit, source, time and applicable location/tariff documented.
- **Receiving operational function:** EV charging decision/request/schedule (and station/route choice *only if* evidence and the selected service model require them). This is a **decision/input**, not a ninth physical equipment subject.
- **Possible downstream physical pathway:** Observed price → *if price responsiveness exists* charging request or schedule → T1 **actual grid-side AC P,Q** (conditional on EVSE, battery and network constraints) → P2/P1 loading and losses → possible temperature/service consequences. The last physical demand influence uses existing AC boundary relationships; I7 itself transfers information, **not AC power or heat**.
- **Direction label on figures:** `I7: observed price π(t) → charging decision/schedule [conditional]`. Use a visually distinct dashed informational arrow, **not** a solid P→T energy arrow or the conditional P3 action arrow. Source can be shown as an external tariff/market input rather than within Power System physical boundary.
- **Evidence status:** literature model precedent L = supported; selection of label/role S = approved; actual tariff, model eligibility E = OPEN; observed price elasticity/causality V = NOT VALIDATED.

## 2. Immutable neighboring relationships

**I1 P→T** ordinary measured grid-side AC power supply at T1.  
**I2 T→P (candidate thermal)** T1/T3 temperature-conditioned charger operation → measured EVSE AC demand → feeder/transformer current, losses and heating. Price-only response never qualifies I2.  
**I3 P→T (candidate thermal)** P1 thermal condition → genuinely implemented P3 operating restriction → permissible EVSE charging. Price never qualifies I3.  
**I4 within T** T1–T3 conversion heat, cooling and derating.  
**I5 within T** T1 DC energy → T2 accepted energy/SOC/readiness.  
**I6 conditional delayed T→P demand** T4 hot-weather HVAC → trip battery depletion → later charging need/schedule → actual T1 AC demand.  
**H(t)** shared extreme heat is not causal intersystem exchange.

**Do not claim seven thermally causal interfaces.** I7 is a supporting economic/behavioral *information pathway*; the two candidate cross-system **thermal** pathways remain I2 and I3. Exactly P1–P4 and T1–T4 remain the research component roster.

## 3. Mathematical status

Possible phenomenological demand schedule operator, *not calibrated or admitted as a physical law*:

```math
P_{\mathrm{req}}(t)=\mathcal D\!\left(\pi(t),E_{\mathrm{need}},t_{\mathrm{departure}},\xi_{\mathrm{operations}};\theta_D\right).
```

This equation **must not be used as a fitted price elasticity** without observed data and a valid identification strategy. If tariff response is not demonstrated, `P_req(t)` stays an observed/exogenous schedule and `π(t)` is a scenario covariate. **Do not equate request, DC offer, battery-terminal acceptance or metered EVSE AC demand**. I7 does not require OPF–UE equilibrium, route assignment, price optimization, a price state ODE, or a new infrastructure system.

## 4. Sustainability and resilience admission

The canonical **two-pathway sustainability assessment** remains the authority:

1. Qualified thermal interdependency → electricity/mobility service effect → measured environmental/economic/social consequences.
2. An evidenced engineering response → changed physical state/operation/service → its environmental/economic/social consequences.

Include charging cost, tariffs, affordability/access or shifts in service only when actual definitions, functional units, boundaries and credible data exist. SDG 7, 9, 11 and 13 are *possible* interpretive links, not automatically realized benefits. A lower price is **not** automatically greater service resilience or lower emissions.

**Test before promotion:** observed applicable tariffs, synchronized charging requests/actual AC P,Q, battery acceptance, EVSE temperatures, common ambient forcing, non-EV demand, charger action logs, departure/service requirements, price responsiveness/counterhypotheses, uncertainty and independent evaluation. An inter-system price association is not by itself validated causal price response.

## 5. Article provenance

Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). “Interdependence between transportation system and power distribution system: a comprehensive review on models and applications.” *Journal of Modern Power Systems and Clean Energy*, 7(3), 433–448. https://doi.org/10.1007/s40565-019-0516-7

**Section 2.3.1 (pp. 438–439), Fig. 1:** traffic/EV charging load links transportation and power; retail/LMP prices *may* influence charging choices.  
**Section 2.3.2 (p. 439), Eq. (28):** reviews OPF–UE fixed-point price-feedback under specific assumptions. Those equilibrium equations are *not* adopted into our thesis and do not validate I7 price response in the selected case.

## 6. Figure specification

Show an **external price box** (`π(t)`, source and unit where known) → a **dashed labeled informational arrow** (`I7: price-informed charging decision — conditional`) → a **charging request/schedule port** in T. Downstream any demand influence must pass through realized **T1 AC demand** and **P2/P1 electrical loading/loss constraints**; the power-system physical supply remains I1; the conditional P3 restriction remains I3. No false direct price→transformer heat arrow, price→P3 action or generalized P↔T physical energy flow.

**No empirical price effect, new resilience improvement, numerical thermal result, protected release, or formal ASU approval is claimed by this document.**
