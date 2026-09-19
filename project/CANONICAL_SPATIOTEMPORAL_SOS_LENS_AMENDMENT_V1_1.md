# Canonical Spatiotemporal SoS Lens Amendment v1.1 — Pant Spatial-Risk / Functional-Pathway Alignment

**Status:** CANONICAL ADDITIVE AMENDMENT TO P1.11  
**Effective date:** 2026-09-19  
**Parent authority:** \`project/CANONICAL_SPATIOTEMPORAL_SOS_RESILIENCE_TRANSFORMATION_LENS_V1.md\`  
**Evidence role:** Pant et al., Chapter 12 supports spatial hazard, interdependent-network, functional-pathway, service-consequence and risk-analysis concepts; it does not validate the thesis-derived hybrid/viability mathematics.  
**Seven-stage architecture:** UNCHANGED  
**RQ1–RQ7 / SO1–SO7 / H1–H5:** UNCHANGED  
**Empirical effect:** NONE

## 1. Purpose

This amendment closes five interpretive gaps made explicit by the Pant et al. spatial interdependent-risk framework:

1. functional pathways must be distinguished from bare graph paths;
2. common-cause spatial hazard exposure must be separated from cross-system cascade;
3. criticality must distinguish topology, flow/service consequence, hazard conditioning and viability sensitivity;
4. binary/static failure models are bounded special cases, not the universal thesis state model;
5. risk and resilience are complementary but non-equivalent scientific objects.

## 2. Spatially coherent hazard and causal chronology

For spatially dependent disturbances, the default causal chronology is:

~~~math
\boxed{
\eta(\mathbf r,t)
\rightarrow
\text{direct asset effects}
\rightarrow
\text{qualified cross-system propagation}
\rightarrow
\text{service consequences}
\rightarrow
\text{recovery/resilience consequences}.
}
~~~

Permanent firewall:

~~~math
\boxed{
P\leftarrow\eta\rightarrow T
\neq
P\rightarrow T
\neq
T\rightarrow P.
}
~~~

A common hazard may generate correlated failures in both systems without establishing a directed interdependency.

The hazard representation must preserve spatial coherence at the resolution required by the mechanism/QOI. A scalar hazard is admissible only when justified by the intended use and does not erase material spatial heterogeneity.

## 3. Functional pathways are mandatory where service propagation is claimed

A graph path is structural. A functional pathway links source, transmission/transport mechanism, sink and service recipient.

~~~math
\boxed{
\text{graph path}
\neq
\text{functional pathway}.
}
~~~

When a thesis claim depends on service delivery or restoration, the relevant pathway shall be represented as applicable:

~~~math
\boxed{
\text{source}
\rightarrow
\text{network/interface pathway}
\rightarrow
\text{service sink}
\rightarrow
\text{service recipient}.
}
~~~

Examples:

~~~math
\text{generation/substation}
\rightarrow
\text{electrical network}
\rightarrow
\text{load}
\rightarrow
\text{electric service},
~~~

~~~math
\text{origin}
\rightarrow
\text{transport path}
\rightarrow
\text{destination}
\rightarrow
\text{mobility service},
~~~

~~~math
\text{crew depot}
\rightarrow
\text{road path}
\rightarrow
\text{damaged power asset}
\rightarrow
\text{repair}
\rightarrow
\text{restored electrical service}.
~~~

A dependency arrow without a defensible functional pathway cannot, by itself, establish a service-consequence claim.

## 4. Spatial proximity is evidence of possibility, not proof of dependency

Permanent:

~~~math
\boxed{
\text{nearest spatial asset}
\neq
\text{observed physical dependency}.
}
~~~

Nearest-neighbour or nearest-compatible-network mapping may be used only as:
- a synthesis assumption;
- a candidate crosswalk;
- a hypothesis-generation device;
- a bounded proxy with explicit uncertainty.

It cannot alone make \(G_2^{causal}=PASS\) or \(G_{2\to3}=PASS\).

## 5. Static/binary models are bounded special cases

Binary state:

~~~math
r_i\in\{0,1\}
~~~

is admissible for a declared reliability/risk abstraction, but:

~~~math
\boxed{
\{0,1\}
\subset
\text{allowable thesis state representations}
}
~~~

and is not the universal state model.

Power and transportation may require continuous or hybrid states such as loading, voltage, capacity, speed, density, queue, accessibility, derating, islanding, partial blockage and restoration mode.

Likewise, fixed route assignment/no-rerouting may be used as a benchmark or bounded approximation, but dynamic claims involving congestion, accessibility, crew travel or rerouting require a transport representation capable of those effects.

## 6. Criticality hierarchy

The thesis shall keep at least the following criticality concepts distinct:

~~~math
\boxed{
C^{topo}
\neq
C^{flow/service}
\neq
C^{hazard}
\neq
C^{\mathcal V}.
}
~~~

Interpretation:

- \(C^{topo}\): structural graph importance;
- \(C^{flow/service}\): importance conditional on flows, users or service delivered;
- \(C^{hazard}\): importance under spatially/temporally conditioned hazard exposure;
- \(C^{\mathcal V}\): mechanism/state-specific influence on viability/recoverability.

The progression

~~~math
\boxed{
\text{topological}
\rightarrow
\text{service-weighted}
\rightarrow
\text{hazard-conditioned}
\rightarrow
\text{viability-sensitive}
}
~~~

is a diagnostic hierarchy, not a claim that later measures are automatically superior.

If the thesis claims incremental engineering value for \(C^{\mathcal V}\), it must be tested against qualified simpler comparators under P1.3/P1.4/P1.9 controls.

## 7. Spatial criticality may be local or field-like

Two complementary objects are admissible:

~~~math
C_e^{local}
~~~

for a component/interface/mechanism, and

~~~math
C^{spatial}(\mathbf r,t)
~~~

for spatial concentrations of interacting infrastructure/service importance.

No field-like criticality representation is required unless the evidence, data and intended use justify spatial interpolation/aggregation.

## 8. Risk is not resilience

Pant-style risk may be represented abstractly as:

~~~math
R(r)=D(r)P(r)
~~~

within its declared probability/consequence model.

The thesis resilience object remains separate:

~~~math
\boxed{
\text{risk}
\neq
\text{resilience}.
}
~~~

Risk asks what may fail, with what likelihood and consequence.

Resilience asks whether acceptable service can remain or return under disturbance, with quantified confidence/uncertainty.

A legitimate cross-stage relation is:

~~~math
\boxed{
\text{hazard/risk evidence}
\rightarrow
\text{candidate vulnerability}
\rightarrow
\text{dynamic resilience analysis}
\rightarrow
\text{intervention}.
}
~~~

Risk metrics do not replace Stage-5 viability/reachability objects.

## 9. Service consequence remains distinct from economic consequence

Permanent:

~~~math
\boxed{
\text{asset state}
\neq
\text{service disruption}
\neq
\text{economic/social consequence}.
}
~~~

The thesis core may terminate at service/resilience/sustainability consequences without implementing a macroeconomic input-output model unless such a model becomes an explicit, evidence-supported scope requirement.

## 10. Spatiotemporal acceptability

Where requirements vary spatially, Stage 5 may use spatially indexed service requirements:

~~~math
Q_j^{req}(\mathbf r,t).
~~~

The canonical acceptable set remains an object over the full system state:

~~~math
\boxed{
K(t)
=
\left\{
Y:
h_j(Y,t)\le 0,\ j=1,\ldots,n_K
\right\},
}
~~~

with \(h_j\) permitted to evaluate spatially distributed services.

This avoids redefining \(K\) as a continuous spatial field unless the model requires one.

## 11. Interface criticality must retain conditioning

A viability-sensitive interface diagnostic shall be interpreted as conditioned on the declared operating point/scenario/hazard/control context.

Conceptually:

~~~math
S_e^{\mathcal V}
=
S_e^{\mathcal V}
\left(
Y,\eta,u,\Theta,\Omega,t
\right)
~~~

where applicable.

This is an interpretation of conditioning, not a mandatory universal functional form.

The diagnostic must answer:

~~~text
Which interface?
Where?
When?
Under which hazard?
Under which operating/control state?
With what uncertainty?
~~~

## 12. Recovery versus transformation

Permanent:

~~~math
\boxed{
\text{recovery}
\neq
\text{transformation}.
}
~~~

Recovery concerns return to acceptable service under the current/declared system.

Transformation changes long-lived architecture, capacity, technology, interface structure or future feasible actions.

## 13. P2 mandatory audit additions

The global Stage 1–7 master register must include explicit audit fields for:

~~~text
HAZARD_SPATIAL_COHERENCE
COMMON_CAUSE_VS_CASCADE
FUNCTIONAL_PATHWAY
SPATIAL_PROXY_STATUS
STATE_MODEL_FIDELITY
TRANSPORT_REROUTING_FIDELITY
CRITICALITY_CLASS
RISK_VS_RESILIENCE
SERVICE_VS_ECONOMIC_CONSEQUENCE
SPATIOTEMPORAL_ACCEPTABILITY
INTERFACE_CRITICALITY_CONDITIONING
RECOVERY_VS_TRANSFORMATION
~~~

Each field shall be PASS / BLOCKED / N/A with rationale and provenance.

## 14. Evidence boundary

Pant et al. provide a strong precedent for spatially explicit interdependent infrastructure risk analysis, service/functional pathways, customer/consequence mapping and topological cascading logic.

They explicitly do not provide the thesis's state-dependent hybrid flow/jump dynamics, viability/reachability formulation or validated viability-sensitive interface metric.

~~~math
\boxed{
\text{Pant spatial-risk precedent}
\neq
\text{validation of thesis-derived dynamic/viability mathematics}.
}
~~~

## 15. Empirical firewall

~~~math
\boxed{
G_{P1.11.1}^{design}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

No case-specific dependency, hazard field, parameter, threshold, validation outcome or hypothesis result is created by this amendment.
