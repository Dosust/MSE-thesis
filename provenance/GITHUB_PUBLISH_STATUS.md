# GitHub publish status

Repository: `Dossiya-SE/MSE-thesis`  
Visibility: **private**  
Branch: `main`

## Published directly to GitHub

- repository README and thesis scope;
- conversation authenticity policy;
- verbatim current-conversation user requests available in the visible thread;
- assistant-response artifact index;
- provenance rules and full session artifact inventory with SHA-256 identities.

## Artifact-byte inventory

`provenance/INVENTORY.csv` records the exact names, sizes, and SHA-256 values of the source datasets, derived corpora, prompts, Python code, workbooks, reports, previews, and ZIP packages prepared in the active session.

## Connector boundary

The available GitHub write actions accept UTF-8 content inline but do not expose a local-file upload parameter for arbitrary binary/local-runtime files. Therefore the inventory is authoritative for artifacts that could not be transferred byte-for-byte through the connector in this run. No missing artifact is falsely described as uploaded.

This status file must be updated if additional raw artifacts are subsequently committed.
