# Closed-Corpus 325-Paper Protocol — Secondary Coverage Audit

![Status](https://img.shields.io/badge/status-SECONDARY%20COVERAGE%20AUDIT-9A6700)
![Primary Search](https://img.shields.io/badge/primary%20evidence%20search-FRESH%20FROM%20ZERO-1A7F37)

**Status:** SECONDARY / SUPERSEDED AS PRIMARY EVIDENCE-SELECTION METHOD  
**Corpus:** frozen 325-paper dataset  
**Current role:** post-search coverage audit only  
**Primary search authority:** [`FRESH_HYPOTHESIS_EVIDENCE_SEARCH_PROTOCOL.md`](FRESH_HYPOTHESIS_EVIDENCE_SEARCH_PROTOCOL.md)

The 325-paper PRISMA-style + Monte Carlo protocol remains methodologically useful for corpus-bounded ranking, but it no longer defines the evidence universe for $H_1$–$H_5$ or the demonstrator.

Its legitimate claim remains:

> **highest-priority records within the frozen 325-paper corpus under the declared ranking model.**

It must not be interpreted as establishing the primary thesis evidence base.

---

## 1. Why its role changed

The current scientific questions and demonstrator requirements require a fresh reproducible search from first principles. Therefore

```math
\textbf{new scientific question}
\Rightarrow
\textbf{new evidence search from first principles}.
```

The old corpus cannot be allowed to preselect the papers that support the current hypotheses.

The following are no longer permitted:

```math
H_i
\rightarrow
\text{search only inside }\mathcal P_{325},
```

or

```math
\mathcal P_{325}
\rightarrow
\text{preferred papers}
\rightarrow
\text{demonstrator}.
```

---

## 2. Preserved methodological strengths

The old protocol remains valuable as a bounded methodological artifact because it contains:

- strict single-dataset locking;
- file hash and schema checks;
- duplicate/identity gates;
- anti-leakage rules;
- separation of scientific relevance from evidence confidence;
- explicit missing-data treatment;
- Beta uncertainty on criterion scores;
- Dirichlet uncertainty on ranking weights;
- explicit limitation of claims to the frozen corpus.

These properties may inform later coverage diagnostics or sensitivity analysis, but they do not override the fresh-search protocol.

---

## 3. Current allowed use

After the fresh evidence search produces

```math
\mathcal P_{\rm NEW},
```

compare it with the old corpus using

```math
\mathcal P_{\rm NEW}
\cap
\mathcal P_{325}
```

and

```math
\mathcal P_{325}
\setminus
\mathcal P_{\rm NEW}.
```

The first quantity measures overlap. The second identifies previously known papers not recovered by the new search.

A missing paper triggers a search-diagnostics question, not automatic inclusion:

> Why was this previously important record not recovered?

Possible explanations include incomplete query terms, missing database coverage, indexing differences, or changed relevance to the current hypothesis.

If a true search weakness is discovered, the search protocol is amended and rerun transparently. The paper is not manually inserted merely because it was previously known.

---

## 4. Boundary with FTEE

The old 325-paper ranking does not determine the papers entering FTEE.

The current primary sequence is

```math
H_1-H_5
\rightarrow
\text{fresh database search}
\rightarrow
\text{screening}
\rightarrow
\mathcal P_{\rm eligible}^{\rm NEW}
\rightarrow
\text{FTEE}.
```

Only afterward may the 325-paper corpus be used for coverage auditing.

---

## 5. Governing rule

```math
\textbf{No paper is evidence because it belonged to the frozen 325-paper corpus.}
```

A paper from that corpus enters the new thesis evidence base only if the fresh reproducible search finds it and the new eligibility protocol qualifies it.
