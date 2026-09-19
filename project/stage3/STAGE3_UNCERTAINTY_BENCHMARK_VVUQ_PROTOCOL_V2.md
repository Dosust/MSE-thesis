# Stage 3 — Uncertainty, Benchmark and VVUQ Protocol v2

**Status:** CANONICAL STAGE-3 VVUQ DESIGN PROTOCOL  
**Effective date:** 2026-09-19  
**Purpose:** freeze uncertainty classes, benchmark roles, verification/validation boundaries and H1 evidential requirements before confirmatory execution.  
**Empirical closure:** NOT IMPLIED.

## 1. Core distinction

\`\`\`math
\boxed{
\text{verification}
\neq
\text{validation}
\neq
\text{uncertainty quantification}
\neq
\text{H1 adjudication}.
}
\`\`\`

A verified implementation may still be invalid for its intended physical use.

## 2. Stage-3 uncertainty object

\`\`\`math
\boxed{
\mathbb U_3
=
(
U_\theta,
U_{IC},
U_\eta,
U_{\mathbb I},
U_M,
U_N
).
}
\`\`\`

### \(U_\theta\)
Physical/operational parameter uncertainty.

### \(U_{IC}\)
Initial physical state/topology/mode uncertainty.

### \(U_\eta\)
Hazard/environmental forcing uncertainty.

### \(U_{\mathbb I}\)
Dependency mapping, activation, response-law, delay and applicability uncertainty.

### \(U_M\)
Alternative plausible model structures/equations/closures.

\`\`\`math
\boxed{
U_M\neq U_\theta.
}
\`\`\`

### \(U_N\)
Discretization, solver, event-detection, synchronization and finite-sampling uncertainty.

## 3. Aleatory/epistemic status

Each source must be tagged:

\`\`\`text
ALEATORY
EPISTEMIC
MIXED
UNRESOLVED
\`\`\`

according to scientific meaning, not computational convenience.

An epistemic unknown does not become aleatory merely because a probability distribution is convenient.

## 4. Uncertainty registry

Every influential source must record:

\`\`\`text
uncertainty_id
owner
quantity
meaning
unit
aleatory/epistemic/mixed status
source/provenance
representation
distribution/bounds/ensemble if justified
dependence/correlation assumptions
validity domain
propagation method
sensitivity method
validation/revision evidence
status
\`\`\`

## 5. Probability firewall

Probability may be used only with justified probabilistic semantics. Otherwise use interval, set, scenario, ensemble and sensitivity language.

\`\`\`math
\boxed{
\text{scenario coverage}\neq\text{probability}.
}
\`\`\`

## 6. UQ sequence

\`\`\`math
\boxed{
\text{uncertainty registry}
\rightarrow
\text{screening}
\rightarrow
\text{global sensitivity}
\rightarrow
\text{propagation}.
}
\`\`\`

Existing Morris/Sobol methods remain candidate implementation tools, not universal requirements.

## 7. Benchmark ladder

\`\`\`math
\boxed{
B_{3,0}
\rightarrow
B_{3,1}
\rightarrow
B_{3,2}
\rightarrow
B_{3,3}.
}
\`\`\`

### B3,0 — analytic/unit fixtures

Purpose: dimensional identities, conservation identities, exact simple solutions, event/reset fixtures, nested limits, software regression.

Claim ceiling:

\`\`\`text
CODE / MECHANISM VERIFICATION ONLY
\`\`\`

### B3,1 — independent subsystem benchmarks

Purpose: P-model and T-model verification/validation and relevant hazard-response submodels.

Claim ceiling:

\`\`\`text
SUBSYSTEM CREDIBILITY ONLY
\`\`\`

### B3,2 — coupled synthetic benchmark

Purpose: execute ready interfaces against controlled truth; verify sign, units, memory, event order, synchronization and nested limits.

Claim ceiling:

\`\`\`text
COUPLED IMPLEMENTATION / SYNTHETIC VALIDATION
\`\`\`

Not observational real-world validation.

### B3,3 — qualified thesis case

Purpose: evaluate the selected Stage-3 model in the declared case, conduct independent-reference comparison where available, and adjudicate H1 only if confirmatory gates pass.

## 8. Code verification

Required as applicable:

- dimensional/unit tests;
- conservation/balance tests;
- sign tests;
- event/reset logic;
- \(\Phi_e=0\) uncoupled limit;
- \(\gamma_e=0\) inactive limit;
- zero-delay limit;
- deterministic reproducibility;
- configuration/guard tests.

Passing these does not validate real physics.

## 9. Solution verification

Required as applicable:

- timestep refinement;
- spatial/grid/network refinement;
- communication-step refinement;
- event-time sensitivity;
- nonlinear-solver tolerance sensitivity;
- stochastic-sampling convergence.

Numerical acceptance thresholds remain DEFERRED until QOI/context/reference are qualified.

## 10. Subsystem validation

Validation must use independent or appropriately reserved evidence matched to intended context.

Calibration and validation evidence must be distinguished.

Realistic-synthetic source consistency cannot be relabeled as observed utility/transport validation.

## 11. Coupled prediction assessment

A difference between \(M_2\) and \(M_1\) is not evidence of greater accuracy.

With independent qualified reference \(y^R\),

\`\`\`math
E_q^{(M)}
=
d_q(y_q^{(M)},y_q^R),
\`\`\`

\`\`\`math
\Delta E_{21}^{(q)}
=
E_q^{(M_1)}-E_q^{(M_2)}.
\`\`\`

This may support an incremental-information claim only when metric, aggregation and materiality are prospectively frozen.

Without \(y^R\), report

\`\`\`math
\Delta Q_{21}=Q(M_2)-Q(M_1)
\`\`\`

as model divergence/omitted-dynamics effect only.

## 12. H1 adjudication

### SUPPORTED
The valid preregistered test meets the prospectively frozen criterion.

### NOT SUPPORTED
The valid test executes but does not meet the criterion.

### NOT TESTED
A prerequisite/data/VVUQ gate fails.

\`\`\`math
\boxed{
\text{BLOCKED prerequisite}
\not\Rightarrow
\text{H1 falsification}.
}
\`\`\`

## 13. Reference hierarchy

For predictive/explanatory comparison:

1. independent empirical observation;
2. independent higher-fidelity/reference model justified for context;
3. analytical/synthetic truth for benchmark/verification only.

The third cannot be called empirical validation.

## 14. Mechanism/model sensitivity

Assess where material:

- ready-mechanism ablations;
- parameter sensitivity;
- model-family sensitivity;
- numerical-resolution sensitivity.

## 15. UQ convergence

Before confirmatory execution, freeze:

\`\`\`text
monitored statistic/QOI
sample-growth sequence
tolerance/criterion
repeat/bootstrap rule if relevant
stopping rule
\`\`\`

No universal tolerance is authorized here.

## 16. Existing preview fixture

A deterministic preview reproducing committed software values is \(B_{3,0}\) unless evidence elevates it.

\`\`\`text
PREVIEW PASS = SOFTWARE FIXTURE REPRODUCTION
\`\`\`

not H1 evidence.

## 17. Claim ladder

\`\`\`text
Lambda3,0 = specification only
Lambda3,1 = verification
Lambda3,2 = realistic-synthetic developmental evidence
Lambda3,3 = predictive/explanatory comparison
Lambda3,4 = confirmatory H1 adjudication
\`\`\`

## 18. Current empirical status

This protocol does not change current empirical closure. Case, parameter, reference, exact QOI and UQ gates remain unresolved until evidence closes them.

## 19. Claim boundary

This file freezes how credibility will be built. It does not itself verify, validate or confirm the Stage-3 model.
