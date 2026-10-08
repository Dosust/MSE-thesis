# Module 01 Paper Audit P08 V1 — Direct Hottest-Spot Observability

**Status:** WORKING EVIDENCE RECORD — HIGH-RIGOR / EVIDENCE-DENSE  
**Effective date:** 2026-10-08  
**Evidence authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`

## P08 — Lobo Ribeiro et al. (2008)

**Title:** Multipoint Fiber-Optic Hot-Spot Sensing Network Integrated Into High Power Transformer for Continuous Monitoring  
**Journal:** IEEE Sensors Journal, 8(7), 1264–1267  
**DOI:** 10.1109/JSEN.2008.926926  
**Evidence class:** `[A3]`  
**Access status:** IEEE metadata verified; author-uploaded full text inspected.

## Core evidence

The paper embeds a 12-point fiber Bragg grating temperature-sensing network inside a 20 MVA power transformer. Sensors were placed in windings, cellulose insulation, magnetic-circuit regions, and cooling-oil locations. A laboratory test included a 10% overload at 22 °C ambient.

The sensing system is reported with approximately:

~~~text
temperature accuracy: ±1 °C
temperature resolution: 0.1 °C
operating range: −25 °C to +250 °C
~~~

These are instrument-specific results, not universal fiber-optic performance values.

## Most important thesis result

P08 shows that winding temperature can be measured directly at embedded locations without treating hottest-spot temperature as only a model output.

However:

~~~text
direct local winding-temperature measurement
≠
guaranteed observation of the true global hottest spot
~~~

A rigorous observation model is:

~~~math
y_j(t)=T(x_j,t)+epsilon_j(t)
~~~

where (x_j) is the sensor location.

A thesis-defined sensor-network estimate could be:

~~~math
hat(theta)_HS(t)=max_j y_j(t)
~~~

while the physical hottest spot is conceptually:

~~~math
theta_HS(t)=max_(x in winding) T(x,t).
~~~

Therefore:

~~~text
hat(theta)_HS = theta_HS
~~~

only if sensor placement/spatial coverage is sufficient or a validated model maps the measurements to the true maximum.

## Standard alignment

Current IEEE C57.169-2023 explicitly treats direct hottest-spot measurement and emphasizes that an accurate thermal model is needed to locate temperature sensors correctly.

Thus:

~~~text
measurement technology
+ physically justified sensor placement
+ thermal model
→ credible hottest-spot observation
~~~

## What P08 establishes

- Embedded optical sensors can directly measure local winding/internal temperatures.
- Fiber-optic sensing avoids the electromagnetic-interference limitation associated with conventional electrical sensing inside high-voltage windings.
- Multipoint measurements provide stronger observability than only external/top-oil measurements.
- Hottest-spot validation is fundamentally a **spatial measurement problem**, not only an instrument-accuracy problem.

## What remains OPEN

- Whether a finite sensor network captures the true global hottest spot.
- Optimal sensor-placement method for the final transformer.
- Measurement uncertainty beyond the reported instrument accuracy/resolution.
- Applicability to the selected distribution/depot transformer.
- Extreme-heat and EV-loading validation.
- State-to-capability mapping.

## Thesis-transfer decision

**CORE OBSERVABILITY / VALIDATION EVIDENCE.**

Upgrade `theta_HS` from merely a model-predicted candidate state to a **physically measurable but spatially conditional candidate state**.

Do not freeze `theta_HS` as directly observable unless sensor placement or a validated estimator establishes the relation between local measurements and the true hottest spot.
