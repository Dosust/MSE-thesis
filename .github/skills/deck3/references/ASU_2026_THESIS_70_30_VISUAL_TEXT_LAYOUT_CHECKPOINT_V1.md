# ASU 2026 MSE Thesis — 70% Visual / 30% Editable Text Layout Checkpoint

**Date:** 2026-10-14 (session transition from 2026-10-13)
**User direction:** "the visual should take 70% of the normal space and the words content should take 30 % well organized".

## Google Slides working copies
- **New 70:30 review deck (editable text):** https://docs.google.com/presentation/d/1Ty3G-SXslT4l2da-qcvgIJRmXy-La_jBOeOY9eZ-iSo/edit?usp=drivesdk
- **Prior full-illustration review copy (unchanged):** https://docs.google.com/presentation/d/1slUwTyVLbaiHxJ0JrZw2xr7FMXsF749OJ36kZQmW78U/edit?usp=drivesdk
- **Original official ASU ten-slide research authoring deck (unchanged):** https://docs.google.com/presentation/d/1q6ts7HL1tlmJeo5ac8NROHOCASTbU4LlIK0TVNR87Ls/edit?usp=drivesdk

## Reproducible body-layout contract
- Live deck uses official 2026 ASU inherited master `p20`; exactly **10 slides**.
- Canvas **720 × 405 pt (16:9)**. A title zone sits above content. Separate body content of `x=29..690` points into visual and text regions.
- Image on each slide: `x=29, y=91, rendered width=454.955, height=256.048 pt`, preserving the source 1672 × 941 image aspect ratio. Body visual is ~70% of available content width; text column `x=495..690` is ~30%, with a 12-point gutter and a thin divider at x=489.
- Editable title `y≈16` and the concise framing sentence `y≈59`; Slide 1 has its three-line title in the main title zone; Slide 10 uses the official closing style.
- Right text: exactly **three purposeful heading+explanation pairs**, with each heading and body separately editable natively in Slides. Semantic text colors from approved palette. Small source/review status at column foot; white canvas, no new colored panel fills. ASU maroon titles / restrained institutional gold accent.
- Since inserted images are raster copies of earlier image-generator visuals, words/diagrams inside those images are *not* independently editable. The 30% sidebar native copy is editable. Keep scientific references and correction notices in native text.
- Deleted obsolete covering text boxes and drawings **only in the new review copy**; left original/native-authoring presentation untouched.

## Verified after edits
- Ten slide IDs and official ASU master `p20` verified through the live Google Slides API.
- All ten images have measured rendered dimensions of ~455 × 256 pt at exactly `x=29,y=91`.
- Each slide has three native editable sidebar sections, one title, a divider and a science-QA/source footer. Approximately 70/30 body allocation is consistent across ten slides.
- **No final native rendered-image QA performed**; slides must still be opened at full display size for text wrapping, projection readability and caption-safe overlays. The figure text may be too small after 70% scaling on Slides 5–8 and require a redesigned cropped/vector asset.

## Continuing scientific restrictions
**SCIENTIFIC REVIEW DRAFT — NOT READY FOR RELEASE.** The previously identified scientific figure flaws are unresolved: Slide 5 serial P3 and unsupported fan depiction, Slide 6 proposed arrows, Slide 7 fabricated-looking scatter depiction, and Slide 8 mandatory recovery/double-arrow semantic flaws. Those slides carry native visible warnings. The 70/30 improvement concerns visual/text hierarchy only. It does not qualify unverified mechanisms, constitute experimentally validated data, or override the frozen SO1–SO3 and sustainability framework. Do not promote these generated figure pixels to a thesis-final release without correcting and auditing the actual image assets.
