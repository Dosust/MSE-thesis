from __future__ import annotations
from itertools import chain
from typing import Dict, List

from .dictionaries import P_KEYWORDS, F_KEYWORDS, S_KEYWORDS, D_KEYWORDS
from .pdf_io import find_candidate_passages

def flatten(mapping: Dict[str, List[str]]) -> List[str]:
    return list(dict.fromkeys(chain.from_iterable(mapping.values())))

def retrieve_four_passes(pages: List[str]) -> Dict[str, List[dict]]:
    """Return retrieval candidates only. No scientific code is assigned."""
    return {
        "P": find_candidate_passages(pages, flatten(P_KEYWORDS)),
        "S": find_candidate_passages(pages, flatten(S_KEYWORDS)),
        "F": find_candidate_passages(pages, flatten(F_KEYWORDS)),
        "D": find_candidate_passages(pages, D_KEYWORDS),
    }
