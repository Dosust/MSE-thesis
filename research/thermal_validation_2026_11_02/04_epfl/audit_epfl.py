#!/usr/bin/env python3
"""Read actual EPFL native XLSX cells via streaming OOXML, never edit the workbooks.

No new physical assumptions: P(W) is the publisher's P label; AC/DC metering
boundary MUST be independently verified. Integrate P only as conditional
engineering consistency diagnostics (no verified AC/DC loss inference).
"""
import argparse, collections, csv, hashlib, json, math, statistics, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
import numpy as np

NS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
HEAD=['A','B','C','D','E','F','G','H','I','J','K','L','M']

def shared(z):
    if 'xl/sharedStrings.xml' not in z.namelist():return []
    root=ET.fromstring(z.read('xl/sharedStrings.xml'))
    return [''.join(el.itertext()) for el in root.findall(NS+'si')]

def rows(z, tab, strings):
    with z.open('xl/worksheets/sheet'+str(tab)+'.xml') as s:
        tree=ET.iterparse(s,events=('start','end')); root=None
        for action,elem in tree:
            if root is None:root=elem
            if action=='end' and elem.tag==NS+'row':
                vals={}
                for cell in elem:
                    if cell.tag!=NS+'c':continue
                    ref=cell.attrib.get('r','');col=''.join(x for x in ref if x.isalpha())
                    if col not in HEAD:continue
                    v=cell.find(NS+'v')
                    if v is not None and v.text:
                        value=v.text
                        if cell.attrib.get('t')=='s':value=strings[int(value)]
                        vals[col]=value
                yield vals
                elem.clear()

def num(x):
    try:
        v=float(x);return v if math.isfinite(v) else float('nan')
    except (TypeError,ValueError):return float('nan')

def ok(v):return math.isfinite(v)

def run(src,session_src,out,expected_measurements=64277,capacity_W=172500):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    f=Path(src)
    powers_by_timestamp=collections.defaultdict(lambda:[float('nan'),float('nan')])
    qa={}; metrics=[];anomaly=[]
    with zipfile.ZipFile(f) as z:
        strs=shared(z)
        for si,connector in [(1,'CCS1'),(2,'CCS2')]:
            totalrows=0;populated=0;missing=collections.Counter();sessions=collections.defaultdict(list)
            unusual=[]; badtime=0
            for i,r in enumerate(rows(z,si,strs)):
                if i==0:
                    qa[connector+'_column_headers']={h:r.get(h) for h in HEAD};continue
                totalrows+=1
                if 'C' not in r:continue
                populated+=1
                v={key:num(r.get(col)) for key,col in [('t','A'),('session','C'),('p','D'),('set','E'),('req','F'),('energy','J'),('soc','K'),('ctrl_t','L'),('ctrl_s','M')]}
                for col in ('D','E','F','J','K'):missing[col]+=not ok(num(r.get(col)))
                if not ok(v['t']) or not ok(v['session']):badtime+=1;continue
                ident=str(int(v['session']))
                sessions[ident].append(v)
                if ok(v['p']):powers_by_timestamp[round(v['t']*1440)][si-1]=v['p']
                if ok(v['p']) and v['p']<0 and len(unusual)<15:unusual.append({'time':v['t'],'session':ident,'p_W':v['p'],'reason':'negative'})
            for sid, rec in sessions.items():
                rec.sort(key=lambda x:x['t']);p=np.array([x['p'] for x in rec]);t=np.array([x['t'] for x in rec])*24;energy=np.array([x['energy'] for x in rec]); req=np.array([x['req'] for x in rec]);setp=np.array([x['set'] for x in rec]);soc=np.array([x['soc'] for x in rec]);
                dt=np.diff(t);phys=(dt>0)&(dt<=2/60) # <=2 minutes, no filling
                valid_p=np.isfinite(p);valid_e=np.isfinite(energy)
                integral=float(np.sum(.5*(p[:-1][phys & valid_p[:-1] & valid_p[1:]]+p[1:][phys & valid_p[:-1] & valid_p[1:]])*dt[phys & valid_p[:-1] & valid_p[1:]])) if len(p)>1 else 0
                # dt in hours; yields Wh. A delta in cumulative session Energy is only comparable if documented.
                dE=np.diff(energy)
                bad_e=int(np.sum((dE< -1e-5)&np.isfinite(dE)))
                metrics.append({'connector':connector,'session':sid,'n_records':len(rec),
                   'first_excel_serial':rec[0]['t'],'last_excel_serial':rec[-1]['t'],
                   'gap_intervals_gt_2min':int(np.sum(dt>2/60+1e-7)),
                   'time_nonincreasing':int(np.sum(dt<=0)),
                   'measured_power_max_W':float(np.nanmax(p)),
                   'request_max_W':float(np.nanmax(req)) if np.isfinite(req).any() else None,
                   'setpoint_max_W':float(np.nanmax(setp)) if np.isfinite(setp).any() else None,
                   'P_integrated_contiguous_Wh':integral,
                   'energy_column_first_Wh':float(energy[0]) if ok(energy[0]) else None,
                   'energy_column_last_Wh':float(energy[-1]) if ok(energy[-1]) else None,
                   'energy_column_difference_Wh':float(energy[-1]-energy[0]) if ok(energy[-1]) and ok(energy[0]) else None,
                   'energy_decreases_count':bad_e,
                   'soc_start_pct':float(soc[0]) if ok(soc[0]) else None,
                   'soc_end_pct':float(soc[-1]) if ok(soc[-1]) else None,
                   'p_above_172_5kW_count':int(np.sum(p>capacity_W+1))})
            qa[connector]={'all_time_grid_rows':totalrows,'populated_session_rows':populated,'distinct_sessions':len(sessions),
                'invalid_timestamp_or_session':badtime,'missing_fields_count':dict(missing),
                'negative_power_examples':unusual}
    concurrent=0;over=0;maxsum=0;dual_times=[]
    for minute,(p1,p2) in powers_by_timestamp.items():
        a=p1 if ok(p1) else 0;b=p2 if ok(p2) else 0
        if ok(p1) and ok(p2):concurrent+=1
        total=a+b;maxsum=max(maxsum,total)
        if total>capacity_W+1:
            over+=1
            if len(dual_times)<30:dual_times.append({'excel_minute_index':minute,'CCS1_P_W':a,'CCS2_P_W':b,'sum_W':total})
    qa.update({'measured_rows_total':qa['CCS1']['populated_session_rows']+qa['CCS2']['populated_session_rows'],
       'published_count_to_verify':expected_measurements,'published_minus_populated':expected_measurements-(qa['CCS1']['populated_session_rows']+qa['CCS2']['populated_session_rows']),
       'unique_observed_minutes':len(powers_by_timestamp),'concurrent_two_connector_minutes':concurrent,
       'above_documented_station_capacity_minutes':over,'max_observed_combined_connector_P_W':maxsum,
       'station_capacity_assumed_from_source_W':capacity_W,'above_capacity_examples':dual_times,
       'source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
       'comparison_warning':'Do not infer grid AC/DC efficiencies or violate conservation based on P label until metering boundary and station rating verified. Power-integral vs Energy-column difference is a diagnostic, not a proof of equivalence.'})
    # Reconcile the independent session workbook by composite (connector, session) key.
    session_key={};session_meta={};
    if session_src and Path(session_src).exists():
        with zipfile.ZipFile(session_src) as z:
            sstr=shared(z)
            for idx,rec in enumerate(rows(z,1,sstr)):
                if idx==0:session_meta['headers']=rec;continue
                if not rec.get('A') or not rec.get('B'):continue
                connector=rec['B']
                if connector not in ('CCS1','CCS2'):continue
                # Publisher session workbook IDs are global across connectors; measurement tabs
                # restart numbering at 1. Derive (and later time-validate) the CCS2 offset.
                global_id=int(num(rec['A']))
                ident=str(global_id-1129 if connector=='CCS2' else global_id)
                key=(connector,ident)
                session_key[key]={'energy_Wh':num(rec.get('F')),'stay_min':num(rec.get('E')),'arrival':num(rec.get('C')),'departure':num(rec.get('D')),'controlled':num(rec.get('I'))}
        matched=0;missing=0;discrepancies=[];power_ratios=[]
        for row in metrics:
            key=(row['connector'],row['session'])
            si=session_key.get(key)
            if not si:missing+=1;continue
            if abs(row['first_excel_serial']-si['arrival'])*1440>3:
                missing+=1;continue  # never match solely on assumed offset
            matched+=1
            row['session_reported_energy_Wh']=si['energy_Wh']
            row['session_reported_stay_min']=si['stay_min']
            row['session_controlled_flag']=si['controlled']
            if si['energy_Wh']>100 and row['P_integrated_contiguous_Wh']>100 and row['gap_intervals_gt_2min']==0:
                power_ratios.append(row['P_integrated_contiguous_Wh']/si['energy_Wh'])
            if len(discrepancies)<20 and si['energy_Wh']>0 and row['energy_column_last_Wh'] is not None and abs(row['energy_column_last_Wh']/si['energy_Wh']-1)>.10:
                discrepancies.append({'connector':key[0],'session':key[1], 'reported_session_Wh':si['energy_Wh'],'measurement_cumulative_end_Wh':row['energy_column_last_Wh']})
        session_meta.update({'total_session_rows':len(session_key),'observed_session_keys':len(metrics),'matched_session_keys':matched,'unmatched_measurement_session_keys':missing,
           'unmatched_session_book_keys':len(session_key)-matched,'CCS2_session_id_offset_for_matching':1129,
           'median_measured_P_integral_over_session_energy_for_no_gap_sessions':float(np.median(power_ratios)) if power_ratios else None,
           'comparisons_eligible':len(power_ratios),'selected_energy_mismatch_examples':discrepancies})
        qa['session_workbook']=session_meta
    with (out/'epfl_session_energy_diagnostics.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=sorted(set().union(*(row.keys() for row in metrics))));w.writeheader();w.writerows(metrics)
    # A few robust diagnostics using observed records only; no hidden imputation
    ratios=[]
    for r in metrics:
        en=r['energy_column_difference_Wh']; integrated=r['P_integrated_contiguous_Wh']
        if en is not None and en>1000 and integrated>1000 and r['gap_intervals_gt_2min']==0: ratios.append(integrated/en)
    qa['energy_integral_to_reported_delta_ratio_median_clean_sessions']=float(np.median(ratios)) if ratios else None
    qa['no_gap_sessions_for_ratio']=len(ratios)
    (out/'epfl_summary.json').write_text(json.dumps(qa,indent=2))
    return qa

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--measurement',required=True);a.add_argument('--session',default=None);a.add_argument('--out',required=True)
    args=a.parse_args();result=run(args.measurement,args.session,args.out)
    print(json.dumps({k:result[k] for k in ['measured_rows_total','published_minus_populated','concurrent_two_connector_minutes','above_documented_station_capacity_minutes','energy_integral_to_reported_delta_ratio_median_clean_sessions']},indent=2))
