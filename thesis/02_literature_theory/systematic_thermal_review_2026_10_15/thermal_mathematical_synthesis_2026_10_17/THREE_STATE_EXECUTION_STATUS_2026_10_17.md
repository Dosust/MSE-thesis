# Three-state research execution report — 17 October 2026

**Output:** [THREE_STATE_ELECTROTHERMAL_THEOREMS_V01.md](THREE_STATE_ELECTROTHERMAL_THEOREMS_V01.md) and [VERIFY_THREE_STATE_THEOREMS_V01.py](VERIFY_THREE_STATE_THEOREMS_V01.py). This is a *conditional theoretical model* with reproducible synthetic verification, NOT a calibrated/validated physically coupled P–T system or certified transformer/EVSE limits.

## Source evidence

- Gong 2015: original IEEE 9-page article verified, experimental transformer thermal component response (top-winding and top-oil, **not true hotspot**), programmed EV-like schedules rather than observed same-site real EVSE thermal response.
- Kunlasing 2022: original 4-page IEEE paper verified; field oil/PT100 load monitoring, two EVSE manual Zigbee/PWM command test, three-EV automatic loading **simulation**; monitored oil temperature **not an experimentally demonstrated charging control trigger**.
- Krama 2026: original 16-page publisher PDF verified; actual heat-conditioned EVSE offered power, rectifier proxy temperature and AC/DC observations, but no measured upstream distribution-transformer thermal receiving state. Underlying raw 5-min thermal/1-min AC/DC data unavailable.
- Susa 2005 paper original IEEE exact governing equations not checked; Aalto research metadata and abstract available, DOI 10.1109/TPWRD.2004.835255. IEEE **C57.91-2025** official status and IEC **60076-7:2018** official scope checked, not full standard equations. No attributed standard coefficient or thermal rating imported.

## User-required equation explanation standard

Every M, E, J, D, S, O, X formula in the main document includes surrounding definitions of variables/operators/indices/units, physical carrier, role, mathematical derivation, assumptions and limitations. A full first-use symbol register appears in §1 and local shorthand definitions in §§2–9. Effective winding state is not certified true hotspot; EVSE rectifier proxy is not semiconductor junction; temperatures K for SI, °C numerically only for differences/derivatives; actual delivered DC power vs offered/current limit distinguished.

## Seven investigation gates

| Gate | Result | Precise claim boundary |
|---|---|---|
| 1. Conservation and SI | **Mathematically checked**; transformer interior heat exchange cancels; secondary AC/DC accounting explicitly scoped | Simplified constant efficiency and balanced system; no harmonic AC field proof |
| 2. Equilibrium | **Existence and uniqueness proven** by monotone scalar fixed-point under nonincreasing smooth/continuous power limits | Only sufficiently demanded saturated-DC operation and constant ambients/loss coefficients |
| 3. Stability | **Local exponential stability proven in smooth neighborhoods of equilibrium** using actual 3×3 cubic Routh–Hurwitz positive coefficients and gap | Ties/nonsmooth relay logic/delays/battery taper, full grid DAE and nonlinear hardware physics unproven |
| 4. Extreme heat | For bounded exogenous ambients, globally bounded solutions established with Lipschitz power caps; equilibrium DC power monotone nonincreasing in either ambient | Do not assert transformer temperature monotonically increases under simultaneous thermal derating; forcing can be spatially distinct |
| 5. Thermal safety | Conservative state-wise upper-box forward invariance proved for bounded ambient/load (Nagumo/inward face) | These U bounds are mathematical enclosures, **not physical nameplate or junction/hotspot safety limits** |
| 6. Charging service | **Sufficient constructive certificate** for constant-command p_0 and deadline E_req<=p_0*t_d if both safety enclosure and worst-case caps admit p_0 | Strong assumptions about vehicle demand, BMS limits, command authority; not general resilience kernel |
| 7. VVUQ | Structural oil→winding observability identity (requires known coefficients/noiseless derivative); charger thermal scale nonidentifiability; original/data gate table | No original raw data, independent site calibration, matched P-Te receiver observations, or validated uncertainty distribution |

## Verification performed

1. **Mathematical / independent symbolic:** the 3-state Jacobian characteristic polynomial and its positivity identity were independently expanded using SymPy, and explicit inequalities for 3x3 Routh–Hurwitz were checked. Do **not** transfer the 2x2 determinant sign test to a 3x3 stable system.
2. **Independent local executable** (same formulas, differently structured standalone Python): 3 strict active-power modes, equilibrium bisection residual, finite-difference vs analytical J, all eigenvalues negative, cubic coefficients/inequality, AC/DC heat budget, transformer cancellation, ambient monotonicity, synthetic service enclosure under 2h constant control, 150 random joint smooth negative-feedback parameter pairs **PASS**.
3. **GitHub reproducibility script** committed under the above linked name, with equivalent tests plus RK4 refinement. **The exact GitHub-committed bytes have not been executed in GitHub CI**, so repository-CI signoff is a remaining gate.
4. The synthetic numerical parameters and thresholds **are arbitrary illustrative constants, not derived/calibrated from Gong, Kunlasing or Krama**. Resulting 3-state temperatures and power levels must never be reported as engineering predictions or manufacturer's limits.

## Explicitly blocked

- Original fulltext of Susa 2005 and exact permitted formulations of full IEEE C57.91-2025 and IEC 60076-7:2018.
- Original Krama field data and matched transformer-to-charger same-site observations, including upstream current, voltage, oil/winding sensors, charger AC/DC, firmware/control events, baseline other loads, and sensor clock offsets.
- Device-specific safe operating limits for equivalent thermal nodes, real mobility trip requirements and control authority.
- Matched experimental calibration, independent hardware/site verification, uncertainty coverage, and a globally defensible novelty claim.
- Proof of global nonlinear stability, switched/hybrid dynamics with delayed feedback, full 3-state network electrical power flow and eventual robust viability kernel.

## Next independently admissible work

Run committed verifier in GitHub CI and resolve any discrepancies; obtain Susa original and IEEE/IEC full text via authorized channels; derive the DAE feeder/network and temperature-dependent winding loss extension; specify physically measured state observation operators. Proceed to non-smooth/hysteretic/delayed control theorem tests without inventing a temperature-triggered controller in Kunlasing. With matched real data, preregister held-out component and interface validation before parameter fitting.
