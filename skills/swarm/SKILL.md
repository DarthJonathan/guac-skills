---
name: swarm
description: "Coordinate workers across distinct slices or a declared race and return one evidence-backed report. Use for swarm or parallel coverage requests."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Swarm

1. Name the done condition and choose partitioned coverage, a race, or a mixture. For a race, declare first-pass, rank-all, or best-of before starting.
2. Give each worker a distinct slice, output location, and verification contract. For commit comparisons, name exact SHAs. For measurements, specify what one sample is, the sampling method, and order.
3. Use permitted native subagents and the swarm workers role, defaulting to inheritance. Do not invent cloud machines or unsupported spawn fields. Respect concurrency limits and isolate writers. Name each model actually used for a model race.
4. Each worker returns PASS, ISSUES, or BLOCKED with evidence and all proven issues. Reject results missing the required artifact identity or measurement method. Retry a missing report once; after that, record a gap.
5. For coverage, account for every required slice. For a race, apply the declared selection rule. Inspect important evidence yourself and integrate any changes coherently.

Return one consolidated report with results, proven issues, evidence, and gaps. If delegation is unavailable or prohibited, execute useful slices sequentially and label the execution mode. A coverage gap never becomes a pass.
