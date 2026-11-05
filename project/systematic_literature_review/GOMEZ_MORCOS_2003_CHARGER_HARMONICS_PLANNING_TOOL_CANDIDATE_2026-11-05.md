# Gómez & Morcos (2003): Distribution planning tool based on charger harmonics and transformer aging
**Date:** 2026-11-05
**Status:** Source-abstract-supported conceptual extraction; original full equations/software and independent validation NOT audited; formal dual-human screening PENDING.
**Article:** Gómez, J. C. & Morcos, M. M. (2003). *Impact of EV battery chargers on the power quality of distribution systems*. IEEE Transactions on Power Delivery 18(3), 975–981. DOI https://doi.org/10.1109/TPWRD.2003.813873.
**Crucial attribution:** User quoted passage about a program that predicts transformer life consumption as function of charger characteristics and charging algorithm is from **Gómez & Morcos (2003)**, **not** Qian et al. (2015), DOI 10.1016/j.ijepes.2014.09.040. Preserve them as separate historical prior art.

## Explicit source claims (abstract-level)
The authors model EV charger harmonic effects, with special attention to distribution transformers. A developed **computational program** assesses transformer life consumption depending on charger design and charging algorithm, presented as a planning and management tool; the method can support decisions about charging time under existing grid load, ambient temperature and time of day. The reported calculations include a **quadratic association** between modeled transformer life consumption and charger-current THD within studied cases. Their cited 25–30% current THD suggestion is a source-specific finding, **not** a universally applicable current standard, safety threshold, or thesis assumption. The abstract does **not** itself document accessible software or a physically tested real-time controller.

## Conceptual engineering role
**Inputs:** ambient air temperature, grid non-EV load, charger power/time behavior, charger input AC current waveform or harmonic spectrum, schedule/policy, transformer parameters.
**Physical chain:** charger harmonic currents + total fundamental load → harmonic-sensitive copper/eddy/stray losses → winding/top-oil heating → winding hot spot → equivalent thermal aging/life consumption → planning decision. This chain follows established electrical energy-loss principles; exact transformer eddy/stray equations, frequency-dependent resistance and method parameters must be verified in original full text before claiming paper-specific implementation.
**Output:** comparative modeled aging and potential schedule selection; physical aging estimates are model-derived, not direct proof of years of life lost.

## Provisional candidate extension of F1 (ours, not quoted from source)
Harmonic current THD:
\[
\mathrm{THD}_I=\frac{\sqrt{\sum_{h\ge2} I_{h,\mathrm{rms}}^2}}{I_{1,\mathrm{rms}}}.
\]
A generic harmonic-dependent loss representation is
\[
P_{loss}(t)=P_{core}(t)+\sum_{h\ge1}R_{ac,h}(T) I_{h,\mathrm{rms}}(t)^2+P_{other}(t),
\]
where `P_other` includes physically substantiated stray/eddy components and must avoid double-counting; actual loss models are equipment- and frequency-specific. The simplified `ΣR_h I_h²` is **not** asserted as the article's exact formula. Couple these losses to a qualified transformer thermal state model and HST-based aging integral for matched comparison with the no-harmonics baseline.
**Candidate controls:** Charging schedule, charger choice/mode and operating constraints, only when equipment/control flexibility and charging requirements can be justified.

## Candidate metrics and thesis objectives
- **SO1:** Transport-to-Power mechanism from charger electrical harmonics to transformer heating; physical P→T feedback is not directly demonstrated.
- **SO2:** THD_I [%], harmonic-sensitive losses [W], estimated HST [°C], equivalent life consumption [h], dynamic state time constants. Compare against first formulation F1 which accounts primarily for stochastic charging power timing and magnitude.
- **SO3:** Potentially quantify threshold crossing, allowable charging curtailment, energy deficit or delayed departures only through separately evidenced controls/service; cannot infer from Gómez paper's abstract alone.
- **Benchmarks:** Compare (i) loading-only thermal model; (ii) harmonic-aware physical model; (iii) conditional PINN method where harmonic-resolved current and measured HST channels are independently available; (iv) proposed coupled state-time response with transparently bounded assumptions.

## Limitations and gates
- Abstract/source bibliographic metadata validated via https://www.scinovex.com/articles/W2131730934 and https://jglobal.jst.go.jp/detail?JGLOBAL_ID=200902213945368441.
- Verify full original IEEE paper, equations, input waveform decomposition, actual software availability, temporal scale, transformers and empirical versus simulated thermal outcomes.
- Clarify source's quadratic THD-lifespan statement mathematically; aging is exponentially sensitive to HST, harmonic power loss scales with harmonic-current squares under qualified assumptions, but **global life consumption as a function of THD need not be universally quadratic**.
- Check modern standards and verified harmonics for the specific charger, equipment, network conditions; do not adopt 25–30% THD as a general pass/fail criterion.
- **Dataset limitation:** Existing qualified SINTEF hourly current/HST alone does not establish harmonic spectra or actual physical charger connectivity. No real-field harmonic-driven hotspot/EVSE interface validation may be claimed from this archive alone.
- Retain as **strong prior-art paper and provisional harmonic-aware model extension candidate**; not an automatic additional required scope or final metric. Need formal JBI review and scientific feasibility comparison.

**Sources:** https://doi.org/10.1109/TPWRD.2003.813873 ; Qian 2015 DOI https://doi.org/10.1016/j.ijepes.2014.09.040.
