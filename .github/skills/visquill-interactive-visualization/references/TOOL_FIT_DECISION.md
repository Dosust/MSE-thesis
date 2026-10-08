# Decision Matrix: Is VisQuill Necessary?

## Core selection
VisQuill GDK is a **2D browser-based TypeScript reactive-geometry library**, not a solver, a citation provider, or a general static-chart library.

| Output goal | Preferred tool | Reason |
|---|---|---|
| Standard thesis temperature or service-vs-time plot | Python/Matplotlib | precise static axes, uncertainty and file export |
| Residuals, credible intervals, validation plots | Python/Matplotlib | analysis and ordinary plotting |
| Static Chapter 1 physical system boundary | SVG editor, diagram skill, PPTX | simple, auditable, no runtime |
| Presentation infographic or process roadmap | SVG/PPTX + infographic skill | editable projection-ready deliverable |
| Interactive drag-based mechanism graph with real geometric constraints | VisQuill GDK | dynamic geometry is central |
| Time scrubber changing multiple physically defined views from approved results | VisQuill GDK MAY be useful | only if reactive 2D spatial layout adds real value |
| Interactive geographic data exploration with lenses | VisQuill Lens candidate | separate product; CSV/mapping use case |
| Full GIS map, routing and large geographic layers | dedicated GIS/map tools | VisQuill alone is not a generic GIS engine |
| Large 3D power/thermal simulation | external scientific solver + appropriate 3D tool | GDK 2D graphics is not designed for 3D |
| Solving heat transfer, estimating parameter uncertainties | external physics/statistical tools | do not use a graphics SDK for analysis |

## Five qualifying questions
1. Does interaction create an understanding unavailable from a static figure?
2. Is this an appropriate *2D geometry/constraints* problem?
3. Does the viewer consume traceable computed results without modifying the physical laws?
4. Can output be understood as a static fallback in a thesis defense/PDF?
5. Is the implementation realistic given the Spring 2027 deadline and tested deployment/attribution obligations?

If 1, 2, 3 or 4 fail: use standard plotting/vector tools. If 5 fails: defer the viewer, deliver static figures first.

## Budget rule
Never postpone evidence qualification, SO1–SO3 validation or thesis writing to build a visually attractive interactive app. Consider a single narrow prototype only after the relevant numerical results and scientific semantics are established.

## Boundaries
The canonical Electrified Transportation System is the full road-vehicle/RESS/propulsion/auxiliary/electrical supply/EVSE/connection/control scope. Displaying only one charger is a labeled **case subset**, not a replacement system definition.

Direction P→Te / Te→P is supported separately; a common forcing heat arrow touching both sides does not justify a feedback loop.

Solid lines and dashed lines have *semantic* meaning; dashed is for control, not a substitute for an OPEN evidence status.
