# Global Symbol and Ontology Registry Amendment v1.1 — Observational Cross-System Relations

**Status:** ADDITIVE TO \`GLOBAL_SYMBOL_AND_ONTOLOGY_REGISTRY_V1.md\`  
**Effective date:** 2026-09-19  
**Purpose:** register cross-stage symbols introduced by P1.11.4 without rewriting the frozen P1.1 registry.

| Symbol | Definition | Type/class | Unit | Owner → consumers | Validity / uncertainty | Status |
|---|---|---|---|---|---|---|
| \(\rightsquigarrow\) | predictive/informational relation without causal claim | relation notation / epistemic | N/A | S4 → S5–S7 reporting | must not be read as causal arrow | CURRENT |
| \(\mathfrak o^{obs}_{s\rightsquigarrow r}\) | cross-system observational/predictive relation record | epistemic/inference tuple | heterogeneous | S4 → downstream evidence | requires \(G_{obs}\) | CURRENT |
| \(\tau_{obs}\) | observational/predictive lag | temporal / epistemic | time | S4 | distinct from physical delay and info latency | CURRENT |
| \(D_P,D_T\) | infrastructure demand/use processes when separately modeled | physical/service-demand quantity | case/native | S3/S4 → downstream | role as state/input/QOI must be declared | CURRENT-CONDITIONAL |
| \(\mathcal M^{align}_{s\to r}\) | spatial/temporal/resolution/semantic alignment operator | data transformation | heterogeneous | S4 | alignment != mechanism; transformation UQ required | CURRENT |
| \(G_{obs}\) | observational-relation admission gate | gate/status | N/A | S4 | predictive admission only | CURRENT |
| \(\mathcal E_{\rm fx}^{info}\) | information/forecast effectiveness object | performance / epistemic | metric-dependent | S4/S6 reporting | not system resilience | CURRENT-CONDITIONAL |
| \(\mathbf C_{info}\) | information resource vector | resource/accounting | heterogeneous | S6/S7 if used | only evidence-supported components | DEFERRED-CONDITIONAL |

Permanent additions:

~~~math
\boxed{
x_P\neq D_P\neq y_P,
\qquad
x_T\neq D_T\neq y_T.
}
~~~

~~~math
\boxed{
\tau_{obs}\neq\delta_e^{phys}\neq\tau^{info}.
}
~~~

~~~math
\boxed{
\rightsquigarrow\neq\rightarrow.
}
~~~
