from es_review.enums import *
from es_review.models import *
from es_review.scoring import score_paper, is_perfect, is_tier_a
from es_review.validation import validate_paper

def make_perfect():
    r=PaperRecord(
        paper_id="P01",rank=1,csv_id="1",authors="A",title="T",
        year=2025,journal="J",doi="10.test/1",pdf_path="x.pdf"
    )
    r.screening=ScreeningKLM(YesNo.YES,YesNo.YES,YesNo.YES)
    r.N_performance_effects="compressive strength"
    r.O_core_elements="1) criteria"
    r.P_procedure="input → calculation → output"
    r.Q_construction_strategy="A vs B"
    r.R_what_evaluated="Engineering + Environmental"
    r.S_validation="Internal"
    r.T_backward_snowballing="LCA"
    r.method_family=MethodFamily.MCDA
    r.method_components={
        "alternatives":"reported","criteria":"reported","weights":"reported",
        "normalization":"reported","aggregation":"reported","decision_rule":"reported",
    }
    r.pfsd.performance.append(PerformanceEvidence(
        PerformanceFamily.MECHANICAL,"compressive strength","test",
        "50","MPa","A","B",True
    ))
    r.pfsd.sustainability.append(SustainabilityEvidence(
        method="MCDM",
        method_family=MethodFamily.MCDA,
        dimension=SustainabilityDimension.INTEGRATED,
        indicator="sustainability index",
        result="0.8",
        unit="",
        functional_basis="A versus B",
        alternative="A",
        method_generated=True,
    ))
    r.pfsd.integration.append(IntegrationEvidence(
        IntegrationClass.F3B,"strength","weighted aggregation","sustainability index",
        True,"I=sum(wz)",FormulaType.AUTHOR_FORMULA,True
    ))
    r.pfsd.decisions.append(DecisionEvidence(
        DecisionType.SELECTION,"A,B","max index","A"
    ))
    r.scores=score_paper(r)
    return r

if __name__=="__main__":
    p=make_perfect()
    assert p.scores.vector()==(3,3,3,3,3), p.scores
    assert is_perfect(p.scores)
    assert is_tier_a(p.scores)
    validate_paper(p)
    print("SELF-TEST PASS", p.scores.vector())
