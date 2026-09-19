# Authoritative Source Catalog V1

This catalog records candidate/identified authoritative sources and their **permitted thesis roles**. Admission into an experiment still requires `G_RW=PASS`.

| Source | Authority | Intended role | Explicit limitation |
|---|---|---|---|
| Greensboro City GIS traffic-signal/infrastructure layers | OFFICIAL | Stage-1 T structure; signal/intersection locations | does not establish P→T causal dependency |
| NCDOT traffic data / continuous counts | OFFICIAL | T operation, volume, calibration/validation | coverage and sampling must be checked per station |
| NCDOT TIMS incident APIs | OFFICIAL | event/disruption forcing and validation | incident record ≠ traffic-state trajectory by itself |
| GreenEVT | PROJECT_SOURCE / RESEARCH_DATASET | coupled development/benchmark case | realistic-synthetic grid ≠ observed utility feeder |
| SMART-DS | RESEARCH_DATASET | source-backed synthetic distribution-system structure/operation | synthetic benchmark, not utility ground truth |
| DOE AFDC | OFFICIAL | charging-station location/configuration/interface evidence | station inventory/status ≠ charging-session demand |
| Joint Office charging-data/API guidance | OFFICIAL | interface semantics / status/data fields | protocol guidance ≠ observed case behavior |
| NREL workplace charging dataset | RESEARCH_DATASET | external empirical charging calibration/distributions | external case, not Greensboro/Austin validation |
| EIA Hourly Electric Grid Monitor | OFFICIAL | regional power operation/boundary conditions | balancing-area operation ≠ feeder state |
| EIA-861 | OFFICIAL | utility reliability/AMI/service-territory evidence | annual/system metrics ≠ event trajectory |
| ERCOT operational/historical data | OFFICIAL | Texas system boundary/plausibility/event context | ERCOT system state ≠ Austin feeder state |
| Austin Energy reports/AARs | OFFICIAL | utility reliability, outage, restoration, organizational evidence | system/event reports may not expose feeder/SCADA truth |
| Austin traffic incidents/open data | OFFICIAL | transportation incident/event evidence | active incident snapshots ≠ complete crash ground truth |
| Austin TPW / Mobility Management / emergency plans | OFFICIAL | Stage-4 organization, roles, signal/road response | narrative/plan evidence ≠ measured latency unless stated |
| NOAA/NWS/NCEI | OFFICIAL | observed hazard forcing | station/radar support and interpolation must be explicit |
| DOE-417 | OFFICIAL | major electric disturbance timing/extent | major-event record ≠ distribution dynamic trajectory |
| NIST Community Resilience Planning Guide | OFFICIAL GUIDANCE | service/recovery-goal methodology | does not provide case-specific numerical threshold |
| Census LODES | OFFICIAL | jobs/OD/opportunity/accessibility reality | employment access ≠ full social equity |
| EPA eGRID / GHG factors | OFFICIAL | electricity carbon factors | factor choice must match geography/time/accounting role |
| NIST EDGe$ | OFFICIAL GUIDANCE | economic comparison methodology | methodology ≠ actual intervention cost |
| ISO/IEC/IEEE 15288:2023 | STANDARD | life-cycle/process traceability | process authority, not physical/causal evidence |
| ISO/IEC/IEEE 24641:2023 | STANDARD | model relationship/governance | process/model governance, not case validation |
| ASME VVUQ portfolio | STANDARD/GUIDANCE | model credibility, verification/validation/UQ | does not validate thesis models automatically |

## Key URLs

- Greensboro GIS traffic signal layer: https://gis.greensboro-nc.gov/arcgis/rest/services/GISDivision/ContactCenterOperations2_MS/MapServer/3
- NCDOT traffic data: https://connect.ncdot.gov/resources/safety/Pages/Traffic-Data.aspx
- NCDOT TIMS APIs: https://tims.ncdot.gov/tims/V2/webservices
- GreenEVT: https://github.com/greenevt/greenevt
- NREL workplace charging: https://data.nrel.gov/submissions/182
- AFDC networks: https://afdc.energy.gov/stations/charging-networks
- Joint Office interoperability: https://driveelectric.gov/software-interoperability
- EIA open data: https://www.eia.gov/opendata/
- EIA-861: https://www.eia.gov/electricity/data/eia861/
- ERCOT current system conditions: https://www.ercot.com/gridinfo/csc
- Austin Energy reports: https://austinenergy.com/about/reports
- Austin traffic report/open data: https://data.austintexas.gov/stories/s/Austin-Travis-County-Traffic-Report-Page/9qfg-4swh/
- NIST community resilience: https://www.nist.gov/community-resilience/planning-guide
- Census LODES: https://lehd.ces.census.gov/data/lehd-code-samples/sections/lodes.html
- EPA eGRID: https://www.epa.gov/egrid
- NIST EDGe$: https://www.nist.gov/services-resources/software/edge-economic-decision-guide-software-online-tool
- ISO 15288: https://www.iso.org/standard/81702.html
- ISO 24641: https://www.iso.org/standard/79111.html
- ASME VVUQ: https://www.asme.org/codes-standards/vvuq-standards
