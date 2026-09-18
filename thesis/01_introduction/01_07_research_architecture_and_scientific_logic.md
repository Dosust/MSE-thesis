# 1.7 Research Architecture and Scientific Logic

Section 1.6 defined the system, modeling, hazard, uncertainty, accounting, and validity boundaries of the research. Within those boundaries, the present section establishes the architecture through which the research problem is decomposed, analyzed, tested, and translated into engineering decisions. The architecture is not intended to reproduce the physical Power–Transportation system as a seven-step process. Rather, it provides a traceable organization of the scientific objects and transformations required to move from critical-service needs to evidence-supported engineering decisions.

The framework follows two complementary principles. First, the **engineering architecture** specifies what must be represented and analyzed: requirements, system structure, causal mechanisms, dynamics, observation and feasible action, resilience, intervention consequences, and decisions. Second, the **scientific methodology** specifies how claims about those objects are established. Rather than introducing a thesis-specific scientific method, this research combines hypothetico-deductive reasoning with established systems-engineering, experimental-design, verification and validation, uncertainty-quantification, statistical-inference, and reproducibility practices. ISO/IEC/IEEE 15288:2023 provides a recognized process framework applicable to systems and Systems of Systems, while NASA systems-engineering guidance similarly organizes design processes around stakeholder expectations, technical requirements, logical decomposition, design solutions, and iterative verification and validation. These standards inform the research design; the thesis does not claim formal certification or comprehensive conformity with them.

The resulting engineering logic is

\`\`\`math
\boxed{
\begin{aligned}
\text{Critical Service Requirements}
&\rightarrow
\text{Spatiotemporal SoS Structure}\\
&\rightarrow
\text{Causal Interdependencies}\\
&\rightarrow
\text{Hybrid Multiscale Dynamics}\\
&\rightarrow
\text{Observation, Estimation, Organization and Control}\\
&\rightarrow
\text{Uncertainty-Aware Viability and Reachability}\\
&\rightarrow
\text{Intervention and Sustainability Consequences}\\
&\rightarrow
\text{Engineering Decision and Transformation}.
\end{aligned}}
\`\`\`

This sequence represents **logical dependency**, not an irreversible linear workflow. Earlier representations may be revised when later verification, validation, sensitivity analysis, or evidence qualification identifies an inconsistency.

## 1.7.1 Foundations and analytical viewpoints

The architecture integrates several complementary intellectual perspectives, each with a distinct function.

**Systems thinking** provides the diagnostic reasoning introduced in Section 1.1:

\`\`\`math
\boxed{
\text{Event}
\rightarrow
\text{Pattern}
\rightarrow
\text{Structure}
\rightarrow
\text{Mechanism / Rule}.
}
\`\`\`

Its role is to prevent observable consequences—such as outages, congestion, signal failure, or delayed restoration—from being treated as sufficient explanations of system behavior. The visible event motivates investigation of recurrent patterns, the structures that permit those patterns, and the mechanisms and decision rules that generate them.

**Systems engineering** translates critical-service needs into requirements, system boundaries, functions, architectures, interfaces, design alternatives, and verification or validation obligations. NASA characterizes system design processes in terms of inputs, activities, and outputs and explicitly describes those processes as interdependent, iterative, and recursive.

The **System-of-Systems viewpoint** then provides the architectural representation of the coupled infrastructure problem, whereas the **complex-dynamical-systems viewpoint** provides its behavioral representation:

\`\`\`math
\boxed{
\text{SoS}
=
\text{architecture},
\qquad
\text{complex dynamical system}
=
\text{behavior}.
}
\`\`\`

Accordingly, the thesis is interpreted through four non-equivalent analytical viewpoints:

\`\`\`math
\boxed{
\begin{array}{lll}
\text{Architectural} &
:&
P,T,I,O,\mathcal G,\mathbb I,\\[1mm]
\text{Behavioral/dynamical} &
:&
Y,F_{\mathcal G}^{m},\eta,\theta,\\[1mm]
\text{Observation/control} &
:&
y,\hat Y,\mathcal U_t,\pi,u,\\[1mm]
\text{Performance/decision} &
:&
\mathfrak R_T,a_k,\mathbf J_{\rm sus},\mathcal A^\star .
\end{array}}
\`\`\`

This separation preserves the fundamental distinction

\`\`\`math
\boxed{
\text{structure}
\neq
\text{behavior}
\neq
\text{research method}
\neq
\text{engineering decision}.
}
\`\`\`

A structural connection is therefore not automatically interpreted as causal dependence; a simulated trajectory is not automatically interpreted as validated physical behavior; and an intervention that improves a resilience indicator is not automatically interpreted as sustainable or preferable.

Engineering design enters only after the problem and diagnosis are sufficiently defined. Service needs are translated into engineering requirements, candidate persistent transformations \(a_k\) are generated, modeled, and compared, and their consequences are evaluated. Design generation therefore supports intervention development, whereas scientific credibility is established separately through hypothesis testing, verification, validation, uncertainty analysis, and reproducibility.

## 1.7.2 Seven-stage research architecture and stage contracts

Each stage is defined as a scientific contract rather than as a descriptive box. For stage \(k\),

\`\`\`math
\boxed{
\Gamma_k
=
\left(
Q_k,\,
I_k,\,
\mathcal O_k,\,
\Phi_k,\,
A_k,\,
Z_k,\,
\Xi_k
\right),
}
\`\`\`

where

\`\`\`math
\begin{aligned}
Q_k &= \text{question addressed},\\
I_k &= \text{qualified inputs},\\
\mathcal O_k &= \text{scientific objects},\\
\Phi_k &= \text{analytical transformation},\\
A_k &= \text{assumptions and constraints},\\
Z_k &= \text{output},\\
\Xi_k &= \text{credibility obligation}.
\end{aligned}
\`\`\`

This representation makes every stage accountable for both its output and the evidence required before that output can support subsequent analysis.

### Stage 1 — Spatiotemporal Multilayer SoS Structure

Stage 1 determines what entities exist, what functions they perform, where they are located, and where interactions are structurally possible. Its principal output is a bounded multilayer representation,

\`\`\`math
\boxed{
\mathcal G
=
\left(
\mathcal G_P,\,
\mathcal G_T,\,
I,\,
O,\,
\Omega,\,
\mathcal B
\right),
}
\`\`\`

together with service requirements and candidate cross-system interfaces. The stage is architectural: topology, proximity, co-location, or common hazard exposure identify possible relationships but do not by themselves establish causal dependence.

Its principal credibility obligations are data provenance, topology consistency, spatial and temporal compatibility, unit consistency, and verification that the representation conforms to the declared system boundary.

### Stage 2 — Evidence-Grounded Causal Interdependencies

Stage 2 determines which candidate relations correspond to defensible directional dependency mechanisms. An admitted mechanism must specify its source, receiver, mechanism, activation condition, consequence, parameters, uncertainty, evidence status, and validity domain.

The admitted set can therefore be represented as

\`\`\`math
\boxed{
\mathbb I^\star
=
\left\{
\mathfrak I_{ij}^{\alpha\beta}
:
\chi_{ij}^{\rm evid}
=
\mathrm{PASS}
\right\}.
}
\`\`\`

The first major scientific transformation is consequently

\`\`\`math
\boxed{
\mathcal G
\longrightarrow
\mathbb I^\star
:
\quad
\text{candidate structural relation}
\longrightarrow
\text{evidence-qualified causal mechanism}.
}
\`\`\`

Evidence identification and reporting for this stage are informed by systematic-review practice, including PRISMA 2020 where applicable. PRISMA is used to improve transparency of search, screening, eligibility, and reporting; it is not treated as proof of causal validity or evidence quality by itself.

### Stage 3 — Physics-Based Hybrid Multiscale Dynamics

Stage 3 translates accepted dependency mechanisms into testable state-, time-, hazard-, and mode-dependent dynamics:

\`\`\`math
\boxed{
\dot Y
=
F_{\mathcal G}^{m}
\left(
Y,u,\eta;
\theta,\mathbb I^\star
\right),
\qquad
m\in\mathcal M.
}
\`\`\`

Here \(Y\) denotes the coupled physical state, \(u\) feasible operational action, \(\eta\) the disturbance process, \(\theta\) the qualified parameter set, and \(m\) the active operating or disruption mode.

The corresponding scientific transformation is

\`\`\`math
\boxed{
\mathbb I^\star
\longrightarrow
F_{\mathcal G}^{m}
:
\quad
\text{accepted causal mechanism}
\longrightarrow
\text{dynamic law generating testable trajectories}.
}
\`\`\`

The credibility obligation now expands from evidence qualification to dimensional consistency, limiting-case checks, numerical or analytical verification, baseline comparison, and validation against admissible physical evidence wherever available.

### Stage 4 — Observation, State Estimation, Organization and Control

The true physical state is not assumed to be perfectly observed, nor is every physically possible action assumed to be operationally feasible. Observation and state estimation are represented generically as

\`\`\`math
y(t)
=
H\!\left(Y(t)\right)+\varepsilon(t),
\`\`\`

\`\`\`math
\hat Y(t)
=
\mathcal E\!\left(y_{0:t}\right),
\`\`\`

while feasible operation satisfies

\`\`\`math
\boxed{
u(t)
\in
\mathcal U_t
\left(
\hat Y(t),I(t),O(t)
\right).
}
\`\`\`

Information \(I\) and organization \(O\) therefore influence knowledge and the feasible action set rather than being treated automatically as additional physical infrastructure networks. Stage 4 asks not simply what could improve system response under perfect information and unlimited coordination, but what response remains admissible under the observation, information, authority, resource, and timing constraints represented by the experiment.

### Stage 5 — Uncertainty-Aware Viability and Reachability Resilience

Stage 5 asks whether required coupled services can remain acceptable and, if they leave the acceptable domain, whether they can return under feasible actions and uncertainty.

The admissible operating set is represented conceptually by

\`\`\`math
\boxed{
K(t)
=
K_{\rm phys}(t)
\cap
K_{\rm svc}(t)
\cap
K_{\rm op}(t).
}
\`\`\`

The resilience object is

\`\`\`math
\boxed{
\mathfrak R_T
=
\left(
\mathcal V_{\alpha,T_V},
\mathcal R_{\beta,T_R},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
}
\`\`\`

This stage therefore separates three questions:

\`\`\`math
\boxed{
\text{remain acceptable}
+
\text{return to acceptable operation}
+
\text{quantify confidence}.
}
\`\`\`

The symbols “+” indicate conceptual composition rather than numerical summation. Stage 5 complements conventional performance and recovery trajectories by asking whether admissible controls exist for maintaining or recovering required services, and with what uncertainty.

### Stage 6 — Resilience Diagnosis, Intervention, and Sustainability Consequences

Stage 6 translates diagnosis into candidate engineering transformations. The thesis preserves

\`\`\`math
\boxed{
u(t)
=
\text{operation of the existing system},
\qquad
a_k
=
\text{persistent change to the system}.
}
\`\`\`

Each admitted candidate transformation is evaluated through

\`\`\`math
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right),
}
\`\`\`

where \(\Delta\mathfrak R^{a_k}\) denotes resilience consequence, \(\mathbf r^{a_k}\) required resources, \(\Delta\mathbf J_{\rm sus}^{a_k}\) admitted sustainability consequences, \(\mathcal F^{a_k}\) feasibility, and \(\mathbf U^{a_k}\) associated uncertainty.

This typed representation preserves

\`\`\`math
\boxed{
\text{effectiveness}
\neq
\text{resource efficiency}
\neq
\text{sustainability}.
}
\`\`\`

A transformation is therefore not declared preferable solely because it increases resilience.

### Stage 7 — Engineering Decision and Adaptive Transformation

Stage 7 integrates the evidence required to compare feasible alternatives. The principal comparison distinguishes alternatives preferred under resilience criteria alone from those remaining admissible when resource, sustainability, feasibility, and uncertainty consequences are included:

\`\`\`math
\boxed{
\mathcal A_R^\star
\qquad
\text{versus}
\qquad
\mathcal A_{R,S}^\star .
}
\`\`\`

Consequences remain vector-valued unless a defensible preference or utility model independently justifies aggregation. The default decision logic therefore emphasizes feasibility, dominance, trade-offs, sensitivity, and robustness rather than imposing an arbitrary composite score.

The research architecture thus terminates with an engineering decision rather than with a resilience index:

\`\`\`math
\boxed{
\text{Need}
\rightarrow
\text{Representation}
\rightarrow
\text{Prediction}
\rightarrow
\text{Diagnosis}
\rightarrow
\text{Intervention}
\rightarrow
\text{Decision}.
}
\`\`\`

## 1.7.3 Scientific and engineering methodological control

The seven stages specify **what the thesis investigates**. Scientific credibility is governed by established methods appropriate to the type of claim being made rather than by a thesis-specific named scientific method.

At the most general level, hypothesis-bearing parts of the thesis follow **hypothetico-deductive reasoning**:

\`\`\`math
\boxed{
\text{Problem}
\rightarrow
\text{Question}
\rightarrow
\text{Hypothesis}
\rightarrow
\text{Prediction}
\rightarrow
\text{Test}
\rightarrow
\text{Evidence}
\rightarrow
\text{Inference}.
}
\`\`\`

A hypothesis is therefore useful only when it generates a discriminating prediction and when the experiment contains an admissible comparator capable of producing evidence inconsistent with that prediction.

This scientific logic is supplemented by a set of recognized methodological controls:

\`\`\`math
\boxed{
\begin{array}{rcl}
\text{Needs, requirements, architecture}
&\leftarrow&
\text{ISO/IEC/IEEE 15288 + NASA systems engineering},\\[1mm]
\text{Evidence synthesis}
&\leftarrow&
\text{systematic review + PRISMA reporting},\\[1mm]
\text{Hypothesis testing}
&\leftarrow&
\text{experimental design + controlled comparators},\\[1mm]
\text{Computational credibility}
&\leftarrow&
\text{IEEE V\&V + ASME VVUQ},\\[1mm]
\text{Quantitative inference}
&\leftarrow&
\text{engineering statistical methods},\\[1mm]
\text{Computational transparency}
&\leftarrow&
\text{reproducibility practice}.
\end{array}}
\`\`\`

ISO/IEC/IEEE 15288:2023 is particularly relevant because its system-life-cycle processes explicitly apply to systems, their elements, and Systems of Systems, and may be applied iteratively, concurrently, and recursively. NASA's Systems Engineering Handbook provides the complementary input–activity–output and iterative design logic used here.

For experimental comparisons, factors, scenarios, comparators, response quantities, and statistical assumptions are specified before confirmatory result interpretation wherever practicable. The NIST/SEMATECH Engineering Statistics Handbook is used as a methodological reference for experiment design and quantitative analysis appropriate to engineering studies.

For computational models, verification and validation are treated as distinct activities. IEEE 1012-2024 defines V&V processes in terms of whether development products conform to requirements and whether the resulting system, software, or hardware satisfies intended use and user needs. ASME VVUQ further distinguishes computational-model verification, real-world validation, and uncertainty quantification. Verification evaluates consistency between the computational implementation and its mathematical description; validation evaluates adequacy for the intended application; uncertainty quantification evaluates the influence of numerical and physical uncertainty on outputs.

Hence,

\`\`\`math
\boxed{
\text{verification}
\neq
\text{validation}
\neq
\text{uncertainty quantification}.
}
\`\`\`

A verified implementation is not automatically a validated physical model, and neither verification nor validation eliminates uncertainty.

## 1.7.4 Scientific handoffs, traceability, iteration, and reproducibility

Progress between stages is conditional. If \(Z_k\) denotes the output of stage \(k\), then it becomes an input to the subsequent stage only after satisfying the relevant scientific acceptance condition:

\`\`\`math
\boxed{
Z_k
\xrightarrow{\chi_k^{\rm acc}=\mathrm{PASS}}
I_{k+1},
\qquad
\chi_k^{\rm acc}
\in
\{
\mathrm{PASS},
\mathrm{FAIL},
\mathrm{BLOCKED}
\}.
}
\`\`\`

A handoff therefore contains three elements:

\`\`\`math
\boxed{
\text{scientific handoff}
=
\text{output}
+
\text{acceptance criterion}
+
\text{provenance}.
}
\`\`\`

Failure of an acceptance gate does not imply that the scientific quantity equals zero or that the corresponding hypothesis is false. It means that the downstream claim is not authorized from the available evidence.

Traceability is maintained bidirectionally:

\`\`\`math
\boxed{
G
\leftrightarrow
RQ
\leftrightarrow
SO
\leftrightarrow
H
\leftrightarrow
M
\leftrightarrow
T
\leftrightarrow
R
\leftrightarrow
C,
}
\`\`\`

where

\`\`\`math
\begin{aligned}
G &= \text{evidence-supported gap},\\
RQ &= \text{research question},\\
SO &= \text{specific objective},\\
H &= \text{applicable hypothesis},\\
M &= \text{model or method},\\
T &= \text{test or experiment},\\
R &= \text{resulting evidence},\\
C &= \text{defensible conclusion}.
\end{aligned}
\`\`\`

The forward trace answers why a model or experiment exists; the reverse trace identifies which evidence supports the eventual conclusion. This logic prevents methods that do not answer a research question, experiments that have no hypothesis or objective, and contribution claims unsupported by validated results.

The architecture is also explicitly iterative:

\`\`\`math
\boxed{
\text{ordered forward dependency}
+
\text{controlled backward revision}.
}
\`\`\`

A failed model check may require revision of a mechanism; a failed validation exercise may require revision of parameters, boundaries, or model form; and an intervention analysis may expose missing constraints. Such iteration is consistent with systems-engineering practice, which treats design processes as iterative and recursive. However, controlled iteration is distinguished from post hoc modification of confirmatory hypotheses, comparators, thresholds, or accounting conventions after inspecting outcomes.

Finally, computational reproducibility is treated as part of scientific credibility. Accordingly, computational experiments should preserve, where legally and technically possible,

\`\`\`math
\boxed{
\text{data provenance}
+
\text{code}
+
\text{parameters}
+
\text{software environment}
+
\text{random seeds}
+
\text{version information}
+
\text{commit identifier}
+
\text{execution instructions}.
}
\`\`\`

The overall scientific logic of the thesis can therefore be summarized as three coupled layers:

\`\`\`math
\boxed{
\begin{array}{c}
\textbf{ENGINEERING LOGIC}\\[1mm]
\text{Need}
\rightarrow
\text{Structure}
\rightarrow
\text{Causality}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Knowledge/Action}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Decision}
\\[4mm]
\textbf{SCIENTIFIC OBJECTS}\\[1mm]
K_{\rm svc}
\rightarrow
\mathcal G
\rightarrow
\mathbb I^\star
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
(\hat Y,\mathcal U_t,\pi)
\rightarrow
\mathfrak R_T
\rightarrow
\mathcal C(a_k)
\rightarrow
\mathcal A^\star
\\[4mm]
\textbf{SCIENTIFIC CONTROL}\\[1mm]
\text{Hypothesis testing}
+
\text{systems engineering}
+
\text{evidence qualification}
+
\text{DOE}
+
\text{V\&V}
+
\text{UQ}
+
\text{statistical inference}
+
\text{reproducibility}.
\end{array}}
\`\`\`

Section 1.7 thus establishes the **reader-facing research architecture and scientific logic** of the thesis. It defines how service needs, scientific objects, analytical transformations, credibility requirements, and engineering decisions are connected without duplicating the detailed mathematical derivations or experimental procedures of later chapters. Sections 1.8–1.11 subsequently translate this architecture into the general research objective, research questions, specific objectives, and hypotheses/test logic, while the methodology and mathematical chapters specify the detailed models, data, algorithms, comparators, verification, validation, uncertainty quantification, and reproducibility procedures required for execution.
