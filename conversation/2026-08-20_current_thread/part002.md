Using them to construct a new ranking would cause:

\[
\text{old ranking}
\rightarrow
\text{new score}
\rightarrow
\text{“validation” against old ranking},
\]

which is circular.

Therefore:

\[
\boxed{
\frac{\partial S_i}{\partial \text{PriorRank}_i}=0.
}
\]

They are used **only after ranking** for validation.

---

# 2. PRISMA conditions

Every record receives exactly one of four states:

\[
Z_i\in
\{E,M,H,X\}
\]

where:

- \(E\) = eligible substantive paper;
- \(M\) = methods-only;
- \(H\) = manual hold;
- \(X\) = excluded.

### P0 — Canonical identity

Require:

\[
\text{CanonicalID}\neq\varnothing,
\]

\[
\text{Title}\neq\varnothing,
\]

\[
\text{Journal}\neq\varnothing,
\]

\[
\text{URL}\neq\varnothing.
\]

### P1 — Methods papers must not compete with scientific thesis papers

The three papers coded as systematic-review/PRISMA methodology are retained for the thesis methodology but removed from the substantive scientific ranking.

Thus:

\[
\boxed{
C_{\text{protocol}}\Rightarrow Z_i=M.
}
\]

This prevents a PRISMA guideline from becoming the supposed “best mathematical-physics paper.”

### P2 — Critical bibliographic conflicts cannot be guessed

If:

```text
Data_Quality_Notes = CONFLICTING_DOI
```

then:

\[
\boxed{Z_i=H}
\]

until manually resolved.

The frozen dataset currently produces:

- **321 ELIGIBLE**
- **3 METHODS_ONLY**
- **1 HOLD**
- **0 identity exclusions**

### P3 — Missing Authors/Year are not automatic exclusions

The dataset has substantial missingness in these fields.

Therefore missing authors/year must cause:

\[
\boxed{\text{greater uncertainty}}
\]

rather than:

\[
\boxed{\text{automatic rejection}}.
\]

This is crucial because otherwise metadata completeness could be confused with scientific importance.

---

# 3. Six independent ranking criteria

For each eligible paper \(p_i\), define

\[
\mathbf x_i=(x_{i1},\ldots,x_{i6})\in[0,1]^6.
\]

The six dimensions are:

| Criterion | Dataset fields used |
|---|---|
| \(C_1\) Direct relevance | `Relevance_207`, `Relevance_259` |
| \(C_2\) Theory architecture | `Relevant_Hypotheses`, architecture anchors |
| \(C_3\) Disciplinary fit | `Primary_Discipline`, `Discipline_Coverage` |
| \(C_4\) Evidence credibility | verification, evidence stratum, full text, DOI, quality notes |
| \(C_5\) Primary-corpus corroboration | primary 207/259 presence only |
| \(C_6\) Title semantic directness | canonical title only |

The selected 76/141/164 datasets **must not** be used for corroboration because those subsets already embody previous rankings.

---

# 4. Direct-relevance mappings

For `Relevance_207`:

\[
\begin{aligned}
CORE &=1.00\\
STRONG\_APPLIED &=0.86\\
FOUNDATION &=0.78\\
SUPPORTING &=0.58
\end{aligned}
\]

For `Relevance_259`:

\[
\begin{aligned}
A_{\text{CORE DIRECT}} &=1.00\\
B_{\text{FOUNDATIONAL}} &=0.80\\
C_{\text{SUPPORTING}} &=0.58
\end{aligned}
\]

`C_PROTOCOL_SUPPORT` is methods-only.

If both sources classify a paper:

\[
R_i=\frac{R_i^{207}+R_i^{259}}{2}.
\]

Missing classification is represented as an uncertain prior rather than invented evidence.

---

# 5. Thesis architecture conditions

The coded hypothesis dimensions receive the following prior importance:

\[
\boxed{
\mathbf q=(0.11,0.15,0.17,0.15,0.17,0.15,0.05,0.05)
}
\]

corresponding to:

\[
(H1,H2,H3,H4,H5,H6,H7,T1).
\]

The strongest emphasis therefore remains on the thesis's central mathematical architecture:

- dynamic/static-timescale interfaces;
- viability/reachability;
- sustainability/equity;
- recovery/control;
- flood/waste/drainage;
- inverse problems/UQ;
- mathematical reduction/decomposition.

Importantly, a paper is not rewarded indefinitely for simply having more tags. Coverage receives a bounded bonus.

---

# 6. Uncertain evidence must be modeled probabilistically

For paper \(i\), criterion \(c\), define:

\[
\mu_{ic}\in[0,1]
\]

as the estimated criterion center and

\[
\rho_{ic}\in[0,1]
\]

as confidence in that estimate.

Then:

\[
\kappa_{ic}=4+96\rho_{ic}.
\]

Define:

\[
\alpha_{ic}=\tilde{\mu}_{ic}\kappa_{ic},
\]

\[
\beta_{ic}=(1-\tilde{\mu}_{ic})\kappa_{ic},
\]

where

\[
\tilde{\mu}_{ic}=\operatorname{clip}(\mu_{ic},0.01,0.99).
\]

Each simulation samples:

\[
\boxed{
X_{ic}^{(b)}\sim\operatorname{Beta}(\alpha_{ic},\beta_{ic})
}
\]

so verified information has narrow uncertainty while weak or missing evidence has a much wider distribution.

That is substantially stronger than pretending every input score is exact.

---

# 7. Do not use one arbitrary weighting vector

Four weighting regimes are pre-specified.

### Balanced

\[
(0.22,0.22,0.16,0.20,0.06,0.14)
\]

### Theory-first

\[
(0.15,0.30,0.20,0.18,0.04,0.13)
\]

### Evidence-first

\[
(0.18,0.18,0.14,0.32,0.06,0.12)
\]

### Applied/direct

\[
(0.28,0.16,0.12,0.18,0.06,0.20).
\]

For each Monte Carlo realization, first sample a scenario, then:

\[
\boxed{
\mathbf w^{(b)}\sim\operatorname{Dirichlet}(80\mathbf w_s)
}
\]

with

\[
w_c^{(b)}\ge0
\]

and

\[
\sum_{c=1}^{6}w_c^{(b)}=1.
\]

Thus the conclusion cannot depend on one hand-picked set of weights.

---

# 8. Monte Carlo score

For realization \(b\):

\[
\boxed{
S_i^{(b)}=\sum_{c=1}^{6}w_c^{(b)}X_{ic}^{(b)}.
}
\]

Then:

\[
R_i^{(b)}=\operatorname{rank}(-S_i^{(b)}).
\]

The implementation uses:

\[
20\times5,000=\boxed{100,000}
\]

Monte Carlo realizations.

Seed:

\[
\boxed{20260820}.
\]

---

# 9. Do not report only one rank

For every paper compute:

\[
\mathbb E[R_i],
\]

\[
P(R_i=1),
\]

\[
P(R_i\le5),
\]

\[
P(R_i\le10),
\]

\[
P(R_i\le25),
\]

\[
\mathbb E[S_i],
\]

and

\[
\sigma(S_i).
\]

The full rank acceptability is:

\[
\boxed{
b_i^r=\frac1B\sum_{b=1}^{B}\mathbf1\{R_i^{(b)}=r\}
}
\]

for every possible rank \(r\).

---

# 10. Mathematical Monte Carlo precision condition

For a rank probability \(\hat p\),

\[
SE(\hat p)=\sqrt{\frac{p(1-p)}{N}}.
\]

The maximum occurs at:

\[
p=0.5,
\]

giving

\[
\boxed{SE_{\max}=\frac{1}{2\sqrt N}.}
\]

For

\[
N=100,000,
\]

the tested implementation gives:

\[
SE_{\max}=0.001581.
\]

The worst-case 95% half-width is:

\[
1.96SE_{\max}=\boxed{0.003099}.
\]

So rank probabilities are estimated to roughly ±0.31 percentage points in the worst case.

For bounded scores \(S\in[0,1]\), Hoeffding gives:

\[
P(|\bar S-\mathbb E[S]|\ge\epsilon)\le2e^{-2N\epsilon^2}.
\]

At 99% confidence:

\[
\boxed{
\epsilon=\sqrt{\frac{\ln(2/0.01)}{2N}}=0.005147.
}
\]

---

# 11. Convergence conditions

The algorithm is accepted only when:

\[
\text{95\% MC half-width}\le0.005,
\]

\[
\max|\Delta P_{\text{Top10}}|\le0.01
\]

over the final five cumulative batches, and

\[
J_{\text{Top10}}\ge0.80.
\]

The tested run obtained:

\[
\max|\Delta P_{\text{Top10}}|=0.000733,
\]

and

\[
J_{\text{Top10}}=1.00.
\]

Therefore:

\[
\boxed{\text{CONVERGENCE PASS}}
\]

for this implementation.

---

# 12. Definition of “best paper”

Do **not** define the winner as the paper with the largest arbitrary deterministic score.

Use the pre-registered lexicographic rule:

\[
p^*=\arg\min_i\mathbb E[R_i].
\]

Ties are resolved sequentially by:

1. higher \(P(R\le10)\);
2. higher \(P(R=1)\);
3. higher mean Monte Carlo score;
4. lower Monte Carlo score SD;
5. canonical ID.

Thus the meaning of “best” is:

\[
\boxed{\text{most robustly highly ranked paper under the pre-specified model}}
\]

—not “objectively the best paper in existence.”

---

## Tested implementation

The code has already been executed successfully against the exact uploaded 325-paper dataset.

