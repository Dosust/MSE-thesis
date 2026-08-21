# Mathematical Specification

## 1. Paper-level state

For focal paper $i$:

$$
\mathcal R_i=[K_i,SM_i,M_i,N_i,O_i,P_i,Q_i,R_i,S_i,T_i,\Omega_i,R_{1i},R_{2i},R_{3i},R_{4i},\lambda_i,\Pi_i]
$$

with

$$
\Omega_i=(P_i,F_i,S_i,D_i).
$$

The fundamental research chain is

$$
\boxed{Q_{\mathrm{construction}}\rightarrow P_{\mathrm{engineering}}\rightarrow F_{\mathrm{integration}}\rightarrow S_{\mathrm{sustainability}}\rightarrow D_{\mathrm{decision}}}
$$

---

## 2. Screening gate

$$
G_i^{KLM}=\mathbb{1}[K_i=1\land SM_i=1\land M_i=1]
$$

For binary variables this is equivalent to

$$
G_i^{KLM}=K_iSM_iM_i.
$$

---

## 3. Traceable-alternative correspondence

Do not require exact alternative-set equality. Define

$$
TA_i=\mathbb{1}[\text{engineering and sustainability evidence are traceably matched at alternative level}].
$$

If $TA_i=0$ then

$$
\lambda_i=0.
$$

---

## 4. Linkage / integration score

$$
\lambda_i=
\begin{cases}
0,&P_i=\varnothing\lor S_i=\varnothing\lor TA_i=0\lor\text{no usable relationship},\\
1,&TA_i=1\land P_i\parallel S_i,\\
2,&P_i\rightarrow S_i\text{ through a directional analytical coupling},\\
3,&\text{author-implemented integrated decision architecture}.
\end{cases}
$$

Examples of $\lambda=2$:

$$
GWP_i^{annual}=\frac{GWP_i^{life}}{SL_i}
$$

or

$$
P_i\ge P_{min}\Rightarrow i\in\mathcal A_{sustainability}.
$$

Examples of $\lambda=3$:

$$
I_i=f(P_i,E_i,C_i,S_i),
$$

$$
I_i=\sum_{j=1}^{m}w_jz_{ij},
$$

$$
I_i=\sum_{j=1}^{m}w_jV_j(x_{ij}),
$$

$$
Hazard\rightarrow Response\rightarrow Damage\rightarrow Loss\rightarrow\{Cost,Downtime,CO_2\},
$$

or

$$
x^*=\arg\min_x F(P(x),S(x)).
$$

A reviewer-reconstructed relation cannot by itself establish $\lambda=3$.

---

## 5. Perfect methodological vector

Define

$$
\mathbf X_i=(R_{1i},R_{2i},R_{3i},R_{4i},\lambda_i).
$$

Perfect status is conjunctive:

$$
\boxed{
\Pi_i=\mathbb{1}[R_{1i}=3\land R_{2i}=3\land R_{3i}=3\land R_{4i}=3\land\lambda_i=3]
}
$$

Equivalently, with all scores bounded in $[0,3]$:

$$
\Pi_i=1\iff\mathbf X_i=(3,3,3,3,3).
$$

---

## 6. Tier-A rule

Tier A is broader than perfect status:

$$
A_i=\mathbb{1}[R_{1i}=3\land R_{2i}\ge2\land R_{3i}=3\land R_{4i}=3\land\lambda_i\ge2].
$$

Therefore Tier-A vectors are

$$
(3,2,3,3,2),\;(3,2,3,3,3),\;(3,3,3,3,2),\;(3,3,3,3,3).
$$

Only the final vector is perfect.

---

## 7. Optional extended routes retained from prior protocol

If the broader analytical corpus is revisited, explicit non-compensatory routes are:

$$
B1_i=\mathbb{1}[R_1=3\land R_2\ge2\land R_3=3\land R_4=3\land\lambda=1],
$$

$$
B2_i=\mathbb{1}[R_1=3\land R_2\ge2\land R_3=2\land R_4=3\land\lambda\ge2],
$$

$$
B3_i=\mathbb{1}[R_1=3\land R_2\ge2\land R_3=3\land R_4=2\land\lambda\ge2].
$$

Eligibility remains route-based rather than total-score based.

---

## 8. R2 supporting coverage statistic

For method-specific applicable component $j$, define

$$
a_{ij}\in\{0,0.5,1\},
$$

where 0 = not reported, 0.5 = partially reported, and 1 = adequately reported.

Then

$$
RC_i=\frac{\sum_{j\in A_i}a_{ij}}{|A_i|}.
$$

Important:

$$
\boxed{RC_i\text{ supports R2 but does not mechanically determine R2.}}
$$

R2 is assigned using method-family essential components.

Examples:

$$
E_{LCA}=\{FU,SB,INV,DataSource,ImpactMethod,Procedure\},
$$

$$
E_{MCDA}=\{Alternatives,Criteria,Weights,Normalization,Aggregation,DecisionRule\},
$$

$$
E_{OPT}=\{DecisionVariables,Objectives,Constraints,Model,Solver/Search,DecisionRule\},
$$

$$
E_{ML}=\{Dataset,Predictors,Target,Model,Training,Validation\}.
$$

---

## 9. Evidence-coverage matrix

For paper $i$ and category $j$:

$$
e_{ij}=\begin{cases}
1,&\text{direct focal-paper implementation/generation (`**`)},\\
0.5,&\text{mentioned/discussed/secondary (`*`)},\\
0,&\text{not identified}.
\end{cases}
$$

Category coverage across $n$ papers:

$$
\boxed{C_j=\frac{1}{n}\sum_{i=1}^{n}e_{ij}}
$$

For $n=10$:

$$
C_j=\frac{N_j^{**}+0.5N_j^*}{10}.
$$

Group coverage for group $g$ with $m_g$ categories:

$$
GC_g=\frac{1}{m_g}\sum_{j\in g}C_j.
$$

Coverage measures presence/provenance, not quality:

$$
e_{ij}=1\not\Rightarrow R=3.
$$

---

## 10. Mapping matrices

### Performance family to integration mechanism

For performance family $p$ and mechanism $f$:

$$
M^{PF}_{pf}=\sum_{i=1}^{n}\mathbb{1}[paper_i\text{ directly implements }P_p\rightarrow F_f].
$$

Normalized:

$$
\widetilde M^{PF}_{pf}=\frac{M^{PF}_{pf}}{n}.
$$

### Integration mechanism to sustainability outcome

$$
M^{FS}_{fs}=\sum_{i=1}^{n}\mathbb{1}[paper_i\text{ directly implements }F_f\rightarrow S_s].
$$

$$
\widetilde M^{FS}_{fs}=\frac{M^{FS}_{fs}}{n}.
$$

### Sustainability outcome to decision

Optional third mapping:

$$
M^{SD}_{sd}=\sum_i\mathbb{1}[S_s\rightarrow D_d].
$$

The full empirical architecture is therefore

$$
P\rightarrow F\rightarrow S\rightarrow D.
$$

---

## 11. Accuracy invariant

Let $C$ be all substantive claims exported and $E\subseteq C$ the claims with explicit source support. The desired output invariant is

$$
\boxed{\frac{|E|}{|C|}=1}
$$

meaning 100% of exported substantive paper-specific claims must be source-supported. This does not claim infallible PDF parsing; uncertainty must be retained as `U`/`NR` rather than filled by inference.

---

## 12. Logical consistency invariants

The implementation must enforce:

$$
SM=0\Rightarrow R_1\neq3,
$$

$$
M=0\Rightarrow R_4\neq3,
$$

$$
R_3=3\Rightarrow AuthorGeneratedP=True,
$$

$$
R_4=3\Rightarrow MethodGeneratedS=True,
$$

$$
\lambda>0\Rightarrow TA=1,
$$

$$
\lambda=3\Rightarrow AuthorIntegratedArchitecture=True,
$$

and

$$
\Pi=1\Rightarrow\mathbf X=(3,3,3,3,3).
$$