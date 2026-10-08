# Module 01 Cross-Paper Synthesis P01–P05 V1

**Status:** WORKING CROSS-PAPER SYNTHESIS — NOT A MODEL FREEZE  
**Effective date:** 2026-10-08  
**Evidence basis:** P01–P05 audits in this module  
**Provenance class for synthesis statements:** [T1] unless directly tagged otherwise

## 1. Governing synthesis question

What can P01–P05 jointly establish about transformer thermal-state physics without exceeding the demonstrated evidence?

## 2. Current physically supported chain

The five papers jointly support the following reduced physical hierarchy:

~~~text
Electrical loading + ambient thermal forcing
→ electrical/core/load losses
→ heat generation
→ thermal storage + heat rejection
→ top-oil / winding thermal-state evolution
→ distinct characteristic thermal times
~~~

A compact working representation is:

~~~math
I(t), T_a(t)
→
P_loss(t)
→
{theta_TO(t), theta_HS(t)}.
~~~

This representation is **not yet the final transformer model**.

## 3. Cross-paper agreements

### 3.1 Losses are the immediate thermal source

Across the reduced-model literature:

~~~text
electrical/core/load losses
→ thermal source terms
~~~

The exact loss decomposition and temperature dependence vary by model and equipment.

### 3.2 Ambient temperature is forcing

The papers consistently treat ambient temperature as an external thermal condition/input rather than an internal transformer state.

~~~text
T_a(t) ≠ X_P,th(t)
~~~

### 3.3 Thermal storage creates memory

Thermal capacitance or equivalent thermal mass causes transformer temperature to evolve over time rather than follow load instantaneously.

~~~text
same instantaneous load
≠
same thermal state
~~~

unless thermal history is also the same.

### 3.4 Top-oil and hottest-spot are distinct

The evidence supports treating top-oil and winding hottest-spot temperature as distinct reduced thermal quantities with different dynamics and physical roles.

~~~text
theta_TO ≠ theta_HS
~~~

### 3.5 Heat rejection can be nonlinear

Swift/Susa/Roslan-type reduced models incorporate nonlinear heat-rejection behavior. Therefore a constant linear thermal resistance is not automatically valid over all operating conditions.

### 3.6 Oil viscosity matters

Susa-type models explicitly connect temperature-dependent oil viscosity to effective heat transfer.

~~~text
temperature
→ oil viscosity
→ convection / effective thermal resistance
→ thermal trajectory
~~~

### 3.7 Construction and cooling architecture matter

P04 strongly supports:

~~~text
transformer construction
→ oil-flow / heat-transfer architecture
→ effective reduced thermal dynamics
~~~

Therefore parameter values cannot be transferred solely by broad cooling label.

### 3.8 Thermal timescales are multiple and condition dependent

P03–P05 jointly support the distinction between oil-side and winding-side thermal response and show that an effective oil time constant is not necessarily invariant.

~~~text
tau_w ≠ tau_o
~~~

and, for the P05 transformer:

~~~text
tau_o = function(load, initial thermal condition, design)
~~~

The exact functional law remains case/model dependent.

## 4. Candidate reduced state architecture

Current evidence strongly supports testing:

~~~math
X_P,th(t)
=
[theta_TO(t), theta_HS(t)]^T
~~~

as the **minimum candidate reduced thermal state vector**.

Status:

~~~text
CANDIDATE — NOT FROZEN
~~~

Why it is not frozen:

- spatial nonuniformity has not yet been sufficiently audited;
- detailed thermal-hydraulic evidence P07/P10 remains pending;
- direct hottest-spot observability evidence P08/P09 remains pending;
- duct/bottom-oil/additional states may become necessary;
- final transformer and cooling architecture are not yet frozen.

## 5. Candidate state-space interpretation

A defensible working synthesis is:

~~~math
dX_P,th/dt
=
F_P(X_P,th, T_a, I; Theta_P).
~~~

Possible state-/condition-dependent constitutive quantities include:

~~~math
mu = mu(T)
~~~

~~~math
P_loss = P_loss(I,T)
~~~

~~~math
R_th,eff = R_th,eff(T, mu, cooling, geometry)
~~~

~~~math
tau_oil = tau_oil(X_P,th, I, design)
~~~

These are cross-paper structural statements only. No final functional form is admitted.

## 6. Permanent distinctions strengthened by P01–P05

~~~text
ambient temperature ≠ transformer thermal state
state ≠ material/property relation
state-dependent property ≠ additional state
sensor reading ≠ true state automatically
top-oil ≠ hottest-spot
temperature prediction ≠ capability prediction
thermal model ≠ numerical solver
model structure ≠ parameterization
mechanism transfer ≠ numerical parameter transfer
calibration ≠ external validation
effective time constant ≠ universal physical constant
~~~

## 7. What P01–P05 do not establish

The following remain OPEN:

- exact active Power thermal state vector;
- exact transformer ODEs for the thesis;
- exact loss model;
- exact oil-viscosity law;
- exact thermal resistance/capacitance values;
- exact oil and winding time constants;
- exact top-oil or hottest-spot limits;
- exact state-to-capability relation;
- exact capability-to-electricity-service relation;
- extreme-heat validity;
- EV-depot loading validity;
- harmonic-loss effects;
- uncertainty propagation;
- final VVUQ protocol.

## 8. State-to-capability handoff remains unresolved

P01–P05 mainly establish:

~~~text
loading / ambient
→ thermal state
~~~

They do **not** yet establish the thesis-critical next handoff:

~~~text
thermal state
→ allowable electrical capability
~~~

Therefore:

~~~math
C_P(t) = C_P(X_P,th(t))
~~~

remains OPEN.

This relation must be established from current standards, exact equipment authority, and compatible evidence.

## 9. Current model-fidelity question

The working question for P06–P10 is:

~~~text
Are theta_TO and theta_HS sufficient reduced states
for the thesis decision problem,
or do spatial/oil-flow/duct/internal states materially change:
- critical transition time,
- predicted capability boundary,
- validation accuracy,
- or eventual service consequence?
~~~

The answer determines the minimum-sufficient Power thermal model.

## 10. Cross-paper synthesis verdict

P01–P05 are sufficient to support a **working nonlinear reduced transformer thermal-state architecture**, but insufficient to freeze:

~~~text
state vector
+ governing equations
+ parameters
+ thresholds
+ capability law
~~~

Current verdict:

~~~text
PHYSICAL ARCHITECTURE — SUPPORTED
REDUCED STATE VECTOR — CANDIDATE
PARAMETERIZATION — OPEN
STATE-TO-CAPABILITY MAP — OPEN
FINAL THESIS MODEL — NOT FROZEN
~~~
