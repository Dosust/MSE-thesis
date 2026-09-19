# Stage 6 Quantity Origin, Uncertainty Lineage, and Effect Resolution Amendment v1.2

**Status:** CANONICAL ADDITIVE STAGE-6 COMPUTATIONAL-CONFIDENCE AMENDMENT
**Effective date:** 2026-09-19
**Cross-stage authority:** P1.11.8
**Sustainability scope:** UNCHANGED
**H4 status:** NOT TESTED

## 1. Quantity origin class

Every material Stage-6 quantity records one or more ordered provenance classes:

~~~text
DIRECT_MEASURED
DIRECT_ACCOUNTED
SIMULATED
ESTIMATED
INFERRED
DERIVED_COMPOSITE
~~~

The origin class does not determine scientific value by itself; it determines the evidence and uncertainty obligations.

## 2. Uncertainty lineage

For a derived quantity:

~~~math
q=f(z_1,\ldots,z_m),
~~~

retain:

~~~math
\boxed{
\mathbb U_q
=
\mathcal P_f
(
\mathbb U_{z_1},\ldots,\mathbb U_{z_m};
\text{dependence assumptions}
).
}
~~~

No independence assumption is introduced merely for computational convenience.

## 3. Sustainability scope unchanged

Current admission remains governed by SUSTAINABILITY_ADMISSION_FREEZE_V1 and the P1.11.6 reconciliation.

This amendment changes confidence/provenance, not the sustainability vector.

## 4. Effect-resolution gate

For an intervention contrast \(\Delta q\):

~~~math
\boxed{
G_{\rm resolve}(\Delta q)
}
~~~

must be preregistered for any claim requiring direction, materiality or engineering relevance.

The method may be interval-, set-, probability-, scenario-, sensitivity- or decision-stability-based, consistent with P1.7.

No universal rule of absolute effect greater than a single uncertainty number is imposed.

## 5. Claim boundary

~~~math
\boxed{
\Delta q\text{ computed}
\not\Rightarrow
\Delta q\text{ resolved}
\not\Rightarrow
\text{causal intervention benefit}.
}
~~~

Matched design, causal intervention semantics, uncertainty and validation remain required according to the relevant Stage-6/H4 authority.
