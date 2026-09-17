#!/usr/bin/env python3
"""Validate the 2026-08-21 thesis memory capsule without overriding current authority.

The capsule is a historical project-state snapshot. This repository-consistency
check verifies (1) capsule integrity, (2) provenance locks that still belong to
that snapshot, and (3) that the current canonical thesis explicitly supersedes
legacy P-W-T-SW scope. It does not validate scientific truth, full-text
literature claims, empirical calibration, or require current thesis files to
retain historical scientific content.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAPSULE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    require(path.exists(), f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    manifest = json.loads(read(CAPSULE / "manifest.json"))
    memory = json.loads(read(CAPSULE / "PROJECT_MEMORY.json"))

    # 1. Historical capsule completeness.
    for name in manifest["files"]:
        require((CAPSULE / name).exists(), f"Manifest file missing: {name}")

    # 2. Historical snapshot self-consistency. Do not compare these legacy
    # scientific objects with the current thesis scope: the capsule is dated
    # 2026-08-21 and has since been superseded scientifically.
    invariants = manifest["critical_invariants"]
    require(
        memory["thesis"]["precise_formulation"] == invariants["precise_title"],
        "Historical precise formulation drifted inside the v2 memory capsule",
    )
    require(
        memory["thesis"]["primary_demonstrator"] == invariants["primary_demonstrator"],
        "Historical primary demonstrator drifted inside the v2 memory capsule",
    )
    require(
        memory["monte_carlo"]["sha256"] == invariants["dataset_sha256"],
        "Historical frozen-dataset SHA-256 drifted inside the v2 memory capsule",
    )

    # 3. Current-authority guardrail. The active thesis must identify itself as
    # current P-T-I-O authority and explicitly demote earlier P-W-T-SW material
    # to historical/provenance status.
    scope = read(ROOT / "project" / "THESIS_SCOPE.md")
    require("CANONICAL CURRENT SCOPE" in scope, "Current scope authority marker missing")
    require("Power–Transportation" in scope, "Current P-T system description missing")
    require("\\mathcal S=\\{P,T,I,O\\}" in scope, "Current P-T-I-O system object missing")
    require(
        "Earlier P–W–T–SW" in scope and "historical/provenance material" in scope,
        "Current scope does not explicitly supersede the legacy P-W-T-SW formulation",
    )

    # 4. Current RQ/SO/H authority must remain RQ0 + RQ1-RQ7 with H1-H5.
    project_readme = read(ROOT / "project" / "README.md")
    require(
        "CANONICAL_RQ_SO_HYPOTHESES_V3.md" in project_readme,
        "Current RQ/SO/H authority link missing from project README",
    )
    require("RQ1–RQ7" in project_readme, "Current RQ1-RQ7 architecture marker missing")
    require("H1–H5" in project_readme, "Current H1-H5 architecture marker missing")

    # 5. Frozen 2026-08-20 literature-corpus lock retained for provenance.
    prompt = read(ROOT / "prompts" / "PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md")
    dataset_hash = memory["monte_carlo"]["sha256"]
    require(
        "Thesis_Final_Unique_Papers_325_2026-08-20(1).csv" in prompt,
        "Frozen logical dataset filename drift",
    )
    require(dataset_hash in prompt, "Frozen dataset SHA-256 drift")
    require("325" in prompt and "34" in prompt, "Frozen dataset shape declaration missing")

    # 6. High-rigor archive copy identity retained for provenance.
    run = read(ROOT / "methods" / "monte_carlo" / "final_run_2026-08-20" / "README.md")
    require(
        "Thesis_Final_Unique_Papers_325_2026-08-20(4).csv" in run,
        "High-rigor execution-copy filename missing",
    )
    require(dataset_hash in run, "High-rigor execution copy does not declare frozen hash")
    require("Robust core size" in run and "**80**" in run, "High-rigor robust-core summary drift")

    # 7. Memory-version invariants.
    require(memory["version"] == 2, "PROJECT_MEMORY.json is not v2")
    require(
        memory["supersedes"] == "project_memory/2026-08-21_chain_architecture/",
        "Superseded v1 path drift",
    )
    require(
        manifest["supersedes"] == "project_memory/2026-08-21_chain_architecture/",
        "Manifest supersession path drift",
    )

    # 8. Root README must point to current authority and state the archive rule;
    # it must not be forced to repeat the historical demonstrator.
    root_readme = read(ROOT / "README.md")
    require(
        "CANONICAL_RQ_SO_HYPOTHESES_V3.md" in root_readme,
        "Root README does not point to current RQ/SO/H authority",
    )
    require(
        "Historical/archive material is provenance only" in root_readme,
        "Root README no longer states the historical-material authority guardrail",
    )

    # 9. Correction-log guardrail: the intermediate nu-notation claim remains retracted.
    correction_log = read(CAPSULE / "14_CORRECTION_LOG.md")
    require("typo claim is retracted" in correction_log.lower(), "Retracted audit finding is not documented")

    print(
        "PASS: historical memory capsule integrity is preserved and current "
        "P-T-I-O / RQ1-RQ7 thesis authority is not overridden by legacy scope."
    )


if __name__ == "__main__":
    main()
