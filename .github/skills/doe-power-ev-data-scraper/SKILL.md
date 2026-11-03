---
name: doe-power-ev-data-scraper
version: 1.0.0
purpose: Evidence-governed discovery, HTTP testing, and bounded acquisition of original public Power–Electrified Transportation research files.
---

# DOE Power–Electrified Transportation: Original Field Data Scraper

## Activate
When the research task asks to locate, download, qualify, or update original transformer/feeder/EVSE/EV/battery datasets from the U.S. DOE, ORNL, EERE, OEDI or related primary scientific repositories. Supports **SO1** directly, and SO2/SO3 only when subsequent evidence supports them. This is **not** permission to declare field validation.

## Mandatory authority (read each before claiming scientific conclusions)
1. `project/CANONICAL_THESIS_TITLE_V3.md` — **Engineering of Power–Electrified Transportation Interdependencies for Resilience** (title only, effective 2026-10-15).
2. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
3. `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`
4. `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`
5. `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`
6. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`
7. `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`
8. `project/AUTONOMOUS_EXECUTION_PROTOCOL_V1.md`

If any file cannot be inspected, record an authority-read blocker and do not override its known frozen requirements.

## Scientific scope
Extreme heat → thermal physical states → temperature-dependent capability/constraint → independently qualified directional `P → T_e` or `T_e → P` effect → state/time → electricity/mobility service consequence.
The complete Electrified Transportation System includes vehicle, RESS/battery, propulsion/auxiliary equipment, vehicle power circuit, EVSE, connection, and required charging communication/control; a charger case is only a bounded application. Shared hot weather or a physical AC connection is **not** proof of directed thermal dependency.

## Working methods: LEARN → VERIFY → FORMULATE → DERIVE → TEST → VALIDATE
**S1 Discovery**: use original publisher/repository metadata APIs, explicit dataset pages and hyperlinks, never scraped snippets alone. Record DOI/title, equipment, sensing boundary and exact original URL. DOE's overview is a **gateway**, not an experimental dataset.
**S2 Secure HTTP verification**: allowlisted HTTPS hosts, explicit requests/redirect checks, bounded attempts and stream sizes; never bypass authentication or robots or generate inferred download URLs. Only generate canonical Opendatasoft `/files/{id}` routes when `{id}` is actually present in an API record. Dropbox/restricted links remain review/access leads.
**S3 Acquire**: download only declared public files ≤5 MiB by default, or deliberately amend the bound. Save untouched originals; compute SHA-256; verify repository MD5 or SHA-256 when published; never silently overwrite files.
**S4 Validate format**: reject HTML login/error pages, retain published units, time axes, missing values and quality flags; inspect actual CSV headers and original field descriptions before naming measured channels.
**S5 Qualify physics**: distinguish measured field observations, controlled laboratory measurements, hardware-in-loop/synthetic testbed data, topology models, metadata indexes and published documentation. Require same asset identifiers, feeder/bus/transformer connection, synchronized timestamps and thermal sensors for connected thermal-field validation.
**S6 Record unresolved evidence**: no matching transformer or EVSE temperature, missing operational interventions, separate installations, mismatch of metering boundary, missing sensor placement → `OPEN` or `BLOCKED_EVIDENCE`. Do not compose a synthetic substitute and label it measured.
**S7 Reproduce**: save link audit, HTTP log, original checksums, source API IDs, source-page citation, script version/commit, downloaded paths, block reasons, run date, and unmodified files.

## Official target sources
- DOE OE overview: `https://www.energy.gov/oe/power-system-data-analytics` — methodology/gateway, not itself a downloadable thermal field dataset.
- ORNL OpenEnergyDataPortal: `doe-ev-data-collection-charging-data` (DOI `10.15483/1989855`; EVSE, vehicle or utility submeter data; 35 files claimed by metadata; sensor origin varies).
- Iowa Distribution Test Systems (ORNL catalog and author site `https://wzy.ece.iastate.edu/testsystem.html`): real feeder topology, secondary-transformer-aggregated meter readings; no established EVSE or transformer temperatures.
- ORNL CODAS EV Energy Router: CHIL/control testbed; **not connected measured field thermal evidence**.
- TU Dortmund high-resolution synchronized EV charger/grid laboratory dataset (`10.5281/zenodo.14065331`): small metadata indexes `measurements.csv` / `parameters.csv` and larger raw/merged archives; same laboratory electrical measurements, not transformer thermal data.
- SINTEF transformer thermal component observations (`10.5281/zenodo.17223516`): not from the same installation as the charger data.
- KIT multivoltage electrical recordings (`10.5281/zenodo.22826984`): electrical network and sensor mapping need source-level verification.

## Execution
```bash
python -m pip install requests
python -m unittest discover -s .github/skills/doe-power-ev-data-scraper/tests -v
python .github/skills/doe-power-ev-data-scraper/scripts/doe_scraper.py \
  --out doe_scraper_output --download-small --max-file-mb 5 --max-files 8 --max-api-calls 70
```
May execute in Colab, local environment with network, or GitHub Actions. If network is unavailable, do not claim the HTTP steps passed; use the CI run's actual results.

## Required outputs
- `file_candidates.csv`: original metadata-based file URLs, source class, DOI, file type, declared checksum/size and test/download status.
- `http_search_log.csv`: API/page fetches and specific errors, including access blockers.
- `original_downloads/`: untouched source files, not edited or synthesized.
- `run_summary.json`: number of attempted requests, links and actual successful downloads, scientific validation barrier.

## Admission gates
- `G0` frozen title/scope loaded.
- `G1` source/DOI confirmed from primary metadata.
- `G2` exact original file URL obtained and HTTP-tested.
- `G3` original retrieved within allowed access/cost/size.
- `G4` integrity and format verified; preservation proven.
- `G5` measured variables/units/timestamps/quality audited from contents.
- `G6` asset topology and shared installation confirmed.
- `G7` comparable synchronized thermal channels and directional mechanism qualified.
- `G8` calibrated mathematical model independently validated.
- `G9` service consequences and uncertainty evaluated within validity domain.

Do not upgrade a downstream gate because an upstream step produced CSV files. Output `PASS`, `FAIL`, `OPEN`, or `BLOCKED_ACCESS` for each claim.

## Next experiments
1. Audit raw DOE EV data filenames, headers and sensor origins when publicly downloadable.
2. Inspect Iowa feeder OpenDSS topology and transformer-aggregated meters; verify if it identifies EVSE (unknown).
3. Inspect high-resolution TU Dortmund grid/charger measurement indices, identify actual temperature sensors and their role, and request full data only when needed and within download bounds.
4. Continue independent SINTEF transformer calibration (separate installation).
5. Contact principal investigators only when data need an authorized request. Never describe separate-site data as physically connected measurements.
