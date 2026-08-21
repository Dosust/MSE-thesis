from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Tuple
import re

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()

def extract_pdf_pages(pdf_path: str) -> List[str]:
    """Extract page text using PyMuPDF. No OCR is performed."""
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(pdf_path)
    try:
        import fitz  # PyMuPDF
    except ImportError as exc:
        raise RuntimeError("PyMuPDF (fitz) is required for PDF text extraction.") from exc

    doc = fitz.open(str(path))
    pages = []
    for page in doc:
        pages.append(page.get_text("text") or "")
    return pages

def join_pages(pages: List[str]) -> str:
    return "\n\n".join(f"[PAGE {i+1}]\n{t}" for i, t in enumerate(pages))

def find_candidate_passages(
    pages: List[str],
    keywords: List[str],
    context_chars: int = 450,
) -> List[Dict[str, object]]:
    """Keyword retrieval only. It does not classify evidence."""
    results = []
    seen = set()
    for page_no, text in enumerate(pages, start=1):
        lower = text.lower()
        for kw in keywords:
            start = 0
            kw_l = kw.lower()
            while True:
                idx = lower.find(kw_l, start)
                if idx < 0:
                    break
                left = max(0, idx - context_chars)
                right = min(len(text), idx + len(kw) + context_chars)
                snippet = text[left:right].strip()
                key = (page_no, kw_l, snippet[:120])
                if key not in seen:
                    seen.add(key)
                    results.append({
                        "page": page_no,
                        "keyword": kw,
                        "snippet": snippet,
                    })
                start = idx + max(1, len(kw))
    return results

def section_guess(text: str) -> str:
    """Conservative section hint; not evidence."""
    t = text.lower()
    for sec in [
        "abstract", "introduction", "methods", "methodology", "materials",
        "experimental", "results", "discussion", "conclusion", "references"
    ]:
        if sec in t[:180]:
            return sec.title()
    return ""
