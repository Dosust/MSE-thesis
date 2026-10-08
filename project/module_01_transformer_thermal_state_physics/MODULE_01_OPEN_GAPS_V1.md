# Module 01 Open Gaps V1 — P06–P10 Reading Burden

**Status:** ACTIVE WORKING GAP MAP  
**Effective date:** 2026-10-08  
**Evidence basis:** P01–P05 checkpoint  
**Purpose:** define exactly what P06–P10 must resolve before any Power-side thermal model freeze.

## 1. Current unresolved core question

P01–P05 support a reduced nonlinear thermal architecture, but they do not yet prove that the minimum active Power-side state vector should be only:

~~~math
X_P,th = [theta_TO, theta_HS]^T.
~~~

The remaining question is:

~~~text
Are theta_TO and theta_HS sufficient reduced states
for the intended extreme-heat / coupled-service problem,
or do additional spatial/oil-flow/duct/internal states
materially change the engineering conclusion?
~~~

## 2. P06 burden — independent time-constant evidence

**Target role:** numerical + experimental validation of thermal time-constant variation with load factor.

P06 must answer:

1. Is load dependence of effective thermal time constant observed independently of P05?
2. What physical mechanism is used to explain the variation?
3. Which transformer type, rating, cooling architecture, and test conditions were used?
4. How is thermal time constant defined mathematically?
5. How is it estimated from data?
6. Is the quantity an effective reduced descriptor or tied directly to a physical RC parameter?
7. What numerical model is used?
8. What experimental measurements validate it?
9. Are uncertainty/error metrics reported?
10. Is the result transferable beyond the tested transformer?

**Gap-closing target:**

~~~text
P05 empirical calibration
+ P06 independent numerical/experimental evidence
→ stronger cross-paper support for state/load-dependent thermal timescale
~~~

## 3. P07 burden — detailed thermal-hydraulic model

**Target role:** determine what reduced models omit.

P07 must answer:

1. What spatial domain is modeled?
2. Are oil flow and heat transfer solved explicitly?
3. Which governing PDEs are used?
4. Which heat sources are distributed spatially?
5. Which material properties are temperature dependent?
6. What are the initial and boundary conditions?
7. How are radiators/tank/windings/oil ducts represented?
8. What outputs correspond to top-oil and hottest-spot quantities?
9. What parameters are needed that reduced models avoid?
10. Does the detailed model materially change peak temperature, timing, or threshold prediction?

**Gap-closing target:**

~~~text
reduced model states
↔
spatial thermal-hydraulic reference model
~~~

The goal is not to adopt CFD automatically. The goal is to determine whether higher fidelity changes the thesis-relevant result.

## 4. P08 burden — direct hottest-spot observability

**Target role:** determine how directly winding hottest-spot temperature can be observed.

P08 must answer:

1. What sensing technology is used?
2. Where are sensors physically located?
3. How is the hottest location determined?
4. What spatial coverage exists?
5. What measurement uncertainty/resolution is reported?
6. Does the measurement capture the true hottest point or only a local proxy?
7. How are sensors calibrated?
8. What transformer geometry/cooling mode is involved?
9. How are measurements used for model validation?
10. What remains unobservable?

**Gap-closing target:**

~~~text
candidate hottest-spot state
→ measurement/estimation evidence
→ validation feasibility
~~~

## 5. P09 burden — dense internal temperature distribution

**Target role:** quantify spatial nonuniformity.

P09 must answer:

1. How many internal temperature measurements exist?
2. Where are they located?
3. How large are spatial temperature differences?
4. Does top-oil represent the full oil field adequately?
5. Does one hottest-spot state preserve the relevant winding behavior?
6. Are bottom-oil/duct-oil/tank/radiator temperatures materially distinct?
7. Which states respond on different timescales?
8. Does loading alter the location of the hottest region?
9. What reduced state set best reproduces measured dynamics?
10. Which omitted spatial details are decision-relevant?

**Gap-closing target:**

~~~text
full spatial measurement
→ reduced-state sufficiency test
~~~

## 6. P10 burden — detailed thermal-hydraulic physics

**Target role:** explain reduced parameters from first-principles heat transfer.

P10 must answer:

1. Which momentum/energy equations govern oil circulation?
2. How do buoyancy, viscosity, density, conductivity, and heat capacity enter?
3. Which dimensionless groups govern flow/heat transfer?
4. How are winding/tank/radiator losses coupled to oil flow?
5. What determines effective thermal resistance?
6. What determines effective thermal capacitance?
7. What determines characteristic thermal times?
8. How does construction change flow paths and temperature fields?
9. What approximations permit model reduction?
10. Which detailed mechanisms must remain in the thesis model?

**Gap-closing target:**

~~~text
detailed heat-transfer physics
→ interpretation of reduced parameters
→ minimum-sufficient model
~~~

## 7. Standards gaps to close in parallel

Before Module 01 model freeze, direct standard audit must establish where applicable:

- definitions of top-oil and hottest-spot quantities;
- relevant temperature-rise test procedures;
- current loading/temperature calculation models;
- transformer/cooling applicability conditions;
- any normative thermal limits used;
- any current standard state-to-loading/capability relationship;
- whether duct-oil or additional temperature states are required for the selected architecture.

Relevant current authority candidates are listed in `MODULE_01_STANDARDS_SPINE_V1.md`.

## 8. Model-admission questions after P10

After P06–P10, answer explicitly:

### Q1 — State sufficiency
Can:

~~~math
X_P,th = [theta_TO, theta_HS]^T
~~~

represent the transformer with sufficient fidelity for the thesis decision problem?

### Q2 — Time sufficiency
Are `tau_o` and `tau_w` sufficient effective timescale descriptors, or are additional dynamic modes required?

### Q3 — Parameter identifiability
Can all required parameters be obtained for the selected transformer?

### Q4 — Observability
Can the required states be measured or estimated with acceptable uncertainty?

### Q5 — Validation
What experimental/benchmark data can validate the chosen reduced model?

### Q6 — Capability handoff
Can a current standard/manufacturer-supported map from thermal state to allowable electrical capability be established?

### Q7 — Extreme-heat transfer
Is the chosen model valid over the intended ambient-temperature range?

### Q8 — EV-loading transfer
Can the model accept the load/harmonic conditions generated by the eventual charging case?

## 9. Module 01 completion output

At the end of P10, Module 01 must produce one of only two outcomes:

~~~text
A. CANDIDATE POWER THERMAL MODEL ADMITTED FOR CASE-SPECIFIC PARAMETERIZATION
~~~

or:

~~~text
B. MODEL REMAINS OPEN — ADDITIONAL EVIDENCE REQUIRED
~~~

No model will be frozen merely to preserve schedule or narrative continuity.
