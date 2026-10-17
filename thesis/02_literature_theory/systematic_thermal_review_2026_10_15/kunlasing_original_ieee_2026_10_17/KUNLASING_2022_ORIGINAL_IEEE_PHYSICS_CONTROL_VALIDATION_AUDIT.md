# Kunlasing et al. (2022) — original IEEE full-text physics, measurement, and validation audit

**Verified 17 October 2026; original full text obtained.** Patchimaporn Kunlasing, Noppadol Charbkaew, Teratam Bunyagul and Yotaka Chompusri, *Transformer Load Monitoring and EV Charging Control Function*, **2022 19th ECTI-CON**, IEEE DOI [10.1109/ECTI-CON54298.2022.9795360](https://doi.org/10.1109/ECTI-CON54298.2022.9795360). Four-page original IEEE Xplore PDF; ASU authorized-use watermark/download 2026-10-17 05:51:41 UTC. PDF SHA-256 `4f95ec94a621dd74e02b4bcd7e389667fe4296853312fc1a6451ed9fe8ff90b4`, 3,119,729 bytes. Original copyrighted/ASU-licensed PDF retained in authorized user upload, **not copied into GitHub**.

## Source-scoped engineering claim

The Transformer Load Monitoring (TLM) system uses electrical and thermal **measurements** and supplies an overload-responsive EV-current **control capability**. The experimentally demonstrated charger actuation is a manual-request test via Zigbee and IEC 61851 control-pilot PWM. The authors additionally report a **three-EV simulation** of overload mitigation. The 2022 paper does **not demonstrate that measured transformer oil temperature triggers EV-current reduction**, nor a quantitative physical receiving-side EVSE heat or transformer thermal-control experiment.

## Equation and system audit (original printed page references)

| Original source locator | Precise object | Physical/observational meaning | Status and boundary |
|---|---|---|---|
| Eq. (1), PDF page 2 / Section II.A | `I_rms=sqrt((sum_(n=0)^4095 i[n]^2)/4096)` | Root-mean-square current computation from a sample buffer (4,096 samples at 4,096 Hz for I and V acquisition, per article text). | **Only numbered mathematical equation** in the article; metrology, **not** thermal ODE/PDE or coupling law. |
| Sec. II.A, page 2; Figs. 3–4 | Four CTs (3 phases + neutral) on LV transformer; 24-bit current and 16-bit voltage ADC; 4096 Hz sampling; stated 0.2S metering performance | Real distribution-transformer electrical sensing and data records | Metering class is not thermal-sensor uncertainty, and electrical sampling rate is not time-stamped synchronized physical interface validation. |
| Sec. III.A, page 3; Figs. 7–8 | Three-wire **PT100 oil-temperature sensor**, MAX31865 resistance-to-digital converter over SPI, continuous oil-temperature monitoring; ambient temperature and transformer percent load | Direct **transformer oil temperature** observation; recorded transformer oil vs ambient vs % rated kVA for office-building-fed transformer | **No measured winding hot-spot** and no verified numerical heat-balance law. Plot is descriptive; load and weather confounded. Sampling interval, temperature probe uncertainty, time alignment and independent test splits not specified. |
| Sec. IV, pp. 3–4; Figs. 11–12 | On overload, TLM can transmit Zigbee request; charger changes IEC 61851 control-pilot **PWM duty cycle** to change allowed EV charging current. Increase request when load below 80%. | Controllable information/control pathway from P load status through I to T EVSE. Figure 12 illustrates different **permitted charging limits** (30 A and 7 A). | Prototype actuation **physically tested on-site with two EV chargers, but requests were generated MANUALLY**; do not claim closed-loop automatic field operation or actual current/energy time-series validation. |
| Sec. IV, p. 4; Fig. 13 | Three-EV controlled vs uncontrolled charging **computer simulation**; uncontrolled transformer overload during 19:00–21:00, controlled reduction commands at 19:00 and 20:00 and increase at 21:00 | Simulation of electrical-load management, not a thermal field test | Do not describe Fig. 13 as measured transformer current, temperature response, actual grid service, or measured restored charging energy. |

## Experimental separation

**Demonstrated physical observables**:
1. TLM meter installed with LV current transformers; online voltage/current/load records.
2. Transformer oil temperature and ambient temperature monitored; Fig. 8 depicts an office load case and interpretation by authors: ambient temperature accompanies lower oil temperature during rainy period; office load profile peaks before ambient. **Observational association, not isolated ambient causal identification**.
3. Two instrumented/modified EV chargers receive manually issued Zigbee current-reduction requests. Control pilot PWM duty cycle changes. Figure 12 illustrates changed **current limits**, not a report of calibrated delivered charging power/SOC, transformer hot-spot or charging delay.

**Simulation**: separate three-EV simulated charging with overload scenario and virtual current-control requests. It must not be conflated with the two-charger manual on-site actuation test.

**Not established by this four-page source**:
- No transient transformer **thermal ODE/PDE**, thermal RC parameter or experimentally calibrated heating law presented.
- No demonstration of **oil-temperature-conditioned PWM command generation**. The implemented control condition is electrical *overload/percent load*, despite availability of oil temperature telemetry.
- No same-event timestamped oil-temperature → charging-curtailment → transformer receiving-temperature test.
- No high-ambient EVSE rectifier thermally derating evidence; no measured transformer winding maximum/hot-spot; no calibrated cross-domain thermal propagation lag/uncertainty.
- No independent measured matched charging energy or mobility mission requirement.

## Interface direction and mathematical thesis interpretation (AUTHOR'S findings vs candidate model)

Published physical-and-informational architecture:
`P transformer currents/load measurements → TLM/ICT Zigbee message → EVSE IEC61851 pilot PWM limit → allowed charging current`.
This is **P-load-conditioned T charging-current actuation** via an information interface, with *control capable* of electrical load feedback, but **not** a directly temperature-triggered test. Separately, TLM records transformer oil and ambient temperature. Shared equipment does not prove thermal cause of its charging-controller messages.

Thesis-only candidate (NOT in Kunlasing Eq. 1):
`u_EVSE(t) <= u_max(s_P(t), I(t), O(t))`
where `s_P` is transformer electrical loading; a temperature-conditioned extension `u_max(T_oil(t), T_hotspot_hat(t), ...)` would be a **new hypothesis/implementation**, not a validated result from this paper. Because Gong (2015) and RACE (2025) already represent thermal-aware load allocation, novelty cannot be declared merely from adding a hypothetical oil-temperature rule.

## Evidence verdict

**Source type:** Original IEEE 2022 conference article **verified**.
**Strongly verified:** Practical P metering with oil/ambient temperature monitoring; IEC 61851/Zigbee charger control-pilot response to manual commands on two chargers.
**Scenario only:** Automated multiple-EV overload reduction performance in three-EV simulation.
**Not validated:** Thermal-state-conditioned automatic utility-to-charger control, directional P-to-T thermal receiving causality, actual on-site transformer temperature improvements due to automatic EV reduction, or coupled field thermal viability.
**Next:** Focus follow-up search on legitimate automatically commissioned P oil/hotspot threshold-command-action logs and time-synchronized measured EVSE AC/DC and transformer thermal response. Krama raw thermal/charger data requested by user but not received. Do not characterize missing novel physics as established.

### Source audit notes
- Original conference DOI printed PDF p.1 and genuine ASU watermark.
- Paper layout/images inspected: Fig. 8 source is temperature + load illustration; Fig. 12 different PWM charging limits; Fig. 13 is explicitly **simulation**.
- No raw experimental data, full model calibration/uncertainty tables, or separate independent validation statistics supplied.
