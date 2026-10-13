# Scientific engineering animation QA — V1

Every item requires PASS, FAIL, OPEN, NOT_RUN or N/A with supporting evidence. A failed required gate cannot be offset by a good-looking video.

| Gate | Required test | Evidence to retain |
|---|---|---|
| G0 Authority | Correct current title/scope/objectives; resolve presentation variant; preserve frozen slide text | authority paths and variant ID |
| G1 Science | Component IDs, boundaries, ports, typed energy/control/measurement/forcing, direction, thermal/electrical conservation; no I2/I3 promotion | figure contract, edge ledger, source trace |
| G2 Evidence and rights | Device claims and model parameters traceable; artwork original or usage rights checked; unsupported status clear | citations, licence/permissions, provenance |
| G3 Simplicity | One principal message, minimal meaningful motion, enough whitespace, legible explanatory text | storyboard and necessity audit |
| G4 Geometry/render | 16:9, no clipping/overlaps/distortion, exact allowed authored colors, Times New Roman as available, all sampled frames legible | PNG first/mid/final, slide render, font audit |
| G5 Native semantics | Editable PPTX titles/labels/equations/arrows/diagram; note embedded video is *not* natively editable | PPTX shapes/media/font checks |
| G6 Animation | Check frame count/fps/duration; distinguish presenter seconds from model time; validate modeled trajectories if any; **desktop PowerPoint slideshow actual click playback separately** | ffprobe output, animation clock declaration, playback evidence or NOT_RUN |
| G7 Reproducibility | SVG/source code, build deps/version, hash manifest, QA, original-source rights, explicit OPEN issues | source files and SHA256 manifest |

## Model-time evidence gate

If the moving geometry is a modeled state or flow, require **governing equation, dimensional units, initial conditions, boundary conditions, numeric solver, parameters and their evidence, verification tests, validation plan and model scope**. Otherwise **narrative reveal only**; no invented curve, delay, thermal threshold or modeled outcome.

## Evidence status syntax

- **Measured:** trace to actual observed dataset and its limits.
- **Modeled:** equation + parameter source + verification, and validation status (not automatically validated).
- **Candidate / Not Yet Qualified:** physically plausible hypothesis; conditional arrow style and text in every relevant frame.
- **Unknown / Open:** not assumed or filled.
- **Not Run:** a test was not executed.
- **N/A:** scientifically inapplicable (e.g., ODE solver validation for staged object reveal).

## Animation export checks

- SVG contains original, individually identifiable shapes or groups, with exact color tokens for authored graphics.
- Media video dimensions and rate verified using `ffprobe`, not guessed from target settings.
- Beginning, middle and end frames are independently inspected; no temporary visual suggests a causal claim without its qualifier.
- 16:9 slide and poster geometry tested, text legibility verified, PowerPoint editability checked through shape inventory.
- A separate `pptx_real_slideshow_playback` check must remain **NOT_RUN** until actually played and evaluated on desktop PowerPoint.
- Record distinction between first-person or editorial timeline motion and actual time variable `t` whenever state-time theory is referenced.
