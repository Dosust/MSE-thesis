#!/usr/bin/env python3
"""Static QA for active thesis Markdown, notation, and configuration.

The linter is intentionally conservative. It does not judge scientific truth; it
checks repository presentation contracts that can be tested deterministically:
GitHub-safe mathematical delimiters, malformed tables/fences, stale active
ontology tokens, and machine-readable authority invariants.

Historical/provenance trees are excluded so the audit preserves research history
rather than rewriting it.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - CI installs PyYAML
    yaml = None

ROOT = Path(__file__).resolve().parents[1]

ACTIVE_MARKDOWN_ROOTS = (
    ROOT / "project",
    ROOT / "methods",
    ROOT / "figures",
    ROOT / "evidence",
)
ROOT_MARKDOWN = (ROOT / "README.md", ROOT / "PROJECT_MEMORY.md")

EXCLUDED_PARTS = {
    "archive",
    "research_archive",
    "conversation",
    "project_memory",
    "99_manifest",
    "provenance",
    "prompts",
    "research_memory",
}
EXCLUDED_FILES = {
    "ADAPTIVE_VISUAL_CI_EXCEPTION_2026-08-22.md",
}

# These terms are forbidden only in active thesis-authority / implementation
# paths. Evidence-review records are allowed to preserve their local vocabulary.
DRIFT_SCAN_PREFIXES = (
    "project/",
    "methods/architecture/",
    "config/",
    "schemas/",
)
DRIFT_TERMS = {
    "P–W–T–SW": "superseded P–W–T–SW ontology",
    "P-W-T-SW": "superseded P-W-T-SW ontology",
    "solid_waste": "superseded solid-waste state/configuration",
    "waste_drainage": "superseded waste–drainage mechanism",
    "pwtsw": "superseded P-W-T-SW identifier",
}

TAG_RE = re.compile(r"\\tag\s*\{")
OLD_DISPLAY_OPEN_RE = re.compile(r"(?<!\\)\\\[")
OLD_DISPLAY_CLOSE_RE = re.compile(r"(?<!\\)\\\]")
LONG_BOX_RE = re.compile(r"\\boxed\s*\{([^{}]|\{[^{}]*\}){120,}\}")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_excluded(path: Path) -> bool:
    if path.name in EXCLUDED_FILES:
        return True
    return any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts)


def markdown_files() -> list[Path]:
    files = [p for p in ROOT_MARKDOWN if p.exists()]
    for base in ACTIVE_MARKDOWN_ROOTS:
        if not base.exists():
            continue
        files.extend(p for p in base.rglob("*.md") if not is_excluded(p))
    return sorted(set(files))


def top_level_pipe_count(line: str) -> int:
    """Count Markdown table separators outside inline-code spans."""
    in_code = False
    escaped = False
    count = 0
    for char in line:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "`":
            in_code = not in_code
            continue
        if char == "|" and not in_code:
            count += 1
    return count


def active_drift_scan(path: Path, lines: list[str], errors: list[str]) -> None:
    rp = rel(path)
    if path in ROOT_MARKDOWN or any(rp.startswith(prefix) for prefix in DRIFT_SCAN_PREFIXES):
        for lineno, line in enumerate(lines, 1):
            lower = line.lower()
            if "msc" in lower and "mse" not in lower:
                errors.append(f"{rp}:{lineno}: active thesis text contains MSc; canonical degree is MSE")
            for token, description in DRIFT_TERMS.items():
                if token.lower() in lower:
                    errors.append(f"{rp}:{lineno}: {description}: {token!r}")


def lint_markdown(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    rp = rel(path)

    # Track fenced regions so code examples are not treated as mathematical source.
    in_fence = False
    fence_marker = ""
    dollar_delimiters = 0
    fence_count = 0

    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        left = line.lstrip()

        if left.startswith("```"):
            marker = left.split()[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker[:3]
            elif left.startswith(fence_marker):
                in_fence = False
                fence_marker = ""
            fence_count += 1
            continue

        if in_fence:
            continue

        if stripped == "$$":
            errors.append(
                f"{rp}:{lineno}: standalone $$ delimiter is fragile in GitHub Markdown; "
                "use a fenced math block for multiline display mathematics"
            )

        # A one-line display must contain both opening and closing delimiters.
        if "$$" in line and line.count("$$") == 1 and stripped != "$$":
            errors.append(
                f"{rp}:{lineno}: unmatched one-line $$ delimiter; keep both delimiters on "
                "the same line or use a fenced math block"
            )

        dollar_delimiters += line.count("$$")

        if TAG_RE.search(line):
            errors.append(f"{rp}:{lineno}: \\tag{{...}} in Markdown; use a Markdown equation label")
        if OLD_DISPLAY_OPEN_RE.search(line) or OLD_DISPLAY_CLOSE_RE.search(line):
            errors.append(
                f"{rp}:{lineno}: legacy \\[...\\] display delimiter; use a fenced math block"
            )
        if LONG_BOX_RE.search(line):
            errors.append(f"{rp}:{lineno}: oversized \\boxed{{...}}; move prose/specification outside math")

    if in_fence:
        errors.append(f"{rp}: unbalanced triple-backtick code fences")
    if dollar_delimiters % 2:
        errors.append(f"{rp}: unbalanced $$ display-math delimiters")

    # Check contiguous Markdown tables. A valid row must preserve the number of
    # top-level separators across the block.
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            block: list[tuple[int, str]] = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append((i + 1, lines[i]))
                i += 1
            if len(block) >= 2:
                counts = [top_level_pipe_count(line) for _, line in block]
                expected = counts[0]
                for (lineno, _), count in zip(block, counts):
                    if count != expected:
                        errors.append(
                            f"{rp}:{lineno}: malformed Markdown table; expected {expected} separators, found {count}"
                        )
            continue
        i += 1

    active_drift_scan(path, lines, errors)
    return errors


def lint_authority_files() -> list[str]:
    errors: list[str] = []

    stage7 = ROOT / "project" / "STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md"
    if not stage7.exists():
        errors.append("project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md: missing frozen Stage-7 authority")

    framework = ROOT / "project" / "CANONICAL_7_STAGE_FRAMEWORK.md"
    if framework.exists():
        text = framework.read_text(encoding="utf-8")
        if "Stages 1–7" not in text and "Stages 1--7" not in text and "scopes-1--7" not in text:
            errors.append("project/CANONICAL_7_STAGE_FRAMEWORK.md: framework freeze does not visibly cover Stages 1–7")

    proposition_path = ROOT / "config" / "scientific_propositions.yaml"
    hypothesis_path = ROOT / "config" / "research_hypotheses.yaml"
    if yaml is None:
        errors.append("tools/thesis_display_lint.py: PyYAML unavailable; cannot validate YAML authority registries")
    else:
        if proposition_path.exists():
            data = yaml.safe_load(proposition_path.read_text(encoding="utf-8"))
            if data.get("version") != 2:
                errors.append("config/scientific_propositions.yaml: expected version 2")
            if set(data.get("propositions", {})) != {f"P{i}" for i in range(1, 11)}:
                errors.append("config/scientific_propositions.yaml: expected proposition IDs P1–P10")
        else:
            errors.append("config/scientific_propositions.yaml: missing")

        if hypothesis_path.exists():
            data = yaml.safe_load(hypothesis_path.read_text(encoding="utf-8"))
            if set(data.get("hypotheses", {})) != {f"H{i}" for i in range(1, 6)}:
                errors.append("config/research_hypotheses.yaml: expected primary hypothesis IDs H1–H5")
            if data.get("status", {}).get("numerical_thresholds_frozen") is not False:
                errors.append("config/research_hypotheses.yaml: numerical thresholds must remain unfrozen")
        else:
            errors.append("config/research_hypotheses.yaml: missing")

    schema_path = ROOT / "schemas" / "thesis_model.schema.json"
    model_path = ROOT / "config" / "example_model.json"
    for path in (schema_path, model_path):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - linter should report all parse failures
            errors.append(f"{rel(path)}: invalid JSON: {exc}")

    return errors


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    for path in files:
        errors.extend(lint_markdown(path))
    errors.extend(lint_authority_files())

    if errors:
        print(f"THESIS DISPLAY/ONTOLOGY QA: FAIL ({len(errors)} issue(s))")
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"THESIS DISPLAY/ONTOLOGY QA: PASS ({len(files)} active Markdown files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
