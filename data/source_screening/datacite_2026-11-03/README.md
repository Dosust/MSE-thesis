# DataCite Commons search-screening audit — 2026-11-03

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience (V3).  
**User requirement:** Only genuine operating-installation field measurements. NO synthetic, laboratory-only, or pure modelling datasets.

## Input and interpretation

- Source: user-supplied plain-text extraction of a **DataCite Commons Works search-results listing** on 2026-11-03.
- Search-result facets in pasted material: **478 Works**, including **67 Dataset** records. This is the search's reported result universe, **not 478 records reviewed**.
- The pasted text explicitly lists **25 DOI records**; all 25 were screened against the field-only rule.
- Local pasted-source SHA-256: `f93243530e50a222d1a9431be6b7d4a54cae03271858a888b230f4b110c4093c` (metadata trace only, not uploading copyrighted search excerpts).
- Screening is based on pasted metadata, enhanced with primary record pages for the transformer IR workbench dataset and Mongolian ger Dryad dataset and laboratory boiling Dryad dataset.
- The screening outcome **does not assert that all 67 dataset records have been examined**. No original measurement file was acquired or inspected for this screening batch.

## Results for the 25 visible records

| Classification | Count | Meaning |
|---|---:|---|
| `LAB_EXCLUDED` | 5 | Laboratory/controlled experiment, not operating-site data |
| `FIELD_OFF_SCOPE` | 2 | Operational field observations, but wrong physical domain |
| `NOT_RELEVANT` | 12 | Not relevant to physical power–EVSE problem |
| `TOPIC_LEAD_NOT_DATA` | 5 | Method/paper lead without established original eligible field files |
| `SYNTHETIC_EXCLUDED` | 1 | Explicit synthetic series |
| **FIELD_THESIS_ELIGIBLE** | **0** | No qualifying transformer/EVSE operating-site measurement files established |

### Important decisions

1. **Transformer IRT** [doi:10.17632/8mg8mkc7k5](https://doi.org/10.17632/8mg8mkc7k5): a *real camera measurement* of controlled **laboratory** transformer faults, at circa 23 °C, does not meet the **field-only** gate. Reject even though the work is an actual Dataset.
2. **AQUAIR** [doi:10.6084/m9.figshare.28934375.v1](https://doi.org/10.6084/m9.figshare.28934375.v1): timestamped field observations from a trout hatchery, but **not** electrical-transformer/EV charging equipment. Reject as thesis evidence.
3. **Mongolian ger** [doi:10.5061/dryad.fbg79cp4s](https://doi.org/10.5061/dryad.fbg79cp4s): the Dryad record contains source CSVs from **occupied field dwellings** as well as test structures; authentically field-monitored *in part*, but **off-domain**. Reject as transformer/EVSE evidence.
4. **Transformer monitoring XBee and winding FBG articles** [doi:10.5281/zenodo.1472703](https://doi.org/10.5281/zenodo.1472703) and [doi:10.21307/ijssis-2017-771](https://doi.org/10.21307/ijssis-2017-771): possible sensor-method leads **only**, not original field datasets confirmed by the pasted description. Do not include as accepted measured data.
5. **PINN sensor placement** [doi:10.48550/arxiv.2502.00552](https://doi.org/10.48550/arxiv.2502.00552): useful as methodology literature only; it cannot be used as evidence of field-validated transformer state-time trajectories.
6. **Swiss district heating conference paper** [doi:10.5281/zenodo.23055411](https://doi.org/10.5281/zenodo.23055411): mentions operation-site monitored heating and flexibility, but is **outside** the power–EVSE thermal scope, and its **underlying source files were not verified**.
7. **Beware keyword contamination**: “transformer” can mean a deep-learning model, while “thermal” may describe boiling, housing, ocean temperatures or other systems. Metadata labels alone do not prove admissible equipment.
8. **No causal coupling can be inferred** by merging separate real-world datasets.

## Admission rule — strict

An admissible original candidate must contain original measurements made at an actual operating distribution-transformer installation or EVSE. Its original publication/provenance must identify equipment and sensor location, units, sampling/timestamps and site. For a **jointly validated directional-interdependency** claim, additionally require **documented electrical connection and synchronized power/ambient/equipment temperature observations** from a common installation. Missing details must be marked OPEN, not guessed.

## Correct next search

- Apply **Work Type = Dataset** to the original 478-result search and inspect **all 67 dataset records** if accessible; the 25 visible records are not exhaustive.
- Better: replace broad `transformer temperature` with `"distribution transformer" "field measurement" "top oil"`, `"charging station" "measured" "derating"` and `"transformer" "charging station" monitoring`; search other data indexes for explicitly released *operating-site data*.
- For any candidate with actual matching equipment: open the repository landing page; verify downloadable original files; extract physical equipment, variables, units, time zone, sensor positions, owner/license, duration and electrical connectivity; only then propose admission to the canonical data inventory.

## Integration status
- This folder is a **screening log**, not an accepted field-measurement dataset.
- Do **not** modify canonical thesis objectives, model admission status, validation claims or accepted numerical results based on this search snippet.
- The same rows are indexed under the Google Drive thesis Data folder in the existing SPS Lab evidence workbook's dedicated DataCite screen tab.
