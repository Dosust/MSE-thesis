# Evidence-extraction schema guide

Use [EVIDENCE_EXTRACTION_TEMPLATE.csv](./EVIDENCE_EXTRACTION_TEMPLATE.csv) **once per included original study** (and a separate linked row when same paper reports independent installations/experiments whose measurement bases differ). Empty cells mean not extracted yet; use explicit `NOT_REPORTED`, `NOT_APPLICABLE`, `NOT_VERIFIED` where appropriate and do not equate these states.

## Identity
`study_id,doi,title,authors,year,publication_type,peer_review_status,evidence_stream`. Preserve exact publisher DOI and publication status; note study/report duplicates.

## Measurement, operating domain and equipment
`country,facility_site,transformer_type,transformer_rating_kVA,transformer_cooling_mode,evse_type,evse_rating_kW`. Do not invent equipment values. Record environmental and electrical conditions, sensors, sample interval, number of physically independent equipment units and sessions. Row count is not equipment count.

## Physical linkage and directionality
`equipment_topology_verified,same_site_power_ev_connection` must identify actual feeder and physical transformer-to-EVSE mapping to support a field-coupling claim. A simulated IEEE benchmark connection should be `MODEL_TOPOLOGY_ONLY`, never `MEASURED_CONNECTED`.

## State measurement flags
For each signal specify `MEASURED`, `CALCULATED_FROM_MEASURED`, `SIMULATED`, `NOT_REPORTED` or `NOT_APPLICABLE`, not just vague yes/no. Distinguish `transformer_topoil_measured`, `transformer_winding_hotspot_measured`, `evse_internal_temp_measured`, `ev_battery_temp_measured`, and `ambient_measured`.

## Electrical/charging boundaries
Distinguish charger grid AC input (actual power meter), charger DC terminal output, battery-terminal DC measured values, offered charging capacity, accepted charging power, fan/cooling status, restriction/protection event and required versus delivered energy. Use actual units and sign conventions.

## Methodology and bias
`physics_equations_source`: exact equation or referenced standard **and article page/section**. `parameter_identifiability_method`: structural/profile likelihood/excitation vs simple numerical fit. `calibration_design` and `validation_holdout_design`: temperature/season split, equipment/site independence and whether observed future forcing is used. `uncertainty_method`: sensor, parameters, numerical, structural, forcing, prediction intervals and calibration.

For appraisal rate independently each domain as `LOW_CONCERN`, `SOME_CONCERN`, `HIGH_CONCERN`, `NOT_REPORTED`, `NOT_APPLICABLE`, supported by precise page or table evidence. Do not calculate a single invented numeric score.

## Eligibility decisions
`eligibility_screen_1,eligibility_screen_2,final_inclusion`: allowable values `INCLUDE`, `EXCLUDE`, `UNCLEAR`, `NOT_DONE`; second screen is `NOT_DONE` until a distinct independent human screen occurs. `exclusion_reason` uses E1 wrong system; E2 no thermal/time mechanism; E3 wrong study design/non-primary; E4 inaccessible/insufficient; E5 duplicate; E6 later than cutoff; E7 wrong exposure/outcome.

A secondary review or methods guideline is a source for backward/forward search or standards, not a new experiment. A supplemental original dataset is linked to its study and not counted as another independent publication.
