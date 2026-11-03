#!/usr/bin/env python3
"""Evidence-governed DOI/repository file discovery & bounded original-data acquisition.

Run: python doe_scraper.py --out results --download-small --max-file-mb 5
Uses public metadata endpoints only; no circumvention, login automation, or fabricated physical links.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import time
from urllib.parse import urljoin, urlparse, unquote

import requests

API_BASE = 'https://openenergyhub.ornl.gov/api/explore/v2.1/catalog/datasets'
ALLOW = {'zenodo.org', 'www.zenodo.org', 'openenergyhub.ornl.gov',
         'wzy.ece.iastate.edu', 'www.dropbox.com', 'dl.dropboxusercontent.com',
         'www.energy.gov', 'energy.gov'}
RECORDS = (
    ('TU Dortmund DriVe2X', '14065331', 'LAB_MEASURED', '10.5281/zenodo.14065331'),
    ('SINTEF transformer', '17223516', 'FIELD_COMPONENT_MEASURED', '10.5281/zenodo.17223516'),
    ('KIT multi-voltage', '22826984', 'ELECTRICAL_MEASURED_TOPOLOGY_PENDING', '10.5281/zenodo.22826984'),
)
ORNLS = (
    ('DOE EV Data Collection - Charging Data', 'doe-ev-data-collection-charging-data', 'FIELD_MEASURED_BUT_SENSOR_ORIGIN_VARIES', '10.15483/1989855'),
    ('Iowa Distribution Test Systems', 'iowa-distribution-test-systems', 'REAL_TOPOLOGY_TRANSFORMER_AGGREGATED_SMART_METERS', ''),
    ('CODAS EV energy router', 'energy-router-electric-vehicle-dataset', 'CHIL_CONTROL_TESTBED_NOT_FIELD', ''),
)
FIELDS = ['source', 'evidence_class', 'doi', 'record_page', 'file_name', 'file_url',
          'reported_bytes', 'reported_checksum', 'provenance', 'kind',
          'direct_link_status', 'http_status', 'actual_bytes', 'sha256',
          'checksum_verified', 'actual_format', 'observed_columns', 'local_file',
          'note', 'connected_thermal_field_verified']
SEARCH_LOG = ['source','url','http_status','outcome','detail']


def allowed(url: str) -> bool:
    p = urlparse(url)
    host = (p.hostname or '').lower()
    return p.scheme == 'https' and host in ALLOW and not p.username and not p.password


def safe_name(value: str) -> str:
    return re.sub(r'[^A-Za-z0-9._-]+', '_', value or '')[:110].strip('._') or 'unnamed'


def classify_name(name):
    lower = (name or '').lower().split('?')[0]
    ext = Path(lower).suffix
    if ext in ('.csv', '.tsv', '.parquet', '.xlsx', '.xls', '.h5', '.mat'):
        return 'CANDIDATE_DATA_FILE'
    if ext in ('.dss', '.glm', '.dyr', '.raw'):
        return 'ELECTRICAL_TOPOLOGY_MODEL'
    if ext in ('.zip', '.tar', '.gz', '.7z'):
        return 'ARCHIVE_CONTENT_UNKNOWN'
    if ext in ('.pdf', '.doc', '.docx', '.txt'):
        return 'DOCUMENT_NOT_MEASUREMENTS'
    return 'UNKNOWN_TYPE'


class HrefParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.hrefs=[]; self.href=None; self.caption=[]
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.href = dict(attrs).get('href'); self.caption=[]
    def handle_data(self, data):
        if self.href is not None: self.caption.append(data)
    def handle_endtag(self, tag):
        if tag == 'a' and self.href:
            self.hrefs.append((self.href, ' '.join(''.join(self.caption).split())))
            self.href=None; self.caption=[]


class Scraper:
    def __init__(self, out, max_api_calls=55, delay=0.12, timeout=30):
        self.out=Path(out); self.out.mkdir(parents=True, exist_ok=True)
        self.session=requests.Session()
        self.session.headers.update({'User-Agent': 'PowerEV-Thesis-OriginalDataAudit/1.0 (scientific research; metadata only)'})
        self.max_api_calls=max_api_calls; self.calls=0; self.delay=delay; self.timeout=timeout
        self.rows=[]; self.log=[]; self._seen=set()

    def request(self, method, url, **kwargs):
        if not allowed(url): raise ValueError('Host not allowlisted: '+url)
        if self.calls >= self.max_api_calls: raise RuntimeError('REQUEST_LIMIT_REACHED')
        self.calls += 1
        if self.delay: time.sleep(self.delay)
        response=self.session.request(method,url,timeout=self.timeout,allow_redirects=False,**kwargs)
        # Redirects are not followed blindly: URLs must remain in explicit public allowlist.
        for _ in range(5):
            if response.status_code not in (301,302,303,307,308): break
            redirect=urljoin(response.url,response.headers.get('Location',''))
            response.close()
            if not allowed(redirect): raise ValueError('REDIRECT_REQUIRES_REVIEW: '+redirect)
            if self.calls >= self.max_api_calls: raise RuntimeError('REQUEST_LIMIT_REACHED')
            self.calls+=1
            response=self.session.request(method,redirect,timeout=self.timeout,allow_redirects=False,**kwargs)
        return response

    def logged_json(self, source, url):
        try:
            with self.request('GET',url) as response:
                response.raise_for_status()
                result=response.json()
                self.log.append(dict(source=source,url=url,http_status=response.status_code,outcome='JSON_OK',detail=''))
                return result
        except (Exception,) as e:
            self.log.append(dict(source=source,url=url,http_status='',outcome='ERROR',detail=str(e)[:400]))
            return None

    def logged_html(self, source, url):
        try:
            with self.request('GET',url) as response:
                response.raise_for_status()
                content=response.text
                self.log.append(dict(source=source,url=url,http_status=response.status_code,outcome='HTML_OK',detail=''))
                return content
        except Exception as e:
            self.log.append(dict(source=source,url=url,http_status='',outcome='ERROR',detail=str(e)[:400]))
            return None

    def add(self, source, evidence_class, doi, page, filename, url, size='', checksum='', origin=''):
        url=(url or '').strip();filename=(filename or '').strip()
        if not url or not allowed(url):
            self.log.append(dict(source=source,url=url,http_status='',outcome='IGNORED_UNSAFE_OR_EMPTY_URL',detail=filename))
            return
        identity=(url,filename,source)
        if identity in self._seen: return
        self._seen.add(identity)
        self.rows.append({**dict.fromkeys(FIELDS,''), 'source':source,
            'evidence_class':evidence_class,'doi':doi,'record_page':page,
            'file_name':filename,'file_url':url,'reported_bytes':size,
            'reported_checksum':checksum,'provenance':origin,
            'kind':classify_name(filename),'direct_link_status':'DISCOVERED_UNTESTED',
            'connected_thermal_field_verified':'NO'})

    def zenodo(self, name, record, evidence, doi):
        page='https://zenodo.org/records/'+record
        url='https://zenodo.org/api/records/'+record
        data=self.logged_json(name,url)
        if not isinstance(data,dict):return
        files=data.get('files',[])
        if isinstance(files,dict):files=files.get('entries',[]) or files.get('files',[]) or []
        if isinstance(files,dict):files=[{'key':k,**(v if isinstance(v,dict) else {})} for k,v in files.items()]
        if not isinstance(files,list):files=[]
        for f in files:
            if not isinstance(f,dict):continue
            key=f.get('key') or f.get('filename') or f.get('name') or ''
            links=f.get('links',{})
            link=links.get('content') or links.get('self') or links.get('download') if isinstance(links,dict) else ''
            self.add(name,evidence,doi,page,key,link,f.get('size',''),f.get('checksum',''),'Zenodo public record API file metadata')

    def ornl(self,name,slug,evidence,doi):
        page=f'https://openenergyhub.ornl.gov/explore/dataset/{slug}/'
        base=f'{API_BASE}/{slug}'
        meta=self.logged_json(name,base)
        if isinstance(meta,dict):
            # Opendatasoft attachments may be exposed in public metadata.
            self._walk_files(name,evidence,doi,page,slug,meta,'ORNL public dataset metadata')
        data=self.logged_json(name,base+'/records?limit=50')
        if isinstance(data,dict):
            for record in (data.get('results') or [])[:50]:
                self._walk_files(name,evidence,doi,page,slug,record,'ORNL Opendatasoft record')

    def _walk_files(self,name,evidence,doi,page,slug,object_,origin):
        # Only recognize actual public URLs or file ids explicitly exposed by API.
        def walk(node,key='',depth=0):
            if depth>9:return
            if isinstance(node,dict):
                possible_name=node.get('filename') or node.get('name') or node.get('file_name') or ''
                link=node.get('url') or node.get('content_url') or node.get('download_url') or ''
                if not link and isinstance(node.get('links'),dict):
                    link=node['links'].get('self') or node['links'].get('download') or ''
                file_id=node.get('id') or node.get('file_id')
                if key.lower() in ('file','files','attachment','attachments') and isinstance(file_id,str) and re.fullmatch(r'[a-f0-9]{32}',file_id):
                    link=f'{API_BASE}/{slug}/files/{file_id}'
                if isinstance(link,str) and link.startswith('https://') and (possible_name or key.lower() in ('file','files','attachment','attachments')):
                    self.add(name,evidence,doi,page,possible_name or key,link,
                             node.get('size',''),node.get('checksum',''),origin)
                for k,v in node.items():walk(v,str(k),depth+1)
            elif isinstance(node,list):
                for v in node[:100]:walk(v,key,depth+1)
            elif isinstance(node,str):
                if (node.startswith('https://') and key.lower() in ('file','files','download_url','url')):
                    self.add(name,evidence,doi,page,unquote(urlparse(node).path.rsplit('/',1)[-1]),node,origin=origin)
        walk(object_)

    def iowa(self):
        name='Iowa real distribution test systems';url='https://wzy.ece.iastate.edu/testsystem.html'
        html=self.logged_html(name,url)
        if not html:return
        p=HrefParser();p.feed(html)
        for link,description in p.hrefs:
            u=urljoin(url,link)
            if not allowed(u):continue
            # retain actual page link; do not invent Dropbox direct-download URLs
            if any(k in description.lower() for k in ('smart meter','opendss','system description','time-series','dropbox')) or re.search(r'\.(zip|xlsx?|dss|mat)(\?|$)',u,re.I):
                namepart=unquote(urlparse(u).path.rsplit('/',1)[-1])
                self.add(name,'REAL_TOPOLOGY_TRANSFORMER_AGGREGATED_SMART_METERS','',url,
                         namepart,u,origin='Linked verbatim from academic investigator webpage; '+description)

    def doe(self):
        src='DOE Power System Data Analytics gateway';url='https://www.energy.gov/oe/power-system-data-analytics'
        html=self.logged_html(src,url)
        if not html:return
        p=HrefParser();p.feed(html)
        for link,description in p.hrefs:
            u=urljoin(url,link)
            if not allowed(u):continue
            if re.search(r'\.(csv|zip|xlsx)(\?|$)',urlparse(u).path,re.I):
                fn=unquote(urlparse(u).path.rsplit('/',1)[-1]);self.add(src,'GATEWAY_ONLY','',url,fn,u,origin='DOE exact HTML hyperlink; file content unverified')
        self.log.append(dict(source=src,url=url,http_status='',outcome='GATEWAY_NOT_DATASET',detail='No public transformer–EVSE synchronized thermal files established by this overview page'))

    def discover(self):
        self.doe()
        for r in RECORDS:self.zenodo(*r)
        for o in ORNLS:self.ornl(*o)
        self.iowa()

    @staticmethod
    def signature(path):
        with open(path,'rb') as f:sample=f.read(5000)
        if sample.startswith(b'PK\x03\x04'):return 'ZIP_CONTAINER'
        if sample.startswith(b'PAR1'):return 'PARQUET'
        if sample.startswith(b'\x89HDF'):return 'HDF5'
        if sample[:100].lower().lstrip().startswith((b'<!doctype html',b'<html',b'<?xml',b'{"error"')):return 'REJECT_HTML_OR_API_ERROR'
        if b'\x00' in sample:return 'BINARY_OR_UNKNOWN'
        try:
            decoded=sample.decode('utf-8-sig')
            first=decoded.splitlines()[0] if decoded else ''
            if ',' in first or ';' in first or '\t' in first: return 'TEXT_DELIMITED'
        except UnicodeDecodeError:pass
        return 'UNKNOWN'

    def download(self,max_file_mb=5,max_files=8):
        limit=int(max_file_mb*1024*1024); folder=self.out/'original_downloads';folder.mkdir(exist_ok=True)
        # prioritize metadata-index CSVs and typed datasets before large archives/documents
        candidates=sorted(self.rows,key=lambda r:(r['kind']!='CANDIDATE_DATA_FILE',r['kind']=='ARCHIVE_CONTENT_UNKNOWN',str(r['source']),r['file_name']))
        count=0
        for r in candidates:
            if count>=max_files:break
            if r['kind'] not in ('CANDIDATE_DATA_FILE','ELECTRICAL_TOPOLOGY_MODEL','ARCHIVE_CONTENT_UNKNOWN'):continue
            if r['file_url'].startswith('https://www.dropbox.com/'):
                r['direct_link_status']='ACCESS_ROUTE_REVIEW_REQUIRED';continue
            if r['reported_bytes']:
                try:
                    if int(r['reported_bytes'])>limit:
                        r['direct_link_status']='SKIPPED_SIZE_LIMIT';continue
                except (TypeError,ValueError):pass
            tmp=folder/(safe_name(r['source'])+'__'+safe_name(r['file_name'])+'.partial')
            final=Path(str(tmp).removesuffix('.partial'))
            try:
                with self.request('GET',r['file_url'],stream=True) as response:
                    r['http_status']=response.status_code
                    response.raise_for_status()
                    ct=response.headers.get('Content-Type','').lower()
                    if 'text/html' in ct:
                        r['direct_link_status']='REJECT_HTML_NOT_ORIGINAL';continue
                    size=0;sha=hashlib.sha256();md5=hashlib.md5()
                    with tmp.open('wb') as f:
                        for chunk in response.iter_content(chunk_size=128*1024):
                            if not chunk:continue
                            size+=len(chunk)
                            if size>limit:raise ValueError('EXCEEDS_FILE_LIMIT')
                            f.write(chunk);sha.update(chunk);md5.update(chunk)
                signature=self.signature(tmp)
                if signature=='REJECT_HTML_OR_API_ERROR':raise ValueError(signature)
                r.update(actual_bytes=size,sha256=sha.hexdigest(),actual_format=signature)
                declared=(r['reported_checksum'] or '').strip().lower()
                if declared.startswith('md5:'):
                    match=md5.hexdigest()==declared[4:]
                elif declared.startswith('sha256:'):
                    match=sha.hexdigest()==declared[7:]
                else: match=None
                r['checksum_verified']='PASS' if match else ('FAIL' if match is False else 'NO_PUBLISHED_CHECKSUM')
                if match is False:raise ValueError('CHECKSUM_MISMATCH')
                if r['kind']=='CANDIDATE_DATA_FILE' and r['file_name'].lower().endswith(('.csv','.tsv')) and signature=='TEXT_DELIMITED':
                    with tmp.open('r',encoding='utf-8-sig',errors='replace',newline='') as f:
                        header=next(csv.reader(f,delimiter='\t' if r['file_name'].endswith('.tsv') else ','),[])
                    r['observed_columns']=' | '.join(header[:50])[:2000]
                tmp.rename(final)
                r['local_file']=str(final.relative_to(self.out))
                r['direct_link_status']='DOWNLOADED_ORIGINAL_VERIFIED' if match is True else 'DOWNLOADED_ORIGINAL_CHECKSUM_NOT_PUBLISHED'
                count+=1
            except Exception as e:
                r['direct_link_status']='FAILED_DOWNLOAD_OR_CHECKSUM'
                r['note']=str(e)[:240]
                self.log.append(dict(source=r['source'],url=r['file_url'],http_status=r['http_status'],outcome='DOWNLOAD_FAILURE',detail=str(e)[:250]))
            finally:
                if tmp.exists():tmp.unlink()
        return count

    def write(self):
        for fn,rows,fields in [('file_candidates.csv',self.rows,FIELDS),('http_search_log.csv',self.log,SEARCH_LOG)]:
            with (self.out/fn).open('w',newline='',encoding='utf-8') as f:
                w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
        counts={}
        for r in self.rows:counts[r['direct_link_status']]=counts.get(r['direct_link_status'],0)+1
        downloaded=[r for r in self.rows if r['direct_link_status'].startswith('DOWNLOADED')]
        summary={
            'sources_searched':len(RECORDS)+len(ORNLS)+2,
            'requests_used':self.calls,'files_discovered':len(self.rows),
            'files_downloaded':len(downloaded),'downloaded_bytes':sum(int(r['actual_bytes']) for r in downloaded),
            'status_counts':counts,
            'measured_connected_transformer_evse_thermal_field_data_verified':False,
            'interpretation':'Downloaded original data do not establish thermal coupling; topology, synchronization, and sensor provenance require separate scientific qualification.'
        }
        (self.out/'run_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
        return summary


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default='doe_scraper_output')
    parser.add_argument('--download-small',action='store_true')
    parser.add_argument('--max-file-mb',type=float,default=5)
    parser.add_argument('--max-files',type=int,default=8)
    parser.add_argument('--max-api-calls',type=int,default=70)
    args=parser.parse_args()
    if not 0.1 <= args.max_file_mb <= 50 or not 1<=args.max_files<=30:parser.error('Bounded size/count required')
    s=Scraper(args.out,max_api_calls=args.max_api_calls)
    s.discover()
    if args.download_small:s.download(args.max_file_mb,args.max_files)
    print(json.dumps(s.write(),indent=2))

if __name__=='__main__':main()
