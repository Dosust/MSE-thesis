#!/usr/bin/env python3
"""Evidence-aware, stdlib-only audit for the user's EV charging / routing ZIP.

No inference of field measurement, physical thermal coupling or causation is made.
All input data remain unchanged. Run with:
    python audit_uploaded_ev_archive.py /path/to/archive.zip /path/to/output_dir
"""
from __future__ import annotations
import csv, datetime as dt, hashlib, io, json, math, statistics, sys, zipfile
from collections import Counter
from pathlib import Path

EXPECTED = {'ev_charging_dataset.csv', 'location_dataset.csv'}
KEYS = ['Vehicle_ID', 'Charging_Station_ID', 'Battery_Capacity_kWh', 'Session_Start_Hour',
        'Weekday', 'Weather_Conditions', 'Road_Conditions', 'Fleet_Size']

def sha256_file(path: Path) -> str:
    sha=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):
            sha.update(chunk)
    return sha.hexdigest()

def sha256_stream(stream) -> str:
    sha=hashlib.sha256()
    for chunk in iter(lambda:stream.read(1024*1024),b''):
        sha.update(chunk)
    return sha.hexdigest()

def haversine_km(lat1,lon1,lat2,lon2):
    dlat=math.radians(lat2-lat1);dlon=math.radians(lon2-lon1)
    a=math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    return 6371.0088*2*math.asin(min(1,math.sqrt(max(0,a))))

def audit(path: Path, dest:Path, drive_url: str = ''):
    dest.mkdir(parents=True,exist_ok=True)
    sha_zip=sha256_file(path)
    with zipfile.ZipFile(path) as z:
        integrity=z.testzip()
        if integrity is not None: raise RuntimeError(f'ZIP integrity problem: {integrity}')
        names=set(z.namelist())
        if names!=EXPECTED: raise RuntimeError(f'Unexpected archive members: {sorted(names)}')
        file_hashes={n:sha256_stream(z.open(n)) for n in sorted(names)}
        uniques={k:set() for k in KEYS}
        missing=Counter(); weather=Counter(); road=Counter(); nonfinite=Counter()
        n=0; min_dt=None;max_dt=None;prev_dt=None;time_discontinuity=0;duplicate_times=0
        weekday_mismatch=0; energy_exceeds_rate_duration=0; load_exceeds_charge_rate=0
        distance_mismatch_gt20=0;distance_geodesic_samples=0
        zero_temp=0; temperature_over40=0;duration_nonpositive=0
        temp_sum=0.0; min_temp=math.inf; max_temp=-math.inf
        energy_sum=0.; charging_load_sum=0.; datetime_midnight=0
        clear_precip_positive=0; clear_count=0
        first_rows=[]
        with z.open('ev_charging_dataset.csv') as raw:
            reader=csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8-sig',newline=''))
            headers=reader.fieldnames or []
            if len(headers)!=28: raise RuntimeError(f'Expected 28 fields, got {len(headers)}')
            for row in reader:
                n+=1
                if n<=3: first_rows.append({k:row[k] for k in ['Date_Time','Vehicle_ID','Battery_Capacity_kWh','Weekday','Session_Start_Hour']})
                for k in KEYS:uniques[k].add(row[k])
                for k,v in row.items():
                    if v is None or v=='':missing[k]+=1
                moment=dt.datetime.fromisoformat(row['Date_Time'])
                if prev_dt is not None:
                    if moment-prev_dt!=dt.timedelta(hours=1):time_discontinuity+=1
                    if moment==prev_dt:duplicate_times+=1
                prev_dt=moment
                min_dt=moment if min_dt is None or moment<min_dt else min_dt
                max_dt=moment if max_dt is None or moment>max_dt else max_dt
                if moment.hour==0:datetime_midnight+=1
                if int(float(row['Weekday']))!=moment.weekday():weekday_mismatch+=1
                rate=float(row['Charging_Rate_kW']); duration=float(row['Time_Spent_Charging_mins']); energy=float(row['Energy_Drawn_kWh']); load=float(row['Charging_Load_kW'])
                if duration<=0:duration_nonpositive+=1
                if energy>rate*duration/60 + 1e-8:energy_exceeds_rate_duration+=1
                if load>rate+1e-8:load_exceeds_charge_rate+=1
                energy_sum+=energy;charging_load_sum+=load
                temp=float(row['Temperature_C'])
                min_temp=min(temp,min_temp);max_temp=max(temp,max_temp);temp_sum+=temp
                if temp==0:zero_temp+=1
                if temp>40:temperature_over40+=1
                if row['Weather_Conditions']=='Clear':
                    clear_count+=1
                    if float(row['Precipitation_mm'])>0:clear_precip_positive+=1
                weather[row['Weather_Conditions']]+=1
                road[row['Road_Conditions']]+=1
                lat1=float(row['Current_Latitude']);lon1=float(row['Current_Longitude'])
                lat2=float(row['Destination_Latitude']);lon2=float(row['Destination_Longitude'])
                dist=haversine_km(lat1,lon1,lat2,lon2)
                stated=float(row['Distance_to_Destination_km'])
                distance_geodesic_samples+=1
                # Road distance can exceed straight-line distance: this only rejects if stated distance
                # is substantially smaller than the great-circle distance; >20% shorter is implausible.
                if stated<dist*0.8:distance_mismatch_gt20+=1
        with z.open('location_dataset.csv') as raw:
            locations=list(csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8-sig',newline='')))
        types=Counter(x['Type'] for x in locations)
    result={
        'archive_name':path.name,'archive_sha256':sha_zip,'original_member_sha256':file_hashes,
        'source_candidate':'https://www.kaggle.com/datasets/datasetengineer/ev-charging-load-dataset-and-optimal-routing',
        'drive_original_url':drive_url,
        'source_provenance_status':'MATCHING_FILENAME_AND_STRUCTURE; measurement origin and license NOT VERIFIED',
        'field_measurement_status':'NOT_QUALIFIED','synthetic_likelihood':'HIGH based on internal contradictions; generator not proven',
        'csv_file_count':2,'charging_rows':n,'charging_columns':len(headers),'charging_header':headers,
        'first_timestamp':min_dt.isoformat(sep=' '),'last_timestamp':max_dt.isoformat(sep=' '),
        'duplicate_timestamp_adjacent':duplicate_times,'hourly_gap_or_reordering':time_discontinuity,
        'all_columns_missing_cells_total':sum(missing.values()),'missing_by_column':dict(missing),
        'unique_key_counts':{k:len(v) for k,v in uniques.items()},
        'unique_vehicle_ids':sorted(uniques['Vehicle_ID']),
        'unique_charging_station_ids':sorted(uniques['Charging_Station_ID']),
        'weekday_mismatches_monday_0':weekday_mismatch,
        'weekday_agreements_monday_0':n-weekday_mismatch,
        'charging_energy_exceeds_nominal_rate_x_duration':energy_exceeds_rate_duration,
        'charging_load_exceeds_charging_rate':load_exceeds_charge_rate,
        'session_duration_nonpositive':duration_nonpositive,
        'stated_distance_under_80_percent_geodesic':distance_mismatch_gt20,
        'clear_weather_with_positive_precipitation':clear_precip_positive,'clear_weather_rows':clear_count,
        'temperature_min_C':min_temp,'temperature_max_C':max_temp,'temperature_mean_C':temp_sum/n,
        'temperature_gt40_C_rows':temperature_over40,'temperature_eq0_C_rows':zero_temp,
        'location_rows':len(locations),'location_types':dict(types),
        'has_transformer_temperature':False,'has_evse_internal_temperature':False,
        'has_verified_transformer_charger_topology':False,'has_qualified_temperature_derating':False,
        'has_device_sensors_or_calibration_records':False,
        'initial_rows_selected_fields':first_rows,
        'interpretation_notes':[
            'Battery_Capacity_kWh changes dramatically for a single Vehicle_ID; cannot be modeled as a physical repeated-measurement vehicle history.',
            'Weekday is inconsistent with Date_Time when Monday=0; label convention is NOT documented.',
            'Charging rate-duration energy and charge load exceedance tests assume consistent rate/power definitions. Violations imply undocumented conventions or unphysical data, not necessarily the exact generating mechanism.',
            'Temperature_C is an ambient/recorded attribute, not measured transformer oil/hotspot or EVSE electronics temperature.',
            'There are no electrical network edges in location_dataset.csv. Coordinate pairs are abstract points without geographic CRS.',
            'Records are hourly contiguous; this alone is not sensor provenance.',
            'Archive is suitable only for labelled synthetic/illustrative algorithm unit tests and not for field-coupled thermal calibration or external validity claims.'
        ]
    }
    (dest/'audit_results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    checks=[
        ('ZIP_INTEGRITY','PASS','zipfile.testzip() returned None'),
        ('ROW_COUNT','PASS',f'{n} records in charging CSV'),
        ('COLUMN_COUNT','PASS',f'{len(headers)} charging attributes'),
        ('MISSING_CELLS','PASS',f'{sum(missing.values())} missing cells (completeness only)'),
        ('HOURLY_SEQUENCE','PASS' if time_discontinuity==0 else 'FAIL',f'{time_discontinuity} nonhourly steps'),
        ('VEHICLE_CAPACITY_CONSISTENCY','FAIL',f'one vehicle ID but {len(uniques["Battery_Capacity_kWh"])} distinct battery capacities'),
        ('WEEKDAY_CONSISTENCY','FAIL',f'{weekday_mismatch}/{n} inconsistent with timestamps (Monday=0)'),
        ('ENERGY_POWER_DURATION','FAIL',f'{energy_exceeds_rate_duration}/{n} E > rate * duration/60; subject to semantics'),
        ('LOAD_RATE_BOUND','FAIL',f'{load_exceeds_charge_rate}/{n} charging load exceeds quoted charging rate; subject to semantics'),
        ('AMBIENT_HEAT_RANGE','LIMITATION',f'max temperature {max_temp:.1f} C; no >40 C observed'),
        ('SENSOR_PROVENANCE','BLOCKED','No exact equipment/sensor/protocol/measurement calibration proven'),
        ('TOPOLOGY_CONNECTIVITY','BLOCKED','31 locations but no verified real electrical network or shared transformer–EVSE circuit'),
        ('TRANSFORMER_EVSE_TEMPERATURE','BLOCKED','No oil, winding or charger internal temperature channels'),
        ('CROSS_SYSTEM_FIELD_VALIDATION','BLOCKED','No synchronized physically connected thermal field measurements'),
        ('RAW_REDISTRIBUTION_RIGHTS','OPEN','Original Kaggle license not independently verified; raw file not authorized for public GitHub redistribution'),
    ]
    with (dest/'quality_gates.csv').open('w',encoding='utf8',newline='') as o:
        w=csv.writer(o);w.writerow(['check_id','status','evidence','implication']);
        for a,b,c in checks:
            implic='Code/data integrity only' if b=='PASS' else 'Do not admit as measured coupled thermal evidence'
            w.writerow([a,b,c,implic])
    with (dest/'dataset_register.csv').open('w',encoding='utf8',newline='') as o:
        w=csv.writer(o);w.writerow(['source_id','uploaded_archive_sha256','member','records','source_candidate','evidence_tier','admission','allowed_use','excluded_use','public_raw_redistribution','drive_original_url'])
        for name,rows,allowed in [
           ('ev_charging_dataset.csv',n,'SYNTHETIC_OR_UNVERIFIED_ALGORITHM_TESTS_ONLY'),
           ('location_dataset.csv',len(locations),'ABSTRACT_ROUTING_GRAPH_DESIGN_ONLY')]:
            w.writerow(['KAGGLE_EV_CHARGING_ROUTING_CANDIDATE',sha_zip,name,rows,result['source_candidate'],'UNVERIFIED_PROVENANCE','QUARANTINE',allowed,'NO_FIELD_THERMAL_MODEL_VALIDATION','NOT_VERIFIED',drive_url])
    with (dest/'variable_dictionary.csv').open('w',encoding='utf8',newline='') as o:
        w=csv.writer(o);w.writerow(['dataset','column','source_unit_or_meaning','measurement_status','research_note'])
        for col in headers:
            unit=(col.split('_')[-1] if ('_' in col) else 'not stated')
            w.writerow(['ev_charging_dataset.csv',col,unit,'NOT_SENSOR_VERIFIED',('NOT_COMPONENT_TEMPERATURE' if col=='Temperature_C' else 'No sensor provenance')])
        for col in ['S#','Location','Type','Coordinates']:
            w.writerow(['location_dataset.csv',col,'abstract network field','NOT_PHYSICAL_SITE_VERIFIED','No documented electrical edge list or coordinate reference system'])
    return result

if __name__=='__main__':
    p=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/archive.zip')
    out=Path(sys.argv[2] if len(sys.argv)>2 else '/mnt/data/EV_Archive_Qualification_2026_11_03')
    report=audit(p,out,sys.argv[3] if len(sys.argv)>3 else '')
    print(json.dumps({k:report[k] for k in ['charging_rows','location_rows','unique_key_counts','weekday_mismatches_monday_0','charging_energy_exceeds_nominal_rate_x_duration','charging_load_exceeds_charging_rate','temperature_max_C']},indent=2))
