# Literature and Evidence Map — Bounded 207-Corpus Recall

This file records literature anchors that are explicitly present in the local 207-paper corpus or directly supplied in this chat. It is **not** a globally complete literature review.

## Chain I — Physical system / interdependencies / representation

### Rinaldi, Peerenboom & Kelly (2001)
**Title:** *Identifying, understanding, and analyzing critical infrastructure interdependencies*  
**DOI:** `10.1109/37.969131`  
**Role:** foundational infrastructure-interdependency taxonomy and conceptual structure.  
**Status:** `SUPPORTED_IN_207`.

### Ouyang (2014)
**Title:** *Review on modeling and simulation of interdependent critical infrastructure systems*  
**DOI:** `10.1016/j.ress.2013.06.040`  
**Role:** review of interdependent-infrastructure modeling approaches.  
**Status:** `SUPPORTED_IN_207`.

### Buldyrev et al. (2010)
**Title:** *Catastrophic cascade of failures in interdependent networks*  
**DOI:** `10.1038/nature08932`  
**Role:** dependency-driven cascades and abrupt collapse in interdependent networks.  
**Status:** `SUPPORTED_IN_207`.

### Multilayer network mathematics
The 207 corpus contains *Mathematical Formulation of Multilayer Networks*, *Multilayer networks*, and *The structure and dynamics of multilayer networks*. Some rows have incomplete author/year/DOI metadata.  
**Role:** formal network representation.  
**Status:** `SUPPORTED_IN_207_METADATA_INCOMPLETE`.

## Chain II — Identification / inverse problems / UQ

### Bayesian reconstruction of interdependent infrastructure
**Title:** *Bayesian approach for the network reconstruction of interdependent critical infrastructure systems from cascading failures*  
**DOI:** `10.1103/vswp-h4hx`  
**Year:** 2026  
**Role:** establishes that uncertain interdependent infrastructure topology can already be inferred from cascading-failure observations.  
**Status:** `SUPPORTED_IN_207`.

**Novelty guardrail:** do not claim that the thesis is first to infer hidden interdependencies. The sharper candidate problem is uncertainty propagation from interface identification into viability/recoverability geometry.

## Chain III — Hazard / failure / cascade

The 207 corpus contains multiple interdependency/cascade studies. The current memory uses hazard → damage → failure → cascade → functionality → service as an ontological chain. Generic fragility formulas discussed in chat are representative existing practice, but they should not be attributed to a specific 207 record unless that record is explicitly checked.

## Chain IV — Viability / reachability / recovery

### Mitchell, Bayen & Tomlin (2005)
**Title:** *A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games*  
**DOI:** `10.1109/TAC.2005.851439`  
**Role:** HJ/HJI reachable-set foundation.  
**Status:** `SUPPORTED_IN_207`.

### Bansal, Chen, Herbert & Tomlin (2017)
**Title:** *Hamilton-Jacobi Reachability: A Brief Overview and Recent Advances*  
**Role:** HJ reachability review.  
**Status:** `SUPPORTED_IN_207`.

### Infrastructure HJ viability precedent
**Title:** *Hamilton-Jacobi Reachability for Viability Analysis of Constrained Waste-to-Energy Systems under Adversarial Uncertainty*  
**DOI:** `10.1016/j.ejcon.2026.101501`  
**Year:** 2026  
**Role:** direct infrastructure precedent for HJ viability/reachability.  
**Status:** `SUPPORTED_IN_207`.

**Novelty guardrail:** do not claim first HJ viability application to infrastructure.

## Chain V — Control / restoration / design

The local corpus contains restoration, recovery, resilience, and design studies. Restoration optimization is treated as an established research area. A thesis contribution must therefore be sharper than “optimize restoration.” A candidate downstream extension is to optimize architecture/control with respect to viability/recoverability geometry rather than only a scalar resilience score.

## Chain VI — Sustainability / equity / decision

### Equitable resilience
**Title:** *Equitable Resilience in Infrastructure Systems: Empirical Assessment of Disparities in Service Disruptions and Recovery*  
**DOI:** `10.1061/(ASCE)NH.1527-6996.0000401`  
**Year:** 2020  
**Role:** evidence that infrastructure disruption/recovery burdens are heterogeneous and equity-aware service consequences already exist in literature.  
**Status:** `SUPPORTED_IN_207`.

### Sustainability / climate-resilience trade-offs
**Title:** *Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery*  
**Role:** sustainability/climate-resilience recovery trade-off literature.  
**Status:** `SUPPORTED_IN_207_METADATA_INCOMPLETE`.

## Evidence discipline

The 207 corpus supports the **existence** of literature on:
- infrastructure interdependencies;
- multilayer/network representation;
- cascading failures;
- Bayesian reconstruction of interdependent infrastructure structure;
- HJ reachability and infrastructure viability;
- equitable resilience;
- sustainability/climate-resilience recovery trade-offs.

The following exact mathematical forms are **thesis-integrating / candidate**, not attributed to these papers as written:

\[
m_{ij}(t),
\]

\[
K=K_{phys}\cap K_{service}\cap K_{sus}\cap K_{eq},
\]

\[
E_{inv}=d_H(\mathcal V(\theta^\star),\mathcal V(\hat\theta)),
\]

\[
S_j^{\mathcal V}=\lim_{\delta\to0}\frac{d_H[\mathcal V(\theta),\mathcal V(\theta+\delta e_j)]}{|\delta|}.
\]

## Source files used in this chat
- `High_Rigor_Thesis_Paper_Corpus_207.csv`
- `High_Rigor_Thesis_Literature_Corpus_207.xlsx`
- `High_Rigor_Thesis_Literature_Corpus_207.zip`
- `High_Rigor_Thesis_Journal_Landscape.csv`
- attached six-chain mathematical-depth note: `Pasted markdown(20260820-083427).md`

Future chats must verify exact metadata against the source file before adding author/year/DOI fields that are absent in the local row.
