# P3.0.1 Execution-Gate Semantics Amendment v1

**Status:** CANONICAL NARROW CORRECTION TO P3 CONTROL PLANE  
**Effective date:** 2026-09-20  
**Parent:** P3_CASE_DATA_EXECUTION_READINESS_PROTOCOL_V1.md  
**Scope:** execution-gate semantics only  
**Case:** AUS-P5U-2018-V1  
**H1–H5:** NOT TESTED  
**Sustainability authority:** UNCHANGED

## 1. Case admissibility is not experiment execution readiness

~~~math
\boxed{
G_{case,adm}
=
\text{Austin final-case admissibility under the case contract}.
}
~~~

~~~math
\boxed{
G_{repo,exec}
=
G_{runner}
\land
G_{syntax}
\land
G_{tests}
\land
G_{authority\_lint}
\land
G_{case\_instrument}.
}
~~~

~~~math
\boxed{
\mathcal O_{req}(E)
=
\text{scientific objects required by experiment }E.
}
~~~

~~~math
\boxed{
G_E^{objects}
=
\bigwedge_{o\in\mathcal O_{req}(E)}
G_o^{ready}.
}
~~~

~~~math
\boxed{
G_{exp,exec}(E)
=
G_{case,adm}
\land
G_{repo,exec}
\land
G_E^{objects}.
}
~~~

Only G_{exp,exec}(E)=PASS authorizes confirmatory execution.

~~~math
\boxed{
G_{case,adm}
\neq
G_{repo,exec}
\neq
G_E^{objects}
\neq
G_{exp,exec}.
}
~~~

Current state:

~~~math
\boxed{
G_{case,adm}=BLOCKED,
\qquad
G_{repo,exec}=BLOCKED,
\qquad
G_{exp,exec}=BLOCKED.
}
~~~

## 2. Runner assignment is explicit

G_runner=PASS requires evidence that a workflow job was assigned a runner and recorded at least its first executable workflow step.

Both observed attempts show:

~~~text
runner_id = 0
runner_name = ""
recorded_step_count = 0
conclusion = failure
~~~

Therefore:

~~~text
CLASSIFICATION = PRE_RUNNER_ASSIGNMENT_FAILURE
~~~

and G_runner=BLOCKED.

~~~math
\boxed{
\text{PRE-RUNNER ASSIGNMENT FAILURE}
\neq
\text{test failure}
\neq
\text{data qualification failure}
\neq
H_i\text{ evidence}.
}
~~~

## 3. Feeder notation remains feeder-specific

~~~math
\boxed{
G_f
=
G_P(f)
\land
G_T(f)
\land
G_S(f)
\land
G_H(f)
\land
G_V(f).
}
~~~

~~~math
\mathcal F_{adm}
=
\{f:G_f=PASS\}.
~~~

The earlier F_required(experiment) expression is superseded. Experiment readiness uses \mathcal O_{req}(E), so feeder f is never overloaded as a generic execution object.

## 4. Runner-attempt evidence is versioned

Authoritative record:

~~~text
project/global_integration/P3_RUNNER_ASSIGNMENT_OBSERVATION_V1_2026-09-20.json
~~~

It records RUN_ID, RUN_ATTEMPT, JOB_ID, HEAD_SHA, requested runner label, RUNNER_ID, RUNNER_NAME, RECORDED_STEP_COUNT, CONCLUSION, CLASSIFICATION, and OBSERVED_AT for the first attempt and controlled retry.

## 5. Machine-output semantics

The readiness instrument emits:

~~~text
case_admissibility_status
repository_execution_status
experiment_object_readiness_status
experiment_execution_status
~~~

It must never infer experiment execution PASS from case admissibility alone.

Until a versioned \mathcal O_{req}(E) mapping and object-readiness record exist:

~~~text
experiment_object_readiness_status = BLOCKED
required_object_set_status = OPEN_NOT_FROZEN
~~~

## 6. Empirical firewall

~~~math
\boxed{
G_{P3.0.1}^{control}=PASS
\not\Rightarrow
G_{case,adm}=PASS
\not\Rightarrow
G_{exp,exec}=PASS
\not\Rightarrow
H_i=SUPPORTED.
}
~~~

This amendment changes execution semantics only. It does not alter H1–H5, case data, feeder outcomes, parameter values, or sustainability scope.
