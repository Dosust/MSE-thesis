# Primary-source reading batch 01 — thermal Power–Electrified Transportation (5 November 2026)

**Status:** Executed targeted paper-reading and evidence extraction. **NOT** a completed systematic evidence map, PRISMA study inclusion, independent reviewer, model replication, or frozen mathematics. Append-only to the existing research.  
**Working branch:** `user-data-qualification-2026-11-03`  
**Governing scope:** frozen GO/SO1–SO3, extreme-heat thermal mechanisms only; state ≠ capability ≠ service ≠ resilience.  
**Source paths:** `project/systematic_literature_review/EXTRACTION_BRAGONE_ACKER_DAY01_2026-11-03.md` and `FULLTEXT_MATHEMATICAL_EVIDENCE_MATRIX_V01.csv` reused, not overwritten.

## A. Source-first results and access restrictions

| ID | Literature work and source | Original access in this pass | Distinct evidence | Excluded claims / next gate |
|---|---|---|---|---|
| RB01 | Fletcher & Khan (2025), RACE for 2030 report [original Part 1 PDF](https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf) | **Full technical-report searchable text reviewed in selected original sections**; original PDF screenshot requested but returned cache miss; figures visually unverified | IEC-related transformer thermal state-time model with modeled EV charging load and simulated thermal control / energy delivered | **F5 numerical/scenario**, not observed same-site connected transformer–EVSE thermal field validation. Part 2 longitudinal two-transformer tests planned in the source; no independent new Part 2 report found in this pass |
| RB02 | Bragone et al. (2022), DOI [10.1016/j.epsr.2022.108447](https://doi.org/10.1016/j.epsr.2022.108447); [KTH publication PDF](https://www.diva-portal.org/smash/get/diva2%3A1683236/FULLTEXT01.pdf) | **Full journal-method/results searchable PDF text**, prior GitHub detailed extraction reused; PDF screenshot request cache miss, so figure visual audit open | One-dimensional heat PDE, measured transformer ambient/loading/top-oil boundary, PINN vs FVM numerical comparison | **F3 input measurements + F5 numerical distribution**; not independent spatial field ground truth or unobserved top-oil forecasting |
| RB03 | Acker, Hofmann & Konrad (online 2025; volume 2026), DOI [10.1007/s41104-025-00157-7](https://doi.org/10.1007/s41104-025-00157-7) | **Original publisher full-text HTML sections 2–4**, checked against already extracted GitHub evidence | Measured Audi e-tron battery and coolant data; measured/calibrated first-law thermal/coolant model; NMPC optimization assessed in simulator | **F4/F5** vehicle, *not* EVSE converter thermal state, site transformer or observed mobility outcome |
| RB04 | Pan et al. (2025), DOI [10.1049/hve2.70024](https://doi.org/10.1049/hve2.70024) | **Publisher original full-text indexed content/selected methods and tables**, direct-open cache miss; equation-by-equation extraction not closed | Active EV response + dynamic thermal rating of distribution cables/transformers; 13-node numerical planning; illustrative transformer time constants | **F5 simulation**, not connected site extreme-heat field-measured service transitions |
| RB05 | Krama et al. (2026), DOI [10.1016/j.ecmx.2026.101960](https://doi.org/10.1016/j.ecmx.2026.101960) | Publisher original article metadata/abstract and HBKU institutional original abstract; **primary full-text equation audit pending** | Field observed 50-kW air-cooled EVSE ambient 15–55°C, rectifier derating, offered/delivered power, SOC, session time; raw data on request | **F3 measured charger**, no verified providing-transformer thermal topology, thermal control-event logged mechanism, raw validation split |
| RB06 | Li, Chang & Lu (2026), DOI [10.1109/PESGM58988.2026.11693150](https://doi.org/10.1109/PESGM58988.2026.11693150) | Third-party indexed summary only; original IEEE full text unavailable in this pass | 2000 kVA bus charger station transformer primary/secondary *electrical* measurements described | **PROVISIONAL F2**, do not promote to measured winding/EVSE temperatures or field thermal causality |

**Source-visual constraint:** web PDF screenshots requested for RB01 and RB02 and failed with cache miss; local PDF download was also blocked. This batch **does not** claim that PDF figures/images were independently visually checked. Any full-text equation or figure assessment requiring visual geometry stays open.

## B. RB01 — RACE Fletcher & Khan 2025, most consequential direct predecessor

### Original study design and stated data boundaries
- Report executive summary pp. 2–3 explicitly distinguishes Part 1 desktop feasibility **modeling informed by practical heat-run tests** from a proposed Part 2 longitudinal study with two purpose-built instrumented transformers. Do not relabel Part 1 outputs as in-field observed thermal restrictions.
- Original report introduction and methods pp. 8–13: representative EV charging profiles, non-EV load, one-MVA distribution-transformer scenarios; proposed MATLAB implementation of the IEC 60076-7 transformer state-time model. Model inputs: load factor (K(t)), ambient (	heta_a(t)); model outputs: top-oil (	heta_o(t)), hot-spot (	heta_h(t)), ageing and allowable charging capacity.
- Report Table 1, p. 12, uses **illustrative ONAN model values** (	au_w=4,mathrm{min}), (	au_o=180,mathrm{min}), (Delta	heta_{h,R}=23,^{circ}mathrm C), (Delta	heta_{o,R}=55,^{circ}mathrm C), load/no-load-loss ratio (R=5), (x=0.8), (y=1.6), and model constants (k_{11}=1), (k_{21}=1), (k_{22}=2). The study itself warns physical values are asset-dependent and may require heat-run calibration. Do NOT copy them as measured SINTEF nameplate calibration.
- Report pp. 24–26: proposed 4-level thermal hysteresis restricts EV charging power in steps of 25% when transformer hotspot enters simulated thermal bands with thresholds 100, 103, 107, 110°C. These are **scenario control settings**, not a universal physical or normative safe-charge threshold.
- Report's 10-hour **simulation** of 23 EVs: demand 1,364 kWh, supply 1,262 kWh (reported about 92% delivered). This is already a *modeled* thermal-restriction-to-charging-energy service consequence. Unserved simulation energy is 102 kWh. No observed missed departure, completed trip, charger availability or measured site-service realization is established by this result.
- Scope excludes EVSE rectifier sensor temperature and causal thermal derating in the *same* physical site; the report itself flags ancillary component limits, harmonic currents, instrumented validation and future Part 2 as outstanding.

**Direct implication:** Reject the novelty claim “first dynamic transformer thermal control that changes EV charging energy”. A more defensible SO3 claim would distinguish **(1) transformer thermal threshold time**, **(2) implementation/propagation restriction time**, and **(3) mobility-service deadline consequence**, using physically connected measurements or labeling latter two conditional simulation.

**Source:** [Fletcher & Khan RACE original report, pp. 2–3, 11–13, 24–26, 29–30](https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf).

### RB01 methodological appraisal
- Source authenticity: PASS for official report; model equipment and specific original heat-run dataset linkage PARTIAL.
- Physical topology/cause: PARTIAL for model path, FAIL for demonstrated same-site observed thermal causal event.
- Confounding: battery SOC acceptance, concurrent base demand, ambient and connector/ancillary constraints not jointly causally identified in field.
- Mathematics: IEC-style dynamic ratings suitable **model precedent**, but actual scenario heat-run calibration and uncertainty remain OPEN.
- Validation: numerical simulation, not prospective independent transformer/EVSE physical deployment.
- Service: delivered-versus-requested charging **simulation** present, actual mobility requirement/deadline evidence absent.

## C. RB02 — Bragone et al. (2022) physical PDE and PINN comparison

Original paper §2, equations (1)–(3), pp. 2–3:

[
k,partial_{xx}T + q = ho c_p partial_t T,qquad
q=P_0 + P_K(t)-h(T-T_a(t)), qquad P_Ksimmu K^2.
]
Boundary conditions: (T(0,t)=T_a(t),;T(H,t)=T_o(t)), where (T_o(t)) is **observed upper boundary data**, (H=1,mathrm m) is an effective simplified height.

- Paper Table 1 gives (P_0,mu) in W and convective (h) in W/(m² K), while 1D diffusion equation source should be W/m³ (for physically volumetric interpretation). A transferable dimensional model needs loss / volume and convection via surface/volume. This is a **model adaptation/unit-check requirement**, not a declaration that the original authors made an error.
- A dimensionally interpretable *candidate reformulation* is
[
ho c_ppartial_t T=kpartial_{xx} T+(P_0+P_K)/V-(h A_{mathrm{loss}}/V)(T-T_a),
]
with independently justified geometry. Do not assume (V), area, and coefficients have been physically identified by the original effective model.
- Paper eqs. (6)–(11): PINN automatic differentiation for the PDE residual and supervised boundary/forcing loss terms; source inputs include real transformer measured ambient, top-oil and load factor.
- Paper results first 100 h and selected (4	imes50) NN, (N_u=100,N_f=10000). Relative (L_2) spatial distribution difference to **FVM numerical** solution reported 0.145; relative norm of the top-oil comparison 0.0259 for selected setting. These are *relative norms*, not °C RMSE or prospective independent-asset tests.
- In paper §4, authors explicitly state that PINN **could not outperform FVM with this amount/type of data**. This is a single-paper conditional conclusion; not a universal claim that PINNs cannot work.

**Methodological consequence:** FVM agreement validates matching a numerical comparator under assumed physics; observed top-oil boundary use precludes interpreting this result by itself as leakage-free future top-oil forecast or experimentally measured internal temperature distribution. A future thesis PINN requires a fair same-input holdout against physics and persistence.

**Source:** [Bragone et al., original published article and KTH-hosted text, §2–4, Tables 1–6](https://www.diva-portal.org/smash/get/diva2%3A1683236/FULLTEXT01.pdf).

## D. RB03 — Acker et al. battery cooling physical model

Original publisher §2–§4 with measured Audi e-tron 55 quattro (2019) battery/coolant signals and thermal subsystem details:

[
i_{bat}=f(T_{bat},SOC),quad
R_{int}=(U_{bat}-U_{OC})/i_{bat},quad
dot Q_{ohm}=R_{int}i_{bat}^2,
]
[
m_{bat}c_{bat}dot T_{bat}=dot Q_{ohm}+dot Q_{coolant}+dot Q_{ambient}.
]

Pumped coolant is an actual modeled actuator path, not direct arbitrary heat-flow control; paper §3 eqs 8–16 include pump mass flow, chiller COP, inlet/outlet coolant volumes and compressor energy. The paper models constant coolant heat capacity/density, ideal mixing and ignores pipe pressure dynamics. Controller savings (up to 0.41 kWh) and shorter charge time (up to 4.5%) were assessed in a **validated simulation model**, not documented as observed deployed real-world mobility.

**Consequence for our thesis:** Vehicle heat acceptance is not identical to EVSE rectifier protection; neither battery temperature nor generic CAN inlet/outlet readings can be relabeled as measured rectifier/coolant flow without instrumentation qualification.

**Source:** [Acker et al., Springer article, eqs 1–16, §§2–4](https://link.springer.com/article/10.1007/s41104-025-00157-7).

## E. RB04–RB06 important counterexamples and access gates

- **Pan 2025**: distribution planning model combines active EV response and DTR of cables and transformers. Reported illustrative time constants (	au_o=155) min, (	au_w=5) min (Table 2). Case-study claims of 4.8% investment savings and 96% uplift are **numerical case results**, not experimental validation of installed transformer–EVSE thermal feedback. **Novelty implication:** combining transformer dynamic rating and active EV responses is established modeling prior art. [Publisher article](https://doi.org/10.1049/hve2.70024).
- **Krama 2026**: field EVSE evidence strongest for extreme desert ambient 15–55°C; 50-kW air-cooled charger; publisher abstract reports offered power drop up to 35–40 kW once rectifier around 55°C, and winter/summer charging durations 86 and 169 min for tested SOC window; raw on request. These are source-reported results, not a universal derating curve or same transformer–EVSE field mechanism. **Status: primary ABSTRACT; full model equations remain to obtain.** [Publisher](https://doi.org/10.1016/j.ecmx.2026.101960); [HBKU university profile](https://elmi.hbku.edu.qa/en/publications/impact-of-extreme-climatic-conditions-on-fast-ev-charger-performa/).
- **Li et al. 2026**: indexed third-party summary describes simultaneous primary/secondary electrical measurements on one 2000 kVA transformer supplying an EV bus depot. No inspected publisher full paper, hot-spot/oil/rectifier measurements, site time alignment or thermal cause logs in this pass; **do not count as full-text extraction**. [DOI](https://doi.org/10.1109/PESGM58988.2026.11693150).

## F. Provisional cross-study synthesis and source-to-objective trace

| Mechanism/evidence need | Closest original predecessor | Verified level | SO | Still needed |
|---|---|---|---|---|
| Transformer top-oil/hotspot dynamic thermal load | RACE; Bragone | Model and measured component inputs; no same-site EVSE sensor thermal | SO1/SO2 | Physically parameterized transformer, independent extreme-heat validity |
| Transformer temp → allowed EV power → charging energy | RACE | Numerical scenario with requested/delivered energy | SO2/SO3 | Actual restriction reason/timestamps and mobility deadlines |
| Extreme ambient → EVSE rectifier heat → charger offered power | Krama | Source-reported single EVSE field observation, full text pending | SO1/SO3 | Raw temperature/control/alignment and providing transformer |
| Active EV demand control ↔ transformer DTR | Pan | Model/planning simulation | SO2/SO3 | In situ dynamic timing, cross-system causal validation |
| EV battery heating/cooling/acceptance | Acker | Real vehicle instrumentation + derived physics; controller simulation | SO1/SO2 | Representative vehicle/site and charging-state instrumentation |
| Transformer PINN physics vs numerical | Bragone | Field forcing, 1D effective PDE and numerical FVM benchmark | SO2 | Honest operational forecast, dimensional calibration and external validation |
| Bus EV charging connected electrical side | Li | Third-party indexing only | SO1 | Primary full text, topology and measured thermal channels |

**No universal novelty verdict.** Strong counterexamples reject “first” claims for PINN transformer physics, dynamic transformer EV thermal-charging control, EVSE extreme-heat derating, and EV-responsive DTR planning. Potential bounded contribution remains combined thermally causal, instrumented **state→capability→service through measured event times**, if and only if connected observations can validate it.

## G. Study-unit/mathematics protocol required before SLR completion

1. **Record identity**: no new canonical `LIT-` IDs assigned from this paper-reading batch; match to master IDs and 590 workbook before any formal paper-count.
2. **Study family**: IFAC 2022 transformer PINN proceedings DOI 10.1016/j.ifacol.2022.09.070 and Bragone EPSR 2022 DOI 10.1016/j.epsr.2022.108447 must be compared for duplicated analyses before counting independent experiments.
3. **Search**: original platform-native Scopus, Compendex, IEEE, WoS A–F queries, their timestamped exported results, and hash evidence still not executed for current version.
4. **Eligibility**: no independent human adjudication of 259 provisional TA exclusions, 107 uncertain, 98 advance candidates. No PRISMA-ScR numerator/denominator closure is admissible.
5. **Source depth**: review each primary complete text with exact equation/figure, apparatus/sensor semantics, units, independent holdout and uncertainty. Krama/Li primary full-text status open.
6. **Data**: independent time-synchronized transformer+EVSE+controls+service physical installation not established by source aggregation.

**Next research work:** (i) obtain unchanged local V5 590 workbook; (ii) complete immutable 533↔590 dedup crosswalk, (iii) executable database-native A–F searches and human adjudication, (iv) continue deep original reading of Krama and Li after acquiring full papers, plus Gong experimental transformer 25 kVA, Pan equation-by-equation and RACE control details. Do not describe missing source access as negative study findings.
