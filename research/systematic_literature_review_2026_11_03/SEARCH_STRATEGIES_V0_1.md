# Search protocol and first exploratory search — 2026-11-03

**Version:** 0.1. Search strategies below are **draft database translations, NOT YET EXECUTED** on Scopus, Web of Science or IEEE Xplore. Do not assign results counts or PRISMA coverage to them. All dates in this document are YYYY-MM-DD.

## A. Search streams and conceptual blocks

1. **Transformer thermo-physics**: (`power transformer`, `distribution transformer`, oil immersed, transformer winding) AND (thermal, hot spot, top oil, thermal inertia, thermal rating) AND (experiment, sensor, field, numerical validation, identifiability).
2. **EVSE thermo-physics**: (EVSE, EV fast charger, DC fast charging) AND (thermal, rectifier, heatsink, cooling, derating, temperature, extreme heat) AND (measured, laboratory, field, operational power, performance).
3. **Coupled power-to-transportation interfaces**: (electric vehicle charging, electrified transport) AND (distribution network, distribution transformer, power system) AND (temperature, thermal, overloading, dynamic thermal rating, resilience) AND (time, dynamics, service, constraints).
4. **Mathematical validation**: (transformer, EVSE, charger) AND (thermal) AND (physics based, physics informed, dynamic differential equation, identifiability, uncertainty, parameter estimation, external validation).
5. **Secondary diagnostic sweep**: (electric vehicle charging) AND (thermal derating, transformer overload, extreme heat) with citation chasing from included studies, to catch cross-stream papers.

## B. Draft Scopus strategies (not executed)

Run each separately in **Scopus Advanced Search** and export retrieved DOI/title/abstract/bibliography and exact result count:

### SCOPUS-A
```
TITLE-ABS-KEY(
  ("power transformer" OR "distribution transformer" OR "oil-immersed transformer" OR "transformer winding")
  AND
  ("thermal model*" OR "thermal dynamic*" OR "top oil" OR "top-oil" OR "hot spot" OR "hot-spot" OR "dynamic thermal rating")
  AND
  (measurement* OR experiment* OR field OR validation OR identifiab*)
)
```

### SCOPUS-B
```
TITLE-ABS-KEY(
  ("electric vehicle charger" OR "EV charger" OR EVSE OR "DC fast charg*" OR "fast charging station")
  AND
  (thermal OR "rectifier temperature" OR "heat sink" OR heatsink OR cooling OR derat* OR heatwave OR "extreme heat")
  AND
  (experiment* OR measurement* OR "field test*" OR "charging power" OR performance)
)
```

### SCOPUS-C
```
TITLE-ABS-KEY(
  ("electric vehicle charg*" OR "electrified transportation" OR "electrified transport")
  AND
  ("distribution transformer" OR "distribution network" OR "power grid" OR "power system")
  AND
  (thermal OR "hot-spot" OR "dynamic thermal rating" OR overheating OR overload* OR "heat stress")
  AND
  (dynamic* OR resilience OR service OR constrain* OR charging)
)
```

### SCOPUS-D
```
TITLE-ABS-KEY(
  (transformer OR "EV charger" OR EVSE OR "battery thermal")
  AND
  (thermal OR temperature)
  AND
  ("physics-informed" OR "physics informed" OR PINN OR "thermal RC" OR "state space" OR "differential equation" OR identifiab* OR "uncertainty quantification" OR "parameter estimation" OR "out of distribution")
)
```

**Provisional syntax:** Scopus wildcard and quoted phrases should be tested and copied exactly from the platform after execution. No promise that untested queries are syntactically valid in a particular current user interface.

## C. Draft Web of Science Core Collection translations (not executed)

Use Web of Science Advanced Search on one stream at a time. Example translation for Stream C; replace the inner conceptual blocks for A, B, D based on Scopus formulas:

```
TS=(("electric vehicle charging" OR "EV charging" OR "electrified transportation")
AND ("distribution transformer" OR "distribution network" OR "power system")
AND (thermal OR "hot spot" OR "dynamic thermal rating" OR overload OR overheating)
AND (dynamic* OR resilience OR service OR constraints))
```

**Execute and log**: database edition(s), platform, date, original query exactly, field filters, raw records and export hash. Do not claim all fields or the same wildcard behavior as Scopus without validating them.

## D. IEEE Xplore and additional source search (not executed)

IEEE Xplore may require its own boolean/grouping and field selector. Independently search four equivalent streams in **All Metadata**, verify phrase syntax with the current platform, and export all candidates; do not paste Scopus's `TITLE-ABS-KEY` unmodified. Save the exact query run. Scholarly search expansion: IET/Wiley, ScienceDirect, Springer, OSF/Zenodo dataset article search, Crossref/OpenAlex DOI enrichment and forward/backward citation searching. Tag every supplementary route and avoid treating a web top-results list as full bibliographic export.

## E. Public-web exploratory queries ACTUALLY executed today

Public-web search is a **pilot / seed-discovery** stage. The following are literal search strings submitted on 2026-11-03; the interface did not supply stable exhaustive hit/export counts. They do **NOT** constitute a PRISMA database search or formal screened corpus.

```text
PRISMA 2020 statement checklist flow diagram official BMJ 2021
PRISMA-S extension reporting literature searches systematic reviews 2021 full search strategies
systematic review transformer thermal models EV charging heat extreme weather measured datasets field 2024 2025 2026
IEEE C57.91 2025 guide loading mineral oil transformers thermal
"power transformer" "electric vehicle charging" "thermal" measured field study
"EV fast charger" "ambient temperature" "rectifier" "derating" experiment 2026
"distribution transformer" "EV charging" "hot-spot" "dynamic thermal rating" field measurements
"physics informed" "transformer" thermal parameter identification oil temperature experimentally validated
"electric vehicle charging" "temperature" "charging power" "resilience" heat wave dynamic thermal
```

Several results were then checked against original publisher pages, including [Qatar charger field study](https://doi.org/10.1016/j.ecmx.2026.101960), [Bragone et al. transformer PINN](https://doi.org/10.1016/j.epsr.2022.108447), [Zakaria et al. EV dynamic rating](https://doi.org/10.1049/gtd2.13025), [Ahmed et al. review](https://doi.org/10.1016/j.apenergy.2025.126961), [Qian et al. transformer ageing](https://doi.org/10.1016/j.ijepes.2014.09.040), [IEEE 2022 transformer PINN conference](https://doi.org/10.1109/ICMLA55696.2022.00215), [2025 transformer RBA-PINN](https://doi.org/10.1016/j.engappai.2024.109556). These are **candidate records** and citation-mining seeds, not systematically included studies.

## F. Search reproducibility log

Use [SEARCH_EXECUTION_LOG.csv](./SEARCH_EXECUTION_LOG.csv). Require `query_id,source_platform,source_collection,date_time_timezone,exact_query,filters,actual_executed,raw_hit_count,export_sha256,export_location,limitations`. Unknown hit counts remain empty rather than `0`. Record missing access explicitly. Every query change increments a version and requires date/reason.

## G. Calibration before bulk screening

Test search *recall* against seed records: full-record, direct Qatar EVSE thermal paper (B); transformer PINN (A/D); physically modelled EV-to-transformer ageing paper (C); Zakaria EV dynamic ratings (C); Raue profile likelihood (D). If missing, document why and revise **before locking strategy**, not after inspecting desirable results. Check false positives such as "transformer" meaning neural network or unrelated transformer imaging, and pure EV battery thermal reviews without charger/grid interface.

## H. Review coverage status as of today

| Source | Search | Export | Screening |
|---|---|---|---|
| Public web engine | 9 exploratory query strings above executed | Not an exhaustive result export | Seed triage only |
| Scopus | NOT RUN | None | None |
| Web of Science Core Collection | NOT RUN | None | None |
| IEEE Xplore systematic query | NOT RUN | None | None |
| Other structured indexes, citation chains | NOT RUN systematically | None | None |

No PRISMA flow quantities (identified, deduplicated, excluded, full-text included) are declared until they are actually measured and reconciled.
