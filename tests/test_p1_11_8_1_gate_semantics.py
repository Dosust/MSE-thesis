from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def test_gate_admission_validation_separation():
    txt = read("project/CANONICAL_MEASUREMENT_IDENTIFICATION_GATE_SEMANTICS_AMENDMENT_V1_8_1.md")
    assert "G_{\\rm EST}^{admit}" in txt
    assert "G_{\\rm VAL}^{result}" in txt
    assert "admissible estimator" in txt
    assert "validated estimated result" in txt

def test_structural_vs_strength():
    txt = read("project/CANONICAL_MEASUREMENT_IDENTIFICATION_GATE_SEMANTICS_AMENDMENT_V1_8_1.md")
    assert "G_{\\rm ID}^{struct}" in txt
    assert "G_{\\rm ID}^{strength}" in txt
    assert "SET_PARTIAL" in txt
    assert "N_A_NONINFERENTIAL" in txt

def test_three_axis_source_status():
    txt = read("project/global_integration/GLOBAL_SOURCE_SUPPORT_CLASSIFICATION_PROTOCOL_V1_1.md")
    assert "STATUS_i=(REPO_i,SOURCE_i,CASE_i)" in txt
    assert "CASE_VALIDATED is not a source-support category" in txt
    assert "NOT_TESTED" in txt

def test_monte_carlo_classes():
    txt = read("project/global_integration/GLOBAL_COMPUTATIONAL_ROLE_AND_OUTPUT_CLAIM_PROTOCOL_V1_1.md")
    assert "MONTE_CARLO_METHOD_TEST" in txt
    assert "UNCERTAINTY_PROPAGATION" in txt
    assert "CASE_VALIDATION" in txt

def test_stage3_two_level_parameter_gate():
    txt = read("project/stage3/STAGE3_EMPIRICAL_PARAMETER_IDENTIFICATION_READINESS_AMENDMENT_V2_1_1.md")
    assert "G_{\\theta,e}^{pre}" in txt
    assert "G_{\\theta,e}^{ready}" in txt
    assert "G_{\\rm EST}^{admit}" in txt
    assert "G_{\\rm VAL}^{result}" in txt

def test_stage4_corrected_chain():
    txt = read("project/stage4/00_governance/STAGE4_MEASUREMENT_IDENTIFICATION_ESTIMATION_AMENDMENT_V1_4_1.md")
    assert "G_{\\rm ID}^{struct}" in txt
    assert "G_{\\rm ID}^{strength}" in txt
    assert "result_validation_status" in txt

def test_sustainability_unchanged():
    txt = read("project/CANONICAL_MEASUREMENT_IDENTIFICATION_GATE_SEMANTICS_AMENDMENT_V1_8_1.md")
    assert "\\mathbf r_{\\rm core}" in txt
    assert "C_{\\rm direct}" in txt
    assert "E_{\\rm op}" in txt
    assert "CO_{2e}" in txt
