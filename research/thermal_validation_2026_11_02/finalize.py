#!/usr/bin/env python3
"""Scientific acceptance review from actual derived numerical outputs.
Missing field evidence is never silently promoted to PASS."""
import csv,json,sys
from pathlib import Path
import numpy as np
import pandas as pd

def main(root):
 root=Path(root)
 v=root/'02_vehicle';t=root/'03_transformer';e=root/'04_epfl'
 uncertainty=pd.read_csv(v/'15min_uncertainty_screen.csv')
 comparison=pd.read_csv(v/'heldout_baseline_comparison.csv') if (v/'heldout_baseline_comparison.csv').exists() else None
 if comparison is None:
  m=pd.read_csv(v/'15min_session_metrics.csv');q=m[m.split=='test']
  agg=[]
  for (vehicle,mode,model),g in q.groupby(['vehicle','mode','model']):
   agg.append({'vehicle':vehicle,'mode':mode,'model':model,'mean_session_MAE_C':g.mae_C.mean()})
  comparison=pd.DataFrame(agg);comparison.to_csv(v/'heldout_baseline_comparison.csv',index=False)
 transformer=pd.read_csv(t/'conditional_24h_summary.csv')
 epfl=json.loads((e/'epfl_summary.json').read_text())
 vehicle_g=[]
 for r in uncertainty.itertuples():
  group=comparison[(comparison.vehicle==r.vehicle)&(comparison['mode']==r.mode)]
  b=float(group[group.model=='persistence'].mean_session_MAE_C.iloc[0]) if not group[group.model=='persistence'].empty else None
  phys=float(group[group.model=='thermal'].mean_session_MAE_C.iloc[0]) if not group[group.model=='thermal'].empty else None
  vehicle_g.append({'vehicle':r.vehicle,'mode':r.mode,'holdout_rmse_C':r.test_rmse_C,'test_coverage_nominal90':r.test_coverage_fraction,
   'mean_session_mae_thermal_C':phys,'mean_session_mae_persistence_C':b,
   'gate':'BLOCKED' if r.test_coverage_fraction<.80 or phys is None or b is None or phys>=b else 'PROVISIONAL',
   'warning':'Model uses observed future current and ambient; not forecast. Model coefficients not uniquely identified.'})
 (v/'model_acceptance.json').write_text(json.dumps(vehicle_g,indent=2))
 top=transformer[(transformer.split=='holdout')&(transformer.state=='Top oil [degC]')].iloc[0]
 hv=transformer[(transformer.split=='holdout')&(transformer.state=='Hot-spot HV [degC]')].iloc[0]
 lv=transformer[(transformer.split=='holdout')&(transformer.state=='Hot-spot LV [degC]')].iloc[0]
 gates=[
  ('01_Raw_Data_Provenance_and_QA','PROVISIONAL','SINTEF sensor and calculated CSV publisher MD5 match; BEV charging CSV SHA256 registered. Full equipment signal dictionary and all published hashes not verified.'),
  ('02_KU_Leuven_Vehicle_Thermal_Validation','BLOCKED','AC test intervals under-cover and independent session-weight improvements inconsistent; DC model large errors; BEV1 DC insufficient sessions. Physical pack-state identification unresolved.'),
  ('03_SINTEF_Transformer_Thermal_Validation','PROVISIONAL',f'Top-oil 24h holdout RMSE {top.model_rmse_C:.3f} vs persistence {top.persistence_rmse_C:.3f} C. Hotspot HV {hv.model_rmse_C:.3f} vs {hv.persistence_rmse_C:.3f}; LV {lv.model_rmse_C:.3f} vs {lv.persistence_rmse_C:.3f}. Norway operating range not extreme-heat transfer verified.'),
  ('04_EPFL_Electrical_Interface_Validation','PROVISIONAL',f"Measurement rows={epfl['measured_rows_total']}, original reported 64277, discrepancy={epfl['published_minus_populated']}; session records matched {epfl['session_workbook']['matched_session_keys']}/1878 after time-verified CCS2 ID offset; observed concurrent sums above stated shared capacity {epfl['above_documented_station_capacity_minutes']} times. AC/DC metering boundary unknown."),
  ('05_EVSE_Thermal_Law_Evidence','BLOCKED','No current Drive original internal EVSE rectifier/heatsink temperatures, cooling states or source-equipment thermal ratings. Qatar author dataset request-only; do not transplant charger limits.'),
  ('06_Directional_Coupling_Qualification','BLOCKED','SINTEF Norway, KU Leuven vehicles, EPFL Switzerland and Turkish network not demonstrated to share physical connection. No same-site synchronized thermal interdependency.'),
  ('07_Coupled_Model_VVUQ','BLOCKED','Existing synthetic model tests numerical structure only. Component thermal/EVSE law gates fail; do not issue thesis-qualified coupled output.'),
  ('08_Service_Resilience_Sustainability_Results','BLOCKED','EPFL sessions support conditional charging-service metrics; mobility readiness and grid-service requirements, field propagation and sustainability inventory not established.')
 ]
 with (root/'acceptance_gates.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['work_package','decision','evidence_and_reason']);w.writerows(gates)
 for dirname,decision,why in gates:
  folder=root/(dirname[:2]+'_'+{'01':'provenance','02':'vehicle','03':'transformer','04':'epfl','05':'evse','06':'coupling','07':'vvuq','08':'services'}[dirname[:2]])
  (folder/'STATUS.md').write_text(f'# {dirname}\n\n**Decision: {decision}**\n\n{why}\n')
 (root/'05_evse'/'missing_evidence.json').write_text(json.dumps({'EVSE_internal_temperature_measured':False,'EVSE_cooling_state_measured':False,'verified_thermal_derating_law_for_same_model':False,
 'qatar_2026_article':'https://doi.org/10.1016/j.ecmx.2026.101960','qatar_raw_field_data_in_current_folder':False,'qualification':'BLOCKED'},indent=2))
 (root/'06_coupling'/'required_interfaces.json').write_text(json.dumps({'P_to_Te':{'mechanism':'transformer thermal capability -> charger available AC input -> charging service',
 'required':'verified transformer rating, thermal operating limits, feeder-to-EVSE connection, synchronized logs','status':'BLOCKED'},
 'Te_to_P':{'mechanism':'charging + EVSE cooling power -> transformer loading -> transformer thermal state',
 'required':'metered grid-side AC input and auxiliary, EVSE thermal control, common node and synchronized timestamps','status':'BLOCKED'},
 'warning':'Separate installations cannot be concatenated and represented as observed causal coupling'},indent=2))
 (root/'07_vvuq'/'policy.txt').write_text('No thesis-qualified coupled-simulation regeneration. Existing exploratory numerical checks do not constitute field validation.\n')
 (root/'08_services'/'policy.txt').write_text('Do not report causal service deficits, propagation delays or sustainability conclusions until physical assumptions, service targets and boundaries pass gates.\n')
 report=f'''# Executed physical-data research audit — 2026-11-02

**All output is component-level. Field-validated coupled thermal model: BLOCKED.**

## Raw integrity
- Original SINTEF source files authenticated against the publisher MD5 in `01_provenance/source_registry.csv`.
- KU Leuven: 134 charging CSV files, 109 AC and 25 DC, session SHA256 registry.
- Raw files remain unmodified. Calculated SINTEF data are not used as independent measured truth.

## KU Leuven: session-separated 15-minute conditional hindcast
| Vehicle / mode | Test RMSE °C | Nominal 90% interval empirical coverage | Gate |
|---|---:|---:|---|
'''
 for v0 in vehicle_g:report+=f"| {v0['vehicle']} {v0['mode']} | {v0['holdout_rmse_C']:.3f} | {100*v0['test_coverage_nominal90']:.1f}% | {v0['gate']} |\n"
 report+='''
The maximum BMS temperature sensor is not an independently observed lumped thermal state. Model uses *future observed* current and ambient. Charging power sign/scale and vehicle cooling mechanisms are not yet identified.

## SINTEF: 24-hour conditional hindcast
'''
 report+=f"- Top oil: {top.model_rmse_C:.3f} °C RMSE vs persistence {top.persistence_rmse_C:.3f} °C (PROVISIONAL).\n"
 report+=f"- HV hotspot: {hv.model_rmse_C:.3f} vs persistence {hv.persistence_rmse_C:.3f} °C (REJECT).\n"
 report+=f"- LV hotspot: {lv.model_rmse_C:.3f} vs persistence {lv.persistence_rmse_C:.3f} °C (REJECT).\n"
 report+='''No power-system thermal transfer to a hypothetical distribution transformer is justified. Late-period error bands are descriptive, because evaluation windows overlap.

## EPFL minute-level charging interface
'''
 report+=f"- Actual populated measurements: {epfl['measured_rows_total']:,} vs documented 64,277; unresolved difference {epfl['published_minus_populated']:,}.\n"
 report+=f"- Reconciled {epfl['session_workbook']['matched_session_keys']:,}/1,878 session IDs after time-verified CCS2 global offset of 1,129.\n"
 report+=f"- Both connectors observed concurrently at {epfl['concurrent_two_connector_minutes']:,} minute stamps; sum above stated 172.5 kW at {epfl['above_documented_station_capacity_minutes']:,} minute stamps (interpret only after meter/plant boundaries established).\n"
 report+=f"- Median source `P(W)` integration / source Session Energy ratio on {epfl['session_workbook']['comparisons_eligible']:,} complete no-gap sessions: {epfl['session_workbook']['median_measured_P_integral_over_session_energy_for_no_gap_sessions']:.3f}. This is an unresolved consistency difference, **not** efficiency.\n"
 report+='''
## Remaining blockers
- No original **EVSE internal thermal measurements** in the Drive portfolio.
- No proof of **same-site transformer→feeder→charger physical topology** or common timestamps.
- No admitted charger model-specific derating and auxiliary loss law.
- No verified thermal threshold, operational resilience service requirement or measured propagation delay.
- Existing UrbanEV derived energy, Turkish network benchmark and generic resilience CSV cannot substitute for matched field thermal observations.

## Accept/reject rule
All 8 stage results are recorded in `acceptance_gates.csv`. No stage gets PASS merely because executable code ran. The next experiment is diagnostic, not a new accepted synthetic dataset.
'''
 (root/'EXECUTED_FINDINGS.md').write_text(report)
 print(report[:3300]);return gates

if __name__=='__main__':main(sys.argv[1])
