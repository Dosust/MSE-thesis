# SO1–SO3 scientific literature synthesis — evidence-bounded v1.0

**Date:** 3 November 2026. **Stage:** PRIOR-ART SYNTHESIS OF VERIFIED/PARTIAL COMPETITORS, NOT FINAL SYSTEMATIC REVIEW.  
**Scope authority:** [frozen canonical SO1–SO3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md).  
**Data foundation:** [533-record reconciled register](./MASTER_SYSTEMATIC_LITERATURE_REGISTER_V01.csv), [784-row source crosswalk](./HISTORICAL_BIBLIOGRAPHY_PROVENANCE_CROSSWALK_V01.csv), [claim-level pilot matrix](./FULLTEXT_MATHEMATICAL_EVIDENCE_MATRIX_V01.csv). Do not count 533 as systematically included studies.

## SO1 — Physical thermal states and directional physical interfaces

**Established by source-specific prior art, within studied conditions:**
- IEC 60076-7:2018 specifies oil/winding thermally relevant state modeling, loading guides and aging interpretation for mineral-oil-immersed transformers. A guide is not itself a measured site-specific protection-trip policy: https://webstore.iec.ch/en/publication/34351 .
- Hilshey et al. 2013 DOI [10.1109/TSG.2012.2217385](https://doi.org/10.1109/TSG.2012.2217385) and Gong et al. 2015 DOI [10.1109/TSG.2014.2365452](https://doi.org/10.1109/TSG.2014.2365452) address EV charging schedules, transformer thermal consequences/aging and transformer experiment in case-specific designs. No claim of first-ever transformer-aware charging is available.
- Krama et al. 2026 DOI [10.1016/j.ecmx.2026.101960](https://doi.org/10.1016/j.ecmx.2026.101960) report real 50-kW EVSE derating under Qatar desert heat with ambient/rectifier/power/efficiency/THD/charging-time observations, evaluated data-driven predictor. Do **not** claim charger heat derating or its charging-time consequence is newly discovered here.
- Li, Chang & Lu 2026 DOI [10.1109/PESGM58988.2026.11693150](https://doi.org/10.1109/PESGM58988.2026.11693150) report primary/secondary electrical metering for a 2000-kVA bus-depot transformer. Actual oil/winding and EVSE-internal thermal sensors and their coincident service outcomes are **not yet verified** from currently accessible original report metadata.

**Precise open SO1 interface:** \`P→T_e\` requires real thermal state \`T_P\` → explicitly implemented state-dependent allowed power or protective action \`C_P\` → measured EVSE AC supply and delivered charging. \`T_e→P\` requires real EVSE/battery heat and controller derating → measured AC load \`P_AC\` → mapped feeder/transformer current → evolving transformer heat. Co-occurring high ambient \`T_a\` on both components is a **common cause**, not proof of cross-system feedback. Both directional chains should remain \`CANDIDATE/OPEN\` without a valid observation operator and same-site instrumentation.

## SO2 — Valid governing mathematical and physical dynamics

A **candidate, dimensionally audited first-law structure**, not a validated site-specific model:
\[
C_P(\theta_P)\dot T_P=P_{\mathrm{loss},P}(I_P,T_P;\theta_P)-\dot Q_{\mathrm{rej},P}(T_P,T_a;\theta_P).
\]
\[
C_C(\theta_C)\dot T_C=P_{\mathrm{diss},C}(P_{AC},P_{DC},u,T_C;\theta_C)-\dot Q_{\mathrm{rej},C}(T_C,T_a;\theta_C).
\]
\[
P_{AC}=P_{DC}+P_{\mathrm{conv,loss}}+P_{\mathrm{aux}}
\]
under a **defined AC/DC/auxiliary metering boundary** and with no unaccounted storage. The AC–DC difference is **not automatically heat rejected** by EVSE.

Battery internal \(R_{\mathrm{int}}I^2\) loss and coolant exchange are already parameterized in Acker et al. 2025 online/2026 vol DOI [10.1007/s41104-025-00157-7](https://doi.org/10.1007/s41104-025-00157-7), using real Audi e-tron vehicle/bench measurements; their improved NMPC charging/auxiliary outcome was evaluated **using simulation**.

Bragone et al. 2022 DOI [10.1016/j.epsr.2022.108447](https://doi.org/10.1016/j.epsr.2022.108447) already used real transformer field ambient/load/top-oil measurements with a 1D heat PDE and PINN versus finite-volume method (FVM). The spatial temperature is **predicted**, not fully observed in the whole transformer; observed top-oil also provides a boundary. A transformer thermal PINN alone therefore is not new, and the benchmark reported no PINN superiority over FVM under that setup.

Cao et al. 2026 DOI [10.1016/j.applthermaleng.2026.130776](https://doi.org/10.1016/j.applthermaleng.2026.130776) already use a physics-informed **neural Transformer sequence model** on EV thermal management under extreme temperatures. It is not a power transformer study. Likewise, [Pan et al. 2025](https://doi.org/10.1049/hve2.70024) already combine dynamic thermal ratings of transformers/cables with active EV response in **distribution planning models**.

**Our component evidence:** SINTEF 8592 original hourly transformer measurements give an exploratory same-site thermal predictor, but ambient max **25.97°C** and physical heat capacities/loss terms are not identified; no hot-climate transfer. TUM battery/vehicle thermal series are not admitted until sentinel and charging-state temporal QA. The sought physical law/operating site, data observability and multi-rate coupling remain open. Avoid source parameter transfer between different hardware.

## SO3 — Critical time, resilience and service consequences

Do **not** conflate three different quantities:
\[
\tau_{\mathrm{th}} \quad\text{(component heat response)}, \qquad
\delta_{\mathrm{interface}} \quad\text{(cross-interface event lag)},\qquad
\tau_{\mathrm{service}} \quad\text{(missed service/threshold onset)}.
\]

The RACE for 2030 2025 transformer study [project and final report](https://www.racefor2030.com.au/project/taking-the-heat-out-of-electric-vehicle-charging/) developed temperature-conditional transformer EV charge service simulation with heat-run context. Modeled charging-energy shortfalls/relative aging **are not** observed vehicle missed departures or observed physical transformer aging.

Krama measured charger heat-related session duration increase, already a direct EVSE-to-vehicle performance prior. The strongest new thesis question would be **actual directional transformer↔EVSE thermal state coupling and dated electricity/mobility requirement consequences**, if the literature counterexample search and available data justify it.

No qualified field source currently establishes measured bidirectional heat-feedback propagation and observed mobility-service recovery for a physically instrumented linked transformer/charger/fleet. This is an **evidence gap in the current corpus**, **not proof of global novelty**.

## Confirmed limitations and interpretation

1. **F1/F2 field connected status is claim-specific.** A station can be physically connected with primary/secondary electrical metering yet lack thermal feedback evidence.
2. **F5 measured-driven simulation** must identify actually measured inputs/outputs; modeled internal spatial fields are not field-validated internal temperatures.
3. **F6 simulated improvement** is valid only within assumptions and benchmark conditions. No causal event-time or field mobility claim is transferred automatically.
4. A source's reported weather temperature may be broader than the user's experiment's **coincident measured charging and internal thermal observations**.
5. PRISMA-ScR and final novelty closure remain blocked until the locked systematic queries, complete screening, full texts, critical appraisal, counterexample chase and manual study-family resolution are executed.

**Next scientific source tasks:** examine full Krama and Li apparatus/equations; verify RACE Part-2 field outcomes; complete transformer heat model standards applicability; test actual thermal-response/charging-service observability and parameter identifiability; then write formally selected-literature synthesis, not before.
