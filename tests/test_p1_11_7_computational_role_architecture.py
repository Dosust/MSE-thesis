from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def test_p1117_chapter2_registration():
    txt = read("thesis/02_literature_theory/02_00c_accepted_core_evidence.md")
    assert "A-038" in txt
    assert "Li & Mostafavi" in txt
    assert "10.1038/s44304-025-00104-4" in txt

def test_p1117_computational_firewalls():
    txt = read("project/CANONICAL_COMPUTATIONAL_ROLE_ARCHITECTURE_AMENDMENT_V1_7.md")
    for phrase in [
        "physical system",
        "computed features",
        "MECHANISTIC",
        "OBSERVATIONAL",
        "DECISION",
        "data-driven post-event characterization",
        "machine learning",
        "causal identification",
    ]:
        assert phrase in txt

def test_p1117_raw_data_not_demand_notation():
    txt = read("project/stage4/00_governance/STAGE4_FEATURE_ENGINEERING_AND_REFERENCE_STATE_AMENDMENT_V1_3.md")
    assert "\\mathcal D_{\\rm raw}" in txt
    assert "existing \\(D_i\\) demand/use notation is not reused for raw data" in txt

def test_p1117_resilience_diagnostic_separation():
    txt = read("project/stage5/00_governance/STAGE5_DATA_DRIVEN_RESILIENCE_DIAGNOSTICS_AMENDMENT_V1_2.md")
    assert "\\mathfrak R_T" in txt
    assert "\\mathcal D_R" in txt
    assert "PCA" in txt

def test_p1117_source_hash():
    txt = read("project/global_integration/P1_11_SOURCE_DOCUMENT_PROVENANCE_REGISTER_V1.md")
    assert "bf60180521d59635a9df6ccfbbdca9fb3aa76967de489f7fbc0bcd1022345da2" in txt

def test_p1117_power_limitation():
    txt = read("project/CANONICAL_COMPUTATIONAL_ROLE_ARCHITECTURE_AMENDMENT_V1_7.md")
    assert "power outages" in txt
    assert "do not provide direct evidence for" in txt
