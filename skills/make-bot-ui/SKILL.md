---
name: make-bot-ui
description: "Build a UI for an existing user-supplied automation webhook, keeping credentials server-side. Use when the user requests buttons or a dashboard to trigger that webhook."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Make a bot UI

Build a small interface for an existing authorized webhook integration.

Codex does not supply an assumed equivalent of Cursor's automation webhook provisioning or SendToUser secret handoff. Do not invent an inbound Codex endpoint or request a secret in the chat. If the user needs a native Codex scheduled task, use the available automation tool instead.

1. Establish the actual webhook contract, desired actions, authentication mechanism, response shape, and deployment destination from the supplied integration. Inspect the existing project before choosing a stack.
2. Keep credentials in the server environment or the integration's secure secret mechanism. The browser sends action requests to the local or deployed application server; only that server contacts the webhook. Never include a sender key in source, a client bundle, a URL query, logs, or a screenshot.
3. Limit actions and validate payloads at the server boundary. Preserve the existing authorization model. Show progress, a concrete result, and useful failure messages. Avoid duplicate submissions where a retry could repeat an effect.
4. Verify with a mock or read-only path first. Exercise a live side effect only when the user's authorization covers it.
5. Publish, expose through a tunnel, or configure network access only within the user's requested scope. Give the user a concrete local result and name any missing external endpoint.

Return the working interface, configuration names without their secret values, verification results, and any deployment or integration boundary still awaiting authorization.
