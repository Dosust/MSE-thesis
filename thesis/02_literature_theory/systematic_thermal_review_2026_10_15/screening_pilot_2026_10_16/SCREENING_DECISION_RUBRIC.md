# Screening decision rubric — Power–Electrified Transportation extreme-heat literature

**Reviewer modes:** AI-assisted discovery ≠ formal title/abstract screen. The latter records explicit inclusion/uncertainty/exclusion decisions; if performed by only one reviewer, record that limitation; do not silently label AI output as independently double-screened.

**Primary status values**: `CORE_DIRECT` = coupled Power and Electrified Transportation with temperature/heat-conditioned source/interface/receiver; `COMPONENT_POWER` = transformer/line physical heat dynamics; `COMPONENT_TE` = EVSE/cable/rectifier/vehicle heat dynamics relevant to interface; `MATHEMATICS_METHOD` = heat ODE/PDE numerical/PINN or grey-box and real validation; `SERVICE_OR_COUPLING_CONTEXT` = operational services and nonheat P–Tₑ relationships; `EXCLUDE_WITH_REASON` = outside scope; `UNCERTAIN_RETRIEVE_FULLTEXT` = abstract cannot settle physical classification. **A paper may receive secondary tags**.

**Decision rule:** Do not promote `CORE_DIRECT` on generic co-presence of EV and Power terms, ambient as common forcing, EV battery internal heat, or a hypothetical simulation with no actual interface constraint. `CORE_DIRECT_SIMULATED` and `CORE_DIRECT_OBSERVED` must be distinct subcategories.

**Explicit exclusion reasons:** `AI_TRANSFORMER_ONLY`, `EV_MEANS_EXTRACELLULAR`, `THERMAL_POWER_GENERATION_ONLY`, `UNRELATED_HEAT_TRANSFER`, `NO_RELEVANT_P_OR_TE_ASSET`, `DUPLICATE_RECORD`, `SUPERSEDED_PUBLICATION`, `RETRACTED` (flag verification), `OTHER_EXPLAIN`. For non-English abstracts record translator/access limitation rather than silent exclusion.

**Original full text fields:** bibliographic identity, page/section/equation number and source version; P vs Tₑ subsystem, sensor location, units, state-time variables, heat/charge conservation equations, constitutive losses/convective heat rejection, initial/boundary conditions and constraints; temperature-conditioned mechanism and independent direction P→Tₑ and Tₑ→P; simulation/calibration/heldout field observations, uncertainty and confounders; qualified electricity/mobility service targets and timing. An observed thermal state is NOT the same as observed heat-conditioned curtailment or actual mobility service.

**Research conclusion:** Evidence grades `ILLUSTRATIVE`, `EVIDENCE_BOUNDED`, `CALIBRATED`, `INDEPENDENTLY_VALIDATED` are separate flags rather than implying universal hierarchy; validate the SAME physical target with an independent observed dataset. `SIMULATED_REFERENCE` can be used but is not independent experimental proof.

**Data custody:** No bulk Scopus abstracts, addresses, correspondence or licensed corpus in the GitHub branch absent authorized license permission. DOI/EID citation list and authored notes only.
