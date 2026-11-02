#!/usr/bin/env python3
"""SINTEF measured-transformer *candidate* thermal calibration on chronological holdout.
Scientific status: preliminary grey-box model-screening, NOT IEC 60076-7 implementation,
NOT a validated extreme-heat model, NOT a coupled-system calibration.
Usage: python transformer_calibration.py --sensor Barug2025_sensordata.csv --out output_dir
Requires original Zenodo measured CSV, not computed/calculated CSV.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
EXPECTED_MD5='5d81840a2f901f04fded98c3e1097b6e'
COLS=['Timestamp','Voltage [kV]','Current [A]','Ambient [degC]','Top oil [degC]',
      'Hot-spot HV [degC]','Hot-spot LV [degC]']

def checksum(path):
    h=hashlib.md5()
    with open(path,'rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()

def read_sensor(path):
    md5=checksum(path)
    if md5!=EXPECTED_MD5:
        raise ValueError('CSV checksum does not match SINTEF published sensor file. Never calibrate on unverified/reprocessed data without a separate provenance record.')
    df=pd.read_csv(path,low_memory=False)
    absent=[x for x in COLS if x not in df.columns]
    if absent: raise ValueError(f'Missing required headers {absent}')
    df['Timestamp']=pd.to_datetime(df['Timestamp'],errors='coerce',utc=True)
    for c in COLS[1:]:df[c]=pd.to_numeric(df[c],errors='coerce')
    df=df.dropna(subset=COLS).sort_values('Timestamp')
    if df['Timestamp'].duplicated().any(): raise ValueError('Duplicate timestamp(s), inspect rather than overwrite.')
    if len(df)<250:raise ValueError('Insufficient measured records')
    df=df.set_index('Timestamp')
    # All unfilled gaps retained as gaps; no interpolation or artificial timestamps.
    return df,md5

def blocks(df):
    delta=df.index.to_series().diff().dt.total_seconds().div(3600).fillna(1)
    # new episode if gap > 1.5h or nonpositive.
    episode=((delta>1.5)|(delta<=0)).cumsum()
    return [g for _,g in df.groupby(episode) if len(g)>=4]

def exp_step(T, target,tau,dt):
    return target+(T-target)*np.exp(-dt/tau)

def simulate_oil(g,params,Iref,Vref):
    d0,di,tau=params
    obs=g['Top oil [degC]'].to_numpy()
    I=g['Current [A]'].to_numpy();V=g['Voltage [kV]'].to_numpy();Ta=g['Ambient [degC]'].to_numpy()
    t=g.index.view('int64')/3.6e12
    out=np.empty(len(g));out[0]=obs[0]
    for j in range(len(g)-1):
        Teq=Ta[j]+d0*(V[j]/Vref)**2+di*(I[j]/Iref)**2
        out[j+1]=exp_step(out[j],Teq,tau,t[j+1]-t[j])
    return out

def simulate_hot(g,oil_prediction,p,Iref,col):
    dh,tau=p
    obs=g[col].to_numpy()
    I=g['Current [A]'].to_numpy();t=g.index.view('int64')/3.6e12
    out=np.empty(len(g));out[0]=obs[0]
    for j in range(len(g)-1):
        # uses oil *prediction*, not contemporaneous measured oil when forecasting
        Teq=oil_prediction[j]+dh*(I[j]/Iref)**2
        out[j+1]=exp_step(out[j],Teq,tau,t[j+1]-t[j])
    return out

def metrics(obs,pred):
    err=np.array(pred)-np.array(obs)
    return {'n':len(obs),'rmse_C':float(np.sqrt(np.mean(err**2))),
            'mae_C':float(np.mean(np.abs(err))),
            'bias_C':float(np.mean(err)),
            'constant_initial_baseline_rmse_C':float(np.sqrt(np.mean((obs-obs[0])**2)))}

def run(sensor,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    data,md5=read_sensor(sensor)
    chronological_split=data.index[int(len(data)*.7)]
    train=data.loc[data.index<chronological_split];test=data.loc[data.index>=chronological_split]
    # Reference values are observed normalizers, NOT rated nameplate values.
    Iref=float(train['Current [A]'].abs().median());Vref=float(train['Voltage [kV]'].abs().median())
    if Iref<=0 or Vref<=0:raise ValueError('Invalid measured reference scaling')
    tr=blocks(train);te=blocks(test)
    if not tr or not te:raise ValueError('Insufficient contiguous measured train/test blocks')
    def oil_resid(p):
        return np.hstack([(simulate_oil(g,p,Iref,Vref)-g['Top oil [degC]'].to_numpy())/np.sqrt(len(g)) for g in tr])
    fit_o=least_squares(oil_resid,[5,10,8],bounds=([0,0,0.5],[80,200,200]),loss='soft_l1',max_nfev=250)
    if not fit_o.success: raise ValueError('Oil parameter optimization did not converge')
    estimates={'top_oil':{'Delta_no_load_C':float(fit_o.x[0]),'Delta_current_C':float(fit_o.x[1]),'tau_o_h':float(fit_o.x[2])}}
    models={'Top oil [degC]':lambda g:simulate_oil(g,fit_o.x,Iref,Vref)}
    for col in ['Hot-spot HV [degC]','Hot-spot LV [degC]']:
        def resid(p):return np.hstack([(simulate_hot(g,simulate_oil(g,fit_o.x,Iref,Vref),p,Iref,col)-g[col].to_numpy())/np.sqrt(len(g)) for g in tr])
        fit=least_squares(resid,[10,1],bounds=([0,0.1],[200,48]),loss='soft_l1',max_nfev=150)
        if not fit.success:raise ValueError(f'Hot spot optimization failed: {col}')
        estimates[col]={'Delta_hot_C':float(fit.x[0]),'tau_hot_h':float(fit.x[1])}
        models[col]=lambda g,p=fit.x,c=col:simulate_hot(g,simulate_oil(g,fit_o.x,Iref,Vref),p,Iref,c)
    rows=[]
    for split,groups in [('train',tr),('holdout',te)]:
        for k,g in enumerate(groups):
            for col,func in models.items():
                result=metrics(g[col].to_numpy(),func(g))
                rows.append({'split':split,'episode':k,'state':col,'start':str(g.index[0]),'end':str(g.index[-1]),**result})
    pd.DataFrame(rows).to_csv(out/'transformer_calibration_episodes.csv',index=False)
    report={'status':'PRELIMINARY measured-data grey-box candidate; NO equipment/IEC/heat-coupled model admission',
     'input':str(Path(sensor).name),'md5':md5,'measurement_rows_after_complete_case':int(len(data)),
     'train_rows':int(len(train)),'holdout_rows':int(len(test)),
     'chronological_holdout_start':str(chronological_split),'train_contiguous_episodes':len(tr),'holdout_contiguous_episodes':len(te),
     'I_reference_A_observed_median_not_nameplate':Iref,'V_reference_kV_observed_median_not_nameplate':Vref,
     'estimated_effective_parameters':estimates,
     'limitations':['Semi-empirical grey-box, not verified implementation of an industry standard',
     'Model uses measured initial state at each observed episode only',
     'No interpolation across data gaps; complete-case rows can form new gaps',
     'Hot-spot time constants below hourly sampling resolution may be poorly identifiable',
     'Only Norwegian installation; cannot extrapolate to unobserved extreme heat or different rating',
     'Transformer nameplate losses, cooling stages, loading topology, power factor not supplied',
     'Full multi-parameter uncertainty/identifiability and external equipment tests still required']}
    (out/'transformer_candidate_fit.json').write_text(json.dumps(report,indent=2))
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--sensor',required=True)
    parser.add_argument('--out',default='transformer_results')
    args=parser.parse_args();print(json.dumps(run(args.sensor,args.out),indent=2))
