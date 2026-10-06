# Diagram Selection and Rendering Matrix

Use this file as a fast decision aid.

| Scientific intent | Diagram family | Time explicit? | Boundary explicit? | Best rendering |
|---|---|---:|---:|---|
| System vs environment | Context diagram | no | yes | SVG/vector |
| Component architecture | Block/internal structure | no | yes | SVG/vector |
| Input transformation | IDEF0-style | no | optional | SVG/vector |
| Ordered behavior | Activity/process | yes/order | optional | SVG/vector |
| Interaction over time | Sequence | yes | implicit lanes | SVG/vector |
| Operational modes | State machine | yes/events | no | SVG/vector |
| Heat/state propagation | Dynamic causal state-flow | yes | often | SVG/vector |
| Requirements to design variables | Relation/traceability | no | no | matrix/vector |
| Source view to target view | Transformation diagram | maybe | no | vector |
| Feasible region | Mathematical plot | parameter/time | no | Python/vector |
| Conceptual physical scene | Scientific illustration | optional | optional | generative/hybrid |
| Thesis integrated logic | Layered framework | maybe | yes | vector/hybrid |

## Default decision

If arrow direction, labels, equations, topology, or exact boundaries matter:

```text
prefer deterministic vector rendering
```

If conceptual physical appearance matters more than exact topology:

```text
generative rendering may be used
```

If both matter:

```text
hybrid draft
→ vector reconstruction
→ semantic QA
```
