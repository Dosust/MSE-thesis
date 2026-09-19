# Stage 6 Sustainability Accounting Protocol v1

## 1. Governing accounting structure

\[
\boxed{
\mathbf J_{\rm sus}
=
\left(
\mathbf J_{\rm social},
\mathbf J_{\rm environmental},
\mathbf J_{\rm economic}
\right)
}
\]

with the canonical H4 core:

\[
\boxed{
\mathbf J_{\rm sus}^{core}
=
\begin{bmatrix}
J_{\rm access}\\
J_{\rm energy}\\
J_{\rm carbon}\\
J_{\rm cost}
\end{bmatrix}.
}
\]

The three domains remain separate unless a later Stage-7 value model is explicitly justified.

## 2. Environmental LCA rule

Environmental accounting is ISO-14040/14044-aligned:

\[
\boxed{
\text{goal/scope}
\rightarrow
\text{functional unit}
\rightarrow
\text{inventory}
\rightarrow
\text{impact assessment}
\rightarrow
\text{interpretation}.
}
\]

A formal claim of ISO-conformant LCA requires the actual case study to satisfy the relevant requirements; the design protocol alone does not claim conformity.

## 3. Energy

Lifecycle energy is decomposed rather than hidden in one model term:

\[
\boxed{
J_{\rm energy}
=
E_{\rm materials/manufacture}
+
E_{\rm construction}
+
E_{\rm operation}
+
E_{\rm maintenance}
+
E_{\rm replacement}
+
E_{\rm hazard/repair}
+
E_{\rm EOL}.
}
\]

Credits/recycling substitutions, if used, are separately reported with allocation method.

Do not double-count electricity consumed by both the physical simulation and background LCA inventory.

## 4. Carbon

ISO 14067:2018 is used as the carbon-footprint methodological anchor.

\[
\boxed{
J_{\rm carbon}
=
\sum_{r}
A_r\,EF_r^{CO2e}
}
\]

where \(A_r\) is a physical activity/inventory flow and \(EF_r^{CO2e}\) is a qualified, versioned greenhouse-gas factor.

Decompose:

\[
J_{\rm carbon}
=
C_{\rm embodied}
+
C_{\rm construction}
+
C_{\rm operation}
+
C_{\rm maintenance}
+
C_{\rm repair}
+
C_{\rm replacement}
+
C_{\rm EOL}.
\]

Rules:

1. factors must record source, geography, technology and year;
2. attributional average factors and consequential/marginal factors are not mixed;
3. carbon offsets are not silently subtracted from the physical footprint;
4. grid decarbonization assumptions belong in scenarios/uncertainty;
5. carbon is one environmental impact category, not total sustainability.

For U.S. electricity, EPA eGRID and the EPA GHG Emission Factors Hub are admissible authoritative sources when geographically and methodologically appropriate.

## 5. Extended environmental impacts

When inventory support is adequate, an extended vector may be reported:

\[
\mathbf J_{\rm env}^{ext}
=
[
J_{\rm acid},
J_{\rm eutro},
J_{\rm smog},
J_{\rm health},
J_{\rm ecotox},
J_{\rm water},
J_{\rm resource},
\ldots
]^\top.
\]

EPA TRACI provides characterization factors for several environmental impact categories.

The case protocol must preregister which categories are material to the intervention mechanism and why.

## 6. Accessibility

Accessibility is not defined as traffic speed alone.

For group/origin \(g\) and opportunities \(j\),

\[
\boxed{
A_g(t;a)
=
\sum_j
O_j\,f(c_{gj}(t;a))
}
\]

is an admissible generic location-based structure, where:

- \(O_j\): opportunities/services available at destination \(j\);
- \(c_{gj}\): generalized travel impedance;
- \(f\): preregistered impedance function.

Cumulative-opportunity, gravity-based or utility-based accessibility may be used when justified by the case and data.

Geurs and van Wee (2004) show why accessibility measure selection must reflect theoretical basis, interpretation and data requirements.

## 7. Distributional social consequences

Aggregate accessibility is insufficient.

Report:

\[
\mathbf A(t)
=
[A_1(t),A_2(t),\ldots,A_G(t)]^\top
\]

for declared spatial/population groups when data support this.

Candidate diagnostics include:

\[
A_{\min}(t)=\min_g A_g(t),
\]

\[
\Delta A_{g_1,g_2}(t)=A_{g_1}(t)-A_{g_2}(t),
\]

and a preregistered inequality/distribution index if the distributive principle is independently justified.

The thesis must specify:

1. inequality of what outcome;
2. across which population/spatial units;
3. according to which distributive principle.

This follows the transport-equity logic summarized by Pereira et al. (2017) and subsequent distributional-accessibility research.

## 8. Power-service social consequences

A power-service consequence may be disaggregated by critical/community function only if the mapping is authoritative:

\[
S_{P,g}(t)
=
\frac{
\text{served declared demand for group/function }g
}{
\text{declared demand for }g
}.
\]

No synthetic critical-load weight is relabeled as a community social requirement.

## 9. Lifecycle social assessment

If lifecycle social claims extend beyond operational accessibility/service distribution, use an explicit S-LCA study consistent with ISO 14075:2024 and UNEP 2020.

Relevant stakeholder categories can include workers, consumers/users, local communities, society and value-chain actors, subject to study goal and scope.

Stakeholder inclusion/exclusion must be justified. Vulnerable groups must not be silently excluded because aggregate data are easier to obtain.

## 10. Cost

For perspective \(p\),

\[
\boxed{
J_{\rm cost}^{(p)}(a)
=
C_0^{(p)}
+
\sum_{y=1}^{H_{LC}}
\frac{
C_{op,y}^{(p)}
+
C_{maint,y}^{(p)}
+
C_{repair,y}^{(p)}
+
C_{repl,y}^{(p)}
}{
(1+r_p)^y
}
+
\frac{C_{EOL}^{(p)}}{(1+r_p)^{H_{LC}}}.
}
\]

The discount rate, currency year, inflation convention and cost bearer are frozen prospectively.

ISO 15686-5:2017 requires agreed lifecycle cost scope and analysis period. NIST SP 1197/EDGe$ compares alternatives with status quo and considers co-benefits, co-costs, uncertainty and non-market effects.

## 11. No double counting

If an environmental or social externality is monetized, the monetary term must be flagged so that it is not simultaneously counted as an independent physical burden inside a scalar total.

Default Stage-6 reporting therefore keeps:

\[
\boxed{
\text{cost}
\quad+\quad
\text{physical environmental impacts}
\quad+\quad
\text{social consequences}
}
\]

as separate outputs.

ISO 14008:2019 provides a framework if a later analysis deliberately performs monetary valuation of environmental impacts.

## 12. Weighting and normalization

ISO/TS 14074:2022 explicitly recognizes that weighting involves value choices.

Therefore:

\[
\boxed{
\text{normalization}\neq\text{weighting}\neq\text{physical measurement}.
}
\]

Normalization may be used for visualization or dimensionless comparison only with a declared reference.

No single score is a confirmatory H4 outcome unless its weighting rule was independently justified and frozen before confirmatory results.
