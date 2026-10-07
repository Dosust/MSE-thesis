# Mathematical Framework Specification V2 — Thermal Interdependency State-Time Focus

**Status:** CANONICAL — CURRENT ACTIVE MATHEMATICAL FRAMEWORK  
**Effective date:** 2026-10-07  
**Scope authority:** `CANONICAL_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`  
**Objective authority:** `CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`  
**System-boundary authority:** `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`  
**Supersedes for active mathematical work:** `MATHEMATICAL_FRAMEWORK_SPEC_V1.md`

## 1. Purpose

Formalize only the active thesis question:

> how qualified thermal interdependencies between the Power System and Electrified Transportation System evolve through physical state and time and produce electricity and mobility consequences.

## 2. Extreme-heat forcing

Let

[
H(x,t)
]

denote the external extreme-heat forcing field or time series required by the selected models.

[
H(x,t)
eq X(t).
]

External heat forcing is not itself a system state.

## 3. Thermally active subsystem states

Let

[
X_P^{th}(t)
]

contain only selected Power-system states whose thermal dependence is required by the admitted mechanism.

Let

[
X_{T_e}^{th}(t)
]

contain only selected Electrified-Transportation states whose thermal dependence is required by the admitted mechanism.

The canonical Electrified Transportation System scope remains broader than the activated state model:

[
	ext{system-scope membership}
eq	ext{mandatory detailed state}.
]

## 4. Thermal coupling object

Define

[
Z_{PT}^{th}(t)
]

as the thermally relevant cross-system exchanged quantities, constraints, or interface states needed to represent a qualified directional thermal dependency.

It is a mathematical coupling object, not a third physical infrastructure system.

A relation is admissible only when

[
	ext{thermal state/temperature}
ightarrow
	ext{change in cross-system dependency}
ightarrow
	ext{receiver consequence}
]

is physically and evidentially justified.

## 5. Coupled thermal state

[
X^{th}(t)
=
egin{bmatrix}
X_P^{th}(t)\
Z_{PT}^{th}(t)\
X_{T_e}^{th}(t)
end{bmatrix}.
]

A general active representation is

[
dot X^{th}
=
F_{th}
left(
X^{th},
H,
	heta
ight),
]

or, where direction-specific forms are required,

[
dot X_P^{th}
=
f_P^{th}
left(
X_P^{th},
H,
Z_{PT}^{th};
	heta_P
ight),
]

[
dot X_{T_e}^{th}
=
f_{T_e}^{th}
left(
X_{T_e}^{th},
H,
Z_{PT}^{th};
	heta_T
ight).
]

No universal thermal law is assumed across heterogeneous components.

## 6. Critical thermal transition time

For a thermally relevant state or capability constraint

[
g_i(X_i^{th},H,t)le 0,
]

define

[
	au_i^C
=
inf
left{
t:
g_i(X_i^{th}(t),H(t),t)=0
ight}.
]

The threshold must have physical or operational evidence.

## 7. Thermal-interdependency propagation delay

For an admitted source transition (i) and receiver response (j),

[
delta_{ij}^{th}
=
t_j^{response}
-
	au_i^C.
]

This quantity is used only when the source-to-receiver thermal mechanism is qualified.

[
delta_{ij}^{th}

eq
	ext{graph distance}.
]

## 8. Service consequences

Electricity-service trajectory:

[
Q_P(t)
=
G_P(X^{th}(t)).
]

Mobility-service trajectory:

[
Q_T(t)
=
G_T(X^{th}(t)).
]

If thresholds are required,

[
Q_P(t)ge Q_P^{min},
qquad
Q_T(t)ge Q_T^{min},
]

with thresholds independently justified.

## 9. Directional thermal pathways

### Power → Electrified Transportation

[
X_P^{th}
ightarrow
Z_{PT}^{th}
ightarrow
X_{T_e}^{th}
ightarrow
Q_T.
]

### Electrified Transportation → Power

[
X_{T_e}^{th}
ightarrow
Z_{PT}^{th}
ightarrow
X_P^{th}
ightarrow
Q_P.
]

Reciprocity is not assumed. Each direction requires independent evidence.

## 10. Active outputs

The primary mathematical outputs are:

[
X_P^{th}(t),
quad
X_{T_e}^{th}(t),
quad
Z_{PT}^{th}(t),
quad
	au_i^C,
quad
delta_{ij}^{th},
quad
Q_P(t),
quad
Q_T(t).
]

## 11. Excluded mathematical objects

The active framework does not require:
- generic organizational state;
- generic information-network state;
- broad viability kernels;
- sustainability aggregation;
- SDG mappings;
- economic-development models;
- generic intervention optimization;
- non-thermal dependency states.

Such objects require a future explicit scope amendment before becoming active thesis mathematics.

## 12. Governing discipline

[
oxed{
	ext{minimum sufficient thermal physics}
+
	ext{directional mechanism evidence}
+
	ext{state-time traceability}
}
]

No equation enters the active thesis merely because it is mathematically available.
