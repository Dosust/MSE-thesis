# Canonical Temperature-Mediated Electrical–Thermal Research Objectives V2

**Decision date:** 2026-10-12  
**Decision authority:** Researcher-approved formal version-controlled objective amendment.  
**Status:** APPROVED OBJECTIVE WORDING — PENDING INTEGRATION TO `main`; becomes the current canonical objective authority **when the amendment is merged under repository governance**. Until that point, `CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md` remains the active main-branch frozen record.  
**Supersession upon merge:** Replaces **only the exact General Research Objective and SO1–SO3 wording** in `CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`. Preserve V1 unchanged as superseded historical provenance.  
**Official thesis title:** `CANONICAL_THESIS_TITLE_V2.md` (unchanged).  
**Governing scope:** `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md` and `CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md` (unchanged).  
**Other unchanged authorities:** `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`, `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`, `CANONICAL_RESILIENCE_DEFINITION_V1.md`, `CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`, `PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md`, conceptual framework V5 and mathematical framework V3.

## 1. General Research Objective — exact researcher-approved wording

> **To investigate and mathematically model temperature-mediated electrical–thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and quantify their effects on electricity and mobility service resilience over time.**

## 2. Specific Research Objectives — exact researcher-approved wording

### SO1 — Identify and Qualify

> **Identify, characterize, and qualify relevant physical states, interfaces, and candidate temperature-mediated electrical–thermal coupling mechanisms between the Power System and the Electrified Transportation System under extreme heat.**

### SO2 — Develop and Model

> **Develop physics-based mathematical models of the qualified temperature-mediated electrical–thermal coupling mechanisms and their state–time evolution under extreme heat.**

### SO3 — Analyze and Quantify

> **Analyze and quantify supported critical transition times, propagation delays where identifiable, and the resulting consequences for electricity and mobility service resilience.**

**Verbatim text control:** Do not silently remove "temperature-mediated" from GO/SO1/SO2, convert candidate mechanisms to established facts, or reinstate "required" as an adjective attached to "service resilience" in SO3. The canonical *definition of resilience* still refers to maintaining/recovering **required electricity and mobility services**; SO3 has not modified that definition.

## 3. Amendment type and scope preservation

This is a **clarifying objective-language amendment**, not an expansion to general electrical interdependencies or a new research program. In this thesis, "temperature-mediated electrical–thermal coupling" means a qualified directional dependency for which a heat/temperature-dependent physical state, capability, or realized thermal operating condition changes electrical loading/transfer constraints, actual charging capability, or electricity/mobility service **through an explicit physical/operational pathway**.

- **External extreme heat** acts on the two separate systems; shared thermal exposure alone **does not demonstrate intersystem coupling**.
- **Ordinary AC transfer/charging load** is a required physical/electrical boundary, not automatically a thermally mediated interdependency.
- **I2 T→P:** candidate charger temperature/cooling/control response → actually observed grid-side AC P,Q/current → P2/P1 loss and thermal behavior; **not** V2G or reverse electric flow.
- **I3 P→T:** candidate P1 thermal state → demonstrably installed/implemented P3 protective or permission action → real T1 charging availability/acceptance; **OPEN** unless installed rule and effect qualified.
- **I4** internal EVSE heating/cooling/derating, **I5** actual DC transfer to T2 energy/SOC/readiness, **I6** later HVAC-to-charging demand pathway remain supporting/component-level mechanisms under existing evidence rules.
- **I7** supporting **electricity-price-informed charging decision** was separately researcher-approved on pricing PR #75, still outside physical thermal-coupling qualification. Pricing is not a thermal state or additional research objective. That separate PR/its merge status is not changed by this amendment.
- **Eight selected equipment subjects** remain P1 Distribution Transformer, P2 Distribution Feeder, P3 Transformer Protection/Load-Management Hardware, P4 Transformer Cooling Equipment; T1 DC EV Charger, T2 Vehicle Battery Pack, T3 EVSE Cooling Equipment, T4 Vehicle HVAC Equipment.
- These eight research subjects are not eight required thermal ODEs, and are not the exhaustive physical system boundary. Do not revise component membership, frozen state–time definitions, M0/M1/M2 meanings, the source-priority rules, or the evidence/validation gates.
- AI development, digital twins, price/market optimization, full traffic equilibrium, a new independent sustainability/SDG objective, or universal resilience optimization are **not introduced**.

## 4. Scientific chain: interpretation, not a prevalidated causal discovery

```text
H(t) external heat forcing
    ↓ affects component states (independently unless coupling shown)
Relevant evolving states and observed port quantities
    ↓ formulate and evaluate candidate pathways [SO1]
Qualified temperature-mediated electrical–thermal interfaces (if supported)
    ↓ derive minimum-sufficient equations, states and constraints [SO2]
Coupled state–time trajectories (within admitted model's validity domain)
    ↓ test hypotheses against independent evidence and quantify [SO3]
Transition/action/receiver/service times and electricity–mobility service resilience
```

Distinguish the methodological sequence from physical arrows. In particular, a physically valid result may be **no identified I3 action, no meaningful propagation delay, or unresolved causal attribution**; do not manufacture an effect to fulfill SO3.

## 5. Mathematical interpretation and operator-type discipline (not frozen constitutive laws)

An admissible *candidate* physics-first DAE structure is:

```math
\begin{aligned}
\dot{\mathbf{x}}_P&=\mathbf f_P(\mathbf{x}_P,\mathbf z,\mathbf u,H;\boldsymbol\theta_P),\\
\dot{\mathbf{x}}_T&=\mathbf f_T(\mathbf{x}_T,\mathbf z,\mathbf u,H;\boldsymbol\theta_T),\\
\mathbf 0&=\mathbf g_{\mathrm{network+admitted}}(\mathbf{x}_P,\mathbf{x}_T,\mathbf z,\mathbf u,H).
\end{aligned}
```

- `H(t)` is exogenous heat/weather forcing, not a Power→Transportation or Transportation→Power physical interface, and not an internal state.
- `x_P` and `x_T` hold only necessary admitted physical/operational/energy states; `SOC` is an **energy** state, not a thermal state.
- `z` contains algebraic interface/port quantities, e.g. **actual EVSE grid-side AC** real/reactive demand and relevant network voltage/current; received DC power and battery-terminal power are not automatically identical.
- `u` contains operating control/permissions when evidenced, **not** arbitrarily presumed thermal actions.

The user's proposed conceptual decomposition

```math
\mathbf g \sim
\begin{bmatrix}
\mathbf g_{\mathrm{network}}\\
\mathcal I_{P\to T}\\
\mathcal I_{T\to P}
\end{bmatrix}
```

is a useful **relationship classification**, not automatically an exact DAE stacking of three algebraic equalities. Only constraints with compatible defined domains/codomains are assembled as `0=g(...)`; qualified I2 may involve a constitutive temperature-to-actual-AC-demand law and cross-network load influence, whereas I3 may involve a measured/evidenced *hybrid control or discrete protection action*. Neither requires an independently evolving interface state without memory evidence. Prevent duplicate counting of I1 grid supply/network flow, P4/T3 heat rejection, and price information as thermal coupling.

This amendment **does not choose** exact device heat-transfer laws, transformer thresholds, charger derating parameters, P3 trip logic, available datasets or formal validation results.

## 6. Time, delay, and service-output safeguards

For a physically declared admissible set `K`, study horizon `[t_0,t_f]`, and meaningful modeled state `x(t)`, define first exit only if it occurs:

```math
t_{\mathrm{crit}}=\inf\{t\in[t_0,t_f]:\mathbf x(t)\notin\mathcal K\}.
```

If the set is empty, state **no observed/predicted first exit within the study horizon**; do not fabricate a finite time. Similarly,

```math
\tau_{i\to j}=t_j^{\mathrm{response}}-t_i^{\mathrm{event}}
```

is an *attributable propagation delay* only after the source-to-receiver mechanism, event/response definitions and confounding controls are qualified. Correlated event times are not enough.

With service quantities defined on compatible units/functional bases:

```math
D_e(t)=[S_{e,\mathrm{req}}(t)-S_{e,\mathrm{del}}(t)]_+,\qquad
D_m(t)=[S_{m,\mathrm{req}}(t)-S_{m,\mathrm{del}}(t)]_+.
```

These deficits require explicit time-dependent **service requirements** and **actual delivered services**. Readiness can be a justified *proxy* for mobility service, not proof of completed trips. Maintaining or recovering required services remains the current canonical resilience definition; no universal scalar resilience index is created.

## 7. Scientific approval and unresolved model/evidence gates

**Approved:** This exact objective wording and its narrow electrothermal interpretation, with independent SO1 qualification, SO2 mathematical modeling, and SO3 supported/time-resolved consequences.

**Unresolved:** precise equipment/case parameters, P3 deployed action, full I2 causal demonstration, I6 delay, I7 user price response, threshold crossings and delays, validated equations, credible independent validation, physical causality, numeric sustainability outcomes, and final testable RQs/hypotheses.

**Finality:** On merge, V2 supersedes the **objective wording** in V1; V1 remains immutable history. This change is not evidence that all hypothesized thermal paths or resulting resilience changes exist.
