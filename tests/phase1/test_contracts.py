from phase1_exec.contracts import (
    CausalSemantics,
    Composition,
    Dependency,
    Epistemic,
    evaluate_dependency,
)


def test_guard_zero_disables_only_dependency():
    dep = Dependency(
        Composition("T", "out", "P", "load", "power"),
        CausalSemantics(
            operator=lambda source, receiver, params, state: params["gain"] * source,
            guard=lambda context: bool(context["active"]),
            parameters={"gain": 2.0},
        ),
        Epistemic(("synthetic-test",), "verification-only"),
    )
    assert evaluate_dependency(dep, 3.0, 0.0, {"active": False}) == 0.0
    assert evaluate_dependency(dep, 3.0, 0.0, {"active": True}) == 6.0
