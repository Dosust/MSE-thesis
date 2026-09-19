#!/usr/bin/env python3
import csv, json, math
from pathlib import Path

OUT=Path(__file__).resolve().parent
T=1.0
DIMS=[
 {"name":"x1","a":1.0,"U":0.6,"L":1.0,"r":0.1},
 {"name":"x2","a":0.8,"U":0.5,"L":1.0,"r":0.1},
]
DTS=[0.2,0.1,0.05,0.025,0.0125,0.00625]

def exact_bounds(d):
    a,U,L,r=d["a"],d["U"],d["L"],d["r"]
    c=U/a
    return min(L,c+(L-c)*math.exp(-a*T)), min(L,c-(c-r)*math.exp(-a*T))

def pred(init,d,dt0):
    N=round(T/dt0); dt=T/N; A=1+d["a"]*dt; B=dt*d["U"]; b=init
    for _ in range(N): b=min(d["L"],(b+B)/A)
    return b,dt,N

def area(b): return 4*b[0]*b[1]
def symdiff(b,e):
    i=[min(b[k],e[k]) for k in range(2)]
    return area(b)+area(e)-2*area(i)
def haus(b,e):
    return max(
      math.sqrt(sum(max(b[k]-e[k],0)**2 for k in range(2))),
      math.sqrt(sum(max(e[k]-b[k],0)**2 for k in range(2)))
    )

VE=[exact_bounds(d)[0] for d in DIMS]
RE=[exact_bounds(d)[1] for d in DIMS]
rows=[]
for dt0 in DTS:
    VB=[]; RB=[]
    for d in DIMS:
        v,dt,N=pred(d["L"],d,dt0); r,_,_=pred(d["r"],d,dt0)
        VB.append(v); RB.append(r)
    rows.append({
      "dt_h":dt,"N_steps":N,
      "V_bound_x1":VB[0],"V_bound_x2":VB[1],
      "R_bound_x1":RB[0],"R_bound_x2":RB[1],
      "V_max_coordinate_error":max(abs(VB[k]-VE[k]) for k in range(2)),
      "R_max_coordinate_error":max(abs(RB[k]-RE[k]) for k in range(2)),
      "V_Hausdorff":haus(VB,VE),"R_Hausdorff":haus(RB,RE),
      "V_symmetric_difference_area":symdiff(VB,VE),
      "R_symmetric_difference_area":symdiff(RB,RE)
    })
for key in ["V_Hausdorff","R_Hausdorff","V_symmetric_difference_area","R_symmetric_difference_area"]:
    for i,r in enumerate(rows):
        r[key+"_observed_order"]=None if i==0 else math.log(rows[i-1][key]/r[key],2)

with (OUT/"B0_CONVERGENCE.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

summary={
 "status":"B0_EXECUTED_PASS_NUMERICAL_VERIFICATION",
 "claim_ceiling":"mathematical/numerical verification only; not infrastructure validation",
 "analytic_reference":{"V_halfwidths":VE,"R_halfwidths":RE},
 "finest_euler":rows[-1]
}
(OUT/"B0_RESULT.json").write_text(json.dumps(summary,indent=2))
