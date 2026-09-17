# H1 Level 2 — Source and Provenance Register v1.1

**Retrieval audit date:** 2026-09-18  
**Purpose:** freeze the public lineage used by the Level-2 realistic synthetic spatial twin and distinguish source data, authoritative methods, calibration evidence, and thesis assumptions.  
**Machine manifest:** `config/source_manifest_v1.json`.

## S1 — SMART-DS Greensboro electrical distribution data

- Dataset: *SMART-DS Synthetic Electrical Network Data OpenDSS Models for SFO, GSO, and AUS*.
- Publisher: Open Energy Data Initiative / National Renewable Energy Laboratory.
- Landing page: https://data.openei.org/submissions/2981
- Role: realistic synthetic Greensboro electrical distribution topology, OpenDSS models and load-profile lineage.
- Status: `SOURCE_DATA_SYNTHETIC_NOT_OBSERVED_UTILITY_TOPOLOGY`.
- Boundary: synthetic assets must never be described as the actual Greensboro utility network.

## S2 — GreenEVT coupled Greensboro testbed

- Paper: Nilsson et al., *GreenEVT: Greensboro Electric Vehicle Testbed*.
- Paper: https://arxiv.org/abs/2305.12722
- Repository: https://github.com/GreenEVT/GreenEVT
- Upstream `main` audited at commit: `6aff1cac48869ccfa0183643979f5f04b04e1124`.
- Role: OpenDSS/SUMO co-simulation lineage, OSM-derived road network, and parcel/bus/road crosswalk workflow.
- Status: `SOURCE_TESTBED_METHODS_LINEAGE`.
- Boundary: GreenEVT spatial coupling does not convert SMART-DS into observed utility infrastructure.

## S3 — NOAA precipitation-frequency standard status

- Authority: NOAA/NWS Office of Water Prediction.
- Status page: https://water.noaa.gov/about/atlas15
- Audit finding on 2026-09-18: the page identifies NOAA Atlas 14 as the current precipitation-frequency standard and Atlas 15 as under development, with supersession occurring after publication/release.
- Level-2 rule: Atlas 14 is primary until a documented authoritative supersession and versioned protocol amendment. Atlas 15 preliminary estimates may be sensitivity inputs only.

## S4 — HEC-RAS 2D hydraulic modeling

- Authority: U.S. Army Corps of Engineers, Hydrologic Engineering Center.
- Documentation: https://www.hec.usace.army.mil/software/hec-ras/documentation.aspx
- Role: 2D rain-on-grid / spatial precipitation hydraulic modeling and solution-verification guidance.
- Status: `AUTHORITATIVE_METHOD_DOCUMENTATION`.

## S5 — Terrain, soil, land cover

### USGS 3DEP
- Source: https://data.usgs.gov/datacatalog/data/USGS:77ae0551-c61e-4979-aedd-d797abdcde0e
- Role: terrain/elevation input.

### USDA-NRCS SSURGO
- Source: https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo
- Role: soil-property evidence used to parameterize a declared HEC-RAS infiltration formulation.

### USGS NLCD 2021 v2.0 (June 2026)
- Source: https://www.usgs.gov/data/national-land-cover-database-nlcd-2021-products-ver-20-june-2026
- Role: land-cover/imperviousness evidence.

These sources are authoritative geospatial inputs. The transformation from those inputs into model parameters remains a thesis modeling step and must be documented separately.

## S6 — Road flood response evidence

- Pregnolato et al. (2017), *The impact of flooding on road transport: A depth-disruption function*.
- DOI: https://doi.org/10.1016/j.trd.2017.06.020
- Role: candidate empirical depth-speed relation, restricted to its documented validity domain.
- Boundary: the function is not to be extrapolated automatically to all flood depths, road classes, or crew-vehicle classes.

- FHWA road-weather/flood safety guidance: https://ops.fhwa.dot.gov/publications/fhwahop16093/ch4.htm
- Role: safety/closure evidence; exact operational threshold remains a parameter to be qualified and frozen.

## S7 — Flood impact on electrical equipment

- FEMA Hazus resource: https://www.fema.gov/flood-maps/tools-resources/flood-map-products/hazus
- Role: authoritative starting evidence for flood vulnerability/functionality of relevant ground-level electrical facilities.
- Boundary: flood depth alone must not be used as an overhead-line failure mechanism.

## S8 — Modeling, verification and uncertainty guidance

### NASA-HDBK-7009B
- Source: https://standards.nasa.gov/standard/NASA/NASA-HDBK-7009
- Document date: 2026-02-03; active at the source audit date.
- Role: model/simulation credibility and V&V practice.

### JCGM 101:2008
- Source: https://www.bipm.org/en/doi/10.59161/jcgm101-2008
- Role: propagation of input probability distributions through mathematical models using Monte Carlo methods.

### SALib Sobol implementation
- Source: https://salib.readthedocs.io/en/main/api/SALib.sample.html
- Role: implementation rule for scrambled Sobol sampling; with `calc_second_order=False`, the design requires `N(D+2)` model evaluations.
- Boundary: software documentation determines implementation mechanics, not the scientific admissibility of the chosen uncertainty model.

## Provenance/evidence semantics

Every Level-2 dependency follows the canonical thesis epistemic object `Pi_e=(P_e,V_e,U_e)`. Parameter/source records additionally use one of:

```text
DATASET
AUTHORITATIVE_EXTERNAL
PEER_REVIEWED_CALIBRATION
UNCERTAIN_PRIOR
EXPLICIT_ASSUMPTION
```

and dependency evidence states must remain compatible with the canonical contract, including:

```text
EVIDENCE_SUPPORTED
MEASURED
CALIBRATED
HYPOTHESIZED
INFERRED_PENDING_VERIFICATION
REJECTED
UNKNOWN_UNOBSERVED
```

No inferred/synthetic input may be reported as an observed Greensboro value. No Level-2 model difference may be called predictive improvement without an independent qualified reference and frozen comparison metric.
