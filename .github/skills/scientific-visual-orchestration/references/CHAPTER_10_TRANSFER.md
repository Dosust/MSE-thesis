# Chapter 10 transfer: mathematical ideas without physics substitution

**Conceptual reference:** [Gonzalez Vivo and Lowe, *The Book of Shaders*, Chapter 10 — Random](https://thebookofshaders.com/10/). This is an educational adaptation using original equations and example code, not a reproduction of the chapter's assets. Separate reusable learning implementation exists in the [Mathematics Art repository's skill](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience/blob/8f83c379c247ce7c1c7d7e3e8559e7836a13a2ef/skills/shader-randomness-scientific-visuals/SKILL.md); it is **read-only input** with a different project color policy and domain-neutral scope.

## Transferable mathematical lessons

| Topic | Exact learning objective | Permitted Deck3 transfer | Forbidden inference |
|---|---|---|---|
| Fragment coordinates | `u=x/W,v=y/H` | resolution-aware visual coordinate transforms | normalized coordinates are physical units |
| `floor`/`fract` | `fract(x)=x-floor(x)` including negative values | stable tiling and local coordinates | tiling equals finite-element or physical mesh |
| Fractional sine | deterministic `fract(A sin(ωx+φ))` | exploratory repeated patterns, labeled as synthetic | independent/uniform random variables |
| Distribution shaping | `Y=U^γ`, `γ>0`, under **U uniform** | textbook theoretical CDF/mean chart | a sine hash proves a calibrated distribution |
| Coordinate hashing | `h(i,j,seed)` | reproducible placement and tile orientation | inferred infrastructure topology |
| Moving rows | `d_j(t)=∫_0^t v_j(s)ds` | synthetic display-time animation | a real transportation speed or recovery law |
| Interpolated value field | bilinear interpolation with `q(t)=3t²-2t³` | explicitly *synthetic* smooth graphic; a Chapter 11-facing extension | inferred spatial covariance, heat exposure or reliability field |

### Exact probability condition

For `U~Uniform(0,1)` and `Y=U^γ`, `F_Y(y)=y^(1/γ)` for `0<=y<=1` and `E[Y]=1/(γ+1)`. This is a theorem **conditional** on the uniform input assumption; it cannot be silently transferred to a procedural sine hash.

### Correct time-varying motion

If a row has `v_j(t)=v0_j+a_j sin(ωt+φ_j)` for `ω!=0`, then the displacement is `d_j(t)=v0_j*t+(a_j/ω)*(cos(φ_j)-cos(ωt+φ_j))`. Multiplying instantaneous `v_j(t)*t` is generally wrong if `v_j` denotes velocity. Label display-time motion honestly; a real model's states must come from an admissible solver and time units.

### Code use decision

Prefer analytical Python/NumPy + vector SVG for exact mathematical figures and charts, SVG/PPTX-native geometry for arrows and diagrams, and PowerPoint click reveals for thesis stage-by-stage mechanisms. GLSL/WebGL is **optional** only when live fragment evaluation materially clarifies the question and a separate tested static fallback is provided. A browser canvas image embedded in PPTX does not convey working browser interaction or independently editable graphic elements.

### Color reconciliation

A distinct mathematics-art repository uses a separate blue aesthetic. When re-creating an *authored thesis figure* in this MSE repository, remap all authored strokes/labels to **the 13 exact values** in `../../deck3/references/DECK3_SRGB_PALETTE.json`. Do not copy a blue hexadecimal value from another project without checking registration. All authored canvases/boxes white. ASU Gold is limited to a small **nonessential** branded accent; no independent essential gold signal on white.

### Evidence transfer gate

The original code examples are *educational mechanics*, not evidence of extreme-heat interactions, functional dependency, reliability, resilience, emissions or sustainability. A new scientific field visualization requires admissible state equations, units, parameters, primary evidence, initial/boundary conditions, numerical verification, uncertainty and external validation status. A tile layout is not a Power/Transportation interface or a causal edge.
