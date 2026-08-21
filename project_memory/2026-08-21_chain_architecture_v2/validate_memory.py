#!/usr/bin/env python3
"""Validate critical invariants of the corrected thesis memory capsule.

This is a repository-consistency check. It does not validate scientific truth,
full-text literature claims, or empirical calibration.
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

    # 1. Manifest completeness.
    for name in manifest["files"]:
        require((CAPSULE / name).exists(), f"Manifest file missing: {name}")

    # 2. Authoritative scope invariants.
    scope = read(ROOT / "project" / "THESIS_SCOPE.md")
    title = memory["thesis"]["precise_formulation"]
    demonstrator = memory["thesis"]["primary_demonstrator"]
    require(title in scope, "Precise thesis formulation drifted from project/THESIS_SCOPE.md")
    require("Power (P)" in scope and "Water / drainage (W)" in scope, "P/W sector scope mismatch")
    require("Transportation (T)" in scope and "Solid Waste (SW)" in scope, "T/SW sector scope mismatch")
    require(demonstrator in scope, "Primary demonstrator wording drifted from project/THESIS_SCOPE.md")
    require(
        "dynamic coupling → admissibility → viability → recovery" in scope,
        "Core mathematical contribution statement missing from authoritative scope",
    )

    # 3. Mathematical-object invariants.
    foundation = read(ROOT / "project" / "MATHEMATICAL_FOUNDATION.md")
    for token in ["K_R=K_{\\mathrm{phys}}", "\\mathcal V_R", "\\mathcal C_R", "\\partial\\mathcal V_R"]:
        require(token in foundation, f"Mathematical foundation missing invariant token: {token}")
    require("\\xi(t)\\longrightarrow\\eta(t)" in foundation, "xi -> eta distinction missing")

    # 4. Proposition registry invariants.
    props_md = read(ROOT / "project" / "SCIENTIFIC_PROPOSITIONS.md")
    props_yaml = read(ROOT / "config" / "scientific_propositions.yaml")
    for pid in [f"P{i}" for i in range(1, 8)]:
        require(f"**{pid}**" in props_md, f"{pid} missing from scientific proposition table")
        require(f"  {pid}:" in props_yaml, f"{pid} missing from machine-readable registry")

    # 5. Frozen corpus lock.
    prompt = read(ROOT / "prompts" / "PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md")
    dataset_hash = memory["monte_carlo"]["sha256"]
    require(
        "Thesis_Final_Unique_Papers_325_2026-08-20(1).csv" in prompt,
        "Frozen logical dataset filename drift",
    )
    require(dataset_hash in prompt, "Frozen dataset SHA-256 drift")
    require("325" in prompt and "34" in prompt, "Frozen dataset shape declaration missing")

    # 6. High-rigor archive copy identity.
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

    # 8. Root README alignment with corrected v2 memory.
    root_readme = read(ROOT / "README.md")
    require(demonstrator in root_readme, "Root README demonstrator drifted from authoritative scope")
    require(
        "project_memory/2026-08-21_chain_architecture_v2" in root_readme,
        "Root README does not point to corrected v2 memory",
    )
    require(
        "dynamic coupling" in root_readme.lower()
        and "admissibility" in root_readme.lower()
        and "viability" in root_readme.lower()
        and "recovery" in root_readme.lower(),
        "Root README no longer exposes the core MSE architecture",
    )

    # 9. Correction-log guardrail: the intermediate nu-notation claim must remain retracted.
    correction_log = read(CAPSULE / "14_CORRECTION_LOG.md")
    require("typo claim is retracted" in correction_log.lower(), "Retracted audit finding is not documented")

    print("PASS: corrected thesis memory capsule invariants are consistent with authoritative repository files.")


if __name__ == "__main__":
    main()
