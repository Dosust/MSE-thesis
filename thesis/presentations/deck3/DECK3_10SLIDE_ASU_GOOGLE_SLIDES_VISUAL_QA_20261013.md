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


## 2026-10-13 — Ten generated figure previews placed into Google Slides

**User-directed change:** Imported the ten 1672×941 PNG image previews, one on each corresponding native ASU slide, using the Google Slides API local-image sidecar; removed previous overlapping slide-local content and retained editable native slide titles and evidence caveats. Source 2026 ASU template unchanged; an independent backup of the prior Deck3 presentation was made before this update.

- **Current updated presentation:** https://docs.google.com/presentation/d/1sQkwI99ymiz1PYEmy-3suW_064bHDlTjF__8T-yYB9Q/edit?usp=drivesdk
- **Backup (previous image/shape integration):** https://docs.google.com/presentation/d/1iHUoIuSXGMxwBhDZAVgO30jPwT9_-7hksxQpfliGAV8/edit?usp=drivesdk
- **In Google Drive:** same Deck3 folder, id `1DVphEnPcVSgnEG2fexjhVAZ7CkKxhrYx`.
- **Image-object readback:** 10/10 slides contain exactly one newly embedded `deck3_visual_20261013_sXX` image; each has independently editable title. Figures preserve source 1672:941 aspect ratio.
- **Render API:** 10/10 native Google Slides thumbnail requests succeeded at 800×450, but this is NOT a pixel/legibility QA pass.
- **Explicit caveats added:** Figures are conceptual; photos in generated scenes are not authenticated field images; Bærug displayed time series is illustrative rather than source-derived; network and thermal relationship drawings are not engineering-verified; source streams are separate; candidate thermal mechanisms are unqualified and no coupled validation is claimed.

**New representation caveat:** The new primary figures are **raster PNGs**, so internal figure labels/diagrams are not editable native slide objects; native slide titles and caveat notes remain editable. The earlier vector-style diagram draft is preserved in the backup. This version is a **visual review deck**, NOT a final scientifically approved thesis figure set. The earlier science risks documented above still require correction; placing the images does not resolve them.


## 70/30 layout update — 13 October 2026

**Google-native deck:** https://docs.google.com/presentation/d/1sQkwI99ymiz1PYEmy-3suW_064bHDlTjF__8T-yYB9Q/edit?usp=drivesdk

**User-requested redesign:** The ten generated visual previews now occupy approximately **70% of the usable slide-body width** (left region), and each slide has a separately editable **30% concise scientific-text column** (right region). The images are scaled proportionally, not cropped; white background and minimal maroon rule retain the ASU research-deck hierarchy. Each right panel contains one main message and three short content points; evidence caveats/source notes remain at the foot of the slide. The long thesis title received custom header spacing.

**Rollback copy of the preceding image-first variant:** https://docs.google.com/presentation/d/1-wFWQTaGrOSwdtgGi6VdeHCdxZwz1Nq_3bl0KCP0Ul4/edit?usp=drivesdk

**Verification:** native element readback found 10/10 images each approximately 478×269 pt at x=18 pt, no slide-boundary overflow, and 10/10 Google-native 800×450 thumbnail generation checks passed. This is **layout-level verification**, not a pixel-level overlap, small in-image caption legibility, data-origin or formal scientific validation pass. Previous cautions regarding illustrative charger and transformer scenes, hypothetical service curves, unqualified I2/I3 and source-specific data remain in force.

## Latest active Google Slides layout — 14 October 2026 (supersedes 70/30 draft)

**User-directed result:** The SAME editable native Google Slides presentation now uses a **65/35 usable-content body split**, with a scientific-visual region at approximately x=26–455 pt (width ≈429 pt) and an editable research-message region at approximately x=468–696 pt (width ≈228 pt), separated by a narrow gutter. Percentages describe the two content regions excluding their gutter and slide title/footer. The resulting body split is approximately **65.3% / 34.7%**. White canvas and white panel interiors; all authored elements conform to the canonical 13-color sRGB palette. Photographs retain their natural colors.

**Current artifact:** https://docs.google.com/presentation/d/1sQkwI99ymiz1PYEmy-3suW_064bHDlTjF__8T-yYB9Q/edit?usp=drivesdk

**Recovery backup (before this 65/35 rebuild):** https://docs.google.com/presentation/d/1MBhmtzAfPe6FLFTlKFnTE9zGXYgOB1GCKXj4DbmkrZg/edit?usp=drivesdk

### Scientific content and presentation form corrected
- **S1:** authentic, separately licensed Wikimedia Commons transformer and DC charging-station photographs (independent installations, not joint field test), with source credits; prior AI image replaced.
- **S2:** native editable three-stage research roadmap, no generic illustrative chart.
- **S3:** native editable two-system external-heat and operating-process diagram; independent external forcing does not prove thermal cross-system causality.
- **S4:** separate T_e→P I2/H1 and P→T_e I3/H2 candidate mechanisms, dashed unknown/conditional links. Three frozen V1 objectives are represented in concise slide-summary text; full official text remains in canonical source.
- **S5:** all eight selected P1–P4/T1–T4 hardware components placed in their physical-system roles; correct main AC P1→P2→T1 and DC T1→T2 energy path; auxiliary/cooling hardware not falsely inserted in the series supply.
- **S6:** evidence admission, electrical verification, thermal state formulation, independent directional tests and bounded service assessment, with the **general**, not calibrated, DAE.
- **S7:** exact checkpoint numerical summaries only; TU Wien 50 kW DC conditional assumptions η=0.95/PF=0.98 with 377.62 V and 4.760 kW *network resistive losses*; independent Bærug 40 MVA dataset 8,592 rows and held-out 0.907 K MAE/1.156 K RMSE; independent published Qatar CPC50 tested charging durations 86 vs 169 min. No fabricated time-series plot, invented feeder topology, or combined installation.
- **S8:** independent electricity-service and mobility-service assessments, distinct direct vs engineering-response sustainability pathways, and environmental/economic/social consequence categories. No measured service deficits or unsupported SDG claims.
- **S9:** proposed 2026–2027 research phases, with a prominently identified synchronized-data **GO/NO-GO** evidence requirement. No timeline tasks claimed complete.
- **S10:** intentionally minimal native conceptual chain labeled **target research logic**, not an established coupled validation result.

### Verified
- Google Slides native asset/readback: **10 slides**, **all 10 render** as 800×450 thumbnails.
- All slide-local shapes are within the 720×405 pt canvas; **0 geometrical text-box intersections** under the audit threshold (>8 pt width and >7 pt height).
- Every authored slide-local foreground and filled shape uses the existing **13-color Deck3 palette** after removal of legacy `#303C49` and `#A5AFBA`.
- Native text and engineering figure shapes remain independently editable; only the two title-slide *authentic photographs* are image elements.
- Google Drive folder unchanged; prior deck backed up.

### Open release checks (NOT_RUN)
- Pixel-level thumbnail inspection for exact kerning, image composition, caption-area collision, and projection-distance readability was not performed.
- True export/presentation playback, interaction and animation testing were not performed.
- This remains an engineering design **draft**. Complete equipment-specific thermal-interface validation and measured service/sustainability outcomes are still OPEN. The source records are separate, not one physical testbed.

**Governance:** This ten-slide ASU Google-native variant remains separate from the frozen eight-slide three-minute version and Chapter 1 variants. No canonical thesis authorities or unmerged objective PRs were modified.


## ASU-native engineering redesign — 2026-10-14 (active)

**Google Slides delivery:** https://docs.google.com/presentation/d/1sQkwI99ymiz1PYEmy-3suW_064bHDlTjF__8T-yYB9Q/edit?usp=drivesdk

**Recovery copy before this pass:** https://docs.google.com/presentation/d/1oIeC4fHNLrTGMZPRSFQQB6kIjLcMECKBtOM-KWTxPn4/edit?usp=drivesdk

**Scope:** User-requested practical implementation of ASU-oriented visual, higher-resolution photographic, scientific-mechanism and Google-native human design improvements in the ten-slide **65/35 variant**. No modification to canonical research files or the separate eight-slide/Chapter-1 masters.

### Applied, native and scientific
1. All 10 slides: ASU-approved system font **Arial** applied to editable text as an **explicit presentation-variant exception** to the repository's general Deck3 Times New Roman policy (which remains unmodified). Main slide headings upgraded where they fit and colored ASU Maroon `#8C1D40`; physics roles retain approved blue/green/teal/red. The existing 13-token sRGB authored palette, white interiors, 65/35 usable-content arrangement and 16:9 structure are preserved.
2. Slide 1: replaced two lower-resolution reference imports with Commons originals requested at 2048/3840px variants, with native image frames proportioned to actual *source* image ratios 3672×4896 (transformer) and 8064×4536 (charging site). Natural equipment colors preserved; independent-site/non-testbed caveats and click-through source captions kept.
3. Slide 3: authentic separate transformer and charger photo references inserted, with source aspect ratios preserved and heat exposure separated. The photograph-connecting AC arrow was removed, because the two photographed facilities are not one physical system; overlapping photo annotation removed.
4. Slide 5: rebuilt the main P1→P2→T1 AC and T1→T2 DC diagram, and added explicitly differentiated equipment support associations P3→P1 conditionally, P4/P1 transformer cooling, T3/T1 EVSE cooling, and T4 vehicle auxiliaries (NOT battery cooling). Technical figure is individually editable native Slides shapes/lines.
5. Slide 6: directional process flow added, including an evidence-admission GO/NO-GO-type conditional route. General, not fitted, DAE retained; numerical verification ≠ coupled field validation.
6. Slide 7: replaced densely packed small number columns with three native, separately attributed evidence rows: TU Wien conditional electrical simulation; independent Bærug transformer test; published Qatar CPC50 field study. No fabricated observational curves or spurious combined testbed.
7. Slide 8: recreated electricity and mobility service deficits as separate operations; service comparisons feed two scenario *consequence* pathways (direct heat and response), with environmental/economic/social indicators distinguished. No aggregation of unlike service units and no unsupported observed response.
8. Slide 9: explicit directional proposed chronology, admission decision, and NO-GO narrowing statement; no future tasks reported completed.
9. Slide 10: removed repetitive boxes; minimal scientific closing with qualifying question.

### Verified after final mutation
- Native Google Slides readback: **10/10 slides**, 100% editable text with font `Arial` (native diagrams + 4 real photographs across S1/S3). Figure labels, arrows, and right-column copy remain individually editable.
- 13-color exact governed sRGB palette: **0** unapproved authored text/panel colors detected; natural photo pixels exempt.
- 720×405pt canvas: **0** slide-local element out-of-bounds errors, **0** text-box geometric overlap pairs. Heuristic line-wrap check reported **0** risks after repair (not equivalent to actual pixel review).
- Arrow connector counts: S2=2; S3=2 (separate external forcing); S4=4; S5=6; S6=5; S8=4; S9=3; S10=1.
- Google Slides render service: **10/10** medium 800×450 thumbnails generated.
- The two authenticated S1 photo captions link to Wikimedia Commons source pages.
- Photo source identity: Yoshieslunchbox, *Distribution Transformer 1.jpg*, CC BY-SA 4.0, 3672×4896; G. Edward Johnson, *DC fast charging at Ikea College Park MD ...*, CC BY 4.0, 8064×4536. Both are illustrative *independent facilities*, not the research's P1/T1 case or Qatar CPC50. Source: respective Commons image-file metadata.
- ASU typeface source: https://brandguide.asu.edu/brand-elements/design/fonts (Arial approved system/Google fallback); photo treatment source: https://brandguide.asu.edu/execution-guidelines/photo-video/art-direction; logo usage source: https://brandguide.asu.edu/brand-elements/logos/asu-logo.

### Explicit NOT_RUN / OPEN release gates
- Google thumbnail **pixel-level visual inspection** at actual projection scale: NOT_RUN (10 successful render API calls do not establish pixel inspection).
- Insertion and clear-space review of an **approved official ASU logo asset**: NOT_RUN; no fabricated/recolored ASU logo was authored.
- Projector playback / animation checks and rigorous native chart source-vs-render checks: NOT_RUN.
- Researched **coupled I2/I3 physical evidence** and field validation, fixed service metrics, and measured sustainability indicators: OPEN, unchanged. The deck describes evidence qualification, not a validated joint physical testbed.
- Source photo license/redistribution sign-off for publication: REVIEW, including CC BY-SA obligations.

**Result status:** materially improved human-editable ASU-oriented 65/35 presentation; engineering/scientific release still gated by actual pixel viewing and physical-evidence review.


## Current typography and layout correction — 2026-10-14

**User-authorized change:** Changed the **ten-slide active Google Slides presentation** back from the prior Arial variant to **Times New Roman** for all editable slide text. This directly restores the default Deck3 thesis typography policy, superseding the earlier presentation-only Arial exception for this active file. Slide body remains 65/35 with white panels and the established scientific palette.

**Current active Google Slides:** https://docs.google.com/presentation/d/1sQkwI99ymiz1PYEmy-3suW_064bHDlTjF__8T-yYB9Q/edit?usp=drivesdk

**Prior-version backup:** https://docs.google.com/presentation/d/1g9m84mu2YCC4sSYH2g8FQIfmE6R0Xizufs0ElQE6psk/edit?usp=drivesdk

**Changed:** 181 text-bearing shapes initially; one subsequently removed as a duplicate photo-license caption that geometrically overprinted the large official ASU signature on Slide 1. Photo source links on Slide 1 and attribution on Slide 3 remain.

**Readback:** 180/180 current native text-bearing slide objects use Times New Roman (211 explicitly styled text runs); all 10 slides retain their content; bounding-box check found 0 slide-local non-line objects outside 720×405pt slides. Exported Google Slides PDF contains exactly 10 pages and no extracted text spans outside page bounds; rendered all 10 pages at 120 dpi and inspected the whole contact sheet, including title-slide fix. The ASU master/layout's own inherited copyright/signature font was not overridden. The PDF renders do not constitute guaranteed projector playback or exhaustive semantic/physical validation.

**Open design item not changed in this typography-focused pass:** gold vertical stripe inherited from the ASU layout on Slide 2, and other original template decorative features. Does not prevent text fitting. In this iteration avoid patching institutional master layers without a separately authorized review.
