## Slide 1 — Thesis Title

# Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience

**Chapter 1 — Introduction**

Dossiya Dakou  
Master of Science in Engineering (MSE)  
Sustainable Engineering  
Arizona State University

---

## Slide 2 — Presentation Outline

**From an engineering problem to a physics-based investigation of infrastructure resilience.**

1. **Research context:** Engineering background, extreme heat, research problem and existing knowledge.
2. **Research definition:** Questions, objectives, physical systems and candidate thermal interdependencies.
3. **Research approach:** Mathematical modeling, methodology, expected contributions, resilience, sustainability and SDG relevance.

---

## Slide 3 — Engineering Background

**Power and Electrified Transportation are distinct physical systems connected through electricity supply and charging operations.**

- **Power → Transportation:** Electrical infrastructure supplies energy for EV charging and electric mobility.
- **Transportation → Power:** Charging demand affects electrical loading and can influence transformer thermal behavior.
- **Physical interconnection:** An electrical connection does not automatically establish a temperature-conditioned thermal interdependency.

*Sources: Hilshey et al. (2013); Qian et al. (2015).*

---

## Slide 4 — Extreme-Heat Research Context

**Extreme heat changes equipment thermal conditions, making physical state and time important to infrastructure operation.**

- **Power System:** Transformer temperature depends on electrical losses, ambient conditions, thermal storage and cooling.
- **Electrified Transportation:** Elevated temperatures can affect charging-equipment operating capability.
- **State and time:** Thermal behavior depends on present operating conditions and previous loading and heat exposure.

**Key distinction:** Both systems may respond to the same external heat without transmitting a thermal effect between them.

*Sources: IEEE Std C57.91-2025, where applicable; Krama et al. (2026).*

---

## Slide 5 — Research Problem

**Under extreme heat, do temperature-conditioned effects propagate between Power and Electrified Transportation systems, and if so, how do they affect required services over time?**

- **P → Tₑ candidate:** Transformer thermal constraints may affect permissible supply and charging capability when applicable operating restrictions exist.
- **Tₑ → P candidate:** Temperature-dependent charger operation may change grid-side AC demand and subsequent transformer thermal behavior.
- **Engineering consequences:** Determine whether these interactions produce critical transitions, attributable propagation delays or changes in electricity and mobility services.

*The two directional thermal mechanisms are investigated independently, not presumed to be established.*

---

## Slide 6 — Existing Knowledge and Research Opportunity

**Previous studies examine important equipment effects; this thesis investigates their relevance to directional thermal interdependencies and service consequences.**

| Research area | Existing evidence | Proposed investigation |
|---|---|---|
| Transformer thermal behavior | EV charging, temperature and ageing (Hilshey et al., 2013; Qian et al., 2015) | Relevant thermal states and constraints under extreme heat |
| Charging-equipment behavior | Field-observed DC fast-charger thermal derating (Krama et al., 2026) | Temperature-conditioned changes in actual grid-side AC operation |
| Service consequences | EV charging and transformer service-disruption risk (Visakh & Selvan, 2023) | Attributable state–time and electricity/mobility service effects |

**Research opportunity:** Connect qualified directional mechanisms with physical state, time and service consequences in a selected application.

*The final novelty boundary requires comparison with the closest relevant studies.*

---

## Slide 7 — Proposed Research Questions

**The research asks what physical mechanisms can be qualified, how they evolve and what consequences they produce.**

**RQ1 — Physical mechanisms**

Which thermally sensitive physical states and directional thermal interdependencies can be identified and qualified between the Power System and Electrified Transportation System under extreme heat?

**RQ2 — Mathematical modeling**

How can the qualified thermal mechanisms be represented mathematically to describe their evolution and propagation through physical state and time?

**RQ3 — Engineering consequences**

Under what conditions do critical transitions and attributable propagation delays occur, if observed, and how do they affect required electricity and mobility services?

---

## Slide 8 — General and Specific Research Objectives

### General Objective

To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.

### Specific Objectives

**SO1 — Identify and qualify**

Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.

**SO2 — Model state-time evolution**

Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.

**SO3 — Quantify consequences**

Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

---

## Slide 9 — Physical Systems and Interdependency Interface

**The investigation distinguishes the complete physical systems from the selected subsystem and its mathematical representation.**

- **Power System (P):** Electricity supply and distribution infrastructure, including relevant transformer behavior and operating constraints.
- **Electrified Transportation (Tₑ):** Road EVs, rechargeable batteries, propulsion, auxiliaries, power circuits, EVSE, charging connections and required communication/control.
- **Selected application:** A transformer–grid-side AC–EVSE–vehicle configuration represents a possible research subsystem, not either complete infrastructure system.

**Measurable interface:** AC voltage, current and active power.

**Candidate directional effects:**

- **Tₑ → P:** Charger thermal response → AC operating behavior → transformer thermal response.
- **P → Tₑ:** Transformer thermal state → applicable operating constraint → charging capability.

*Each directional pathway requires a qualified physical mechanism and relevant operating evidence.*

---

## Slide 10 — Physics-Based Modeling Logic and Working Assumptions

**The mathematical approach will connect thermal-state evolution with qualified interface behavior and required services.**

- **External and operating inputs:** Extreme heat, electrical loading, equipment conditions and controls.
- **Physical principles:** Heat-generating losses, thermal-energy storage and net heat exchange.
- **Working assumptions:** Selected states, parameters and temperature-conditioned interfaces will be justified for the physical application.

**Foundational thermal-energy balance**

For a defined thermal control volume:

\[
\frac{dU_{\mathrm{th}}}{dt}
=
P_{\mathrm{heat}}-\dot Q_{\mathrm{net,out}}
\]

**Proposed modeling workflow**

Qualify physical inputs and laws → Formulate state–time behavior → Examine interface mechanisms → Evaluate required services.

*The arrows indicate stages of research. They do not impose one-way physical causality or exclude feedback.*

---

## Slide 11 — Research Methodology and Expected Contributions

**Each research objective connects a scientific activity to an intended output.**

| Objective | Research activity | Intended output |
|---|---|---|
| **SO1 — Qualify** | Review physical evidence and identify admissible thermal mechanisms | Mechanism and assumption register |
| **SO2 — Model** | Formulate and examine the physics-based state–time representation | Mathematical model with documented assumptions and limits |
| **SO3 — Quantify** | Investigate critical events, attributable delays and service behavior | Supported estimates and uncertainty, where feasible |

**Model credibility:** Numerical verification, justified scenario comparisons and independent physical observations where available.

*The contributions are expected research products, not already demonstrated findings.*

---

## Slide 12 — Resilience, Sustainability and SDG Relevance

**The engineering significance of thermal interdependencies depends on their consequences for required services and sustainable infrastructure performance.**

- **Resilience:** Examine whether required electricity and mobility services are maintained or recovered as physical states evolve.
- **Sustainability:** Assess environmental, economic and social consequences through direct effects and justified engineering responses.
- **SDG relevance:** Relate measured outcomes to eligible targets under SDGs 7, 9, 11 and 13.

**Two assessment pathways**

**Pathway 1 — Direct consequences:** Qualified thermal interdependency → Service effects → Sustainability indicators.

**Pathway 2 — Engineering responses:** Improve / Adapt / Restore → Service changes relative to a reference → Sustainability indicators.

**Illustrative quantities:** Delivered charging energy (kWh), vehicle departure readiness, electrical energy losses (kWh) and service-disruption costs.

*Charging energy is not itself a mobility-service measure. Project indicators are not automatically official UN SDG indicators.*

---

## Slide 13 — Thesis Organization and Immediate Research Direction

**The thesis progresses from physical evidence and mathematical investigation to supported findings and their engineering implications.**

- **Chapters 1–2 — Foundations:** Research background, problem, objectives, literature and physical theory.
- **Chapters 3–5 — Investigation:** System architecture, physics-based mathematical model, methodology and results.
- **Chapters 6–7 — Interpretation:** Discussion, limitations, resilience and sustainability implications, conclusions and recommendations.

**Immediate research priorities**

Complete the closest-prior-art review, qualify the selected physical interface, establish admissible assumptions and data, and develop the mathematical model and its testing plan.

*The seven-chapter structure is proposed and subject to supervisory approval.*