# Module 01 Paper Audits P01–P05 V1

**Status:** WORKING EVIDENCE RECORD — PAPER-SPECIFIC ACCESS DEPTH DECLARED  
**Effective date:** 2026-10-08  
**Evidence authority:** `../CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`  
**Reading method:** `../THERMAL_PAPER_SCHOOL_V2.md`

## 0. Audit rule

Each record distinguishes:

```text
metadata verified
≠
full text accessed
≠
equation audited
≠
parameter transferable
≠
model admitted
```

No numerical value, equation, or conclusion is transferable solely because it appears in a relevant paper.

---

# P01 — Roslan et al. (2017)

## Verified metadata

**Title:** A Simplified Top-Oil Temperature Model for Transformers Based on the Pathway of Energy Transfer Concept and the Thermal-Electrical Analogy  
**Venue:** *Energies*  
**Year:** 2017  
**DOI:** 10.3390/en10111843  
**Evidence class:** `[A3 + A4]`  
**Access status:** public full article available from publisher.

## Scientific problem

Develop and test a reduced top-oil-temperature model derived from energy-transfer pathways and thermal-electrical analogy.

## Physical mechanism

```text
electrical losses
→ heat input
→ thermal storage
+ nonlinear heat rejection
→ top-oil temperature evolution
```

## State / forcing interpretation

- Candidate reduced state: top-oil temperature / top-oil rise.
- Ambient temperature: external forcing.
- Loading/losses: input/forcing to the thermal subsystem.

## Mathematical lesson

The paper supports an energy-balance architecture of the form:

```text
heat generated − heat rejected = rate of thermal energy storage
```

with nonlinear heat rejection.

Any simplified equation written in this repository from that architecture is `[T1]` unless copied and audited directly from the paper with exact equation provenance.

## Experimental/model evidence

The model was evaluated using measured transformer top-oil data across multiple transformers and a step-loading case.

## Established

- Reduced top-oil dynamics can be represented through energy storage and heat-rejection terms.
- Thermal-electrical analogy is useful as a reduced representation.
- Ambient temperature and loading influence the transient top-oil trajectory.

## Limited

- Focus is top-oil temperature.
- The paper does not establish the final hottest-spot model required by the thesis.
- The paper does not establish a thermal-state-to-electrical-capability law.
- Numerical parameters are equipment-specific.

## Remaining

```text
top-oil prediction
→ hottest-spot prediction
→ transformer-specific parameterization
→ state-to-capability mapping
```

## Thesis transfer decision

`SUPPORTING / CORE MODEL EVIDENCE` for reduced top-oil energy-balance architecture.

---

# P02 — Swift, Molinski & Lehn (2001)

## Verified metadata

**Title:** A Fundamental Approach to Transformer Thermal Modeling—Part I: Theory and Equivalent Circuit  
**Venue:** *IEEE Transactions on Power Delivery*  
**Year:** 2001  
**Volume/issue/pages:** 16(2), 171–175  
**DOI:** 10.1109/61.915478  
**Evidence class:** `[A4]`  
**Companion validation paper:** Part II, DOI 10.1109/61.915479  
**Access status:** metadata verified from IEEE; technical interpretation supported by accessible copies/reproductions. Direct publisher full-text equation audit remains desirable before any exact Swift equation is frozen.

## Scientific problem

Formulate transformer transient thermal behavior from heat-transfer theory using a thermal-electrical equivalent circuit rather than relying only on empirical exponential temperature curves.

## Physical mechanism

```text
core + winding losses
→ thermal-source terms
→ oil-side energy storage
→ nonlinear heat rejection
→ oil temperature
→ winding/hot-spot thermal response
```

## State / forcing interpretation

- Reduced oil temperature: candidate thermal state.
- Reduced winding/hottest-spot temperature: candidate thermal state.
- Ambient temperature: external forcing.
- Electrical losses: thermal inputs.

## Mathematical lesson

Thermal-electrical analogy maps heat-flow rate to current, temperature potential to voltage, thermal resistance to resistance, and thermal capacitance to capacitance because the governing conservation equations share analogous structure.

Thermal capacitance provides state memory.

Nonlinear heat rejection means a single fixed linear RC time constant need not describe all operating conditions.

## Validation status

The companion Part II paper provides field verification for the top-oil model on one large OFAF transformer.

Do not conflate:

```text
top-oil validation
≠
hot-spot validation
```

Later independent literature reported structural inadequacy of the Swift hottest-spot formulation for the datasets tested; that criticism does not invalidate conservation of energy or the general thermal-electrical analogy.

## Established

- Energy-balance/equivalent-circuit architecture is physically defensible as a reduced model.
- Thermal capacitance creates memory.
- Heat rejection can be nonlinear.
- Ambient is forcing, not transformer state.

## Limited

- Lumped nodes are reduced/effective states, not literal full spatial fields.
- Hot-spot formulation requires separate validation.
- Field validation domain is narrow.
- Historical IEEE guide context is not current normative authority.

## Remaining

- Which reduced states are sufficient for the final transformer?
- Which current standard formulation applies?
- How do parameters transfer to a distribution/depot transformer?
- How does thermal state map to capability?

## Thesis transfer decision

`CORE PHYSICAL FOUNDATION`, but **do not freeze Swift's hottest-spot equation**.

---

# P03 — Susa, Lehtonen & Nordman (2005), Power Transformers

## Verified metadata

**Title:** Dynamic Thermal Modelling of Power Transformers  
**Venue:** *IEEE Transactions on Power Delivery*  
**Year:** 2005  
**Volume/issue/pages:** 20(1), 197–204  
**DOI:** 10.1109/TPWRD.2004.835255  
**Evidence class:** `[A3 + A4]`  
**Access status:** metadata verified; technical interpretation supported by accessible paper copies, author/institution records, and later peer-reviewed reproductions. Exact equation-symbol audit should be repeated against authoritative full text before model freeze.

## Scientific problem

Improve transient top-oil and hottest-spot temperature prediction by incorporating temperature-dependent oil viscosity and temperature-dependent losses within a nonlinear reduced thermal model.

## Physical mechanism

```text
load + ambient
→ losses
→ oil temperature
→ viscosity
→ convective heat transfer / effective thermal resistance
→ oil dynamics
→ winding/hottest-spot dynamics
```

and:

```text
winding temperature
→ winding resistance / loss contribution
→ heat generation
→ winding temperature
```

## State / constitutive distinction

Candidate reduced states:

```math
X_{P,th}
=
[\theta_o,\theta_{HS}]^T.
```

Constitutive/state-dependent quantities such as viscosity or effective thermal resistance need not be additional states if they are algebraic functions of admitted states.

Permanent lesson:

```text
state-dependent property ≠ additional state variable
```

## Mathematical lesson

The model is nonlinear and cascaded:

```text
ambient + load
→ top-oil dynamic state
→ winding/hottest-spot dynamic state
```

with temperature-dependent material/heat-transfer effects.

## Experimental evidence

The reported evaluation used varying-load tests on large ONAF/OFAF transformers and fiber-optic temperature measurements.

## Established

- Temperature-dependent oil properties materially belong in the reduced physics.
- Top-oil and hottest-spot are distinct dynamic quantities.
- Effective thermal resistance/time behavior may depend on state.
- Large-transformer experimental data support the model family.

## Limited

- Validation equipment consists of large power transformers.
- Cooling architectures differ from likely ONAN distribution/depot applications.
- Historical IEEE comparator is not the current IEEE loading guide.
- Exact parameter transfer is prohibited.

## Remaining

- Distribution-transformer applicability.
- Transformer-specific identification of thermal parameters.
- Current-standard compatibility.
- State-to-capability relation.

## Thesis transfer decision

`STRONG CORE CANDIDATE MODEL FAMILY — NOT FINAL MODEL`.

---

# P04 — Susa, Lehtonen & Nordman (2005), Distribution Transformers

## Verified metadata

**Title:** Dynamic Thermal Modeling of Distribution Transformers  
**Venue:** *IEEE Transactions on Power Delivery*  
**Year:** 2005  
**Volume/issue/pages:** 20(3), 1919–1929  
**DOI:** 10.1109/TPWRD.2005.848675  
**Evidence class:** `[A3 + A4]`  
**Access status:** IEEE metadata/abstract verified. Supporting physical interpretation is available from Susa's dissertation and secondary reproductions. **Direct full-paper equation-by-equation audit remains OPEN.**

## Scientific problem

Test dynamic transformer thermal modeling on a distribution-scale ONAN transformer and account for construction-dependent differences in thermal behavior.

## Experimental system

Publisher metadata identifies a 2500-kVA ONAN transformer without external cooling, with thermocouple measurements under varying loading.

## Physical mechanism

```text
transformer construction
→ oil-flow path / heat-transfer architecture
→ effective thermal resistance/capacitance
→ thermal time behavior
→ top-oil / hottest-spot dynamics
```

## Key cross-paper lesson

```text
same broad cooling label
≠
same thermal architecture
≠
same thermal parameters
```

The paper/author evidence indicates that hottest-spot-to-top-oil behavior and top-oil time-constant representation depend on construction.

## State / observation distinction

Thermocouple readings are observations at installed locations; they are not automatically identical to the true global hottest-spot state.

```text
state ≠ sensor reading
```

## Established

- Distribution-scale transformer construction materially affects reduced thermal dynamics.
- Top-oil/hottest-spot gradients are dynamic and design dependent.
- Effective thermal time behavior cannot be transferred solely by transformer class label.

## Limited

- One specific 2.5-MVA ONAN transformer.
- Direct equation audit of the published paper remains incomplete in the present evidence record.
- No EV-charging or extreme-heat-specific validation.
- Capability mapping remains absent.

## Remaining

- Quantitative identification of oil time constant for a specific ONAN transformer.
- Cross-transformer parameter transferability.
- Observability and spatial nonuniformity.
- Current-standard comparison.

## Thesis transfer decision

`CORE SCALE/CONSTRUCTION EVIDENCE`; **parameter transfer not authorized**.

---

# P05 — Wang et al. (2020)

## Verified metadata

**Title:** Top-oil temperature modelling by calibrating oil time constant for an oil natural air natural distribution transformer  
**Venue:** *IET Generation, Transmission & Distribution*  
**Year:** 2020  
**Volume/issue/pages:** 14(20), 4452–4458  
**DOI:** 10.1049/iet-gtd.2020.0155  
**Evidence class:** `[A3 + A4]`  
**Access status:** publisher metadata verified; institutional full-text manuscript available and audited at equation/result level for the key claims recorded here.

## Scientific problem

Determine whether top-oil time constant should be treated as a fixed rated value or calibrated as a function of operating/initial thermal condition for a specific ONAN distribution transformer.

## Experimental system

Reported transformer:

```text
200 kVA
11/0.433 kV
ONAN
mineral oil
```

Temperature-rise experiments were conducted using a standard-based test methodology.

## State / parameter distinction

Top-oil temperature/rise is the dynamic state quantity.

Oil time constant is a dynamic descriptor/model parameter; it need not be an additional independent state if it is obtained algebraically from current/initial state and load.

Permanent lesson:

```text
state-dependent parameter ≠ additional state
```

## Key equations audited

Steady-state top-oil rise model:

```math
\Delta\theta_{oil}
=
\Delta\theta_{oil,rated}
\left(
\frac{1+RI_{pu}^{2}}
{1+R}
\right)^n.
```

Constant-load transient fitting form:

```math
\Delta\theta_{oil}(t)
=
\Delta\theta_{oil,initial}
+
(\Delta\theta_{oil,ultimate}-\Delta\theta_{oil,initial})
(1-e^{-t/\tau_{oil}}).
```

The paper also uses normalized/relative oil-time-constant concepts and develops a correction incorporating operating and initial thermal condition.

## Parameter identification evidence

The authors used multiple temperature-rise tests over approximately 0.7–1.4 pu loading to identify/calibrate thermal quantities.

A fitted oil exponent around (n=0.82) is reported for this transformer.

A rated-reference oil time constant around (294.3) min is reported for this transformer.

**These numerical values are case-specific and must not be transferred.**

## Dynamic evaluation

The improved model was evaluated under additional changing-load and step-overload profiles, including a reported 0.7→1.8→0.7 pu sequence.

Reported trajectory RMSEs favor the improved state/load-dependent time-constant treatment over the fixed-time-constant comparator for the tested cases.

These are `[A3]` case-specific results, not universal performance guarantees.

## Established

- Effective oil time constant can vary with loading and initial thermal state for the tested transformer.
- Thermal history materially influences transient response.
- Transformer-specific parameter calibration improves top-oil prediction for the tested dynamic profiles.
- Treating oil time constant as universally fixed can materially degrade transient prediction.

## Limited

- One transformer.
- Within-transformer calibration/validation is not cross-transformer validation.
- Good first-order fitting does not prove the real thermal field has only one mode.
- Extreme ambient heat was not the primary hazard experiment.
- Hottest-spot and capability mapping remain outside the main P05 contribution.

## Remaining

- Independent numerical/experimental confirmation of load-dependent time constants.
- Physical explanation of time-constant variation from detailed heat transfer.
- Cross-design generality.
- Coupled top-oil/hottest-spot prediction.
- State-to-capability relation.

## Thesis transfer decision

`CORE PARAMETER-IDENTIFICATION / STATE-TIME EVIDENCE`; numerical values **NOT TRANSFERABLE**.

---

# P01–P05 cumulative status

```text
P01 — reduced top-oil energy-transfer architecture
P02 — fundamental energy-balance/equivalent-circuit architecture
P03 — temperature-dependent viscosity/loss nonlinear dynamics
P04 — construction/cooling architecture affects reduced dynamics
P05 — effective oil time constant varies with operating/initial condition
```

These five papers jointly justify proceeding to P06–P10, but they do **not** justify freezing the final state vector, exact ODEs, thermal limits, or Power-system capability law.
