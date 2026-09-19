# Stage 4 Cross-System Observation and Inference Amendment v1.2

**Status:** CANONICAL ADDITIVE STAGE-4 AMENDMENT — DESIGN/PROTOCOL ONLY  
**Effective date:** 2026-09-19  
**Parent:** \`STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md\`  
**Cross-stage authority:** P1.11.4 observational/informational interdependency amendment  
**Empirical H2 closure:** NOT IMPLIED

## 1. Purpose

Allow measurements from one infrastructure domain to improve estimation/prediction in another without misclassifying predictive association as physical causality.

## 2. Extended available-information object

The parent object remains:

~~~math
\mathcal I_t=\{y_{0:t},\text{messages},\text{forecasts},\text{reports}\}.
~~~

Cross-system observations may be included as typed members:

~~~math
\boxed{
\mathcal I_t^{xsys}
=
\mathcal I_t
\cup
\{
\widetilde y_s^{0:t}:
G_{obs,s\to r}=PASS
\}.
}
~~~

They remain observations/features, not physical states.

## 3. Observational relation record

Use:

~~~math
\boxed{
\mathfrak o^{obs}_{s\rightsquigarrow r}
=
(
y_s,
\mathcal M^{align}_{s\to r},
\tau_{obs},
\mathcal E_r,
\widehat q_r,
\mathbb U_{obs},
\Omega_{obs},
\Pi_{obs}
).
}
~~~

The arrow \(\rightsquigarrow\) is explicitly noncausal.

## 4. Admission gate

~~~math
\boxed{
G_{obs}
=
G_{source}
\land
G_{align}
\land
G_{time}
\land
G_{sem}
\land
G_{leak}
\land
G_{baseline}
\land
G_{eval}
\land
G_U
\land
G_{\Omega}
\land
G_{prov}.
}
~~~

Where:
- source data are qualified;
- space/time/semantic/resolution alignment is reproducible;
- no future leakage occurs;
- comparator/baseline is declared;
- evaluation is protected;
- uncertainty and validity are reported.

## 5. Estimation

A receiver estimator may use cross-system observations:

~~~math
\boxed{
b_t
=
\mathcal E
(
\mathcal I_t^{xsys},
\mathfrak M_3
).
}
~~~

or, for a declared predictive QOI:

~~~math
\widehat q_r(t+\tau)
=
\mathcal E_r(\mathcal I_t^{xsys}).
~~~

No estimator output becomes physical truth.

## 6. Lag semantics

~~~math
\boxed{
\tau_{obs}
\neq
\delta_e^{phys}
\neq
\tau^{info}.
}
~~~

Lag selection/estimation must be performed without confirmatory outcome leakage.

## 7. H2 information comparator

A qualified Stage-4 information comparison may hold physical scenario, Stage-3 mechanisms and physical parameters fixed while changing only admitted information:

~~~math
\boxed{
\mathscr N_{I0}
:
\mathcal I_t^{target}
\qquad\text{vs}\qquad
\mathscr N_{I1}
:
\mathcal I_t^{target}
\cup
\mathcal I_t^{xsys}.
}
~~~

Primary information QOIs must be preregistered.

System-resilience effects require the additional control/service chain and cannot be inferred directly from forecast error reduction.

## 8. Claim boundary

~~~math
\boxed{
G_{obs}=PASS
\not\Rightarrow
G_2^{causal}=PASS
\not\Rightarrow
H2=SUPPORTED.
}
~~~

Predictive validity, causal validity and resilience benefit are separate claims.
