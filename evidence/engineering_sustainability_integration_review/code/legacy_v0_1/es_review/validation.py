from __future__ import annotations
from typing import Iterable, List

from .config import FrameworkConfig
from .enums import YesNo, FormulaType, IntegrationClass
from .models import PaperRecord
from .rules import F3, method_essential_status
from .scoring import is_perfect

class FrameworkValidationError(ValueError):
    pass

def validate_manifest(records: List[PaperRecord], config: FrameworkConfig) -> None:
    if len(records) != config.expected_papers:
        raise FrameworkValidationError(
            f"Expected {config.expected_papers} papers; got {len(records)}."
        )
    ids = [r.paper_id for r in records]
    dois = [r.doi.strip().lower() for r in records]
    if len(ids) != len(set(ids)):
        raise FrameworkValidationError("Duplicate Paper_ID detected.")
    if len(dois) != len(set(dois)):
        raise FrameworkValidationError("Duplicate DOI detected.")

def validate_paper(record: PaperRecord) -> None:
    if record.screening is None:
        raise FrameworkValidationError(f"{record.paper_id}: missing KLM screening.")
    if record.scores is None:
        raise FrameworkValidationError(f"{record.paper_id}: missing scores.")

    r1, r2, r3, r4, lam = record.scores.vector()

    if record.screening.SM == YesNo.NO and r1 == 3:
        raise FrameworkValidationError(f"{record.paper_id}: SM=No contradicts R1=3.")

    if record.screening.M == YesNo.NO and r4 == 3:
        raise FrameworkValidationError(f"{record.paper_id}: M=No contradicts R4=3.")

    if r3 == 3 and not any(p.author_generated for p in record.pfsd.performance):
        raise FrameworkValidationError(
            f"{record.paper_id}: R3=3 requires focal-author-generated engineering evidence."
        )

    if r4 == 3 and not any(s.method_generated for s in record.pfsd.sustainability):
        raise FrameworkValidationError(
            f"{record.paper_id}: R4=3 requires method-generated sustainability output."
        )

    if lam > 0 and not any(x.traceable_alternatives for x in record.pfsd.integration):
        raise FrameworkValidationError(
            f"{record.paper_id}: lambda>0 requires traceable alternative correspondence."
        )

    if lam == 3:
        valid_f3 = [
            x for x in record.pfsd.integration
            if x.integration_class in F3
            and x.traceable_alternatives
            and x.author_integrated_architecture
            and x.formula_type != FormulaType.REVIEWER_RECONSTRUCTION
        ]
        if not valid_f3:
            raise FrameworkValidationError(
                f"{record.paper_id}: lambda=3 lacks valid author-implemented F3 architecture."
            )

    if r2 == 3:
        essentials = method_essential_status(record)
        if essentials and any(v in ("NR","U","",None,"PARTIAL") for v in essentials.values()):
            raise FrameworkValidationError(
                f"{record.paper_id}: R2=3 conflicts with missing/partial essential method component."
            )

    if is_perfect(record.scores):
        if record.scores.vector() != (3,3,3,3,3):
            raise FrameworkValidationError(f"{record.paper_id}: impossible perfect-state inconsistency.")

def validate_all(records: List[PaperRecord], config: FrameworkConfig) -> None:
    validate_manifest(records, config)
    for r in records:
        validate_paper(r)
