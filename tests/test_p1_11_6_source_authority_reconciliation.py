from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def test_p1116_evidence_registration():
    txt = read("thesis/02_literature_theory/02_00c_accepted_core_evidence.md")
    for token in ["A-033", "A-034", "A-035", "A-036", "A-037"]:
        assert token in txt

def test_p1116_screening_not_universal_modeling():
    txt = read("project/CANONICAL_SPATIOTEMPORAL_SOS_RESILIENCE_TRANSFORMATION_LENS_V1_1.md")
    assert "mandatory **screening dimensions**" in txt
    assert "screen every dimension" in txt
    assert "model every dimension" in txt

def test_p1116_sustainability_scope_precedence():
    txt = read("project/stage6/00_governance/STAGE6_SUSTAINABILITY_SCOPE_RECONCILIATION_AMENDMENT_V2_1_1.md")
    assert "C_{\\rm direct}" in txt
    assert "E_{\\rm op}" in txt
    assert "CO_{2e}" in txt
    assert "full multi-category LCA" in txt
    assert "OUT current scope" in txt

def test_p1116_kays_hard_constraint_blocked():
    txt = read("project/CANONICAL_SUSTAINABILITY_TRAJECTORY_TRADEOFF_AMENDMENT_V1_5_1.md")
    assert "G_{K_{\\rm sus}}=BLOCKED" in txt

def test_p1116_acosta_current_name():
    assert (ROOT / "project/CANONICAL_CROSS_SYSTEM_OBSERVATIONAL_INFERENCE_AMENDMENT_V1_4_1.md").exists()

def test_p1116_source_hashes():
    txt = read("project/global_integration/P1_11_SOURCE_DOCUMENT_PROVENANCE_REGISTER_V1.md")
    hashes = [
        "cadfa029e3e313e4319a6c99436fc1b9b297339060987a12ba7264b627777b3f",
        "2ac3f57cbda6c486a27cc3f52cd83b03c07281a380800ea6a908c06f8f9b0e54",
        "f9b3133402d2e4a6e93a7fd31d2ebbdad81a19cd567b5200afdc2efdedd8b338",
        "b4253eae45c8be405065d25e7f9f4ff46fbe9c586b0587358e3a0386f5ac5e5b",
        "67d986a658aceceedec490f490534d4586d258352063295526bc6b8b0f741c71",
    ]
    for h in hashes:
        assert h in txt

def test_p1116_source_support_axis():
    txt = read("project/global_integration/GLOBAL_SOURCE_SUPPORT_CLASSIFICATION_PROTOCOL_V1.md")
    assert "REPO=PASS" in txt
    assert "SOURCE=DIRECT" in txt
    assert "CASE_VALIDATED" in txt
