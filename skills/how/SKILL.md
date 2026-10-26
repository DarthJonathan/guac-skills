---
name: how
description: "Explain how a subsystem works, including runtime flow, ownership, layering, and code locations. Use for code walkthroughs and architecture questions."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# How

Answer the user's concrete question from the source and, when needed, observable runtime behavior.

For a narrow function or module, explore directly. For a cross-cutting subsystem, split the investigation into two to four useful angles and use permitted native subagents when they add value. Read [the explorer prompt](references/explorer-prompt.md) for delegated exploration and [the explainer prompt](references/explainer-prompt.md) for synthesis. Keep investigations read-only unless the user asked for implementation.

Trace entry points, data structures, ownership, calls, state changes, and error paths. Follow real callers rather than inferring use from a definition. Use the how explorer and how explainer role preferences from pstack configuration, defaulting to inheritance.

Bring the findings together in an explanation that builds a working mental model. Use the relevant sections from the explainer prompt: Overview, Key Concepts, How It Works, Where Things Live, and Gotchas. Include precise source pointers and distinguish runtime evidence from inferred behavior. Route motivation and historical rationale to why.
