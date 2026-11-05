# Measurement-first protocol for Power–Electrified Transportation interdependencies (v1)

**Date:** 2026-11-05. **Status:** Definition of evidence and metrics, not a new experimental finding.  
**Thesis scope:** Physics-based P ↔ electrified transport under extreme heat. Separate measured electrical behavior from unmeasured thermal or service effects.

## Scientific rule

An interdependency is a *physical or operational cross-system dependence through an identifiable interface*, not merely two measured curves moving together. A numerical similarity or an imposed threshold cannot establish wiring, mechanism, causal direction or service consequences. The analysis must say precisely which feature it measured and which physical claims are still unverified.

## M1–M6: What to measure and how to interpret it

| Metric | Exact question and variable(s) | Definition / units | Evidentiary qualification |
|---|---|---|---|
| **M1 — Network interface** | Is the EV-point meter supplied through the particular power feeder/transformer? | Documented binary topology connection A(g,e) = 1 if verified; otherwise **unknown** | Feeder map and source meter identification required; correlation cannot establish exact feeder ancestry |
| **M2 — Cross-voltage co-response** | Do measured 20 kV and EV-point 400 V voltage changes coincide? | Relative voltage change δU_k = (median U_k,post − median U_k,pre) / median U_k,pre [dimensionless]; change-point timing Δt_U = t_400 − t_20 [s]; optionally ratio G_U = δU_400/δU_20 when denominator exceeds measurement noise | Establishes electrical **co-variation**, not physical path attribution or causal transfer by itself |
| **M3 — P→T electrical response** | How does measured EV-point active power vary around a measured supplied-voltage event? | P_EV = P_L1 + P_L2 + P_L3 [W] only if phases valid; pre/post ΔP [W]; **P_EV at t=0**, first sustained power-transition time t_P [s], and τ = t_P − t_U [s] | Event-time loading, stable pre-baseline, competing charger/control transitions and matched references needed before interpreting as operational dependence |
| **M4 — T→P loading response** | Does EV-point operation change loading of its verified parent feeder? | Matched changes in measured feeder P and EV-point P [W]; optional ratio ΔP_feeder / ΔP_EV if denominator is identifiable | Requires feeder-specific metered active power, topology and other-load controls; unrelated 110 kV aggregate power or 20 kV current alone is insufficient |
| **M5 — Thermal interface** | Does heat constrain transformer or EVSE electricity supply or charge capacity? | Transformer headroom T_limit − T_hotspot [°C]; allowable current minus actual [A]; EVSE allowable charging power minus requested [W] | Real thermal state / calibrated physical parameters and documented derating curves required; none derivable from synchronized voltage alone |
| **M6 — Mobility consequence** | Was required charging/mobility service not delivered because of a verified electrical or thermal constraint? | Charging-energy shortfall integral max(0, P_required − P_delivered) dt [Wh]; service availability and deadline measures | Requires charging requirement, EV/charger state and service outcome; metered power alone does not establish a service failure |

These six metrics address different questions. **Never aggregate them into a single “interdependency score”** where missing topology, thermal data or service ground truth can be hidden by an electrical correlation.

## Rules for every dataset, plot and event

1. **Define the physical interface** and what is known or unknown about connectivity and device state.
2. **Name measurements precisely**, with units, source device, sample interval, missingness, voltage basis (positive sequence vs phase-to-neutral), and meter sign convention.
3. **Declare the metric before evaluating it:** event trigger, baseline, windows, active-power cutoff, sensor threshold, change-point rule, expected mechanism and whether a timing analysis is meaningful.
4. **Use reference noise and instrument accuracy:** the exploratory 0.15% voltage-step screen, 500 W pre-power screen, 100 W change summary and 45 s gap are not proven laws of devices. Sensitivity-check them. If a detection threshold is needed, justify it using metrology or empirical baseline-noise distributions (e.g. 1.4826 × MAD for a clean difference signal).
5. **Require temporal ordering:** distinguish instantaneous 100 ms jump, sustained change onset, one-second average jump and pre/post window medians. A post-window median shift can be caused by a power transition *before* the selected voltage step.
6. **Control alternatives:** charging session start/end, charger setpoints, source OLTC controls, other feeder loads, ambient conditions, common disturbances and episode clustering. Forty-five seconds between timestamps does not guarantee independent experiments.
7. **Report a bounded claim** under one of: OBSERVED SIGNAL, OBSERVED CO-RESPONSE, STRUCTURALLY VERIFIED INTERFACE, CONDITIONALLY SUPPORTED OPERATIONAL DEPENDENCE, CAUSALLY IDENTIFIED DIRECTION, NOT IDENTIFIABLE, NOT MEASURED.
8. **Do not invent physical causality.** A verified operational interdependency requires evidence of a cross-system connection/mechanism plus meaningful measurement of dependence under documented operating conditions; a truly causal claim needs defensible identification beyond time-lag and correlation.

## KIT campus measured dataset: classification as of 2026-11-05

**Original:** https://doi.org/10.5281/zenodo.22826984. Original 100 ms 110/20/400 V data verified earlier; 50-day 1 s derivatives and two narrowly extracted 100 ms event windows analyzed on user's Mac.

| Existing evidence | Valid conclusion | What remains unestablished |
|---|---|---|
| 20 kV and EV-meter 400 V voltage curves rise together around 2026-03-10 15:32:02 UTC, fall together around 15:55:02 UTC, with 110 kV comparatively stable | **M2 OBSERVED: cross-voltage co-response** within same campus measurement system | Exact parent-feeder link, physical causation and transfer function |
| EV meter point peak real power ~9.628 kW; 101,930 valid 1 s entries have absolute real power ≥500 W | Substantial measured electrical power exchange at EV-labeled point | Battery charge-state/status not directly measured |
| 159 of 45,789 20 kV 1 s voltage-step candidates had preceding median absolute EV-point real power ≥500 W; strongest spaced 60 selected | **Conditioned event co-occurrence** | Not 159 independent physical experiments; top-60 cap is selection, not all cases |
| 10 selected events had absolute pre/post power change ≥100 W; 8 had a >100 W power jump *before* selected voltage event | **M3 descriptive event response confounded** in most screened cases | Voltage-induced power change not established |
| 16:00:03 UTC power drop precedes t=0 by 11–12 s | Selected t=0 voltage step **cannot explain the earlier power decline** | Could reflect independent charging-point state or an earlier unexamined disturbance |
| In original 100 ms event windows, largest later power jumps −243.55 W at +9.8 s (15:32:02 event) and +229.37 W at +8.3 s (15:55:02 event) | **M3 time-ordered co-variation observed**; lag of *largest jump*, not mechanism onset | Causal response, controller intervention or charging status not verified |
| Same-location multi-voltage recordings but no proven branch-specific feeder map, measured feeder real-power response, temperature/derating or service demand | M1/M4 unverified; **M5/M6 NOT MEASURED** | Cannot validate extreme heat or mobility resilience with this dataset alone |

**Permitted thesis language:** The KIT source demonstrates synchronized cross-voltage electrical changes and time-varying power at an EV-labeled metering point. It supports bounded electrical co-response analysis and hypotheses about power–EV operating dependence. It does **not** by itself identify a causal feeder-to-charger mechanism, thermal derating, or unmet mobility service.

## Required next workflow

**INTERFACE → OBSERVABLES → UNIT/TIME QA → DEFINE METRIC AND BASELINE → MEASURE → UNCERTAINTY AND ALTERNATIVES → EVIDENCE GRADE → SCIENTIFIC CLAIM**

For these two 551-row raw 100 ms CSV windows, next compute **M2 voltage-step amplitudes/timings** and **M3 event-time EV power / sustained change-point timing / baseline stability** with explicit thresholds and an alternative-event check. This is **electrical co-response measurement**; do not call it thermal causality or resilience validation. Then seek real feeder topology and loading for M1/M4 and independently measured thermal/service information for M5/M6.

## Local project evidence

- [Whole-record EV power](KIT_EV_POWER_FULL_RECORD_FINDINGS_2026-11-05.md)
- [Power-conditioned 20 kV candidates](KIT_EV_POWER_CONDITIONED_VOLTAGE_RESULTS_2026-11-05.md)
- [10-event temporal check and two original-resolution waveform audits](KIT_EV_POWER_LARGE_CHANGE_EVENT_AUDIT_2026-11-05.md)
- [Original-window analysis script](../../../tools/kit_oltc_100ms_event_window_audit.py)
