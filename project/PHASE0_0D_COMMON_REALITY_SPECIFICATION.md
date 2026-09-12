# Phase 0D — Common Reality Specification

**Status:** FROZEN TEST FIXTURE v1.0  
**Purpose:** define one infrastructure reality that must be represented by both `M_0` and `M_1` without changing physics, evidence, services, or test cases.  
**Authority:** Theoretical Decision Gate v1.0; 0C bounded saturation is closed.  
**Anti-bias rule:** only the ontology/type system may differ between `M_0` and `M_1` during 0D–0E.

---

## 1. Scientific control principle

The controlled comparison is

```math
\text{same reality}
+
\text{same evidence}
+
\text{same physics}
+
\text{same relation payload}
+
\text{same services}
+
\text{same test cases}.
```

Only the representation of **system identity and aspect/layer membership** changes.

No model may receive an additional state, mechanism, authority fact, evidence item, delay, service definition, or coupling fact unavailable to the other.

---

## 2. Constituent physical systems

The physical constituent systems are fixed as

```math
\mathcal D_{PT}=\{P,T\}.
```

### Power

```math
P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP}.
```

Representative physical state:

```math
x_P=[V,\theta,f,P_{ij},Q_{ij},P_G,P_L,SOC_B]^\top.
```

### Transportation

```math
T=T_R\cup T_B\cup T_U\cup T_H\cup T_M.
```

Representative physical state:

```math
x_T=[q,k,v,TT,A,SOC_{EV},s_{rail}]^\top.
```

The common physical state is

```math
X(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)
\end{bmatrix}.
```

---

## 3. Domain physics are invariant

The governing laws are not part of the ontology competition.

```math
\dot x_P=F_P(x_P,u_P,h_P,\vartheta_P),
```

```math
\dot x_T=F_T(x_T,u_T,h_T,\vartheta_T),
```

with

```math
F_P\neq F_T
```

in general.

Any accepted cross-domain relation may enter the receiving dynamics through the same common coupling payload used by both models, but neither ontology may replace `F_P` or `F_T` with a generic network law.

---

## 4. Informational and organizational reality

The common reality also contains informational and organizational states already present in the thesis:

```math
z_I=[A_I,L_I,Q_I,\Delta_I,p_{loss},e_X,\epsilon_{sync}]^\top,
```

```math
z_O=[A_O,C_O,R_O,W_O,\tau_D,\tau_C^O,\tau_M]^\top.
```

These are **real modeled functions/states in the test fixture**, not evidence that `I` and `O` must be represented as global layers or as domain-indexed aspects. That ontological choice is precisely what 0D tests.

The complete common state information available to both representations is

```math
Y^*(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix}.
```

---

## 5. Common service outputs

Both representations must support exactly the same service set:

```math
\mathcal Q^*=\{
Q_{electricity},
Q_{mobility},
Q_{emergency\ access}
\}.
```

Let

```math
Q_k(t)=G_k\!\left(Y^*(t)\right)
```

for the declared service functional `G_k`.

0D does not calculate resilience, viability, cascade loss, or recovery performance. It only verifies whether the ontology can preserve the information needed for later computation of these services.

---

## 6. Common entity universe

Let

```math
\mathcal V^*=\{e_1,\ldots,e_n\}
```

be the common set of engineering entities.

Every entity has an immutable identifier `id(e)`. The evidence fixture may also state factual attributes such as:

```text
- physical system affiliation;
- informational function;
- organizational responsibility;
- operator/authority identity;
- source and receiver in a dependency;
- mechanism;
- state/time information;
- evidence/provenance status.
```

These facts belong to the common evidence budget. **How an ontology encodes those facts is not predetermined by the fixture.**

To avoid privileging `M_1`, the common fixture does not declare the ordered pair `(domain, aspect)` to be the ontology. It merely retains source facts from which either representation may encode its own labels.

---

## 7. Equal evidence budget

Define the fixed fact set

```math
\mathcal E^*=\{f_1,\ldots,f_N\}.
```

The controlled information condition is

```math
\mathcal E_{M_0}=\mathcal E_{M_1}=\mathcal E^*.
```

Examples of facts that must be supplied identically to both models include:

```text
F1: a power feeder supplies electrical power to a fast-charging station;
F2: EV arrival/charging demand changes feeder loading;
F3: transport-side EV forecasts may be used by a power controller;
F4: information quality/latency can alter a control decision;
F5: a road authority can determine access conditions;
F6: road accessibility constrains power-repair crew mobilization;
F7: delayed repair can prolong electricity-service disruption;
F8: evidence supporting a relation has a declared confidence/provenance state.
```

No fact may be added to one model after a representational difficulty is observed unless the same fact is added to both and the protocol is versioned.

---

## 8. Common relation payload

0D intentionally does **not** compare dependency-contract designs.

For every relation `e`, both ontologies receive the same canonical Stage-2 payload fields:

```math
\mathcal R_e^*=
\left(
M_e,
w_e,
\delta_e,
\tau_e,
a_e,
m_e,
\mathcal H_{e,t}
\right).
```

Only endpoint typing differs between `M_0` and `M_1`.

This prevents the confound

```math
\text{ontology change}+\text{dependency-object change}.
```

The alternative dependency contracts

```math
\mathfrak d_e=(s,r,\rho,m,q,M,z,w,\delta,c,U,\mathcal H)
```

and

```math
\mathfrak D_e=(\mathcal C_e,\Sigma_e,\Pi_e,\Xi_e)
```

are explicitly deferred to 0F.

---

## 9. Frozen verification cases

Both ontologies must later encode the same five frozen cases from `REPRESENTATION_REQUIREMENTS_MATRIX.md`:

```text
V1 — reciprocal physical EV charging / feeder coupling;
V2 — information-mediated EV forecast -> power controller -> physical setpoint;
V3 — road authority -> access -> crew mobilization -> restoration;
V4 — mediated P -> T -> P feedback;
V5 — extension from P+T to P+T+W.
```

No case-specific ontology extension is allowed during comparison.

---

## 10. Invariance checklist

Before any 0E score can be entered, verify:

| Controlled quantity | `M_0` | `M_1` | Must match? |
|---|---|---|---|
| physical entities | same `V*` | same `V*` | yes |
| `x_P,x_T` | identical | identical | yes |
| `F_P,F_T` | identical | identical | yes |
| `z_I,z_O` facts | identical | identical | yes |
| service set `Q*` | identical | identical | yes |
| evidence set `E*` | identical | identical | yes |
| relation payload `R_e*` | identical | identical | yes |
| V1–V5 | identical | identical | yes |
| ontology/type labels | `M_0` | `M_1` | **no — experimental variable** |

---

## 11. Validity boundary

This file specifies a **symbolic/common engineering reality**, not a calibrated empirical case study.

Therefore 0D can establish formal information preservation, ambiguity, type-system differences and representational complexity. It cannot establish predictive superiority, resilience improvement, empirical causality, or novelty.
