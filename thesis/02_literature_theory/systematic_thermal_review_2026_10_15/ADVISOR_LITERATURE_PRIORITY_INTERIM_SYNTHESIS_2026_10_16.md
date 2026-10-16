# Advisor literature-review priority — interim synthesis (2026-10-16)

**Status: INTERIM, SIX SOURCE-QUALIFIED STUDIES; NOT A THOROUGH OR COMPLETED SYSTEMATIC REVIEW.**
**Research contract:** Extreme heat; ONLY thermal P↔Tₑ mechanisms; retain exact frozen General Objective and SO1–SO3. Physical heat states, direction and electrical/mobility service separate.
**Driver:** Professor Pat Phelan requests a thorough review of existing work before mathematical model selection. Physics-informed ML is an option **only if suitable experimental measurements exist**; otherwise a physics-based model with appropriately bounded evidence.

## Verified prior-art findings

| Source | Model / physical contribution | Observed vs simulated or inferred | Significance for current research / what remains unproven |
| --- | --- | --- | --- |
| [Godina et al., 2016](https://doi.org/10.1016/j.enconman.2016.04.087) | EV charging profiles and load-factor effects in existing transformer transient thermal/hot-spot aging calculations; published equations and real feeder/base-load inputs | **Actual background load**, EV charging scenarios and transformer HST **modeled**, not independently measured coupled charger thermal data | Tₑ electrical load→P estimated thermal effect prior art. Extreme-heat-induced charger controller activation and observed receiving HST not established |
| [Villarroel et al., 2017](https://doi.org/10.1049/oap-cired.2017.1102) | IEC-family transient transformer heat model, internal fiber-optic sensor measurements in 200 kVA transformer, separate overload validation test | Internal winding temperatures physically **measured** in single transformer laboratory experiment; model calibrated/validated within same device | Qualified P heat evolution and genuine hotspot measurement precedent, **no EVSE or mobility observation** |
| [Bragone et al., 2022](https://doi.org/10.1016/j.epsr.2022.108447) | 1D heat diffusion PDE / PINN versus finite-volume numerical solution using actual boundary/load measurement inputs | Inputs from real transformer; spatial solution agreement primarily **PINN vs numerical FVM** rather than directly measured full temperature field | Transformer PINNs are already prior art; superiority or real-world field coupling unshown in this benchmark |
| [Blomgren et al., 2023](https://doi.org/10.1016/j.segan.2023.101048) | Physically motivated stochastic RC/grey-box thermal ODEs, current-loss heating and ambient exchange; estimated/forecast transformer temperature with field data | Two actual DSO distribution transformers (400 and 200 kVA) with **measured lid temperature** and feeder electrical/weather inputs; 0.4–0.6°C six-hour MAE reported in publisher abstract | P temperature prediction validated on lid, **not independently measured winding HST**; feeder customers own EVs but no matched EVSE thermal/charging telemetry |
| [Balogun et al., 2024](https://doi.org/10.1109/TSG.2023.3339374) | EV-EcoSim couples EV charging, grid transformers, battery/storage and distribution network on multiple timescales | Coupled outcomes **simulation**, evaluated for operational/cost effects; author arXiv manuscript inspected; publisher journal equivalence not cross-verified | Integrated P–Tₑ co-simulation is existing research; not independent field validation of extreme-heat thermal directionality |
| [Krama et al., 2026](https://doi.org/10.1016/j.ecmx.2026.101960) | Extreme climate field DC charger, ambient/rectifier temperature, charging offered vs delivered output, efficiency, harmonics, session time; empirical temporal/cross-session analysis | **Measured Tₑ heat-induced derating** reported in publisher abstract; **original publisher full PDF and raw measurements unavailable** | Strong component premise for thermal Tₑ source; no matched external P transformer temperature or actual mission-completion measurement |

**Independent scientific summary:** Existing research already covers transformer heat/time dynamics, EV charging effects on *modeled* transformer thermal aging, measured charger heat derating, PINN and grey-box approaches, and grid–charging co-simulation. **No novelty claim** may be based solely on connecting those labels. The available six studies do not themselves prove a single-site measured thermal P→Tₑ or Tₑ→P process with both electricity and actual mobility-service consequences. This is a finding about **these sources**, not evidence that no other paper has already solved it.

## What is established, conditional and absent

- **Physics established in particular sources:** transformer current-dependent losses and thermal inertia; measured/specified boundary heat-transfer behavior, charger component power derating at observed hot conditions; thermal dynamics and finite-volume/PINN comparison.
- **Conditional in thesis:** physical P→Tₑ temperature-triggered supply restriction; Tₑ→P heat-derating mediated AC load and resulting P temperature; thresholds and coupling coefficients; service demand/fulfillment; attributable propagation intervals; transfer between hardware and climates.
- **Not demonstrated for selected installation:** actual installed transformer↔EVSE paired temperature/commands/AC/DC data; actual high-heat source events; independent cross-sector receiver effects; independent service resilience measurements; calibrated joint model.

## Critical review-scope questions

1. **Scientific mechanism:** How is directionality physically demonstrated rather than inferred from co-exposure to ambient heat, electrical connectivity or simulation?
2. **Thermal laws:** Which component conservation equations/IEC/IEEE temperature methods, RC ODEs, heat PDEs, derating/controller switching, and loss approximations apply to the targeted device class?
3. **Time semantics:** Do papers quantify response transients, first threshold hitting times, cross-interface propagation delays, service deterioration and recovery with distinct definitions?
4. **Observability:** Are winding temperature, transformer lid, EVSE rectifier temperature and load commands measured or estimated, and at what sensor/time resolution?
5. **Validation:** Were model outputs compared against independent physical measurements and held-out heat events, or other simulated solvers?
6. **Resilience:** Is an actual electricity supply requirement or mobility trip/departure commitment observed, or only EVSE session proxies?
7. **Method selection:** If authentic and sufficiently informative experimental data exist, does an appropriately compared PINN/physics-informed ML achieve better uncertainty-calibrated prediction of measured states/events than governing-equation/grey-box baselines? Otherwise PHY remains the default; PINN is not assumed mandatory.

## Search and completeness restrictions

This addendum is an **interim targeted publisher/source verification** of six known records, not a new completed formal systematic screening. Prior source audits in this PR contain 15 provisional leads, four original PDF artifacts inspected in text (including an author manuscript), and publisher text for Villarroel; Krama is abstract-level. The current targeted public web searches on 2026-10-16 verified bibliographic identity and scope of the six, and discovered additional 2022 IFAC PINN publication (DOI [10.1016/j.ifacol.2022.09.070](https://doi.org/10.1016/j.ifacol.2022.09.070)) for future distinct-article screening. **This IFAC record is not included as a seventh original full-text paper**.

The academic Elicit connector returned **api_access_denied** for the connected account. Scopus/Web of Science/IEEE Xplore/Compendex authenticated queries, their exports, deduplication, systematic screening decisions and final PRISMA counts have **not been executed**. Retrieval of publisher abstract or paper landing page does not mean a full PDF was read. Source access is not a proxy for paper relevance or study quality. Do not repeat speculative claims from unauthenticated PDFs.

## Next operations required by Pat Phelan

1. **Execute and export** formal database search strings in Scopus/WoS/IEEE/Compendex through licensed institutional access (not claim public web search fulfills these).
2. **Deduplicate and screen** title, abstract and full text against predeclared P–Tₑ extreme-heat inclusion criteria, recording exclusions and actual counts.
3. **Extract and verify** per-paper original physics: constitutive equations, initial/boundary conditions, Tₑ and P equipment, electrical interface, named measured variables, data/access/validation, timing and service variables.
4. **Compare competing papers and registered counterexamples** before stating any confirmed novelty or gap.
5. **Evaluate experimental raw-data suitability** independent of bibliography completeness; condition PHY/GREY/PIML decision on actual measurement quality and what observable targets exist.
6. Produce advisor-facing **fully cited matrix, reproducible PRISMA accounting and a provisional-versus-established research-gap decision**.

**Current decision:** Review work **IN PROGRESS**. No final mathematical model chosen, no system-level experimental causality established and no formal novelty conclusion authorized.
