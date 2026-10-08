# Module 01 Paper Audit P09 V1 — Spatial Temperature Nonuniformity

**Status:** WORKING EVIDENCE RECORD — HIGH-RIGOR / EVIDENCE-DENSE  
**Effective date:** 2026-10-08  
**Evidence authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`

## P09 — Raza et al. (2021)

**Title:** Empirical Thermal Investigation of Oil–Immersed Distribution Transformer under Various Loading Conditions  
**Journal:** Computer Modeling in Engineering & Sciences, 129(2), 829–847  
**DOI:** 10.32604/cmes.2021.017360  
**Evidence class:** `[A3]` experimental measurement + supporting FEA  
**Access status:** publisher full text verified.

## Experimental architecture

Test transformer:

~~~text
10 kVA
10/0.38 kV
single-phase
oil-immersed
ONAN
disc-type
~~~

Internal temperature network:

~~~text
42 PT100 sensors total
23 winding
10 core
9 oil
~~~

Loading range:

~~~text
80% to 120%
~~~

Sensor locations were informed by electromagnetic/thermal FEA before manufacture.

## Core result

The measured transformer temperature field is strongly spatially nonuniform.

The paper reports that:
- winding temperature changes with vertical position;
- oil temperature differs between regions near primary and secondary windings;
- core temperature varies spatially;
- the hottest region remained in the upper part of the primary winding for the tested loading cases;
- at 120% loading, the reported HST was 73.2 °C at about 85% of primary-winding height.

These numerical results are **case-specific** and must not be transferred.

## Most important thesis lesson

P09 directly supports:

~~~text
transformer temperature ≠ one scalar field value
~~~

and:

~~~text
top-oil temperature ≠ winding hottest-spot temperature
~~~

A reduced state such as `theta_HS` is therefore an **extreme descriptor of a spatial field**, not a spatially uniform physical condition.

A rigorous [T1] abstraction is:

~~~math
theta_HS(t) = max_(x in winding) T(x,t)
~~~

while sensor measurements provide only samples:

~~~math
y_j(t)=T(x_j,t)+epsilon_j(t).
~~~

Thus:

~~~text
max measured sensor temperature
≠ guaranteed global physical maximum
~~~

unless spatial coverage/model evidence is adequate.

## What P09 establishes

1. Dense internal sensing confirms substantial spatial thermal nonuniformity in oil, core, and windings.
2. The location of the hottest measured winding region can remain spatially localized across loading levels for one transformer.
3. Sensor placement should be informed by expected spatial thermal/electromagnetic structure.
4. A single top-oil measurement cannot represent the complete transformer thermal field.
5. A reduced hottest-spot scalar can remain useful only as a deliberately defined field descriptor.

## Validation strength and limitation

The study compares FEA and measurement for **core temperature**, reporting close agreement for the tested cases.

Do not overstate this as validation of the full oil/winding thermal field:

~~~text
core-model agreement
≠ full transformer thermal-model validation
~~~

The study uses one purpose-built 10 kVA transformer. Its geometry, sensor arrangement, temperatures, hottest-spot location, and loading interpretations are not transferable to a different transformer without qualification.

## Safety/capability caution

The authors describe certain tested loading levels as safe/unsafe for their experiment. Those statements are **not accepted as thesis capability limits**.

For the thesis:

~~~text
paper-observed temperature
≠ normative loading limit
≠ allowable electrical capability
~~~

Any final capability boundary must come from the applicable current standard and exact equipment authority.

## Thesis-transfer decision

**CORE SPATIAL-NONUNIFORMITY / REDUCED-STATE-SUFFICIENCY EVIDENCE.**

P09 strengthens, rather than invalidates, the candidate reduced state pair:

~~~math
X_P,th = [theta_TO, theta_HS]^T
~~~

provided that:
- `theta_TO` is explicitly defined as an observable reduced oil descriptor;
- `theta_HS` is explicitly defined as the maximum/relevant winding-temperature descriptor;
- spatial evidence or a validated estimator supports the reduction;
- omitted spatial detail does not materially change transition timing, capability, or service consequence.

## Remaining

- Whether the hottest location moves under the final transformer geometry/duty cycle.
- Whether two reduced states preserve transient behavior under extreme heat.
- Whether duct/bottom-oil or other internal states materially affect the final model.
- State-to-capability mapping.
- EV-depot and harmonic-loading transferability.

## Decision

~~~text
SPATIAL NONUNIFORMITY — ESTABLISHED FOR TESTED TRANSFORMER
theta_HS — STRONGLY SUPPORTED REDUCED DESCRIPTOR
theta_TO + theta_HS — STILL CANDIDATE, NOT FROZEN
FULL SPATIAL MODEL — NOT YET REQUIRED
~~~
