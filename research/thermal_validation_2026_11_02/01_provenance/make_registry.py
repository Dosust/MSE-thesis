#!/usr/bin/env python3
"""Source-asset inventory; SHA256 original bytes; never modify source data."""
import argparse,csv,hashlib,json,os
from pathlib import Path

SOURCES=[
 ('Barug2025_sensordata.csv','SINTEF measured 40MVA transformer 2024','https://doi.org/10.5281/zenodo.17223516','measured original','5d81840a2f901f04fded98c3e1097b6e'),
 ('Barug2025_calculated.csv','SINTEF calculated 40MVA transformer temperatures','https://doi.org/10.5281/zenodo.17223516','publisher model output; NOT independent truth','a84bf4facad907bae75819c149d0f109'),
 ('doi-10.48804-8kpdtw.zip','KU Leuven BEV Energy Dynamics','https://doi.org/10.48804/8KPDTW','measured vehicle records; nested archive',None),
 ('Measurement_data.xlsx','EPFL two-connector charging measurements','https://github.com/DESL-EPFL/Level-3-EV-charging-dataset','measured station power; boundary not established',None),
 ('Session_data.xlsx','EPFL CCS session summary','https://github.com/DESL-EPFL/Level-3-EV-charging-dataset','measured/publisher session summary',None),
 ('doi_10_5061_dryad_np5hqc04z__v20260204.zip','UrbanEV','https://doi.org/10.5061/dryad.np5hqc04z','real occupancy and estimated energy; not metered thermal data',None),
 ('Data.rar','Turkish power system reference archive',None,'network benchmark; not measured coupled topology',None),
 ('Reduced Turkish Power System.xlsx','Turkish benchmark network',None,'network benchmark; not field-connected to an EVSE',None),
 ('DCs and Cities.xlsx','Turkish network/city candidate reference',None,'geography/network benchmark',None),
 ('Counties.xlsx','Turkish counties candidate reference',None,'geographic context',None),
 ('power_grid_transport_resilience_dataset.csv','Unqualified resilience table',None,'not admitted as thermal observations',None),
 ('17223516.json','SINTEF source catalogue metadata','https://doi.org/10.5281/zenodo.17223516','source metadata',None),
]
def filehash(path,name):
 h=hashlib.new(name)
 with path.open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()

def run(data,out):
 data,out=Path(data),Path(out);out.mkdir(parents=True,exist_ok=True)
 rows=[]
 for name,source,url,kind,md5 in SOURCES:
  p=data/name
  d={'asset':name,'file_present':p.is_file(),'size_bytes':p.stat().st_size if p.is_file() else None,
     'sha256':filehash(p,'sha256') if p.is_file() else None,'source':source,'doi_or_source':url,
     'scientific_classification':kind,'publisher_md5_expected':md5,
     'publisher_md5_matches':filehash(p,'md5')==md5 if md5 and p.is_file() else None}
  rows.append(d)
 with (out/'source_registry.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (out/'source_registry.json').write_text(json.dumps(rows,indent=2))
 if not all(x['publisher_md5_matches'] for x in rows if x['publisher_md5_expected']):
  raise RuntimeError('SINTEF publisher checksum mismatch; STOP scientific calibration')
 return rows
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--data',required=True);a.add_argument('--out',required=True);args=a.parse_args()
 print('Registered',len(run(args.data,args.out)),'sources')
