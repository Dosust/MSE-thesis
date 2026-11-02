#!/usr/bin/env python3
"""Chronological 24-hour *conditional hindcasts*: future observed I,V,Tambient provided.
Original SINTEF measurements hash verified in imported read_sensor. No inter-site extrapolation.
Uncertainty: first half of holdout calibrates descriptive absolute-error band;
last half evaluates coverage. Overlapping windows invalidate formal iid coverage.
"""
import json,argparse
from pathlib import Path
import numpy as np
import pandas as pd
from transformer_calibration import read_sensor,blocks,simulate_oil,simulate_hot

def calc(src,fitpath,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 js=json.loads(Path(fitpath).read_text());params=js['estimated_effective_parameters'];s= params['top_oil']
 oilparams=[s['Delta_no_load_C'],s['Delta_current_C'],s['tau_o_h']]
 Iref=js['I_reference_A_observed_median_not_nameplate'];Vref=js['V_reference_kV_observed_median_not_nameplate']
 df,_=read_sensor(src)
 split=df.index[int(len(df)*.7)];rows=[]
 for partition,frame in [('train',df.loc[df.index<split]),('holdout',df.loc[df.index>=split])]:
  for ep,g in enumerate(blocks(frame)):
   if len(g)<25:continue
   for start in range(0,len(g)-24):
    sub=g.iloc[start:start+25]
    if abs((sub.index[-1]-sub.index[0]).total_seconds()/3600-24)>1e-7:continue
    po=simulate_oil(sub,oilparams,Iref,Vref)
    preds={'Top oil [degC]':po}
    for c in ['Hot-spot HV [degC]','Hot-spot LV [degC]']:
     h=params[c];preds[c]=simulate_hot(sub,po,[h['Delta_hot_C'],h['tau_hot_h']],Iref,c)
    for col,forecast in preds.items():
     obs=float(sub[col].iloc[-1]);model=float(forecast[-1]);initial=float(sub[col].iloc[0]);
     rows.append({'split':partition,'state':col,'episode':ep,'start':str(sub.index[0]),'end':str(sub.index[-1]),
      'true_C':obs,'model_C':model,'persistence_C':initial,'error_C':model-obs,'baseline_error_C':initial-obs})
 prediction=pd.DataFrame(rows);prediction.to_csv(out/'conditional_24h_predictions.csv',index=False)
 summary=[]
 for (split,state),g in prediction.groupby(['split','state']):
  summary.append({'split':split,'state':state,'windows':len(g),'model_rmse_C':float(np.sqrt(np.mean(g.error_C**2))),
    'persistence_rmse_C':float(np.sqrt(np.mean(g.baseline_error_C**2))),
    'model_mae_C':float(np.mean(np.abs(g.error_C))),'model_bias_C':float(g.error_C.mean())})
 pd.DataFrame(summary).to_csv(out/'conditional_24h_summary.csv',index=False)
 uncertainty=[]
 for state,g in prediction[prediction.split=='holdout'].groupby('state'):
  times=pd.to_datetime(g.end,utc=True);cut=times.quantile(.5)
  cal=g.loc[times<=cut];test=g.loc[times>cut]
  if len(cal)<30 or len(test)<30:continue
  half=float(np.quantile(np.abs(cal.error_C),.9))
  uncertainty.append({'state':state,'nominal_coverage':.9,'calibration_windows':len(cal),'evaluation_windows':len(test),
   'halfwidth_C':half,'evaluation_coverage':float(np.mean(np.abs(test.error_C)<=half)),
   'limitation':'Overlapping 24h windows; descriptive only, not independent conformal coverage'})
 pd.DataFrame(uncertainty).to_csv(out/'conditional_24h_uncertainty.csv',index=False)
 import matplotlib;matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 g=prediction[(prediction.split=='holdout')&(prediction.state=='Top oil [degC]')].sort_values('end').iloc[::24]
 fig,ax=plt.subplots(figsize=(10,4));ax.plot(pd.to_datetime(g.end),g.true_C,label='Measured top oil')
 ax.plot(pd.to_datetime(g.end),g.model_C,label='Candidate 24h conditional hindcast')
 ax.plot(pd.to_datetime(g.end),g.persistence_C,label='Persistence',alpha=.75)
 ax.set(xlabel='Holdout target time',ylabel='Top oil temperature (°C)');ax.legend();ax.grid(alpha=.2);fig.tight_layout();fig.savefig(out/'top_oil_24h.png',dpi=145);plt.close(fig)
 return pd.DataFrame(summary)

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--sensor',required=True);a.add_argument('--fit',required=True);a.add_argument('--out',required=True)
 args=a.parse_args();print(calc(args.sensor,args.fit,args.out).to_string(index=False))
