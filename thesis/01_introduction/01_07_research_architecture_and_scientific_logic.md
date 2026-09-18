# 1.7 Research Framework and Logic

Section 1.6 defined the validity domain of the study. Within that domain, Section 1.7 provides the **reader-facing architecture** that connects critical-service requirements, scientific objects, stage outputs, acceptance gates, and engineering decisions. It does not reproduce the physical Power–Transportation system as a literal seven-step process, and it does not duplicate the detailed mathematics or experiments of Chapters 3 and 4.

The framework preserves two complementary views:

```math
\boxed{
\text{System of Systems}=\text{architecture},
\qquad
\text{complex dynamical system}=\text{behavior}.
}
```

The physical core remains (P+T), with Information and Organization represented as supporting domains that affect observation, interpretation, coordination, resources, authority, and feasible action. Critical-service requirements are an **input to the framework**, not an additional research stage.

The canonical scientific progression is

```math
\boxed{
\begin{aligned}
\text{Critical Service Requirements}
&\rightarrow
\text{Spatiotemporal Multilayer System-of-Systems Structure}\\
&\rightarrow
\text{Evidence-Grounded Causal Interdependencies}\\
&\rightarrow
\text{Physics-Based Hybrid Multiscale Dynamics}\\
&\rightarrow
\text{Observation, State Estimation, Organization and Control}\\
&\rightarrow
\text{Uncertainty-Aware Viability and Reachability Resilience}\\
&\rightarrow
\text{Resilience Diagnosis, Engineering Intervention and Sustainability Consequences}\\
&\rightarrow
\text{Engineering Decision and Adaptive Transformation}.
\end{aligned}}
```

This order expresses **scientific dependency**, not irreversible chronology. Later evidence may require controlled revision of an earlier representation.

## 1.7.1 Analytical foundation and stage contract

Systems thinking motivates the progression from visible events toward the structures, mechanisms, and rules that generate them:

```math
\boxed{
\text{Event}
\rightarrow
\text{Pattern}
\rightarrow
\text{Structure}
\rightarrow
\text{Mechanism / Rule}.
}
```

Systems engineering supplies the complementary discipline of moving from service needs to requirements, architecture, interfaces, verification obligations, design alternatives, and decisions. The thesis therefore keeps architectural, dynamical, observation/control, and performance/decision viewpoints distinct.

Each research stage is represented by the compact scientific contract

```math
\boxed{
\Gamma_k
=
\left(
RQ_k,,
I_k,,
\Phi_k,,
Z_k,,
A_k,,
\Xi_k
\right),
}
```

where (RQ_k) is the canonical research-question identifier, (I_k) the qualified inputs, (Phi_k) the stage transformation, (Z_k) the output, (A_k) the declared assumptions and constraints, and (Xi_k) the credibility obligation. The exact wording of RQ1–RQ7 is preserved in Section 1.9 and is not replaced here by alternative questions.

## 1.7.2 Seven-stage specification

The seven rows below define the Chapter-I scientific specification. Detailed equations, algorithms, parameterizations, and confirmatory test designs are deferred to Chapters 3 and 4.

| Stage | RQ | Scientific function | Principal output | Minimum credibility / handoff obligation |
|---|---|---|---|---|
| **1. Spatiotemporal Multilayer System-of-Systems Structure** | RQ1 | Define the bounded (P\!-!T\!-!I\!-!O) architecture, locations, states, services, and candidate interfaces | ((\mathcal S,\mathcal G,X,Y)) | Boundary consistency, provenance, topology checks, spatial/temporal compatibility |
| **2. Evidence-Grounded Causal Interdependencies** | RQ2 | Qualify directional source–mechanism–receiver relations and their activation/validity conditions | (\mathbb I(x,t,Y,m)=\{\mathfrak d_e\}) | Mechanism evidence, directionality, activation conditions, uncertainty and validity domain |
| **3. Physics-Based Hybrid Multiscale Dynamics** | RQ3 | Translate accepted mechanisms into coupled state-, time-, hazard-, and mode-dependent behavior | (F_{\mathcal G}^{m}), (Y(x,t)), (Q(x,t)) | Dimensional/limiting checks, numerical verification, comparator consistency and available physical validation |
| **4. Observation, State Estimation, Organization and Control** | RQ4 | Connect physical state to what can be observed, inferred, authorized, coordinated, and executed | ((\widehat Y_t,p(Y_t\mid\mathcal I_t),\mathcal U_t,u_t)) | Observation/estimation adequacy, explicit information/organization assumptions, feasible-control consistency |
| **5. Uncertainty-Aware Viability and Reachability Resilience** | RQ5 | Determine **remain + return + confidence** under feasible controls and uncertainty | (\mathfrak R_T) | Service set (K(t)), feasible controls, viability/reachability computation, UQ, and comparison with conventional performance/recovery information |
| **6. Resilience Diagnosis, Engineering Intervention and Sustainability Consequences** | RQ6 | Convert resilience diagnosis into candidate interventions, quantify effectiveness/resource/sustainability consequences, and derive sustainability requirements within declared boundaries | (\mathcal D_R), (\mathcal C(a_k)), derived sustainability requirements | Preserve effectiveness (\neq) efficiency (\neq) sustainability; qualify accounting boundaries, metric admission, feasibility and uncertainty |
| **7. Engineering Decision and Adaptive Transformation** | RQ7 | Compare defensible transformations and, where separately justified, intervention sequences | (\mathcal A_{R,S}^{\star}) and conditional transformation sequence | Feasibility, dominance/robustness, uncertainty sensitivity, and no unsupported scalar aggregation |

Stage 5 therefore preserves the canonical resilience interpretation

```math
\boxed{
\textbf{Resilience}
=
\underbrace{\text{remain}}_{\text{viability}}
+
\underbrace{\text{return}}_{\text{reachability}}
+
\underbrace{\text{confidence}}_{\text{probability}},
}
```

where the plus signs indicate conceptual composition rather than numerical addition. Stage 6 preserves

```math
\boxed{
u(t)=\text{operate the existing system},
\qquad
a_k=\text{change the system},
}
```

and the intervention-performance distinction

```math
\boxed{
\text{effectiveness}
\neq
\text{resource efficiency}
\neq
\text{sustainability}.
}
```

## 1.7.3 Cross-cutting scientific control

The seven stages specify **what the thesis investigates**. Scientific-control practices specify **how claims are allowed to become defensible**. Systems engineering, evidence qualification, experimental design, verification, validation, uncertainty quantification, statistical inference, and reproducibility therefore act across the architecture rather than as an eighth stage:

```math
\boxed{
\text{Stages }1\text{--}7
\subset
\text{scientific control + V\&V + UQ + reproducibility}.
}
```

Verification, validation, and uncertainty quantification remain distinct:

```math
\boxed{
\text{verification}
\neq
\text{validation}
\neq
\text{uncertainty quantification}.
}
```

Hypothesis-bearing stages use controlled comparators and non-support criteria defined in Section 1.11 and operationalized in Chapter 4. RQ1 and RQ2 instead carry developmental and evidence-qualification obligations supporting H1; the thesis therefore does not invent additional hypotheses merely to make the number of hypotheses equal the number of research questions.

## 1.7.4 Scientific handoffs, traceability, and controlled iteration

A stage output is authorized for downstream use only after its acceptance gate is evaluated. Let

```math
\boxed{
s_k
=
\operatorname{Gate}_k
\left(
Z_k,E_k;\Lambda_k
\right)
\in
\{
\mathrm{PASS},
\mathrm{FAIL},
\mathrm{BLOCKED}
\},
}
```

where (E_k) denotes the evidence supporting (Z_k) and (\Lambda_k) the declared acceptance criteria. Forward progression requires

```math
\boxed{
s_k=\mathrm{PASS}
\quad\Rightarrow\quad
Z_k\rightarrow I_{k+1}.
}
```

The three gate states have different meanings:

```math
\boxed{
\begin{aligned}
\mathrm{PASS} &: \text{required acceptance evidence is satisfied},\\
\mathrm{FAIL} &: \text{a required criterion is demonstrably violated},\\
\mathrm{BLOCKED} &: \text{required evidence or a prerequisite is unavailable}.
\end{aligned}}
```

Hence,

```math
\boxed{\mathrm{BLOCKED}\neq\mathrm{FAIL}.}
```

A FAIL triggers diagnosis, revision of the earliest scientifically implicated object, and re-execution of affected downstream stages. A BLOCKED state triggers acquisition or qualification of the missing evidence or prerequisite and subsequent re-gating; it is not evidence that the model or hypothesis is false.

Traceability is maintained bidirectionally:

```math
\boxed{
G
\leftrightarrow
RQ
\leftrightarrow
SO
\leftrightarrow
(H/\text{obligation})
\leftrightarrow
M
\leftrightarrow
T
\leftrightarrow
R
\leftrightarrow
C.
}
```

This chain links evidence-supported gaps to questions, objectives, hypotheses or developmental obligations, models, tests, results, and bounded conclusions. Material revision of an accepted upstream object requires reevaluation of dependent downstream claims.

The two Chapter-I figures therefore have deliberately different roles:

```math
\boxed{
\text{Figure 1.X}
=
\text{what the seven-stage research architecture is},
}
```

```math
\boxed{
\text{Figure 1.Y}
=
\text{how evidence is accepted, rejected, blocked, traced, and iterated through it}.
}
```

Section 1.7 thus closes the framework portion of the Chapter-I research contract without importing the full mathematical derivations or experiment specifications of later chapters. Section 1.8 next states the single overarching research objective consistent with RQ0 and this seven-stage architecture.
