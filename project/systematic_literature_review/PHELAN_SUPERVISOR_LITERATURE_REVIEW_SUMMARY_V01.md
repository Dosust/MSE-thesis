# Research progress brief for Professor Pat Phelan — draft (NOT a claim of completed systematic review)

**Thesis:** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Research focus:** thermal state–time coupling between distribution power systems and electrified transport under extreme heat.  
**Date:** 3 November 2026. **Status:** working briefing supported by preliminary source audits; requires final review methods and model evaluations.

Dear Professor Phelan,

Following your suggestions, I have concentrated the thesis on what existing research has already established about transformer and EV charging thermal physics, actual experimental observations, and the value of physics-informed modeling.

**What others have already done.** Existing research has examined EV-driven transformer thermal aging and charging control (Hilshey et al. 2013; Gong et al. 2015), dynamic thermal ratings of transformers combined with EV charging decisions (Pan et al. 2025), and temperature-conditioned transformer/fast-charging simulations (Fletcher & Khan, RACE for 2030, 2025). A Qatar field study reports rectifier-temperature-associated fast-charger derating and increased charging times in extreme heat (Krama et al. 2026). Bragone et al. 2022 already investigated transformer thermal PINNs using real transformer operating inputs and compared them with a finite-volume model. Physics-informed neural Transformer approaches also exist for vehicle thermal-management prediction (Cao et al. 2026). Hence, neither transformer heat modeling nor introducing a PINN is a credible stand-alone novelty claim.

**What is not yet verified.** I have not yet identified a *qualified single-installation* dataset that synchronously measures supplying-transformer thermal states, connected EVSE rectifier/thermal derating, AC/DC interface power, relevant operating restrictions and vehicle service commitments. This is a limitation of the sources examined so far, **not proof that such research does not exist**. Distinguishing a common high-temperature exposure from a measured directional thermal interaction is essential.

**Literature-review execution.** I recovered an archived source inventory with 687 raw Scopus/IEEE/Compendex-derived rows and 404 deduplicated bibliographic records, combined it with October screening/thermal papers and November candidates, and created a provenance-preserving 533-record provisional master register (784 source lineage links). These are **bibliographic consolidation figures, not formally included systematic-study counts**. The recorded 200→26 October stage was a metadata-priority screen; full-text verification, search-log completeness, formal eligibility, and PRISMA-ScR reporting remain open. I am reusing already audited paper equations and conducting the remaining checks.

**Experimental data and modeling.** A measured SINTEF transformer series has 8,592 hourly records and a preliminary same-site temperature-prediction benchmark, but it does not cover extreme hot ambient conditions or establish coupled transformer–charger behavior. Separate vehicle and charger measurements are available or identified, subject to sensor/source validation and data access. Accordingly, I propose to derive and independently test a physically justified transformer/EVSE first-law model first. I will compare PINNs or simpler physics-guided hybrids **only where the actual measurements permit a fair and meaningful held-out experiment**. If those conditions are not met, a transparent pure-physics model with documented uncertainty remains the scientifically justified path.

**Next research tasks:** finish systematic search provenance and study-family deduplication; extract the closest papers’ exact equations, measurements and independent validation; qualify actual charger and transformer observations; and then finalize the research gap and methodological comparison with an evidence-bounded conclusion.

Sincerely,

Dossiya Dakou

### Sources for the review and subsequent formal citations

1. Hilshey et al. (2013): https://doi.org/10.1109/TSG.2012.2217385
2. Gong et al. (2015): https://doi.org/10.1109/TSG.2014.2365452
3. Bragone et al. (2022): https://doi.org/10.1016/j.epsr.2022.108447
4. Fletcher & Khan (2025): https://www.racefor2030.com.au/project/taking-the-heat-out-of-electric-vehicle-charging/
5. Pan et al. (2025): https://doi.org/10.1049/hve2.70024
6. Krama et al. (2026): https://doi.org/10.1016/j.ecmx.2026.101960
7. Cao et al. (2026): https://doi.org/10.1016/j.applthermaleng.2026.130776
8. Li, Chang & Lu (2026): https://doi.org/10.1109/PESGM58988.2026.11693150

**Do not send this as proof that a thorough PRISMA-ScR review or matched PINN experiment is finished.** It is an honest working scientific progress report until the open gates are closed.
