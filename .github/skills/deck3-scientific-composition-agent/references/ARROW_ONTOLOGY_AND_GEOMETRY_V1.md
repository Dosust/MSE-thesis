# Deck3 Arrow Ontology, Geometry and Evidence V1

**Controlling principle:** No arrow without a defined scientific relationship, traceable endpoints, direction, units/quantities where applicable, evidence class, and the right figure purpose. Stylistic legend colors are approved **Deck3 13-token authored** colors (the official palette file governs).

| Type | Stroke | Deck3 color | Semantics / qualifiers |
|---|---|---|---|
| `AC_POWER` | solid directional | `#0072B2` | AC electrical power, P1→P2→T1 in ordinary charging; mark AC, port, P/Q where valid |
| `DC_POWER` | solid directional | `#0072B2` | T1 charger output → T2 battery DC; explicitly label DC |
| `HEAT_TRANSFER` | solid directional | `#006D70` | heat generated/rejected across an identified control-volume boundary; define receiver |
| `EXTERNAL_FORCING` | maroon directed | `#8C1D40` | H(t) heat exposure applied independently to P or T_e equipment, not intersystem causality |
| `CONTROL` | dashed directed | `#416985` | installed/documented control/actuation; conditional when not yet verified |
| `MEASUREMENT` | dotted directed | `#555D66` | observation from measured port/state toward instrument; never power flow |
| `CANDIDATE_P_TO_T` | dashed red directed | `#B4232C` | I3/H2 hypothesis: P thermal condition → documented protective/operational mechanism (if any) → charging; **NOT YET QUALIFIED** |
| `CANDIDATE_T_TO_P` | dashed red directed | `#B4232C` | I2/H1 hypothesis: charger thermal behavior → actual AC P/Q port change (if verified) → grid/transformer state; **NOT YET QUALIFIED** |
| `RESEARCH_SEQUENCE` | solid green directional | `#176B42` | methodological order ONLY, not physical cause |
| `ASSESSMENT_MAPPING` | solid green directed | `#176B42` | defined service→resilience→sustainability interpretation, not a direct physical flow |

**Geometry:** large clear arrowheads; endpoint on actual component port/boundary, not a random object center; no occlusion of connection heads; conductor/networks in proper electrical topology; no aesthetics-only bidirectional arrows. A double arrow means *two independently qualified paths*, not one unqualified reciprocal law. Arrows in conceptual uncertainty must keep its status visible **in every image frame**. Never depict all links as electrical wires.

**Arrow record required:** `{id,type,source,target,label,evidence_status,source_id_or_reason,qualifier}`, with separate quantities/units where relevant. Dynamic plots require equation, parameters, time base, model/measurement provenance and validation boundaries. Generic power path is an illustration of a possibility, not proof of installed wiring.

**Review anti-patterns:** shared ambient arrows conflated with physical thermal coupling; P3 as series feeder; unverified cooling fan; T4 independently fed from P2; green "positive sustainability" flow with no measured indicators; static scientific infographic falsely presenting curves/results.
