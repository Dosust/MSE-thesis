#!/usr/bin/env bash
set -euo pipefail

# Rebuild the publication-style PDF from the archived Stage-1 scientific record.
# Requirements: pandoc + xelatex + DejaVu Sans fonts.

HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

TMP="Stage1_Multilayer_Network_of_Networks_Full_Record_COMBINED.md"
OUT="Stage1_Multilayer_Network_of_Networks_Full_Record.pdf"

cat > "$TMP" <<'EOF'
---
title: "Stage 1 - Multilayer Network-of-Networks"
subtitle: "Full Scientific Record and Canonical Modeling Specification"
author: "MSE Thesis Project"
date: "2026-09-09"
geometry: margin=0.75in
fontsize: 10pt
mainfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
colorlinks: true
linkcolor: blue
urlcolor: blue
---
EOF

cat 01_FULL_SCIENTIFIC_RECORD.md >> "$TMP"
printf '\n\\newpage\n' >> "$TMP"
cat 02_CANONICAL_STAGE1_SPECIFICATION.md >> "$TMP"
printf '\n\\newpage\n' >> "$TMP"
cat 03_INTERDEPENDENCY_REGISTER_TEMPLATE.md >> "$TMP"
printf '\n\\newpage\n' >> "$TMP"
cat 04_REFERENCES.md >> "$TMP"

# Convert fenced ```math blocks to display-math delimiters for Pandoc/LaTeX.
python3 - "$TMP" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1])
lines=p.read_text(encoding='utf-8').splitlines()
out=[]
in_math=False
for line in lines:
    if line.strip() == '```math':
        out.append('$$'); in_math=True
    elif in_math and line.strip() == '```':
        out.append('$$'); in_math=False
    else:
        out.append(line)
p.write_text('\n'.join(out)+'\n', encoding='utf-8')
PY

pandoc "$TMP" -o "$OUT" \
  --pdf-engine=xelatex \
  --toc \
  --number-sections \
  -V papersize=a4 \
  -V geometry:margin=0.75in \
  -V mainfont='DejaVu Sans' \
  -V monofont='DejaVu Sans Mono' \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue

rm -f "$TMP"
echo "Built: $OUT"
