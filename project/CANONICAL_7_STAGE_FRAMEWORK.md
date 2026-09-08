# Canonical 7-Stage Thesis Framework

**Status:** CANONICAL / AUTHORITATIVE  
**Effective date:** 2026-09-09  
**Scope:** Thesis framework architecture and all future representations of that architecture  
**Change control:** This specification remains authoritative until the user explicitly approves a change.  
**Representation rule:** Visual redesign may change hierarchy, layout, typography, geometry, spacing, and graphical encoding, but it may not change the scientific content.

---

## 1. Canonical seven-stage sequence

```math
\boxed{ 1\rightarrow2\rightarrow3\rightarrow4\rightarrow5\rightarrow6\rightarrow7 }
```

The seven stage names are:

1. **Multilayer Structure**
2. **Causal Mechanisms**
3. **Coupled Hybrid Multiscale Dynamics**
4. **Feedback & Control**
5. **Viability**
6. **Resilience-to-Sustainability Transformation Interface**
7. **Sustainable Transformation Pathways**

The main conceptual separation is:

```math
\boxed{ \underbrace{\text{Stages 1--5}}_{\text{Resilience Analysis}} \rightarrow \underbrace{\text{Stage 6}}_{\text{Translation Interface}} \rightarrow \underbrace{\text{Stage 7}}_{\text{Sustainable Transformation}} }
```

---

## 2. Exact canonical content

| Stage | Role | Main question |
|---|---|---|
| **1. Multilayer Structure** | P–T–I–O architecture | **What exists?** |
| **2. Causal Mechanisms** | Cross-layer cause-effect pathways | **Why does disruption propagate?** |
| **3. Coupled Hybrid Multiscale Dynamics** | Coupling + continuous dynamics + discrete events + timescales | **How and when does it evolve?** |
| **4. Feedback & Control** | Information, organization, decisions, intervention | **How does the system respond?** |
| **5. Viability** | Survival/recoverability under constraints | **Can it survive?** |
| **6. Resilience-to-Sustainability Transformation Interface** | Translate resilience findings into transformation requirements | **What do the resilience results imply for sustainability?** |
| **7. Sustainable Transformation Pathways** | Technical, organizational, environmental and policy transformation | **What should be changed for long-term sustainability?** |

---

## 3. Canonical mathematical hierarchy

```math
\boxed{ (\mathcal G,Y,Z) \rightarrow \mathcal C \rightarrow (Z,F,J,\tau) \rightarrow (\mathcal H_{\rm obs},\hat Y,I,O,\pi,u) \rightarrow (K,\mathcal V) \rightarrow R \xrightarrow{\mathcal T_{ST}} S }
```

This hierarchy is authoritative for the framework representation unless an explicit future change is approved.

---

## 4. Scientific-content preservation rule

```math
\boxed{ \textbf{CHANGE THE VISUAL HIERARCHY, NOT THE SCIENTIFIC CONTENT.} }
```

No new SDGs, equations, variables, applications, outputs, labels, pathway categories, or interpretations may be inserted into a representation of the canonical framework unless they are already part of this specification or are explicitly approved as a framework revision.

---

## 5. Audit of the previous generated illustration

The previous generated illustration is **illustrative only** and is **not authoritative** because it did not preserve the canonical content 100% verbatim.

The seven-stage sequence itself was preserved, but the illustration introduced extra material, paraphrased some wording, and added mathematical/output elements that were not explicitly part of the frozen canonical framework.

| Item | Status |
|---|---|
| Seven stage names | **Preserved** |
| Stage order | **Preserved** |
| Main questions | Mostly preserved, but some wording was reformatted |
| Roles | Mostly preserved, but some were expanded/paraphrased |
| Core mathematical objects | Some preserved; some extra objects were introduced |
| Stage 6 `R\rightarrow\mathcal T_{ST}\rightarrow S` | Preserved conceptually |
| Stage 7 pathway categories | Preserved conceptually |
| “Downstream Thesis Outputs and Applications” | **Added — not canonical** |
| SDG panel | **Added — not canonical** |
| “Critical interfaces”, “recovery bottlenecks”, etc. | **Added — not canonical** |
| Stage-7 symbols `S_T,S_O,S_E,S_P` | **Added — not frozen** |
| Extra application examples | **Added — not canonical** |
| Some equations/labels | Adapted rather than verbatim |

Therefore, that generated illustration must never be used as the source of scientific truth for the framework.

---

## 6. Representation authority

For future figures:

1. **Scientific source of truth:** this file.
2. **Exact-text figure construction:** Figma, TikZ/LaTeX, SVG, or another deterministic vector workflow.
3. **Generative image outputs:** may be used only as visual inspiration or illustrative drafts unless manually audited against this file.
4. **Any final thesis figure:** must pass the visual-fidelity protocol in [`../figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`](../figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md).

---

## 7. Change-control rule

A future change to the framework is valid only when all of the following are true:

- the change is explicitly requested or approved by the user;
- the canonical stage table is updated;
- the mathematical hierarchy is updated if affected;
- the change is recorded in Git history with a clear commit message;
- downstream figures are re-audited for consistency.

Until then, this seven-stage specification is frozen as the thesis framework authority.
