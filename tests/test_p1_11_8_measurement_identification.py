from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def test_p1118_source_registered():
    txt = read("thesis/02_literature_theory/02_00c_accepted_core_evidence.md")
    assert "A-039" in txt
    assert "10.1016/j.jeconom.2026.106339" in txt

def test_p1118_identification_gate():
    txt = read("project/CANONICAL_MEASUREMENT_ERROR_IDENTIFICATION_AMENDMENT_V1_8.md")
    assert "G_{\\rm ID}" in txt
    assert "G_2^{causal}(e)=PASS" in txt
    assert "G_{\\rm ID}(\\theta_e)=BLOCKED" in txt

def test_p1118_no_default_gmm():
    txt = read("project/CANONICAL_MEASUREMENT_ERROR_IDENTIFICATION_AMENDMENT_V1_8.md")
    assert "No default GMM or 2SLS" in txt
    assert "default P--T estimator" in txt

def test_p1118_stage3_empirical_gate():
    txt = read("project/stage3/STAGE3_EMPIRICAL_PARAMETER_IDENTIFICATION_READINESS_AMENDMENT_V2_1.md")
    assert "G_{\\theta}^{emp}" in txt
    assert "G_{\\rm ID}" in txt
    assert "G_{\\rm EST}" in txt

def test_p1118_stage4_distinctions():
    txt = read("project/stage4/00_governance/STAGE4_MEASUREMENT_IDENTIFICATION_ESTIMATION_AMENDMENT_V1_4.md")
    assert "observability" in txt
    assert "identifiability" in txt
    assert "numerical convergence" in txt

def test_p1118_stage6_resolution():
    txt = read("project/stage6/03_accounting/STAGE6_QUANTITY_ORIGIN_AND_UNCERTAINTY_AMENDMENT_V1_2.md")
    assert "G_{\\rm resolve}" in txt
    assert "No universal rule" in txt

def test_p1118_source_hash():
    txt = read("project/global_integration/P1_11_SOURCE_DOCUMENT_PROVENANCE_REGISTER_V1.md")
    assert "5e992b17581712c31e8b0d38c8d656821a9a0414cf4ca9bc2ed16c7c8e124d54" in txt
