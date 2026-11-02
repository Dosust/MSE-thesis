#!/usr/bin/env python3
"""Source-preserving thesis component-data qualification workflow.

Sources are locally mounted/exported copies of the user's Google Drive data folder;
this script does NOT bypass Google Drive authentication or modify source files.

SO1: observed component thermal states / what is NOT coupled evidence.
SO2: strictly session-heldout *conditional* battery thermal predictions; independent
     transformer conditional model screening; EPFL electrical session accounting.
SO3: observed charging-session proxies only, NOT verified mobility requirements.

Python >=3.10; requires numpy and scipy. Uses stdlib ZIP/XML for streaming XLSX,
not openpyxl/pandas, and leaves all input workbooks untouched.
"""
from __future__ import annotations
import argparse, collections, csv, datetime as dt, hashlib, io, json, math, re, sys, time, zipfile
from pathlib import Path
from statistics import median
import numpy as np
from scipy.optimize import least_squares
import xml.etree.ElementTree as ET

SIGNALS=['Timestamp','RawBattCurrent132','BattVoltage132','SOCave292','BMSminPackTemperature',
         'BMSmaxPackTemperature','VCFRONT_tempAmbient','BMSdissipation312',
         'UI_batteryPreconditioningRequest','BMS_preconditionAllowed','FC_dcCurrent',
         'FC_dcVoltage','ChargeLinePower264']
# Columns used in the minute-scale conditional hindcast: see WINDOW_FEATURES
WINDOW_FEATURES=['BMSminPackTemperature','BMSmaxPackTemperature',
                 'VCFRONT_tempAmbient','RawBattCurrent132','BMSdissipation312',
                 'UI_batteryPreconditioningRequest']
KNOWN_SOURCES={
 'doi-10.48804-8kpdtw.zip':('10.48804/8KPDTW','real vehicle charging CAN records'),
 'Barug2025_sensordata.csv':('10.5281/zenodo.17223516','measured transformer sensor data'),
 'Barug2025_calculated.csv':('10.5281/zenodo.17223516','model-calculated transformer data'),
 'Measurement_data.xlsx':('none verified','measured EPFL charger AC input and controls'),
 'Session_data.xlsx':('none verified','measured EPFL charger session summaries'),
 'power_grid_transport_resilience_dataset.csv':('unknown','provenance unverified; exclude from model fitting'),
 'doi_10_5061_dryad_np5hqc04z__v20260204.zip':('10.5061/dryad.np5hqc04z','real charging demand/weather; archive inspection only'),
 'Data.rar':('unverified','network benchmark archive, not equipment thermal field data')
}

def write_csv(p, rows, cols=None):
    p.parent.mkdir(parents=True,exist_ok=True)
    rows=list(rows)
    cols=cols or sorted({k for r in rows for k in r})
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader();w.writerows(rows)

def jwrite(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,default=str,allow_nan=False),encoding='utf8')

def finite(x):
    try: y=float(x);return y if math.isfinite(y) else float('nan')
    except (ValueError,TypeError,OverflowError): return float('nan')

def stamp(s):
    if not s:return None
    try:
        v=dt.datetime.fromisoformat(s.strip().replace('Z','+00:00'))
        if v.tzinfo is None:v=v.replace(tzinfo=dt.timezone.utc)
        return v.timestamp()
    except (ValueError,OverflowError):return None

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        while b:=f.read(4*1024*1024):h.update(b)
    return h.hexdigest()

def locate(base,name):
    direct=base/name
    if direct.exists():return direct
    matches=list(base.rglob(name))
    return matches[0] if matches else None

def inventory(base,out):
    rows=[]
    names=list(KNOWN_SOURCES)+['Registered vehicles.csv','README.txt','17223516.json']
    for name in names:
        p=locate(base,name)
        if p is None and name=='Barug2025_sensordata.csv':p=locate(base,'Barug2025_sensordata(1).csv')
        if p is None and name=='power_grid_transport_resilience_dataset.csv':p=locate(base,'power_grid_transport_resilience_dataset(1).csv')
        if p:
            doi,role=KNOWN_SOURCES.get(name,('unknown','supporting context'))
            rows.append(dict(filename=name,local_path=str(p),size_bytes=p.stat().st_size,
                             sha256=sha256(p),doi=doi,role=role,
                             original_source_unmodified=True,field_coupling_verified=False))
        else:rows.append(dict(filename=name,local_path='',size_bytes='',sha256='',doi='',role='NOT_MOUNTED',original_source_unmodified='',field_coupling_verified=False))
    write_csv(out/'01_source_registry.csv',rows)
    return {r['filename']:r for r in rows}

def open_bev_zip(path):
    """Return inner ZipFile and its retained backing object (outer ZIP in memory)."""
    outer=zipfile.ZipFile(path)
    inner_files=[i for i in outer.infolist() if i.filename.endswith('.zip') and 'BEV' in i.filename]
    if inner_files:
        name=inner_files[0].filename
        # Member size is bounded by the Drive archive; no disk-wide extraction.
        innerbuf=io.BytesIO(outer.read(name))
        return outer,zipfile.ZipFile(innerbuf),innerbuf
    return outer,outer,None

def read_dbc(z):
    matches=[n for n in z.namelist() if n.lower().endswith('can.dbc')]
    if not matches:return {}
    text=z.read(matches[0]).decode('latin1')
    out={}
    for name in SIGNALS[1:]+['BMS_hvacPowerRequest','BMS_hvacPowerBudget','BMSinletActiveCoolTarget312']:
        m=re.search(r'\bSG_\s+'+re.escape(name)+r'\s*:\s*([^\r\n]+)',text)
        definition=m.group(1).strip() if m else ''
        u=re.search(r'"([^"]*)"',definition)
        out[name]={'CAN_definition':definition,'unit':u.group(1) if u else None,'present_in_dictionary':bool(m)}
    return out

def charge_csv_names(z):
    return sorted(n for n in z.namelist() if n.endswith('.csv') and ('/slow charging sessions/' in n or '/fast charging sessions/' in n))

def parse_charge(z,name,coverage=25):
    """Read selected columns, group by minute; no interpolation or forward-fill."""
    mode='DC' if '/fast charging sessions/' in name else 'AC'
    vehicle=Path(name).name.split('_')[0]
    bins=collections.defaultdict(lambda:collections.defaultdict(list))
    n=0;badtime=0;badtemp=0;dq=0;sat=0;negt=0;seen=set();begin=None;first=None
    with z.open(name) as raw:
        rr=csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8-sig',errors='replace',newline=''))
        present=set(rr.fieldnames or []);seen=present
        for d in rr:
            n+=1;t=stamp(d.get('Timestamp',''))
            if t is None:badtime+=1;continue
            minute=int(t//60)
            if first is None or t<first:first=t
            if begin is None or t>begin:begin=t
            vals={k:finite(d.get(k,'')) for k in SIGNALS[1:]}
            a,b=vals['BMSminPackTemperature'],vals['BMSmaxPackTemperature']
            if math.isfinite(a) and math.isfinite(b) and a>b:negt+=1
            if math.isfinite(a) and not (-40<=a<=100):badtemp+=1
            if math.isfinite(b) and not (-40<=b<=100):badtemp+=1
            x=vals['BMSdissipation312']
            if math.isfinite(x) and x>20:dq+=1
            if math.isfinite(x) and abs(x-20.46)<1e-4:sat+=1
            # Only plausible measured values can feed minute aggregation.
            for k in WINDOW_FEATURES:
                v=vals[k]
                if not math.isfinite(v):continue
                if k in ('BMSminPackTemperature','BMSmaxPackTemperature') and not (-40<=v<=100):continue
                if k=='VCFRONT_tempAmbient' and not (-40<=v<=80):continue
                if k=='RawBattCurrent132' and abs(v)>1100:continue
                if k=='BMSdissipation312' and not (0<=v<=20):continue
                if k=='UI_batteryPreconditioningRequest' and v not in (0,1):continue
                bins[minute][k].append(v)
    minutes=sorted(bins)
    # preserve minute offset; every entry has 6 channels (NaNs mean no observed value)
    mat=np.full((len(minutes),len(WINDOW_FEATURES)),np.nan,float)
    counts=np.zeros(len(minutes),int)
    for i,t in enumerate(minutes):
        b=bins[t]
        counts[i]=len(b.get('RawBattCurrent132',[]))
        for j,k in enumerate(WINDOW_FEATURES):
            if b.get(k):mat[i,j]=float(np.median(b[k]))
    # require adequate raw coverage per one-minute bin, no synthetic interpolation.
    mat[counts<coverage,:]=np.nan
    # candidate model only uses feature-complete minutes; no missing-signal imputation
    good=np.isfinite(mat).all(axis=1) & (mat[:,1]>=mat[:,0]) & (mat[:,1]<=110)
    if len(good):mat[~good,:]=np.nan
    qa={'file':Path(name).name,'mode':mode,'vehicle':vehicle,'raw_rows':n,
        'invalid_timestamps':badtime,'invalid_temperature_observations':badtemp,
        'negative_min_max_spread_rows':negt,'BMSdissipation_gt_20kW':dq,
        'BMSdissipation_20_46_fullscale':sat,'minutes_available':len(mat),
        'minutes_complete_and_covered':int(np.isfinite(mat).all(axis=1).sum()),
        'signals_missing':';'.join(k for k in WINDOW_FEATURES if k not in seen),
        'first_timestamp_UTC':dt.datetime.fromtimestamp(first,dt.timezone.utc).isoformat() if first else '',
        'last_timestamp_UTC':dt.datetime.fromtimestamp(begin,dt.timezone.utc).isoformat() if begin else ''}
    return dict(file=Path(name).name,source_member=name,mode=mode,vehicle=vehicle,
                start=first or 0, minutes=np.array(minutes,dtype=np.int64), x=mat),qa

def windows(session,horizon):
    t=session['minutes'];x=session['x'];
    if len(t)<=horizon:return None
    ret=[]
    # Nonoverlapping; a window never crosses a session or measurement gap.
    for idx in range(0,len(t)-horizon,horizon):
        block=x[idx:idx+horizon+1]
        if len(block)==horizon+1 and t[idx+horizon]-t[idx]==horizon and np.isfinite(block).all():
            ret.append(block)
    return np.array(ret,dtype=float) if ret else None

def assign_splits(sessions,horizon):
    by=collections.defaultdict(list)
    for s in sessions:
        v=windows(s,horizon)
        if v is not None:by[(s['vehicle'],s['mode'])].append((s,v))
    splits={key:[] for key in ['train','validation','test']}
    manifest=[]
    for key,group in sorted(by.items()):
        group.sort(key=lambda item:(item[0]['start'],item[0]['file']))
        n=len(group)
        if n<4:
            for s,v in group:manifest.append(dict(file=s['file'],vehicle=s['vehicle'],mode=s['mode'],partition='excluded_too_few_sessions',windows=len(v)))
            continue
        i=max(1,int(.6*n));j=max(i+1,int(.8*n));j=min(j,n-1)
        for part,ss in [('train',group[:i]),('validation',group[i:j]),('test',group[j:])]:
            for s,v in ss:
                splits[part].append((s,v))
                manifest.append(dict(file=s['file'],vehicle=s['vehicle'],mode=s['mode'],partition=part,windows=len(v)))
    return splits,manifest

def thermal_predict(p,X,kind):
    # All rates expressed in 1/h and temperatures in Celsius; time step 1 minute.
    # States are MINIMUM and MAXIMUM pack sensor channels, NOT mean pack temperature.
    N=len(X);T=X[:,0,:2].copy();h=(X.shape[1]-1)
    for k in range(h):
        v=X[:,k,:]
        amb=v[:,2];I2=(v[:,3]/100.)**2
        d0=(amb-T[:,0]);d1=(amb-T[:,1]); gap=(T[:,1]-T[:,0])
        if kind=='uncoupled':
            rate0=p[0]*d0+p[1]*I2
            rate1=p[2]*d1+p[3]*I2
        else:
            rate0=p[0]*d0+p[1]*I2+p[2]*gap
            rate1=p[3]*d1+p[4]*I2-p[5]*gap
            if kind=='signal_proxy':
                # BMSdissipation312: *statistical covariate only*, not physical watts of cooling.
                # Actuation/preconditioning might also be a request, not actual thermal flux.
                rate0+=p[6]*(v[:,4]/10.)+p[7]*v[:,5]
                rate1+=p[8]*(v[:,4]/10.)+p[9]*v[:,5]
        T[:,0]+=rate0/60.;T[:,1]+=rate1/60.
    return T

def thermo_bounds(kind):
    if kind=='uncoupled':
        return np.array([.001,0,.001,0]),np.array([2.,10.,2.,10.]),np.array([.1,.2,.1,.2])
    low=np.array([.001,0,0,.001,0,0]);high=np.array([2.,10.,2.,2.,10.,2.]);init=np.array([.1,.2,.1,.1,.2,.1])
    if kind=='signal_proxy':
        low=np.r_[low,[-5.,-5.,-5.,-5.]]
        high=np.r_[high,[5.,5.,5.,5.]]
        init=np.r_[init,[0.,0.,0.,0.]]
    return low,high,init

def metric(y,p):
    e=np.asarray(p)-np.asarray(y)
    return dict(N=int(e.size),MAE_C=float(np.mean(np.abs(e))),RMSE_C=float(np.sqrt(np.mean(e*e))),bias_C=float(np.mean(e)))

def joint_windows(groups):
    return np.concatenate([v for s,v in groups],axis=0)

def fit_thermal(X,kind):
    lo,hi,p0=thermo_bounds(kind)
    y=X[:,-1,:2]
    # 3 starts with robust soft-L1 to avoid a single jump dominating learning
    starts=[p0, np.clip(p0*2,lo+1e-8,hi-1e-8)]
    best=None
    for start in starts:
        opt=least_squares(lambda p:(thermal_predict(p,X,kind)-y).ravel(),
                          x0=start,bounds=(lo,hi),max_nfev=90,loss='soft_l1',f_scale=.5)
        if best is None or np.linalg.norm(opt.fun)<np.linalg.norm(best.fun):best=opt
    singular=np.linalg.svd(best.jac,compute_uv=False)
    condition=float(singular[0]/singular[-1]) if len(singular) and singular[-1]>1e-10 else None
    touched=bool(np.any(np.minimum(best.x-lo,hi-best.x)<1e-4))
    return best.x,dict(optimizer_success=bool(best.success),jacobian_condition=condition,
                       on_parameter_boundary=touched,parameter_values=best.x.tolist(),
                       parameter_bounds=[lo.tolist(),hi.tolist()],cost=float(best.cost))

def quantify_thermal(groups,horizon,out):
    modes=['AC','DC']
    reports={};prediction_rows=[]
    for mode in modes:
        filtered={k:[(s,v) for s,v in pair if s['mode']==mode] for k,pair in groups.items()}
        n_sessions={k:len(v) for k,v in filtered.items()}
        if any(n_sessions[k]<2 for k in filtered):
            reports[mode]={'gate':'BLOCKED','reason':'Insufficient independent sessions in a partition','sessions':n_sessions}
            continue
        Xtr=joint_windows(filtered['train']);Xva=joint_windows(filtered['validation']);Xte=joint_windows(filtered['test'])
        if min(map(len,(Xtr,Xva,Xte)))<10:
            reports[mode]={'gate':'BLOCKED','reason':'Insufficient independent windows','sessions':n_sessions,
                           'windows':{'train':len(Xtr),'validation':len(Xva),'test':len(Xte)}}
            continue
        yva=Xva[:,-1,:2];yte=Xte[:,-1,:2]
        candidates={}
        for kind in ('uncoupled','coupled','signal_proxy'):
            theta,info=fit_thermal(Xtr,kind)
            pva=thermal_predict(theta,Xva,kind);pte=thermal_predict(theta,Xte,kind)
            candidates[kind]={'train_fit':info,'validation':metric(yva,pva),
                              'test':metric(yte,pte),'val_predictions':pva,'test_predictions':pte,
                              'theta':theta}
        # Select ONLY using validation MAE. Future-known electrical/ambient inputs are conditional.
        selected=min(candidates,key=lambda k:candidates[k]['validation']['MAE_C'])
        v=candidates[selected];persist_va=Xva[:,0,:2];persist_te=Xte[:,0,:2]
        persist_m=metric(yte,persist_te); persist_v=metric(yva,persist_va)
        residuals=np.abs(yva-v['val_predictions']);halfwidth=np.quantile(residuals,.95,axis=0)
        coverage=((np.abs(yte-v['test_predictions'])<=halfwidth)).mean(axis=0)
        # Inference should reflect per-state model viability; no promotion of predictive covariate to physical heat.
        state_metrics={}
        ok_val=True;ok_test=True
        for k,label in enumerate(('Tmin','Tmax')):
            test=metric(yte[:,k],v['test_predictions'][:,k]);base=metric(yte[:,k],persist_te[:,k])
            val=metric(yva[:,k],v['val_predictions'][:,k]);base_val=metric(yva[:,k],persist_va[:,k])
            iv=(val['MAE_C']<base_val['MAE_C'] and val['RMSE_C']<base_val['RMSE_C'])
            it=(test['MAE_C']<base['MAE_C'] and test['RMSE_C']<base['RMSE_C'])
            ok_val&=iv;ok_test&=it
            state_metrics[label]={'validation':val,'validation_persistence':base_val,
                                  'test':test,'test_persistence':base,'improved_validation':bool(iv),
                                  'improved_test':bool(it),'validation_p95_abs_error_C':float(halfwidth[k]),
                                  'heldout_interval_coverage':float(coverage[k])}
        enough=(n_sessions['test']>=3 and len(Xte)>=20)
        rank_ok=(v['train_fit']['jacobian_condition'] is not None and v['train_fit']['jacobian_condition']<1e8)
        internal=not v['train_fit']['on_parameter_boundary']
        pred_gate=bool(ok_val and ok_test and enough and rank_ok and internal and np.all((coverage>=.85)&(coverage<=1)))
        gate=('PROVISIONAL_CONDITIONAL_PREDICTION' if pred_gate else 'BLOCKED_FOR_PHYSICAL_VALIDATION')
        reports[mode]={'gate':gate,'selected_model_by_validation':selected,'sessions':n_sessions,
                       'windows':{'train':len(Xtr),'validation':len(Xva),'test':len(Xte)},
                       'candidate_metrics':{kind:{'validation':x['validation'],'test':x['test'],
                           'fit':x['train_fit']} for kind,x in candidates.items()},
                       'state_metrics':state_metrics,'sufficient_test':enough,
                       'stable_identifiability':rank_ok,'interior_parameters':internal,
                       'predictive_gate':pred_gate,'physical_gate':'BLOCKED: heat capacity, sensor location, actual cooling flux and heat losses not identified'}
        offset=0
        for s,X in filtered['test']:
            block=v['test_predictions'][offset:offset+len(X)]
            for i,(w,pred) in enumerate(zip(X,block)):
                prediction_rows.append(dict(mode=mode,vehicle=s['vehicle'],file=s['file'],horizon_min=horizon,
                                            window=i,observed_Tmin_C=float(w[-1,0]),observed_Tmax_C=float(w[-1,1]),
                                            predicted_Tmin_C=float(pred[0]),predicted_Tmax_C=float(pred[1]),
                                            persistence_Tmin_C=float(w[0,0]),persistence_Tmax_C=float(w[0,1]),
                                            model=selected,uses_observed_future_inputs=True))
            offset+=len(X)
    write_csv(out/f'02_KU_Leuven_predictions_{horizon}min.csv',prediction_rows)
    return reports

def bev_pipeline(base,out,archive,horizons):
    qa=[];sessions=[]
    outer,z,buf=open_bev_zip(archive)
    try:
        dbc=read_dbc(z);jwrite(out/'02_KU_Leuven_CAN_dictionary.json',dbc)
        files=charge_csv_names(z)
        print(f'[KU Leuven] Found {len(files)} AC/DC CSVs',flush=True)
        for i,name in enumerate(files):
            try:
                s,q=parse_charge(z,name)
                sessions.append(s);qa.append(q)
            except Exception as e:
                qa.append({'file':Path(name).name,'error':type(e).__name__+': '+str(e)[:200]})
            if (i+1)%35==0:print(f'[KU Leuven] audited {i+1}/{len(files)}',flush=True)
        write_csv(out/'02_KU_Leuven_session_QA.csv',qa)
        reports={}
        for h in horizons:
            splits,manifest=assign_splits(sessions,h)
            write_csv(out/f'02_KU_Leuven_splits_{h}min.csv',manifest)
            reports[str(h)]=quantify_thermal(splits,h,out)
        r={'source_doi':'10.48804/8KPDTW','files':len(files),'sessions_read':len(sessions),
           'mean_pack_temperature_measured':False,'uncoupled_installation':True,
           'BMSdissipation312_semantics':'uncertain; fitted statistical covariate only',
           'future_inputs':'measured current, ambient and BMS signals through target horizon; conditional hindcast, NOT prospective forecast',
           'charging_current_sign':'observed predominantly negative, charging sign not manufacturer-verified',
           'mode_horizon_results':reports,
           'qualification':'ONLY conditional component dynamics; never transformer–EVSE field coupling'}
        jwrite(out/'02_KU_Leuven_report.json',r)
        return r
    finally:
        if z is not outer:z.close()
        outer.close()
        if buf is not None:buf.close()

# XLSX streaming from OOXML using only the standard library.
# This deliberately DOES NOT write/edit the workbook or use alternate spreadsheet packages.
_NS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
def xlsx_strings(z):
    if 'xl/sharedStrings.xml' not in z.namelist():return []
    with z.open('xl/sharedStrings.xml') as f:
        root=ET.parse(f).getroot()
    return [''.join(node.text or '' for node in si.iter() if node.tag==_NS+'t') for si in root]

def xlsx_rows(z,sheet,strings,max_rows=None):
    with z.open(sheet) as f:
        # Iteration by row, clearing accumulated XML nodes regularly.
        context=ET.iterparse(f,events=('start','end'))
        root=None;count=0
        for event,elem in context:
            if root is None and event=='start':root=elem
            if event=='end' and elem.tag==_NS+'row':
                out={}
                for c in elem:
                    if c.tag!=_NS+'c':continue
                    letter=re.match('[A-Z]+',c.attrib.get('r',''))
                    if not letter:continue
                    v=c.find(_NS+'v')
                    if v is None:
                        inline=c.find(_NS+'is')
                        if inline is None:continue
                        txt=''.join(n.text or '' for n in inline.iter() if n.tag==_NS+'t')
                    else:
                        txt=v.text
                        if c.attrib.get('t')=='s':
                            try:txt=strings[int(txt)]
                            except (ValueError,IndexError,TypeError):txt=''
                    out[letter.group()]=txt
                count+=1
                yield out
                elem.clear()
                if count%1000==0 and root is not None:root.clear()
                if max_rows and count>=max_rows:break

def excel_time(serial):
    v=finite(serial)
    if math.isfinite(v) and 30000<v<70000:
        return (dt.datetime(1899,12,30,tzinfo=dt.timezone.utc)+dt.timedelta(days=v)).timestamp()
    return stamp(serial)

def epfl_pipeline(out,measurefile,sessionfile,maxrows):
    if not measurefile or not sessionfile:return {'gate':'BLOCKED','reason':'EPFL original XLSX files absent'}
    results={'measured_file':measurefile.name,'sessions_file':sessionfile.name,
             'measurement_rows_examined':0,'populated_measurement_rows':0,
             'station_or_feeder_power_measured':False,
             'power_boundary':'P(W) is reported station AC power; must verify whether per connector or total',
             'temperature_channels_available':False,
             'original_source_is_xlsx':True,'charging_service_proxies_only':True}
    # Session summary: caller must not interpret Pmax > 172.5kW as necessarily impossible without boundary/definition verification.
    with zipfile.ZipFile(sessionfile) as z:
        strs=xlsx_strings(z)
        rows=iter(xlsx_rows(z,'xl/worksheets/sheet1.xml',strs))
        header=next(rows)
        head={key:v for key,v in header.items() if v}
        counts=collections.Counter();identifiers=set();energy_positive=0;pmax_gt=0;session_meta={}
        for row in rows:
            v={head[c]:raw for c,raw in row.items() if c in head}
            sid=str(v.get('Session','')).strip()
            if not sid:continue
            sc=str(v.get('CCS',''));identifiers.add((sc,sid));counts['n_rows']+=1
            session_meta[(sc,sid)]={'reported_energy_Wh':finite(v.get('Energy (Wh)')),'reported_Pmax_W':finite(v.get('Pmax (W)')),'arrival_UTC_s':excel_time(v.get('Arrival'))}
            if finite(v.get('Controlled session (0=False, 1=True)'))==1:counts['controlled']+=1
            if finite(v.get('Energy (Wh)'))>0:energy_positive+=1
            if finite(v.get('Pmax (W)'))>172500:pmax_gt+=1
        results.update(session_distinct=len(identifiers),session_rows=counts['n_rows'],
                       controlled_sessions=counts['controlled'],
                       positive_energy_sessions=energy_positive,
                       Pmax_above_172500W_sessions=pmax_gt)
    # Stream 2 x ~100-MB XML worksheets, avoid loading entire sheets into memory.
    measurement_summary={};measure_rows=[]
    with zipfile.ZipFile(measurefile) as z:
        strs=xlsx_strings(z)
        for sheet in sorted(n for n in z.namelist() if re.fullmatch(r'xl/worksheets/sheet\d+\.xml',n)):
            it=iter(xlsx_rows(z,sheet,strs,max_rows=maxrows))
            head0=next(it,{})
            head={k:v for k,v in head0.items() if v}
            stat=collections.Counter();session_count=collections.Counter()
            last=collections.defaultdict(lambda:None);energy=collections.defaultdict(float)
            first=collections.defaultdict(lambda:None);last_time={}
            for row in it:
                stat['examined']+=1
                v={head[k]:raw for k,raw in row.items() if k in head}
                sid=str(v.get('Session','')).strip()
                p=finite(v.get('P (W)'))
                if not sid or not math.isfinite(p):continue
                stat['populated']+=1
                session_count[sid]+=1
                t=excel_time(v.get('Date and time'))
                # Determine measured sampling and integrate actual AC input only over continuous 1--2min intervals.
                if t is not None:
                    prev=last[sid]
                    if prev is not None:
                        dt_s=t-prev[0]
                        if 0<dt_s<=120:
                            energy[sid]+=.5*(p+prev[1])*dt_s/3600.0
                            stat['integrable_intervals']+=1
                        elif dt_s<=0:stat['reversed_or_duplicate_time']+=1
                        else:stat['gaps_gt_2min']+=1
                    last[sid]=(t,p);first[sid]=t if first[sid] is None else first[sid];last_time[sid]=t
                if p<0:stat['negative_power_rows']+=1
                if p>172500:stat['P_above_172500W_rows']+=1
                if finite(v.get('Pset (W)'))>=0:stat['nonnegative_setpoint_rows']+=1
            entry=dict(sheet=sheet,headers=head,n_examined=stat['examined'],n_populated=stat['populated'],
                       n_sessions=len(session_count),integrable_intervals=stat['integrable_intervals'],
                       negative_power_rows=stat['negative_power_rows'],
                       power_above_station_rating_rows=stat['P_above_172500W_rows'],
                       sum_integrated_Wh_on_contiguous_observed_intervals=float(sum(energy.values())),
                       time_gaps_gt_2min=stat['gaps_gt_2min'],
                       nonmonotone_time_events=stat['reversed_or_duplicate_time'])
            measurement_summary[sheet]=entry
            results['measurement_rows_examined']+=stat['examined'];results['populated_measurement_rows']+=stat['populated']
            print(f"[EPFL] {sheet}: {stat['populated']} populated, {stat['examined']} scanned",flush=True)
            ccs='CCS1' if 'sheet1' in sheet else 'CCS2'
            for sid,n in session_count.items():
                # Important source quirk: measurement worksheet CCS2 IDs restart from 1,
                # while Session_data.xlsx uses global IDs 1130..1878.
                # Verify the resulting match by comparing first measurement time to Arrival.
                gid=str(int(sid)+1129) if ccs=='CCS2' and sid.isdigit() else sid
                original=session_meta.get((ccs,gid),{})
                e_wh=energy.get(sid,float('nan'));reported=original.get('reported_energy_Wh',float('nan'))
                measure_rows.append({'sheet':sheet,'CCS':ccs,'session_id':sid,'observed_rows':n,
                     'integrated_AC_Wh_contiguous_only':round(e_wh,5) if math.isfinite(e_wh) else '',
                     'session_summary_global_id':gid,
                     'measured_start_minus_summary_arrival_seconds':(round(first[sid]-original['arrival_UTC_s'],3) if first.get(sid) is not None and isinstance(original.get('arrival_UTC_s'),(int,float)) else ''),
                     'reported_session_energy_Wh':reported if math.isfinite(reported) else '',
                     'integrated_minus_reported_Wh':(round(e_wh-reported,5) if math.isfinite(e_wh) and math.isfinite(reported) else ''),
                     'relative_error_vs_reported':((e_wh-reported)/reported if math.isfinite(reported) and reported>0 else ''),
                     'reporting_boundary_unverified':True})
    write_csv(out/'04_EPFL_measurement_session_audit.csv',measure_rows)
    paired=[r for r in measure_rows if isinstance(r['relative_error_vs_reported'],float) and math.isfinite(r['relative_error_vs_reported'])]
    linked=[r for r in measure_rows if isinstance(r['measured_start_minus_summary_arrival_seconds'],float)]
    results['session_energy_reconciliation']={
      'matched_sessions':len(paired),
      'start_timestamp_matches_within_60s':sum(abs(r['measured_start_minus_summary_arrival_seconds'])<=60 for r in linked),
      'start_timestamp_validation_count':len(linked),
      'max_absolute_start_timestamp_mismatch_seconds':max((abs(r['measured_start_minus_summary_arrival_seconds']) for r in linked),default=None),
      'total_integrated_AC_Wh_contiguous_only':float(sum(r['integrated_AC_Wh_contiguous_only'] for r in paired)),
      'total_reported_session_energy_Wh':float(sum(r['reported_session_energy_Wh'] for r in paired)),
      'median_absolute_relative_difference':float(np.median([abs(r['relative_error_vs_reported']) for r in paired])) if paired else None,
      'fraction_within_10pct':float(np.mean([abs(r['relative_error_vs_reported'])<=.1 for r in paired])) if paired else None,
      'CCS2_local_to_global_session_offset':1129,
      'NOT_confirmed_energy_balance':True}
    results['sheets']=measurement_summary
    results['published_n_measurements']=64277
    results['difference_from_published_count']=results['populated_measurement_rows']-64277
    results['gate']='PROVISIONAL'
    results['limitations']=['Source summary energy and integrated power use potentially different accounting boundaries; differences are not immediately electrical losses',
                            'What constitutes a published measurement needs reconciliation with paper and 1-minute tabs',
                            'P(W) grid-versus-connector boundary and control semantics require original station documentation',
                            'Session energy and integrated power may use different time/integration definitions',
                            'No measured charger internal temperatures or same-site transformer temperatures.']
    jwrite(out/'04_EPFL_report.json',results)
    return results

def sintef_pipeline(out,path):
    if not path:return {'gate':'BLOCKED','reason':'SINTEF raw CSV absent'}
    rec=[]
    with path.open(newline='',encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            t=stamp(row.get('Timestamp',''))
            if t is None:continue
            vals=[finite(row.get(k,'')) for k in ['Ambient [degC]','Current [A]','Top oil [degC]','Hot-spot HV [degC]']]
            if all(map(math.isfinite,vals)):rec.append((t,*vals))
    a=np.array(rec,float);a=a[np.argsort(a[:,0])]
    if len(a)<1000:return {'gate':'BLOCKED','reason':'Not enough complete SINTEF records'}
    t=a[:,0];Ta,I,T_o,T_h=a[:,1:].T
    gaps=int(np.sum(np.diff(t)>3600*1.1));duplicate=int(np.sum(np.diff(t)==0))
    # Splits by absolute date, no future leakage for params/model choice.
    tr=dt.datetime(2024,7,1,tzinfo=dt.timezone.utc).timestamp()
    va=dt.datetime(2024,10,1,tzinfo=dt.timezone.utc).timestamp()
    # Conditional hindcast: observed future current + ambient, no unknown future meteorology prediction.
    def collect(h):
        groups={'train':[],'validation':[],'test':[]}
        for k in range(0,len(a)-h,h):
            if not np.all(np.abs(np.diff(t[k:k+h+1])-3600)<2):continue
            if (t[k]<tr<=t[k+h]) or (t[k]<va<=t[k+h]):continue
            group='train' if t[k+h]<tr else 'validation' if t[k+h]<va else 'test'
            groups[group].append(a[k:k+h+1])
        return {key:np.array(v) for key,v in groups.items()}
    def propagate(p,X):
        # Effective first-order oil/winding dynamics, NOT IEEE/IEC qualified hotspot law.
        oil=X[:,0,3].copy();hot=X[:,0,4].copy()
        # ref current 100A, observed future meteorology and electrical inputs
        for i in range(X.shape[1]-1):
            Ta=X[:,i,1];curr=(X[:,i,2]/100)**2
            oil_prev=oil.copy()
            oil+=(p[0]*(Ta-oil)+p[1]*curr+p[2])
            hot+=(p[3]*(oil_prev-hot)+p[4]*curr+p[5])
        return np.stack([oil,hot],axis=-1)
    split=collect(6)
    if any(len(x)<20 for x in split.values()):return {'gate':'BLOCKED','reason':'Insufficient 6h windows'}
    Xtr,Xva=split['train'],split['validation']
    lo=[.0001,0,-3,.0001,0,-3];hi=[.95,15,3,.95,15,3];start=[.08,.05,0,.12,.05,0]
    opt=least_squares(lambda p:(propagate(p,Xtr)-Xtr[:,-1,3:5]).ravel(),start,bounds=(lo,hi),
                      max_nfev=140,loss='soft_l1',f_scale=.5)
    pars=opt.x
    residual=np.abs(propagate(pars,Xva)-Xva[:,-1,3:5]);width=np.quantile(residual,.95,axis=0)
    report={'gate':'PROVISIONAL','source_doi':'10.5281/zenodo.17223516','records':len(a),
            'gaps_over_1hr':gaps,'duplicate_timestamps':duplicate,'ambient_C_observed_minmax':[float(np.min(Ta)),float(np.max(Ta))],
            'model':'effective two-state top-oil and HV-hotspot conditional ODE discrete h=1h, nonphysical constant bias; not a manufacturer rating law',
            'parameters':pars.tolist(),'training_window_length_hours':6,
            'val_residual_abs_q95_C':width.tolist(),'metrics':{},
            'claims_not_authorized':['Extreme heat field validation (Norwegian ambient exposure only)',
                                     'Transformer hot-spot capacity restriction on unrelated 350kVA transformer',
                                     'Same-site EVSE connection; feedback P<->Te']}
    for h in [1,6,24]:
        g=collect(h)
        if not len(g['test']):continue
        X=g['test'];y=X[:,-1,3:5];ph=propagate(pars,X);baseline=X[:,0,3:5]
        coverage=(np.abs(ph-y)<=width).mean(axis=0)
        report['metrics'][str(h)+'h']={'n_nonoverlapping_test_windows':len(X),
                     'top_oil':{'model':metric(y[:,0],ph[:,0]),'persistence':metric(y[:,0],baseline[:,0])},
                     'HV_hotspot':{'model':metric(y[:,1],ph[:,1]),'persistence':metric(y[:,1],baseline[:,1])},
                     'coverage_using_6h_validation_halfwidth':[float(x) for x in coverage]}
    jwrite(out/'03_SINTEF_report.json',report)
    return report

def archive_inventory(out,p,label):
    if not p:return {'status':'NOT_MOUNTED'}
    try:
        with zipfile.ZipFile(p) as z:
            entries=[i for i in z.infolist() if not i.is_dir()]
            # Do not decompress private/unreviewed bulk archives
            result={'status':'INSPECTED_ARCHIVE_ONLY','source':label,'members':len(entries),
                   'compressed_bytes':p.stat().st_size,
                   'sample_members':[{'name':i.filename,'bytes':i.file_size} for i in entries[:35]],
                   'no_physical_thermal_validation_performed':True}
            jwrite(out/'01_'+label+'_archive_manifest.json',result);return result
    except (OSError,zipfile.BadZipFile) as e:return {'status':'ARCHIVE_ERROR','error':str(e)}

def selftest():
    X=np.zeros((2,6,6));X[:,:,0]=20;X[:,:,1]=24;X[:,:,2]=26;X[:,:,3]=100
    for kind in ('uncoupled','coupled','signal_proxy'):
        a,b,p=thermo_bounds(kind)
        assert np.all(np.isfinite(thermal_predict(p,X,kind)))
        assert thermal_predict(p,X,kind).shape==(2,2)
    # Zero forcing, equal ambient + initial temps => unchanged state.
    X[:,:,:]=0;X[:,:,0]=20;X[:,:,1]=20;X[:,:,2]=20
    for kind in ('uncoupled','coupled','signal_proxy'):
        *_,p=thermo_bounds(kind)
        assert np.allclose(thermal_predict(p,X,kind),20)
    assert stamp('2024-01-01 00:00:00+00:00') is not None
    print('[selftest] Thermal model integrations and time parser OK')

def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--drive-dir',default='/mnt/data',help='Folder with downloaded Drive exports; may be Colab-mounted Drive directory')
    cli.add_argument('--out',default='/mnt/data/Thesis_Drive_Pipeline_V3/results')
    cli.add_argument('--horizons',default='5,15',help='Comma-separated horizons (minutes)')
    cli.add_argument('--epfl-max-rows',type=int,default=None,help='Optional FAST DEMO cap per EPFL sheet; capped run is NOT a complete audit')
    cli.add_argument('--skip-epfl-raw',action='store_true')
    cli.add_argument('--skip-vehicle',action='store_true')
    cli.add_argument('--skip-sintef',action='store_true')
    cli.add_argument('--self-test',action='store_true')
    args=cli.parse_args();selftest()
    if args.self_test:return
    base=Path(args.drive_dir);out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    horizons=[int(x) for x in args.horizons.split(',')]
    if any(h<1 or h>60 for h in horizons):raise ValueError('Horizon must be 1–60 minutes')
    print('[start] source integrity registry',flush=True)
    registry=inventory(base,out)
    bev=locate(base,'doi-10.48804-8kpdtw.zip') or locate(base,'BEV_energy_dynamic_data_V2_nested.zip')
    sintef=locate(base,'Barug2025_sensordata.csv') or locate(base,'Barug2025_sensordata(1).csv')
    epfl=locate(base,'Measurement_data.xlsx');sessions=locate(base,'Session_data.xlsx')
    reports={'data_scope':'multiple independent physical installations; NEVER a synchronized coupled field dataset',
             'source_registry':str(out/'01_source_registry.csv'),'component_gates':{},
             'users_original_Google_Drive_files_changed':False,
             'epfl_raw_scan_capped':args.epfl_max_rows is not None}
    if bev and not args.skip_vehicle:
        reports['KU_Leuven']=bev_pipeline(base,out,bev,horizons)
        reports['component_gates']['vehicle']='BLOCKED_FOR_PHYSICAL_VALIDATION'
    else:reports['component_gates']['vehicle']='BLOCKED: data not mounted or skipped'
    if sintef and not args.skip_sintef:
        reports['SINTEF']=sintef_pipeline(out,sintef)
        reports['component_gates']['transformer']=reports['SINTEF'].get('gate','BLOCKED')
    else:reports['component_gates']['transformer']='BLOCKED: data not mounted or skipped'
    if epfl and sessions and not args.skip_epfl_raw:
        reports['EPFL']=epfl_pipeline(out,epfl,sessions,args.epfl_max_rows)
        reports['component_gates']['charging_interface']='PROVISIONAL' if args.epfl_max_rows is None else 'INCOMPLETE_FAST_DEMO'
    else:reports['component_gates']['charging_interface']='BLOCKED: files missing or skipped'
    reports['UrbanEV']=archive_inventory(out,locate(base,'doi_10_5061_dryad_np5hqc04z__v20260204.zip'),'UrbanEV')
    reports['component_gates'].update(EVSE_internal_temperature='BLOCKED: no internal EVSE temperature data in Drive',
                                       P_to_Te='BLOCKED: no connected site field proof',
                                       Te_to_P='BLOCKED: no connected site field proof',
                                       field_qualified_synthetic='BLOCKED: candidate component models not fully qualified')
    jwrite(out/'00_FINAL_GATE_REPORT.json',reports)
    print(json.dumps({'results':str(out),'component_gates':reports['component_gates']},indent=2),flush=True)

if __name__=='__main__':main()
