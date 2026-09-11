# Fresh Evidence Search Governance Change

**Date:** 2026-09-11  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Decision type:** evidence-search methodology change  
**Scientific effect:** changes the evidence-discovery universe; does not change the frozen seven-stage framework or frozen $H_1$–$H_5$ hypothesis logic

---

## Decision

The frozen 325-paper corpus no longer defines the primary evidence base for the thesis hypotheses or demonstrator.

The governing rule is now

```math
\textbf{New scientific question}
\Rightarrow
\textbf{new evidence search from first principles}.
```

Primary evidence selection must begin from fresh, reproducible, hypothesis-specific database searches. Memory, previous rankings, and previously selected papers may support recognition or later coverage diagnostics but cannot determine inclusion.

---

## Primary workflow

```math
H_i
\rightarrow
\text{mechanisms/constructs}
\rightarrow
\text{search concepts}
\rightarrow
\text{database searches}
\rightarrow
\text{screening}
\rightarrow
\text{full-text eligibility}
\rightarrow
\mathcal P_{\rm eligible}^{\rm NEW}
\rightarrow
\text{FTEE}
\rightarrow
\mathfrak M_{\rm required}
\rightarrow
\text{candidate demonstrators}
\rightarrow
\mathcal M_D^*.
```

Previously known and unknown papers are equivalent during screening:

```math
P_{\rm known}\equiv P_{\rm unknown}.
```

---

## 325-paper corpus

The old corpus is retained as a methodological/provenance artifact and secondary coverage audit only.

After the fresh search:

```math
\mathcal P_{\rm NEW}\cap\mathcal P_{325}
```

measures overlap, while

```math
\mathcal P_{325}\setminus\mathcal P_{\rm NEW}
```

identifies previously known papers not recovered by the new search.

A missing old paper triggers search diagnostics, not automatic inclusion.

---

## Files changed

- created `project/FRESH_HYPOTHESIS_EVIDENCE_SEARCH_PROTOCOL.md`;
- changed `project/CLOSED_CORPUS_EVIDENCE_SELECTION_PIPELINE.md` from primary evidence-selection methodology to secondary coverage audit;
- synchronized `project/README.md`;
- synchronized root `README.md`;
- synchronized `PROJECT_MEMORY.md`.

The current authority is the fresh-search protocol. Any older statement that the 325-paper ranking is the primary entry condition for evidence extraction is superseded by this decision.

---

## Immediate next step

Before executing any new search, freeze the database-specific search strings, searchable construct decomposition for $H_1$–$H_5$, search fields/dates, deduplication rules, inclusion/exclusion criteria, screening forms, citation-chasing rules, amendment procedure, and PRISMA accounting schema.
