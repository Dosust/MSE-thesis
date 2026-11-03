#!/usr/bin/env python3
"""Reproduce the additional Report 1 RQ7 and RQ8-RQ10 results.
Inputs must be the SINTEF publisher-MD5-matched sensor CSV and the
user-uploaded OSF 94GKC nested ZIP. Component observations only:
no field-validated power-EVSE coupling and no extreme-heat validation.
Install numpy, pandas, scipy. Original inputs are not modified.
"""
import argparse, hashlib, io, json, re, zipfile
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import lsq_linear

SINTEF_MD5 = "5d81840a2f901f04fded98c3e1097b6e"

def met(actual,pred):
    e = np.asarray(pred) - np.asarray(actual)
    e = e[np.isfinite(e)]
    if not len(e): return {"n":0}
    return {"n":int(len(e)), "rmse_C":float(np.sqrt(np.mean(e*e))),
            "mae_C":float(np.mean(abs(e))), "bias_C":float(e.mean())}

def thermal(source,out):
    if hashlib.md5(Path(source).read_bytes()).hexdigest()!=SINTEF_MD5:
        raise ValueError("Original SINTEF publisher MD5 does not match")
    d=pd.read_csv(source,parse_dates=["Timestamp"])
    t=d["Timestamp"]
    T=d["Top oil [degC]"].to_numpy(float)
    A=d["Ambient [degC]"].to_numpy(float)
    I=d["Current [A]"].to_numpy(float)
    tomorrow=np.roll(T,-1)
    good=((t.shift(-1)-t)==pd.Timedelta(hours=1)).to_numpy()
    good &= np.isfinite(T)&np.isfinite(A)&np.isfinite(I)&np.isfinite(tomorrow)
    train=good&(t<pd.Timestamp("2024-07-01")).to_numpy()
    test=good&(t>=pd.Timestamp("2024-10-01")).to_numpy()
    ref=float(np.median(I[train]))
    X=np.column_stack((A-T,(I/ref)**2,np.ones(len(d))))
    y=tomorrow-T
    coef=lsq_linear(X[train],y[train],bounds=([0,0,0],[1,np.inf,np.inf])).x
    a,b,c=map(float,coef)
    x=X[train]
    scaled_cond=float(np.linalg.cond(x/np.linalg.norm(x,axis=0)))
    rank=int(np.linalg.matrix_rank(x))
    idx=np.where(train)[0];L=24
    starts=np.array([i for i in range(len(idx)-L+1) if idx[i+L-1]-idx[i]==L-1])
    rng=np.random.default_rng(20261103);boots=[]
    for _ in range(180):
        p=rng.choice(starts,int(np.ceil(len(idx)/L)),replace=True)
        sample=(p[:,None]+np.arange(L)).ravel()[:len(idx)]
        result=lsq_linear(x[sample],y[train][sample],bounds=([0,0,0],[1,np.inf,np.inf]))
        if result.success:boots.append(result.x)
    boots=np.asarray(boots)
    ci={name:np.quantile(boots[:,j],[.025,.5,.975]).tolist()
        for j,name in enumerate(("a","b","c"))}
    pd.DataFrame([{"parameter":k,"q025":v[0],"q50":v[1],"q975":v[2]}
                  for k,v in ci.items()]).to_csv(out/"REPORT_01_RQ8_BLOCK_BOOTSTRAP.csv",index=False)
    itest=float(np.median(I[test])); ip95=float(np.quantile(I[test],.95))
    def sim(ta,ii,coefnew=coef):
        aa,bb,cc=coefnew
        state=20.
        for _ in range(24): state+=aa*(ta-state)+bb*(ii/ref)**2+cc
        return float(state)
    base=sim(20.,itest)
    sens={"dTnext_dTa":a,"dTnext_dI_at_test_median":2*b*itest/ref**2,
          "dTnext_dI_at_test_p95":2*b*ip95/ref**2,
          "dTnext_dT":1-a,"test_median_I_A":itest,
          "test_p95_I_A":ip95,
          "plus_10pct_current_next_hour_C":b*((1.1*itest/ref)**2-(itest/ref)**2),
          "conditional_24h_reference_T_C":base,
          "conditional_24h_T_change_plus_1C_ambient":sim(21.,itest)-base,
          "conditional_24h_T_change_plus_10pct_current":sim(20.,1.1*itest)-base,
          "conditional_24h_T_change_plus_10pct_a":sim(20.,itest,[a*1.1,b,c])-base,
          "conditional_24h_T_change_plus_10pct_b":sim(20.,itest,[a,b*1.1,c])-base,
          "conditional_24h_T_change_plus_10pct_c":sim(20.,itest,[a,b,c*1.1])-base}
    pred=T+X@coef
    ranges={}
    for key,arr in (("ambient_C",A),("current_A",I),("oil_C",T)):
        ranges[key]={"train":[float(arr[train].min()),float(arr[train].max())],
                     "test":[float(arr[test].min()),float(arr[test].max())]}
    inside=np.ones(int(test.sum()),dtype=bool)
    for key,arr in (("ambient_C",A),("current_A",I),("oil_C",T)):
        lo,hi=ranges[key]["train"]
        inside &= (arr[test]>=lo)&(arr[test]<=hi)
    months=[]
    testmonth=t[test].dt.month.to_numpy()
    for m in (10,11,12):
        use=(testmonth==m)
        months.append({"month":m,"model":met(tomorrow[test][use],pred[test][use]),
                       "persistence":met(tomorrow[test][use],T[test][use])})
    pd.DataFrame([{"month":v["month"],"model_rmse_C":v["model"]["rmse_C"],
                   "persistence_rmse_C":v["persistence"]["rmse_C"]}
                  for v in months]).to_csv(out/"REPORT_01_RQ10_MONTHLY_HOLDOUT.csv",index=False)
    return {
        "RQ8":{"fit":{"a":a,"b":b,"c":c,"Iref_A":ref},"n_train":int(train.sum()),
               "design_rank":rank,"normalized_condition_number":scaled_cond,
               "block_bootstrap":{"n":len(boots),"block_hours":24,"percentiles":ci},
               "nominal_tau_discrete_h":float(-1/np.log(1-a)),
               "physical_parameter_identifiability":"NOT established for distinct heat capacities, losses and cooling"},
        "RQ9":{"analytic_and_24h_model_only_sensitivities":sens,
               "assumptions":"24h fixed Ta=20C, initial top oil 20C; current=test median; source model, NOT observed experiment"},
        "RQ10":{"n_test":int(test.sum()),"training_test_marginal_ranges":ranges,
                "fraction_within_all_three_training_marginal_ranges":float(inside.mean()),
                "by_month":months,
                "test_one_step":{"model":met(tomorrow[test],pred[test]),
                                 "persistence":met(tomorrow[test],T[test])},
                "external_transfer_validated":False,"extreme_heat_validated":False}
    }

def osf(source,out):
    with zipfile.ZipFile(source) as outer:
        inside_name=next(x for x in outer.namelist()
                         if x.lower().startswith("high-resolution dataset"))
        nested=outer.read(inside_name)
    rows=[]
    with zipfile.ZipFile(io.BytesIO(nested)) as z:
        names=[x for x in z.namelist() if x.lower().endswith(".csv")]
        if len(names)!=313:raise ValueError("Unexpected OSF CSV count")
        for name in names:
            base=name.split("/")[-1];category=name.split("/")[0]
            duration=re.search(r"duration_?([0-9]+(?:\.[0-9]+)?)s",base,re.I)
            start=re.search(r"_Start_([0-9]+(?:\.[0-9]+)?)",base,re.I)
            dur=float(duration.group(1)) if duration else float("nan")
            t0=float(start.group(1)) if start else 20.
            data=pd.read_csv(z.open(name),encoding="latin1",
                             usecols=lambda col:col in ("Time [s]","HV_Battery_Current [A]",
                                                       "HV_Battery_Voltage [V]","HV_Battery_Temperature"),
                             low_memory=False)
            data.columns=[str(c).strip().removeprefix("ï»¿")
                          for c in data.columns]
            def numeric(key):
                if key not in data:return np.full(len(data),np.nan)
                return pd.to_numeric(data[key],errors="coerce").to_numpy(float)
            t=numeric("Time [s]");current=numeric("HV_Battery_Current [A]")
            temp=numeric("HV_Battery_Temperature")
            pre=(t>=t0-10)&(t<t0-2)&np.isfinite(current)
            event=(t>=t0)&(t<t0+dur)&np.isfinite(current)
            accept=(np.isfinite(dur) and dur>=.5 and pre.sum()>=30 and event.sum()>=10)
            before=float(np.median(np.abs(current[pre]))) if pre.any() else float("nan")
            during=float(np.median(np.abs(current[event]))) if event.any() else float("nan")
            rows.append({"file":name,"category":category,"n_rows":len(data),
                         "n_current":int(np.isfinite(current).sum()),
                         "n_temperature":int(np.isfinite(temp).sum()),
                         "duration_s":dur,"n_pre":int(pre.sum()),"n_event":int(event.sum()),
                         "pre_median_abs_I_A":before,
                         "event_median_abs_I_A":during,
                         "eligible":bool(accept),
                         "eligible_nonzero_baseline":bool(accept and before>=1.0),
                         "event_minus_pre_abs_current_A":during-before if accept else np.nan})
    tab=pd.DataFrame(rows)
    tab.to_csv(out/"REPORT_01_RQ7_OSF_BY_EXPERIMENT.csv",index=False)
    groups=[]
    for cat,g in tab.groupby("category",sort=True):
        ok=g[g.eligible_nonzero_baseline]
        v=ok.event_minus_pre_abs_current_A.to_numpy()
        groups.append({"category":cat,"files":len(g),"eligible":len(ok),
                       "median_event_minus_pre_abs_current_A":
                           float(np.median(v)) if len(v) else None})
    pd.DataFrame(groups).to_csv(out/"REPORT_01_RQ7_OSF_BY_CATEGORY.csv",index=False)
    return {"n_csv":len(tab),"n_nonempty_csv":int((tab.n_rows>0).sum()),
            "n_empty_csv":int((tab.n_rows==0).sum()),"n_main_csv":250,
            "n_sag_extended_csv":63,"parsed_rows":int(tab.n_rows.sum()),
            "valid_battery_current_values":int(tab.n_current.sum()),
            "nonempty_battery_temperature_values":int(tab.n_temperature.sum()),
            "n_eligible_event_comparisons":int(tab.eligible.sum()),
            "n_eligible_and_baseline_at_least_1A":int(tab.eligible_nonzero_baseline.sum()),
            "source_zip_sha256":hashlib.sha256(Path(source).read_bytes()).hexdigest(),
            "unresolved_previous_audit_row_count":4061379,
            "groups":groups,
            "caveat":"Within-test descriptive battery current contrasts, NOT proven grid-side voltage/cause, thermal derating, or linked transformer field effects."}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--sintef",required=True)
    p.add_argument("--osf",required=True)
    p.add_argument("--out",default="report1_extended_results")
    args=p.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    result={"source_evidence":"Independent original component datasets; no P-EVSE field topology",
            "RQ7":osf(args.osf,out),
            "RQ8_RQ9_RQ10":thermal(args.sintef,out),
            "RQ6":"NOT computed; original OPSD household series absent",
            "RQ11":"Conditional mathematics only; missing connected thermal service data"}
    with open(out/"REPORT_01_EXTENSION_RQ7_RQ11_RESULTS.json","w",encoding="utf8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2,allow_nan=False)
    print(json.dumps({"RQ7":result["RQ7"]["groups"],
                      "RQ8":result["RQ8_RQ9_RQ10"]["RQ8"],
                      "RQ9":result["RQ8_RQ9_RQ10"]["RQ9"],
                      "RQ10":result["RQ8_RQ9_RQ10"]["RQ10"]["by_month"]},indent=2))
if __name__=="__main__":
    main()
