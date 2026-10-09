# Dossiya's Expert Concept Cards — Lessons 01–12

**Source:** conversation's submitted answers and earlier lesson explanations, summarized 2026-10-09. This is teaching content, not physical-model evidence or a frozen thesis model.

## Twelve concepts: one idea, one check

| Lesson | Essential principle | Expert-level diagnostic |
|---|---|---|
| 01 | Common extreme heat may independently affect two systems. Cross-system thermal causation requires direction, source mechanism, interface and receiver evidence. | Why is shared forcing not an interdependency? |
| 02 | Temperature is a thermal condition, not automatically an equipment's allowable electrical capability. | Which ratings, cooling and control limits map state to capability? |
| 03 | Thermal time constant, critical transition time and cross-system delay measure different things. | What exact event defines each time? |
| 04 | Thermally initiated charging degradation may coexist with intact required mobility service. | Which declared task was actually not performed? |
| 05 | An operating margin can decrease while required service is still satisfied. | Is the claimed loss service, flexibility, or only a margin? |
| 06 | Positive nominal margin may coexist with uncertain deficits; bounds do not assign probabilities. | Which probability distribution and coverage are supported? |
| 07 | Numerically solving an assumed law correctly does not establish it is physically accurate. | What was verified numerically, and what real data validate it? |
| 08 | Calibration fit, parameter identifiability and independent predictive validation are different tests. | Could different parameters match, and was the test data independent? |
| 09 | Model-generated hotspot estimates do not establish observability or real physical accuracy. | Can measured outputs distinguish the internal state? |
| 10 | Measuring only the first state in an uncoupled diagonal two-state LTI model gives observability rank one. | Which second-state initial values produce indistinguishable output? |
| 11 | A mathematical influence from an unmeasured to a measured state may permit reconstruction; it does not establish physical cross-system coupling. | Is the mathematical connection evidence-qualified? |
| 12 | A system can be full rank yet poorly estimable when output sensitivity to an internal state is extremely weak. | How do noise, observation length, scale and conditioning affect estimation? |

**Progress:** Lessons 01–11 passed *chat explanation* grading. Lesson 12 has no submitted answer and is PENDING. Computational and independent experimental tests remain unperformed.

## Minimum mathematical facts from the lessons

**Generic didactic lumped energy balance** — not a selected transformer's law:

C_th dT/dt = P_loss - (T-T_a)/R_th.

Thermal resistance R_th [K/W], thermal capacitance C_th [J/K]. With positive constant coefficients, heat generation and ambient temperature:

- T_inf = T_a + R_th P_loss.
- tau_th = R_th C_th.
- T(t) = T_inf + (T_0-T_inf) exp[-t/tau_th].
- If T_0 < T_lim < T_inf and monotone heating holds: t_C = tau_th ln[(T_inf-T_0)/(T_inf-T_lim)].

A temperature threshold is not a verified transformer protection or curtailment law. Crossing time is not automatically a cross-system delay.

**Observation matrix (separate from thermal capacitance):**

State equation x-dot = A x, output y = C_obs x. For two-state LTI:

O = [C_obs ; C_obs A]. Full rank 2 is required for full state observability.

- A=[[-1,0],[0,-2]], C_obs=[1,0]: O=[[1,0],[-1,0]]; rank=1.
- A=[[-1,1],[0,-2]], C_obs=[1,0]: O=[[1,0],[-1,1]]; rank=2; ideal second state is derivative(y)+y under given coefficients and units.
- A=[[-1,epsilon],[0,-2]], C_obs=[1,0]: det(O)=epsilon. Epsilon nonzero implies full rank but does not ensure reliable reconstruction from noisy data; state normalization and time units matter.

**Capability and required services:**
- Physical state x(t) is not operating capability, delivered electrical power or a mobility service.
- Delivered charging energy equals the time-integral of actual charge power at the specified electrical boundary, not automatically stored usable battery energy.
- Departure energy margin M_E = E_usable,dep - E_req represents *one* service-related condition, not all mobility service.
- In the illustrative 105 kWh available, requirement [95,110] kWh example: nominal margin +5 kWh at 100 kWh requirement; margin range [-5,+10] kWh; deficit probability not inferable from range alone.
- Specific Q_P/Q_T, requirements, dataset, equipment and uncertainty for our actual thesis remain OPEN.

## Eight anti-overclaim checks
1. Is it measured, assumed, derived, or proposed?
2. Which component, operating condition and validity domain?
3. Are input forcing, dynamic state, capability, exchange and service distinct?
4. Where is the exact authoritative law/parameter/protection constraint?
5. Could shared heat or another condition explain the same observation?
6. Are source and receiver effects independently evidenced in the claimed direction?
7. Are predictive errors tested against independent real observations with uncertainty?
8. What observation or counterexample would change the conclusion?

## Applying Dossiya logic
Choose one real engineering unknown. Explain **why** from physics, derive only the minimum equation, identify the claimed service effect, show the evidence gap, and test it. Do not read another paper merely to make a long literature list.
