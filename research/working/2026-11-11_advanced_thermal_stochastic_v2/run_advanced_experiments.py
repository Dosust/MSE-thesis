#!/usr/bin/env python3
"""Physics-first ASU thesis extension, 11 Nov 2026.
Original inputs are user-owned Drive backed files, no external measured data.
Exploratory independent component results only. A cross-site thermal EV coupling is BLOCKED.
EPFL sessions parsed by artifact_tool (prior source-qualification code reused).
"""
from pathlib import Path
import csv, json, hashlib, math, zipfile, io, sys
from collections import Counter, defaultdict
from datetime import datetime
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path('/mnt/data')
D=ROOT/'thermal_extension_20261111_v2';D.mkdir(exist_ok=True)
SIN=ROOT/'SINTEF_Barug2025_sensordata_original_MD5verified_2026-11-03.csv'
EP_S=ROOT/'Session_data.xlsx'; EP_M=ROOT/'Measurement_data.xlsx'
KU=ROOT/'KU_Leuven_C5PT0R_Measured_EV_Charging_Efficiency_UserOriginal_2026-11-03.zip'
SP=ROOT/'STREAM_Slovenia_control_measurements_P_2025_original_MD5verified.csv'
SQ=ROOT/'STREAM_Slovenia_control_measurements_Q_2025_original_MD5verified.csv'
FILES=[SIN,EP_S,EP_M,KU,SP,SQ]

def sourcehash(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()

def read_sintef():
 with SIN.open(newline='') as f:r=list(csv.DictReader(f))
 t=np.array([datetime.fromisoformat(x['Timestamp']) for x in r],dtype='datetime64[s]')
 cols={k:np.array([float(x[k]) if x[k] not in ('','NaN','nan') else float('nan') for x in r]) for k in r[0] if k!='Timestamp'}
 return t,cols

def thermal_fit(t,arr):
 n=len(t); good=np.where((t[1:]-t[:-1]).astype('timedelta64[s]').astype(int)==3600)[0]
 cutoff=int(.7*n)
 tr=good[good+1<cutoff]
 te=good[good>=cutoff]
 I=arr['Current [A]']; Ta=arr['Ambient [degC]']; Y=arr['Top oil [degC]']
 ref=float(np.median(I[:cutoff]));q=(I/ref)**2
 def pred(par,ii):
  tau,d,g=par; a=np.exp(-1/tau)
  return a*Y[ii]+(1-a)*(Ta[ii]+d+g*q[ii])
 def obj(par,ii):return pred(par,ii)-Y[ii+1]
 fit=least_squares(lambda p:obj(p,tr),[11,13.5,.75],bounds=([.25,-40,0],[200,90,100]),max_nfev=500,ftol=1e-12,xtol=1e-12,gtol=1e-12)
 params=fit.x
 def metric(ii):
  z=pred(params,ii);base=Y[ii];y=Y[ii+1]
  return {'pairs':len(ii),'model_rmse_C':float(np.sqrt(np.mean((z-y)**2))),'model_mae_C':float(np.mean(abs(z-y))),'model_bias_C':float(np.mean(z-y)),
          'persistence_rmse_C':float(np.sqrt(np.mean((base-y)**2))),'persistence_mae_C':float(np.mean(abs(base-y)))}
 report={'row_count':n,'observed_ambient_max_C':float(Ta.max()),'hot_spot_audit':{},'observed_ambient_at_least_30C':int((Ta>=30).sum()),
         'training_pairs':int(len(tr)),'holdout_pairs':int(len(te)), 'Iref_training_median_A':ref, 'params_effective':{'tau_h':float(params[0]),'ambient_offset_C':float(params[1]),'Iref_current_sq_gain_C':float(params[2])},
         'training_metrics':metric(tr),'holdout_metrics':metric(te)}
 # log tau, d, g derivatives, then standardized: tests local linear sensitivities only.
 z=pred(params,tr); X=[]
 for k in range(3):
  step=1e-4*max(1,abs(params[k])); p1=params.copy();p2=params.copy();p1[k]+=step;p2[k]-=step
  derivative=(pred(p1,tr)-pred(p2,tr))/(2*step)
  if k==0:derivative*=params[0] # log-tau coordinate
  X.append(derivative)
 jac=np.column_stack(X); norms=np.linalg.norm(jac,axis=0); Jstd=jac/norms
 sval=np.linalg.svd(Jstd,compute_uv=False)
 report['local_sensitivity']={'coordinates':['log_tau','offset_C','gain_C'],'raw_col_l2_norm':[float(v) for v in norms], 'unit_column_singular_values':sval.tolist(),
  'standardized_condition_number':float(sval[0]/sval[-1]),'linearized_parameter_column_correlation':np.corrcoef(jac.T).tolist(),
  'interpretation':'Local one-step sensitivity only; no structural-identifiability proof or calibrated parameter CI.'}
 # tau profile, optimize d and g exactly linearly. Some parameter opt constraints may matter at extremes.
 grid=np.linspace(3,30,70); sse=[]
 for tau in grid:
  a=np.exp(-1/tau)
  rhs=Y[tr+1]-a*Y[tr]-(1-a)*Ta[tr]
  basis=np.column_stack([np.full(len(tr),1-a),(1-a)*q[tr]])
  beta=np.linalg.lstsq(basis,rhs,rcond=None)[0]
  sse.append(float(np.sum((basis@beta-rhs)**2)))
 sse=np.array(sse)
 report['tau_profile']={'tau_grid_h':grid.tolist(),'relative_sse_to_fitted_minimum':(sse/(np.sum(obj(params,tr)**2))).tolist(),
   'profile_type':'unconstrained linear least squares in offset/gain for fixed effective tau; not likelihood CI'}
 # Calendar windows: contiguous training pair subsets; effective parameters may vary with weather/excitation.
 cal=[]
 for lab,lo,hi in [('Jan-Apr',np.datetime64('2024-01-01'),np.datetime64('2024-05-01')),
                   ('May-Aug',np.datetime64('2024-05-01'),np.datetime64('2024-09-01')),
                   ('Sep-Dec',np.datetime64('2024-09-01'),np.datetime64('2025-01-01'))]:
  ii=good[(t[good]>=lo)&(t[good+1]<hi)]
  f=least_squares(lambda p:obj(p,ii),params,bounds=([.25,-40,0],[200,90,100]),max_nfev=350)
  cal.append({'period':lab,'pairs':len(ii),'tau_h':float(f.x[0]),'offset_C':float(f.x[1]),'gain_C':float(f.x[2]),'ambient_range_C':[float(Ta[ii].min()),float(Ta[ii].max())]})
 report['seasonal_refits']=cal
 # Chronological split for model fit: training first 60%, calibration next 20%, evaluation last 20%.
 nfit=int(.6*n); ncal=int(.8*n)
 aa=good[good+1<nfit]; cc=good[(good>=nfit)&(good+1<ncal)];ee=good[good>=ncal]
 fit2=least_squares(lambda p:obj(p,aa),params,bounds=([.25,-40,0],[200,90,100]),max_nfev=300)
 rcal=abs(obj(fit2.x,cc)); q90=float(np.quantile(rcal,np.ceil((len(rcal)+1)*.9)/len(rcal),method='higher')) if len(rcal)>10 else None
 re=abs(obj(fit2.x,ee))
 report['chronological_residual_band']={'first_60pct_train_pairs':len(aa),'next_20pct_cal_pairs':len(cc),'last_20pct_eval_pairs':len(ee),'calibrated_abs_residual_cut_C':q90,
   'test_marginal_coverage':float(np.mean(re<=q90)),'test_mean_band_width_C':2*q90,'limitation':'Constant-width empirical residual band; chronology violates usual exchangeability assumptions; not guaranteed physical predictive coverage.'}
 # Hot-spot vs top-oil diagnostic; no applied life-consumption metric until sensor qualified.
 To=arr['Top oil [degC]']
 for key in ['Hot-spot HV [degC]','Hot-spot LV [degC]']:
  v=arr[key];mask=np.isfinite(v)&np.isfinite(To); vv=v[mask]
  thr=np.quantile(vv,.95)
  report['hot_spot_audit'][key]={'count':int(mask.sum()),'fraction_below_top_oil':float(np.mean(vv<To[mask])),
    'temperature_range_C':[float(vv.min()),float(vv.max())],'p95_empirical_threshold_C':float(thr),
    'fraction_above_own_empirical_p95':float(np.mean(vv>thr)),
    'mean_excess_C_hours_per_record':float(np.mean(np.maximum(vv-thr,0))),
    'safety_threshold_status':'None. p95 is a sample quantile, NOT equipment limit.',
    'aging_life_status':'BLOCKED_SENSOR_SEMANTICS_AND_EQUIPMENT_APPLICABILITY'}
 # Permute measured current order (same sum I²) in unbroken holdout 24h windows, same ambient and start T.
 # This is a *within-transformer* counterfactual, NOT EV charging or forecast.
 def rollout(st, seq):
  z=float(Y[st]);trajectory=[z];a=np.exp(-1/params[0])
  for k,qq in enumerate(seq):
   z=a*z+(1-a)*(Ta[st+k]+params[1]+params[2]*qq)
   trajectory.append(z)
  return np.array(trajectory)
 cases=[]
 for st in range(cutoff,n-24,24):
  if (t[st+24]-t[st]).astype('timedelta64[s]').astype(int)!=24*3600:continue
  v=q[st:st+24]
  o=rollout(st,v);front=rollout(st,np.sort(v)[::-1]);back=rollout(st,np.sort(v))
  cases.append({'start':str(t[st]), 'observed_order_final_C':float(o[-1]),'frontloaded_final_C':float(front[-1]),'backloaded_final_C':float(back[-1]),
                'observed_order_max_C':float(o.max()),'frontloaded_max_C':float(front.max()),'backloaded_max_C':float(back.max()),
                'current_square_sum_invariant':True})
 report['same_site_load_order_stress_test']={'cases':len(cases),'median_abs_final_difference_front_vs_back_C':float(np.median([abs(x['frontloaded_final_C']-x['backloaded_final_C']) for x in cases])),
   'median_abs_peak_difference_front_vs_back_C':float(np.median([abs(x['frontloaded_max_C']-x['backloaded_max_C']) for x in cases])),
   'max_abs_final_difference_C':float(np.max([abs(x['frontloaded_final_C']-x['backloaded_final_C']) for x in cases])),
   'limitations':'Observed current values permuted, current squared sum preserved; ambient and T0 fixed; offline model-based scenarios, not observed intervention; no EV charging site.'}
 (D/'sintef_load_order_cases.csv').write_text('start,original_final_C,frontloaded_final_C,backloaded_final_C,original_max_C,frontloaded_max_C,backloaded_max_C\n'+''.join(','.join(str(x[y]) for y in ['start','observed_order_final_C','frontloaded_final_C','backloaded_final_C','observed_order_max_C','frontloaded_max_C','backloaded_max_C'])+'\n' for x in cases))
 fig,ax=plt.subplots(figsize=(7.7,4));ax.plot(grid,sse/sse.min());ax.axvline(params[0],linestyle='--',label='Fitted effective tau')
 ax.set(xlabel='Effective tau (hours)',ylabel='Training SSE / minimum',title='SINTEF one-step tau profile (not a confidence interval)');ax.legend();fig.tight_layout();fig.savefig(D/'sintef_tau_profile.png',dpi=180);plt.close(fig)
 fig,ax=plt.subplots(figsize=(7.7,3.8));ax.hist([x['frontloaded_final_C']-x['backloaded_final_C'] for x in cases],bins=24)
 ax.set(xlabel='Frontloaded minus backloaded final oil temperature (°C)',ylabel='24-hour windows',title='Equal-current-square thermal timing sensitivity (within SINTEF only)');fig.tight_layout();fig.savefig(D/'sintef_load_order.png',dpi=180);plt.close(fig)
 return report

def epfl_analysis():
 sys.path.insert(0,str(ROOT/'thermal_extension_20261111'))
 from epfl_reproduce import read_sessions
 s=read_sessions()
 assert len(s)==1878
 # session values original sensor report, observed stay windows, not customer stated need.
 good=[x for x in s if x['b']>x['a'] and x['Pmax']>0 and x['E']>=0]
 arrival=np.array([24*(x['a']%1) for x in good]);dur=np.array([24*(x['b']-x['a']) for x in good]);eng=np.array([x['E'] for x in good]);power=np.array([x['Pmax'] for x in good])
 rho=spearmanr(dur,eng)
 byday=defaultdict(list)
 for x in good:
  if math.floor(x['a'])==math.floor(x['b']-1e-10):byday[math.floor(x['a'])].append(x)
 daily=[]
 for day,items in sorted(byday.items()):
  events=sorted([(x['a'],+1) for x in items]+[(x['b'],-1) for x in items])
  n=0;peak=0
  for _,d in events:
   n+=d;peak=max(peak,n)
  daily.append({'day_serial':day,'sessions':len(items),'peak_active_sessions':peak,'total_reported_energy_kWh':float(sum(x['E'] for x in items))})
 # Bootstrap entire observed days: no resampling individual minutes or inventing users.
 vals=np.array([x['peak_active_sessions'] for x in daily]);rng=np.random.default_rng(20261111)
 boot=np.mean(rng.choice(vals,size=(1500,len(vals)),replace=True),axis=1)
 report={'sessions':len(s),'valid_arrival_departure_power_energy_sessions':len(good),'same_calendar_day_sessions':int(sum(len(x) for x in byday.values())),
 'days_with_same_day_sessions':len(daily),'session_energy_kWh_quantiles_10_50_90':np.quantile(eng,[.1,.5,.9]).tolist(),
 'stay_hours_quantiles_10_50_90':np.quantile(dur,[.1,.5,.9]).tolist(), 'arrival_hour_quantiles_10_50_90':np.quantile(arrival,[.1,.5,.9]).tolist(),
 'session_power_field_kW_quantiles_10_50_90':np.quantile(power,[.1,.5,.9]).tolist(), 'spearman_stay_duration_vs_recorded_energy':float(rho.statistic),
 'daily_peak_active_sessions_median':float(np.median(vals)), 'daily_peak_active_sessions_mean':float(np.mean(vals)),
 'block_bootstrap_day_mean_peak_95pct_interval':np.quantile(boot,[.025,.975]).tolist(),
 'joint_dependence':'Resampling intact observed calendar days preserves within-day session dependence; does not model out-of-sample site growth or temporal nonstationarity.',
 'reported_energy_measurement_boundary':'Session energy is observed record, not verified driver target; minute-power energy mismatch unresolved.',
 'reproduced_16day_peak_optimization_status':'Previously executed/recorded baseline, 44.0092% median vs hypothetical frontloading; new script does not claim reoptimizing it.',
 'charging_thermal_objective':'BLOCKED_NO_QUALIFIED_POWER_TO_TRANSFORMER_CURRENT_THERMAL_TRANSFER'}
 fig,ax=plt.subplots(figsize=(7.7,3.8));ax.hist(vals,bins=np.arange(.5,max(vals)+1.5,1));ax.set(xlabel='Simultaneously active recorded sessions',ylabel='Days',title='EPFL day-block concurrency (measured session times)');fig.tight_layout();fig.savefig(D/'epfl_daily_concurrency.png',dpi=180);plt.close(fig)
 with (D/'epfl_day_summary.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=daily[0].keys());w.writeheader();w.writerows(daily)
 return report

def ku_analysis():
 result={};total=0
 with zipfile.ZipFile(KU) as z:
  for name in sorted(n for n in z.namelist() if n.endswith('.csv')):
   with z.open(name) as f:rows=list(csv.DictReader(io.TextIOWrapper(f,encoding='utf-8-sig')))
   total+=len(rows)
   k='BMSmaxPackTemperature';x=np.array([float(r[k]) if r.get(k) not in ('',None) else np.nan for r in rows]); valid=x[np.isfinite(x)]
   dates=[r['timestamps'] for r in rows]
   result[name]={'rows':len(rows),'battery_max_pack_temperature_count':len(valid),'range_native':[float(valid.min()),float(valid.max())] if len(valid) else None,
   'temperature_column_name':k,'measurement_semantics':'BMS-reported pack temperature; not charger rectifier temperature',
   'timestamp_negative_step_count':int(sum(dates[i]<dates[i-1] for i in range(1,len(dates))))}
 return {'total_rows':total,'files':result,'battery_charger_thermal_causality':'NOT_ESTABLISHED'}

def stream_analysis():
 with SP.open(newline='') as f:p=list(csv.reader(f))
 with SQ.open(newline='') as f:q=list(csv.reader(f))
 assert p[0]==q[0] and [x[0] for x in p[1:]]==[x[0] for x in q[1:]]
 names=p[0][1:]; pnum=np.array([[float(v) if v else np.nan for v in row[1:]] for row in p[1:]]);
 qnum=np.array([[float(v) if v else np.nan for v in row[1:]] for row in q[1:]])
 native=np.hypot(pnum,qnum);out=[]
 for j,name in enumerate(names):
  a=pnum[:,j];b=qnum[:,j];s=native[:,j]
  out.append({'station':name,'P_p50_native':float(np.nanmedian(a)),'Q_p50_native':float(np.nanmedian(b)),
    'P_Q_pearson':float(np.corrcoef(a,b)[0,1]),'sqrtP2Q2_p50_native_if_units_consistent':float(np.nanmedian(s)),
    'sqrtP2Q2_p95_native_if_units_consistent':float(np.nanquantile(s,.95)),
    'fraction_Q_negative':float(np.nanmean(b<0))})
 return {'time_rows':len(p)-1,'stations':len(names),'P_Q_station_time_pairs':(len(p)-1)*len(names),'native_value_units':'UNVERIFIED; sqrt(P²+Q²) is not qualified as kVA',
 'P_Q_station_statistics':out,'harmonics_from_P_Q':'BLOCKED_NO_HARMONIC_SPECTRA_OR_WAVEFORMS','thermal_loss_from_P_Q':'BLOCKED_UNKNOWN_RATINGS_VOLTAGE_BOUNDARY_AND_LOSS_LAW'}

def numerical_verification(tau):
 init=0.37;forcing=1.0;exact=forcing+(init-forcing)*np.exp(-1/tau)
 dat=[]
 for h in [1,.5,.25,.125,.0625]:
  n=round(1/h);z=init;r=init
  for _ in range(n):
   z+=h*(forcing-z)/tau
   fn=lambda x:(forcing-x)/tau
   k1=fn(r);k2=fn(r+h*k1/2);k3=fn(r+h*k2/2);k4=fn(r+h*k3)
   r+=h*(k1+2*k2+2*k3+k4)/6
  dat.append({'substeps':n,'euler_abs_error':abs(z-exact),'rk4_abs_error':abs(r-exact)})
 return {'exact_solution':exact,'rows':dat,'interpretation':'Numerical test ODE with fixed forcing and nondimensional temperature; not physical validation.'}

def main():
 for p in FILES:
  assert p.exists(),str(p)
 manifest=[{'filename':x.name,'size_bytes':x.stat().st_size,'SHA256':sourcehash(x),'source':'Authenticated Drive-backed original mounted files'} for x in FILES]
 (D/'ORIGINAL_INPUT_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
 print('SOURCE HASHES WRITTEN',flush=True)
 t,a=read_sintef();sin=thermal_fit(t,a);print('SINTEF',json.dumps({k:v for k,v in sin.items() if k not in ('tau_profile','hot_spot_audit','local_sensitivity')}),flush=True)
 ep=epfl_analysis();print('EPFL',json.dumps(ep),flush=True)
 ku=ku_analysis();print('KU',ku['total_rows'],flush=True)
 stream=stream_analysis();print('STREAM',stream['P_Q_station_time_pairs'],flush=True)
 verification=numerical_verification(sin['params_effective']['tau_h'])
 res={'run_date':'2026-11-11','status':'EXPLORATORY assistant-executed; no same-site thermal EV coupling','original_data_sha256':manifest,
     'SINTEF':sin,'EPFL':ep,'KU_Leuven':ku,'STREAM':stream,'ODE_solver_check':verification,
     'scientific_gates':{'SO1':'PARTIAL_COMPONENT_ONLY','SO2':'PARTIAL_TRANSFORMER_ODE_ONLY','SO3':'BLOCKED_THERMAL_SERVICE_CAUSALITY',
       'aging_life':'BLOCKED_SENSOR_SEMANTICS_AND_EQUIPMENT_APPLICABILITY','harmonic_losses':'BLOCKED_MISSING_SPECTRA',
       'temperature_constrained_EV_optimization':'BLOCKED_SOURCE_TO_SITE_POWER_CURRENT_AND_THERMAL_CAPABILITY_MAPPING',
       'extreme_heat_empirical_validation':'BLOCKED_NO_30C_PLUS_AMBIENT_MEASUREMENTS_IN_SINTEF',
       'PDE_model':'BLOCKED_EXACT_EQUIPMENT_GEOMETRY_AND_MATERIAL_PROPERTIES',
       'Q_compensation_thermal_benefit':'BLOCKED_RATINGS_CAPABILITY_VOLTAGE_AND_LOSS_LAW'}}
 (D/'RESULTS.json').write_text(json.dumps(res,indent=2,allow_nan=False))
 print('DONE',D,flush=True)
if __name__=='__main__':main()
