---
name: automate-me
description: "Create or update a personal working-style skill from the user’s demonstrated preferences and corrections. Use for automate-me or requests for a personal mode."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Automate me

Draft a personal mode from evidence about how the user actually works.

1. Honor a named target or existing personal skill. Inspect relevant project and personal skill locations, without changing plugin caches. Preserve an existing destination and invocation policy.
2. Mine the current conversation and only in-scope Codex chats available through host tools or explicitly supplied transcripts. Look for repeated corrections, decision standards, review preferences, communication choices, and methods that saved time. Record examples rather than inventing habits from a username or project path.
3. Separate durable preferences from task-specific constraints and one-off experiments. If history is unavailable, disclose that and draft from current evidence. Ask only for missing choices that materially affect the mode, such as its requested name or a disputed preference.
4. Use skill-creator to create or revise the skill. A new mode should be short and precise, route to poteto-mode only when that workflow applies, and state only the user's meaningful differences. Do not copy all pstack instructions into the mode.
5. Use the configured personal skill destination unless the user or repository specifies project scope. For project scope, use .agents/skills/<name>/. Preserve existing skills and review changes before overwriting unrelated content.
6. Validate the skill and give the user its location, how to invoke it, the preferences encoded, and any evidence gaps.

This creates a working-style skill. Scheduling future runs is a separate action and requires a user request for recurring or later work.
