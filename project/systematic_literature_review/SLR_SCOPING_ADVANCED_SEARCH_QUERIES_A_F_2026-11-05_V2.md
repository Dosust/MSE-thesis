# Systematic scoping review: advanced search codes A–F (V2)

## Search boundaries

| Setting | Selection |
|---|---|
| Research field | Mathematical physics and electrical/systems engineering of thermal power–electrified transportation |
| Publication period | 2000-01-01 through 2026-11-05; indexed year filters 2000–2026; exclude future-dated works on eligibility checking |
| Foundational physics before 2000 | Retrieve separately by reference/citation chasing, recorded as additional-source searches |
| Preferred full-text languages | English and French |
| Search language | **All languages, no database language filter**; non-English/French potentially eligible when a reliable translation is available; record access/translation limitations |
| Location | Worldwide, no geographical limits |
| Source types | Journal articles, conference studies, technical reports, standards, theses, data descriptors, preprints; distinguish peer-reviewed primary studies from other strata at screening |
| Metadata field | Title, abstract, keywords/index terms; avoid full-text-only retrieval |
| Research questions | A/F: transformer physical laws; B: EVSE; C: connected thermal field; D: power and mobility service; E: ODE/PDE/FVM/PINN validation |
| Search execution status | **Proposed query translations: not executed, not platform-debugged or search-hit verified** |

## Six scoping search blocks

| Block | Scope | Objective |
|---|---|---|
| A | Transformer thermal physics | SO1, SO2 |
| B | EVSE thermal physics and extreme heat | SO1, SO2, SO3 |
| C | Connected power–EVSE physical interdependencies | SO1, SO2, SO3 |
| D | Coupled dynamics and electricity–mobility service | SO1, SO3 |
| E | Physics-based and physics-informed thermal modeling | SO2 |
| F | Standards, loading limits and experimental validation | SO2 |

## SCOPUS ADVANCED SEARCH

**Limits:** Search year embedded, 2000–2026; export results as of 2026-11-05.

### A: Transformer thermal physics

```text
TITLE-ABS-KEY(("distribution transformer" OR "power transformer" OR "oil-immersed transformer") AND (thermal OR "top oil" OR "top-oil" OR hotspot OR "hot spot" OR "winding temperature" OR "thermal rating" OR "loss of life")) AND PUBYEAR AFT 1999 AND PUBYEAR BEF 2027
```

### B: EVSE thermal physics and extreme heat

```text
TITLE-ABS-KEY(("electric vehicle" OR EVSE OR "charging station" OR "fast charging" OR "DC charger") AND (thermal OR temperature OR derating OR cooling OR "ambient temperature" OR "power limit")) AND PUBYEAR AFT 1999 AND PUBYEAR BEF 2027
```

### C: Connected power–EVSE physical interdependencies

```text
TITLE-ABS-KEY(("electric vehicle" OR EVSE OR "charging station" OR "electric bus") AND (transformer OR feeder OR "distribution network") AND (measur* OR monitor* OR experiment* OR thermal OR derating)) AND PUBYEAR AFT 1999 AND PUBYEAR BEF 2027
```

### D: Coupled dynamics and electricity–mobility service

```text
TITLE-ABS-KEY(("power-transportation" OR "power transportation" OR "transportation-power" OR "transportation and electricity" OR "electric vehicle charging" OR "charging network") AND (resilien* OR recover* OR service OR "charging delay" OR "unserved energy" OR "power curtailment" OR "thermal limit" OR "dynamic coupling")) AND PUBYEAR AFT 1999 AND PUBYEAR BEF 2027
```

### E: Physics-based and physics-informed thermal modeling

```text
TITLE-ABS-KEY(("physics-informed" OR PINN OR "neural operator" OR "hybrid physics" OR "finite volume" OR "finite element" OR "heat equation" OR "reduced-order") AND (transformer OR "charging converter" OR "battery thermal" OR "electric vehicle battery") AND (thermal OR temperature OR heat OR "parameter identification")) AND PUBYEAR AFT 1999 AND PUBYEAR BEF 2027
```

### F: Standards, loading limits and experimental validation

```text
TITLE-ABS-KEY(("IEC 60076-7" OR "IEEE C57.91" OR "transformer loading guide" OR "thermal loading" OR "heat run" OR "thermal model") AND (transformer OR "charging station" OR "EV battery")) AND PUBYEAR AFT 1999 AND PUBYEAR BEF 2027
```

## WEB OF SCIENCE CORE COLLECTION ADVANCED SEARCH

**Limits:** Set Publication Years = 2000–2026 in interface; if necessary process in five-year ranges (2000–2004; 2005–2009; 2010–2014; 2015–2019; 2020–2024; 2025–2026) and combine with source IDs.

### A: Transformer thermal physics

```text
TS=(("distribution transformer" OR "power transformer" OR "oil-immersed transformer") AND (thermal OR "top oil" OR "top-oil" OR hotspot OR "hot spot" OR "winding temperature" OR "thermal rating" OR "loss of life"))
```

### B: EVSE thermal physics and extreme heat

```text
TS=(("electric vehicle" OR EVSE OR "charging station" OR "fast charging" OR "DC charger") AND (thermal OR temperature OR derating OR cooling OR "ambient temperature" OR "power limit"))
```

### C: Connected power–EVSE physical interdependencies

```text
TS=(("electric vehicle" OR EVSE OR "charging station" OR "electric bus") AND (transformer OR feeder OR "distribution network") AND (measur* OR monitor* OR experiment* OR thermal OR derating))
```

### D: Coupled dynamics and electricity–mobility service

```text
TS=(("power-transportation" OR "power transportation" OR "transportation-power" OR "transportation and electricity" OR "electric vehicle charging" OR "charging network") AND (resilien* OR recover* OR service OR "charging delay" OR "unserved energy" OR "power curtailment" OR "thermal limit" OR "dynamic coupling"))
```

### E: Physics-based and physics-informed thermal modeling

```text
TS=(("physics-informed" OR PINN OR "neural operator" OR "hybrid physics" OR "finite volume" OR "finite element" OR "heat equation" OR "reduced-order") AND (transformer OR "charging converter" OR "battery thermal" OR "electric vehicle battery") AND (thermal OR temperature OR heat OR "parameter identification"))
```

### F: Standards, loading limits and experimental validation

```text
TS=(("IEC 60076-7" OR "IEEE C57.91" OR "transformer loading guide" OR "thermal loading" OR "heat run" OR "thermal model") AND (transformer OR "charging station" OR "EV battery"))
```

## IEEE XPLORE COMMAND SEARCH

**Limits:** Select Metadata (not Full Text), Publication Years = 2000–2026 in refinements.

### A: Transformer thermal physics

```text
("distribution transformer" OR "power transformer" OR "oil-immersed transformer") AND (thermal OR "top oil" OR "top-oil" OR hotspot OR "hot spot" OR "winding temperature" OR "thermal rating" OR "loss of life")
```

### B: EVSE thermal physics and extreme heat

```text
("electric vehicle" OR EVSE OR "charging station" OR "fast charging" OR "DC charger") AND (thermal OR temperature OR derating OR cooling OR "ambient temperature" OR "power limit")
```

### C: Connected power–EVSE physical interdependencies

```text
("electric vehicle" OR EVSE OR "charging station" OR "electric bus") AND (transformer OR feeder OR "distribution network") AND (measur* OR monitor* OR experiment* OR thermal OR derating)
```

### D: Coupled dynamics and electricity–mobility service

```text
("power-transportation" OR "power transportation" OR "transportation-power" OR "transportation and electricity" OR "electric vehicle charging" OR "charging network") AND (resilien* OR recover* OR service OR "charging delay" OR "unserved energy" OR "power curtailment" OR "thermal limit" OR "dynamic coupling")
```

### E: Physics-based and physics-informed thermal modeling

```text
("physics-informed" OR PINN OR "neural operator" OR "hybrid physics" OR "finite volume" OR "finite element" OR "heat equation" OR "reduced-order") AND (transformer OR "charging converter" OR "battery thermal" OR "electric vehicle battery") AND (thermal OR temperature OR heat OR "parameter identification")
```

### F: Standards, loading limits and experimental validation

```text
("IEC 60076-7" OR "IEEE C57.91" OR "transformer loading guide" OR "thermal loading" OR "heat run" OR "thermal model") AND (transformer OR "charging station" OR "EV battery")
```

## ENGINEERING VILLAGE / COMPENDEX EXPERT SEARCH

**Limits:** Select Compendex only; set Date → Published → 2000–2026. WN KY = Subject/Title/Abstract/index terms, not controlled-terms only.

### A: Transformer thermal physics

```text
(("distribution transformer" OR "power transformer" OR "oil-immersed transformer") AND (thermal OR "top oil" OR "top-oil" OR hotspot OR "hot spot" OR "winding temperature" OR "thermal rating" OR "loss of life")) WN KY
```

### B: EVSE thermal physics and extreme heat

```text
(("electric vehicle" OR EVSE OR "charging station" OR "fast charging" OR "DC charger") AND (thermal OR temperature OR derating OR cooling OR "ambient temperature" OR "power limit")) WN KY
```

### C: Connected power–EVSE physical interdependencies

```text
(("electric vehicle" OR EVSE OR "charging station" OR "electric bus") AND (transformer OR feeder OR "distribution network") AND (measur* OR monitor* OR experiment* OR thermal OR derating)) WN KY
```

### D: Coupled dynamics and electricity–mobility service

```text
(("power-transportation" OR "power transportation" OR "transportation-power" OR "transportation and electricity" OR "electric vehicle charging" OR "charging network") AND (resilien* OR recover* OR service OR "charging delay" OR "unserved energy" OR "power curtailment" OR "thermal limit" OR "dynamic coupling")) WN KY
```

### E: Physics-based and physics-informed thermal modeling

```text
(("physics-informed" OR PINN OR "neural operator" OR "hybrid physics" OR "finite volume" OR "finite element" OR "heat equation" OR "reduced-order") AND (transformer OR "charging converter" OR "battery thermal" OR "electric vehicle battery") AND (thermal OR temperature OR heat OR "parameter identification")) WN KY
```

### F: Standards, loading limits and experimental validation

```text
(("IEC 60076-7" OR "IEEE C57.91" OR "transformer loading guide" OR "thermal loading" OR "heat run" OR "thermal model") AND (transformer OR "charging station" OR "EV battery")) WN KY
```

## Search-language, date and field sources

- ASU: https://libguides.asu.edu/evidence_synthesis/search-strategy
- MIT Libraries keyword/subject terms: https://libguides.mit.edu/c.php?g=175963&p=1160804
- Oxford Physics databases: https://libguides.bodleian.ox.ac.uk/physics/home
- Oxford postgraduate SLR planning: https://libguides.bodleian.ox.ac.uk/mastersSLR/plan
- Cambridge Engineering: https://libguides.cam.ac.uk/engineering/literature-searching
- Cambridge search methodology: https://libguides.cam.ac.uk/systematic-reviews/search-strategy
- Scopus field syntax: https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search
- Web of Science TS/PY: https://webofscience.zendesk.com/hc/en-us/articles/26916347018257-Web-of-Science-Core-Collection-Advanced-Search-Field-Tags
- IEEE help: https://ieeexplore-dev.ieee.org/Xplorehelp/downloads/user-guides/IEEE_Xplore_Searching_and_Saving_Searches.pdf
- Engineering Village WN KY: https://www.elsevier.support/engineering-village/answer/what-are-the-search-fields-in-the-compendex-database
- Engineering Village year/language filters: https://www.elsevier.support/engineering-village/answer/how-can-i-limit-searches-by-database
