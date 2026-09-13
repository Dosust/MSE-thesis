import csv,json,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from egmiv_h1 import Line,RadialNetwork,Cell,Turn,CTMNetwork,Charger,M0Runner,M1Runner

ROOT=Path(__file__).resolve().parents[1]

def build(dt=0.01):
    power=RadialNetwork(3,0,[Line(0,1,0.005,0.002,2.0),Line(1,2,0.005,0.002,1.0)],v_min_pu=0.9)
    traffic=CTMNetwork([Cell(1,60,20,150,1800,0),Cell(1,60,20,150,1800,1800)],1,[Turn(0,1,0,1.0)],dt_h=dt)
    charger=Charger(2,0,0,1.0,0.08,0.0001,0.9)
    return power,traffic,charger

def arrays(K=120,demand=600.0):
    p=np.tile([0.0,0.15,0.10],(K,1)); q=np.tile([0.0,0.03,0.02],(K,1)); pa=np.ones((K,2),bool)
    td=np.zeros((K,2,1)); td[:,0,0]=demand; occ=np.zeros((2,1)); ca=np.ones((K,2),bool)
    return p,q,pa,td,occ,ca

def discrepancy(a,b):
    return float(np.mean(np.abs(np.asarray(a)-np.asarray(b))))

rows=[]
for sid,demand,outage,chargers in [('S0',600,False,True),('S1',900,False,True),('S2',600,True,True),('S6',600,False,False)]:
    power,traffic,charger=build(); args=list(arrays(demand=demand))
    if outage: args[2][60:,1]=False
    r0=M0Runner(power,traffic).run(*args)
    r1=M1Runner(power,traffic,[charger] if chargers else []).run(*args)
    row={
      'scenario':sid,
      'demand_vph':demand,
      'outage':outage,
      'coupling_enabled':chargers,
      'M0_LP_h':r0.cumulative_power_service_loss_h,
      'M1_LP_h':r1.cumulative_power_service_loss_h,
      'M0_LT_h':r0.cumulative_transport_service_loss_h,
      'M1_LT_h':r1.cumulative_transport_service_loss_h,
      'D_SP_mean_abs':discrepancy(r1.power_service,r0.power_service),
      'D_ST_mean_abs':discrepancy(r1.transport_service,r0.transport_service),
      'M0_max_line_loading':max(x.max_thermal_loading for x in r0.power_results),
      'M1_max_line_loading':max(x.max_thermal_loading for x in r1.power_results),
      'M0_min_voltage_pu':min(x.min_voltage_pu for x in r0.power_results),
      'M1_min_voltage_pu':min(x.min_voltage_pu for x in r1.power_results),
      'M1_mean_fulfillment':float(r1.charger_fulfillment.mean()) if r1.charger_fulfillment.size else 1.0,
      'M1_mapping_residual_pu':r1.max_ev_load_mapping_residual_pu,
    }
    rows.append(row)

csvp=ROOT/'reports'/'m0_m1_matched_scenarios.csv'
with csvp.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
report={
 'method':'EGMIV','hypothesis':'H1','comparison':'M0_vs_M1','parameter_status':'BENCHMARK_TEST_HARNESS_ONLY',
 'scenarios':rows,
 'interpretation':[
  'S0 tests normal coupled operation; differences in voltage/loading are allowed, but all physical constraints must remain feasible.',
  'S1 increases same-step transport/charging demand and tests T→P algebraic loading without queue memory.',
  'S2 de-energizes the charger bus halfway through the horizon and tests immediate P→T charging-service loss.',
  'S6 removes all charger interfaces and must numerically collapse M1 to M0.',
  'No engineering-materiality threshold is evaluated here; the report is verification evidence, not H1 confirmation.'
 ]
}
(ROOT/'reports'/'m1_matched_scenarios.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
