# Top-10 Reference Set

## Status

These ten papers were selected from the adjudicated perfect-score corpus as reference archetypes for distinct engineering–sustainability integration architectures. Their Top-10 ordering is a secondary reference-strength ranking; it does not alter their methodological eligibility.

The working perfect vector for each selected paper is:

```math
(R_1,R_2,R_3,R_4,\lambda)=(3,3,3,3,3)
```

subject always to retained full-text evidence and the frozen definitions in this folder.

---

## 1. CSV ID 245 — Rank 1

**Title:** Linking seismic resilience into sustainability assessment of limited-ductility RC buildings  
**DOI:** `10.1016/j.engstruct.2019.03.021`

**Reference role:** causal physics/structural-response → damage → loss → sustainability architecture.

Representative analytical chain:

```math
Hazard\rightarrow Structural\ Response\rightarrow Damage\rightarrow Loss\rightarrow\{Repair\ Cost,Downtime,Energy/CO_2\}
```

This is the strongest archetype for causal engineering-state-to-sustainability consequence modelling.

---

## 2. CSV ID 241 — Rank 2

**Title:** Low carbon concrete for prefabricated modular construction in circular economy: An integrated approach towards sustainability, durability, cost, and mechanical performances  
**DOI:** `10.1016/j.jobe.2024.109368`

**Reference role:** explicit weighted author-defined integrated performance equation combining engineering and sustainability dimensions.

Reported working form used in prior extraction:

```math
P=0.05(P_m/P_{m0})+0.05(P_f/P_{f0})+0.30(P_{c0}/P_c)+0.30(P_{e0}/P_e)+0.30(P_{CO_2,0}/P_{CO_2})
```

This equation must remain tied to the exact paper evidence when used in final analysis.

---

## 3. CSV ID 232 — Rank 3

**Title:** Experimental characterization of comfort performance parameters and multi-criteria sustainability assessment of recycled textile-reinforced cement facade cladding  
**DOI:** `10.1016/j.jclepro.2022.131900`

**Reference role:** experimentally generated serviceability evidence → MIVES value functions/weights → sustainability index.

Representative chain:

```math
Experimental\ Performance\rightarrow MIVES\ Indicators/Value\ Functions\rightarrow Sustainability\ Index
```

---

## 4. CSV ID 59 — Rank 4

**Title:** Innovative safety framework and direct load–settlement method to optimize vertical subgrade modulus in sustainable mat foundations  
**DOI:** `10.1016/j.eiar.2025.108191`

**Reference role:** geotechnical mechanics → structurally equivalent alternatives → LCSA → NAHP-G/ELECTRE IS decision architecture.

Representative chain:

```math
K_s\ mechanics\rightarrow Equivalent\ foundation\ designs\rightarrow LCSA\ indicators\rightarrow NAHP\text{-}G\rightarrow ELECTRE\ IS\rightarrow Preferred\ design
```

**Taxonomy note:** this paper exposes the current classification issue between `LCSA + outranking` and the broader `Hybrid MCDM` label. Before final matrix freeze, use one unambiguous mapping rule.

---

## 5. CSV ID 124 — Rank 5

**Title:** Integrated environmental, economic, and performance assessments of cold recycling technologies for asphalt pavements  
**DOI:** `10.1016/j.resconrec.2025.108335`

**Reference role:** engineering + environmental + economic indicators → AHP + entropy weighting → TOPSIS integrated ranking.

Representative chain:

```math
\{Engineering,Environmental,Economic\}\rightarrow AHP+EWM\rightarrow TOPSIS\rightarrow Ranking
```

---

## 6. CSV ID 169 — Rank 6

**Title:** Sustainability assessment of granite cutting waste incorporated cement sand rendering mortar: Technical, environmental, cost, and social parameters  
**DOI:** `10.1016/j.jclepro.2024.144108`

**Reference role:** four-domain technical–environmental–economic–social integration into a consolidated sustainability quantity.

Representative chain:

```math
\{Technical,Environmental,Economic,Social\}\rightarrow Normalization/Consolidation\rightarrow Integrated\ Index
```

---

## 7. CSV ID 282 — Rank 7

**Title:** Life cycle sustainable assessment of natural vs artificial lightweight aggregates  
**DOI:** `10.1016/j.jclepro.2022.133064`

**Reference role:** hierarchical LCSA in which technical performance is structurally co-equal with society, economy, and environment.

Representative architecture:

```math
SI=\text{weighted aggregation of normalized social + economic + environmental + technical sub-indices}
```

---

## 8. CSV ID 83 — Rank 8

**Title:** Serviceability parameters and social sustainability assessment of flax fabric reinforced lime-based drywall interior panels  
**DOI:** `10.1016/j.jobe.2023.107406`

**Reference role:** measured thermal/acoustic/post-fire serviceability → MIVES → social sustainability index.

Representative chain:

```math
Measured\ Serviceability\rightarrow MIVES\ Value\ Functions/Weights\rightarrow Social\ Sustainability\ Index
```

---

## 9. CSV ID 23 — Rank 9

**Title:** An integrated energy-emergy approach to building form optimization: Use of EnergyPlus, emergy analysis and Taguchi-regression method  
**DOI:** `10.1016/j.buildenv.2014.10.013`

**Reference role:** simulation → emergy assessment → Taguchi/ANOVA/regression metamodel → building-form optimization.

Prior extracted equation example:

```math
y=-62.43x_1+181.74x_2+166.11x_3-43.13
```

Use exact equation/passage from the focal paper in final evidence tables.

---

## 10. CSV ID 10 — Rank 10

**Title:** Robust decision-making design for sustainable pedestrian concrete bridges  
**DOI:** `10.1016/j.engstruct.2019.109968`

**Reference role:** PCA criterion reduction → kriging/surrogate optimization → robust solution set → AHP decision support.

Representative chain:

```math
Criteria\rightarrow PCA\rightarrow Kriging\ Optimization\rightarrow Robust\ Solutions\rightarrow AHP\ Decision
```

---

## Collective methodological coverage

The Top 10 intentionally span different integration architectures rather than ten variants of one method:

- causal structural-response/damage/loss transformation;
- weighted integrated equation;
- MIVES/value-function integration;
- LCSA + outranking;
- hybrid MCDM;
- consolidated technical-sustainability index;
- hierarchical sustainability index;
- simulation → emergy → regression/metamodel;
- robust/surrogate optimization + decision support.

The set should therefore be analysed as a collection of mathematical/methodological archetypes for the bridge

```math
P_{engineering}\rightarrow F_{integration}\rightarrow S_{sustainability}\rightarrow D_{decision}.
```