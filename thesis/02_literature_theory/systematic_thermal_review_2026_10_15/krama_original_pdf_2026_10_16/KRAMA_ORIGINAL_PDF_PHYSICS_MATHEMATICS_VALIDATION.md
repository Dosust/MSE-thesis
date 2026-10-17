# Original Elsevier article: Krama et al. (2026) — full-text physics, equations and evidence audit

**Source:** A. Krama, N. Kamal, N. Sezer, S. Bayhan. *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*, Energy Conversion and Management: X 31 (2026) 101960. DOI https://doi.org/10.1016/j.ecmx.2026.101960. **Original Elsevier 16-page publisher PDF supplied by user**, visually checked pp.3,5,13 and text-reviewed throughout. CC BY 4.0.
**File:** `1-s2.0-S2590174526004435-main.pdf`, 10,618,002 bytes, SHA-256 `150224c92e07afef9d9685aa2e964b5aaa1d8502a99974e3038e049f469d9a72`. The full copyrighted PDF is not reproduced in this GitHub branch.

## Equipment and physics boundary (SO1)

One **50-kW air-cooled DC EV charger**, 400-V three-phase AC inlet, CCS2, Aiways U5 EV, Qatar 2024–25 sessions across approx. 15–55 °C ambient (pp.4–5). The measured physical heat mechanism is **ambient heat → charger rectifier thermal stress → heat-conditioned charger offered DC power, delivered DC charging, session time and AC-side harmonic changes**. This demonstrates Tₑ component thermal behavior, NOT a same-site thermally coupled Power (P) distribution transformer.

**Critical boundary observation:** The instrument labeled **“Transformer” in Fig. 4 (p.6) is *inside the EVSE enclosure* (Tₑ)**, not the external utility P transformer. AC power/harmonics at the charger's upstream terminal do not measure external P transformer hotspot, thermal loss or actual utility thermal dispatch. This original paper does not independently demonstrate P→Tₑ or Tₑ→P field thermal *receiving-side* causality.

## Observations and measurement quality (pp.4–6, Tables 2–3)

- **Rectifier temperature:** mean of wireless sensors 1,2,3,7 affixed to rectifier modules; this is **not measured semiconductor junction temperature**. **5-minute** samples, individual sensor ±1°C.
- **Ambient:** sensors 9,10 externally shaded, averaged; **5-minute** samples, ±1°C.
- **Electrical:** PQ3198 Class-A AC grid-side power quality/analyzer at EVSE inlet, 3-phase RMS V/I, current THD up to 50th harmonic and PCC voltage THD; **1-minute** samples, instrument V ±0.1%, I ±0.2%; Hall AC probe ±0.5%, DC clamp ±0.3%.
- **DC and vehicle:** manufacturer/OCPP offered power, delivered DC power and SOC; **1-minute** stream. Authors timestamp-align AC/DC/thermal, claim clock mismatch less than one sampled interval.
- **Missing:** raw row-level field data; actual manufacturer limiter state/firmware thresholds; semiconductor junction temperature, semiconductor-only switching/conduction losses, measured heat flux/heat rejection; utility P transformer temperature/load attribution; scheduled mobility trip or departure obligation.

**Timing caution:** Measured rectifier temperature is sampled only every **5 min**, so one cannot infer one-minute-accurate thermal crossing or prove a sub-5-minute thermal propagation lag without additional evidence. Published 3–10 min derating onset is an authors' operational finding, not a measured 1-min thermal sensor event.

## Source physics and mathematics (original equation numbers/pages)

| Eq. | Original expression | Scientific meaning and evidentiary limit |
|---|---|---|
| (1), p3 | `T_j = T_c + Z_th P_loss` | Approximate semiconductor thermal impedance; **neither junction temperature nor Z_th measured**, and not a developed ODE/PDE |
| (2), p3 | `P_loss(t) = P_in,AC(t) - P_out,DC(t)` | Calculated **whole charger electrical conversion loss**, not measured semiconductor-only heat flux |
| (3),(4), p4 | `THD_X=100 sqrt(sum_{n>=2}X_n^2)/X_1` | Measured harmonic distortion ratio; ratio alone does not quantify extra upstream utility-transformer heating |
| (5), p5 | `eta(t)=P_out,DC(t)/P_in,AC(t)` | Time-aligned wall-to-DC conversion efficiency |
| (6), p11 | `G(t)=100[P_off(t)-P_del(t)]/P_off(t)` | Charger vs BMS diagnostic; only if `P_off>0`. Charger-limited rule: `P_off<P_rated`, `G<=5%`; battery-limited: `P_off=P_rated`, `G>=20%` |
| (7), p12 | `R2=1-SSE/SST` | Statistical predictive agreement, not physical conservation |
| (8), pp12–13 | `P_off=-0.0723 T_rect^2+5.1235 T_rect-36.6929` | Offered DC kW vs rectifier °C, fit `R2=.9625, MAE=1.772 kW` |
| (9), p13 | `P_off=-0.0514 T_amb^2+2.7961 T_amb+16.0253` | Ambient-only kW fit, `R2=.6865, MAE=5.367 kW`; markedly weaker |
| (10), p13 | `DeltaT=T_rect-T_amb` | Rectifier-above-ambient temperature rise. Paper calls this *headroom*; **not conventional thermal safety margin `T_max-T_rect`** |
| (11), p13 | `P_off=c1+c2 T_amb+c3 DeltaT+c4 T_amb^2+c5 DeltaT^2+c6 T_amb DeltaT` | Field-calibrated empirical polynomial, `c=(-35.9792,5.7939,4.4707,-.0849,-.0883,-.1363)`; `R2=.9852, MAE=.949 kW, RMSE=1.642 kW` |
| (12), p13 | `t_chg=.2533 T_amb^2-15.9486 T_amb+290.0163` | Session charging-duration minutes vs °C, `R2=.996, MAE=2.729 min`; **not independent trip/mobility service validation** |

The actual main modeling contribution is **field-calibrated, physics-motivated regression**, NOT a first-principles transient heat balance / PDE for rectifier temperature and NOT a PINN. The Eq. (1) impedance analogy supports interpretation of measured device temperature but has **no identified device `T_j` or heat-flow law**. Do not reuse empirical coefficients outside this charger class/temperature domain without physical and numerical limits.

## Main empirical results and holdouts (pp.9–15)

**Table 5 (p11):** severe 11 June 2024 mean ambient **53.5°C**, rectifier **55.9°C**, offered **20.7 kW**, delivered **20.1 kW**, charging **169 min**. Winter 9 January 2025 ambient **18.8°C**, rectifier **32.5°C**, offered **50.0 kW**, delivered **32.9 kW**, charging **86 min**. Summer was charger-limited, winter mainly battery-acceptance-limited. These are seasonal comparisons, not automatically identical trip obligations.

**Independent session holdout on offered power, Eq. (11):** leave-one-session-out June `R2=.416, MAE=5.41 kW, RMSE=6.23 kW`; August `R2=.983, MAE=.9 kW, RMSE=1.29 kW`; September `R2=.955, MAE=1.85 kW, RMSE=2.39 kW`. A strict temporal test trains on June/August and tests September: `R2=.955, MAE=1.847 kW, RMSE=2.39 kW` (p13, Fig9 p14). **Holdout is by sessions on same charger, not independent device/site; June generalization weaker.** The duration fit Eq. (12) reports accuracy without an unambiguous separate independent-duration test.

**Uncertainty and confounding:** ambient and rectifier each measured ±1°C (differenced values have nontrivial uncertainty); 5-min temperature alignment vs 1-min AC/DC; solar loading, dust, wind and humidity not independently measured or parameterized; no native manufacturer's limiter flag time series exposed. Elevated THDi at partial load does not prove measured transformer heat, and `P_in-P_out` is total system loss rather than separately measured device-generated heat.

## Research significance and next gate

**Already shown by this prior art:** actual hot-climate EVSE rectifier temperature, AC/DC power, measured thermal-power deterioration and cross-session validated empirical capability prediction. **Not shown:** independently observed upstream **P transformer** thermal receiving state, verified transformer heat-conditioned electrical restriction, connected thermal propagation lag, or actual electricity/mobility requirement failure/recovery.

**Data gap:** The original article p15 states **“Data will be made available on request.”** Original corresponding author email **akrama@hbku.edu.qa** is printed in PDF p1. The raw field dataset has **NOT BEEN PROVIDED OR DOWNLOADED**. Request original 5-min individual temperature channels, 1-min AC/DC offered/delivered, controls, SOC and THD, time zone/sync, uncertainty and full session holdout identifiers and data permission. Author contact request saved separately, **NOT SENT**.

**Methods:** Physics/heat-transfer mathematics stay foundational. With actual raw data test a dimensionally consistent RC/ODE baseline and this published regression on the same measured target/independent events; only evaluate PINNs if identifiable temperature states and robust real-data holdouts justify it. Without data, do not claim full observed P↔Tₑ thermal model validation.

**Publication status:** This source is a verified original 16-page publisher article; numerical raw data and P-side thermal field verification remain separate unsatisfied gates.
