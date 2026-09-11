# Reuse Anywhere Guide

This package is intentionally stored in multiple open text formats so the Stage-1 model can be reused without depending on a single application.

## GitHub / Markdown

Use:
- `01_MASTER_SCIENTIFIC_CONTENT.md`
- `02_STAGE1_DEEP_DIVE_OUTLINE.md`
- `03_STAGE1A_COMPLETENESS_PROTOCOL.md`
- `09_REFERENCES_AND_CITATION_GUIDE.md`

These can be copied directly into GitHub, Obsidian, Notion, Typora, VS Code, Quarto, or converted with Pandoc.

## Overleaf / LaTeX

Copy the displayed equations from the Markdown files directly into LaTeX math environments. The canonical object is:

```latex
\[
\mathfrak M_1^{*}=
(\Omega,\mathcal G,\mathcal Q_{adm},\mathbf S,
\mathcal R_D,\mathcal R_N,\mathcal R_C,\mathcal R_L,
\mathcal R_U,\mathcal E_{prov},Y_0,\Lambda_{sus})
\]
```

## Miro / Canvs / draw.io / Mermaid

Use `07_ENGINEERING_LOGIC_CHART.mmd` as the portable diagram source. It deliberately uses a **left-to-right engineering logic chart**, not a radial rainbow mind map.

For manual recreation, follow `04_VISUAL_ENGINEERING_LOGIC_MAP_SPEC.md`.

## XMind / MindMap tools

Use `08_STAGE1_PORTABLE_OUTLINE.opml` where OPML import is supported. If OPML is not supported, paste the tree from `02_STAGE1_DEEP_DIVE_OUTLINE.md` and `03_STAGE1A_COMPLETENESS_PROTOCOL.md`.

## Python / Julia / MATLAB / R

Use `05_PORTABLE_MODEL_SCHEMA.yaml` as the machine-readable conceptual schema and `06_RELATION_REGISTER_TEMPLATE.csv` as the tabular relation database.

Recommended computational objects:

```text
entities.csv / dataframe        -> Ω
relations.csv / dataframe       -> Qadm + Sij + rij
graph objects                   -> GP, GT, GI, GO
cross-layer edge table          -> E×
evidence table                  -> Eprov
initial-state table/vector      -> Y0
sustainability metadata table   -> Lambda_sus
```

## Database implementation

The relation register can be implemented as a relational table with `(source_id, target_id)` as the primary candidate key, or as a property graph where every relation stores:

- direction;
- dependency type;
- carrier;
- mechanism;
- activation condition;
- geographic relation;
- status `D/N/C/L/U`;
- evidence level;
- provenance;
- scope boundary.

## Portability rule

The canonical scientific meaning is defined by the Markdown/YAML/CSV source files, **not by any particular rendered diagram**.

Therefore a future Canva, Miro, draw.io, XMind, Figma, or PowerPoint visualization may change visually without changing the scientific model as long as it preserves:

```math
\boxed{\Omega\rightarrow Q_{adm}\rightarrow S_{ij}\rightarrow r_{ij}\rightarrow\text{Evidence}\rightarrow\mathfrak M_1^*}
```
