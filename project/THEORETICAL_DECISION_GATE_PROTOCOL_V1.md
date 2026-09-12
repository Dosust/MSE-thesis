# Theoretical Decision Gate — Protocol v1.0

**Status:** FROZEN BEFORE COMPARATIVE SCORING  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Purpose:** determine what an infrastructure dependency/interdependency must contain before changing the frozen thesis ontology or interpreting H1.  
**Permitted final decision:** `RETAIN`, `REVISE`, or `REPLACE`.  
**Current canonical ontology remains unchanged during the gate.**

---

## 0. Governing research rule

```math
\boxed{
\text{No claim without a definition, mechanism, evidence, assumptions, test, and boundary of validity.}
}
```

The gate follows the thesis-wide reasoning protocol:

```math
\boxed{
\text{LEARN}
\rightarrow
\text{VERIFY}
\rightarrow
\text{FORMULATE}
\rightarrow
\text{DERIVE}
\rightarrow
\text{TEST}
\rightarrow
\text{VALIDATE}
\rightarrow
\text{SYNTHESIZE}
\rightarrow
\text{ADVANCE}.
}
```

Every substantive statement is classified as:

```math
[E],\ [D],\ [H],\ [P],\ [A],\ [U].
```

This protocol is upstream of Stages 1–3 and H1. It may recommend a versioned ontology revision, but it may not silently alter `CANONICAL_SYSTEM_DEFINITION.md`, `FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`, `CANONICAL_7_STAGE_FRAMEWORK.md`, or `RESEARCH_HYPOTHESES.md`.

---

# 1. Gate question

```math
\boxed{
\text{What is the minimum sufficient mathematical representation required to describe}
}
```

```math
\boxed{
\text{heterogeneous, directional, dynamic, physical, informational and organizational}
}
```

```math
\boxed{
\text{dependencies between Power and Transportation while preserving domain physics,}
}
```

```math
\boxed{
\text{service consequences, evidence status, and extensibility to additional infrastructures?}
}
```

The gate is a **model/ontology adequacy study**, not a search for the most sophisticated notation.

---

# 2. Competing representations

## `M_0` — frozen thesis baseline

```math
\boxed{M_0:\ \mathcal S=\{P,T,I,O\}}
```

with

```math
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
```

## `M_1` — Phase-0 candidate

```math
\boxed{M_1:\ (\alpha,a)\in\mathcal D\times\mathcal A}
```

with

```math
\mathcal D=\{P,T,W,ICT,\ldots\},
\qquad
\mathcal A=\{Ph,In,Or\}.
```

The candidate is **not presumed superior**.

---

# 3. Gate hypothesis

## Null proposition

```math
\boxed{
H_{0,GATE}:\quad
M_1\text{ provides no necessary representational or engineering capability beyond }M_0.
}
```

## Alternative proposition

```math
\boxed{
H_{1,GATE}:\quad
M_1\text{ resolves at least one material deficiency of }M_0
}
```

without erasing domain physics or introducing unjustified complexity.

This is not automatically a frequentist statistical hypothesis. It becomes statistical only where stochastic outputs and prespecified sampling models exist.

---

# 4. Frozen work sequence

```math
\boxed{
0A\rightarrow0B\rightarrow0C\rightarrow0D\rightarrow0E\rightarrow0F\rightarrow0G
}
```

| Phase | Task | Frozen output | Completion rule |
|---|---|---|---|
| `0A` | terminology/definition register | `INTERDEPENDENCY_DEFINITION_REGISTER.md` | every term has source meaning, thesis meaning, math, boundary, uncertainty |
| `0B` | representation requirements | `REPRESENTATION_REQUIREMENTS_MATRIX.md` | R1–R12 and V1–V5 fixed before scoring |
| `0C` | existing-representation evidence search | theory benchmark evidence table | bounded reproducible search + source-level extraction |
| `0D` | formalize `M_0` and `M_1` | executable/traceable representation specifications | same entities, cases and output semantics |
| `0E` | run V1–V5 | case-level comparison | no representation-specific easier test |
| `0F` | dependency-field ablation | minimum sufficient contract | every retained field earns explanatory/identification/predictive/decision value |
| `0G` | synthesis and decision | `RETAIN`, `REVISE`, or `REPLACE` | frozen decision rule applied without post-result modification |

---

# 5. Phase 0A — definition gate

## Frozen terminology set

```math
\mathcal T=
\{
\text{system},
\text{constituent system},
\text{SoS},
\text{interaction},
\text{interface},
\text{dependency},
\text{interdependency},
\text{coupling},
\text{feedback},
\text{cascade}
\}.
```

For each `T_k`:

```math
\mathcal R_{T_k}
=
(D_k^{source},S_k,D_k^{thesis},M_k,B_k,U_k).
```

The frozen register is `project/INTERDEPENDENCY_DEFINITION_REGISTER.md`.

### 0A acceptance criterion

0A passes only if:

1. source meaning and thesis meaning are visibly separated;
2. no proposed definition is mislabeled as established;
3. boundaries distinguish at least:

```math
\text{interface}
\neq
\text{dependency}
\neq
\text{interdependency}
\neq
\text{coupling operator};
```

4. correlation/common-cause exposure is not silently promoted to dependency/cascade;
5. unresolved terminology is tagged `[U]` rather than invented away.

**0A status at protocol freeze:** COMPLETE FOR v1.0.

---

# 6. Phase 0B — representation requirements gate

The frozen requirement set is

```math
\mathcal R=\{R_1,\ldots,R_{12}\}
```

covering:

```math
\begin{aligned}
R_1 &: \text{constituent-system identity},\\
R_2 &: \text{mechanism explicitness},\\
R_3 &: \text{directionality},\\
R_4 &: \text{information},\\
R_5 &: \text{organization},\\
R_6 &: \text{state dependence},\\
R_7 &: \text{time/delay},\\
R_8 &: \text{feedback/mediated reciprocity},\\
R_9 &: \text{evidence/uncertainty status},\\
R_{10} &: \text{service consequence},\\
R_{11} &: \text{domain-physics preservation},\\
R_{12} &: \text{extensibility/composability}.
\end{aligned}
```

Detailed criteria, non-compensable gates `G1–G5`, scoring definitions and test cases are frozen in `project/REPRESENTATION_REQUIREMENTS_MATRIX.md`.

**0B status at protocol freeze:** COMPLETE FOR v1.0.

---

# 7. Phase 0C — existing-representation evidence study

## 7.1 Scientific purpose

The purpose is not to find papers that resemble our idea. It is to test whether existing theory already satisfies `R_1–R_{12}` and therefore makes `M_1` unnecessary or derivative.

## 7.2 Search families

Use six independent search families:

### `S_C1` — System-of-Systems architecture

Core concepts:

```text
system of systems AND (architecture OR constituent system OR operational independence OR managerial independence)
```

### `S_C2` — infrastructure dependency/interdependency ontology

```text
critical infrastructure AND (dependency OR interdependency) AND (ontology OR representation OR model OR taxonomy OR mechanism)
```

### `S_C3` — multilayer / temporal / network-of-networks representation

```text
infrastructure AND (multilayer OR multiplex OR temporal network OR network of networks) AND (interdependency OR coupling)
```

### `S_C4` — socio-technical / cyber-physical-human representation

```text
infrastructure AND (cyber physical OR socio technical OR human organizational OR information control) AND framework
```

### `S_C5` — architecture / ontology / interoperability

```text
infrastructure AND (architecture description OR ontology OR knowledge representation OR interoperability) AND cross-domain
```

### `S_C6` — dynamic Power–Transportation coupling

```text
(power transportation OR power traffic OR transportation power) AND (dynamic coupling OR interdependency OR EV charging OR V2G) AND model
```

## 7.3 Evidence sources

Primary engineering databases for the formal search:

1. Scopus;
2. Web of Science Core Collection;
3. Compendex;
4. IEEE Xplore.

Standards/foundational authoritative sources may be added outside bibliographic databases when the claim is definitional or architectural, including:

- ISO/IEC/IEEE standards;
- SEBoK/INCOSE;
- NIST;
- original foundational papers.

Web search is discovery/triage support only; it is not a substitute for the frozen database search where systematic coverage is claimed.

## 7.4 Search boundary

Default interval:

```math
\text{database inception}\rightarrow\text{final Phase-0C search date}.
```

No publication-year restriction is imposed unless a search family requires one and the reason is documented before execution.

## 7.5 Inclusion criteria

Include a source when it does at least one of the following:

1. formally defines system/dependency/interdependency architecture;
2. proposes a reusable cross-domain representation;
3. explicitly integrates physical with information/control and/or organization;
4. represents time-varying or state-dependent dependency;
5. maps heterogeneous infrastructure models while preserving domain-specific physics;
6. provides a validated Power–Transportation interdependency representation relevant to `R_1–R_{12}`.

## 7.6 Exclusion criteria

Exclude from the core benchmark when a source:

1. only reports resilience outcomes without a representation object;
2. uses `interdependency` rhetorically without defining/operationalizing it;
3. treats only one infrastructure with no cross-system representation relevance;
4. presents a generic AI/optimization method with no dependency semantics;
5. cannot be checked at source sufficiently to score requirements.

## 7.7 Extraction object

For each eligible representation `M_j`, extract

```math
\boxed{
M_j=
\{
O_j,R_j,D_j,A_j,I_j,O_j^{org},T_j,U_j,Q_j,F_j,V_j,L_j
\}
}
```

where:

- `O_j`: core mathematical/ontological object;
- `R_j`: relation semantics;
- `D_j`: directionality;
- `A_j`: assumptions;
- `I_j`: informational treatment;
- `O_j^{org}`: organizational treatment;
- `T_j`: dynamics/time/delay;
- `U_j`: uncertainty/evidence treatment;
- `Q_j`: service/outcome mapping;
- `F_j`: domain-physics preservation;
- `V_j`: verification/validation evidence;
- `L_j`: limitations/boundary.

## 7.8 Benchmark score

For each method and requirement:

```math
B_{jk}
=
\begin{cases}
0,& M_j\text{ cannot support }R_k,\\
1,& M_j\text{ supports }R_k\text{ only indirectly/ad hoc},\\
2,& M_j\text{ explicitly supports }R_k.
\end{cases}
```

No score is accepted without a source excerpt/page/section or a derivation from the formal model.

## 7.9 Anchor sources already verified for orientation `[E]`

These are **anchors, not the completed 0C corpus**:

- Maier (1998), system-of-systems operational/managerial independence;
- Rinaldi, Peerenboom & Kelly (2001), dependency/interdependency classes;
- Johansson & Hassel (2010), structural/functional interdependency modeling;
- Kivelä et al. (2014), multilayer-network formalism;
- NIST SP 1500-201 / SP 1900-202, cross-domain CPS component/aspect framework;
- ISO/IEC/IEEE 42010:2022, architecture-description viewpoints/model kinds for systems and systems-of-systems;
- Zhao et al. (2025), failure dependence/cascading terminology review.

These anchors prevent rediscovering established concepts but receive no privileged score in the final benchmark.

**0C status at protocol freeze:** PREREGISTERED, NOT YET COMPLETE.

---

# 8. Phase 0D — formalize `M_0` and `M_1`

Both models must encode the **same entities, same scenario, same evidence and same service variables**.

## 8.1 Baseline specification

`M_0` must be represented exactly as the current thesis intends, not as a weakened straw man.

```math
M_0:
\mathcal S=\{P,T,I,O\}
```

with the current Stage-2 interdependency object and Stage-3/4 dynamics preserved.

## 8.2 Candidate specification

`M_1` uses

```math
(\alpha,a)\in\mathcal D\times\mathcal A
```

and a candidate dependency contract

```math
\mathfrak d_e(t)
=
(s_e,r_e,\rho_e,m_e,q_e,M_e,z_e,w_e,\delta_e,c_e,U_e,\mathcal H_{e,t}).
```

No field is accepted as necessary merely because it appears in the tuple.

## 8.3 Fair-comparison rule

If a capability can be added to `M_0` without changing its ontology, that capability must be credited to `M_0` rather than reserved for `M_1`.

This is essential to prevent artificially manufacturing superiority for the candidate.

---

# 9. Phase 0E — frozen verification cases

Use exactly V1–V5 from `REPRESENTATION_REQUIREMENTS_MATRIX.md`:

```math
V_1:\ P^{Ph}\leftrightarrow T^{Ph},
```

```math
V_2:\ T^{In}\rightarrow P^{In}\rightarrow P^{Ph},
```

```math
V_3:\ T^{Or}\rightarrow T^{Ph}\rightarrow P^{Or/Ph},
```

```math
V_4:\ P\rightarrow T\rightarrow P,
```

```math
V_5:\ P+T\rightarrow P+T+W.
```

For every case report:

1. entities represented;
2. relation semantics;
3. governing mechanism;
4. direction;
5. state/time dependence;
6. uncertainty/evidence status;
7. service consequence;
8. extra assumptions;
9. ad hoc exceptions;
10. result for each relevant `R_k`.

A diagram or notation that merely looks clearer is insufficient evidence of superiority.

---

# 10. Phase 0F — dependency-object ablation

The candidate contract is tested incrementally.

Start with

```math
D_0=(s,r)
```

and add one semantically distinct capability at a time:

```math
\begin{aligned}
D_1&=D_0+m,\\
D_2&=D_1+q,\\
D_3&=D_2+z(t),\\
D_4&=D_3+w(t),\\
D_5&=D_4+\delta(t),\\
D_6&=D_5+c(t),\\
D_7&=D_6+\rho,\\
D_8&=D_7+U,\\
D_9&=D_8+\mathcal H_t.
\end{aligned}
```

`M_e` (structural existence/admissibility) is evaluated separately because it may be implicit in whether `e\in\mathcal E` rather than a necessary stored field.

## 10.1 Field value vector

For field `f_k`, record

```math
\Delta V_k
=
\left(
\Delta E_k,
\Delta I_k,
\Delta P_k,
\Delta D_k
\right),
```

where:

- `ΔE_k`: change in explanatory mechanism capability;
- `ΔI_k`: change in identifiability/discrimination of relations;
- `ΔP_k`: change in prediction/trajectory capability where testable;
- `ΔD_k`: change in engineering decision/service consequence.

A field does **not** earn core status merely because it stores useful metadata.

## 10.2 Retention rule

Retain field `f_k` in the **core** dependency grammar only if at least one component of `ΔV_k` is non-zero on a frozen case **and** the effect cannot be obtained from an existing field without semantic ambiguity.

Otherwise:

- move it to optional metadata; or
- remove it entirely.

## 10.3 Identifiability rule

A retained dynamic parameter must also state how it could, in principle, be observed, calibrated, bounded or inferred.

A field that materially improves conceptual description but is not identifiable may remain in the ontology but cannot be promoted into the minimal executable model without an explicit evidence strategy.

---

# 11. Validation ladder

Each result must identify the highest validation level actually reached:

```math
\boxed{
\begin{array}{c}
\text{logical consistency}\\
\downarrow\\
\text{dimensional/semantic consistency}\\
\downarrow\\
\text{mathematical consistency}\\
\downarrow\\
\text{representation verification}\\
\downarrow\\
\text{numerical verification}\\
\downarrow\\
\text{sensitivity/ablation}\\
\downarrow\\
\text{baseline comparison}\\
\downarrow\\
\text{physical plausibility}\\
\downarrow\\
\text{empirical validation}
\end{array}
}
```

Do not call representation completeness `validation` of real infrastructure behavior.

---

# 12. Four validity dimensions

## `V_math` — mathematical validity

Check type/domain/codomain consistency, composition, non-contradiction and preservation of sector-specific governing objects.

## `V_phys` — physical/mechanistic validity

Every accepted dependency must have a defensible mechanism; shared exposure/correlation is not enough.

## `V_epi` — epistemic validity

Separate physical relation state from evidence/confidence about the relation.

```math
\text{physical state}\neq\text{evidence quality}.
```

## `V_eng` — engineering validity

The representation must support

```math
\boxed{\Delta\mathfrak d\rightarrow\Delta X\rightarrow\Delta Q}
```

for at least one frozen case before it can be called an engineering model rather than only a taxonomy.

---

# 13. Complexity audit

For each model:

```math
C(M)
=
\left(
N_{objects},
N_{relation\ classes},
N_{required\ parameters},
N_{assumptions},
N_{ad\ hoc\ exceptions},
N_{external\ formalisms}
\right).
```

No arbitrary weighted scalar is used in v1.0.

A representation that adds structure without resolving a requirement or changing explanation/identification/prediction/decision is penalized qualitatively as unnecessary complexity.

---

# 14. Decision rule — frozen before results

The final decision must be exactly one of:

```math
\boxed{\text{RETAIN}\quad\lor\quad\text{REVISE}\quad\lor\quad\text{REPLACE}.}
```

## RETAIN

Select `RETAIN` when `M_1` adds no necessary capability beyond `M_0`, or added complexity is not justified by a documented deficiency.

## REVISE

Select `REVISE` when components of `M_1` materially improve the current ontology but can be incorporated without replacing the fundamental `P–T–I–O` system identity.

## REPLACE

Select `REPLACE` only if:

1. `M_0` fails at least one non-compensable gate `G1–G5`;
2. the failure cannot be repaired without fundamental ontology change;
3. `M_1` passes all gates on V1–V5 without ad hoc exception;
4. `M_1` preserves distinct domain physics and passes the Water extensibility test;
5. the added complexity is demonstrably necessary.

No final decision may be based only on notation elegance, total score, or novelty preference.

---

# 15. Required result architecture

Every final gate conclusion must use:

```math
\boxed{
\text{CLAIM}
\rightarrow
\text{EVIDENCE}
\rightarrow
\text{MECHANISM}
\rightarrow
\text{MATHEMATICS}
\rightarrow
\text{ASSUMPTIONS}
\rightarrow
\text{TEST}
\rightarrow
\text{RESULT}
\rightarrow
\text{ENGINEERING IMPLICATION}.
}
```

and must answer:

1. What is established?
2. How do we know it?
3. What is only derived/proposed?
4. What failed?
5. What remains uncertain?
6. What would reverse the decision?

---

# 16. Source hierarchy for the gate

Use, in decreasing authority where appropriate to the claim:

1. standards and authoritative systems-engineering definitions;
2. original foundational papers;
3. peer-reviewed systematic/review literature for synthesis;
4. peer-reviewed application studies;
5. project derivations and experiments.

No secondary summary may override an accessible primary source.

---

# 17. Initial verified anchor references

These establish the Phase-0 starting boundary; they do **not** predetermine the final benchmark.

1. Maier, M. W. (1998). *Architecting principles for systems-of-systems*. Systems Engineering, 1(4), 267–284.
2. Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). *Identifying, understanding, and analyzing critical infrastructure interdependencies*. IEEE Control Systems Magazine, 21(6), 11–25.
3. Johansson, J., & Hassel, H. (2010). *An approach for modelling interdependent infrastructures in the context of vulnerability analysis*. Reliability Engineering & System Safety, 95(12), 1335–1344. https://doi.org/10.1016/j.ress.2010.06.010
4. Kivelä, M., et al. (2014). *Multilayer Networks*. Journal of Complex Networks, 2(3), 203–271. https://doi.org/10.1093/comnet/cnu016
5. Griffor, E., Greer, C., Wollman, D. A., & Burns, M. J. (2017). *Framework for Cyber-Physical Systems: Volume 1, Overview*. NIST SP 1500-201. https://doi.org/10.6028/NIST.SP.1500-201
6. NIST SP 1900-202. *Cyber-Physical Systems and Internet of Things* — unified logical/physical/transducing/human component model.
7. ISO/IEC/IEEE 42010:2022. *Software, systems and enterprise — Architecture description*.
8. Zhao, Y., Cai, B., Cozzani, V., & Liu, Y. (2025). *Failure dependence and cascading failures: A literature review and research opportunities*. Reliability Engineering & System Safety, 256, 110766. https://doi.org/10.1016/j.ress.2024.110766

---

# 18. Gate status at v1.0 freeze

| Phase | Status |
|---|---|
| 0A Definitions | **COMPLETE / FROZEN v1.0** |
| 0B Requirements + V1–V5 | **COMPLETE / FROZEN v1.0** |
| 0C Theory benchmark | **PREREGISTERED / NOT YET COMPLETE** |
| 0D Formal comparison | **NOT STARTED** |
| 0E V1–V5 execution | **NOT STARTED** |
| 0F Field ablation | **NOT STARTED** |
| 0G Decision | **BLOCKED UNTIL 0C–0F COMPLETE** |

The canonical thesis remains unchanged until `0G` is reached.
