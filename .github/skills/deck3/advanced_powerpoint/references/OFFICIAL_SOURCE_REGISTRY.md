# Primary Sources for Deck3 Advanced PowerPoint Engineering

**Retrieved/checked:** 2026-10-09. These links establish **software capabilities only**. They DO NOT substantiate physical thermal links, model parameters or thesis novelty. Verify the exact product/channel version before claiming runtime compatibility.

| ID | Product feature or API | Official / primary source | Boundary |
|---|---|---|---|
| MS-01 | Animate text, shapes, images and click settings | [Microsoft Support — Animate text or objects](https://support.microsoft.com/en-us/powerpoint/training/animate-text-or-objects) | Effect availability varies by host/version |
| MS-02 | Click a shape to trigger effects | [Microsoft Support — Trigger an animation effect](https://support.microsoft.com/en-us/powerpoint/trigger-an-animation-effect) | Mac/Windows UX differs |
| MS-03 | Curve/freeform motion paths | [Microsoft Support — Add a motion path animation effect](https://support.microsoft.com/en-us/powerpoint/add-a-motion-path-animation-effect) | Custom path moves an object; not a physical equation |
| MS-04 | Morph same semantic objects across slides | [Microsoft Support — Morph tips and tricks](https://support.microsoft.com/en-us/powerpoint/morph-transition-tips-and-tricks) | Objects with same `!!name` require one-to-one matching |
| MS-05 | Morph desktop/web availability | [Microsoft Support — Use the Morph transition](https://support.microsoft.com/en-us/powerpoint/training/use-the-morph-transition-in-powerpoint) | Charts may crossfade instead of morph |
| MS-06 | Shape-attached connectors | [Microsoft Support — Draw or delete a connector](https://support.microsoft.com/en-us/powerpoint/draw-or-delete-a-line-or-connector) | Curves/freeform/scribble differ from attached connectors |
| MS-07 | Freeform + edit points | [Microsoft Support — Draw or edit a freeform shape](https://support.microsoft.com/en-us/office/graphics-visuals/draw-or-edit-a-freeform-shape) | Freeform not automatically snapped to shape attachment points |
| MS-08 | Merge shapes | [Microsoft Support — Combining and merging shapes](https://support.microsoft.com/en-us/powerpoint/draw-a-picture-by-combining-and-merging-shapes) | Selection order can change operation semantics |
| MS-09 | SVG edit / convert to shape | [Microsoft Support — Edit SVG images](https://support.microsoft.com/en-gb/office/graphics-visuals/edit-svg-images-in-microsoft-365) | Converted shape fidelity requires checking |
| MS-10 | Equations in LaTeX/OMML | [Microsoft Learn — LaTeX Support in Microsoft 365](https://learn.microsoft.com/en-us/office/math/latex) | Only supported commands; round-trip tests |
| MS-11 | SmartArt build | [Microsoft Support — Animate SmartArt](https://support.microsoft.com/en-us/powerpoint/animate-your-smartart-graphic) | Appropriate for hierarchy, not causal physics |
| MS-12 | 3D models | [Microsoft Support — 3D models](https://support.microsoft.com/en-us/office/graphics-visuals/get-creative-with-3d-models) | Rotation/orientation; not actual equipment model without evidence |
| MS-13 | 3D animation | [Microsoft Support — 3D animation effects](https://support.microsoft.com/en-us/powerpoint/3d-animation-effects-in-powerpoint) | Subscription and platform dependent |
| MS-14 | Save slide as image/SVG | [Microsoft Support — Save a slide as an image](https://support.microsoft.com/en-us/powerpoint/save-a-slide-as-an-image-or-as-a-separate-presentation-file) | Export fidelity differs from editable slide and animation |
| MS-15 | Accessible reading order and alt text | [Microsoft Support — Reading Order pane](https://support.microsoft.com/en-us/powerpoint/make-slides-easier-to-read-by-using-the-reading-order-pane) | Grouping an already animated object may remove animations |
| MS-16 | Accessibility checker rules | [Microsoft Support — Rules for Accessibility Checker](https://support.microsoft.com/en-us/accessibility/office-accessibility/rules-for-the-accessibility-checker) | Manual reading order/contrast check still required |
| AS-01 | Aspose timeline and native On Click | [Aspose.Slides Python — Shape animation](https://docs.aspose.com/slides/python-net/shape-animation/) | Commercial/vendor API; verify installed library/version |
| AS-02 | Aspose custom cubic motion path | [Aspose.Slides Python — Custom animation](https://docs.aspose.com/slides/python-net/custom-animation/) | Coordinates normalized; behavior API complex |
| AS-03 | Add/remove/manage animation | [Aspose.Slides Python — Animation examples](https://docs.aspose.com/slides/python-net/examples/elements/animation/) | Run small executable test first |
| PG-01 | PptxGenJS primary repository | [gitbrent/PptxGenJS](https://github.com/gitbrent/pptxgenjs) | Strong slide object authoring, notes on imports |
| PG-02 | PptxGenJS known unimplemented features | [PptxGenJS Wiki — Unimplemented features](https://github.com/gitbrent/PptxGenJS/wiki/Unimplemented-Features) | Lists native animations; reevaluate only if a supported release implements them |

**Avoid citation laundering:** a documentation page about a curved arrow proves a software operation, not a real physical feedback path. Current thesis scientific sources must be cited next to the appropriate scientific mechanism separately.