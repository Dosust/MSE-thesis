#!/usr/bin/env python3
"""Reproduce Report 1 RQ8-RQ10 SINTEF component-only results.
Usage: python REPORT_01_EXTENDED_TRANSFORMER_REPRODUCE.py --source Barug2025_sensordata.csv
Requires: pandas numpy scipy. Does not edit source files. No cross-site inference.
"""
from __future__ import annotations
import argparse, hashlib, json, math
import numpy as np
import pandas as pd
from scipy.optimize import lsq_linear

PUBLISHER_MD5 = "5d81840a2f901f04fded98c3e1097b6e"

def metric(y, yhat):
    e = np.asarray(y)-np.asarray(yhat)
    return {"n": int(len(e)), "RMSE_C": round(float(np.sqrt(np.mean(e*e))),6),
            "MAE_C":round(float(np.mean(np.abs(e))),6)}

def fit(X,y,mask,cols):
    xx=X[mask][:,cols]
    lo=np.zeros(len(cols));hi=np.full(len(cols),np.inf)
    if 0 in cols:hi[cols.index(0)]=1
    z=lsq_linear(xx,y[mask],bounds=(lo,hi),max_iter=2000,tol=1e-11)
    ans=np.zeros(3);ans[cols]=z.x
    return ans

def hindcast(T,Ta,I,t,p,Iref,h,starts):
    y=[];yh=[];yp=[]
    for i in starts:
        if i+h>=len(T) or t[i+h]-t[i]!=pd.Timedelta(hours=h):continue
        temp=T[i];aa,bb,cc=p
        for j in range(h):
            temp+=aa*(Ta[i+j]-temp)+bb*(I[i+j]/Iref)**2+cc
        y.append(T[i+h]);yh.append(temp);yp.append(T[i])
    return np.asarray(y),np.asarray(yh),np.asarray(yp)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True)
    ap.add_argument("--output",default="REPORT_01_TRANSFORMER_RQ8_RQ10.json")
    args=ap.parse_args()
    raw=open(args.source,"rb").read()
    if hashlib.md5(raw).hexdigest()!=PUBLISHER_MD5:
        raise RuntimeError("Source-original MD5 mismatch")
    d=pd.read_csv(args.source,parse_dates=["Timestamp"]).sort_values("Timestamp").reset_index(drop=True)
    t=d["Timestamp"]
    T=d["Top oil [degC]"].to_numpy(float)
    Ta=d["Ambient [degC]"].to_numpy(float)
    I=d["Current [A]"].to_numpy(float)
    contiguous=(t.shift(-1)-t==pd.Timedelta(hours=1)).to_numpy()
    train=contiguous&(t<pd.Timestamp("2024-07-01")).to_numpy()
    test=contiguous&(t>=pd.Timestamp("2024-10-01")).to_numpy()
    Iref=float(np.median(I[train]))
    X=np.column_stack([Ta-T,(I/Iref)**2,np.ones(len(T))])
    delta=np.roll(T,-1)-T
    p=fit(X,delta,train,[0,1,2])
    pa=fit(X,delta,train,[0,2])
    pi=fit(X,delta,train,[1,2])
    obs=np.roll(T,-1)[test]
    results={"source_MD5":PUBLISHER_MD5,"I_ref_A":Iref,
             "model":"T[k+1]=T[k]+a(Ta[k]-T[k])+b(I[k]/Iref)^2+c",
             "training_1h_transitions":int(train.sum()),
             "heldout_1h_transitions":int(test.sum()),
             "abc_all":p.tolist(),
             "one_hour_test":{
               "persistence":metric(obs,T[test]),
               "ambient_plus_constant":metric(obs,T[test]+X[test]@pa),
               "current_plus_constant":metric(obs,T[test]+X[test]@pi),
               "full_model":metric(obs,T[test]+X[test]@p)
             }}
    ss={}
    for name,months in [("Jan_Mar",[1,2,3]),("Apr_Jun",[4,5,6])]:
        m=train&t.dt.month.isin(months).to_numpy()
        ss[name]={"n":int(m.sum()),"abc":fit(X,delta,m,[0,1,2]).tolist()}
    results["RQ8_sensitivity_of_fitted_coefficients_to_training_season"]=ss
    xt=X[train].copy()
    xs=np.column_stack([(xt[:,0]-xt[:,0].mean())/xt[:,0].std(),
                        (xt[:,1]-xt[:,1].mean())/xt[:,1].std(),np.ones(len(xt))])
    s=np.linalg.svd(xs,compute_uv=False)
    results["RQ8_design_scaled_condition_number"]=float(s[0]/s[-1])
    results["RQ8_feature_correlation"]=float(np.corrcoef(xt[:,0],xt[:,1])[0,1])
    horizons={}
    starts=np.where((t>=pd.Timestamp("2024-10-01")).to_numpy())[0]
    for h in (1,6,24):
        y,yhat,persist=hindcast(T,Ta,I,t,p,Iref,h,starts)
        horizons[str(h)+"h"]={"model":metric(y,yhat),
                                 "persistence":metric(y,persist)}
    results["RQ10_chronological_conditional_hindcasts"]=horizons
    bins={}
    for name,lo,hi in [("ambient_le_0",-np.inf,0),
                       ("ambient_0_to_10",0,10),
                       ("ambient_10_to_20",10,20),
                       ("ambient_gt_20",20,np.inf)]:
        m=(Ta[test]>lo)&(Ta[test]<=hi)
        if m.any():
            bins[name]={"model":metric(obs[m],(T[test]+X[test]@p)[m]),
                         "persistence":metric(obs[m],T[test][m]),
                         "ambient_min_C":float(Ta[test][m].min()),
                         "ambient_max_C":float(Ta[test][m].max())}
        else:bins[name]={"n":0}
    results["RQ10_holdout_by_ambient_bin"]=bins
    results["observed_ranges"]={
      "ambient_C":[float(Ta.min()),float(Ta.max())],
      "current_A":[float(I.min()),float(I.max())],
      "top_oil_C":[float(T.min()),float(T.max())]}
    # Same Oct1-Dec30 start set for every perturbation to preserve matched comparisons.
    special_starts=np.where(((t>=pd.Timestamp("2024-10-01"))&
                             (t<=pd.Timestamp("2024-12-30"))).to_numpy())[0]
    _,nom,_=hindcast(T,Ta,I,t,p,Iref,24,special_starts)
    pert={}
    for k,name in enumerate(["a","b","c"]):
        for factor in (0.9,1.1):
            pp=p.copy();pp[k]*=factor
            _,prediction,_=hindcast(T,Ta,I,t,pp,Iref,24,special_starts)
            pert[f"{name}_x{factor}"]={
              "median_abs_delta_C":float(np.median(np.abs(prediction-nom)))}
    for offset in (-5,5):
        _,prediction,_=hindcast(T,Ta+offset,I,t,p,Iref,24,special_starts)
        pert[f"ambient_{offset:+}C"]={"median_delta_C":float(np.median(prediction-nom))}
    for factor in (0.9,1.1):
        _,prediction,_=hindcast(T,Ta,I*factor,t,p,Iref,24,special_starts)
        pert[f"current_x{factor}"]={"median_delta_C":float(np.median(prediction-nom))}
    pert["initial_top_oil_plus_2C_24h_effect_C"]=float(2*(1-p[0])**24)
    results["RQ9_deterministic_24h_sensitivity"]={"n_starts":len(nom),
       "one_at_a_time_perturbations":pert,
       "WARNING":"Not predictive UQ and not observed extreme-heat conditions"}
    results["scope_warning"]="No thermal field coupling or independent cross-site transfer is tested."
    with open(args.output,"w") as f:json.dump(results,f,indent=2)
    print(json.dumps(results,indent=2))

if __name__=="__main__":main()
