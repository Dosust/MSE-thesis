# Stage 5 to Stage 6 Handoff Contract v1

Stage 6 may activate only when the accepted Stage-5 diagnosis remains traceable to Stages 1–5.

## Handoff object

\[
\boxed{
I_{5\to6}
=
\left(
\mathfrak M_{1:5},
\mathfrak R_T,
\mathcal D_R,
\mathbb I_{\rm active},
\mathcal U_{\rm feas},
\mathbf U_{1:5},
\mathcal K_{\rm req},
\Lambda_5,
\Omega_5
\right).
}
\]

Where:

- \(\mathfrak M_{1:5}\): traceable model/object lineage;
- \(\mathfrak R_T\): resilience evidence;
- \(\mathcal D_R\): engineering diagnosis;
- \(\mathbb I_{\rm active}\): only Stage-2/3 qualified active physical mechanisms;
- \(\mathcal U_{\rm feas}\): Stage-4 feasible actions;
- \(\mathbf U_{1:5}\): cumulative uncertainty lineage;
- \(\mathcal K_{\rm req}\): service requirement authority;
- \(\Lambda_5\): maximum defensible claim;
- \(\Omega_5\): validity domain.

## Stage-6 readiness questions

The handoff must answer:

\[
\boxed{
\text{WHERE?}
+
\text{WHY?}
+
\text{WHEN?}
+
\text{HOW MUCH?}
+
\text{HOW CERTAIN?}
}
\]

before Stage 6 asks:

\[
\boxed{\text{What should we change?}}
\]

A Stage-5 critical interface is not automatically the Stage-6 intervention target. Stage 6 may instead intervene on a source/receiver component, sensing, information, authority, resources, redundancy or another diagnosed leverage point.

## Activation gate

\[
G_{1:5\to6}
=
G_{1\to2}\land
G_{2\to3}\land
G_{3\to4}\land
G_{4\to5}\land
G_5.
\]

`BLOCKED` means obtain/constitute the missing prerequisite. `FAIL` means return to the earliest invalid stage, amend under change control, re-execute affected downstream work, and re-gate.
