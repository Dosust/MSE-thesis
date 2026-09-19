# Stage 5 Numerical / Empirical Closure Campaign — Execution Status v1

**Date:** 2026-09-19  
**Authority:** frozen Stage-5 scientific design/protocol v1  
**Rule:** case data/results instantiate the frozen design; they do not redefine canonical governance.  
**Current verdict:** `MAXIMUM_VALID_EXECUTION_REACHED_IN_CURRENT_RUNTIME — STAGE 5 NOT SCIENTIFICALLY CLOSED`.

## 1. Executed work

### B0 mathematical reference verification — PASS

A two-state bounded-control viability/recovery problem with closed-form reference sets was executed. Time-refinement errors converge with approximately first-order behavior, and the spatial set representation remains inside its geometric resolution bound. See `B0/`.

This follows the frozen requirement that low-dimensional references precede high-dimensional approximations. Viability methods face dimensionality limitations, so reference problems are needed to separate numerical error from model/projection error (Maidens et al., 2013, https://doi.org/10.1016/j.automatica.2013.03.020). Formal abstraction literature likewise requires quantified precision before safety/reachability properties are transferred between models (Girard & Pappas, 2007, https://doi.org/10.1016/j.automatica.2007.01.019).

### B2a synthetic fixture — independently rerun

The benchmark-only M0/M1/M2 fixture was rerun under the preregistered research profile:

[
	heta_P=	heta_T=0.90,qquad
	heta_{rec}=0.95,qquad
Delta t_{hold}=0.25;h,qquad
t_{evt}=0.75;h.
]

| Model | min S_P | min S_T | max queue [veh] | first exit [h] | recovery from event [h] | time outside K [h] |
|---|---:|---:|---:|---:|---:|---:|
| M0 | 0.594023 | 0.575000 | 0 | 0.90000 | 2.10000 | 1.70750 |
| M1 | 0.563869 | 0.448500 | 0 | 0.90000 | 2.10000 | 1.70750 |
| M2 | 0.563869 | 0.448500 | 4.187162 | 0.75375 | 6.47125 | 6.46625 |

Structural falsification checks pass exactly:

- service bounds: PASS;
- queue non-negativity: PASS;
- decoupling limit: max service error = 0;
- M2→M1 when memory and dynamic repair are suppressed: max service error = 0.

This remains `SYNTHETIC VERIFICATION ONLY`. It is not the source-backed B2 benchmark, not B3, and not H3 evidence.

## 2. Upstream scientific audit

### Stage 3

The current case-specific causal authority admits only Q05:

[
mathcal A_v(t)ightarrow N_{EV,b}^{chg}(t)ightarrow P_b^{new}(t).
]

GreenEVT couples SUMO transportation simulation and OpenDSS distribution simulation through EV charging (Nilsson et al., 2023, https://doi.org/10.1109/JSYST.2023.3343692). OpenDSS supports sequential/QSTS distribution studies; SUMO is a microscopic time-discrete traffic simulator.

The Stage-3 register still has unresolved final model/state/case gates, including model class/state space, synchronization, parameter credibility, uncertainty, numerical verification, V&V, QOI freeze and the matched H1 experiment. A failed prerequisite means `NOT TESTED`, not hypothesis falsification.

### Stage 4

Current Stage-4 status remains:

- `G4-CON = PASS`;
- `G4-CASE = BLOCKED`;
- `G4-V = BLOCKED`;
- `G4-H2 = BLOCKED / NOT TESTED`;
- `G4→5 = BLOCKED`.

Therefore a final-case (mathcal U_{feas}(t)), observation/estimation model and information/organizational realization are not available for B3 controlled viability/reachability.

## 3. Source-backed B2 acquisition audit

The public GreenEVT repository uses Git LFS. Required entries resolve to pointer files rather than materialized data in this runtime:

- `data/UDS.db`: LFS SHA-256 `74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724`, declared size 107,778,048 bytes;
- `data/sumo_network/greensboro.net.xml`: LFS SHA-256 `f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06`, declared size 351,967,227 bytes.

The execution runtime has no `git-lfs`, no installed SUMO/OpenDSS Python backends, and no external DNS/network access from the container. Treating LFS pointers as source data would violate provenance.

[
oxed{B_2^{source-backed}=mathrm{BLOCKED_BY_MATERIALIZATION}}
]

The GreenEVT source also contains workflow-specific EV charging defaults of 7.5 kW (`custom_workflow.py`) and 7.2 kW (`interactive_simulator.py`). They are workflow defaults, not a universal physical standard; no B3 value is inferred from this conflict.

## 4. Social, economic and environmental rigor

NIST's Community Resilience Planning Guide links infrastructure performance to social/economic functions and community-defined performance goals (McAllister, 2015, https://doi.org/10.6028/NIST.SP.1190v1; NIST, 2020, https://doi.org/10.6028/NIST.SP.1190GB-16). Resilience-curve literature also shows that performance measures and targets are consequential and stakeholder-dependent (Poulin & Kane, 2021, https://doi.org/10.1016/j.ress.2021.107926).

Therefore:

[
oxed{	ext{technical service}
eq	ext{social consequence}
eq	ext{environmental consequence}}
]

and these quantities must not be silently collapsed into one weighted score.

For the final case, social rigor requires disaggregated service reporting where data support it (e.g. critical-function power service and transport accessibility/travel-time consequences for declared beneficiary/OD groups). Environmental quantities such as energy use, emissions and carbon are tracked explicitly and passed to Stage 6 unless independently justified Stage-5 requirements make them constraints. This avoids assuming that resilience improvement automatically implies sustainability improvement; infrastructure studies document resilience–sustainability–CO2 trade-offs (Liu et al., 2024, https://doi.org/10.1016/j.scs.2024.105647).

## 5. Updated closure status

| Gate | Executed status | Reason |
|---|---|---|
| G5-CON | PASS | frozen constitution |
| G5-LIT | PASS-DEVELOPMENTAL | evidence architecture exists |
| G5-REQ | PARTIAL | research profile frozen; B3 hard constraints/control/case binding incomplete |
| G5-RM | PARTIAL | projection constitution + B2a memory pilot executed; B3 fidelity blocked |
| G5-MATH | PASS-CONSTITUTION + B0 VERIFIED | analytic/numerical reference executed |
| G5-UQ | PARTIAL / BLOCKED-B3 | final distributions/bounds not case-bound |
| G5-VIA | PASS-B0 / BLOCKED-B3 | B0 viable set verified; no qualified B3 set |
| G5-REA | PASS-B0 / BLOCKED-B3 | B0 recovery set verified; no qualified B3 set |
| G5-BENCH | PARTIAL | B0 executed; B1 needs final constituent binding; source-backed B2 not materialized; B3 blocked |
| G5-VVUQ | PARTIAL | B0 time/grid verification passed; no B3 full-model/probability validation |
| G5-H3 | NOT TESTED | A0–A4 blocked before B3/VVUQ closure |
| G5-DIAG | PASS-SCHEMA / RESULTS BLOCKED | no qualified B3 V/R result |
| G5-PROV | PASS | hashes and blockers recorded |
| G5-CLAIM | PASS | claim ceiling preserved |

## 6. Why Stage 5 is not yet closed

The remaining B3 prerequisites include:

[
Y^{phys},quad F_{mathcal G}^{m},quad
mathcal U_{feas},quad
F_{unsafe}^{B3},quad
mathbb U_5^{B3},quad
	ext{qualified source-backed case data}.
]

Without them, a defensible final-case (mathcal V,mathcal R,P_{viable},P_{recover}) and the confirmatory (A_0)–(A_4) comparison cannot be executed. Creating substitutes after benchmark outcomes would violate the frozen preregistration.

## 7. Exact external unblock package

To continue without redesign, materialize/provide:

1. GreenEVT Git-LFS objects required by the Level-2 acquisition script;
2. executable SUMO and OpenDSS/OpenDSSDirect environment, or qualified precomputed outputs with hashes;
3. final Stage-3 case/model/state/QOI binding;
4. final Stage-4 observation/uncertainty/organization/control-feasibility handoff;
5. authoritative or explicitly preregistered B3 hard constraints and scenario manifest.

Then the frozen chain is:

[
oxed{
B_1ightarrow B_2ightarrow B_3
ightarrow(mathcal V,mathcal R)
ightarrow VVUQ
ightarrow A_0{:}A_4
ightarrow H3
ightarrow I_{5	o6}.
}
]

## 8. Current conclusion

[
oxed{	ext{Stage-5 numerical verification advanced; empirical/scientific closure is NOT YET PASS.}}
]

This is a blocking-data/upstream-model result, not a negative H3 result.
