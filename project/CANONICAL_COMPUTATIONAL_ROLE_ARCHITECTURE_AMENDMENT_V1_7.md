# Canonical Computational Role Architecture Amendment v1.7 — Li & Mostafavi Alignment

**Status:** CANONICAL ADDITIVE AMENDMENT TO P1.11.6
**Effective date:** 2026-09-19
**Evidence source:** Li & Mostafavi (2025), *Machine learning approach for disaster risk and resilience assessment in coupled human infrastructure systems performance*, npj Natural Hazards 2:56, DOI 10.1038/s44304-025-00104-4
**Primary scientific contribution:** observational/data-driven post-event computation and resilience diagnostics
**Seven-stage architecture:** UNCHANGED
**RQ1–RQ7 / SO1–SO7 / H1–H5:** UNCHANGED
**Sustainability admission scope:** UNCHANGED
**Empirical effect:** NONE

## 1. Permanent computational ontology

The thesis shall distinguish:

~~~math
\boxed{
\text{physical system}
\neq
\text{observations}
\neq
\text{computed features}
\neq
\text{indices}
\neq
\text{diagnostic patterns}
\neq
\text{decisions}.
}
~~~

Computation transforms declared scientific objects. It does not create physical truth, causal mechanisms, requirements, preferences or validation by itself.

## 2. Three computational lanes

For audit and implementation, computation is classified into three thesis-derived lanes:

~~~math
\boxed{
\begin{array}{ccc}
\textbf{MECHANISTIC} &
\textbf{OBSERVATIONAL} &
\textbf{DECISION}\\
\text{What could physically happen?} &
\text{What is/was the system doing?} &
\text{How should qualified alternatives be compared?}
\end{array}
}
~~~

### Mechanistic lane

~~~math
(\mathcal G,\mathbb I^{qualified},\theta,\eta,u)
\rightarrow
Y^{phys}(t).
~~~

Primary owners: Stages 2–3.

The Li–Mostafavi paper does not validate this lane for Power–Transportation dynamics.

### Observational lane

~~~math
\boxed{
\mathcal D_{\rm raw}
\rightarrow
\mathcal M^{align}
\rightarrow
\Phi_{\rm feat}
\rightarrow
Z^{obs}
\rightarrow
\mathcal E
\rightarrow
(b_t,\widehat Y,\widehat q,\mathcal D_R).
}
~~~

Primary owners: Stages 1, 4 and diagnostic parts of Stage 5.

Where:
- \(\mathcal D_{\rm raw}\): raw heterogeneous datasets;
- \(\mathcal M^{align}\): spatial/temporal/semantic support alignment;
- \(\Phi_{\rm feat}\): scientifically specified feature transformation;
- \(Z^{obs}\): computed observational feature object;
- \(\mathcal E\): estimator/statistical model;
- \(b_t,\widehat Y,\widehat q\): belief/estimate/QOI;
- \(\mathcal D_R\): resilience-diagnostic products.

### Decision lane

~~~math
\text{qualified results}
\rightarrow
\text{comparison}
\rightarrow
\text{robustness/trade-offs}
\rightarrow
\text{decision support}.
~~~

Primary owners: Stages 6–7.

Decision computation cannot silently insert preferences, weights or policy values.

## 3. Every computation requires a scientific-role record

For every algorithm, simulation, spatial join, regression, estimator, PCA, clustering routine, optimizer or visualization, record:

~~~text
COMPUTATION_ID
STAGE
LANE
SCIENTIFIC_QUESTION
INPUT_OBJECT_CLASS
INPUT_PROVENANCE
TRANSFORMATION
OUTPUT_OBJECT_CLASS
SPATIAL_SUPPORT_IN
SPATIAL_SUPPORT_OUT
TEMPORAL_SUPPORT_IN
TEMPORAL_SUPPORT_OUT
REFERENCE_STATE_ID
UNCERTAINTY
VERIFICATION
VALIDATION
SOURCE_SUPPORT
CLAIM_CEILING
ALLOWED_CLAIM
PROHIBITED_INFERENCE
VERSION
~~~

Permanent:

~~~math
\boxed{
\text{input object}
\rightarrow
\text{declared transformation}
\rightarrow
\text{output object}
\rightarrow
\text{allowed claim}.
}
~~~

## 4. Analysis support must be explicit

Heterogeneous observations shall not be silently pooled across incompatible spatial units.

~~~math
\boxed{
\Omega_i^{raw}
\xrightarrow{\mathcal M^{align}}
\Omega^{anal}.
}
~~~

\(\Omega^{anal}\) may be a node, road link, intersection, service area, zone, interface or other declared support appropriate to the QOI.

Permanent:

~~~math
\boxed{
\text{raw spatial resolution}
\neq
\text{analysis support}.
}
~~~

Aggregation/crosswalk uncertainty and information loss must be recorded.

## 5. Stage-2 causal firewall

Data-driven outputs cannot qualify a physical dependency by themselves.

~~~math
\boxed{
\text{association}
\neq
\text{causal mechanism}.
}
~~~

~~~math
\boxed{
\text{feature importance}
\neq
\text{physical interface strength}.
}
~~~

~~~math
\boxed{
\ell_i^{PCA}
\neq
\theta_e^{phys}
\neq
C_e^{causal}
\neq
C_e^{\mathcal V}.
}
~~~

The final two quantities are thesis scientific objects; they are not PCA meanings.

## 6. Stage-3 firewall

~~~math
\boxed{
\text{data-driven post-event characterization}
\neq
\text{physical/hybrid dynamic simulation}.
}
~~~

Stage 3 remains governed by qualified mechanisms and executable dynamics:

~~~math
\dot Y=F_{\mathcal G}(Y,u,\eta;\theta)
~~~

or the active hybrid flow/jump formulation.

PCA, clustering or post-event indices cannot replace \(F_{\mathcal G}\).

## 7. Stage-4 feature architecture

Stage 4 may construct scientifically defined observational features before estimation.

~~~math
\boxed{
Z^{obs}
=
\Phi_{\rm feat}
\left(
\mathcal M^{align}(\mathcal D_{\rm raw});
R^{ref}
\right).
}
~~~

\(R^{ref}\) denotes a declared reference/baseline object where the feature definition requires one.

Feature construction must record:
- raw data identity;
- units;
- temporal window;
- spatial support;
- reference period/state;
- transformation;
- missing-data handling;
- normalization/scaling;
- uncertainty;
- validity domain.

## 8. Reference-state rule

Many observed performance features are meaningful only relative to a declared reference.

~~~math
\boxed{
\Delta Q(t)=Q(t)-Q^{ref}(t)
}
~~~

when this contrast is scientifically appropriate.

Intervention contrasts remain:

~~~math
\Delta\mathfrak R(a_k)
=
\mathfrak R(a_k)-\mathfrak R(a_{ref}),
~~~

~~~math
\Delta J_j(a_k)
=
J_j(a_k)-J_j(a_{ref}).
~~~

A reference state is not automatically an authoritative requirement.

## 9. Formal resilience versus diagnostics

The formal Stage-5 resilience carrier remains \(\mathfrak R_T\).

Data-driven diagnostic outputs remain in the existing Stage-5 diagnosis object \(\mathcal D_R\).

~~~math
\boxed{
\mathfrak R_T
\neq
\mathcal D_R.
}
~~~

Examples of \(\mathcal D_R\):
- recovery-duration summaries;
- spatial archetypes;
- clustering labels;
- feature contributions/loadings;
- diagnostic maps;
- post-event classifications.

A PCA-derived resilience index from another study is not imported as the thesis definition of resilience.

## 10. Statistical importance firewall

~~~math
\boxed{
\text{statistical importance}
\neq
\text{physical importance}
\neq
\text{causal importance}
\neq
\text{viability criticality}.
}
~~~

PCA loadings describe the statistical construction used by that method.

They are not physical coupling parameters or causal sensitivity coefficients.

## 11. Spatial heterogeneity

Where material to the QOI, retain spatially resolved results before aggregation:

~~~math
Q(\mathbf r,t),
\qquad
\rho_{\mathcal V}(\mathbf r,t),
\qquad
\Delta J_j(\mathbf r,t).
~~~

Permanent:

~~~math
\boxed{
\bar Q(t)
\text{ may hide }
Q(\mathbf r,t).
}
~~~

Aggregation must state the support, weighting and information loss.

## 12. Socioeconomic attributes are context, not automatic endpoints

A population/context variable such as income is not automatically a resilience metric, sustainability metric, requirement or preference.

~~~math
\boxed{
\text{population attribute}
\neq
\text{social-sustainability endpoint}.
}
~~~

If scientifically admitted, attributes may stratify/disaggregate an existing result:

~~~math
Q^{(g)},
\qquad
J_j^{(g)}.
~~~

Group definitions and weights require provenance and must not be invented.

This does not reopen the frozen sustainability scope.

## 13. Intervention-effect firewall

Observed clusters/archetypes do not establish intervention effects.

~~~math
\boxed{
\text{observational cluster}
\not\Rightarrow
\Delta\mathfrak R(a_k).
}
~~~

Stage 6 requires matched intervention comparisons or another qualified causal design.

## 14. Algorithm-specific claim ceilings

### PCA

~~~math
Z^{obs}\xrightarrow{PCA}Z^{PC}.
~~~

Allowed:
- dimension reduction;
- statistical variance structure;
- method-specific feature contribution.

Not allowed by PCA alone:
- physical causality;
- interface strength;
- requirement satisfaction;
- intervention effect;
- viability criticality.

### Clustering

~~~math
Z\xrightarrow{cluster}\{\mathcal C_1,\ldots,\mathcal C_K\}.
~~~

Allowed:
- pattern/archetype discovery within the declared feature space.

Not allowed by clustering alone:
- proof of a physical dynamical regime;
- causal mechanism;
- optimal intervention;
- policy preference.

### Machine learning

Predictive/diagnostic ML may support estimation or pattern recognition subject to validation.

~~~math
\boxed{
\text{ML performance}
\neq
\text{causal identification}.
}
~~~

## 15. Source-specific evidence boundary

Li & Mostafavi provide direct evidence for:
- multi-source post-event feature construction;
- common spatial analysis support at Census Block Group level;
- PCA-based risk/resilience index construction;
- hierarchical clustering into spatial archetypes;
- recovery features relative to pre-event/normal activity;
- spatial and socioeconomic heterogeneity;
- data limitations and need for contextual interpretation.

They do not provide direct evidence for:
- Power \(\to\) Transportation or Transportation \(\to\) Power causal mechanisms;
- coupled P–T Stage-3 dynamics;
- thesis viability/reachability geometry;
- H1–H5 outcomes;
- thesis sustainability accounting definition;
- intervention-effect identification.

The paper explicitly excluded power outages from its Harvey analysis because extensive power outages did not occur in the study area.

## 16. Permanent computational firewalls

~~~math
\boxed{
\begin{aligned}
\text{more computation} &\not\Rightarrow \text{more scientific validity},\\
\text{more features} &\not\Rightarrow \text{better model},\\
\text{machine learning} &\neq \text{causal identification},\\
\text{index} &\neq \text{physical state},\\
\text{diagnostic pattern} &\neq \text{physical mechanism}.
\end{aligned}
}
~~~

## 17. P2 mandatory fields

P2 shall include:

~~~text
COMPUTATION_ID
COMPUTATIONAL_LANE
SCIENTIFIC_ROLE
INPUT_OBJECT_CLASS
OUTPUT_OBJECT_CLASS
TRANSFORMATION_ID
RAW_DATASET_ID
FEATURE_DEFINITION_ID
ALIGNMENT_OPERATOR_ID
SPATIAL_SUPPORT_IN
SPATIAL_SUPPORT_OUT
TEMPORAL_SUPPORT_IN
TEMPORAL_SUPPORT_OUT
REFERENCE_STATE_ID
NORMALIZATION_ID
UNCERTAINTY_ID
VERIFICATION_STATUS
VALIDATION_STATUS
SOURCE_SUPPORT_CLASS
CLAIM_CEILING
ALLOWED_CLAIM
PROHIBITED_INFERENCE
DIAGNOSTIC_VS_PRIMARY_OBJECT
AGGREGATION_INFORMATION_LOSS
GROUP_STRATIFICATION_STATUS
~~~

## 18. Empirical firewall

~~~math
\boxed{
G_{P1.11.7}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

No empirical P–T mechanism, resilience superiority, sustainability result, intervention effect or decision ranking is established by this amendment.
