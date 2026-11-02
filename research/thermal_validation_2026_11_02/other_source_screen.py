#!/usr/bin/env python3
"""Read-only inventory of secondary data without inferring same-site connectivity."""
import json,zipfile,hashlib,sys
from pathlib import Path
from xml.etree import ElementTree as ET

def run(data,root):
 data=Path(data);out=Path(root)/'01_provenance';names=['Reduced Turkish Power System.xlsx','DCs and Cities.xlsx','Counties.xlsx']; info=[]
 for f in names:
  p=data/f
  if not p.is_file():info.append({'file':f,'status':'not_local'});continue
  try:
   with zipfile.ZipFile(p) as z:
    workbook=ET.fromstring(z.read('xl/workbook.xml'))
    ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    names=[s.get('name') for s in workbook.findall(ns+'sheets/'+ns+'sheet')]
    info.append({'file':f,'status':'workbook_structure_verified','sheets':names,'note':'Network benchmark only; no verified transformer-to-EVSE site connectivity'})
  except Exception as e:info.append({'file':f,'status':'cannot_inspect','error':str(e)})
 p=data/'power_grid_transport_resilience_dataset.csv'
 if p.is_file():
  with p.open(errors='replace') as fp:head=fp.readline().strip().split(',');count=sum(1 for _ in fp)
  info.append({'file':p.name,'status':'excluded_from_thermal_field_validation','rows':count,'columns':head})
 p=data/'doi_10_5061_dryad_np5hqc04z__v20260204.zip'
 info.append({'file':p.name,'status':'original_zip_not_accessible_locally' if not p.exists() else 'zip_locally_present; not independently qualified',
  'source':'https://doi.org/10.5061/dryad.np5hqc04z','warning':'UrbanEV published energy is computed from duration and charger rating, not direct thermal or matched transformer measurements'})
 (out/'secondary_sources.json').write_text(json.dumps(info,indent=2));return info
if __name__=='__main__':run(sys.argv[1],sys.argv[2])
