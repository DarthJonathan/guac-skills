---
name: recall
description: "Rebuild the current state of the user’s recent work from scoped Codex chats, live repository state, and available shared evidence."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Recall

Reconstruct working context before resuming a topic. A request to resume one specific chat uses the session-pickup playbook instead.

1. Fix the scope from the request: topic, project, and time window. Use the active project and the last seven days when recent is unspecified. If a complete state capsule is already supplied, verify it and skip unnecessary history reads.
2. Use available Codex thread-listing and thread-reading tools. Select relevant project and topic matches before reading their content. Preserve exact source-provided thread titles when naming them. Do not scan filesystem session stores or unrelated projects. If history is unavailable, say which part could not be reconstructed and use the current conversation.
3. For a large in-scope set, partition evidence gathering among permitted read-only workers. Collect goal, decisions, open work, corrections, and artifacts with actual chat references. Summaries locate evidence; they do not prove commands ran.
4. For a named subsystem or bug, use why's available source playbooks to check the shared record for attempted fixes, reversions, active symptoms, and decisions. State access gaps.
5. Check surfaced PRs, branches, and tickets against live state. Distinguish merged, open, in-flight, verified-but-uncommitted, reverted, and planned work. Never infer completion from an agent's claim alone.

Return a short state capsule, one line per work thread with its status and evidence, recurring problems, and the most useful next action. Keep private context out of public artifacts.
