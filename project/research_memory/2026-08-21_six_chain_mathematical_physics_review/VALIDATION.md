# Reproducibility Validation

**Validation date:** 2026-08-21  
**Purpose:** verify that the structured ontology can regenerate a valid editable Draw.io document.

## Test performed

The repository-local files are designed to be used side by side:

- `CHAIN_LAYER_MATRIX.csv`
- `DRAWIO_REGENERATION.py`

Validation command:

```bash
python DRAWIO_REGENERATION.py
```

Expected output:

```text
Six_Chain_Ontology_Regenerated.drawio
```

The generated file was then parsed with Python's XML parser:

```python
import xml.etree.ElementTree as ET
ET.parse("Six_Chain_Ontology_Regenerated.drawio")
```

## Result

**PASS.** The local validation run generated a Draw.io XML file of **47,196 bytes** and `xml.etree.ElementTree` parsed it successfully.

## Staging-path note

During local packaging, the first test placed the script and CSV in different temporary directories, so the script correctly failed to find its declared side-by-side input. After matching the repository layout—placing `CHAIN_LAYER_MATRIX.csv` beside `DRAWIO_REGENERATION.py`—the regeneration and XML parse both passed. This was a staging-layout issue, not a scientific or code-generation defect.

## Reproducibility contract

A future modification should preserve these invariants:

1. all six chains remain distinct analytical logics;
2. mathematics remains cross-cutting rather than a seventh physical chain;
3. optimization remains cross-cutting rather than a lifecycle stage;
4. `topology != interdependency != interface mechanism`;
5. `physical state != functionality != service != societal consequence`;
6. literature anchors support layer/method families unless exact equation provenance is independently verified;
7. the generated `.drawio` must remain valid XML and editable in diagrams.net/draw.io.
