#!/usr/bin/env python3
import csv, json, math, os, re, sys
from collections import defaultdict
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RAW = Path('/mnt/data/Q0_Raw_Provenance_Map_687_v1.csv')
TARGET = Path('/mnt/data/Pasted text(20260930-080046).txt')
OUTDIR = Path('/mnt/data')

RQ = (
    'How do time-varying physical states and interdependencies between power and transportation systems '
    'determine service degradation and recovery under extreme heat, and how can targeted operational '
    'interventions reduce the resulting coupled service deficits?'
)

WEB_SEEDS = [
    {
        'Title':'Spatial and temporal modelling of coupled power and transportation systems: A comprehensive review',
        'Year':2021,'DOI':'10.1049/enc2.12034','Authors':'Sun, Y.; Zhao, P.; Wang, L.; Malik, S.M.',
        'Source':'Energy Conversion and Economics','Document_Type':'Review','Database':'Fresh web verification',
        'Abstract':('Reviews power-grid and transportation-network models across spatial and temporal scales, '
                    'classifies coupled power-traffic network applications into long-, mid-, and short-term horizons, '
                    'and identifies uncertainty, driver preference and resilience as important directions. EV spatiotemporal '
                    'behavior is the principal coupling mechanism.'),
        'Keywords':'coupled power transportation; spatial temporal; electric vehicles; review; resilience',
        'Source_URL':'https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/enc2.12034'
    },
    {
        'Title':'Electrical Vehicle Charging Services Planning and Operation with Interdependent Power Networks and Transportation Networks: A Review of the Current Scenario and Future Trends',
        'Year':2020,'DOI':'10.3390/en13133371','Authors':'Review article authors','Source':'Energies','Document_Type':'Review','Database':'Fresh web verification',
        'Abstract':('Reviews EV charging-service planning and operation in interdependent power and transportation networks, '
                    'including charging scheduling, traffic congestion, charging loads on the power grid and coupled-network challenges.'),
        'Keywords':'EV charging; interdependent power transportation; planning; operation; review',
        'Source_URL':'https://www.mdpi.com/1996-1073/13/13/3371'
    },
    {
        'Title':'Investigating state-of-the-art planning strategies for electric vehicle charging infrastructures in coupled transport and power networks: a comprehensive review',
        'Year':2024,'DOI':'10.1088/2516-1083/ad6be1','Authors':'Li, J.; Chew, A.; Wang, H.','Source':'Progress in Energy','Document_Type':'Review','Database':'Fresh web verification',
        'Abstract':('Comprehensive review of planning strategies for EV charging infrastructure in coupled transport and power networks, '
                    'covering network representation, charging-station planning, coupled constraints and research directions.'),
        'Keywords':'EV charging infrastructure; coupled transport power; planning; review',
        'Source_URL':'https://doi.org/10.1088/2516-1083/ad6be1'
    },
    {
        'Title':'Tri-level collaborative optimization strategy for coupled power and transportation networks considering energy scheduling of fast charging stations',
        'Year':2025,'DOI':'10.1016/j.apenergy.2025.126806','Authors':'','Source':'Applied Energy','Document_Type':'Article','Database':'Fresh web verification',
        'Abstract':('Proposes a tri-level collaborative optimization model for coupled transportation and power distribution networks. '
                    'The upper level optimizes EV charging-station selection and routing with temperature effects and queue waiting time; '
                    'the middle level schedules fast-charging-station energy and prices; the lower level solves AC optimal power flow. '
                    'Real-world road-network cases are used for evaluation.'),
        'Keywords':'coupled power transportation; fast charging station; temperature; queue; ACOPF; routing; optimization',
        'Source_URL':'https://www.sciencedirect.com/science/article/pii/S0306261925015363'
    },
    {
        'Title':'Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers',
        'Year':2026,'DOI':'10.1016/j.ress.2025.112005','Authors':'Wang, S.; Lu, Q.-C.; Liu, L.; Xu, P.-C.; Wang, R.; Zhang, L.',
        'Source':'Reliability Engineering & System Safety','Document_Type':'Article','Database':'Fresh web verification',
        'Abstract':('Develops a supply-demand-based interdependency model for coupled power and transportation networks with heterogeneous EV-driver risk perceptions. '
                    'The Guizhou earthquake case shows interdependency changes with disaster severity and charging decisions; partially failed fast-charging stations can become highly interdependent.'),
        'Keywords':'interdependency; power transportation; EV charging decisions; supply demand; V2G; dynamic disaster',
        'Source_URL':'https://www.sciencedirect.com/science/article/pii/S0951832025012049'
    },
    {
        'Title':'Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar',
        'Year':2026,'DOI':'10.1016/j.ecmx.2026.101960','Authors':'Krama, A.; Kamal, N.; Sezer, N.; Bayhan, S.',
        'Source':'Energy Conversion and Management: X','Document_Type':'Article','Database':'Fresh web verification',
        'Abstract':('Field experiments on a commercial 50 kW air-cooled DC fast charger under 15-55 C ambient conditions show severe thermal derating. '
                    'Rectifier temperature explains more than 96 percent of offered-power variation, and charging duration nearly doubles under peak summer heat. '
                    'Data-driven thermal performance models are validated with hold-out analyses.'),
        'Keywords':'fast EV charger; extreme heat; thermal derating; rectifier temperature; field data; validation',
        'Source_URL':'https://www.sciencedirect.com/science/article/pii/S2590174526004435'
    },
    {
        'Title':'Extreme heat effects on electric vehicle energy consumption and driving range',
        'Year':2025,'DOI':'10.1016/j.apenergy.2024.125051','Authors':'','Source':'Applied Energy','Document_Type':'Article','Database':'Fresh web verification',
        'Abstract':('Uses 345,622 battery-electric-vehicle trips in Phoenix to quantify high-temperature effects on energy consumption and range. '
                    'Energy use rises by roughly 25-28 percent from 26-30 C to 46-50 C, with an estimated approximately 15 percent increase in aggregate charging demand for a hypothetical 500,000-BEV fleet on the hottest days.'),
        'Keywords':'extreme heat; electric vehicle; energy consumption; charging demand; Phoenix; empirical data',
        'Source_URL':'https://www.sciencedirect.com/science/article/abs/pii/S0306261924024358'
    },
]

PSTRONG=[r'\bpower\b',r'power system',r'power grid',r'power distribution',r'distribution network',r'distribution system',r'electric grid',r'electricity system',r'microgrid',r'transmission network',r'transmission line',r'transformer',r'power network',r'power flow',r'electric power',r'power infrastructure']
TSTRONG=[r'transportation',r'traffic',r'road network',r'road infrastructure',r'mobility',r'electric vehicle',r'\bEV\b',r'\bEVs\b',r'charging station',r'charging infrastructure',r'electric bus',r'fleet',r'rail',r'route',r'routing',r'transport infrastructure']
CSTRONG=[r'coupled',r'interdepend',r'power[-– ]transport',r'transportation[-– ]power',r'traffic[-– ]power',r'nexus',r'cross[- ]network',r'vehicle[- ]to[- ]grid',r'\bV2G\b',r'\bG2V\b',r'charging demand',r'charging station',r'interface',r'co[- ]optim']
HSTRONG=[r'extreme heat',r'heatwave',r'heat wave',r'high temperature',r'thermal',r'ambient temperature',r'derat',r'hottest[- ]spot',r'ampacity',r'overheat',r'heat transfer',r'urban heat',r'extreme climatic']
HEAT_TARGET=[r'extreme heat',r'heatwave',r'heat wave',r'high temperature',r'hot climate',r'extreme temperature',r'extreme climatic',r'thermal derat',r'ambient temperature',r'hottest[- ]spot',r'ampacity',r'pavement temperature',r'rail.*heat',r'climate warming',r'rising air temperature']
RSTRONG=[r'resilien',r'recovery',r'restoration',r'vulnerab',r'outage',r'service loss',r'unserved',r'cascad',r'functionality',r'performance loss',r'load shedding',r'load restoration',r'ridership']
DSTRONG=[r'dynamic',r'time[- ]vary',r'spatiotemporal',r'spatial[- ]temporal',r'temporal',r'state[- ]dependent',r'multi[- ]period',r'real[- ]time',r'rolling horizon',r'trajectory',r'time-dependent',r'evolution']
USTRONG=[r'control',r'optim',r'schedul',r'dispatch',r'routing',r'reconfigur',r'demand response',r'managed charging',r'\bV2G\b',r'resource allocation',r'policy',r'intervention']
MSTRONG=[r'power flow',r'traffic assignment',r'\bODE\b',r'\bDAE\b',r'differential',r'thermal model',r'energy balance',r'\bMILP\b',r'mixed[- ]integer',r'stochastic',r'Monte Carlo',r'Bayesian',r'Markov',r'graph',r'optimization',r'reinforcement learning',r'Fokker[- ]Planck',r'agent[- ]based',r'co-simulation',r'ACOPF']
VSTRONG=[r'case study',r'simulation',r'validated',r'validation',r'empirical',r'field',r'experiment',r'real[- ]world',r'IEEE \d+',r'data',r'measure',r'numerical experiment']
ASSET=[r'transformer',r'charger',r'charging station',r'battery',r'conductor',r'feeder',r'pavement',r'rail',r'generator',r'electric vehicle',r'EV',r'thermal']
STATE=[r'physical state',r'state[- ]dependent',r'\bstate\b',r'SOC',r'state of charge',r'temperature',r'capacity',r'loading',r'queue',r'voltage',r'flow']
SERVICE=[r'electricity service',r'mobility service',r'service',r'unserved',r'load shedding',r'load restoration',r'outage',r'recovery',r'restoration',r'travel time',r'ridership',r'charging availability',r'resilien']


def anyp(text,pats): return any(re.search(p,text,re.I) for p in pats)
def countp(text,pats): return sum(bool(re.search(p,text,re.I)) for p in pats)
def normdoi(x):
    x=str(x or '').strip().lower()
    x=re.sub(r'^https?://(dx\.)?doi\.org/','',x)
    return x

def combine_records():
    raw=pd.read_csv(RAW)
    for c in ['Title','Abstract','Keywords','Authors','Source','Document_Type','Master_Databases','DOI','Database']:
        raw[c]=raw[c].fillna('').astype(str)
    raw['text_len']=raw['Abstract'].str.len()+raw['Keywords'].str.len()
    canon=raw.sort_values(['Master_ID','text_len'],ascending=[True,False]).groupby('Master_ID',as_index=False).first()
    canon['provenance']='Q0_687_database_corpus'
    canon['Source_URL']=np.where(canon['DOI'].str.len()>0,'https://doi.org/'+canon['DOI'].str.lower(),'')

    targ=pd.read_csv(TARGET,sep='\t')
    tr=pd.DataFrame({
        'Master_ID':['TGT-%03d'%i for i in range(1,len(targ)+1)],
        'Title':targ['title'].fillna(''),'Year':targ['year'].fillna(''),'DOI':targ['doi'].fillna(''),
        'Authors':targ['authors'].fillna(''),'Source':'Targeted heat-resilience audit','Document_Type':'Article/Review',
        'Abstract':targ['thermal_role'].fillna('')+' '+targ['math_method'].fillna('')+' '+targ['main_finding'].fillna(''),
        'Keywords':targ['system'].fillna('')+'; '+targ['hazard'].fillna('')+'; '+targ['thermal_level'].fillna(''),
        'Master_Databases':'Targeted audit','Cluster_Size':1,'Match_Basis':'TARGETED_AUDIT','Database':'Targeted audit',
        'provenance':'targeted_heat_resilience_audit','Source_URL':np.where(targ['doi'].fillna('').str.len()>0,'https://doi.org/'+targ['doi'].fillna('').str.lower(),'')
    })
    web=pd.DataFrame(WEB_SEEDS)
    web['Master_ID']=['WEB-%03d'%i for i in range(1,len(web)+1)]
    web['Master_Databases']='Fresh web verification'; web['Cluster_Size']=1; web['Match_Basis']='WEB_SEED'; web['provenance']='fresh_web_seed'

    cols=sorted(set(canon.columns)|set(tr.columns)|set(web.columns))
    for d in (canon,tr,web):
        for c in cols:
            if c not in d: d[c]=''
    allr=pd.concat([canon[cols],tr[cols],web[cols]],ignore_index=True)
    allr['DOI']=allr['DOI'].fillna('').astype(str)
    allr['Title']=allr['Title'].fillna('').astype(str)
    allr['Abstract']=allr['Abstract'].fillna('').astype(str)
    allr['Keywords']=allr['Keywords'].fillna('').astype(str)
    allr['doi_norm']=allr['DOI'].map(normdoi)
    allr['title_norm']=allr['Title'].str.lower().str.replace(r'[^a-z0-9]+',' ',regex=True).str.strip()
    allr['dedup_key']=np.where(allr['doi_norm'].str.len()>5,'doi:'+allr['doi_norm'],'title:'+allr['title_norm'])
    allr['info_len']=allr['Abstract'].str.len()+allr['Keywords'].str.len()
    allr=allr.sort_values(['info_len'],ascending=False).drop_duplicates('dedup_key',keep='first').reset_index(drop=True)
    return raw, allr

def add_flags(df):
    d=df.copy()
    d['fulltext']=d['Title']+' '+d['Abstract']+' '+d['Keywords']
    patterns={'P':PSTRONG,'T':TSTRONG,'C':CSTRONG,'H':HSTRONG,'R':RSTRONG,'D':DSTRONG,'U':USTRONG,'M':MSTRONG,'V':VSTRONG}
    for k,pats in patterns.items():
        d['n'+k]=d['fulltext'].map(lambda x:countp(x,pats))
        d['f'+k]=d['n'+k]>0
    d['directPT']=d.fP & d.fT & d.fC
    d['heatTitle']=d['Title'].map(lambda x:anyp(x,HEAT_TARGET))
    d['heatContextCount']=(d['Abstract']+' '+d['Keywords']).map(lambda x:countp(x,HEAT_TARGET))
    d['heatTarget']=(d['heatTitle'] | (d['heatContextCount']>=2)) & (d.fP | d.fT)
    d['heatMech']=d['heatTarget']
    d['dynamicInfra']=d.fC & d.fR & d.fD
    d['serviceControl']=d.fR & d.fU & (d.fP | d.fT)
    d['eligible_broad']=d.directPT | d.heatMech | d.dynamicInfra | d.serviceControl | ((d.fP & d.fT)&(d.fR|d.fD)) | ((d.fH & d.fD)&(d.fP|d.fT))
    return d

def select_200(d):
    q=('time varying physical states interdependencies power transportation service degradation recovery extreme heat '
       'targeted operational interventions coupled service deficits electric vehicle charging transformer thermal state '
       'dynamic interface capability resilience mobility electricity service')
    vec=TfidfVectorizer(stop_words='english',ngram_range=(1,2),min_df=1,max_df=.95)
    X=vec.fit_transform([q]+d['fulltext'].tolist())
    d=d.copy(); d['rq_similarity']=cosine_similarity(X[0:1],X[1:]).ravel()
    d['pre_score']=(30*d.rq_similarity+18*d.directPT.astype(int)+13*d.heatMech.astype(int)+10*d.dynamicInfra.astype(int)+6*d.serviceControl.astype(int)+3*np.minimum(d.nD,2)+3*np.minimum(d.nR,2)+2*np.minimum(d.nM,2)+2*np.minimum(d.nV,2))
    e=d[d.eligible_broad].sort_values(['pre_score','rq_similarity'],ascending=False).copy()
    # Remove proceedings/whole-conference records; individual conference papers remain eligible.
    proceedings=(e['Document_Type'].str.contains('conference review|proceedings',case=False,na=False) |
                 e['Title'].str.match(r'^20\d{2} .*Conference',case=False,na=False))
    e=e[~proceedings].copy()
    # Guarantee that the targeted heat audit and fresh web-verified comparators are actually screened.
    forced=e[e['provenance'].isin(['targeted_heat_resilience_audit','fresh_web_seed'])].copy()
    rest=e[~e['dedup_key'].isin(set(forced['dedup_key']))].copy()
    if len(forced)>200: forced=forced.head(200)
    out=pd.concat([forced,rest.head(200-len(forced))],ignore_index=True)
    if len(out)<200: raise RuntimeError(f'Only {len(out)} eligible papers after exclusions; need 200')
    return out.sort_values(['pre_score','rq_similarity'],ascending=False).reset_index(drop=True)

def dims(row):
    text=row['fulltext']
    if row.directPT: scope=5.0
    elif row.fP and row.fT: scope=4.2
    elif row.heatMech: scope=3.8
    elif row.dynamicInfra: scope=3.3
    elif row.fP or row.fT: scope=2.5
    else: scope=1.0
    ac=countp(text,ASSET); hc=int(row.nH)
    if row.heatMech and ac>=2 and hc>=2: physics=5.0
    elif row.heatMech and ac>=1: physics=4.3
    elif row.fH and ac>=1: physics=3.5
    elif ac>=3 and anyp(text,[r'physical',r'capacity',r'failure',r'degradation']): physics=2.8
    else: physics=1.2 if ac else .5
    sc=countp(text,STATE); dyn=int(row.nD)
    state_time=min(5.0,.8*min(sc,4)+.9*min(dyn,3))
    if anyp(text,[r'time[- ]vary',r'state[- ]dependent',r'trajectory',r'rolling horizon',r'real[- ]time']): state_time=min(5,state_time+.6)
    c=int(row.nC); coupling=min(5.0,1.1*min(c,4)+(0.6 if row.directPT else 0))
    if anyp(text,[r'bidirectional',r'supply[- ]demand',r'interface']): coupling=min(5,coupling+.5)
    qc=countp(text,SERVICE); service=min(5.0,.9*min(qc,4)+.5*min(int(row.nR),3))
    if anyp(text,[r'trajectory',r'duration',r'recovery time',r'whole[- ]of[- ]event',r'unserved energy',r'load restored']): service=min(5,service+.6)
    intervention=min(5.0,1.0*min(int(row.nU),5))
    method=min(5.0,.8*min(int(row.nM),5)+(.5 if anyp(text,[r'optimization|simulation|model|framework']) else 0))
    evidence=0.0
    if str(row.DOI).strip(): evidence+=1.0
    if len(str(row.Abstract))>=500: evidence+=1.0
    evidence+=min(2.0,.7*min(int(row.nV),3))
    if ';' in str(row.Master_Databases) or row.provenance in {'targeted_heat_resilience_audit','fresh_web_seed'}: evidence+=.7
    evidence=min(5,evidence)
    return pd.Series({'scope5':scope,'physics5':physics,'state_time5':state_time,'coupling5':coupling,'service5':service,'intervention5':intervention,'method5':method,'evidence5':evidence})

def score_200(d):
    dd=pd.concat([d.reset_index(drop=True),d.apply(dims,axis=1).reset_index(drop=True)],axis=1)
    W={'scope5':18,'physics5':16,'state_time5':14,'coupling5':14,'service5':14,'intervention5':8,'method5':8,'evidence5':8}
    dd['rigor_score']=sum(dd[k]*(w/5) for k,w in W.items())
    dd['coverage_dims']=sum((dd[k]>=3).astype(int) for k in W)
    dd['framework_review']=dd['Document_Type'].str.contains('review',case=False,na=False)|dd['Title'].str.contains('review',case=False,na=False)
    dd['transfer_dynamic']=dd.dynamicInfra & (~dd.directPT)
    return dd

def choose_26(d):
    d=d.copy()
    # Role-specific screening prevents one mature sub-literature from crowding out the evidence chain.
    is_review=(d['Document_Type'].str.contains('review',case=False,na=False) |
               d['Title'].str.contains('review',case=False,na=False))
    pt_title=d['Title'].str.contains(r'power.*(?:transport|traffic)|(?:transport|traffic).*power',case=False,regex=True,na=False)
    ev_title=d['Title'].str.contains(r'electric vehicle|EV|charging',case=False,regex=True,na=False)
    d['framework_specific']=is_review & (pt_title | (d.directPT & ev_title))
    temp_context=(d['Title'].str.contains(r'cold climate|cold-weather|temperature|thermal',case=False,regex=True,na=False) |
                  d['Abstract'].str.contains(r'temperature effects|cold climate|cold-weather|thermal',case=False,regex=True,na=False))
    d['closest_temp']=d.directPT & (~d.heatTarget) & temp_context

    # Role-specific evidence scores. All terms are 0-5 from the same rubric.
    verified=(d.provenance=='fresh_web_seed').astype(int)
    targeted=(d.provenance=='targeted_heat_resilience_audit').astype(int)
    d['role_review']=20*d.scope5+20*d.coupling5+15*d.state_time5+15*d.method5+15*d.evidence5+15*d.service5+45*verified
    d['role_heat']=28*d.physics5+18*d.evidence5+16*d.state_time5+12*d.service5+12*d.method5+8*d.scope5+6*d.coupling5+35*verified+15*targeted
    d['role_core']=22*d.coupling5+20*d.state_time5+18*d.service5+14*d.scope5+12*d.method5+8*d.evidence5+6*d.intervention5+35*verified
    d['role_temp']=22*d.physics5+20*d.scope5+18*d.state_time5+15*d.coupling5+15*d.method5+10*d.evidence5+40*verified
    d['role_service']=26*d.service5+24*d.intervention5+14*d.state_time5+12*d.scope5+10*d.coupling5+8*d.method5+6*d.evidence5
    d['role_transfer']=24*d.state_time5+22*d.coupling5+20*d.service5+14*d.method5+12*d.evidence5+8*d.scope5

    selected=[]; selected_keys=set()

    # Expert anchor comparators: these papers are kept because they sit directly on the
    # framework/method boundary of the thesis.  The anchors do NOT mean they support a
    # novelty claim; they ensure the screen learns from the closest existing methods.
    anchor_roles={
        '10.1049/enc2.12034':'FRAMEWORK_REVIEW',
        '10.1016/j.ress.2025.112005':'CORE_PT_DYNAMIC',
        '10.1016/j.apenergy.2025.126806':'CLOSEST_TEMP_PT',
        '10.1016/j.ecmx.2026.101960':'HEAT_PHYSICS',
        '10.1016/j.apenergy.2024.125051':'HEAT_PHYSICS',
    }

    def add_anchor(doi,role,scorecol):
        pool=d[d['DOI'].str.lower().eq(doi.lower())]
        if pool.empty:
            raise RuntimeError(f'Mandatory anchor missing from 200-paper screen: {doi}')
        row=pool.iloc[0]
        key=row['dedup_key']
        if key not in selected_keys:
            rec=row.to_dict(); rec['evidence_role']=role; rec['role_score']=float(row[scorecol]); rec['anchor_comparator']=True
            selected.append(rec); selected_keys.add(key)

    role_scorecol={
        'FRAMEWORK_REVIEW':'role_review','HEAT_PHYSICS':'role_heat','CLOSEST_TEMP_PT':'role_temp',
        'CORE_PT_DYNAMIC':'role_core','SERVICE_CONTROL':'role_service','TRANSFER_DYNAMIC':'role_transfer'
    }
    for doi,role in anchor_roles.items():
        add_anchor(doi,role,role_scorecol[role])

    def take(role,n_total,mask,scorecol):
        already=sum(1 for r in selected if r.get('evidence_role')==role)
        need=max(0,n_total-already)
        if need==0:
            return
        pool=d[mask].sort_values([scorecol,'rigor_score','coverage_dims'],ascending=False)
        got=0
        for _,row in pool.iterrows():
            key=row['dedup_key']
            if key in selected_keys:
                continue
            rec=row.to_dict(); rec['evidence_role']=role; rec['role_score']=float(row[scorecol]); rec['anchor_comparator']=False
            selected.append(rec); selected_keys.add(key); got+=1
            if got>=need:
                break
        if got<need:
            raise RuntimeError(f'Could only select {got}/{need} remaining papers for {role}')

    # Evidence architecture tied directly to the guiding RQ.
    take('FRAMEWORK_REVIEW',3,d.framework_specific,'role_review')
    take('HEAT_PHYSICS',8,d.heatTarget,'role_heat')
    take('CLOSEST_TEMP_PT',2,d.closest_temp,'role_temp')
    take('CORE_PT_DYNAMIC',8,d.directPT & (d.fD|d.fR) & (~d.framework_specific) & (~d.heatTarget) & (~d.closest_temp),'role_core')
    take('SERVICE_CONTROL',3,d.directPT & d.serviceControl & (~d.framework_specific) & (~d.heatTarget),'role_service')
    take('TRANSFER_DYNAMIC',2,d.dynamicInfra & (~d.directPT),'role_transfer')

    out=pd.DataFrame(selected)
    out=out.sort_values(['rigor_score','coverage_dims'],ascending=False).reset_index(drop=True)
    out['priority_rank']=np.arange(1,len(out)+1)
    return out

def extract_sentence(text,keywords):
    sents=re.split(r'(?<=[.!?])\s+',str(text).strip())
    cand=[s for s in sents if any(k.lower() in s.lower() for k in keywords)]
    return (cand[0] if cand else (sents[0] if sents else ''))[:700]

def enrich_top26(d):
    d=d.copy()
    frameworks=[]; methods=[]; findings=[]; limitations=[]; validations=[]; relevance=[]; improvements=[]
    for _,r in d.iterrows():
        a=str(r.Abstract)
        frameworks.append(extract_sentence(a,['framework','model','approach','network','interdepend','coupl']))
        methods.append(extract_sentence(a,['method','optimization','simulation','monte carlo','traffic assignment','power flow','thermal','model']))
        findings.append(extract_sentence(a,['result','find','show','demonstrat','indicat','reveal','found']))
        lim=extract_sentence(a,['limitation','however','future','not consider','neglect','simplif','challenge'])
        if not any(k in a.lower() for k in ['limitation','however','future','not consider','neglect','simplif','challenge']):
            lim='Not explicit in abstract/metadata — requires full-text review; no inferred limitation is treated as author-stated.'
        limitations.append(lim)
        val=extract_sentence(a,['validated','validation','case study','simulation','experiment','field','data','numerical'])
        validations.append(val)
        if r.heatMech and r.directPT:
            rel='Closest comparator: heat/temperature plus P–T coupling. Inspect whether physical interface capability is an explicit dynamic state and whether coupled service trajectories are evaluated.'
        elif r.heatMech:
            rel='Mechanism-transfer evidence for heat-driven physical states or service effects; candidate physics module for the coupled P–T model.'
        elif r.directPT:
            rel='Core P–T baseline for coupling, dynamics, resilience or intervention; candidate method to adopt/modify rather than reinvent.'
        elif r.dynamicInfra:
            rel='Transferable dynamic-interdependency/recovery method outside the exact P–T heat setting.'
        else:
            rel='Contextual method evidence relevant to the thesis chain.'
        relevance.append(rel)
        if r.directPT and not r.fH:
            imp='Test whether adding heat-dependent physical state/interface capability changes predicted service deficit or intervention choice.'
        elif r.heatMech and not r.directPT:
            imp='Embed the verified heat mechanism into a coupled P–T resilience baseline and test cross-system service consequences.'
        elif r.heatMech and r.directPT:
            imp='Use as a closest benchmark; improvement must be narrower than “temperature + P–T” and should target dynamic physical interface capability/service resilience.'
        else:
            imp='Adopt the method only if it resolves a limitation directly linked to the guiding RQ; compare against its original baseline.'
        improvements.append(imp)
    d['framework_extract']=frameworks; d['method_extract']=methods; d['finding_extract']=findings; d['limitation_status']=limitations; d['validation_extract']=validations; d['relevance_to_thesis']=relevance; d['candidate_improvement']=improvements
    return d

def save_outputs(raw,unique,screened,top):
    audit_cols=['Master_ID','Title','Year','DOI','Authors','Source','Document_Type','Database','Master_Databases','provenance','Source_URL','rq_similarity','pre_score','directPT','heatTarget','heatMech','dynamicInfra','serviceControl','fP','fT','fC','fH','fR','fD','fU','fM','fV','scope5','physics5','state_time5','coupling5','service5','intervention5','method5','evidence5','rigor_score','coverage_dims']
    screened[audit_cols].to_csv(OUTDIR/'PT_200_screened.csv',index=False)
    top_cols=['priority_rank','evidence_role','Title','Year','DOI','Authors','Source','Document_Type','provenance','Source_URL','rigor_score','coverage_dims','scope5','physics5','state_time5','coupling5','service5','intervention5','method5','evidence5','framework_extract','method_extract','finding_extract','limitation_status','validation_extract','relevance_to_thesis','candidate_improvement']
    top[top_cols].to_csv(OUTDIR/'PT_26_high_rigor.csv',index=False)
    # JS input only needs the 200 records and fields used in final scoring/selection
    recs=[]
    for _,r in screened.iterrows():
        rec={k:(None if pd.isna(v) else v) for k,v in r.to_dict().items() if k not in {'fulltext'}}
        rec['Abstract']=str(r.Abstract); rec['Keywords']=str(r.Keywords); rec['Title']=str(r.Title); rec['DOI']=str(r.DOI)
        recs.append(rec)
    with open(OUTDIR/'PT_200_screening_input.json','w',encoding='utf-8') as f: json.dump(recs,f,ensure_ascii=False,indent=2)
    with open(OUTDIR/'PT_26_python.json','w',encoding='utf-8') as f: json.dump(top[['priority_rank','evidence_role','Title','Year','DOI','rigor_score']].to_dict('records'),f,ensure_ascii=False,indent=2)
    summary={
        'raw_rows':int(len(raw)),
        'unique_records_after_dedup':int(len(unique)),
        'screened_records':int(len(screened)),
        'selected_fulltext_priority':int(len(top)),
        'role_counts':top['evidence_role'].value_counts().to_dict(),
        'provenance_counts_200':screened['provenance'].value_counts().to_dict(),
        'provenance_counts_26':top['provenance'].value_counts().to_dict(),
    }
    with open(OUTDIR/'PT_screening_summary.json','w') as f: json.dump(summary,f,indent=2)
    return summary

def main():
    raw,unique=combine_records()
    flagged=add_flags(unique)
    screened=select_200(flagged)
    scored=score_200(screened)
    top=choose_26(scored)
    top=enrich_top26(top)
    summary=save_outputs(raw,unique,scored,top)
    print(json.dumps(summary,indent=2))
    print('\nTOP 26')
    for _,r in top.iterrows():
        print(f"{int(r.priority_rank):02d}. [{r.evidence_role}] {r.Title} ({r.Year}) — {r.rigor_score:.1f}")

if __name__=='__main__': main()