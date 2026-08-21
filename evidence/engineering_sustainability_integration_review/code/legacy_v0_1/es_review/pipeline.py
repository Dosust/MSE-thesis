from __future__ import annotations
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Mapping
import json

from .config import FrameworkConfig
from .models import PaperRecord
from .pdf_io import extract_pdf_pages
from .retrieval import retrieve_four_passes
from .scoring import score_paper
from .validation import validate_all
from .workbook_builder import build_workbook

class ReviewPipeline:
    """Deterministic orchestration layer.

    This class does NOT invent paper-specific evidence. It:
      - extracts PDF text,
      - retrieves candidate passages,
      - accepts explicitly coded evidence,
      - computes scores from coded evidence,
      - validates invariants,
      - builds workbook.
    """

    def __init__(self, config: FrameworkConfig | None = None):
        self.config = config or FrameworkConfig()

    def retrieve_candidates(self, record: PaperRecord) -> Dict[str, List[dict]]:
        pages = extract_pdf_pages(record.pdf_path)
        return retrieve_four_passes(pages)

    def score_records(self, records: List[PaperRecord]) -> List[PaperRecord]:
        for r in records:
            r.scores = score_paper(r)
        return records

    def validate(self, records: List[PaperRecord]) -> None:
        validate_all(records, self.config)

    def build(
        self,
        records: List[PaperRecord],
        evidence_symbols: Mapping[str, Mapping[str, str]],
        performance_mapping: Mapping[str, Mapping[str, int]],
        outcome_mapping: Mapping[str, Mapping[str, int]],
        output_path: str,
    ) -> str:
        self.score_records(records)
        self.validate(records)
        return build_workbook(
            records,
            evidence_symbols,
            performance_mapping,
            outcome_mapping,
            output_path,
            self.config,
        )
