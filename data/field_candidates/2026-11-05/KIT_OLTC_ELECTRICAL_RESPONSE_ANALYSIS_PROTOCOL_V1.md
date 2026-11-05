# KIT OLTC synchronized electrical-response analysis: protocol V1

**Date:** 2026-11-05  
**Active thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.  
**Original source:** KIT Campus North multivoltage OLTC dataset, Moster et al. (2026), DOI https://doi.org/10.5281/zenodo.22826984.  
**Status:** PYTHON ANALYSIS CODE PREPARED; MEASURED RESULTS NOT YET EXECUTED ON USER MAC.  
**Input evidence:** [KIT acquisition audit](KIT_OLTC_22826984_ACQUISITION_AUDIT.md), [campus topology and scope decision](KIT_OLTC_ELECTRICAL_TOPOLOGY_EVIDENCE_AUDIT.md).  

## 1. Already verified, avoid repeating

The user originally acquired three Parquet files under ~/Downloads/KIT_OLTC_22826984/:
- oltc_fail_110kV_PMU04_TK1_100ms.parquet;
- oltc_fail_20kV_PMU01_J01_100ms.parquet;
- oltc_fail_400V_EV_SH.J.6_100ms.parquet.

Each matched its original Zenodo MD5. Each has 43,200,000 source rows, 44 row groups, shared original period 2026-02-03 23:00 UTC through 2026-03-25 22:59:59.9 UTC. The user independently checked all **129,600,000 timestamps** against a strict 100 ms UTC grid with **zero mismatches**.

Both the source and KIT literature place the measurements in the same campus power system. Exact circuit ancestry PMU04_TK1 → PMU01_J01 → EV_SH.J.6 remains unverified, but the user explicitly directs continuing a **system-level synchronized electrical analysis** without obtaining feeder maps. Do not block that descriptive comparison.

## 2. The measured signals that support this analysis

| Source | Variables used | Unit and caution |
|---|---|---|
| 110 kV original | u_pos[V], p[MW], q[MVAr], f[Hz] | 110 kV positive-sequence voltage, active/reactive power and frequency at instrumented point |
| 20 kV original | u_pos[V], i_pos[A] | 20 kV positive-sequence voltage and current; **no measured active-power field at 20 kV** |
| 400 V EV original | u_L1[V], u_L2[V], u_L3[V] | Three individual voltage measurements, phase convention unqualified |
| 400 V EV original | p_L1[W], p_L2[W], p_L3[W] | Measured per-phase real powers; sum only with all three valid. Sign convention unqualified |
| All three | time[UTC], fault_phase | Original time grid verified; source phase annotations require source semantics |

**Thermal data missing:** no ambient, transformer winding/oil or EVSE internal temperature, cooling state, charger thermal limit, battery SOC or trip/service requirement in these three original schemas. This dataset alone cannot validate heat-induced thermal interdependency.

## 3. Exact scientific questions

E1. During candidate 20 kV voltage steps, what are the same-time normalized relative changes at 110 kV, 20 kV and 400 V EV measurement points?

E2. During those candidate events, what is the change in EV point three-phase **measured active power** (sum of valid phase powers)? If sign remains unqualified, refer to absolute electrical exchange rather than definite charge/draw.

E3. What are the corresponding measured 20 kV current and upstream 110 kV real-power variations? Neither is a measurement of the other point's missing active power.

E4. Which source annotation labels are present, before and during candidate disturbances? Do not equate annotations with independently verified tap-position telemetry.

## 4. Reproducible preparation

The full Python program delivered as an attachment in the 2026-11-05 ChatGPT conversation is named **kit_oltc_electrical_response_analysis.py**. Its SHA-256 at creation was:

~~~text
d9b526b04b15c514e9d36014e4d1526efe95c535a0a410cdce695806f3c30df9
~~~

**IMPORTANT:** The original large Parquet files and this executable file have not been uploaded to GitHub. This repository document records the program's specifications and execution instructions; it does not claim GitHub contains those bytes. The generated Python code passed syntax compilation and pure-function synthetic self-tests in the assistant environment, **not** a raw-KIT measurement run.

The program streams original Parquet 100 ms samples in PyArrow batches, creates one-second finite-only arithmetic means per 10 samples, retains first-of-second source fault annotation, preserves original raw bytes, and writes 4,320,000 one-second bins per file. This 1 s aggregation loses sub-second timing resolution; **do not use it to claim precise 100 ms propagation delays**.

Derived features:
- EV three-phase active power: sum of three phase measured powers in W, only when all three means are finite.
- EV voltage summary: arithmetic mean of three measured phase voltages, only when all three means are finite; **not a phasor or nominal line-to-line conversion**.
- Independently normalized voltage change for each level: 100 × (post-event voltage / its own pre-event median − 1), if denominator is valid positive.

## 5. Exploratory event selection and reporting

Event trigger is absolute one-second relative step in measured 20-kV positive-sequence voltage. The source documents a real OLTC voltage-regulation anomaly, but **0.15%** is a working candidate-search threshold, **not** an established equipment or thermal limit.

Default options:
- voltage-step screening threshold: 0.15% (user-adjustable);
- minimum spacing between selected events: 45 seconds;
- maximum 60 strongest event candidates;
- pre-event median window: event−20 through event−6 s;
- post-event median window: event+5 through event+19 s;
- significant EV active-power exchange flag: |P_EV_pre| ≥ 500 W (working descriptive threshold, not confirmed charging).

For each selected event, report UTC, fault_phase annotation, local 20 kV step, separate percent voltage responses at 110/20/400 V, EV pre/post/delta active power kW, 20 kV current change A, and 110 kV P change MW. Do not report causal effect solely from correlated changes. Do not force output when no candidates pass the sensitivity threshold.

Requested figures:
- 50-day hourly median voltage relative to each signal's own median plus EV terminal real power (not temperature).
- ±30-second aligned event figure comparing normalized voltages and measured EV power for the largest selected 20-kV event.

## 6. Mac execution, once script is saved in Downloads

~~~bash
python3 -m pip install numpy pyarrow matplotlib

python3 "$HOME/Downloads/kit_oltc_electrical_response_analysis.py" --self-test

python3 "$HOME/Downloads/kit_oltc_electrical_response_analysis.py" \
  --folder "$HOME/Downloads/KIT_OLTC_22826984" \
  --out "$HOME/Downloads/KIT_OLTC_Electrical_Results" \
  --step-threshold-pct 0.15 \
  --max-events 60
~~~

The script creates in the output directory:
- grid110_1s.parquet, grid20_1s.parquet and ev400_1s.parquet (derived);
- event_metrics.csv;
- analysis_summary.json;
- 01_voltage_power_50days.png;
- 02_largest_event_comparison.png only when an event candidate exists.

Rerunning with a changed event-screening threshold may use --reuse-summaries **only with the same unchanged original data**.

## 7. Results that can and cannot be claimed

**When actual Mac execution succeeds:** report descriptive, synchronized electrical response and measured EV-terminal active-power changes during source-associated voltage perturbations, conditional on field QA, source labels, sign conventions and exact sampling/selection rules.

**Do not claim:** that the specific 110 kV PMU is the EV's unique physical parent, that observed correlations demonstrate directional power-flow causality, that the source anomaly is an extreme-heat disturbance, or that the dataset empirically validates EVSE thermal derating, thermal propagation or actual mobility-service resilience.

The official thermal-only research scope remains controlled by [scope V4](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md) and [SO1–SO3](../../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md); the [non-invention standard](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md) applies.

## 8. Next evidence handoff

Run the full script using the acquired originals. Share **analysis_summary.json, event_metrics.csv and the two PNG figures**. Then verify source fault_phase semantics and measurement sign/phase conventions before reporting quantitative findings. **No measured numerical analysis outcome has been fabricated or declared complete in this pre-execution note.**
