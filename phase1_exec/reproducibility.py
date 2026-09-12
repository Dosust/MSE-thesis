"""Deterministic seed derivation and run-identity helpers."""
import hashlib
from typing import Iterable


MASTER_SEED = 20260912


def derive_seed(run_id: str, master_seed: int = MASTER_SEED) -> int:
    payload = f"{master_seed}|{run_id}".encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    return int(digest[:16], 16)


def sha256_text(parts: Iterable[str]) -> str:
    digest = hashlib.sha256()
    for part in parts:
        digest.update(part.encode("utf-8"))
    return digest.hexdigest()
