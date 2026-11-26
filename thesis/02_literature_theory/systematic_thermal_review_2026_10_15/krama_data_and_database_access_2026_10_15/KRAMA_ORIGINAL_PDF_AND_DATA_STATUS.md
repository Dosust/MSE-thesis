# Krama et al. (2026): authentic PDF acquisition and experimental data request audit

**Date of check:** 2026-10-15  
**DOI:** https://doi.org/10.1016/j.ecmx.2026.101960  
**Publisher PII:** `S2590174526004435`  
**Journal:** *Energy Conversion and Management: X*, Vol. 31, article 101960, 16pp  
**Corresponding author (as identified by HBKU):** Abdelbasset Krama (QEERI/HBKU).  
**Research status:** ACCESS AND REQUEST PREPARED — NOT PDF/DATA ACQUIRED.

## What IS authenticated
- **Paper identity and open-access status**: [official Elsevier/ScienceDirect landing page](https://www.sciencedirect.com/science/article/pii/S2590174526004435) identifies title, authors, DOI, PII, journal, article number and open-access / Creative Commons status.
- **Independent institutional bibliography**: [HBKU original record](https://elmi.hbku.edu.qa/en/publications/impact-of-extreme-climatic-conditions-on-fast-ev-charger-performa/) confirms peer-reviewed 16-page publication and identifies Krama as corresponding author.
- **Reported observational categories**: ambient and rectifier temperatures, offered and delivered DC power, conversion efficiency, upstream electrical input and current harmonics, EV SOC evolution and charging duration.
- **Published high-level reported results**: approximately 15–55 °C ambient conditions, 50 kW air-cooled charger, offered-power thermal reduction, 86 vs 169 min for specific reported charging conditions; authors mention cross-session and temporal holdout regression validation.
- **Data availability statement in official publisher article:** "Data will be made available on request." This is NOT an executed request or evidence that files are available without author approval.

## What was attempted (without guessing that attempted links mean access)
1. Publisher landing URL: open returned **403 Forbidden** in the current retrieval tool; searchable index exposes citation/abstract only.
2. Official ScienceDirect `/pdfft` and `/pdf` endpoints at publisher PII: retrieval returned **cache miss**, no file bytes read or visual PDF pages verified.
3. Elsevier API PDF request: not available through current client/host.
4. Elsevier `ars.els-cdn.com` predictable path: source not available through retrieval tool; **do not infer availability from guessed URL**.
5. User-provided library LibKey full-text link: open returned **cache miss**; no original PDF authenticated or downloaded.
6. HBKU Pure original record: full metadata and published abstract, DOI only; no deposited repository PDF attachment found through inspected page.
7. ResearchGate record: **request PDF** (author-access route), not a downloadable copy.
8. Search for exact title with `filetype:pdf`, exact PII and preprint/repository: no authenticated publisher/author-accepted manuscript PDF identified by the searches; a Scribd-hosted transcription exists, but it is **lower-provenance, NOT a verified source of full-text PDF pages, equations, tables or figure pixels**.
9. Local PDF acquisition/inspection: **NO VALID ORIGINAL PDF FILE PRESENT**; do not count page rendering, read full text or DA-2 as passed.

## Evidence status / scientific boundary
| Gate | Outcome | Reason |
| --- | --- | --- |
| Identity | VERIFIED | Publisher DOI/PII and official institutional record |
| Official open-access license | VERIFIED on publisher landing record | Creative Commons; access delivery endpoints still blocked |
| Original PDF file in the current workspace | **NOT OBTAINED** | 403/cache miss/retrieval restrictions |
| Equations and figure pixels directly audited | **NOT DONE** | Cannot authenticate/re-render a PDF |
| Published field experimental study | CONFIRMED BY PUBLISHER | Original study describes the actual commercial air-cooled charger field trials |
| Actual raw time series opened | **NOT OBTAINED** | Data on request; no author response or attachment |
| DA-2 (raw file opened) | **FAIL / NOT YET** | Do not substitute abstract, screenshots or reconstructed series |
| DA-4 (parameter identifiability + independent test) | **NOT ASSESSED** | Actual raw rows, exact channels, timestamps and holdouts missing |
| DA-5 (same-site power–transport interface + service) | **NOT ASSESSED / UNVERIFIED** | No matched distribution transformer temperature, EVSE physical state and observed trip/schedule service established |

### Thermal power-system boundary
A component called 'transformer' inside an EV charger cabinet belongs to the **EVSE within `T_e`**, not to a separate externally measured distribution transformer within Power System `P`. Grid-side analyzer voltage/current at the charger input does not by itself verify upstream transformer winding temperature or a measured heat-conditioned `P→T_e` interface.

## Required raw measurements (data request, not assumed contents)
- Original time-indexed ambient and rectifier temperatures, sensor units/accuracy and sampling/resampling rules.
- Input 3-phase power and quality channels, offered/commanded versus actual delivered DC power, power-limiting flags where recorded.
- Session IDs and dates, EV battery SOC and vehicle/battery temperature where available (not presumed).
- Details of internal sensor placement and 'transformer' distinction, cooling/fan state if recorded, device ratings and relevant protection setpoints when sharable.
- Alignment/time zones of PQ analyzer, wireless sensor platform and OCPP/charger logs; missingness, known calibration and duplicated rows.
- Training and holdout event/session split metadata, licenses/use permission, anonymization restrictions.
- Explicit statement whether **a same-site upstream distribution transformer** was instrumented (if not, label component-only empirical validation).
- Confirmation of permitted use for thesis parameter calibration and independent validation; redistribution rights not assumed.

## Next action
The concise request to the corresponding author is saved in [DATA_REQUEST_EMAIL_DRAFT.md](DATA_REQUEST_EMAIL_DRAFT.md) with no assertion that an email was sent. User-authorized email integration or user sending from their own institutional account is still required.

Use a user-obtained original publisher PDF or accepted manuscript with a real provenance link and run the render→inspect→extract workflow. Keep current manuscript only as publisher-metadata/abstract-verified.
