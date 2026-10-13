# Transformer model-time animation lesson V1 — Najar-family pedagogical demonstrator

**Status:** Separate classroom exercise, **not** validated active-thesis model; does not amend the canonical presentation or evidence authorities.

## Source boundary

Najar, S., Tissier, J.-F., Cauet, S., & Etien, E. (2017), *Improving thermal model for oil temperature estimation in power distribution transformers*, Applied Thermal Engineering 119, 73–78, DOI:10.1016/j.applthermaleng.2017.03.061. Inspect **Fig. 1** and **Table 2** of the full article, not just abstracts or synthesized search summaries. The 160-kVA ONAN transformer identified parameters are **x = 0.80, R = 9.15, τo = 199 min, Δθor = 54.87 K**. These values were fitted using the paper's test arrangement, including a reduced-voltage short-circuit method. They are **not** calibrated to this thesis's grid or charger equipment.

The original transfer-function figure includes **k11**, not numerically listed among the four Table 2 fitted parameters. This exercise declares **k11=1 as an educational assumption**; it does not claim this factor is measured or source-validated.

## Conditional classroom model

For physical model time t in hours:

```text
Delta_theta_inf(K) = Delta_theta_or * ((1 + R*K^2)/(1+R))^x
tau_eff*d(theta_o)/dt + theta_o = theta_a(t) + Delta_theta_inf(K(t))
tau_eff = k11*tau_o, with k11=1 ASSUMED for class.
```

Initial condition: steady state at θa(0)=30°C and K(0)=0.50. **Synthetic inputs** for **12 hours**: ambient 30°C until 2h, rises linearly to 40°C at 5h, holds to 8h, falls linearly to 33°C at 11h; imposed load 0.50 for [0,3), 0.85 for [3,7), 0.65 for [7,12] hours. These are not the source paper's measured environmental or load profiles.

**Derived exercise result only:** computed top-oil start approximately 52.27°C, peak approximately 73.60°C and end approximately 67.57°C. No operational threshold is inferred. Solver: SciPy solve_ivp RK45, rtol 1e-9, atol 1e-10, max step 0.025h. Publish source/CSV, parameter manifest, frame samples and tests. Playback: 8 seconds at 24fps (192 frames), **representing 12 model hours**, not propagation delay or observation times.

## Design and QA

Original vector transformer symbol, white background, current 13-color palette, native Times New Roman PPTX text/lines, separate synthetic forcing and computed oil-temperature trajectories. Label conditional scenario in **every relevant frame**; do not depict I2/H1 or I3/H2 as established. If animation is model-based, display physical-time axis and keep presenter-time vs model-time explicit.

Follow sibling `../references/ANIMATION_QA_CHECKLIST_V1.md` with G0–G7 evidence gates. Actual Microsoft PowerPoint slideshow playback remains **NOT_RUN** unless independently performed. Full local reproducible training package (original Python source, SVG, MP4, GIF, editable PPTX, CSV, QA manifest) must not be claimed to be committed to GitHub until its bytes are uploaded and verified.

**Training question:** Why does a simulated θo response by itself not demonstrate that T1 charger thermal behavior changed actual grid-side AC demand or that P1 thermal protection curtailed charging?
