# KIT EV-point matched quiet-window comparison (derived 1-second means)

**Status:** observed descriptive comparison; NOT evidence of causal voltage-induced change.
**Source:** https://doi.org/10.5281/zenodo.22826984
**Matching:** same source phase, same UTC date and similar pre-event EV load / 20kV voltage; no one-second voltage steps ≥0.15% anywhere from −20 to +30 seconds around the control.
**Consistency:** case metrics recalculated on SAME 1-second grid as controls; original 100-ms M2/M3 metrics remain separately preserved.

| Case UTC | Case ΔP (W) | Case ΔU20 (%) | Clean controls (n) | Control median ΔP (W) | Case minus control median (W) |
|---|---:|---:|---:|---:|---:|
| 2026-03-10T15:32:02+00:00 | -422.088 | +0.711 | 4 | +0.067 | -422.155 |

## Event 2026-03-10T15:32:02+00:00
- Phase: fault
- Availability/rejections: {"candidate_strided_same_day": 17270, "after_event_exclusion": 17126, "quiet_voltage_windows": 4310, "all_signals_finite_windows": 4310, "same_source_fault_phase": 4310, "load_and_voltage_matched": 55, "pre_power_stable": 52, "selected": 4, "matched_case_fault_phase": "fault", "matched_case_date_utc": "2026-03-10"}
- Status: **DESCRIPTIVE_WITHIN_PHASE_AND_DATE_COMPARISON_ONLY**

| 2026-03-10T15:55:02+00:00 | +407.733 | -0.714 | 0 | n/a | n/a |

## Event 2026-03-10T15:55:02+00:00
- Phase: fault
- Availability/rejections: {"candidate_strided_same_day": 17270, "after_event_exclusion": 17126, "quiet_voltage_windows": 4310, "all_signals_finite_windows": 4310, "same_source_fault_phase": 4310, "load_and_voltage_matched": 0, "pre_power_stable": 0, "selected": 0, "matched_case_fault_phase": "fault", "matched_case_date_utc": "2026-03-10"}
- Status: **NO_CLEAN_MATCHED_CONTROLS_AVAILABLE**

**Scientific limit:** Co-variation is not physical feeder verification or an identified voltage effect. This dataset lacks verified EVSE commands/charge status and thermal/service measurements.
**Decision:** if clean matches do not exist during the OLTC recurring-steps episode, report the absence rather than relax criteria after seeing outcomes. A separate controlled PHIL dataset can test voltage-driven device behavior, but cannot be merged as same feeder.
