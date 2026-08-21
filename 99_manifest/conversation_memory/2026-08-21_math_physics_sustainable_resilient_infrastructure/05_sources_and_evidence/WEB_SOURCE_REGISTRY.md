# Source Registry Used/Discussed in This Conversation

This registry records sources explicitly cited, supplied, or used in the conversation. It is a recall/reproducibility aid and **not a substitute for re-verification before publication**.

## A. Mathematical taxonomy / formal knowledge architecture

### A1. Duke 2002 educational taxonomy — user-supplied

**Source:** `https://sites.math.duke.edu/education/mathnsdl02/math-taxonomy-0202-1web.htm`

**Identity:** "Core Subject Taxonomy for Mathematical Sciences Education" — "Final" Draft, February 2002, proposed by the Mathematical Sciences Conference Group on Digital Educational Resources.

**Verified project interpretation:** an educational browse/catalog taxonomy intended to allow digital libraries/collections to map internal subject taxonomies into a common human-browsable scheme. It is **not** MSC2000/MSC2020 and must not be used as a theorem/prerequisite graph.

Top-level educational categories: Elementary Mathematics; Logic and Foundations; Algebra and Number Theory; Discrete Mathematics; Geometry; Calculus; Analysis; Differential and Difference Equations; Statistics and Probability; Applied Mathematics; Mathematics History.

### A2. MSC2020 — canonical research subject classification

Official/current sources:
- `https://msc2020.org/`
- `https://mathscinet.ams.org/mathscinet/msc/msc2020.html`
- `https://zbmath.org/classification/`

**Verified project interpretation:** MSC2020 is jointly maintained by Mathematical Reviews and zbMATH and is the canonical scholarly research classification layer for this project. Use it for literature/PRISMA subject coding, not as a causal, prerequisite or theorem-dependency graph.

### A3. Knowledge representation stack discussed

The project additionally uses or proposes:
- SKOS / ISO 25964 for controlled concept schemes/thesaurus relations;
- RDF / OWL 2 for typed ontology relations;
- OpenMath for mathematical semantics;
- MathML for mathematical representation;
- OMDoc/MMT for theory/formal dependency structure;
- MaRDI MathModDB for applied mathematical models/formulations/tasks;
- PROV-O for provenance;
- Lean / Isabelle / Rocq / Mizar for formal proof/certification layers.

These are role-separated. A taxonomy category must not be silently converted into a formal dependency relation.

## B. Interdependent infrastructure / resilience

1. Rinaldi, Peerenboom & Kelly (2001), interdependent infrastructures. DOI: `10.1109/37.969131`.
2. Ouyang (2014), review of interdependent infrastructure modelling. DOI: `10.1016/j.ress.2013.06.040`.
3. Buldyrev et al. (2010), catastrophic cascade in interdependent networks. DOI: `10.1038/nature08932`.
4. Gao, Barzel & Barabási (2016), universal resilience patterns in complex networks. DOI: `10.1038/nature16948`.
5. Bruneau et al. (2003), quantitative framework for seismic resilience. DOI: `10.1193/1.1623497`.
6. Hosseini et al. (2016), resilience review. DOI: `10.1016/j.ress.2015.08.006`.
7. Poulin & Kane (2021), resilience/recovery related work. DOI: `10.1016/j.ress.2021.107926`.
8. Mitchell, Bayen & Tomlin (2005), Hamilton–Jacobi reachability. DOI: `10.1109/TAC.2005.851439`.

## C. 2026 frontier papers discussed

9. Zhang et al. (2026), *A people-centric framework for worst-case disruption analysis of interdependent infrastructure systems*, Reliability Engineering & System Safety, Vol. 274. DOI recorded in chat: `10.1016/j.ress.2026.112343`. ScienceDirect PII URL used: `https://www.sciencedirect.com/science/article/pii/S0951832026001596`.
   - conversation takeaway: explicit power/gas/water/road service-to-population mapping; performance-centric and people-centric worst-case conclusions can differ materially.

10. *Hamilton-Jacobi reachability for viability analysis of constrained waste-to-energy systems under adversarial uncertainty* (2026). ScienceDirect PII URL used: `https://www.sciencedirect.com/science/article/pii/S0947358026000543`.
   - conversation takeaway: formal HJ/HJBI viability exists for a moderate-dimensional single-sector WtE setting; this does not establish a general high-dimensional multi-sector identified-interface viability theory.

11. Jiang et al. (2026), recovery-coupling work discussed through Reliability Engineering & System Safety / RePEc. PII referenced: `S0951832026001912`.
   - conversation takeaway: time-varying recovery coupling has been modelled; therefore "recovery coupling has not been modelled" is too broad a novelty claim.

## D. AI / scientific computing / industry

12. Google DeepMind — AlphaEarth Foundations: `https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/`.
13. Google DeepMind — GraphCast: `https://deepmind.google/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/`.
14. Google DeepMind — GenCast: `https://deepmind.google/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/`.
15. Google DeepMind — AlphaEvolve impact: `https://deepmind.google/blog/alphaevolve-impact/`.
16. IEA — Energy and AI: `https://www.iea.org/reports/energy-and-ai/`.
17. IEA — AI for energy optimisation and innovation: `https://www.iea.org/reports/energy-and-ai/ai-for-energy-optimisation-and-innovation`.
18. IEA — energy demand from AI: `https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai`.
19. JTC Singapore — Punggol Digital District sustainability / Open Digital Platform: `https://www.jtc.gov.sg/punggoldigitaldistrict/story-articles/punggol-digital-district-a-blueprint-for-sustainable-mixed-use-development` and `https://www.jtc.gov.sg/about-jtc/news-and-stories/press-releases/first-of-its-kind-open-digital-platform-for-smart-city-solutions-in-punggol-digital-district`.
20. Safe RL for power systems review discussed via arXiv: `https://arxiv.org/abs/2407.00681`.
21. Physics-informed ML infrastructure systematic review discussed via Springer: `https://link.springer.com/article/10.1007/s44163-026-01747-6`.
22. Neural/operator learning review discussed via Annual Reviews: `https://www.annualreviews.org/content/journals/10.1146/annurev-statistics-042424-070908`.

## E. Wolfram design/computational visualization

23. Stephen Wolfram (2020), *Finally We May Have a Path to the Fundamental Theory of Physics… and It’s Beautiful*: `https://writings.stephenwolfram.com/2020/04/finally-we-may-have-a-path-to-the-fundamental-theory-of-physics-and-its-beautiful/`.
24. Wolfram Physics Project Visual Summary: `https://www.wolframphysics.org/visual-summary/`.
25. Wolfram Function Repository — `WolframPhysicsProjectStyleData`: search by exact resource-function name in the Wolfram Function Repository.

## F. Sustainability goals

26. United Nations Sustainable Development Goals: `https://sdgs.un.org/goals/`.
   - infrastructure-related goals discussed include SDG 6, 7, 9, 10, 11, 12 and 13.

## G. Internal authoritative artifacts used to correct this memory archive

The following are not web sources but are important internal provenance anchors:
- `Dossiya_Dakou_MSE_Thesis_Frontier_Integrated_Research_Design_v0.5.pdf` — frozen v0.5 MSE research design; controls executable scope and formal-object semantics.
- `Six_Interacting_Scientific_Chains.drawio` — records that the six chains are distinct analytical logics connected by feedback, not one causal pipeline.
- `Sustainable_Resilience_High_Rigor_Audit.xlsx` — audit/provenance artifact for research rigor and candidate coverage.
- current Figma file `https://www.figma.com/design/Iss9o33vEjRmHaODdkeuc6` — live design state should be checked rather than inferred from stale memory.

## Verification discipline

Before thesis submission, re-check metadata, publication status, authorship, volume/pages, quantitative claims, and exact source semantics against primary sources. A URL being present in this registry does not automatically make every prior conversational statement about it verified.
