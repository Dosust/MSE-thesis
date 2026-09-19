# Canonical SoS Information Architecture Amendment v1.2 — Barr Chapter 13 Alignment

**Status:** CANONICAL ADDITIVE AMENDMENT TO P1.11  
**Effective date:** 2026-09-19  
**Parent authority:** \`project/CANONICAL_SPATIOTEMPORAL_SOS_RESILIENCE_TRANSFORMATION_LENS_V1.md\`  
**Prior refinement:** \`project/CANONICAL_SPATIOTEMPORAL_SOS_LENS_AMENDMENT_V1_1.md\`  
**Scope:** data hierarchy, cross-model alignment, provenance, orchestration, visualization and versioned system information  
**Seven-stage architecture:** UNCHANGED  
**RQ1–RQ7 / SO1–SO7 / H1–H5:** UNCHANGED  
**Empirical effect:** NONE

## 1. Scientific decision

A credible Power–Transportation System-of-Systems thesis requires three coupled but non-identical systems:

~~~math
\boxed{
\begin{aligned}
\mathscr S_{\rm physical}&=\text{actual P--T infrastructure SoS},\\
\mathscr S_{\rm model}&=\text{mathematical/computational representation},\\
\mathscr S_{\rm information}&=\text{data + metadata + provenance + orchestration}.
\end{aligned}
}
~~~

Permanent:

~~~math
\boxed{
\mathscr S_{\rm physical}
\neq
\mathscr S_{\rm model}
\neq
\mathscr S_{\rm information}.
}
~~~

The information system supports traceable model execution; it is not itself the physical dynamics.

## 2. Vertical hierarchy versus horizontal interaction

Infrastructure representation shall distinguish vertical membership/aggregation from horizontal interaction.

Vertical hierarchy:

~~~math
\boxed{
\text{asset}
\rightarrow
\text{network}
\rightarrow
\text{sector/system}
\rightarrow
\text{System of Systems}.
}
~~~

Define conceptually:

~~~math
\mathcal H_V=\text{containment/aggregation relations},
~~~

~~~math
\mathcal H_H=\text{candidate/qualified interaction relations}.
~~~

Permanent:

~~~math
\boxed{
\text{membership}
\neq
\text{causal influence}.
}
~~~

A substation belonging to the power network does not imply a cross-sector dependency. A road link belonging to the transport network does not imply a repair dependency until Stage 2 qualifies a mechanism.

## 3. Spatial, temporal and semantic alignment are explicit operations

Power and Transportation data/models may use different spatial supports, temporal resolutions and semantic conventions.

Define the representation-alignment operator:

~~~math
\boxed{
\mathcal M_{P\leftrightarrow T}^{align}
=
\left(
\mathcal M^{space},
\mathcal M^{time},
\mathcal M^{sem}
\right).
}
~~~

An aligned transfer may be written:

~~~math
x_P(\mathbf r_P,t_P)
\xrightarrow{\mathcal M^{align}}
\xi_{P\to T}(\mathbf r_T,t_T).
~~~

Permanent firewall:

~~~math
\boxed{
\text{representation alignment}
\neq
\text{causal mechanism}.
}
~~~

Only a qualified Stage-2 mechanism may map the aligned quantity into a receiver effect:

~~~math
\xi_{P\to T}
\xrightarrow{\Phi_e}
x_T.
~~~

Every alignment must declare source/target support, interpolation/aggregation/resampling rule, units, uncertainty effect and validity domain.

## 4. Data resolution is not physical truth

The thesis may represent infrastructure information as points, lines, polygons, zones, networks, rasters, time series or aggregated sectors.

Permanent:

~~~math
\boxed{
\text{database representation}
\neq
\text{physical reality}.
}
~~~

And:

~~~math
\boxed{
\text{resolution}
\neq
\text{accuracy},
\qquad
\text{aggregation}
\neq
\text{homogeneity}.
}
~~~

A yearly data series does not imply yearly physical dynamics. A road represented by one edge is not assumed physically uniform. A service polygon does not imply identical service everywhere within it.

## 5. Physical coupling versus software coupling

Physical coupling:

~~~math
P\xrightarrow{\Phi_{PT}}T
~~~

is a scientific statement.

Computational coupling:

~~~math
M_P\xrightarrow{\mathcal H_{P\to T}^{data}}M_T
~~~

is an implementation statement.

Permanent:

~~~math
\boxed{
\text{physical coupling}
\neq
\text{software coupling}.
}
~~~

The two must be traceable to one another when software coupling implements a physical mechanism.

A data/API connection between two solvers is not evidence that the corresponding physical interdependency exists.

## 6. Database/result broker role

The information architecture may act as a result-set broker among modules:

~~~math
M_i
\rightarrow
R_i
\rightarrow
D_{\rm broker}
\rightarrow
X_j
\rightarrow
M_j.
~~~

The broker stores and serves qualified data/results. It does not define the scientific law that relates producer and consumer.

Permanent:

~~~math
\boxed{
\text{stored relation}
\neq
\text{qualified causal dependency}.
}
~~~

## 7. Observation / estimation / database firewall

The existing physical–epistemic distinction is extended with the explicit data carrier:

~~~math
\boxed{
Y^{phys}
\neq
y
\neq
\widehat Y
\neq
b_t
\neq
D.
}
~~~

where:
- \(Y^{phys}\): physical system state;
- \(y\): observation/measurement;
- \(\widehat Y\): point/state estimate where used;
- \(b_t\): epistemic belief/information state where used;
- \(D\): stored data/database representation.

A database value is never treated as physical truth merely because it is machine-readable.

## 8. Canonical inter-model handoff provenance

Every material computational transfer shall create or reference a provenance record:

~~~math
\boxed{
\mathfrak P_h
=
(
HID,
M_s,V_s,RID_s,X_s,U_s,S_s,T_s,
\mathcal T_h,
M_r,V_r,X_r,U_r,S_r,T_r,
\mathbb U_h,
SID,
DVer,
CVer,
VVUQ_h,
\Omega_h,
\Lambda_h,
Status_h,
Prov_h
).
}
~~~

Minimum semantics:
- immutable handoff ID;
- source model/module and version;
- source run/result ID;
- source variable/object and unit;
- source spatial/temporal support;
- transformation/alignment rule;
- receiving model/module and version;
- target variable/object and unit;
- target spatial/temporal support;
- uncertainty IDs / propagation rule;
- scenario ID;
- data version;
- code/model version or hash;
- VVUQ status;
- validity/context-of-use domain;
- claim ceiling;
- gate/status;
- exact provenance.

## 9. Mandatory transfer trace

Every material inter-model transfer must be reconstructable as:

~~~math
\boxed{
\text{source}
\rightarrow
\text{source variable}
\rightarrow
\text{space/time/semantic transform}
\rightarrow
\text{qualified interface/mechanism}
\rightarrow
\text{receiver variable}
\rightarrow
\text{downstream result}.
}
~~~

For confirmatory work, the trace must also recover:
- root scenario / experimental arm / run ID;
- relevant requirement baseline;
- uncertainty representation;
- model/data/code versions;
- result ID and claim family.

## 10. Uncertainty is part of the information object

A scientific data record is not merely a scalar \(x\).

Conceptually:

~~~math
\boxed{
D_x
=
(
x,
unit,
\mathbf r,
t,
U_x,
source,
version,
quality,
validity,
provenance
).
}
~~~

No probability distribution is required unless justified.

The thesis-wide uncertainty chain remains:

~~~math
\boxed{
\text{data/measurement uncertainty}
\rightarrow
\text{parameter/state uncertainty}
\rightarrow
\text{service uncertainty}
\rightarrow
\text{viability uncertainty}
\rightarrow
\text{decision uncertainty}.
}
~~~

P1.7 remains the controlling uncertainty authority.

## 11. Hazard as a versioned data object

For spatial hazard analysis, \(\eta(\mathbf r,t)\) shall be backed by a qualified hazard-data object that records, as applicable:

~~~text
hazard_id
hazard_type
geometry/support
coordinate reference
spatial resolution
temporal support/resolution
intensity variable
unit
source/version
uncertainty
processing/transformation
validity domain
scenario/run linkage
provenance
~~~

Hazard intersection with an asset/network object is a transformation step and must be traceable.

## 12. Visualisation has scientific roles but is not evidence

Visualization may support:

~~~math
\boxed{
\text{verification}
+
\text{scientific interpretation}
+
\text{decision communication}.
}
~~~

Permanent:

~~~math
\boxed{
\text{visual plausibility}
\neq
\text{model validation}.
}
~~~

A visually convincing cascade, map, animation or dashboard cannot establish mechanism validity without independent evidence/VVUQ.

## 13. Three geometries must remain distinct

The thesis may use:

~~~math
d_{\rm geo}(i,j)
~~~

for physical/geographic distance,

~~~math
d_{\mathcal G}(i,j)
~~~

for network/topological distance,

and

~~~math
d_g(Y,\partial\mathcal V)
~~~

for state/viability geometry.

Permanent:

~~~math
\boxed{
\text{physical geography}
\neq
\text{network topology geometry}
\neq
\text{state/viability geometry}.
}
~~~

No distance may be substituted for another without an explicit transformation and justification.

## 14. Transformation requires versioned architectures

A Stage-7 transformation shall not silently overwrite the baseline system.

Use versioned architecture/state-of-design objects:

~~~math
\boxed{
\mathcal G^{(0)}
\rightarrow
\mathcal G^{(1)}
\rightarrow
\mathcal G^{(2)}
\rightarrow
\cdots
}
~~~

with corresponding versions where applicable:

~~~math
\Theta^{(k)},
\qquad
\mathbb I^{(k)},
\qquad
\mathcal U_{\rm feas}^{(k)}.
~~~

Every transition must identify the intervention/action that produced it, the prior version, provenance, uncertainty and effective horizon.

## 15. Different scientific outputs remain different result objects

Stage 6/7 reporting shall not collapse:

~~~math
\boxed{
\mathcal O(a_k)
=
\left[
\Delta\mathfrak R^{a_k},
\mathcal E_{\rm fx}(a_k),
\mathcal E_{\rm fy}(a_k),
\Delta\mathbf J_{\rm sus}^{a_k}
\right].
}
~~~

The same simulation may contribute to several result objects, but each object has its own definition, units, uncertainty and claim role.

## 16. Reproducibility / auditability requirement

For every state, interface, parameter, result and decision used in a material thesis claim, the repository must be able to answer:

~~~text
WHAT is it?
WHERE is it defined/measured?
WHEN is it valid/effective?
WHERE did it come from?
WHAT transformations were applied?
WHICH model/module consumed it?
WHICH scenario/run produced or used it?
WITH what uncertainty and validity?
WHICH result and claim depend on it?
~~~

If these questions cannot be reconstructed for a material confirmatory object, the object is BLOCKED for confirmatory use.

## 17. P2 mandatory audit additions

P2 shall add the following explicit audit columns/records:

~~~text
HIERARCHY_LEVEL
VERTICAL_VS_HORIZONTAL_RELATION
SPATIAL_ALIGNMENT
TEMPORAL_ALIGNMENT
SEMANTIC_ALIGNMENT
DATA_REPRESENTATION
RESOLUTION_VS_TRUTH_FIREWALL
PHYSICAL_VS_SOFTWARE_COUPLING
HANDOFF_PROVENANCE_ID
SOURCE_MODEL_VERSION
SOURCE_RUN_RESULT_ID
TRANSFORMATION_ID
TARGET_MODEL_VERSION
UNCERTAINTY_LINEAGE
HAZARD_DATA_PROVENANCE
VISUALIZATION_ROLE
MAP_VS_GRAPH_VS_VIABILITY_GEOMETRY
ARCHITECTURE_VERSION
REPRODUCIBILITY_STATUS
~~~

Each applicable field must be PASS / BLOCKED / DEFERRED / N/A with rationale and provenance.

## 18. Evidence boundary

Barr et al. Chapter 13 supports the need for hierarchical SoS data representation, cross-model information exchange, provenance/audit trails, heterogeneous space/time scales, result storage and scientific visualization.

It does not establish that a database schema, software orchestration layer, dashboard or coupled solver is physically valid.

~~~math
\boxed{
\text{information architecture}
\neq
\text{physical-model validation}.
}
~~~

## 19. Empirical firewall

~~~math
\boxed{
G_{P1.11.2}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

No case value, model parameter, hazard realization, dependency, validation outcome or hypothesis result is introduced by this amendment.
