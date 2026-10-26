---
name: setup-pstack
description: "Configure pstack role preferences for Codex using supported models and inherited defaults. Use for setup-pstack or changing pstack model choices."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Set up pstack for Codex

Configure pstack without changing the host's global model or approval settings.

1. Read existing personal and repository pstack-models.json files using the adapter's precedence. A missing file means all roles inherit the host model and reasoning effort.
2. Inspect the currently available subagent schema or other authoritative model listing. Do not guess model names or probe with rejected IDs. If delegation or overrides are unavailable, explain that inheritance still works.
3. Apply choices the user already supplied. For setup without model preferences, use inheritance. If the user wants a comparison or per-role override, show the supported options and ask only for the unresolved choice. Store effort separately from the model ID, and only when explicitly selected.
4. Use [the example configuration](../poteto-mode/references/pstack-models.example.json) for role and panel labels. Each panel entry is one reviewer or candidate. Two inherited entries mean two sessions of the same model, not a multi-model panel.
5. Honor a requested destination. Otherwise use the repository's .codex/pstack-models.json when working in a repository, or the personal file described in the adapter for projectless use. This is a pstack file that skills read explicitly. It is not an always-applied Codex rule.
6. Write valid JSON with schema_version 1, a roles object, and a panels object. Preserve unrelated keys and existing role choices. Check that every configured model and effort is supported and authorized. Write atomically and keep an existing file if validation fails.
7. Report the file and effective choices. A new invocation of a pstack skill reads the updated settings. No host restart is required for this JSON file.

If the user asks for project verification, route to create-verification-skill or create-formal-verification-skill. Setup alone does not create those extra project files.
