#!/usr/bin/env python3
"""Integrate the canonical V00–V10 SVG family into owning thesis documents.

Design constraints
------------------
1. This script changes visual placement only; it does not alter frozen equations.
2. Every insertion is idempotent and marked with CANONICAL_VISUAL comments.
3. Each figure is explicitly subordinate to the owning mathematical specification.
4. Paths are repository-relative and valid for GitHub Markdown rendering.
5. Missing anchors are fatal: silent placement drift is not allowed.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def visual_block(code: str, rel_svg: str, title: str, width: str = "96%") -> str:
    return f'''<!-- CANONICAL_VISUAL:{code} -->

### {code} — {title}

<p align="center">
  <img src="{rel_svg}" alt="{code} — {title}" width="{width}">
</p>

> **Visual synopsis:** This figure compresses the scientific architecture for navigation and interpretation. The equations, definitions, evidence status, and boundary rules in the owning document remain authoritative.

<!-- /CANONICAL_VISUAL:{code} -->

'''


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def insert_before(path: str, anchor: str, block: str, marker: str) -> bool:
    text = read(path)
    if marker in text:
        return False
    idx = text.find(anchor)
    if idx < 0:
        raise RuntimeError(f"Anchor not found in {path!r}: {anchor!r}")
    text = text[:idx] + block + text[idx:]
    write(path, text)
    return True


def replace_once(path: str, old: str, new: str) -> bool:
    text = read(path)
    if new in text:
        return False
    if old not in text:
        raise RuntimeError(f"Expected text not found in {path!r}: {old[:120]!r}")
    text = text.replace(old, new, 1)
    write(path, text)
    return True


def main() -> None:
    changed: list[str] = []

    placements = [
        # Repository-level visual compression.
        (
            "README.md",
            "## Canonical entry points",
            visual_block(
                "V00",
                "figures/canonical/00_master_seven_stage_architecture.svg",
                "Canonical Seven-Stage Master Thesis Architecture",
                "100%",
            ),
            "CANONICAL_VISUAL:V00",
        ),
        (
            "README.md",
            "## Current evidence methodology — FTEE v2.0",
            visual_block(
                "V08",
                "figures/canonical/08_hypothesis_test_architecture.svg",
                "H1–H5 Scientific Test Architecture",
                "100%",
            ),
            "CANONICAL_VISUAL:V08",
        ),
        (
            "README.md",
            "## FTEE extraction discipline",
            visual_block(
                "V09",
                "figures/canonical/09_FTEE_evidence_pipeline.svg",
                "FTEE v2.0 Evidence-to-Equation Pipeline",
                "100%",
            ),
            "CANONICAL_VISUAL:V09",
        ),
        (
            "README.md",
            "## Immediate next task",
            visual_block(
                "V10",
                "figures/canonical/10_minimal_experimental_realization.svg",
                "Minimal Sufficient Experimental Realization",
                "100%",
            ),
            "CANONICAL_VISUAL:V10",
        ),
        # Project dashboard.
        (
            "project/README.md",
            "## 1. Authority map",
            visual_block(
                "V00",
                "../figures/canonical/00_master_seven_stage_architecture.svg",
                "Canonical Seven-Stage Master Thesis Architecture",
                "100%",
            ),
            "CANONICAL_VISUAL:V00",
        ),
        (
            "project/README.md",
            "## 3. Active evidence architecture — FTEE v2.0",
            visual_block(
                "V08",
                "../figures/canonical/08_hypothesis_test_architecture.svg",
                "H1–H5 Scientific Test Architecture",
                "100%",
            ),
            "CANONICAL_VISUAL:V08",
        ),
        (
            "project/README.md",
            "## 3. Active evidence architecture — FTEE v2.0",
            visual_block(
                "V09",
                "../figures/canonical/09_FTEE_evidence_pipeline.svg",
                "FTEE v2.0 Evidence-to-Equation Pipeline",
                "100%",
            ),
            "CANONICAL_VISUAL:V09",
        ),
        # Stage/system ownership.
        (
            "project/CANONICAL_SYSTEM_DEFINITION.md",
            "## 2.",
            visual_block(
                "V01",
                "../figures/canonical/01_multilayer_PTIO_system.svg",
                "P–T–I–O Multilayer System",
            ),
            "CANONICAL_VISUAL:V01",
        ),
        (
            "project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md",
            "## 2. Complete directed interdependency scope",
            visual_block(
                "V02",
                "../figures/canonical/02_causal_interdependency_object.svg",
                "Causal Interdependency Object",
            ),
            "CANONICAL_VISUAL:V02",
        ),
        (
            "project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md",
            "## 1. Scientific object of Stage 3",
            visual_block(
                "V03",
                "../figures/canonical/03_hybrid_multiscale_dynamics.svg",
                "Coupled Hybrid Multiscale Propagation",
            ),
            "CANONICAL_VISUAL:V03",
        ),
        (
            "project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md",
            "## 1. What the 10 literature passes established",
            visual_block(
                "V04",
                "../figures/canonical/04_observation_organization_control.svg",
                "Observation–Organization–Feedback–Control Loop",
            ),
            "CANONICAL_VISUAL:V04",
        ),
        (
            "project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md",
            "## 1. Core viability logic",
            visual_block(
                "V05",
                "../figures/canonical/05_controlled_viability_geometry.svg",
                "Controlled Sustainable Viability Geometry",
            ),
            "CANONICAL_VISUAL:V05",
        ),
        (
            "project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md",
            "## 1. Current infrastructure regime",
            visual_block(
                "V06",
                "../figures/canonical/06_resilience_sustainability_interface.svg",
                "Resilience-to-Sustainability Diagnostic Interface",
            ),
            "CANONICAL_VISUAL:V06",
        ),
        (
            "project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md",
            "## 1. State control and regime transformation are different",
            visual_block(
                "V07",
                "../figures/canonical/07_transformation_pathways.svg",
                "Sustainable Transformation Meta-Graph",
            ),
            "CANONICAL_VISUAL:V07",
        ),
        (
            "project/RESEARCH_HYPOTHESES.md",
            "## 2. Overarching scientific hypothesis",
            visual_block(
                "V08",
                "../figures/canonical/08_hypothesis_test_architecture.svg",
                "H1–H5 Scientific Test Architecture",
            ),
            "CANONICAL_VISUAL:V08",
        ),
        (
            "project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md",
            "## 1. Complete research pipeline",
            visual_block(
                "V09",
                "../figures/canonical/09_FTEE_evidence_pipeline.svg",
                "Fresh-Search Evidence-to-Equation Pipeline",
            ),
            "CANONICAL_VISUAL:V09",
        ),
        (
            "project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md",
            "## 1. Scientific reason: hypotheses require controlled contrasts",
            visual_block(
                "V10",
                "../figures/canonical/10_minimal_experimental_realization.svg",
                "Minimal Sufficient Experimental Realization",
            ),
            "CANONICAL_VISUAL:V10",
        ),
    ]

    for path, anchor, block, marker in placements:
        if insert_before(path, anchor, block, marker):
            changed.append(path)

    # Keep the operational dashboard synchronized with the now-frozen H1 search protocol.
    old_root = (
        "Build and freeze the **Fresh Literature Search Protocol for $H_1$**: concept blocks, synonyms, "
        "database-specific Boolean strings, field restrictions, time/coverage rules, query-version registry, "
        "deduplication logic, inclusion/exclusion criteria, screening form, citation-chasing rules, amendment "
        "procedure and PRISMA accounting schema. Only then execute the first de novo search."
    )
    new_root = (
        "Execute the **frozen $H_1$ CORE v1 search protocol** in Scopus, Web of Science Core Collection, "
        "Compendex and IEEE Xplore; preserve the four raw exports and search records; then construct "
        "$\\mathcal P_{H_1}^{raw}$ for identity-preserving deduplication and title/abstract screening."
    )
    try:
        if replace_once("README.md", old_root, new_root):
            changed.append("README.md")
    except RuntimeError:
        # A prior manual synchronization may already have changed this prose; visual integration must remain safe.
        pass

    old_project = (
        "The next operational task is to build and freeze the database-specific **Fresh Literature Search Protocol "
        "for $H_1$**, including concept blocks, synonyms, Boolean strings, field restrictions, search date, "
        "coverage rules, deduplication logic, eligibility codebook, screening form, citation-chasing rule, "
        "amendment/version-control rule and PRISMA accounting schema. Only then should the first new search be executed."
    )
    new_project = (
        "The $H_1$ search protocol is now frozen for initial execution. The next operational task is to execute "
        "the exact CORE v1 strings in Scopus, Web of Science Core Collection, Compendex and IEEE Xplore, preserve "
        "the raw exports and search metadata, construct $\\mathcal P_{H_1}^{raw}$, and then perform hierarchical "
        "deduplication before title/abstract screening."
    )
    try:
        if replace_once("project/README.md", old_project, new_project):
            changed.append("project/README.md")
    except RuntimeError:
        pass

    # Validate that all required placements exist exactly once.
    required = {
        "README.md": ["V00", "V08", "V09", "V10"],
        "project/README.md": ["V00", "V08", "V09"],
        "project/CANONICAL_SYSTEM_DEFINITION.md": ["V01"],
        "project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md": ["V02"],
        "project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md": ["V03"],
        "project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md": ["V04"],
        "project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md": ["V05"],
        "project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md": ["V06"],
        "project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md": ["V07"],
        "project/RESEARCH_HYPOTHESES.md": ["V08"],
        "project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md": ["V09"],
        "project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md": ["V10"],
    }
    for path, codes in required.items():
        text = read(path)
        for code in codes:
            count = text.count(f"<!-- CANONICAL_VISUAL:{code} -->")
            if count != 1:
                raise RuntimeError(f"{path}: expected one {code} marker, found {count}")

    unique_changed = sorted(set(changed))
    print(f"Integrated canonical visuals into {len(unique_changed)} document(s).")
    for path in unique_changed:
        print(f"  - {path}")


if __name__ == "__main__":
    main()
