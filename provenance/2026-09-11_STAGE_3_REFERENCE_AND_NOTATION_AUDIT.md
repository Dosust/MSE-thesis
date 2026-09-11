# Stage 3 Reference and Notation Audit — 2026-09-11

**Object audited:** [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](../project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)  
**Purpose:** preserve the reasoning used to freeze Stage 3 and prevent notation, scope, and evidence drift.

## 1. Audit result

Stage 3 was accepted as the canonical specification for **Coupled Hybrid Multiscale Dynamics**, subject to explicit scientific boundary rules.

The audit enforced the progression

$$
\{P,T,I,O\}
\rightarrow
\mathfrak I_{ij}^{\alpha\beta}
\rightarrow
\{Y(t),m(t),\mathcal G(t),T_C,v_c\}.
$$

Stage 3 is responsible for **state evolution, event evolution, dynamic topology, temporal propagation, spatial propagation where meaningful, and uncertainty in dynamic trajectories**. It does not redefine Stage-2 causal mechanisms, design the Stage-4 observer/control law, or compute Stage-5 viability objects.

## 2. Notation corrections applied before freeze

### 2.1 Preserve the canonical four-layer state

The Stage-1 state remains

$$
Y(t)=[x_P,x_T,z_I,z_O]^\top.
$$

The operating mode is not silently inserted into $Y$ and then also passed separately to the hybrid dynamics. Instead,

$$
\widetilde Y(t)=(Y(t),m(t))
$$

is the explicit Stage-3 augmented hybrid state.

This removes a double-counting ambiguity in the source draft.

### 2.2 Separate mechanism from dynamic transmission map

Stage 2 retains $M_{ij}$ as the causal mechanism in

$$
\mathfrak I_{ij}^{\alpha\beta}.
$$

Stage 3 uses

$$
\mathcal M_{ij}^{\alpha\beta}
$$

for the **dynamic transmission map induced by that mechanism**. The distinction prevents causal ontology from being conflated with its mathematical realization.

### 2.3 Avoid model/mechanism symbol collision

Coupling-ablation model variants are written

$$
\mathscr M_{PT},\quad \mathscr M_{PTI},\quad \mathscr M_{PTIO}
$$

rather than $M_{PT},M_{PTI},M_{PTIO}$, because $M_{ij}$ is already reserved for Stage-2 mechanisms.

### 2.4 Preserve the Stage-3 / Stage-4 boundary

A dispatch may appear in Stage 3 as a discrete event affecting the trajectory, but the **decision rule producing the dispatch belongs to Stage 4**. Likewise, detection/estimation/decision timestamps may appear in integrated chronology checks, while observer and policy design remain Stage-4 objects.

## 3. Evidence discipline

The Stage-3 document distinguishes three categories:

1. **Established precedent** — e.g., dynamic interdependency models, temporal networks, railway–power coupling, AoI, communication-delay co-simulation, and HELICS.
2. **Thesis synthesis** — the joint hybrid delayed multirate P–T–I–O architecture.
3. **Proposed diagnostics** — e.g., $T_C(j)$ and state-dependent $v_c$ for mechanisms where a spatial-front interpretation is physically meaningful.

No citation is treated as proof that the complete P–T–I–O architecture is novel. Novelty remains a falsifiable literature/evidence question.

## 4. Principal bibliographic checks

The following principal records were cross-checked against publisher, institutional, or authoritative indexing pages on 2026-09-11:

| Reference | Verification focus | Result |
|---|---|---|
| Bellè et al. (2022) | railway–traction–external-power interdependency; DOI `10.1016/j.ress.2021.108091` | verified |
| Cimellaro et al. (2024) | temporal-network infrastructure cascading; DOI `10.1016/j.rcns.2024.05.002` | verified |
| Danziger & Barabási (2022) | recovery coupling; DOI `10.1038/s41467-022-28379-5` | verified |
| Goldbeck et al. (2019) | dynamic network-flow resilience and repair; DOI `10.1016/j.ress.2019.03.007` | verified |
| Hardy et al. (2024) | HELICS federated multi-domain co-simulation; DOI `10.1109/ACCESS.2024.3363615` | verified |
| Li et al. (2024) | dynamic P–T interaction, departure/route choice and charging queues; DOI `10.17775/CSEEJPES.2022.04810` | verified |
| Lian et al. (2026) | flood-responsive P–T emergency-resource dispatch; DOI `10.1016/j.apenergy.2025.127004` | verified |
| Sun et al. (2021) | spatial/temporal P–T modeling review; DOI `10.1049/enc2.12034` | verified |
| Wang et al. (2021) | DER communication delay and instability risk; DOI `10.1109/PVSC43889.2021.9518779` | verified |
| Yang & Zhang (2026) | road-transport/electric-power earthquake interdependency; DOI `10.1016/j.ress.2026.112819` | verified |
| Yates et al. (2021) | Age of Information; DOI `10.1109/JSAC.2021.3065072` | verified |
| Zhang & Peeta (2014) | dynamic/disequilibrium interdependent infrastructure; DOI `10.1016/j.trb.2014.04.008` | verified |
| Zhao et al. (2016) | spatial overload-cascade propagation; DOI `10.1038/ncomms10094` | verified |

## 5. Scientific caution retained

Zhao et al. (2016) support explicit space–time cascade analysis for the studied spatially embedded overload models. The Stage-3 specification **does not generalize their approximately constant propagation velocity into a universal infrastructure law**.

Similarly, HELICS provides precedent for federated heterogeneous co-simulation; its use does not imply that every P–T–I–O subsystem requires maximum simulator fidelity. The controlling rule remains

$$
\text{maximum necessary physical fidelity}\neq\text{maximum possible model detail}.
$$

## 6. Freeze rule

The Stage-3 architecture is frozen at framework level. Later implementation choices may specify particular power-flow, traffic, rail, information, organizational, numerical-integration, synchronization, and uncertainty models **without changing Stage 3**, provided they remain consistent with its scientific objects and boundary rules.
