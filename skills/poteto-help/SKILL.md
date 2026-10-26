---
name: poteto-help
description: "Explain pstack setup, poteto-mode, or which pstack skill or playbook fits a task. Use when the user asks for pstack help."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Pstack help

Answer the part of pstack the user is asking about, then give a concrete prompt they can use. Read local sibling SKILL.md files and poteto-mode's playbook table rather than fetching unpinned upstream instructions.

Start with $poteto-mode for a complete engineering task. Use $how for behavior, $why for rationale, $architect for interface design, $arena for competing solutions, $swarm for partitioned work, $interrogate for review, and $benchmark-checklist for measured performance claims. Use $setup-pstack only when configuring role preferences.

For history, use $recall or $reflect. For communication, use $teach, $bro, $unslop, or $technical-writing. For project proof, use the create/maintain verification skills and $statechart. Consult sibling descriptions for narrower tools.

For code quality, use $no-comments, $typescript-best-practices, or the fork's [Scala and Akka skill](../scala-akka-best-practices/SKILL.md): $scala-akka-best-practices.

There are 59 skills: 58 upstream entries, including 24 principles, plus scala-akka-best-practices. Poteto mode has 23 playbooks. The port uses Codex tool mappings and inherited models. Upstream explicit-only invocation is preserved; the added Scala and Akka skill also supports automatic discovery. Read [the adapter](../poteto-mode/references/codex-adapter.md) before claiming platform support.

For setup examples, read [prompting](references/prompting.md) or [recipes](references/recipes.md). Do not imply that Cursor Automations, external providers, or the excluded Benny pack were installed.
