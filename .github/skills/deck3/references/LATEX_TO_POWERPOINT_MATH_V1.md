# Deck3: main.tex, LaTeX and editable PowerPoint mathematics
Effective 2026-10-09. Applies to all Deck3 forms. This is a workflow specification, not evidence of executed conversion.

## Source and output hierarchy
1. Read main.tex, all input/include files, preamble, macro definitions, bibliography and figure sources before extracting formulas. Preserve file locations, labels and provenance.
2. Keep main.tex as the source of mathematical truth when it is supplied. An equation in PowerPoint is a derivative display object; edit source first and regenerate when equations change.
3. Preferred editable slide output is Office Math (OMML). A rendered SVG/PDF remains scalable but is NOT a native-editable Office Math expression. Plain LaTeX text and PNG are also NOT native equation objects.
4. Microsoft 365 supports conversion of compatible LaTeX and Presentation MathML to Office Math. Check target version and supported commands, not all packages or environments work.
5. Use scalable vector fallback for incompatible complex mathematics or TikZ/PGFPlots; keep source alongside, never claim native equation editability.

## Conversion workflow
A. Inspect source and compile main.tex with its intended engine when possible. Record actual command and result, or NOT_RUN.
B. Inventory each equation: ID, source file and line/label, exact TeX, required macros, physical meaning, variables and units.
C. Classify as NATIVE_OMML, NATIVE_AFTER_EQUIVALENT_REWRITE, VECTOR_WITH_TEX_SOURCE, or BLOCKED.
D. For supported equations, use Insert > Equation in PowerPoint and LaTeX linear input or import supported Presentation MathML; convert to professional Office Math.
E. For programmatic production, verify m:oMath or m:oMathPara exists in saved slide XML. Simply showing correct glyphs, Unicode, SVG or embedded TeX is not proof of editability.
F. Compare original LaTeX render to an actual target PowerPoint render. Check indices, accents, fractions, matrices, alignment, brackets, units and special symbols.
G. Test semantic/dimensional consistency separately from appearance. A generic thermal energy balance is not a case-admitted device model.
H. Store source code and required macros in a slide/equation manifest or speaker notes. Rebuild and retest after any change.

## Platform-specific caution
Windows PowerPoint equation insertion shortcut: Alt+=. Mac PowerPoint insertion: Control+Option+=. Professional conversion Windows: Ctrl+Alt+=; Mac: Command+Option+= in supported versions.
Microsoft states that imported LaTeX equation numbering commands (tag, label, ref, eqref) are discarded; keep numbers and labels separately in editable PowerPoint text. Some display style, matrix alignment, spacing and multiline layout differ from TeX.
Unsupported commands may appear literally. For that reason exact semantic and visual inspection is mandatory.

## Examples for Deck3
Energy balance source: \frac{dU_{\mathrm{th}}}{dt}=P_{\mathrm{heat}}-\dot Q_{\mathrm{net,out}}
Check units dU/dt (J/s = W), heat rate (W), outward heat flow (W), control volume and sign conventions. Show as black editable Office Math on white.
Candidate dynamics: \dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{z},H,\mathbf{u};\boldsymbol{\theta}). Present as proposed model architecture only, not verified coupling.
Service requirement: Q_k(t)\geq Q_k^{\mathrm{req}}(t). Identify electricity/mobility service units and meaning.

## Slide figure rules
Photorealistic equipment should contain no generated equations. Overlay exact math, ports and scientific arrows with editable PowerPoint content.
TikZ and PGFPlots can produce precise SVG/PDF illustrations; resulting SVG is not editable PowerPoint-native geometry unless rebuilt with shapes. Authentic numerical plots require source data, axes, units and provenance.
Use only the 13 approved Deck3 sRGB authored color tokens; equations black, canvas white, Power blue, Transportation forest green, interfaces teal, observations cyan blue, thermal limits deep red.

## Per-equation manifest
eq_id | source_file | source_label | original_tex | expanded_tex | macro_dependencies | slide_number | output_mode | OMML_check | actual_render_check | dimension_check | scientific_status | limitations.

## Acceptance
M01 all source files inventoried; M02 actual compilation status; M03 source-to-slide trace; M04 macro integrity; M05 OMML XML verified; M06 visual/semantic equation matching; M07 numbering trace; M08 units/dimensions; M09 palette; M10 no equations in raster AI images; M11 model assumptions correctly labeled; M12 in-app editability and animation tested or NOT_RUN.

## Authoritative documentation
https://learn.microsoft.com/en-us/office/math/latex
https://learn.microsoft.com/en-us/office/math/mathml
https://learn.microsoft.com/en-us/office/math/
https://support.microsoft.com/en-us/accessibility/office-accessibility/use-keyboard-to-work-with-equations