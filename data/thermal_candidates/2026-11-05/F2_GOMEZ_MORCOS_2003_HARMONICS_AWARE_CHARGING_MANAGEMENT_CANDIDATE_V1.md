# F2 — Gómez & Morcos (2003): harmonic-aware transformer thermal ageing and charging-time planning

**Status (2026-11-05): SOURCE-VERIFIED CANDIDATE METHOD; abstract-level methodological qualification, NOT original-algorithm reproduction, full-text audit, measured harmonic result, adopted model, proved novelty, or supervisor-approved scope change.**
**Current official title:** Engineering of Power–Electrified Transportation Interdependencies for Resilience (canonical V3). Frozen SO1–SO3 unchanged.

## Source identification — NOT Qian et al. (2015)

Gómez, J. C., and Morcos, M. M. (2003), *Impact of EV battery chargers on the power quality of distribution systems*, IEEE Transactions on Power Delivery 18(3):975–981, DOI https://doi.org/10.1109/TPWRD.2003.813873.

Public abstract describes: (1) EV battery charger harmonics and distribution-transformer effects; (2) computer program estimating transformer life consumption as a function of charger characteristics and charging algorithm; (3) distribution planning/management use and possible optimum charging-time selection as a function of existing load, ambient and time of day; (4) substantial modeled harm from connect-and-charge at high load/ambient conditions; (5) modeled quadratic relationship between transformer life consumption and charger current THD under the authors' scenarios, and a paper-specific **25–30% current THD recommendation**.

**Crucial interpretation:** The quoted optimum-time statement is a proposed APPLICATION of the paper's planning tool. The public abstract does not establish that the authors solved, proved globally optimal, or field-validated a general thermal ageing + mobility-service constrained optimization. Their 25–30% current THD threshold and apparent quadratic relation are **case/model-specific** findings, NOT universally applicable IEEE allowable limits or verified laws for current EV chargers or any transformer.

**Independent standards prior art:** IEEE C57.110-2018, https://standards.ieee.org/ieee/C57.110/5948/, prescribes ways of evaluating capability of qualifying distribution/power transformers supplying nonsinusoidal load currents. The transformer type, current spectrum, allowable loss and cooling/rating must be qualified before harmonics loss modeling.

## How F2 differs from F1

| Dimension | F1: Qian, Zhou and Yuan 2015 | F2: Gómez and Morcos 2003 |
|---|---|---|
| Main modeled driver | Stochastic EV arrival/start, initial SOC, modes and penetration | Charger current waveform/harmonic distortion, charging algorithm, time and base load |
| Transformer input | Total EV electrical loading and ambient | Total loading PLUS the frequency composition of non-sinusoidal charger current |
| Thermal consequence | Hot-spot T_H and insulation equivalent ageing | Harmonics-sensitive heating/life consumption |
| Charging-time use | Scenario planning, scheduling sensitivity with stochastic sessions | Distribution planning tool to evaluate/choose charging times conditional on ambient, load and waveform |
| Validation need | HST+current+linked charging sessions | HST+current plus synchronized **high-rate phase current waveform / harmonic spectrum** and asset-specific loss model |

**The methods are complementary, not separate novelty claims.** F1 yields stochastic demand/time trajectories; F2 adds a candidate electrical-loss correction for nonsinusoidal current where instrumented data and physics justify it. Both inform, but do not by themselves establish, a physical Power→Transportation charger constraint.

## Candidate physics integration — our own conceptual equations, not copied from paper

1. EV sessions (scenario omega): P_EV(t,omega)=sum_i p_i(t; start_i,SOC_i,mode_i,control_i,omega), allocated to a **verified parent transformer**.
2. Phase-resolved electrical interface: I_{phi,h}(t) denotes **measured or electrically simulated RMS current at harmonic order h for phase phi**; I_{phi,rms}^2=sum_h I_{phi,h}^2 when harmonics are orthogonal over the declared window.
3. Illustrative aggregate loss decomposition: P_loss(t)=P_core(t)+sum_phi R_phi I_{phi,rms}(t)^2 + sum_{phi,h>=2} K_{phi,h} I_{phi,h}(t)^2 + P_other_stray(t). Coefficients K_{phi,h} must represent additional frequency-dependent eddy/stray heating *beyond* copper RMS loss to avoid double counting. Detailed harmonics loss models should follow applicable transformer standard and actual winding/test evidence; this is not the published Gómez–Morcos equation.
4. Thermodynamics: dot(x_th)=f_th(x_th,P_loss,T_ambient,cooling,theta), T_H=g_th(x_th). Calibrate physical state against independently measured HV/LV hot-spot channels.
5. Reference-equivalent ageing: L_eq=int F_AA[T_H(t)] dt under qualified insulation type/standard/time units. This is a model-derived deterioration proxy, not observed loss of years or field failure probability.
6. Coupled feedback (if qualified): thermal/ageing admissibility constrains EV delivered power P_EV,allow^thermal(t;H) and departure energy, generating P→T service effects. Thermal feedback claims must not be substituted by a mere scalar aggregate ageing score.

**Caution:** Current THD = sqrt(sum_{h>=2} I_h^2) / I_1 (if I_1>0). THD alone discards spectral order, phase imbalance and frequency-dependent winding losses. Equal THD can lead to different detailed transformer heating. Do not infer heat only from aggregate THD without qualifying equipment, harmonics, frequency content and phase connection.

## Candidate experiments

| Design | Pair or variation | Testable metric |
|---|---|---|
| F2-E1 conventional thermal baseline | Sinusoidal/fundamental or appropriately calibrated RMS model vs spectrum-aware losses under **same** ambient and physically consistent phase loading | Delta T_H [degC], loss [W], difference in ageing-equivalent hours |
| F2-E2 charger waveform | Compare qualified observed/reproducible harmonic spectra at compatible delivered energy and relevant fundamental/RMS currents | Harmonic eddy/stray loss and calibrated HST effect |
| F2-E3 charging-time decision | Move comparable EV energy requests among slots while tracking actual/non-EV load, ambient and initial thermal state | Peak HST, equivalent ageing, critical-limit time, energy requested/delivered |
| F2-E4 combined adverse condition | Sensitivity to heatwave, EV penetration/start-time distribution and harmonic spectrum with documented uncertainty | Conditional risk and interaction; no assumed universal ranking or 25–30% limit |

## Actual available-data and admission gate

- The prior KIT PHIL phase-aware files contain ~21 ms samples of **phase RMS voltage and RMS current**, which are **not** sufficiently sampled instantaneous waveforms for spectral current-harmonic estimation. The phase-aware U/I steps and apparent power proxy VA cannot yield EV charger current THD or true power-factor correction.
- The KIT OLTC field 100 ms electrical series and SINTEF transformer thermal HST record must not be presumed to contain phase-resolved high-frequency harmonic spectra. SINTEF qualifies measured HST component validation, not this separate EV charging harmonic source.
- **Required for empirical F2-E2:** synchronized high-bandwidth raw phase currents or validated harmonic-order spectra, transformer measured HST/temperature and loading, verified transformer–charger connection, instrument/time-resolution metadata, and known charger operating modes. Without these, harmonic-aware tests must be **physics-based synthetic scenarios** and cannot validate actual charger harmonic damage.
- Full Gómez and Morcos text, exact implementation, original loss formula and optimizer must be obtained/verified before reproducibility or originality assertions.
- Scope gate: harmonic effects are admitted solely as supporting **electrical loss/thermal forcing** on a qualified thermal mechanism, not a standalone broad power-quality thesis objective.

## F1–F2 hierarchy and final decision

F1 stochastic charging/time model (Qian 2015) → optionally F2 current harmonic/loss correction (Gómez–Morcos 2003 + IEEE C57.110-2018) → equipment-validated transformer winding/oil temperature → equivalent insulation ageing → thermal headroom/criticality → qualified charging restriction and energy/mobility-service consequence.

**Decision:** F2_ADDITIONAL_COMPLEMENTARY_PLANNING_METHOD_CANDIDATE | HARMONIC_SPECTRUM_DATA_NOT_YET_AVAILABLE | ORIGINAL_METHOD_REPRODUCTION_PENDING | NO_25_30_PERCENT_GENERIC_LIMIT | SO1_SO3_UNCHANGED
