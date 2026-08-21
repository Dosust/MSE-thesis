from __future__ import annotations
from typing import Dict, Iterable, Tuple

from .enums import YesNo, EvidenceStatus, Provenance, MethodFamily
from .models import PaperRecord, Scores
from .rules import method_essential_status, linkage_from_integration

def _score_range_check(v: int, name: str) -> None:
    if not isinstance(v, int) or not 0 <= v <= 3:
        raise ValueError(f"{name} must be integer 0..3; got {v!r}")

def score_R1(record: PaperRecord) -> int:
    """Depth/completeness of structured sustainability-method implementation."""
    if record.screening is None:
        raise ValueError("KLM screening not assigned.")

    if record.screening.SM == YesNo.NO:
        return 0

    # For KLM-eligible papers, direct method implementation exists.
    # R1=3 requires operational components + procedure + outputs.
    has_components = bool(record.O_core_elements.strip())
    has_procedure = bool(record.P_procedure.strip())
    has_s_outputs = bool(record.pfsd.sustainability)
    has_method_generated = any(s.method_generated for s in record.pfsd.sustainability)

    if has_components and has_procedure and has_s_outputs and has_method_generated:
        return 3
    return 2

def score_R2(record: PaperRecord) -> int:
    """Method-family-specific reproducibility; no generic percentage threshold."""
    essentials = method_essential_status(record)

    if not essentials:
        # "Other" method: fail closed unless explicit component set was supplied.
        if not record.method_components:
            return 1
        vals = list(record.method_components.values())
    else:
        vals = list(essentials.values())

    # Normalize statuses from strings; "NR"/"U" are essential gaps.
    unresolved = sum(v in ("NR", "U", "", None) for v in vals)
    adequate = sum(v not in ("NR", "U", "", None, "PARTIAL") for v in vals)
    partial = sum(v == "PARTIAL" for v in vals)

    if not vals or adequate == 0:
        return 0
    if adequate <= max(1, len(vals)//3):
        return 1
    if unresolved == 0 and partial == 0:
        return 3
    return 2

def score_R3(record: PaperRecord) -> int:
    """Strength of focal-author-generated engineering evidence."""
    if not record.pfsd.performance:
        return 0

    author = [p for p in record.pfsd.performance if p.author_generated]
    if not author:
        return 1

    def strong(p):
        return all([
            p.method.strip(),
            p.metric.strip(),
            p.result.strip(),
            p.alternative.strip(),
        ])

    if any(strong(p) for p in author):
        return 3
    return 2

def score_R4(record: PaperRecord) -> int:
    """Strength/completeness of quantified sustainability outputs."""
    if record.screening is None:
        raise ValueError("KLM screening not assigned.")

    if record.screening.M == YesNo.NO:
        return 0

    if not record.pfsd.sustainability:
        return 1

    generated = [s for s in record.pfsd.sustainability if s.method_generated]
    if not generated:
        return 1

    def strong(s):
        return all([
            s.method.strip(),
            s.indicator.strip(),
            s.result.strip(),
            s.alternative.strip(),
        ]) and bool(s.unit.strip() or s.dimension.value == "Integrated")

    if any(strong(s) for s in generated):
        return 3
    return 2

def score_paper(record: PaperRecord) -> Scores:
    r1 = score_R1(record)
    r2 = score_R2(record)
    r3 = score_R3(record)
    r4 = score_R4(record)
    lam = linkage_from_integration(record)

    scores = Scores(r1, r2, r3, r4, lam)
    for name, value in zip(("R1","R2","R3","R4","lambda"), scores.vector()):
        _score_range_check(value, name)
    return scores

def is_perfect(scores: Scores) -> bool:
    return scores.vector() == (3, 3, 3, 3, 3)

def is_tier_a(scores: Scores) -> bool:
    r1, r2, r3, r4, lam = scores.vector()
    return r1 == 3 and r2 >= 2 and r3 == 3 and r4 == 3 and lam >= 2
