---
name: reflect
description: "Review the current conversation for durable lessons and prepare concrete edits to existing skills. Use when the user asks to reflect on a session."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Reflect

Find durable lessons in the current conversation and turn them into reviewable changes.

Use the current context or a host-supplied transcript path. A scoped Codex chat read is useful when available. Do not search private session stores. Label a digest when full tool history is unavailable.

Review through three lenses using the packaged prompts when useful:

- [Judgment](references/judgment-reviewer.md).
- [Tooling](references/tooling-reviewer.md).
- [Divergent](references/divergent-reviewer.md).

Use permitted native reviewers when available, otherwise apply the lenses sequentially. Reviewers remain read-only even when they can access MCP tools. Synthesize with [the synthesizer prompt](references/synthesizer.md).

Prefer architecture, types, lint, metadata, or a script over adding another instruction. Accept a lesson only when concrete evidence supports it and it has a real destination. Route a missed trigger to the skill description. Reject one-off preferences presented as universal rules.

Prepare exact proposed edits and their destinations, plus rejected and backlog items. Apply edits when the user has already authorized those skill changes. Otherwise present the concrete patch for selection before changing durable behavior. Never edit a plugin cache. Use a requested source location or an editable local skill copy.

Use skill-creator for substantial authoring and validate changed skills. Keep backlog items local unless the user explicitly authorized filing them externally. Report applied changes, pending choices, and evidence limitations.
