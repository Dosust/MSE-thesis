# Formal Novelty Search Protocol F0/F1/F2 v1.0

**Date frozen:** 2026-09-16  
**Status:** QUERY LOGIC AND DATABASE TRANSLATIONS FROZEN; AUTHENTICATED EXECUTION PENDING  
**Purpose:** close the global novelty gate for the narrowed candidates after public falsification  
**Method:** EGMIV + FTEE; search is designed to find disconfirming/overlapping prior art rather than maximize support for the thesis

## 1. Search authority and field verification

Current official documentation was checked on 2026-09-16:

- Scopus Advanced Search: Elsevier Scopus Support, `https://service.elsevier.com/app/answers/detail/a_id/11365/supporthub/scopus/`.
- Web of Science Core Collection: Clarivate field tag `TS=` searches Title, Abstract, Author Keywords and Keywords Plus, `https://webofscience.help.clarivate.com/Content/wos-core-collection/woscc-search-field-tags.htm`.
- Compendex / Engineering Village: `Subject/Title/Abstract` is searched with `WN KY`, current Elsevier Support page `https://www.elsevier.support/engineering-village/answer/what-are-the-search-fields-in-the-compendex-database`.
- IEEE Xplore Command Search: supports metadata fields such as `"Document Title":` and `"Abstract":`, Boolean operators and command search; `https://xplorestaging.ieee.org/Xplorehelp/searching-ieee-xplore/command-search`.

Database syntax must be rechecked if the platforms change before execution.

## 2. General rules

```math
\boxed{\text{Discovery aims to falsify the residual novelty claim.}}
```

Rules:

1. database inception to final search date unless a narrower range is preregistered;
2. no paper is excluded because it studies a sector other than P–T if its mathematics directly addresses the candidate object;
3. reviews identify terminology and anchors but do not replace primary-method papers;
4. backward/forward citation chasing begins only after database anchors are qualified;
5. exact search date, database version/interface, query, result count and export filename are preserved;
6. all raw exports are retained unchanged before deduplication;
7. eligibility is based on content, not whether the paper supports the thesis;
8. negative/overlapping prior art has the same evidence priority as supporting evidence.

---

# F0 — mechanistic dependency/interface representation

## F0 research question

```math
\boxed{
\text{Does prior work already provide a reusable evidence-qualified directed dependency/interface representation}
\\
\text{with explicit causal semantics, context/activation, uncertainty/provenance and executable composition into heterogeneous infrastructure dynamics?}
}
```

## F0 concept blocks

```text
A0 — infrastructure domain
("critical infrastructure*" OR "interdependent infrastructure*" OR
 "infrastructure system*" OR "infrastructure network*" OR "system* of systems")

B0 — dependency/interface
(dependenc* OR interdependenc* OR coupling OR interface* OR "functional dependency")

C0 — dynamic/causal semantics
(causal OR mechanis* OR dynamic OR "state-dependent" OR "time-varying" OR
 hybrid OR delay* OR activation OR mode*)

D0 — formal representation
(model* OR represent* OR formal* OR ontology OR grammar OR compositional OR provenance OR uncertainty)
```

Primary discovery:

```math
Q_{F0}^{CORE}=A0\land B0\land C0.
```

Diagnostic precision query:

```math
Q_{F0}^{FORMAL}=A0\land B0\land C0\land D0.
```

The FORMAL query cannot replace CORE because requiring representation terminology could hide relevant methods.

## F0 database translations

### Scopus

```text
TITLE-ABS-KEY(
  ("critical infrastructure*" OR "interdependent infrastructure*" OR
   "infrastructure system*" OR "infrastructure network*" OR "system* of systems")
  AND
  (dependenc* OR interdependenc* OR coupling OR interface* OR "functional dependency")
  AND
  (causal OR mechanis* OR dynamic OR "state-dependent" OR "time-varying" OR
   hybrid OR delay* OR activation OR mode*)
)
```

### Web of Science Core Collection

```text
TS=(
  ("critical infrastructure*" OR "interdependent infrastructure*" OR
   "infrastructure system*" OR "infrastructure network*" OR "system* of systems")
  AND
  (dependenc* OR interdependenc* OR coupling OR interface* OR "functional dependency")
  AND
  (causal OR mechanis* OR dynamic OR "state-dependent" OR "time-varying" OR
   hybrid OR delay* OR activation OR mode*)
)
```

### Compendex Expert Search

```text
(("critical infrastructure*" OR "interdependent infrastructure*" OR
  "infrastructure system*" OR "infrastructure network*" OR "system* of systems")
 AND
 (dependenc* OR interdependenc* OR coupling OR interface* OR "functional dependency")
 AND
 (causal OR mechanis* OR dynamic OR "state-dependent" OR "time-varying" OR
  hybrid OR delay* OR activation OR mode*)) WN KY
```

If Engineering Village rejects wildcard use inside exact phrases, execute the platform-valid equivalent with phrase-level truncation expanded explicitly and record the translation amendment before screening.

### IEEE Xplore

IEEE Command Search term limits make a single monolithic translation fragile. Execute a union of narrower metadata searches, including at least:

```text
("Abstract":"interdependent infrastructure" OR "Abstract":"critical infrastructure")
AND
(dependency OR interdependency OR coupling OR interface)
AND
(causal OR mechanism OR dynamic OR hybrid OR delay)
```

and a second query focused on state/context semantics:

```text
("Abstract":"infrastructure system" OR "Abstract":"infrastructure network")
AND
(dependency OR interdependency OR interface)
AND
("state-dependent" OR "time-varying" OR activation OR mode)
```

The raw union is deduplicated after export.

---

# F1 — partial observation / inference to viability

## F1 research question

```math
\boxed{
\text{Has infrastructure research already propagated observation/state-estimation uncertainty into controlled viability,}
\\
\text{safe-set/reachability diagnostics or equivalent future-maintainability decisions?}
}
```

## F1 concept blocks

```text
A1 — infrastructure domain
("critical infrastructure*" OR "infrastructure system*" OR
 "infrastructure network*" OR power OR transportation OR energy OR mobility)

B1 — viability / invariant safety
("viability kernel" OR "viable set" OR "controlled invariance" OR
 "invariant set" OR reachability OR "reach-avoid" OR "safe set")

C1 — partial observation / state inference
("state estimation" OR "partial observability" OR "partially observed" OR
 Bayesian OR posterior OR belief OR filter* OR "measurement uncertainty" OR
 "observation uncertainty" OR "estimation error")
```

Primary discovery:

```math
Q_{F1}^{CORE}=A1\land B1\land C1.
```

A separate cross-domain control-theory search without `A1` is mandatory for conceptual prior art:

```math
Q_{F1}^{CONTROL}=B1\land C1.
```

This prevents a false novelty claim caused by infrastructure-specific vocabulary.

## F1 database translations

### Scopus

```text
TITLE-ABS-KEY(
  ("critical infrastructure*" OR "infrastructure system*" OR "infrastructure network*" OR
   power OR transportation OR energy OR mobility)
  AND
  ("viability kernel" OR "viable set" OR "controlled invariance" OR "invariant set" OR
   reachability OR "reach-avoid" OR "safe set")
  AND
  ("state estimation" OR "partial observability" OR "partially observed" OR Bayesian OR
   posterior OR belief OR filter* OR "measurement uncertainty" OR "observation uncertainty" OR
   "estimation error")
)
```

### Web of Science Core Collection

```text
TS=(
  ("critical infrastructure*" OR "infrastructure system*" OR "infrastructure network*" OR
   power OR transportation OR energy OR mobility)
  AND
  ("viability kernel" OR "viable set" OR "controlled invariance" OR "invariant set" OR
   reachability OR "reach-avoid" OR "safe set")
  AND
  ("state estimation" OR "partial observability" OR "partially observed" OR Bayesian OR
   posterior OR belief OR filter* OR "measurement uncertainty" OR "observation uncertainty" OR
   "estimation error")
)
```

### Compendex

```text
(("critical infrastructure*" OR "infrastructure system*" OR "infrastructure network*" OR
  power OR transportation OR energy OR mobility)
 AND
 ("viability kernel" OR "viable set" OR "controlled invariance" OR "invariant set" OR
  reachability OR "reach-avoid" OR "safe set")
 AND
 ("state estimation" OR "partial observability" OR "partially observed" OR Bayesian OR
  posterior OR belief OR filter* OR "measurement uncertainty" OR "observation uncertainty" OR
  "estimation error")) WN KY
```

### IEEE Xplore

Run multiple metadata queries if needed to respect clause/term limits, including:

```text
("Abstract":"viability kernel" OR "Abstract":"controlled invariance" OR "Abstract":"reachability")
AND
("state estimation" OR "partial observability" OR "partially observed" OR belief OR posterior)
AND
(infrastructure OR power OR transportation OR energy)
```

and

```text
("Abstract":"safe set" OR "Abstract":"reach-avoid")
AND
("state estimation" OR "estimation error" OR "measurement uncertainty")
AND
(infrastructure OR power OR transportation)
```

---

# F2 — dependency-mechanism sensitivity of viability

## F2 research question

```math
\boxed{
\text{Has prior work ranked infrastructure dependencies/interfaces using perturbations of mechanism parameters}
\\
\text{and their effect on a controlled viability/safe-set functional, with intervention validation?}
}
```

## F2 concept blocks

```text
A2 — infrastructure/network domain
("critical infrastructure*" OR "interdependent infrastructure*" OR
 "infrastructure network*" OR "infrastructure system*" OR network*)

B2 — viability geometry/safety set
("viability kernel" OR "viable set" OR "controlled invariance" OR
 "safe set" OR reachability OR "distance to boundary" OR "geometric robustness")

C2 — sensitivity/criticality
(sensitiv* OR critical* OR ranking OR perturb* OR derivative OR robustness OR importance)

D2 — dependency/interface mechanism
(dependenc* OR interdependenc* OR interface* OR coupling OR edge* OR parameter*)
```

Primary discovery:

```math
Q_{F2}^{CORE}=A2\land B2\land C2.
```

Interface-specific diagnostic:

```math
Q_{F2}^{INTERFACE}=A2\land B2\land C2\land D2.
```

## F2 database translations

### Scopus

```text
TITLE-ABS-KEY(
  ("critical infrastructure*" OR "interdependent infrastructure*" OR
   "infrastructure network*" OR "infrastructure system*" OR network*)
  AND
  ("viability kernel" OR "viable set" OR "controlled invariance" OR
   "safe set" OR reachability OR "distance to boundary" OR "geometric robustness")
  AND
  (sensitiv* OR critical* OR ranking OR perturb* OR derivative OR robustness OR importance)
)
```

### Web of Science Core Collection

```text
TS=(
  ("critical infrastructure*" OR "interdependent infrastructure*" OR
   "infrastructure network*" OR "infrastructure system*" OR network*)
  AND
  ("viability kernel" OR "viable set" OR "controlled invariance" OR
   "safe set" OR reachability OR "distance to boundary" OR "geometric robustness")
  AND
  (sensitiv* OR critical* OR ranking OR perturb* OR derivative OR robustness OR importance)
)
```

### Compendex

```text
(("critical infrastructure*" OR "interdependent infrastructure*" OR
  "infrastructure network*" OR "infrastructure system*" OR network*)
 AND
 ("viability kernel" OR "viable set" OR "controlled invariance" OR
  "safe set" OR reachability OR "distance to boundary" OR "geometric robustness")
 AND
 (sensitiv* OR critical* OR ranking OR perturb* OR derivative OR robustness OR importance)) WN KY
```

### IEEE Xplore

Use a union of bounded command searches such as:

```text
("Abstract":"viability kernel" OR "Abstract":"controlled invariance" OR "Abstract":"safe set")
AND
(sensitivity OR criticality OR ranking OR perturbation)
AND
(infrastructure OR network OR dependency OR interface)
```

and

```text
("Abstract":"distance to boundary" OR "Abstract":"geometric robustness" OR "Abstract":reachability)
AND
(sensitivity OR perturbation OR criticality)
AND
(infrastructure OR network OR interface)
```

---

# 3. Screening criteria

## Include

A record enters full-text qualification if it materially addresses at least one of:

```text
F0: formal/dynamic/causal dependency semantics or interface composition;
F1: observation/state-estimation uncertainty coupled to viability/safety/reachability decisions;
F2: viability/safe-set geometry or sensitivity used to rank mechanisms/components/interfaces or interventions.
```

## Exclude

Exclude after recording reason when the paper:

```text
uses “resilience” or “viability” only colloquially;
contains correlation/common-hazard exposure without dependency semantics for F0;
reports uncertainty only as post-hoc error bars for F1;
uses network centrality without any viability/safe-set/reachability object for F2;
is purely conceptual and contains no method relevant to the candidate mathematical object, unless needed for terminology provenance.
```

## Rival evidence

A paper that provides a closer or superior prior formulation is a priority inclusion, not an exclusion.

---

# 4. Required export fields

For every database export preserve, where available:

```text
stable database ID;
DOI;
title;
authors;
year;
source;
abstract;
author keywords;
indexed keywords/controlled terms;
affiliations;
references;
citation counts only as metadata, never quality proof;
document type;
search query ID;
search date.
```

Raw export files must be immutable provenance inputs.

---

# 5. Deduplication and evidence extraction

After unioning database results:

```math
\mathcal P_{Fj}^{raw}
\rightarrow
\text{identity-preserving deduplication}
\rightarrow
\text{title/abstract screening}
\rightarrow
\text{full-text screening}
\rightarrow
\text{FTEE extraction}.
```

FTEE records must extract source notation before mapping to thesis notation.

---

# 6. Novelty adjudication rule

For each residual `N_j'`, classify:

```text
FALSIFIED_EQUIVALENT — an equivalent prior method/integration is demonstrated;
NARROWED — prior art overlaps materially but a narrower testable residual remains;
UNRESOLVED — evidence insufficient to decide;
DISTINCT_WITHIN_DOMAIN — no equivalent found within the completed qualified search domain.
```

`DISTINCT_WITHIN_DOMAIN` is not phrased as “the first ever” unless the evidence actually supports that stronger statement.

---

# 7. Execution block

```math
\boxed{
\text{QUERY DESIGN}=\text{FROZEN},
\qquad
\text{AUTHENTICATED DATABASE EXECUTION}=\text{BLOCKED\_EXTERNAL\_ACCESS}.
}
```

When authenticated access becomes available, execute exactly these queries or document any platform-required syntax amendment before inspecting the resulting corpus.
