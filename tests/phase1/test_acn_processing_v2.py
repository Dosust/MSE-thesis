from datetime import date
import pytest, numpy as np
from phase1_exec.acn_processing import ACNProcessingError
from phase1_exec.acn_processing_v2 import (collapse_equal_timestamps, session_trace_v2,
    calibrate_global_effective_voltage,reconstructed_active_energy_kwh,aggregate_day_power_kw_v2)

def sess(cur_t=None,cur_v=None,pilot_t=None,pilot_v=None,done='Thu, 10 Oct 2019 07:10:00 GMT',disc='Thu, 10 Oct 2019 07:20:00 GMT',e=0.37):
    cur_t=cur_t or ['Thu, 10 Oct 2019 07:00:00 GMT','Thu, 10 Oct 2019 07:05:00 GMT','Thu, 10 Oct 2019 07:10:00 GMT']
    cur_v=cur_v or [10,10,10]; pilot_t=pilot_t or cur_t; pilot_v=pilot_v or [16]*len(pilot_t)
    return {'sessionID':'S1','siteID':'caltech','spaceID':'CA-308','timezone':'America/Los_Angeles',
      'connectionTime':'Thu, 10 Oct 2019 07:00:00 GMT','disconnectTime':disc,'doneChargingTime':done,'kWhDelivered':e,
      'chargingCurrent':{'timestamps':cur_t,'current':cur_v},'pilotSignal':{'timestamps':pilot_t,'pilot':pilot_v}}

def test_duplicate_equal_times_collapsed_by_mean_without_sorting():
    t=['Thu, 10 Oct 2019 07:00:00 GMT','Thu, 10 Oct 2019 07:00:00 GMT','Thu, 10 Oct 2019 07:05:00 GMT']
    x=collapse_equal_timestamps({'timestamps':t,'current':[8,12,10]},'current','chargingCurrent')
    assert len(x.timestamps)==2 and x.values==(10.0,10.0)

def test_true_backward_time_rejected():
    t=['Thu, 10 Oct 2019 07:05:00 GMT','Thu, 10 Oct 2019 07:00:00 GMT']
    with pytest.raises(ACNProcessingError): collapse_equal_timestamps({'timestamps':t,'current':[10,10]},'current','chargingCurrent')

def test_vector_mismatch_rejected():
    with pytest.raises(ACNProcessingError): collapse_equal_timestamps({'timestamps':['Thu, 10 Oct 2019 07:00:00 GMT','Thu, 10 Oct 2019 07:05:00 GMT'],'current':[10]},'current','chargingCurrent')

def test_gap_rule_retained_after_collapse():
    t=['Thu, 10 Oct 2019 07:00:00 GMT','Thu, 10 Oct 2019 07:06:00 GMT']
    with pytest.raises(ACNProcessingError): collapse_equal_timestamps({'timestamps':t,'current':[10,10]},'current','chargingCurrent')

def test_active_endpoint_is_min_done_disconnect():
    tr=session_trace_v2(sess(done='Thu, 10 Oct 2019 07:10:00 GMT',disc='Thu, 10 Oct 2019 08:00:00 GMT'))
    assert tr.active_end.isoformat().startswith('2019-10-10T07:10:00')

def test_invalid_done_before_connection_rejected():
    with pytest.raises(ACNProcessingError): session_trace_v2(sess(done='Thu, 10 Oct 2019 06:59:00 GMT'))

def test_global_effective_voltage_median_known_answer():
    a=session_trace_v2(sess(e=210*6000/(1000*3600)))
    b=session_trace_v2({**sess(e=230*6000/(1000*3600)),'sessionID':'S2'})
    v,n=calibrate_global_effective_voltage([a,b]); assert n==2; assert v==pytest.approx(220,abs=1e-12)

def test_reconstruction_uses_frozen_scale_and_active_endpoint():
    tr=session_trace_v2(sess(e=1.0))
    assert reconstructed_active_energy_kwh(tr,220)==pytest.approx(220*10*(10/60)/1000,abs=1e-12)

def test_five_min_aggregation_known_answer():
    tr=session_trace_v2(sess(e=1.0))
    stamps,p=aggregate_day_power_kw_v2(date(2019,10,10),[tr],220)
    assert len(stamps)==288 and len(p)==288
    assert p[0]==pytest.approx(2.2,abs=1e-12); assert p[1]==pytest.approx(2.2,abs=1e-12); assert np.allclose(p[2:],0)
