# KIT M2/M3 original 100 ms event metrics — measured output

**Source:** https://doi.org/10.5281/zenodo.22826984
**Provenance:** Derived from previously extracted original 100 ms KIT CSV windows. Do not infer heat or causality.
**Definitions:** M2 local voltage median change: -3 to -0.5s versus +0.5 to +3s. M3 active-power pre baseline -5 to -0.5s, post settled-state +20 to +30s; sustained transition = >=100 W for >=3.0s uninterrupted. All windows relative to selected 20kV voltage-step time.

| Event UTC | M2 U20 delta % | M2 U400 delta % | U400/20 ratio | M2 Δt peak 400-20 (s) | P at t=0 (W) | M3 settled ΔP (W) | First sustained shift t (s) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-03-10T15:32:02+00:00 | +0.703 | +0.697 | +0.991 | +0.0 | +2038.45 | -422.24 | +11.1 |
| 2026-03-10T15:55:02+00:00 | -0.716 | -0.725 | +1.011 | +0.0 | +757.61 | +409.22 | +13.8 |

## Per-event checks

### 2026-03-10T15:32:02+00:00
- 20/400V M2 voltage step signs agree: **True**; voltage relative timing is observational at 100ms precision.
- Earlier 20kV steps >=0.15% before selected event: **2**; see JSON for offsets.
- Event-time EV power: **+2038.45 W**; pre baseline +2039.14 W; settled post +1616.90 W.
- Pre-window power 1.4826×MAD **+0.74 W**, maximum absolute deviation **+1.53 W**.
- Largest raw prior 100ms ΔP: **+4.63 W** at t=-16.0 s; largest at/after ΔP: **-243.55 W** at t=9.8 s.
- Sensitivity (change-point onset at thresholds/dwell): 100W/2s -> 11.1s, 100W/3s -> 11.1s, 150W/3s -> 11.1s, 200W/3s -> 11.1s, 300W/3s -> 14.4s

### 2026-03-10T15:55:02+00:00
- 20/400V M2 voltage step signs agree: **True**; voltage relative timing is observational at 100ms precision.
- Earlier 20kV steps >=0.15% before selected event: **0**; see JSON for offsets.
- Event-time EV power: **+757.61 W**; pre baseline +766.77 W; settled post +1176.00 W.
- Pre-window power 1.4826×MAD **+14.18 W**, maximum absolute deviation **+34.07 W**.
- Largest raw prior 100ms ΔP: **+25.40 W** at t=-18.6 s; largest at/after ΔP: **+229.37 W** at t=8.3 s.
- Sensitivity (change-point onset at thresholds/dwell): 100W/2s -> 13.8s, 100W/3s -> 13.8s, 150W/3s -> 13.8s, 200W/3s -> 13.8s, 300W/3s -> 13.9s

## Scientific evidence decision

**M2: OBSERVED synchronized electrical cross-voltage co-response.** Measured relative voltage changes at 20kV and the EV-meter 400V level; ratio and timing are *descriptive*, not a verified transfer factor or feeder cause.

**M3: OBSERVED subsequent EV-meter electrical power-state transitions.** Changes in independently metered EV-point power must be distinguished from battery charging status and controller commands. A stable pre-window and later transition cannot demonstrate voltage-induced operational dependence by themselves.

**Operational P↔T interdependency: NOT VERIFIED from this pair alone.** Specific feeder parentage, alternative controller states / matched controls, and corroborating mechanism remain missing. **Thermal and mobility-service metrics: NOT MEASURED.**

**Data note:** Two events selected within the same labeled fault period are not independent trials. Local noise, thresholds and baseline/window choices are exploratory; evaluate sensitivity before inferential claims.
