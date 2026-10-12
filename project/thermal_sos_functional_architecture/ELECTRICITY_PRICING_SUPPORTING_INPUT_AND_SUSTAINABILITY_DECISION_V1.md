# Electricity Pricing as a Supporting Operational Input — Decision V1

> **SUPERSEDED IN PART, 2026-10-12:** The user subsequently approved adding **I7** as the separate *supporting economic/behavioral pricing-to-charging decision interface*. The authoritative updated decision is [I7 Pricing Interface Decision V2](ELECTRICITY_PRICING_I7_INTERFACE_DECISION_V2.md). This V1 record remains for chronology. Its earlier statements `no new interface ID`, `do not add I7`, and equivalent ID restrictions are **historical and no longer operative**. All constraints on the exact eight components, unchanged I1–I6 meanings, frozen GO/SO1–SO3, evidence, and avoiding unsupported price/thermal causality remain operative.

**Recorded:** 2026-10-12  
**Decision:** User-approved inclusion of electricity-price information where materially relevant to charging decisions, model interpretation, resilience, or bounded sustainability assessment.  
**Status:** Working supporting-method decision; **NOT** a canonical scope amendment, new specific objective, new physical component, new interface ID, or validated empirical price-response model.  
**Repository:** `Dossiya-SE/MSE-thesis`.

## 1. Scope and authority

The thesis remains a physics–mathematics-first investigation of **thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat** and their consequences through **physical state and time**.

Preserve unchanged:
- Frozen General Objective and SO1–SO3 in `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`.
- Full Electrified Transportation System boundary and canonical state–time semantics.
- Exactly P1 Distribution Transformer, P2 Distribution Feeder, P3 Transformer Protection/Load-Management Hardware, P4 Transformer Cooling Equipment, T1 DC EV Charger, T2 Vehicle Battery Pack, T3 EVSE Cooling Equipment, T4 Vehicle HVAC Equipment.
- I1–I6 in `project/thermal_sos_functional_architecture/EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md`.
- Existing bounded two-pathway sustainability assessment; **do not** create an independent price-equilibrium/market-optimization/SDG objective.

**Interpretive decision:** Price may be retained as a supporting externally observed/input operational variable or competing explanatory factor. Price is **not a thermal state or a physical thermal interface**. Do not add I7, rename I2/I3, or imply prices are an implemented transformer protective action.

## 2. Published precedent and limits

Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019), “Interdependence between transportation system and power distribution system: a comprehensive review on models and applications,” *Journal of Modern Power Systems and Clean Energy*, 7(3), 433–448, DOI: https://doi.org/10.1007/s40565-019-0516-7.

- **Section 2.3.1, pp. 438–439 and Figure 1:** Charging demand connects transportation operations to the distribution network; charging prices *may* influence users' route/charging choices when the tariff/behavioral assumptions apply.
- **Section 2.3.2, p. 439 (Eq. 28):** Explains coupled OPF–UE price-feedback equilibrium for the *reviewed models*.
- This is **L-level literature precedent only**; it does not establish local price elasticity, an actual selected-case tariff, a thermally activated protective control, equipment-specific thermal laws, or validated I2/I3.

Be careful: retail charging tariff, time-of-use energy price, and OPF-derived locational marginal price are different quantities. Record the actual price definition, unit (e.g., local currency/kWh), observation source and charging time/location before use.

## 3. Physical/operational placement

**Supporting pathway (conditional on observed response):**

`observed price π(t) → charging request / schedule / station choice → *actually realized* charging AC P,Q → P2 feeder and P1 loading/losses → conditional thermal-state response → required-service consequences`.

A conceptual demand relation, **not an adopted constitutive or empirically calibrated law**, is

`P_req(t) = D(π(t), E_need, t_departure, vehicle/EVSE constraints, operating context; θ_D)`.

Use this relation **only** if its inputs and responsiveness are evidenced; otherwise use a clearly identified exogenous charging-demand schedule `P_req(t)`. Never equate `P_req`, offered DC power, received battery power, and **measured AC power at T1**.

**I1 (P→T):** physical AC supply; its availability and delivered flow are not prices.

**I2 (T→P; candidate thermal mechanism):** thermally conditioned charger behavior must change actual grid-side AC demand and propagate through admissible electrical losses to P thermal response. Price-responsive demand is a possible confound or operating context; **price-only loading does not qualify I2**.

**I3 (P→T; candidate thermal restriction):** requires real manufacturer/operator-implemented P3 temperature-conditioned permission/curtailment/trip. **Price feedback never establishes I3**.

**I4/I5/I6:** internal charger cooling/derating, delivered DC battery energy/readiness, and conditional later HVAC-demand closure retain their original meanings. Pricing can influence applicable operating schedules but must not be substituted for a real delayed HVAC pathway.

**H(t):** common extreme-heat environmental forcing is exogenous; shared thermal exposure alone is not intersystem causation.

## 4. Why retain pricing

1. **Experimental interpretation:** Price-induced shifting of charging may otherwise be mistaken for temperature-induced T1 derating in I2.
2. **Resilience interpretation:** Actual electricity/mobility service delivery may depend on charging timing and affordability, conditional on observed behavior; resilience remains defined by *maintaining/recovering required services*.
3. **Bounded sustainability:** Relevant measured impacts may include charging expenditure, operating costs, service accessibility/affordability and, with independently supported grid factors, energy/emissions.

Use the two authorized pathways:
- **Pathway 1:** qualified thermal interdependency → measured service consequence → bounded environmental/economic/social consequence.
- **Pathway 2:** tested engineering response → changed thermal/capability/service outcome → bounded environmental/economic/social consequence.

SDG 7, 9, 11 and 13 may provide **interpretive context** only. Select *specific targets/indicators* after data-supported metrics are identified; an SDG alignment is never itself proof of an environmental or social benefit. **Price-driven shifting may improve cost without improving resilience or emissions; assess separately.**

## 5. Evidence and testing contract

Before using any price sensitivity:
- Identify actual tariff/market price and its source, timestamps, billing granularity, currency and applicability.
- Specify observed charge requests, actual AC power/P,Q/V/I, charger and battery operating limits, EVSE thermal condition, ambient heat and non-EV load.
- Predefine a competing explanation: thermally conditioned charging response **versus** price-induced schedule changes, SOC/BMS constraints, arrival demand, non-EV loads, controls and common temperature forcing.
- Establish plausible comparison cases and measurement/parameter uncertainty. If no identifiable pricing response is observed, mark as *input-only/conditional*, not a discovered causal effect.
- Do not claim empirical I2/I3 verification, thermal propagation, service improvement, sustainability benefit or price elasticity from simulated sensitivity alone.
- Compare assessments with consistent system boundaries, time horizons, service definitions, tariffs, units and emissions factors.

## 6. Disposition

**KEEP** price as a supporting operational input and possible confound, and as a bounded economic/social indicator **where evidence warrants**.  
**DO NOT** promote electricity-price feedback to a third physical infrastructure system, thermal interface, frozen objective, or validated coupling law.  
**FUTURE ONLY (out of active scope):** endogenous OPF–UE, electricity market/game-theory equilibrium or broad pricing optimization, requiring separate approved scope revision.

**Evidence status:** Literature precedent = supported by Wei et al. (2019); selected-case pricing behavior and effect = **OPEN**; integrated case validation = **NOT DONE**. No scientific outcome or SDG improvement is asserted by this decision document.
