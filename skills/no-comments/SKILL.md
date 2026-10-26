---
name: no-comments
description: "Review comments for redundant narration and hidden design problems, preserving useful contracts and genuine constraints. Use for no-comments requests or focused cleanup."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# No comments

Review the scoped files or diff for comments that repeat code, conceal dead code, or document avoidable workarounds.

When a permitted reviewer is useful, pass [the comment reviewer prompt](../poteto-mode/references/agents/comment-sicko.md) and exact scope to a native read-only subagent. Otherwise perform the review directly. The parent owns any edits.

Preserve legal notices, public API contracts, non-obvious constraints imposed by external systems, useful issue references, and justified tooling directives. Inspect the surrounding implementation before judging a claim. A necessary suppression should not disappear merely because a reviewer dislikes comments.

For avoidable complexity, identify the specific symbol and a concrete structural improvement. Apply only changes within the user's scope and existing authorization. Verify that deleting or rewriting a comment did not change a generated artifact, tool behavior, or a required contract.

Report accepted changes, evidence-backed structural suggestions, and meaningful exceptions.
