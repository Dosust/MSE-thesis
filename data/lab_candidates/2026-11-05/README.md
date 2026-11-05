# Independent EV charging laboratory evidence — 2026-11-05

**Separate evidence stream** from measured KIT 50-day campus OLTC field records and the thesis field candidate directory.

- [Three-source independently controlled EV electrical/charger-state mechanism evidence protocol](INDEPENDENT_EV_LAB_MECHANISM_EVIDENCE_PROTOCOL_V1.md): KIT PHIL 20 ms voltage/current (controlled voltage), TU Dortmund charger status/setpoints (controlled charger power), and Li et al. controlled PQ disturbances with CAN battery charging state. Defines mechanism claims and limitations.
- [Verified script for five KIT PHIL CSVs + Dortmund metadata](../../../tools/independent_ev_lab_voltage_control_audit.py): publisher MD5, source schema checks, controlled-voltage/current response screening, apparent-power-proxy constraint, and separate charger command/state metadata inventory. The synthetic self-test passed; the complete **real measured five-vehicle and Dortmund metadata audit requires local execution**.

**Lab input originals** remain in local Downloads, not in GitHub. The script writes small, reproducible measured outcomes to this directory as `INDEPENDENT_EV_LAB_M2_M3_ELECTRICAL_AUDIT_V1.{json,md}`.

**No source merging:** These lab experiments are not synchronized with, nor identical in equipment to, the original KIT 100 ms 50-day OLTC field time-series and cannot attribute the original two March 10 power-state changes to a particular control/voltage mechanism.
- [Measured KIT PHIL laboratory evidence decision](INDEPENDENT_EV_PHIL_RESULTS_EVIDENCE_DECISION_2026-11-05.md): 64 detected 2 V voltage transitions across four vehicles, small phase-current changes, Nissan Leaf 0 requiring detection-sensitivity QA, separate Dortmund charger-state metadata evidence.

- [KIT PHIL voltage-screen diagnostic script](../../../tools/independent_ev_phil_voltage_screen_diagnostics.py): examine source-verified five-vehicle full-run voltage ranges and 0.5–5 V detector sensitivity from cached original CSVs, without treating zero selected events as no physical disturbance.

- [Phase-aware KIT PHIL V2 source-qualified reanalysis](../../../tools/independent_ev_phil_phase_aware_audit_v2.py): fixes the Nissan Leaf single-energized-phase voltage averaging artifact; preserves V1 as provenance, reconstructs eligible measured events from active phase(s) only, outputs separately versioned V2 JSON/Markdown. Synthetic self-test PASS; actual measured V2 run pending Mac execution.
