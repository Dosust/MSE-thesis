# Source Provenance and Reproducibility

## Source files supplied in this session

| File | Size (bytes) | SHA-256 |
|---|---:|---|
| `High_Rigor_Thesis_Paper_Corpus_207.csv` | 155328 | `e2358619b66b2609cb9af10462d38cf7f170095b11d2e6a7e6460b79c848d5a4` |
| `High_Rigor_Thesis_Literature_Corpus_207.xlsx` | 242454 | `b42b135396c55932d1071361f73504eecc39ffb72242d18bf6bc8ebea097f961` |
| `High_Rigor_Thesis_Literature_Corpus_207.zip` | 285148 | `1c72e57a38983b9b78f1e02456ee6094f49b317824474636a7898f76ea65fc8a` |
| `High_Rigor_Thesis_Journal_Landscape.csv` | 5853 | `2b17f676acbf61cdbc662b11d6b039136656bc14a23cc84f6761f807d346ab9a` |
| `Pasted markdown(20260820-083427).md` | 14970 | `ba3a674ee402300bd9591475a53eb54949bcea6363cd6b5d897a8d8d6809a80d` |

## 207-paper corpus structure

`High_Rigor_Thesis_Paper_Corpus_207.csv` contains **207 records × 18 columns**:

`Paper_ID, Title, Authors, Year, Journal, DOI, Primary_Discipline, Discipline_Tags, Hypothesis_Tags, Relevance_Class, Corpus_Origin, Availability, Local_Full_Text_Status, URL, Metadata_Verification_Status, Evidence_Stratum, Seed_Evidence, Seed_Limitation`

## Reproducibility rules

1. Never silently replace the referenced 207 corpus with a 259-, 325-, 342-, or other corpus.
2. Record input SHA-256 before any re-analysis.
3. Missing metadata remains missing unless independently verified and the verification is documented.
4. Preserve four provenance classes:
   - **source-derived fact**;
   - **literature synthesis**;
   - **mathematical inference**;
   - **proposed thesis formulation**.
5. When notation changes, record the amendment rather than silently redefining symbols.
6. When the thesis center changes, update `STATE.json` and `MASTER_MEMORY.md`.
7. Do not present hidden model reasoning, internal tools, or unavailable raw history as authentic conversation text.
8. Detailed scientific claims require full-text verification; corpus titles/tags alone are not sufficient for equation-level attribution.
9. Absence from the 207-paper corpus cannot establish global novelty.

## Scientific audit order

`source identity → metadata verification → full-text claim verification → mathematical mapping → novelty falsification → model development → computational validation`

## Linked repository evidence

- Framework images: `08_framework_images/`
- Existing conversation provenance: `conversation/`
- Monte Carlo methods: `methods/monte_carlo/`
- Locked 325-dataset representation: `data/authoritative_325_encoded/`
- This chain/framework memory capsule: `09_chat_memory/2026-08-21_six_chains_and_three_frameworks/`

## Local complete backup

A complete structured local capsule was also generated as `MSE_thesis_chat_memory_2026-08-21.zip`; its SHA-256 is:

`1e3e708f649e0d029327e8666355988dfdceafa62a2861dd1e2f0ef42ac05e2a`
