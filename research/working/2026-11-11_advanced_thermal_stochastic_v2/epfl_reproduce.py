#!/usr/bin/env python3
"""Drive-only EPFL original-file QA and hypothetical offline charging LP.
The original xlsx files were authenticated as Google Drive files in this chat.
The output is NOT an actual control outcome, thermal derating, or vehicle trip impact.
"""
import csv, json, math, re, zipfile
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timedelta
from lxml import etree
from artifact_tool import Blob, SpreadsheetFile
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path('/mnt/data/thermal_extension_20261111');D.mkdir(exist_ok=True)
R=Path('/mnt/data');N='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

def read_sessions():
 w=SpreadsheetFile.import_xlsx(Blob.load(str(R/'Session_data.xlsx')))
 v=w.worksheets.get_item_at(0).get_range('A1:N1879').values
 assert v[0][0]=='Session' and v[0][5]=='Energy (Wh)'
 return [{'sid':int(x[0]),'ccs':str(x[1]),'a':float(x[2]),'b':float(x[3]),'stay_min':float(x[4]),'E':float(x[5])/1000,'Pmax':float(x[6])/1000} for x in v[1:]]

def measurement_stream():
    # Read the actual OOXML worksheet bytes with standard ZIP and regex primitives.
    # This avoids hydrating ~1.29 million mostly blank rows as spreadsheet cells.
    info={};meas=defaultdict(list)
    pat=re.compile(rb'<c r="D(\d+)"[^>]*><v>([^<]+)</v>')
    ap=re.compile(rb'<c r="A\d+"[^>]*><v>([^<]+)</v>')
    cp=re.compile(rb'<c r="C\d+"[^>]*><v>([^<]+)</v>')
    with zipfile.ZipFile(R/'Measurement_data.xlsx') as z:
        for name,ccs in [('xl/worksheets/sheet1.xml','CCS1'),('xl/worksheets/sheet2.xml','CCS2')]:
            raw=z.read(name)
            total=raw.count(b'<row ')
            populated=0
            for m in pat.finditer(raw):
                rid=int(m.group(1))
                if rid==1:continue
                st=raw.rfind(b'<row ',0,m.start())
                prefix=raw[st:m.start()]
                ma=ap.search(prefix);mc=cp.search(prefix)
                if ma is None or mc is None:continue
                serial=float(ma.group(1));sid=int(float(mc.group(1)))
                power=float(m.group(2))
                meas[(ccs,sid)].append((serial,power))
                populated+=1
            info[ccs]={'worksheet_rows_including_header':total,'populated_power_rows':populated}
            print(ccs,'populated power rows',populated,flush=True)
            del raw
    return info,meas

def optimize(day_sessions):
 sessions=[]
 for r in day_sessions:
  a=int(round(r['a']*1440));b=int(round(r['b']*1440));e=r['E'];p=r['Pmax']
  if b<=a or e>p*(b-a)/60 or p<=0:return None
  sessions.append((r['ccs'],a,b,p,e))
 for i,(c,a,b,p,e) in enumerate(sessions):
  for C,A,B,P,E in sessions[i+1:]:
   if c==C and max(a,A)<min(b,B):return None
 mn=defaultdict(list);var=[]
 for i,(c,a,b,p,e) in enumerate(sessions):
  for t in range(a,b):
   j=len(var);var.append((i,t,p));mn[t].append(j)
 n=len(var)
 if not n or n>8000:return None
 row=[];col=[];value=[];rhs=[];kk=0
 # Per-session energy equality at optimum: sum(power_i,t / 60) >= recorded delivered kWh.
 for i,(c,a,b,p,e) in enumerate(sessions):
  for j,(ii,t,pj) in enumerate(var):
   if ii==i:row.append(kk);col.append(j);value.append(-1/60)
  rhs.append(-e);kk+=1
 # Aggregate one-minute peak: sum_j power_j,t <= Ppeak.
 for t,ids in mn.items():
  for j in ids:row.append(kk);col.append(j);value.append(1.)
  row.append(kk);col.append(n);value.append(-1.);rhs.append(0);kk+=1
 A=coo_matrix((value,(row,col)),shape=(kk,n+1)).tocsr()
 obj=np.zeros(n+1);obj[-1]=1
 res=linprog(obj,A_ub=A,b_ub=rhs,bounds=[(0,x[2]) for x in var]+[(0,None)],method='highs')
 if not res.success:return None
 delivered=np.zeros(len(sessions));optimized=defaultdict(float);frontloaded=defaultdict(float)
 for j,(i,t,p) in enumerate(var):
  delivered[i]+=res.x[j]/60;optimized[t]+=res.x[j]
 for c,a,b,p,e in sessions:
  remaining=e
  for t in range(a,b):
   rate=min(p,max(remaining,0)*60);frontloaded[t]+=rate;remaining-=rate/60
   if remaining<=1e-9:break
 assert np.all(delivered>=np.array([r[-1] for r in sessions])-1e-5)
 peak_a=max(frontloaded.values());peak_b=max(optimized.values())
 assert peak_b<=peak_a+1e-5
 return {'sessions':len(sessions),'variables':n,'frontloaded_hypothetical_peak_kW':peak_a,'optimized_hypothetical_peak_kW':peak_b,'peak_reduction_percent_conditional':100*(peak_a-peak_b)/peak_a,'maximum_numerical_energy_shortfall_kWh':float(max(0,np.max(np.array([r[-1] for r in sessions])-delivered)))}

def main():
 ss=read_sessions();print('EPFL session rows',len(ss),flush=True)
 sheets,raw=measurement_stream()
 integ=[];delta=[];matched=0
 for s in ss:
  key=(s['ccs'],s['sid']-1129 if s['ccs']=='CCS2' else s['sid'])
  if key not in raw:continue
  r=sorted(raw[key]);matched+=1;energy=0
  delta.append(abs(r[0][0]-s['a'])*1440)
  for (t,p),(u,q) in zip(r,r[1:]):
   dm=(u-t)*1440
   if .98<=dm<=1.02:energy+=p*dm/60000 # kWh from W*min /60000
  if s['E']>0:integ.append((energy,s['E']))
 byday=defaultdict(list)
 for s in ss:
  day=int(s['a'])
  if s['b']<=day+1:byday[day].append(s)
 selected=[]
 for day,daylist in byday.items():
  if len(daylist)<7:continue
  ev=sorted([(round(x['a']*1440),1) for x in daylist]+[(round(x['b']*1440),-1) for x in daylist]);active=mx=0
  for t,d in ev:active+=d;mx=max(mx,active)
  if mx>=2:selected.append((len(daylist),day,daylist))
 solved=[]
 for _,day,items in sorted(selected,key=lambda x:(-x[0],x[1]))[:16]:
  z=optimize(items)
  if z:
   z['date']=str(datetime(1899,12,30)+timedelta(days=int(day)))[:10]
   solved.append(z)
 report={'recorded_sessions':len(ss),'two_connectors':dict(__import__('collections').Counter(s['ccs'] for s in ss)),'worksheet_audit':sheets,'populated_minute_power_rows':sum(x['populated_power_rows'] for x in sheets.values()),'published_minute_row_count':64277,
         'session_keys_matched_to_power_measurements':matched,'CCS2_measurement_local_id_offset':1129,'max_start_timestamp_discrepancy_minutes':float(max(delta)),'total_reported_session_energy_kWh':float(sum(s['E'] for s in ss)),
         'total_contiguous_integrated_measured_power_kWh':float(sum(e for e,r in integ)),
         'median_abs_fractional_energy_discrepancy':float(np.median([abs(e-r)/r for e,r in integ])),
         'fraction_integrated_energy_within_10pct_session_energy':float(np.mean([abs(e-r)/r<.1 for e,r in integ])),
         'eligible_overlap_days':len(selected),'optimized_days':len(solved),'offline_optimization_results':solved,
         'median_peak_reduction_percent_conditional':float(np.median([x['peak_reduction_percent_conditional'] for x in solved])) if solved else None,
         'interpretation':'Energy in the session workbook is a measured reported outcome, not an independently documented requested charging need. Differences between power integration and session energy must not be called losses. Scheduling results are offline conditional counterfactuals, not observed implemented outcomes. Pmax is a session field, not verified station rating; site transformer is not known.'}
 (D/'epfl_results.json').write_text(json.dumps(report,indent=2))
 if solved:
  fig,ax=plt.subplots(figsize=(8.5,3.8));xx=np.arange(len(solved))
  ax.plot(xx,[i['frontloaded_hypothetical_peak_kW'] for i in solved],marker='o',label='Immediate charging at recorded Pmax')
  ax.plot(xx,[i['optimized_hypothetical_peak_kW'] for i in solved],marker='o',label='Offline LP lower peak')
  ax.set(title='EPFL hypothetical charging schedules, not observed intervention',xlabel='Selected high-use day',ylabel='Aggregate charging power (kW)');ax.legend();fig.tight_layout();fig.savefig(D/'epfl_counterfactual.png',dpi=180);plt.close(fig)
 print('FINISHED',json.dumps({k:v for k,v in report.items() if k!='offline_optimization_results'}),flush=True)
if __name__=='__main__':main()
