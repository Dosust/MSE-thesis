#!/usr/bin/env python3
"""Verify thesis evidence-register schemas and prevent unsupported coupled-field status.

Does not validate physics, raw source identity, independent testing or measured datasets.
"""
import argparse,csv,sys
from pathlib import Path

SCHEMAS = {
 'source_registry.csv': {'source_id','raw_sha256','source_access_status','measurement_kind'},
 'asset_topology.csv': {'site_id','upstream_asset_id','downstream_asset_id','topology_verified'},
 'observations.csv': {'source_id','site_id','asset_id','timestamp_utc','channel','observed_value','unit','origin_kind','raw_sha256'},
 'thermal_interface_evidence.csv': {'evidence_id','site_id','direction','same_site_verified','physical_topology_verified','clock_sync_verified','transformer_thermal_measured','evse_thermal_measured','directional_mechanism_verified','independent_test_pass','evidence_tier'},
 'equation_register.csv': {'equation_id','provenance_class','equation_class','physical_meaning','variables_units','validity_domain'},
 'parameter_register.csv': {'parameter_id','asset','symbol','unit','source_identifier','validity_domain'},
 'validation_register.csv': {'validation_id','site_id','test_group','heldout_independent','prediction_horizon','validation_claim'},
 'execution_ledger.csv': {'run_id','gate','result','blocker'},
}
TRUES={'true','1','yes','y'}
FALSIES={'false','0','no','n',''}
ALLOWED_TIERS={'METADATA_ONLY','MEASURED_UNCOUPLED','MEASURED_SAME_PREMISES_ELECTRICAL','MEASURED_CONNECTED_ELECTRICAL','MEASURED_CONNECTED_THERMAL','CONNECTED_THERMAL_FIELD_VALIDATED','SYNTHETIC','UNKNOWN'}
REQUIRED_CONNECTED=('same_site_verified','physical_topology_verified','clock_sync_verified','transformer_thermal_measured','evse_thermal_measured','directional_mechanism_verified','independent_test_pass')

def check_root(root:Path):
 errors=[]; stats={}; seen_source_ids=set()
 for name,mandatory in SCHEMAS.items():
  f=root/name
  if not f.is_file(): errors.append(f'{name}: missing'); continue
  with f.open(encoding='utf-8-sig',newline='') as handle:
   reader=csv.DictReader(handle)
   if not reader.fieldnames: errors.append(f'{name}: missing header');continue
   missing=mandatory-set(reader.fieldnames)
   if missing: errors.append(f'{name}: missing columns {sorted(missing)}');continue
   rows=0
   for r in reader:
    rows+=1
    if name=='source_registry.csv':
     sid=r.get('source_id','')
     if not sid:errors.append(f'{name}:{rows}: blank source_id')
     if sid in seen_source_ids: errors.append(f'{name}:{rows}: duplicate source_id')
     seen_source_ids.add(sid)
    if name=='thermal_interface_evidence.csv':
     tier=r.get('evidence_tier','').strip()
     if tier not in ALLOWED_TIERS:errors.append(f'{name}:{rows}: invalid evidence tier {tier}')
     if r.get('direction') not in {'P_TO_TE','TE_TO_P'}:errors.append(f'{name}:{rows}: direction must be P_TO_TE or TE_TO_P')
     if tier=='CONNECTED_THERMAL_FIELD_VALIDATED':
      bad=[k for k in REQUIRED_CONNECTED if r.get(k,'').strip().lower() not in TRUES]
      if bad:errors.append(f'{name}:{rows}: connected-field validation without {bad}')
      if not r.get('source_id','').strip() or not r.get('source_link','').strip():
       errors.append(f'{name}:{rows}: connected-field validation missing original source/link')
    if name=='observations.csv' and r.get('origin_kind','') not in {'DIRECT_MEASURED','OBSERVED_AGGREGATE','IMPUTED','MODEL_CALCULATED','SYNTHETIC'}:
     errors.append(f'{name}:{rows}: invalid origin_kind')
   stats[name]=rows
 return errors,stats

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',required=True,type=Path);a=p.parse_args()
 errors,stats=check_root(a.root)
 print('Evidence register row counts:')
 for k,v in stats.items():print(f' {k}: {v}')
 if errors:
  print('FAIL:','\n - '.join(['']+errors));return 1
 print('PASS: CSV schemas and explicit claim-tier logic (NOT physics or field validation)');return 0
if __name__=='__main__':sys.exit(main())
