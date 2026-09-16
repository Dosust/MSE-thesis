"""Prospective ACN processing v2 implementing PHASE1_ACN_PROCESSING_AMENDMENT_V2.

This module performs deterministic structural QC, exact-timestamp collapse,
active-charging truncation, one-scalar development calibration, and 5-minute
aggregation. It does not inspect holdout outcomes or execute H1/H2.
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Mapping, Sequence, Tuple, List
import numpy as np
from .acn_processing import (ACNProcessingError, GRID_MINUTES, GRID_SECONDS,
    MAX_TRACE_GAP_SECONDS, SLOTS_PER_24H_DAY, day_status, local_day_bounds,
    parse_aware_timestamp)

@dataclass(frozen=True)
class TimeSeriesV2:
    timestamps: Tuple[datetime,...]
    values: Tuple[float,...]

@dataclass(frozen=True)
class SessionTraceV2:
    session_id: str
    site_id: str
    station_id: str
    connection: datetime
    disconnect: datetime
    active_end: datetime
    kwh_delivered: float
    current: TimeSeriesV2
    pilot: TimeSeriesV2

def _finite_nonnegative(x:object,name:str)->float:
    try: v=float(x)
    except (TypeError,ValueError) as exc: raise ACNProcessingError(f'{name} must be numeric') from exc
    if not math.isfinite(v) or v<0: raise ACNProcessingError(f'{name} must be finite and nonnegative')
    return v

def collapse_equal_timestamps(obj:object,value_key:str,field_name:str)->TimeSeriesV2:
    if not isinstance(obj,Mapping): raise ACNProcessingError(f'{field_name} must be an object')
    if 'timestamps' not in obj or value_key not in obj: raise ACNProcessingError(f"{field_name} must contain 'timestamps' and {value_key!r}")
    rt=obj['timestamps']; rv=obj[value_key]
    if not isinstance(rt,Sequence) or isinstance(rt,(str,bytes)): raise ACNProcessingError(f'{field_name}.timestamps must be a sequence')
    if not isinstance(rv,Sequence) or isinstance(rv,(str,bytes)): raise ACNProcessingError(f'{field_name}.{value_key} must be a sequence')
    if len(rt)!=len(rv): raise ACNProcessingError(f'{field_name} timestamp/value lengths differ')
    if len(rt)<2: raise ACNProcessingError(f'{field_name} needs at least two samples')
    ts=[parse_aware_timestamp(str(x)) for x in rt]
    vs=[_finite_nonnegative(x,f'{field_name}.{value_key}') for x in rv]
    ots=[]; ovs=[]; i=0
    while i<len(ts):
        t=ts[i]; vals=[vs[i]]; j=i+1
        while j<len(ts) and ts[j]==t:
            vals.append(vs[j]); j+=1
        if j<len(ts) and ts[j]<t:
            raise ACNProcessingError(f'{field_name} contains genuine backward time')
        ots.append(t); ovs.append(float(sum(vals)/len(vals))); i=j
    if len(ots)<2: raise ACNProcessingError(f'{field_name} needs at least two distinct timestamps after duplicate collapse')
    for a,b in zip(ots,ots[1:]):
        dt=(b-a).total_seconds()
        if dt<=0: raise ACNProcessingError(f'{field_name} timestamps invalid after duplicate collapse')
        if dt>MAX_TRACE_GAP_SECONDS: raise ACNProcessingError(f'{field_name} contains gap {dt:.0f}s > {MAX_TRACE_GAP_SECONDS}s')
    return TimeSeriesV2(tuple(ots),tuple(ovs))

def session_trace_v2(session:Mapping[str,object])->SessionTraceV2:
    required=('sessionID','siteID','spaceID','connectionTime','disconnectTime','doneChargingTime','kWhDelivered','chargingCurrent','pilotSignal')
    missing=[k for k in required if k not in session]
    if missing: raise ACNProcessingError(f'missing required session fields: {missing}')
    c=parse_aware_timestamp(str(session['connectionTime'])); d=parse_aware_timestamp(str(session['disconnectTime']))
    done=parse_aware_timestamp(str(session['doneChargingTime']))
    if not c<d: raise ACNProcessingError('connectionTime must precede disconnectTime')
    if done<c: raise ACNProcessingError('doneChargingTime must not precede connectionTime')
    e=min(done,d)
    if 'timezone' in session and str(session['timezone'])!='America/Los_Angeles': raise ACNProcessingError('unexpected ACN timezone for Caltech session')
    return SessionTraceV2(
        session_id=str(session['sessionID']), site_id=str(session['siteID']), station_id=str(session['spaceID']),
        connection=c, disconnect=d, active_end=e,
        kwh_delivered=_finite_nonnegative(session['kWhDelivered'],'kWhDelivered'),
        current=collapse_equal_timestamps(session['chargingCurrent'],'current','chargingCurrent'),
        pilot=collapse_equal_timestamps(session['pilotSignal'],'pilot','pilotSignal'))

def _integral_linear(ts:TimeSeriesV2,start:datetime,end:datetime)->float:
    if end<=start: return 0.0
    x=np.asarray([t.timestamp() for t in ts.timestamps],dtype=float); y=np.asarray(ts.values,dtype=float)
    lo=max(start.timestamp(),x[0]); hi=min(end.timestamp(),x[-1])
    if hi<=lo: return 0.0
    interior=x[(x>lo)&(x<hi)]; grid=np.concatenate(([lo],interior,[hi])); vals=np.interp(grid,x,y)
    return float(np.trapezoid(vals,grid))

def active_amp_seconds(trace:SessionTraceV2)->float:
    return _integral_linear(trace.current,trace.connection,trace.active_end)

def calibrate_global_effective_voltage(traces:Sequence[SessionTraceV2])->tuple[float,int]:
    implied=[]
    for tr in traces:
        if tr.kwh_delivered<=0: continue
        a=active_amp_seconds(tr)
        if a<=0: continue
        implied.append(1000.0*3600.0*tr.kwh_delivered/a)
    if not implied: raise ACNProcessingError('no eligible positive-energy development sessions for V_eff calibration')
    return float(np.median(np.asarray(implied,dtype=float))),len(implied)

def reconstructed_active_energy_kwh(trace:SessionTraceV2,v_eff:float)->float:
    v=_finite_nonnegative(v_eff,'V_eff')
    if v<=0: raise ACNProcessingError('V_eff must be positive')
    return v*active_amp_seconds(trace)/(1000.0*3600.0)

def aggregate_day_power_kw_v2(day:date,traces:Sequence[SessionTraceV2],v_eff:float)->tuple[List[datetime],np.ndarray]:
    status=day_status(day)
    if not status.accepted: raise ACNProcessingError(status.reason)
    v=_finite_nonnegative(v_eff,'V_eff')
    if v<=0: raise ACNProcessingError('V_eff must be positive')
    s,e=local_day_bounds(day); edges=[s+timedelta(seconds=i*GRID_SECONDS) for i in range(SLOTS_PER_24H_DAY+1)]
    energy=np.zeros(SLOTS_PER_24H_DAY,dtype=float)
    for tr in traces:
        if tr.active_end<=s or tr.connection>=e: continue
        lo_sec=max(0.0,(tr.connection-s).total_seconds())
        hi_sec=min(24*3600.0,(tr.active_end-s).total_seconds())
        if hi_sec<=lo_sec: continue
        k0=max(0,int(lo_sec//GRID_SECONDS))
        k1=min(SLOTS_PER_24H_DAY-1,int(np.nextafter(hi_sec,-np.inf)//GRID_SECONDS))
        for k in range(k0,k1+1):
            lo=max(edges[k],tr.connection); hi=min(edges[k+1],tr.active_end)
            if hi<=lo: continue
            a=_integral_linear(tr.current,lo,hi)
            if a: energy[k]+=v*a/(1000.0*3600.0)
    return edges[:-1],energy/(GRID_MINUTES/60.0)
