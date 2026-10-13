# All Thesis Presentations — Mandatory Eight-Component Architecture V1

**Researcher directive:** 2026-10-13.  
**Status:** USER-APPROVED PRESENTATION-CONTENT REQUIREMENT; proposed GitHub integration via reviewed PR.  
**Applies to:** every new or revised MSE thesis-facing presentation, regardless of duration or medium: 3-minute/eight-slide Deck3, 10-slide research-progress deck, 13/14-slide Chapter 1, proposals, research meetings, posters with slide-like presentation panels, final defense, and exports.  
**Underlying research selection:** `project/thermal_sos_functional_architecture/SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md`.  
**Governance:** This document controls **visibility in presentations**, not full physical-system boundaries, device parameter/model admission, causal evidence, frozen objectives, or validated interdependency claims. Current scientific scope and evidence authorities prevail.

## Mandatory visible roster — preserve all exact identifiers

**Power System (P):**
- **P1 — Distribution Transformer:** changes voltage level and supplies downstream distribution.
- **P2 — Distribution Feeder:** conveys AC power toward connected loads including charging.
- **P3 — Transformer Protection/Load-Management Hardware:** can enforce a restriction **only if installed/enabled control and its effect are evidenced**.
- **P4 — Transformer Cooling Equipment:** rejects transformer heat within the P subsystem.

**Electrified Transportation System (Tₑ):**
- **T1 — DC EV Charger:** converts grid-side AC to controlled DC charging power.
- **T2 — Vehicle Battery Pack:** stores electrical energy.
- **T3 — EVSE Cooling Equipment:** manages/removes charger heat within Tₑ.
- **T4 — Vehicle HVAC Equipment:** affects vehicle energy consumption and may influence **later** charging needs.

## Minimum acceptance criterion for every presentation
1. **At least one complete, legible architecture slide/figure** visibly names **P1–P4 and T1–T4, all eight**. This does **not** require repeating every component on every slide. Do not hide any of the eight solely in speaker notes, an appendix, a legend too small to read, or inaccessible hover content.
2. Distinct **Power (P)** and **Electrified Transportation (Tₑ)** boundaries; two groups of four with no invented third physical subsystem. The eight are a **selected study roster**, not the exhaustive components of either full system.
3. Emphasize the primary **electrical delivery chain** `P1 → P2 → T1 → T2`: grid-side **AC P2→T1**, then **DC energy T1→T2**. These are physical energy/electrical supply relationships, not evidence of either proposed temperature-mediated I2 or I3 law.
4. Keep P3/P4 within P and T3/T4 within Tₑ with their actual protection/cooling/HVAC/energy roles. An eight-component roster is **not** eight mandatory ODE states, not eight established intersystem mechanisms and not four bidirectional thermal connections.
5. External extreme heat acts on the two subsystems as **common forcing**; do not draw it as P→Tₑ or Tₑ→P evidence.
6. When drawing I2 (Tₑ→P), display `CANDIDATE — charger thermal condition → actual grid-side AC P/Q/current → feeder/transformer loading and conditional temperature`; do **not** draw DC power or V2G as the grid-side causal carrier. The published CPC50 AC measurement precedent does not automatically establish an independently validated temperature-to-AC-demand law.
7. When drawing I3 (P→Tₑ), display `CONDITIONAL / OPEN — transformer thermal condition → actual installed P3 restriction → available charging power`. Do not imply the TU Wien benchmark has a verified installed P3 or thermal trip setting.
8. All authored canvas/panel/box interiors pure white; exact Deck3 13-token sRGB design palette where Deck3 applies; authentic photos preserve real colors; native-editable labels and meaningful large arrows only. Preserve same-slide adjacent verifiable citations for externally sourced claims. Avoid tiny equipment labels on short-format decks.

## Placement by presentation variant
| Variant | Mandatory complete roster placement | Governing exception |
|---|---|---|
| Three-minute / eight-slide Deck3 | **Slide 2 — Research Background** physical systems figure (all 8 readable) | Preserve separately approved slide copy and speaker timing; architecture is the slide's illustration and native labels, not a rewritten body |
| Ten-slide research-progress presentation | **Slide 5 — Physical Systems and Selected Interdependencies** | Full explicit 4+4 roster required in the central figure; avoid consuming Slide 8 numeric-result space |
| Thirteen-/fourteen-slide Chapter 1 versions | **Slide 9 — System/Interface** or mapped approved full-system-equivalent figure | Do not reactivate obsolete IEEE or 19+21 selection IDs; map by purpose, not merely index |
| Proposal / seminar / defense / custom deck | **First system-architecture slide**, ideally immediately after context/problem | One complete 4+4 figure per deck, regardless of overall length |

**Short-deck adaptation:** Keep the complete roster visible once and focus the spoken explanation on P1/P2/T1/T2 with P3/P4/T3/T4 clearly labeled. Compact layout is allowed; omission, illegibility or incorrect group membership is not.

## Automated/manual release gates
- Exact visible component count 8; identifiers `P1,P2,P3,P4,T1,T2,T3,T4` each occur in accessible editable visible shapes.
- Correct grouping and full names; no substitution of old register IDs `P02,P10,...`.
- AC→DC boundary visually unambiguous; candidate arrows qualified; no invented protective settings/temperature limits.
- Source/notes and slide-fit QA; 16:9, legibility/contrast and no overlapping text, image or diagrams.
- No declaration of PASS until a **specific produced slide deck** is rendered and inspected. This rule file is not proof that historical decks have been updated.

**Change control:** A researcher-authorized roster change requires a distinct versioned amendment. Older 3-minute master text, canonical objective wording, manuscript science and literature-evidence records are not silently rewritten by this presentation-level rule.
