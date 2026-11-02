#!/usr/bin/env python3
"""Structural and claim-admission checks for the ECE6378-to-thesis ML register.

PASS only means schema and explicit fields are internally consistent, NOT actual
power-flow feasibility, physics, identifiability, causal inference, or field validation.
"""
from __future__ import annotations
import argparse
import csv
import math
import sys
from pathlib import Path

FILE='ml_experiment_register.csv'
REQUIRED={
'experiment_id','comparison_group','model_id','model_family','target_channel','target_unit',
'site_id','asset_id','source_id','raw_sha256','input_information_set','horizon_minutes',
'train_manifest','validation_manifest','test_manifest','independent_heldout',
'uses_observed_future_inputs','physical_topology_verified','transformer_temperature_measured',
'evse_temperature_measured','claimed_connected_thermal_field_validation',
'source_domain_extreme_heat_verified','physics_constraints_verified','experiment_status',
'test_mae','baseline_mae','test_rmse','baseline_rmse','n_test','notes',
}
BOOL_TRUE={'true','yes','1'}
BOOL_FALSE={'false','no','0',''}
STATUSES={'NOT_RUN','EXPLORATORY','SOFTWARE_VERIFIED','SIMULATION_VERIFIED',
'COMPONENT_CONDITIONAL_VALIDATED','CONNECTED_ELECTRICAL_VALIDATED',
'CONNECTED_THERMAL_FIELD_VALIDATED','COMPARATIVE_CLAIM','BLOCKED_EVIDENCE',
'BLOCKED_EXTERNAL_ACCESS','NOT_COMPARABLE'}


def check_root(root:Path,require_rows=False):
    errors=[]; rows=[]; p=root/FILE
    if not p.is_file():return [f'{FILE}: missing'], {'rows':0}
    with p.open(newline='',encoding='utf-8-sig') as f:
        reader=csv.DictReader(f)
        fields=set(reader.fieldnames or [])
        if missing:=REQUIRED-fields:
            return [f'{FILE}: missing columns {sorted(missing)}'],{'rows':0}
        rows=list(reader)
    if require_rows and not rows:errors.append('no experiment rows: must not claim completed experiment')
    seen=set();groups={}
    for n,row in enumerate(rows,2):
        tag=f'{FILE}:{n}'
        ident=row['experiment_id'].strip()
        if not ident:errors.append(f'{tag}: experiment_id blank')
        if ident in seen:errors.append(f'{tag}: duplicate experiment_id {ident}')
        seen.add(ident)
        status=row['experiment_status'].strip()
        if status not in STATUSES:errors.append(f'{tag}: unrecognized status {status}')
        for col in ('independent_heldout','uses_observed_future_inputs','physical_topology_verified',
                    'transformer_temperature_measured','evse_temperature_measured',
                    'claimed_connected_thermal_field_validation','source_domain_extreme_heat_verified',
                    'physics_constraints_verified'):
            val=row[col].strip().lower()
            if val not in BOOL_TRUE|BOOL_FALSE:
                errors.append(f'{tag}: invalid Boolean {col}={row[col]!r}')
        def true(x):return row[x].strip().lower() in BOOL_TRUE
        def has(x):return bool(row[x].strip())
        def numeric(name):
            val=row[name].strip()
            if not val:return None
            try:
                x=float(val)
                if not math.isfinite(x) or x<0:raise ValueError
                return x
            except ValueError:
                errors.append(f'{tag}: invalid nonnegative finite {name}={val!r}')
                return None
        values={x:numeric(x) for x in ('test_mae','baseline_mae','test_rmse','baseline_rmse','n_test','horizon_minutes')}
        if values['n_test'] is not None and int(values['n_test'])!=values['n_test']:
            errors.append(f'{tag}: n_test must be integer')
        if values['horizon_minutes'] is not None and values['horizon_minutes']<=0:
            errors.append(f'{tag}: horizon_minutes must be positive')
        if true('claimed_connected_thermal_field_validation') or status=='CONNECTED_THERMAL_FIELD_VALIDATED':
            mandatory=('physical_topology_verified','transformer_temperature_measured',
                       'evse_temperature_measured','independent_heldout','physics_constraints_verified')
            if not all(true(x) for x in mandatory):
                errors.append(f'{tag}: connected thermal field claim lacks { [x for x in mandatory if not true(x)] }')
            if true('uses_observed_future_inputs'):
                errors.append(f'{tag}: cannot call conditional hindcast operational field validation')
            for x in ('site_id','asset_id','source_id','raw_sha256','train_manifest','validation_manifest','test_manifest'):
                if not has(x):errors.append(f'{tag}: field claim missing {x}')
            if values['n_test'] is None or values['n_test']<=0:
                errors.append(f'{tag}: field claim lacks nonempty test')
        if status in ('COMPONENT_CONDITIONAL_VALIDATED','COMPARATIVE_CLAIM','CONNECTED_THERMAL_FIELD_VALIDATED'):
            for x in ('target_channel','target_unit','input_information_set','train_manifest','validation_manifest','test_manifest'):
                if not has(x):errors.append(f'{tag}: evaluated result missing {x}')
            if not true('independent_heldout'):
                errors.append(f'{tag}: evaluated claim requires independent heldout')
            if any(values[x] is None for x in ('test_mae','baseline_mae','test_rmse','baseline_rmse','n_test')):
                errors.append(f'{tag}: evaluated claim lacks paired test and baseline metrics')
        if status=='COMPARATIVE_CLAIM':
            key=row['comparison_group'].strip()
            if not key:errors.append(f'{tag}: comparative claim has no comparison_group')
            groups.setdefault(key,[]).append(row)
        if true('uses_observed_future_inputs') and status=='CONNECTED_THERMAL_FIELD_VALIDATED':
            errors.append(f'{tag}: future-forcing leakage of inference')
    for key,group in groups.items():
        # This is deliberately conservative: a comparative claim must include a
        # physics and statistical comparator in the same declared group.
        members={r['model_family'].strip() for r in rows if r['comparison_group'].strip()==key}
        if not {'M0','M1'}.issubset(members):
            errors.append(f'comparison_group={key}: missing M0 physics and/or M1 statistical comparator')
        refs={(r['site_id'],r['target_channel'],r['horizon_minutes'],r['input_information_set'],r['test_manifest'])
              for r in rows if r['comparison_group'].strip()==key}
        if len(refs)>1:errors.append(f'comparison_group={key}: models lack identical site/target/horizon/info/test')
    return errors,{'rows':len(rows),'groups':len(groups)}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',required=True,type=Path)
    p.add_argument('--require-rows',action='store_true')
    a=p.parse_args()
    errors,info=check_root(a.root,a.require_rows)
    print('ML experiment register:',info)
    for e in errors:print('ERROR:',e)
    if errors:return 1
    print('PASS: ML experiment schema/claim predicates ONLY; not physical/field validation')
    return 0

if __name__=='__main__':sys.exit(main())
