# Thesis Configuration Schema

`thesis_model.schema.json` is the machine-readable contract for active P–T–I–O model configuration.

It enforces the current ontology:

$$
\mathcal S=\{P,T,I,O\},
$$

with $P,T$ as physical infrastructure systems and $I,O$ as informational/organizational layers.

The schema checks the presence and basic type structure of:

- P–T–I–O states;
- directed interdependency records;
- hazard definition;
- Stage-4 operational-control symbols;
- Stage-5 viability symbols;
- Stage-6/7 transformation interface;
- analysis capability flags.

The schema validates **configuration structure**, not scientific truth, parameter calibration or physical validity. Those require separate verification/validation.

`../config/example_model.json` is maintained as a passing example and is validated in GitHub Actions.
