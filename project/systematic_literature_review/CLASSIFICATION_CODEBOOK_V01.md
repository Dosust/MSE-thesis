# Classification codebook v1.0 — fixed conceptual scheme for the literature review

**Date:** 2026-11-03. **Protocol state:** working scheme pending dated review-protocol lock. One source may have multiple topic tags; **screening decisions, evidence claims and maturity statuses are different dimensions**.

## Axis A — Scientific research domain (what is studied)

| Code | Domain | Inclusion cues | What it cannot establish alone |
|---|---|---|---|
| C1 | Power-system/transformer thermal physics | Oil/winding/hotspot, ambient/current, IEC/IEEE thermal loading, dynamic ratings, losses, transformer cooling | EVSE state or charger service link |
| C2 | EVSE and vehicle thermal physics | Rectifier/heatsink/cooling derating, EV thermal acceptance, battery losses/pack/coolant temperature | Supplying transformer response |
| C3 | Physical Power↔Electrified-Transportation interdependencies | Feeder topology, EVSE demand, transformer/charger electrical measurement, V2G, physically mapped equipment | Field causal *thermal* coupling if only demand/network simulation |
| C4 | Mathematical dynamics and system identification | ODE/PDE/DAE, multi-time scales, interface feedback, parameter identifiability, propagation | Real installation evidence without sensors |
| C5 | Physics-informed ML / AI / hybrid models | PINN, neural operators, gray-box inverse models, physical residuals, thermodynamics ML | Superiority or true physics from small residual alone |
| C6 | Resilience/viability/control/service | Thermal limits, charging energy, arrivals/departures, mobility, recovery, control, uncertainty | Actual mobility loss from modeled unserved charging kWh |

**Assignment:** one \`primary_domain\` per bibliographic item; \`secondary_domains\` comma-free semicolon tags; may reclassify with recorded reason/date. Avoid splitting one paper into multiple duplicate bibliographic studies because it spans domains.

## Axis B — Evidence for each scientific claim (how it is supported)

- **F1:** Operating *same-installation* connected physical transformer–EVSE system with documented topology, synchronized electrical/thermal observations and actual control/service causal diagnosis; only assert specific mechanisms directly supported.
- **F2:** Operating *same-installation* field connection with partial electrical/thermal observations but no complete causal thermal-service chain.
- **F3:** Operational field data for an individual real-world transformer OR charger OR vehicle.
- **F4:** Controlled laboratory or test-bench instrument measurements.
- **F5:** Model calibrated, driven, or independently evaluated using actual measurements; record **which** variable is measured and whether the model's predicted internal states themselves were measured.
- **F6:** Theory, analytical mathematics, numerical or synthetic simulation/optimization without directly validating the specific physical outcome claimed.
- **F7:** Review, engineering standard or methodological synthesis; does not automatically constitute experimental proof.

**Not a strict ranking:** F5 may be more appropriate than F3 for a PINN's claimed predicted *distribution* even when its forcing/boundary conditions came from field data. A source can have F3 for observed top-oil and F5 for learned internal spatial temperature. The grade requires source, page, claim, actual observed variable and caveat.

## Axis C — Our evidence-workflow maturity (what we actually completed)

| Code | Status | Admission test |
|---|---|---|
| S0 | Task planned | Objective and source need identified, no retrieved source yet |
| S1 | Bibliographic source retrieved/located | DOI/publisher/repository metadata checked; not necessarily full text |
| S2 | Preliminary or formal screened | Title/abstract eligibility decision recorded; \`pilot\` decisions **never** count toward final formal PRISMA until formal corpus methodology is executed |
| S3 | Extracted | Actual equations, measured-vs-modeled variables, assumptions and claims with source section/eq/page recorded |
| S4 | Source-verified | Primary text and relevant equations/tables examined; numerical assertions traceable; figure status and inaccessible portions noted |
| S5 | Independently validated **by our work** | A genuine held-out/replicated mathematical or physical check is run with original qualified data; otherwise stay S4 |
| S6 | Synthesized | Supported cross-paper comparison reviewed; its limitations and closest counterexamples stated |

A fully reviewed paper can be S4 even if the *paper itself* contains excellent external validation. S5 refers to **what our review team actually verified**; it is not an endorsement of the paper.

## Independent bibliographic eligibility fields

- \`record_kind\`: original research | review | standard | technical report | dataset descriptor | preprint.
- \`fulltext_status\`: original examined | abstract only | original inaccessible | license/access pending.
- \`provisional_screen\`: candidate primary | background review/standard | uncertain | clearly out of scope. **Not** final include/exclude.
- \`review_phase\`: PILOT | FORMAL.
- \`prisma_countable\`: ALWAYS NO for pilot sources; YES only after accession through locked formal-search/dedup/screen procedure.

## Quality/confounder fields to extract

Physical hardware/site; source of thermal measurement; electrical AC/DC boundary; sensor location; temperatures/range; heat source/sink and governing equation units; genuine system connectivity; ambient vs load vs SOC taper vs controller reason codes; sampling, data gaps, time-zone; model fitting vs measured holdouts; external-site and extreme heat validation; physical-vs-statistical parameter identification; service commitments and outcomes; source DOI/page and artifacts; uncertainty and contradictory results.

**Critical distinctions:** modeled transformer aging ≠ observed degradation; electricity charging shortfall ≠ missed mobility; rectifier vs battery thermal protection; vehicle pack coolant vs charger internal cooling; field-forcing PINN ≠ field-validated spatial temperature; inferred power loss ≠ directly measured heat.
