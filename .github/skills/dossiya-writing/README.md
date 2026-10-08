# Dossiya Writing Agent v1.2

A reusable writing mode with a repository-local Agent Skills-compatible `dossiya-writing` skill, based on one verified author-written paragraph and explicit user voice preferences.

## Files
```text
.github/skills/dossiya-writing/
├── SKILL.md
├── AGENTS.md
├── README.md
├── QUICKSTART.md
├── references/
│   ├── VOICE_PROFILE.md
│   ├── EXAMPLES.md
│   ├── THESIS_GUARDRAILS.md
│   └── EVALUATION_RUBRIC.md
└── tests/
    └── validate_package.py
```

The **root repository `AGENTS.md`** contains a lightweight dispatcher. All existing thesis-governance instructions remain authoritative.

## Invocation
When the GitHub repository's instructions and skill are available to the assistant:
- `Dossiya, correct the grammar of this paragraph without changing my reasoning.`
- `Use Dossiya to assess my thesis paragraph; give changes only.`
- `Dossiya, adapt this for a scholarship application in my voice.`

The trigger name **Dossiya** identifies the writing mode, not a separate model or continuously running agent. Merely naming Dossiya in an unrelated question is not an activation.

## Usage and limitations
Repository skill files are not automatically installed globally in ChatGPT. A session must have the repository instructions/skill available, or the user must provide the instructions. In this conversation, the assistant can follow the Dossiya invocation convention directly.

The voice profile is provisional and currently draws from one confirmed paragraph, not a trained voice clone. The thesis guardrails are only a convenience snapshot; live canonical research authorities control frozen wording, evidence, and scope.

## Validation
Run: `python .github/skills/dossiya-writing/tests/validate_package.py`

Skill specification: https://agentskills.io/specification

## Updated research-thinking preference
The agent now includes the author's **integration-first research mindset**: use relevant established methods purposefully, qualify the missing interface/relationship, test the bounded combination, and describe contributions only within evidence and validation limits. This is not a claim that an entire field has never studied the topic. See `references/VOICE_PROFILE.md` and `project/INTEGRATION_FIRST_THESIS_APPROACH_WORKING_V1.md`.
