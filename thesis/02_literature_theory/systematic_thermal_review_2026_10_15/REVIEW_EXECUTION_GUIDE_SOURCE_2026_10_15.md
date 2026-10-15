# How to Conduct Your Systematic Literature Review With High Scientific Rigor

For your thesis, the next step is to execute a reproducible systematic review, not simply collect more papers.

Your review should answer Professor Pat Phelan's two questions:

1. What have researchers already demonstrated about extreme-heat effects on thermal interdependencies between power and electrified transportation systems?
2. Which experimental data and modeling methods are scientifically justified for investigating what remains unresolved?

I recommend a systematic evidence map combined with a critical synthesis of physical models and experimental validation.

## 1. Organize the review around your three thesis objectives

| Thesis objective                | Systematic-review question                                                                                        | Required result                                                                        |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| SO1: Identify and qualify       | Which directional thermal mechanisms have been demonstrated between power and electrified transportation systems? | Verified mechanisms, measured states, physical interfaces, and evidence quality        |
| SO2: Model state-time evolution | Which governing equations and modeling methods reproduce thermal behavior and propagation through time?           | Mathematical-model comparison, assumptions, parameters, and validation results         |
| SO3: Quantify consequences      | How do thermal changes affect electrical capability, charging service, transition timing, and mobility service?   | Evidence-supported consequences, critical times, propagation delays, and research gaps |

The current thesis scope is:

\\[ \boxed{ \begin{gathered} \text{Extreme heat}\\\ \downarrow\\\ \text{Thermal physical states}\\\ \downarrow\\\ \text{Capability constraints}\\\ \downarrow\\\ \text{Directional thermal interdependencies}\\\ \downarrow\\\ \text{State-time and service consequences} \end{gathered} } \\]

Do not start with a PINN, grey-box model, or preferred dataset. First determine what physical relationships have been established and what observations would be needed to identify the remaining relationships.

## 2. Follow an eight-phase review workflow

| Phase                      | What to do                                                                                                                    | Required evidence before advancing                                |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 0. Freeze the protocol     | Define research questions, eligibility criteria, review dates, databases, screening process and synthesis rules.              | Written protocol with version and date                            |
| 1. Search systematically   | Search IEEE Xplore, Scopus, Web of Science and Compendex, where accessible. Search experimental-data repositories separately. | Exact search strings, dates, filters, exported results and counts |
| 2. Deduplicate and screen  | Remove duplicate records, then screen titles, abstracts and full texts against predetermined criteria.                        | Inclusion/exclusion decisions and reasons                         |
| 3. Verify original papers  | Read the full PDFs; inspect governing equations, experimental setups, figures, tables and model assumptions.                  | Paper-to-equation and paper-to-claim evidence register            |
| 4. Audit experimental data | Verify whether raw files can actually be opened and whether they contain relevant physical observations.                      | Dataset quality and accessibility assessment                      |
| 5. Compare methods         | Examine how existing physics-only, grey-box and physics-informed ML models were calibrated and tested.                        | Method-comparison matrix                                          |
| 6. Synthesize the findings | Separate established results, inconsistent evidence, unanswered questions and unsupported assumptions.                        | Scientific gap and evidence maps                                  |
| 7. Select the method       | Decide whether the evidence supports physics-only, grey-box or physics-informed ML for a narrowly specified model.            | Justified modeling and validation plan                            |

Use [PRISMA 2020](https://www.prisma-statement.org/prisma-2020) for transparent reporting, [PRISMA-S](https://www.equator-network.org/reporting-guidelines/prisma-s/) for reproducible searches, and [PRESS](https://doi.org/10.1016/j.jclinepi.2016.01.021)

[Download PDF](https://libkey.io/libraries/158/articles/58330356/full-text-file?utm_source=nomad)

&#x20;to review the search strategy for errors and omissions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.prisma-statement.org\&sz=32)

PRISMA statement

+2



## 3. Execute multiple complementary searches

Do not use one restrictive query combining heat + grid + transportation + grey-box + PINN + experimental data. Such a query would omit many relevant physical experiments.

Instead, search these research streams independently:

| Search stream                            | Primary concepts                                                    | What it should retrieve                                                |
| ---------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| L1: Direct thermal interdependencies     | Power distribution + electrified transportation + heat/temperature  | Studies of actual coupled electrical and thermal mechanisms            |
| L2: EV charging thermal physics          | EVSE + thermal derating + ambient temperature                       | Experimental charger behavior and heat-transfer models                 |
| L3: Power equipment thermal physics      | Transformer/distribution equipment + temperature + dynamic rating   | Established transformer/grid thermal equations                         |
| L4: Battery and vehicle thermal behavior | EV battery + electrothermal + charging/driving                      | Battery temperature, charging limits and vehicle-energy studies        |
| L5: Mathematical methods                 | Thermal dynamics + system identification + grey-box + PINN          | Competing model formulations and their validation                      |
| L6: Service consequences                 | Thermal constraints + charging delay + electricity/mobility service | Studies connecting physical degradation to meaningful service outcomes |

For example, an initial Scopus-style query for direct thermal coupling is:

```
TITLE-ABS-KEY(
  (heatwave* OR "extreme heat" OR electrothermal
   OR "thermal derating" OR "ambient temperature")
  AND
  ("electric vehicle" OR EVSE OR
   "charging infrastructure")
  AND
  ("power distribution" OR transformer OR
   "electrical grid")
)
```

This is a proposed search, not a completed database search. Pilot it, assess which known papers it retrieves, then finalize its wording before full execution.

## 4. Establish rigorous inclusion and exclusion decisions

| Include                                                                                            | Exclude from the primary thermal synthesis                                           |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Studies with explicit thermal mechanisms affecting power or electrified transportation             | Generic transportation studies without a relevant thermal mechanism                  |
| Original laboratory or field experiments reporting relevant physical observations                  | Non-relevant temperature correlations without physical or operational correspondence |
| Governing-equation models that can inform the thermal state-time problem                           | Purely decorative network diagrams without operational or mathematical content       |
| Physics-only, grey-box and physics-informed methods with relevant thermal applications             | Unrelated machine-learning performance comparisons                                   |
| Papers reporting unavailable or unsuccessful experimental validation, where relevant to the review | Duplicate journal/preprint versions counted as separate studies                      |

Do not automatically exclude a paper because its raw dataset is unavailable. Such papers may still provide important published evidence; they simply cannot be treated as sources of accessible training data.

Ideally, two people independently screen a pilot sample and resolve disagreements. If the thesis review has only one reviewer, record that limitation and retain a reproducible audit trail.

## 5. Read each original PDF at the equation-and-evidence level

Every important study should answer:

| Question                     | Evidence to extract                                               |
| ---------------------------- | ----------------------------------------------------------------- |
| What was studied?            | Physical system, equipment and study boundary                     |
| What was measured?           | Temperatures, voltage, current, power, SOC, service outcomes      |
| What laws were used?         | Original governing equations, assumptions and boundary conditions |
| What was estimated?          | Parameters, hidden states and model discrepancies                 |
| How was time represented?    | Sampling interval, thermal inertia, thresholds and delays         |
| How was the model validated? | Independent measurements, benchmarks, errors and uncertainty      |
| What data can be accessed?   | Original raw files, measurement metadata, permissions             |
| What remains unproven?       | Limitations and claims not supported by the experiments           |

The key is to distinguish:

\\[ \boxed{ \text{Published model} \neq \text{experimentally validated model} \neq \text{validated coupled-system model} } \\]

## 6. Test experimental-data readiness before selecting Option B

For every candidate dataset, use the following gates:

| Gate | Test                                                                                                                                     |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| D1   | Source identity, metadata and access terms verified                                                                                      |
| D2   | Actual raw files opened; variables and timestamps inspected                                                                              |
| D3   | Units, missing observations, sensors, heat range and physical consistency assessed                                                       |
| D4   | Parameters or states identifiable for a specific model; independent validation feasible                                                  |
| D5   | Physically corresponding power–transport interface and service observations available, with appropriate causal and validation assessment |

For Option B, the essential mathematical test is whether measured inputs and outputs allow identifiable physical parameters to be estimated.

For example:

\\[ C\frac{dT}{dt}=\kappa I^2-G(T-T_a) \\]

The observable dynamics may identify \\(\kappa/C\\) and \\(G/C\\), but not necessarily all three physical parameters independently.

A large dataset does not resolve that identifiability problem automatically.

## 7. Produce a defensible research-gap matrix

The final review should explicitly distinguish three evidence states:

| Research question                                                             | Existing support                                          | Remaining verification                                                        |
| ----------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Is extreme-heat charger derating real?                                        | Published field experiments                               | Transferability across charger types and access to raw measurements           |
| Can transformer temperatures be modeled?                                      | Physics-based, grey-box and PINN studies                  | Validity under the relevant heat/loading conditions                           |
| Can battery thermal behavior be estimated?                                    | Laboratory and vehicle experiments                        | Model scope and heat-regime adequacy                                          |
| Are heat-dependent power–transport interactions experimentally identifiable?  | Component-level evidence and existing coupled simulations | Matched physical-interface observations                                       |
| Can thermal effects be propagated into electricity/mobility-service outcomes? | Partial charging and energy-service evidence              | Actual service measurements and independently tested coupling                 |
| Does grey-box modeling add value?                                             | Strong precedent in component thermal estimation          | Matched evaluation against simpler physics models for your particular problem |

This matrix is an initial research agenda, not a completed systematic-review conclusion.

## 8. Your execution files are ready

Review Protocol — Version 1.0

Defines the five review questions, search streams, eligibility rules, evidence extraction, experimental-data gates and synthesis strategy.

Open systematic review protocol

Systematic Review Execution Tracker

An Excel workbook I created with eight worksheets: START HERE, Search Log, Screening, PDF Evidence, Data Audit, Method Compare, PRISMA and Seed Papers.

It includes proposed search queries, controlled status fields, live operational counts, and eleven known-item search-checking papers.

Download execution tracker (.xlsx)

All database-search entries are explicitly marked NOT RUN. The seed bibliography is marked SEED ONLY, not systematically included. This ensures that no search, paper-screening, or raw-data verification is misrepresented as completed.

## 9. What to do first

The immediate execution sequence is:

1. Have Professor Phelan review the protocol, particularly the scope, research questions and proposed experimental-data requirements.
2. Pilot the six search streams, checking that they retrieve known relevant papers and do not systematically exclude conventional physics or unfavorable model comparisons.
3. Run and export the finalized searches, preserving exact dates, queries, database interfaces, filters and results.
4. Deduplicate and begin independent screening, recording full-text exclusions and unavailable reports.
5. Prioritize original experimental PDFs and dataset verification, starting with the thermal interfaces most relevant to SO1–SO3.

Once that work is complete, the final model decision can be made on evidence rather than preference.

The goal is to give Professor Phelan two scientifically defensible answers: what previous researchers have established, and which observable thermal interdependency your thesis can model and validate with the available experimental evidence.
