#!/usr/bin/env python3
"""Session-separated KU Leuven pack-maximum temperature MODEL SCREEN (not certified physical validation).
Uses actual source ZIP and no silent gap interpolation. Predictions are conditional hindcasts: future
measured charging current and ambient-temperature paths are given, not forecast.
"""
from __future__ import annotations
import io, os, re, json, hashlib, csv, zipfile
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
SRC=Path(os.environ.get('BEV_SOURCE',str(ROOT.parent/'doi-10.48804-8kpdtw.zip')))
OUT=Path(__file__).resolve().parent
QA=ROOT/'01_provenance'
H=90 # 10s samples, 15 min horizon
STRIDE={'train':12,'validation':12,'test':6} # 120s / 120s / 60s
FEATURES=['Timestamp','RawBattCurrent132','BMSminPackTemperature','BMSmaxPackTemperature','VCFRONT_tempAmbient','SOCave292','BMS_preconditionAllowed','UI_batteryPreconditioningRequest']


def as_episode(d, sess, mode, epi, src_hash):
    if len(d)<H+2:return None
    idx=np.arange(0,len(d),10,dtype=int)
    if len(d)-idx[-1]>=8:idx=np.r_[idx,len(d)-1]
    d=d.iloc[idx].copy()
    if len(d)<H+2:return None
    t=(d['Timestamp'].astype('int64').to_numpy()/1e9)
    if np.any(np.diff(t)>12) or np.any(np.diff(t)<=0):return None
    return dict(name=sess,mode=mode,vehicle=sess.split('_')[0],episode=epi,sha256=src_hash,
       t=t-t[0],I=d['RawBattCurrent132'].to_numpy(float),Ta=d['VCFRONT_tempAmbient'].to_numpy(float),
       y=d['BMSmaxPackTemperature'].to_numpy(float),low=d['BMSminPackTemperature'].to_numpy(float),
       soc=d['SOCave292'].to_numpy(float), pre=d.get('BMS_preconditionAllowed',pd.Series(np.nan,index=d.index)).to_numpy(float))

def load_archive():
    episodes=[]; audits=[]; source_files=[]
    with zipfile.ZipFile(SRC) as outer:
        nestedname='BEV energy dynamic data_V2.zip'
        with outer.open(nestedname) as f:
            with zipfile.ZipFile(f) as inner:
                names=[n for n in inner.namelist() if n.endswith('.csv') and ('/fast charging sessions/' in n or '/slow charging sessions/' in n)]
                for n in sorted(names):
                    by=inner.read(n);sha=hashlib.sha256(by).hexdigest();file=Path(n).name
                    mode='DC' if '/fast charging sessions/' in n else 'AC'
                    try:raw=pd.read_csv(io.BytesIO(by),low_memory=False)
                    except Exception as e:
                        audits.append(dict(file=file,mode=mode,error=str(e)));continue
                    nd=len(raw);req=['Timestamp','RawBattCurrent132','BMSminPackTemperature','BMSmaxPackTemperature','VCFRONT_tempAmbient','SOCave292']
                    absent=[x for x in req if x not in raw.columns]
                    if absent:
                        audits.append(dict(file=file,mode=mode,raw_rows=nd,missing_headers=';'.join(absent)));continue
                    d=raw[[x for x in FEATURES if x in raw.columns]].copy()
                    d['Timestamp']=pd.to_datetime(d['Timestamp'],errors='coerce',utc=True)
                    for k in d.columns:
                        if k!='Timestamp':d[k]=pd.to_numeric(d[k],errors='coerce')
                    ts_valid=d['Timestamp'].notna().sum()
                    duplicate=int(d.dropna(subset=['Timestamp'])['Timestamp'].duplicated().sum())
                    # Mask rows with essential measurements missing; gap detection handles all breaks.
                    nonna=d.dropna(subset=req).copy()
                    nonna=nonna.sort_values('Timestamp').drop_duplicates(subset=['Timestamp'])
                    # All sensor ranges retained in QA; no imputation or raw edits.
                    if len(nonna):
                        times=(nonna['Timestamp'].astype('int64').to_numpy()/1e9)
                        split_idx=np.r_[0,np.where(np.diff(times)>2)[0]+1,len(nonna)]
                    else:split_idx=[0,0]
                    num_epi=0
                    for jj,(st,en) in enumerate(zip(split_idx[:-1],split_idx[1:])):
                        ep=as_episode(nonna.iloc[st:en],file,mode,jj,sha)
                        if ep:
                            episodes.append(ep);num_epi+=1
                    audits.append(dict(file=file,mode=mode,raw_rows=nd,valid_timestamps=int(ts_valid),duplicate_timestamps=duplicate,
                        valid_required_rows=len(nonna),eligible_15min_episodes=num_epi,
                        min_pack_temp_C=float(nonna['BMSminPackTemperature'].min()) if len(nonna) else None,
                        max_pack_temp_C=float(nonna['BMSmaxPackTemperature'].max()) if len(nonna) else None,
                        max_minus_min_temp_median_C=float((nonna['BMSmaxPackTemperature']-nonna['BMSminPackTemperature']).median()) if len(nonna) else None,
                        ambient_min_C=float(nonna['VCFRONT_tempAmbient'].min()) if len(nonna) else None,
                        ambient_max_C=float(nonna['VCFRONT_tempAmbient'].max()) if len(nonna) else None,
                        current_min_A=float(nonna['RawBattCurrent132'].min()) if len(nonna) else None,
                        current_max_A=float(nonna['RawBattCurrent132'].max()) if len(nonna) else None,
                        soc_min_pct=float(nonna['SOCave292'].min()) if len(nonna) else None,
                        soc_max_pct=float(nonna['SOCave292'].max()) if len(nonna) else None,
                        is_chargeline_power_zero= bool(np.nanmax(np.abs(pd.to_numeric(raw.get('ChargeLinePower264',pd.Series([np.nan])),errors='coerce'))) == 0) if 'ChargeLinePower264' in raw and raw['ChargeLinePower264'].notna().any() else None))
                    source_files.append(dict(source_path=n,sha256=sha,size_bytes=len(by),source_type='measured_original_unmodified'))
    pd.DataFrame(audits).to_csv(QA/'KU_Leuven_session_QA.csv',index=False)
    pd.DataFrame(source_files).to_csv(QA/'KU_Leuven_original_CSV_SHA256.csv',index=False)
    return episodes, audits

def make_windows(episodes):
    w=[]
    for ep in episodes:
        veh=ep['vehicle'];n=len(ep['y']);
        for j in range(0,n-H,6):
            # no gap >12s and true elapsed duration near 900 seconds
            elapsed=ep['t'][j+H]-ep['t'][j]
            if not (895<=elapsed<=910):continue
            w.append(dict(veh=veh,name=ep['name'],mode=ep['mode'],episode=ep['episode'],start=j))
    return w

def pick_split(episodes):
    # Split by complete file: never a row or a time window within the same CSV in two partitions.
    groups={}
    for e in episodes:
        groups.setdefault((e['vehicle'],e['mode']),set()).add(e['name'])
    manifest=[];maps={}
    for (veh,mode),val in sorted(groups.items()):
        names=sorted(val);n=len(names)
        if n<5:
            for name in names:maps[name]='insufficient_sessions';manifest.append(dict(vehicle=veh,mode=mode,name=name,split='insufficient_sessions'))
            continue
        # Minimum 1 validation and 1 test session, and >= 3 training sessions.
        ntr=max(3,int(n*.6));nval=max(1,int(n*.2));ntr=min(ntr,n-2);nval=min(nval,n-ntr-1)
        for i,name in enumerate(names):
            split='train' if i<ntr else 'validation' if i<ntr+nval else 'test'
            maps[name]=split;manifest.append(dict(vehicle=veh,mode=mode,name=name,split=split))
    pd.DataFrame(manifest).to_csv(OUT/'session_splits.csv',index=False)
    return maps

def pred15(ep,starts,theta,model):
    # Variable-step stable integration, with each driving signal piecewise constant.
    # dT/dt = alpha I² + beta(Ta-T) [+ q0], alpha >=0, beta >=0.
    alpha=theta[0]*1e-7;beta=theta[1]*1e-4;q=theta[2]*1e-3 if model=='netheat' else 0.
    x=ep['y'][starts].astype(float).copy()
    for h in range(H):
        k=starts+h
        dt=ep['t'][k+1]-ep['t'][k]
        forcing=alpha*ep['I'][k]**2+beta*ep['Ta'][k]+q
        decay=np.exp(-beta*dt)
        x=decay*x+np.where(beta>1e-11,-np.expm1(-beta*dt)/max(beta,1e-11),dt)*forcing
    return x

def baseline_recent(ep,starts):
    # Recent-temperature 5min slope; if unavailable, persistence.
    baseline=ep['y'][starts].copy()
    q=starts>=30
    dt=ep['t'][starts[q]]-ep['t'][starts[q]-30]
    slopes=(ep['y'][starts[q]]-ep['y'][starts[q]-30])/dt
    baseline[q]+=slopes*900
    return baseline

def generate_cases(episodes,assign):
    cases={}
    for ep in episodes:
        split=assign.get(ep['name'],'none');ifok=split in ('train','validation','test')
        if not ifok:continue
        stride=STRIDE[split]
        starts=np.arange(0,len(ep['y'])-H,stride,dtype=int)
        eligible=[]
        for j in starts:
            gap=ep['t'][j+H]-ep['t'][j]
            if 895<=gap<=910 and np.max(np.diff(ep['t'][j:j+H+1]))<=12:eligible.append(j)
        if len(eligible)==0:continue
        cases[(ep['name'],ep['episode'])]=(ep,np.asarray(eligible,dtype=int),split)
    return cases

def fit_model(cases,vehicle,mode,model):
    train=[(e,starts) for e,starts,split in cases.values() if split=='train' and e['vehicle']==vehicle and e['mode']==mode]
    if not train:return None
    # Equal-weight each episode instead of each heavily overlapping data point.
    def residual(theta):
        return np.concatenate([(pred15(ep,st,theta,model)-ep['y'][st+H])/np.sqrt(len(st)) for ep,st in train])
    if model=='netheat': bounds=([0,0,-1.0],[200,100,1.0]);start=[1.0,1.0,0]
    else:bounds=([0,0],[200,100]);start=[1.0,1.0]
    fit=least_squares(residual,np.asarray(start),bounds=bounds,max_nfev=100,ftol=1e-7,xtol=1e-7,gtol=1e-7)
    return fit

def per_case_rows(cases,veh,mode,model,params):
    rows=[]; forecasts=[]
    for ep,st,split in cases.values():
        if ep['vehicle']!=veh or ep['mode']!=mode:continue
        pred=pred15(ep,st,params,model) if model not in ('persistence','trend') else ep['y'][st] if model=='persistence' else baseline_recent(ep,st)
        true=ep['y'][st+H]
        for j,k in enumerate(st):
            forecasts.append(dict(vehicle=veh,mode=mode,session=ep['name'],episode=ep['episode'],split=split,model=model,
                 start_sec=float(ep['t'][k]),end_sec=float(ep['t'][k+H]),initial_temp_C=float(ep['y'][k]),
                 observed_temp_C=float(true[j]),predicted_temp_C=float(pred[j]),error_C=float(pred[j]-true[j]),
                 observed_ambient_C=float(ep['Ta'][k+H]),initial_soc_pct=float(ep['soc'][k]),
                 observed_current_A=float(ep['I'][k+H])))
        err=pred-true
        rows.append(dict(vehicle=veh,mode=mode,session=ep['name'],episode=ep['episode'],split=split,model=model,
           horizons=len(st),rmse_C=float(np.sqrt(np.mean(err**2))),mae_C=float(np.mean(np.abs(err))),bias_C=float(np.mean(err))))
    return rows,forecasts

def main():
    if not SRC.exists():raise FileNotFoundError(SRC)
    QA.mkdir(exist_ok=True,parents=True)
    print('Reading archive and auditing originals',flush=True)
    eps,audits=load_archive();assign=pick_split(eps)
    cases=generate_cases(eps,assign)
    print('eligible episodes',len(eps),'cases',len(cases),'windows',sum(len(x[1]) for x in cases.values()),flush=True)
    allmetrics=[];allpred=[];fits={};selection=[]
    for veh,mode in sorted(set((e['vehicle'],e['mode']) for e in eps)):
        key=veh+'_'+mode
        if not any(e['vehicle']==veh and e['mode']==mode and split=='test' for e,st,split in cases.values()):continue
        modelruns={}
        for model in ['persistence','trend','thermal','netheat']:
            fit=fit_model(cases,veh,mode,model) if model in ('thermal','netheat') else None
            params=fit.x if fit is not None else []
            rows,preds=per_case_rows(cases,veh,mode,model,params)
            if not rows:continue
            modelruns[model]=dict(fit=fit,params=list(map(float,params)),metrics=rows,pred=preds)
            # Record all predictions, but selection only from validation data
            if fit is not None:
                fits.setdefault(key,{})[model]=dict(parameters_scaled=list(map(float,fit.x)),success=bool(fit.success),fit_cost=float(fit.cost),parameter_lower_bound=[0,0]+([-1] if model=='netheat' else []),parameter_upper_bound=[200,100]+([1] if model=='netheat' else []),
                  alpha_C_per_s_per_A2=float(fit.x[0]*1e-7),beta_per_s=float(fit.x[1]*1e-4),q0_C_per_s=float(fit.x[2]*1e-3) if model=='netheat' else None,
                  hit_boundary=bool(np.any(fit.x<=np.asarray(fit.bounds[0]) if hasattr(fit,'bounds') else False)))
            allmetrics+=rows;allpred+=preds
        def vscore(m):
            r=[v['mae_C'] for v in modelruns[m]['metrics'] if v['split']=='validation']
            return float(np.mean(r)) if r else np.inf
        if not modelruns:continue
        # Test model choice: physically constrained thermal if its val MAE better than persistence;
        # else baseline. The unconstrained nuisance model is only a diagnostic and cannot pass physics gate.
        baseline=min(('persistence','trend'),key=vscore)
        candidate='thermal'
        chosen=candidate if vscore(candidate)<vscore(baseline) else baseline
        selection.append(dict(vehicle=veh,mode=mode,selected=chosen,validation_mae_C=vscore(chosen),best_baseline=baseline,baseline_validation_mae_C=vscore(baseline),
            netheat_validation_mae_C=vscore('netheat'),temperature_threshold_not_established=True))
        print(key,'selected',chosen,'val MAE',round(vscore(chosen),3),'baseline',baseline,round(vscore(baseline),3),flush=True)
    metric=pd.DataFrame(allmetrics);pred=pd.DataFrame(allpred);sel=pd.DataFrame(selection)
    metric.to_csv(OUT/'15min_session_metrics.csv',index=False);pred.to_csv(OUT/'15min_all_predictions.csv',index=False)
    sel.to_csv(OUT/'model_selection.csv',index=False)
    # Descriptive uncertainty intervals calibrated only on validation windows (overlap, not formal conformal claim).
    cover=[]
    for row in selection:
        g=pred[(pred.vehicle==row['vehicle'])&(pred['mode']==row['mode'])&(pred.model==row['selected'])]
        va=g[g.split=='validation'];te=g[g.split=='test']
        if len(va)==0 or len(te)==0:continue
        band=float(np.quantile(np.abs(va.error_C),0.9))
        cover.append(dict(vehicle=row['vehicle'],mode=row['mode'],model=row['selected'],nominal=0.9,validation_abs_error_q90_C=band,
           test_coverage_fraction=float(np.mean(np.abs(te.error_C)<=band)),test_windows=len(te),test_sessions=te.session.nunique(),
           test_mae_C=float(np.mean(np.abs(te.error_C))),test_rmse_C=float(np.sqrt(np.mean(te.error_C**2))),test_bias_C=float(np.mean(te.error_C))))
    pd.DataFrame(cover).to_csv(OUT/'15min_uncertainty_screen.csv',index=False)
    (OUT/'model_parameters.json').write_text(json.dumps(fits,indent=2))
    print('Summary:');print(pd.DataFrame(cover).to_string(index=False),flush=True)
    # Heldout graphical panel chosen model vs observations and persistence by session
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    for row in selection:
        veh,mode=row['vehicle'],row['mode'];chosen=row['selected']
        d=pred[(pred.vehicle==veh)&(pred['mode']==mode)&(pred.split=='test')&(pred.model==chosen)]
        if d.empty:continue
        top=d.groupby('session').size().sort_values(ascending=False).index[:1]
        ss=d[d.session==top[0]].sort_values('end_sec')
        per=pred[(pred.vehicle==veh)&(pred['mode']==mode)&(pred.split=='test')&(pred.model=='persistence')&(pred.session==top[0])].sort_values('end_sec')
        fig,ax=plt.subplots(figsize=(9,4));ax.plot(ss.end_sec/60,ss.observed_temp_C,label='Measured maximum BMS sensor temperature')
        ax.plot(ss.end_sec/60,ss.predicted_temp_C,label=f'{chosen} conditional 15-min hindcast')
        ax.plot(per.end_sec/60,per.predicted_temp_C,label='Persistence')
        ax.set(xlabel='Session elapsed time (min)',ylabel='Temperature (°C)',title=f'{veh} {mode} — unseen session {top[0]}')
        ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(OUT/f'{veh}_{mode}_heldout_15min.png',dpi=145);plt.close(fig)
    (OUT/'audit_summary.json').write_text(json.dumps(dict(raw_archive_sha256=hashlib.sha256(SRC.read_bytes()).hexdigest(),
       sessions=len(audits),AC_sessions=sum(x['mode']=='AC' for x in audits),DC_sessions=sum(x['mode']=='DC' for x in audits),eligible_episodes=len(eps),windows=sum(len(x[1]) for x in cases.values()),
       caveat='15min conditional hindcast uses FUTURE observed current and ambient; predictions are not operational real-time forecasts; validation windows overlap.'),indent=2))
if __name__=='__main__':main()
