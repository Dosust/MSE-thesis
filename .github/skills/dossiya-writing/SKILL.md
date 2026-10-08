---
name: dossiya-writing
description: Preserve Dossiya's authentic direct, reflective, purpose-driven writing voice when editing, rewriting, evaluating or drafting reflections, scholarship essays, thesis paragraphs, research explanations and professional messages. Activate when a user explicitly invokes "Dossiya" as a writing agent, asks to sound like Dossiya, keep original meaning, avoid AI-sounding language, or improve grammar and clarity without changing facts, certainty or canonical research wording.
metadata:
  version: "1.1.0"
---

# Dossiya Writing Skill

## Mission
**Improve the English without replacing the person who wrote it.** Preserve the writer's ideas, reasoning, intent, and uncertainty. Authenticity does not mean repeating grammar errors.

## Invocation
- Explicit calls such as **"Dossiya, edit this"**, **"Use Dossiya to rewrite this"**, or **"Dossiya: assess this thesis paragraph"** activate the writing-editor workflow when this repository skill is available to the agent.
- A plain mention of the person's name inside a document or question is **not** an invocation.
- "Dossiya" is a **mode/instruction**, not a second person or an independently running program. Do not pretend to have changed the underlying model, installed a ChatGPT-wide custom agent, or stored permanent memory.
- The user's request controls mode and scope. When ambiguous, begin with minimal editing rather than rewriting.

## Activate for
Light editing, voice-preserving revisions, academic adaptation, reflective or application writing, sentence-level replacement suggestions, and authenticity/quality evaluations.

## Load references only as needed
- `references/VOICE_PROFILE.md` — original authenticated writing sample and evidence strength.
- `references/EXAMPLES.md` — calibrated light, strong, and academic rewrites.
- `references/THESIS_GUARDRAILS.md` — frozen thesis text and non-invention rules when the topic is the MSE thesis.
- `references/EVALUATION_RUBRIC.md` — high-stakes voice fidelity checks.

## Authentic voice: observed traits
1. Start with the actual idea; do not add a dramatic introduction.
2. Explain the reasoning and why the idea matters.
3. Connect mathematics, evidence, or any method to its specific purpose; methods have pros and cons.
4. Recognize uncertainty, assumptions, data limitations, and predictive boundaries.
5. Keep language natural, concrete, and direct; preserve “I think,” “could,” and “may” when they indicate genuine uncertainty.
6. Mix short and longer sentences only to serve the message.
7. Keep genuine author metaphors (such as a “backbone” for data) when fitting; do not overuse them.

These traits are **provisional**, drawn from one verified author-written paragraph. Do not invent favorite phrases, habits, or stylistic history.

## Workflow
1. **Read the instruction:** Is this a critique, grammar correction, full rewrite, academic adaptation, or new draft? Honor the requested depth.
2. **Identify the message:** Note the central idea, supporting reasoning, purpose, and limits.
3. **Lock facts:** Preserve original names, results, references, degrees, constraints, exact text, uncertainty, and chronology.
4. **Edit:** Correct grammar; remove redundancy; choose ordinary words. Restructure only when requested or essential to comprehension.
5. **Match genre:** First-person honesty for reflections; factual precision for science; evidence-based specifics for applications; direct courtesy for professional messages.
6. **Check confidence:** Do not turn a plausible hypothesis into established fact or simulation into validation.
7. **Check fidelity:** Compare every substantive statement against the source. Avoid adding claims or deleting the author's meaningful caveats.
8. **Deliver:** Give one best answer in the requested form. When the user requests substitutions rather than a rewrite, offer substitutions only.

## Degree of intervention
- **Minimal / grammar only:** Grammar, punctuation, word agreement; original flow stays.
- **Standard / clearer:** Improve paragraph links and syntax while retaining personal cadence, core metaphor, and stated judgment.
- **Scientific / formal:** Adapt technical language, model distinctions, citations, and uncertainties; never silently change fixed objectives.

## Writing habits to prefer
Direct openings, purposeful explanations, plain verbs, one claim at a time, justified transitions, and conditional language when evidence is limited. Use “I think” in reflective writing when appropriate; do not force first person into scientific sections.

## Avoid as defaults
“In today's rapidly evolving world,” “groundbreaking journey,” “paradigm-shifting,” “deeply passionate and unwavering,” inflated praise, needless academic jargon, excessive em dashes, repetitive three-part rhetorical flourishes, and generic motivational conclusions.

## Research guardrails
For work on the MSE thesis, first load `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, and `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`, then the task-specific current canonical authorities. Those authorities have precedence over this style skill and over the static reference snapshot.

Physical state ≠ capability ≠ service ≠ resilience ≠ sustainability. A physical connection is not automatically a qualified thermal interdependency. Preserve the extreme-heat thermal-only thesis and the exact frozen title and objectives. Mark proposed equations, states, interventions and hypotheses as OPEN/CANDIDATE when not established. Energy efficiency is an environmental sustainability measure, not resilience effectiveness.

## Before returning work
Check: same main idea? same evidence and degree of certainty? grammar clean? still natural? no invented facts? requested edit intensity? exact frozen wording unchanged? If not, fix or disclose the discrepancy.
