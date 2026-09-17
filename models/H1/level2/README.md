# H1 Level 2 — Realistic Synthetic Spatial Twin

**Status:** `LEVEL2_REALISTIC_SYNTHETIC_TWIN`  
**Scientific role:** spatially realistic mechanism testbed for H1; not observational validation.  
**System:** coupled electric power + road transportation, Greensboro, North Carolina lineage.

## Scientific contract

Level 2 binds the verified H1 comparators to a realistic synthetic spatial lineage:

\[
\text{SMART-DS/OpenDSS (GSO)} + \text{OSM/SUMO (Greensboro)}
\rightarrow \text{GreenEVT crosswalk}
\rightarrow \{M_0,M_1,M_2\}.
\]

The public SMART-DS data are synthetic distribution networks designed for realistic testing. GreenEVT couples the Greensboro SMART-DS distribution system to an OpenStreetMap-derived SUMO network through parcel/bus/road associations. Therefore this level supports computational and mechanistic claims on a realistic synthetic infrastructure, but it does **not** establish predictive superiority against observations or describe the actual Greensboro utility network.

## Comparator definitions

- **M0 — independent:** power and transportation are solved with no P↔T feedback.
- **M1 — static/algebraic:** charger demand maps T→P and same-step charger availability maps P→T, but the interface has no memory.
- **M2 — dynamic causal:** charger backlog and state-dependent repair-access progress are explicit states.

The admissible comparison is matched:

\[
\Omega_H,\;Y_0,\;u,\;\eta,\;\theta_{shared}
\quad\text{held fixed across}\quad M_0,M_1,M_2.
\]

## Data lineage

The realistic mode expects a checked-out GreenEVT repository with Git-LFS materialized. Required artifacts are:

- `data/open_dss/Master.dss`
- `data/open_dss/bus_info.csv`
- `data/open_dss/Long_lat_buscoords.txt`
- `data/sumo_network/greensboro.net.xml`
- `data/sumo_network/greensboro.sumocfg`
- `data/UDS.db`

`UDS.db` must expose the GreenEVT crosswalk fields used by the upstream project, including `buses(id,long,lat,sumo_edge,...)` and `parcels(...,bus_id,sumo_edge,...)`.

## Workflow

```text
Acquire -> Audit -> Crosswalk audit -> Reduced spatial case -> M0/M1/M2 -> gates -> UQ/sensitivity
```

Commands:

```bash
python acquire_level2.py --dest external/GreenEVT
python audit_inputs.py --greenevt external/GreenEVT --out input_audit.json
python build_reduced_case.py --greenevt external/GreenEVT --out case_bundle.json
python run_level2.py --case case_bundle.json --out results.json
```

A deterministic `--preview` mode exists only to verify the Level-2 plumbing without the large Git-LFS data:

```bash
python build_reduced_case.py --preview --out preview_case.json
python run_level2.py --case preview_case.json --out preview_results.json
```

`preview` is a software verification fixture, **not** a thesis result.

## Mandatory gates

A realistic run is admissible only if all gates pass:

1. provenance files exist and Git-LFS pointers are fully materialized;
2. `UDS.db` contains buses and parcels with the expected crosswalk fields;
3. no selected bus has a missing road-edge crosswalk;
4. no selected parcel has a missing bus or road-edge crosswalk;
5. selected SUMO edges exist in the Greensboro network;
6. every model uses the same reduced case, disturbance realization, time grid and shared parameters;
7. M2 reduces to M1 when memory and dynamic repair are disabled;
8. outputs label all non-source hazard, repair, charging and uncertainty values as synthetic/sensitivity inputs.

## Interpretation boundary

Level 2 may establish that a mechanism produces reproducible differences among M0/M1/M2 on realistic synthetic spatial infrastructure. It cannot establish H1b predictive superiority against observed events. That requires Level 3 observational/held-out validation.
