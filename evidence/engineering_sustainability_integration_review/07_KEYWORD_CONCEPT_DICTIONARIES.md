# Controlled Keyword / Concept Dictionaries

These terms are retrieval cues only. A hit does not constitute evidence. Every hit must be checked for focal-author action, context, alternative identity, and actual analytical use.

## P — Engineering / functional performance cues

### Mechanical
`strength`, `compressive strength`, `tensile strength`, `flexural strength`, `modulus`, `stiffness`, `ductility`, `toughness`, `bond strength`, `load capacity`.

### Structural
`structural response`, `displacement`, `drift`, `deformation`, `vibration`, `seismic response`, `fragility`, `damage state`, `reliability`, `load-bearing capacity`.

### Durability / service life
`service life`, `durability`, `carbonation`, `chloride penetration`, `permeability`, `freeze-thaw`, `deterioration`, `water absorption`, `corrosion`, `maintenance interval`, `replacement interval`.

### Geotechnical
`settlement`, `bearing capacity`, `subgrade modulus`, `vertical subgrade reaction modulus`, `soil stiffness`, `load-settlement`.

### Thermal / energy
`thermal conductivity`, `thermal resistance`, `U-value`, `heat transfer`, `energy demand`, `operational energy`, `energy performance`, `thermal comfort`.

### Acoustic / fire
`sound absorption`, `acoustic insulation`, `sound transmission`, `fire resistance`, `residual strength`, `elevated temperature`, `post-fire`.

### Pavement
`rutting`, `fatigue`, `resilient modulus`, `cracking`, `skid resistance`, `pavement life`.

### Functional / serviceability / resilience
`serviceability`, `comfort`, `functionality`, `performance requirement`, `performance threshold`, `resilience`, `recovery`, `downtime`, `damage probability`.

Verification question: **Did the focal authors actually measure, calculate, simulate, monitor, or analytically generate the property/result?**

---

## F — Integration cues

### F1 / parallel-comparison cues
`compared with`, `simultaneously evaluated`, `technical and environmental`, `mechanical and sustainability`, `performance and environmental impact`, `alongside`, `separately assessed`, `comparative assessment`.

These are only candidates for $P\parallel S$; they do not prove analytical coupling.

### F2 / directional-coupling cues
`service life`, `functional equivalence`, `equivalent performance`, `performance threshold`, `minimum strength`, `admissible`, `admissibility`, `design thickness`, `replacement interval`, `maintenance interval`, `durability-based`, `normalized per service life`, `adjusted by`, `dependent on`, `influences`, `determines`, `modifies`, `affects`, `used to calculate`, `used as input`, `input to LCA`, `inventory adjustment`, `design requirement`, `performance constraint`.

Verification question: **Does engineering performance actually change the sustainability calculation, functional basis, quantity, admissibility, service life, inventory, or boundary?**

### F3 / integrated-architecture cues
`sustainability index`, `composite index`, `integrated index`, `overall performance`, `consolidated index`, `eco-efficiency`, `performance-normalized`, `strength-normalized carbon`, `weighted score`, `value function`, `utility function`, `objective function`, `optimization function`, `decision function`, `multi-objective optimization`, `MCDM`, `MCDA`, `AHP`, `TOPSIS`, `ELECTRE`, `MIVES`, `grey relational analysis`, `Pareto optimization`, `weighted sum`, `regression model`, `surrogate model`, `response-damage-loss`, `causal chain`, `decision rule`, `ranking model`, `integrated assessment`, `multi-criteria evaluation`.

Verification question: **Does the engineering variable actually enter the author-implemented integrated formula/model/causal architecture/decision mechanism?**

---

## Causal verbs / operators to inspect

`affects`, `influences`, `determines`, `modifies`, `governs`, `contributes to`, `results in`, `leads to`, `translates into`, `incorporated into`, `included in`, `normalized by`, `weighted by`, `constrained by`, `adjusted for`, `based on`, `dependent on`, `used to calculate`, `used as input`, `used to rank`.

A causal verb is not sufficient by itself; confirm subject, object, and focal-study context.

---

## S — Sustainability cues

### Environmental
`LCA`, `life cycle assessment`, `environmental impact`, `GWP`, `global warming potential`, `carbon footprint`, `CO2 emissions`, `CO2-eq`, `embodied carbon`, `embodied energy`, `energy consumption`, `resource depletion`, `acidification`, `eutrophication`, `ecotoxicity`, `human toxicity`, `water consumption`, `waste generation`, `land use`.

### Economic
`LCC`, `life cycle cost`, `cost analysis`, `initial cost`, `maintenance cost`, `operating cost`, `replacement cost`, `total life-cycle cost`, `NPV`, `net present value`, `economic performance`, `cost-effectiveness`.

### Social
`S-LCA`, `social LCA`, `social sustainability`, `worker safety`, `occupational health`, `employment`, `stakeholder`, `community`, `accessibility`, `wellbeing`, `user comfort`, `downtime`, `social cost`, `social indicator`.

### Integrated
`triple bottom line`, `TBL`, `LCSA`, `life cycle sustainability assessment`, `sustainability score`, `sustainability index`, `environmental-economic-social`, `economic-social-environmental`, `integrated sustainability assessment`.

Verification question: **What numerical sustainability result did the implemented method actually generate?**

---

## D — Decision cues

`optimum`, `optimal`, `optimized`, `preferred`, `best alternative`, `selected alternative`, `recommended`, `ranking`, `rank`, `priority`, `decision`, `decision-making`, `selection`, `choose`, `trade-off`, `compromise solution`, `Pareto`, `feasible solution`, `design recommendation`, `preferred mix`, `preferred material`, `preferred technology`, `scenario selection`, `alternative selection`, `design optimization`, `sensitivity analysis`, `robustness`, `robust solution`.

Verification question: **What did the integrated analysis actually cause the authors to select, rank, reject, recommend, optimize, or prioritize?**

---

## Weak/background language

Treat the following cautiously because they commonly signal discussion rather than focal implementation:

`discuss`, `review`, `suggest`, `could`, `may`, `potential`, `previous studies`, `reported by`, `according to`.

---

## Strong implementation-language cues

Potential focal implementation signals include:

`we measured`, `was tested`, `was calculated`, `we performed`, `was assessed`, `was evaluated`, `was simulated`, `was optimized`, `was integrated`, `was used as input`, `was normalized`, `was weighted`.

These still require contextual verification. For example, “Smith et al. measured...” remains secondary evidence.

---

## Retrieval-to-coding boundary

The operational chain is:

$$
Keyword\ Hit\not\Rightarrow Evidence.
$$

Instead:

$$
\boxed{Keyword\rightarrow Candidate\ Passage\rightarrow Focal\ Author\ Action\rightarrow Extracted\ Evidence\rightarrow Interpretation\rightarrow Score.}
$$