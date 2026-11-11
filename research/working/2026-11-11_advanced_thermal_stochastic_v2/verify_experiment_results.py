"""Readbacks and key numeric falsification checks, no fake data."""
from pathlib import Path
import json, math, hashlib
D=Path('/mnt/data/thermal_extension_20261111_v2')
r=json.loads((D/'RESULTS.json').read_text());p=json.loads((D/'EPFL_REPLAY_RESULTS.json').read_text());m=json.loads((D/'ORIGINAL_INPUT_MANIFEST.json').read_text())
assert len(m)==6 and all(len(x['SHA256'])==64 for x in m)
assert all((Path('/mnt/data')/x['filename']).exists() for x in m)
for x in m:
 h=hashlib.sha256((Path('/mnt/data')/x['filename']).read_bytes()).hexdigest(); assert h==x['SHA256'],x['filename']
s=r['SINTEF']; assert s['row_count']==8592 and s['training_pairs']==6012 and s['holdout_pairs']==2576
assert math.isclose(s['holdout_metrics']['model_rmse_C'],.21652866,abs_tol=.000002)
assert s['holdout_metrics']['model_mae_C']>s['holdout_metrics']['persistence_mae_C']
assert s['same_site_load_order_stress_test']['cases']==106
assert .3<s['same_site_load_order_stress_test']['median_abs_final_difference_front_vs_back_C']<.45
assert .80<s['hot_spot_audit']['Hot-spot HV [degC]']['fraction_below_top_oil']<.90
assert r['EPFL']['sessions']==1878 and p['session_keys_matched_to_power_measurements']==1878
assert p['optimized_days']==16 and math.isclose(p['median_peak_reduction_percent_conditional'],44.0092091,abs_tol=.01)
assert r['KU_Leuven']['total_rows']==40873 and r['STREAM']['P_Q_station_time_pairs']==419184
assert r['scientific_gates']['temperature_constrained_EV_optimization'].startswith('BLOCKED_')
assert r['scientific_gates']['aging_life'].startswith('BLOCKED_')
print('PASS: original source SHA256, numeric reproducibility check, source-boundary/negative-result gates')
