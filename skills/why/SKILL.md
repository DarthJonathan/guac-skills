---
name: why
description: "Investigate design rationale, tradeoffs, regressions, and historical decisions using source history and available connected evidence. Use for why questions."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Why

Find why the system took its current shape and what constraints still matter.

1. Resolve the target from the user's question and current context. State a reasonable interpretation when necessary. Read [the epistemic guidance](references/epistemics.md).
2. Discover available source-control, issue-tracker, document, chat, observability, error-tracker, and analytics integrations. Prefer connected tools over asking the user for information they may contain. Do not infer access from a service name or invent an MCP filesystem directory.
3. Read [the source playbook](references/source-playbook.md) and only the source-specific references for evidence categories actually available. Follow cited commits, discussions, decisions, incidents, and measurements. Scope queries to the requested system.
4. For a broad question, assign one permitted read-only investigator per useful evidence category using [the investigator prompt](references/investigator-prompt.md). The why investigators role inherits the host model by default. For a narrow question, investigate directly.
5. Synthesize with [the synthesizer prompt](references/synthesizer-prompt.md) using the why synthesizer role when delegation is useful. Distinguish documented rationale, a plausible inference, and an unresolved gap. Missing access or no search hits do not establish that a discussion never happened.
6. Cite actual evidence near its claim. Separate historical constraints from constraints verified to hold today. If implementation follows, turn the evidence into Preserve, Change, Avoid, and Risk constraints.

Report the answer and its confidence, material alternatives, sources consulted, and remaining gaps. Do not manufacture consensus or motivation from code alone.
