# Verification, Validation and Uncertainty Quantification (VVUQ) — coupled electrothermal model v0

**Status:** Protocol and preregistered decision gates, **NOT results**. Krama original row-level observations have been requested by the user from the corresponding author and remain unreceived. Gong/Kunlasing full PDFs verified but raw synchronized experiments unavailable. No joint EVSE-transformer field dataset has been received. Do not fit unspecified parameters to invented traces.

## A. Verification / physical consistency before calibration

| Gate | Test | Required outcome | Blocker |
|---|---|---|---|
| V1 | SI units on every state term; P+Q not summed; h–s and kWh–J conversions | C[K] * Tdot[K/s] = W; no unit mismatches | None (symbolic) |
| V2 | Transformer internal thermal flux antisymmetry | Sum two-node energy balances cancels G_wo(T_w−T_o) exactly | None |
| V3 | Charger electrical conversion accounting | At matched sample times P_AC = P_DC + L_EVSE, with nonnegative residual and explicit meter boundary | Raw synchronized streams necessary for *empirical* checks |
| V4 | Thermal equilibrium limiting case | For constant ambient/loss and positive conductances, stable equilibrium with correct signs; no nonphysical instantaneous jumps | None for theoretical |
| V5 | Zero-current & unpowered limits | Correct core/no-load heating only while energized; off state must use explicit core/fan modes | Nameplate, control specifications required |
| V6 | Power flow boundary | Balanced approximation valid only with voltage/PF consistency; 3-phase unbalance/harmonics require fuller network | Actual meter traces |
| V7 | Numerical integration and event timing | Step-size/solver tolerance and event-detection refinement until outputs stable; ensure mode hysteresis avoids chattering | Simulator to be implemented and verified |
| V8 | Physical and service constraint enforcement | 0≤P_DC≤each actual limit; E_DC monotone in active charging; no invented recovery reset | Source and scenario specification |
| V9 | Observability vs assumptions | Sensor T_w,top != T_H, measured T_rect != semiconductor junction; charger-internal transformer != upstream utility transformer | Source audit established; data needed |
| V10 | Structural identifiability/rank | Before estimating C,G,alpha prove input excitation and observable combination; profile likelihood or Fisher information/sensitivity rank | Experiment design/raw data |

Uncertainty: use physically justified tolerances, parameter ranges or interval bounds where raw evidence absent. Avoid false confidence intervals from one chosen nominal parameter set.

## B. Source-specific calibration/validation gates

| Source | What is experimentally supported | What can legitimately be benchmarked | Calibration and inference limits |
|---|---|---|---|
| Gong (2015), 9p original | Top-oil & top-winding thermal transients on **one** 25-kVA transformer; DC-equivalent heating under programmed ambient/load; real temperature effect of prescribed schedules; reported max absolute errors <2°C winding top, <4°C oil | Heat-transient response under comparable load/ambient schedule with **same observable T_o or top-winding sensor** | No true winding hotspot measurement, original row-level records or independent hardware set; never label as matched real EVSE P thermal test |
| Kunlasing (2022), 4p original | Live transformer electrical metering & oil PT100; physical **manually generated** Zigbee request changes IEC 61851 PWM current allowance in two chargers | Observation pipeline logic and existence of manual command-to-permitted-current actuation | Automatic temperature-triggered controller and on-site thermal effect of its actuation NOT validated; 3-EV automatic overload schedule is simulated |
| Krama (2026), 16p original audit | 50-kW field charger rectifier/ambient sensors; matched AC/DC offered/delivered and session records; extreme heat causes charger power derating; session holdouts on empirical offer-power response | Power-offered model within comparable charger/ambient/session domain; compare against same-target controlled physical RC baseline if raw records permit | No P utility transformer T measured; whole charger loss != specific junction heat; no native firmware limit flag; one charger/site only; June session R² ~.416 vs stronger other sessions |

**Do not fit a two-way P↔E interface to any of the three independent component datasets.** Such a fit would not be identifiable as joint interface validation, regardless of apparent model agreement.

## C. Parameter-to-observation eligibility

| Parameter or effect | Minimum observations and covariates | Source availability / decision |
|---|---|---|
| P thermal \(C_o,G_{oa}\), oil response | Time-aligned transformer T_o, ambient, measured load/current and losses (or specified model) across load perturbations | Gong has plotted physical traces/calibration results, not user-supplied raw samples; independently reproduce coefficients only if data provided |
| P winding \(C_w,G_{wo}\) | Top-winding or internal temperature, oil, loss split/current at temporal resolution and sensor mapping | Gong physically measures top-winding, not true hotspot; HST calibration not justified from paper alone |
| P hotspot \(H(\cdot)\) | Fibre optic winding hotspot or experimentally justified reference model and calibration | Not measured in Gong or Kunlasing; require separate hardware source/standard-specific validated correspondence |
| Charger \(C_c,G_{ca},\alpha_c\) | T_rect, T_amb, P_AC, P_DC, cooling/fan status or independent constraints, with excited thermal dynamics and time calibration | Krama raw samples requested; absent thermal heat allocation, three parameters structurally non-identifiable from single equation |
| Derating curve \(D(T_c,q_E)\) | Offer-power time series, temperature, firmware/controller modes, vehicle demand/SOC and AC supply | Krama has field offer/deliver/SOC in published analysis; raw data not received; field fit is device-specific; firmware trigger remains unknown |
| Electrical receiving response T_e→P | Simultaneous EVSE P_AC/offer/T_c and upstream transformer P load/temperature, baseline load, ambient, switching and synch clocks | **No matched dataset among 3 focal studies** |
| P restriction→EVSE response | Time-stamped P thermal/electrical state, actual policy/limit command, EVSE acknowledgement, AC/DC delivered, service requirements | Kunlasing manual actuation only; Gong planned schedules on lab P; field automatic temperature-triggered action unobserved |
| Electric mobility viability | Actual required charging energy at departure, departure deadline, delivered DC energy (battery SOC if validated) and other critical services | No real mobility trip obligation measured in 3 studies |

## D. Experimental validation levels (do not merge categories)

1. **Mathematical verification:** symbolic identities, dimensions, numerical convergence and invariants on arbitrary nonempirical test values.
2. **Component calibration:** fit thermal node parameters to training transformer or charger measurements.
3. **Independent temporal/session validation:** evaluate on *unseen* contiguous dates/events or leave-one-session-out without leakage of fitted states, scaling or hyperparameter selection.
4. **Independent hardware/site validation:** test on additional transformers or EVSE chargers with genuinely different hardware/weather/use profiles; recalibration policy defined in advance.
5. **Directional interface validation:** same-event measured source stimulus, control action and downstream electrical/thermal response on **paired** transformer/charger with confounders/time delays controlled.
6. **Service/recovery validation:** real critical-energy requirements and deadlines or a clearly identified simulation demonstrator; no claim to real mobility service without actual obligation observations.

For Krama, the published temporal/session splits from the prior original audit concern **the same charger**. The June LOSO offered-power result (R² .416, MAE 5.41 kW, RMSE 6.23 kW) must be reported alongside August (R² .983) and September (R² .955); do not report only pooled in-sample R² .9852 or insinuate independent-device validation.

## E. Measurement and synchronization plan (conditional on access)

- Preserve raw sensor IDs, raw timestamps and time zones, leap/DST handling, missingness, calibration certificates, rated values, ownership/data use permissions. Never force-fill missing values across distinct time-resolution streams.
- Krama: 5-min ambient/rectifier channels versus 1-min electrical/SOC; compare window-averaged electrical inputs to heat-state samples, and propagate sample-window/timing ambiguity. A sub-five-minute thermal threshold-crossing time cannot be asserted from five-minute temperature readings.
- Gong: electrical DC-equivalent test schedules, programmed ambient, each thermocouple/needle channel, tested transformer thermal initial condition and mode. Keep measured top-winding distinct from modeled hotspot. Where only plots are public, do **not** digitize and treat reconstruction as original laboratory measurements.
- Kunlasing: oil PT100, transformer 3-phase current, manual/automatic command flags and timestamp, Zigbee delivery, charger pilot PWM/current limit and delivered electrical power (if recorded). Published paper lacks paired raw time series; do not assume these fields exist.
- New joint trial needed for actual P↔T_e interface: measured P transformer current/voltage/temperature at a documented point, matched EVSE AC/DC/rectifier signals, ambient near both units, complete EVSE battery-limit and command logs, feeder non-EV load, operational modes and time synchronized clock uncertainty. Original thermal receiver measurements and ethically authorized access necessary.

## F. Baselines, tests and preregistered reporting

Model family order:
- B0: **decoupled** component response given measured exogenous loading and ambient (physics RC/standards-consistent after authorized standard equations verified).
- B1: **electrically coupled but static thermal restriction**, identical physical parameters and controller observation budget.
- B2: **coupled electrothermal ODE/DAE** with dynamic transformer and EVSE thermal states, no data-driven augmentation.
- B3: physics-informed statistical residual **only if** enough aligned, identifiable, independently held-out data show a reliable advantage; no default PINN.

Use matched hazard/initial conditions, matched controller access and fair parameter budgets; compare observed T_o, T_rect, P_AC, offered/delivered kW, triggered events and **time-to-service-completion**. Report MAE, RMSE, signed error, 90/95% interval coverage if intervals are calibrated; event precision/recall and transition-time error **only if** ground-truth event labels exist. For physical validation, preregister folds before optimizing hyperparameters. Avoid random temporal leakage. State confidence limitations for single-device tests.

**Novelty null hypothesis:** a validated prior standard thermal model plus a simple temperature-conditioned power limiter may explain all available effects. The proposed coupled dynamics must outperform or reveal a falsifiable phenomenon under matched boundary/validation, not just add states or draw cross-layer arrows.

## G. Qualification gates and completion decisions

- G0 = exact identity/source version checked (achieved for three primary sources).
- G1 = equations, variables, sensor locations and status traced to source pages (achieved for Gong/Kunlasing, prior Krama original extraction).
- G2 = SI/energy/observation and mathematical well-posedness checks (candidate derivation done, executable tests not completed).
- G3 = original row-level component data under authorized conditions (blocked for all as direct research copies).
- G4 = calibrated vs independent physical **component** outputs (source authors' component results exist; **new thesis** calibration not performed).
- G5 = synchronized joint P-E receiving-state data (blocked).
- G6 = independent field response and critical charging service/viability demonstration (blocked).
- G7 = validated novelty or theorem with declared assumptions/proof/external challenge (not reached).

**Permissible current conclusion:** a proposed dimensionally consistent candidate hybrid electrothermal coupling architecture exists, built on qualified prior component evidence. **Not permissible:** claiming that the physical cross-infrastructure interface is empirically calibrated/validated or that any new theorem has been proved.
