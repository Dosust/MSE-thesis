# Deck3 — Official ASU Ten-Slide Google Slides Scientific Visual Implementation & QA

**Date:** 2026-10-13  
**Artifact:** https://docs.google.com/presentation/d/1sQkwI99ymiz1PYEmy-3suW_064bHDlTjF__8T-yYB9Q/edit?usp=drivesdk  
**Google Drive location:** https://drive.google.com/drive/folders/1DVphEnPcVSgnEG2fexjhVAZ7CkKxhrYx  
**Repository status:** draft presentation visual implementation; no change to frozen scientific research authorities or to the separate user-approved 8-slide Deck3 master.

## 1. Real Google Slides implementation (not illustrative promises)

The ten-slide native copy of the official 2026 ASU template was updated using Google Slides **editable** shapes, text, lines, equation labels and real photograph elements. Imported photography is not a rasterization of the whole slide. Presentation continues to have **exactly ten slides**.

| Slide | Implemented visual | Evidence and limits |
|---|---|---|
| 1 — Thesis title | Two Wikimedia Commons photographs in native image frames with attribution and identification as **distinct illustrative installations** | Substation distribution transformer photo is **not** the TU Wien case; Maryland charging-site photo is **not** Qatar CPC50 |
| 2 — Outline | Native ASU agenda layout and numbered research progression | Textual roadmap; no extraneous equipment artwork |
| 3 — Industrial background | Two additional licensed authentic equipment photos, separate ambient heat-forcing indicators, normal AC supply *architecture* arrow and utility/operator messages | Shared heat does not establish thermal causality; photos are distinct sites, not one installation |
| 4 — Scientific gap and objectives | Two **separately dashed** I2/H1 T_e→P and I3/H2 P→T_e candidate mechanism chains; exact SO1–SO3 objective substance and status labels | Neither hypothesis qualified, all cross-system mechanism claims remain OPEN |
| 5 — Physical architecture | Eight editable P1–P4/T1–T4 component nodes, real transformer/charger reference photographs, normal AC and DC supply arrows, separate support/cooling lines, two named system regions | P3/P4/T3/T4 are **not** in series with AC/DC supply; P4 support is branched from P1; photos are not same equipment as research datasets |
| 6 — Methodology | Five-stage editable process, distinct testing/verification roles, editable general differential–algebraic equations | General schematic only; no simulation claimed as physical validation |
| 7 — Research progress | Native 2026 ASU three-metric layout (8,592 rows; Bærug 0.907 K MAE; external Qatar charger 86→169 min) plus separate-evidence banner | Tu Wien/Bærug/Qatar not one observed coupled system; no fabricated time-series |
| 8 — Services and sustainability | Editable required/delivered-service inputs **both directed into** a per-service deficit definition; two separately routed sustainability consequence pathways | Proposed assessment method, not real coupled-service observation; no automatic sustainability benefit |
| 9 — Research timeline | Editable continuous time-axis with October–November 2026, December–January 2027 and February–April 2027 phases | Explicitly **proposed** milestones, not completed research tasks |
| 10 — Closing | Retained official ASU closing layout, minimal message | No scientific result introduced |

## 2. Physical and mathematical claims

- Architecture: `P1 -> P2 -> T1` is the normal AC supply pathway; `T1 -> T2` is the DC charging energy pathway. These connections do not prove heat-conditioned I2 or I3 causality.
- External extreme heat `H(t)` can act independently on both constituent systems; it is not represented as heat transferred from one installation to another.
- I2/H1 is candidate because the measured charger internal-thermal-state-to-grid-side AC power law is not yet admitted; proposed receiver response remains conditional.
- I3/H2 is conditional on an **implemented**, temperature-conditioned P3 protection/load-management action; transformer temperature alone is not a verified EV charging restriction.
- The illustrative DAE `x_dot = f(x,z,u,H;theta), 0 = g(x,z,u,H;theta)` is a general mathematical modeling form. Each actual constitutive/interface law remains evidence-gated.
- For each service `i`, proposed deficit `D_i(t) = max(0, Q_i^req(t)-Q_i^del(t))` requires **matched units and defined service boundary**. It does not establish observed deficits by itself.
- Resilience and both downstream sustainability consequence pathways are *assessment definitions*, not completed quantified outcomes.

## 3. Actual authentic photo references / licenses

1. **Yoshieslunchbox**, *Distribution Transformer 1.jpg*, 2024, Wikimedia Commons. Described by source as a **12.5 kV substation distribution transformer**; CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Distribution_Transformer_1.jpg, https://creativecommons.org/licenses/by-sa/4.0/.
2. **G. Edward Johnson**, *DC fast charging at Ikea College Park MD 2026-01-20 13-23-57.jpg*, Wikimedia Commons. Maryland outdoor charging site; file metadata describe 350-kW DC charging, **not** Qatar CPC50; CC BY 4.0, https://commons.wikimedia.org/wiki/File:DC_fast_charging_at_Ikea_College_Park_MD_2026-01-20_13-23-57.jpg, https://creativecommons.org/licenses/by/4.0/.

Photographs are authentic independent physical references. Cropped/resized presentation use does **not** establish observed electrical connectivity between them or equivalence to researched equipment. Source credits are on figure-bearing slides. BY-SA adapted-content obligations require checking on redistribution.

## 4. QA ledger — tested, untested and blocked

| Gate | Status | Traceable evidence / limitation |
|---|---|---|
| Exact original official ASU template remains unchanged | PASS | User-supplied native Slides template was copied; only the copy edited |
| Exactly 10-slide native order | PASS | Slides outline API readback |
| Saved under Google Drive Deck3 | PASS | Drive metadata parent readback |
| Native editable text, nodes and arrows | PASS (API-level) | Successful Google Slides batchUpdate operations, subsequent presentation-object readback |
| All ten slides render through Google thumbnail service | PASS (API-level only) | Ten individual MEDIUM slide-thumbnail requests returned 800×450 thumbnails |
| Text/image objects within 16:9 canvas | PASS (structural bounding check) | No true text or image overflow flagged; Google's line-size property uses a degenerate-line convention and cannot be evaluated as a plain rectangle |
| Distinct scientific status/photographic provenance | REVIEWED | Evidence-stream distinctions and source licenses checked; some attribution/reuse details need final release review |
| Full rendered pixel/legibility/overlap review | **NOT_RUN** | Slide thumbnail URLs were not materialized locally for image inspection; API rendering success ≠ visual pass |
| Exact figure-area dominance (70–80% where eligible) | **NOT_MEASURED** | No segmentation-based meaningful scientific-content coverage calculation |
| Photo licensing for final redistribution | REVIEWED, **NOT_RELEASE_APPROVED** | Recheck CC BY-SA derivative obligations and final credit treatment |
| Measured-data plots/complete physical validation | **NOT_DEMONSTRATED** | No Bærug raw-series plot, no matched Qatar–TU Wien field experiment |
| PowerPoint export and actual presentation playback | **NOT_RUN** | Google Slides-native editability demonstrated only; animation not developed or tested |
| Accessibility/caption overlay at actual projected scale | **NOT_RUN** | Template native layout preserved; final WCAG/readability/captions check still required |

**Acceptance state:** working scientific Google Slides visual draft. It has genuine editable diagram content and authentic reference photos, but should not be described as publication/release-ready until rendered pixel inspection, scientific source verification, photo-credit/reuse audit, complete original objective display, and presentation-scale QA are completed.
