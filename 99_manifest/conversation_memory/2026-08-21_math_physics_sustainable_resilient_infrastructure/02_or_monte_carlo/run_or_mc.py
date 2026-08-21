import numpy as np, json, time, math
names = [
"Cyber-physical multi-infrastructure digital twins",
"AI climate/Earth observation & hazard intelligence",
"Predictive maintenance / SHM digital twins",
"Safe RL / MPC for power grids",
"DRL / MPC for water & wastewater",
"Intelligent transport digital twins & control",
"Dynamic interface identification + Bayesian UQ",
"People-centric service resilience",
"Hamilton-Jacobi viability / reachability",
"Recovery coupling + GNN optimization",
"Neural operators for physics simulation",
"Physics-informed machine learning",
"Federated / causal cross-utility data integration",
"Deep-uncertainty adaptation / real options",
"Equity-aware robust infrastructure planning",
"Circular waste / Waste-to-Energy optimization",
"AI algorithm discovery / evolutionary optimization",
"Sustainable AI + data-center energy-water co-optimization",
"Multi-agent distributed infrastructure control"
]
criteria=["industrial_maturity","real_world_evidence","human_value","mathematical_rigor","formal_guarantees","AI_leverage","SDG_impact","cross_sector_relevance","data_readiness","scientific_novelty"]
mu=np.array([
[90,90,92,82,60,90,88,95,82,80],
[92,95,93,83,50,98,95,82,95,72],
[95,95,80,72,50,85,78,65,88,55],
[72,70,95,92,78,98,92,65,82,88],
[75,76,90,88,75,92,90,65,78,82],
[85,85,88,80,55,90,88,70,85,70],
[50,45,94,98,82,86,92,100,60,99],
[60,55,98,88,65,75,98,95,65,95],
[35,30,94,100,100,55,92,85,45,97],
[50,40,90,92,70,92,90,85,55,95],
[60,55,88,96,60,98,88,82,70,95],
[70,65,92,95,70,96,90,90,70,94],
[55,50,90,88,60,94,90,100,60,96],
[70,65,92,94,80,65,98,90,70,88],
[60,55,99,92,70,70,100,90,60,94],
[78,75,90,84,65,75,98,70,78,72],
[78,80,85,96,60,100,80,75,85,98],
[80,85,94,94,65,98,100,80,88,95],
[55,45,92,97,70,95,90,100,55,98]
],dtype=np.float32)
base=np.array([.12,.10,.14,.14,.10,.10,.10,.06,.05,.09],dtype=np.float64)
assert abs(base.sum()-1)<1e-9
# evidence uncertainty: larger when real-world evidence and data readiness are weak
rw=mu[:,1].astype(float); dr=mu[:,8].astype(float)
sigma=(2.0 + 4.0*(1-rw/100.0) + 2.0*(1-dr/100.0)).astype(np.float32)
N=10_000_000
chunk=200_000
conc=120.0
alpha=base*conc
rng=np.random.default_rng(57420260821)
C=len(names); K=len(criteria)
sum_s=np.zeros(C); sumsq=np.zeros(C); winner=np.zeros(C,dtype=np.int64); top3=np.zeros(C,dtype=np.int64)
# histogram for approximate exact quantiles width .05
bins=np.linspace(0,100,2001)
hist=np.zeros((C,2000),dtype=np.int64)
start=time.time()
for st in range(0,N,chunk):
    n=min(chunk,N-st)
    w=rng.dirichlet(alpha,n).astype(np.float32)
    base_scores=w @ mu.T  # n x C
    zc=rng.standard_normal((n,C),dtype=np.float32)
    zk=rng.standard_normal((n,K),dtype=np.float32)
    common=(w*zk).sum(axis=1,dtype=np.float32)
    s=base_scores + (0.65*zc + 0.35*common[:,None])*sigma[None,:]
    np.clip(s,0,100,out=s)
    sum_s += s.sum(axis=0,dtype=np.float64)
    sumsq += (s.astype(np.float64)**2).sum(axis=0)
    win=np.argmax(s,axis=1)
    winner += np.bincount(win,minlength=C)
    idx=np.argpartition(s,-3,axis=1)[:,-3:]
    top3 += np.bincount(idx.ravel(),minlength=C)
    # histogram concept by concept
    for j in range(C):
        hj,_=np.histogram(s[:,j],bins=bins)
        hist[j]+=hj
    if (st//chunk+1)%10==0:
        print(f"{st+n:,}/{N:,} elapsed {time.time()-start:.1f}s",flush=True)
mean=sum_s/N
std=np.sqrt(np.maximum(0,sumsq/N-mean**2))
q05=np.zeros(C); q50=np.zeros(C); q95=np.zeros(C)
for j in range(C):
    cs=np.cumsum(hist[j])
    for q,arr in [(0.05,q05),(0.50,q50),(0.95,q95)]:
        pos=np.searchsorted(cs,q*N)
        arr[j]=(bins[pos]+bins[pos+1])/2
# deterministic scenario scores
scenarios={
"balanced":base,
"industrial":[.24,.24,.14,.06,.03,.08,.06,.03,.08,.04],
"high_rigor":[.03,.02,.10,.25,.18,.07,.08,.10,.02,.15],
"sustainability_human":[.06,.06,.22,.10,.08,.06,.25,.07,.05,.05],
"AI_frontier":[.04,.05,.10,.17,.10,.23,.08,.07,.05,.11]
}
sc_res={}
for key,w in scenarios.items():
    w=np.array(w,float); w=w/w.sum(); sc=mu.astype(float)@w
    order=np.argsort(-sc)
    sc_res[key]=[{"rank":int(r+1),"concept":names[i],"score":float(sc[i])} for r,i in enumerate(order)]
order=np.argsort(-mean)
out={
"seed":57420260821,"N":N,"criteria":criteria,"base_weights":base.tolist(),"score_matrix":{names[i]:{criteria[k]:float(mu[i,k]) for k in range(K)} for i in range(C)},
"sigma":{names[i]:float(sigma[i]) for i in range(C)},
"results":[{"rank":int(r+1),"concept":names[i],"mean":float(mean[i]),"std":float(std[i]),"q05":float(q05[i]),"median":float(q50[i]),"q95":float(q95[i]),"p_first":float(winner[i]/N),"p_top3":float(top3[i]/N)} for r,i in enumerate(order)],
"scenario_rankings":sc_res,"elapsed_seconds":time.time()-start
}
with open('/mnt/data/or_mc10m_results.json','w') as f: json.dump(out,f,indent=2)
print(json.dumps(out['results'][:19],indent=2))
print('elapsed',out['elapsed_seconds'])
