#!/usr/bin/env python3
"""Normalize active thesis Markdown to GitHub-safe mathematical block syntax.

Purpose
-------
GitHub supports both dollar-delimited display math and fenced ``math`` blocks,
but multiline ``$$`` blocks can become raw LaTeX when Markdown line-break
parsing interacts with surrounding content. This formatter converts only
standalone multiline ``$$`` blocks to fenced ``math`` blocks.

Scientific content is not changed. Equation bodies are copied byte-for-byte
except for the opening/closing display delimiters.

Historical/provenance material is excluded deliberately.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ACTIVE_ROOTS = (
    ROOT / "project",
    ROOT / "methods",
    ROOT / "figures",
    ROOT / "evidence",
)
ROOT_FILES = (ROOT / "README.md", ROOT / "PROJECT_MEMORY.md")

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


def excluded(path: Path) -> bool:
    if path.name in EXCLUDED_FILES:
        return True
    return any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts)


def markdown_files() -> list[Path]:
    files = [p for p in ROOT_FILES if p.exists()]
    for base in ACTIVE_ROOTS:
        if base.exists():
            files.extend(p for p in base.rglob("*.md") if not excluded(p))
    return sorted(set(files))


def normalize_text(text: str) -> tuple[str, int]:
    """Convert standalone multiline $$ blocks outside fenced code regions."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    conversions = 0
    in_fence = False
    fence_prefix = ""

    while i < len(lines):
        line = lines[i]
        stripped_left = line.lstrip()
        stripped = line.strip()

        if stripped_left.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_prefix = "```"
            elif stripped_left.startswith(fence_prefix):
                in_fence = False
                fence_prefix = ""
            out.append(line)
            i += 1
            continue

        if not in_fence and stripped == "$$":
            indent = line[: len(line) - len(line.lstrip())]
            j = i + 1
            body: list[str] = []

            while j < len(lines):
                candidate = lines[j]
                if candidate.strip() == "$$":
                    break
                body.append(candidate)
                j += 1

            # Convert only a complete pair. An unmatched delimiter is left for
            # the linter to report rather than guessed at or silently repaired.
            if j < len(lines) and lines[j].strip() == "$$":
                newline = "\n" if line.endswith("\n") else ""
                out.append(f"{indent}```math{newline}")
                out.extend(body)
                closing_newline = "\n" if lines[j].endswith("\n") else ""
                out.append(f"{indent}```{closing_newline}")
                conversions += 1
                i = j + 1
                continue

        out.append(line)
        i += 1

    normalized = "".join(out)
    return normalized, conversions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write normalized files in place")
    args = parser.parse_args()

    changed: list[tuple[Path, int]] = []
    for path in markdown_files():
        original = path.read_text(encoding="utf-8")
        normalized, count = normalize_text(original)
        if normalized != original:
            changed.append((path, count))
            if args.write:
                path.write_text(normalized, encoding="utf-8")

    mode = "UPDATED" if args.write else "WOULD UPDATE"
    for path, count in changed:
        print(f"{mode}: {path.relative_to(ROOT)} ({count} math block(s))")

    total = sum(count for _, count in changed)
    print(f"GitHub math normalization: {len(changed)} file(s), {total} block(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
