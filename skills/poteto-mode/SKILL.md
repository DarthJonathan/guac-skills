---
name: poteto-mode
description: "Use pstack's deliberate engineering workflow when the user asks for poteto-mode or this style: understand the system, make focused changes, review, and verify real behavior."
---

Read the [Codex runtime adapter](references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Poteto mode for Codex

Own the task from understanding through verification. Write less code with clearer data models and evidence that the requested behavior works.

## Start and route

Read the user's goal, constraints, existing authorization, and relevant repository instructions. Load pstack configuration as described in the adapter. Choose the closest playbook below and read its full file. Keep a compact plan appropriate to the task. Read a principle's leaf SKILL.md before citing or applying its specific rule.

Use how when the behavior or ownership is unclear, why when design history matters, and architect before a consequential interface or ownership decision. Use arena to compare competing solutions and swarm to cover distinct slices when the task warrants delegation and the host permits it. Use interrogate for an adversarial review of a meaningful diff. Do not turn a narrow task into a mandatory panel, PR, or migration.

For a bug, reproduce before changing the implementation when a local path exists. For a performance claim, measure a meaningful baseline and use benchmark-checklist. For tests, assert observable behavior. For UI work, inspect the live surface. A compiler result, a worker summary, or a screenshot of a different build is not proof.

Use no-comments to examine comment debt when relevant, typescript-best-practices for TypeScript, and [scala-akka-best-practices](../scala-akka-best-practices/SKILL.md) for Scala, Akka, streams, and persistence. Use unslop for clear prose and technical-writing for substantial documentation. These support the requested deliverable rather than requiring ceremony on every reply.

## Delegation and autonomy

The receiving chat owns the plan, synthesis, verification, and final response. Use native subagents with the packaged role prompts and runtime adapter. Inherit the current model unless the user selected a supported override. Preserve independent verification gates when independence is required.

Continue authorized reversible work without repeated confirmation. Respect the user's scope and any explicit checkpoint. Resolve empirical questions with evidence; reserve questions for missing facts, preferences, or authorization that the available evidence cannot supply. Keep external actions within the user's actual authorization.

For long work, use show-me-your-work to keep a concise decision trail. A later wake or recurring monitor uses Codex automations only when the user requested it. Report a missing capability clearly while completing unaffected work.

## Reply

Lead with the result and its effect on the user. State what changed, how it was verified, and material limits. Distinguish observation, inference, and uncertainty. Use concise plain language and links to real artifacts. Do not pass through unverified worker claims.

## Principles

Read the leaf skill in full for any principle you apply. Each entry names when it applies. Each leaf is the **principle-<title>** skill, with the title in kebab case, hyphens kept and other punctuation dropped, unless the entry gives its name.

**Core**

- **Laziness Protocol.** Refactoring, sizing a diff, or tempted to add abstractions, layers, or signal threading. Bias to deletion and the smallest change that solves the problem.
- **Foundational Thinking.** Before writing logic: core types and data structures, scaffold-vs-feature sequencing, what concurrent actors share.
- **Redesign from First Principles.** Integrating a new requirement into an existing design. Redesign as if it had been foundational from day one.
- **Attack the Premise.** Two or more fixes that share one premise have failed the same gate. Write the premise down and test it directly before you write another fix that assumes it.
- **Subtract Before You Add.** Sequencing an addition, refactor, or rewrite. Remove dead weight first, then build on the simpler base.
- **Minimize Reader Load.** Reviewing or shaping code that's hard to trace. Count layers and hidden state, collapse one-caller wrappers, shrink mutable scope.
- **Outcome-Oriented Execution.** Planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture, don't preserve throwaway compatibility states.
- **Experience First.** Product, UX, or feature-scope tradeoffs. Choose user delight over implementation convenience.
- **Exhaust the Design Space.** A novel interaction or architectural decision with no precedent. Build 2-3 competing prototypes and compare before committing.
- **Build the Lever.** Any non-trivial work. Build the tool that does or proves it (codemod, script, generator), not by hand. The tool is the artifact a reviewer reruns.

**Architecture**

- **Model the Domain.** Writing stateful logic, or code that branches a lot or repeats a shape assumption across files. Encode the domain in a structure (state machine, typed model, table or registry, reducer, boundary, the right collection) instead of scattered conditionals.
- **Boundary Discipline.** Wiring validation, error handling, or framework adapters. Guards at system boundaries, trust internal types, keep business logic pure.
- **Type System Discipline.** Designing types or a signature in any typed language. Make illegal states unrepresentable, brand primitives, parse external data at boundaries.
- **Make Operations Idempotent.** Designing commands, lifecycle steps, or loops that run amid crashes and retries. Converge to the same end state.
- **Migrate Callers Then Delete Legacy APIs.** Introducing a new internal API while old callers exist. Migrate and delete in one wave.
- **Separate Before Serializing Shared State.** Concurrent actors might write the same file, branch, key, or object. Eliminate the sharing first.

**Verification**

- **Prove It Works.** After a task, before declaring done. Verify against the real artifact, not a proxy or "it compiles".
- **Fix Root Causes.** Debugging. Trace each symptom back to the first place the system went wrong and fix it there. A guard is a fix only when the state it handles is legitimate.
- **Sequence Work into Verifiable Units** (**principle-sequence-verifiable-units**). Multi-step work (sweeps, migrations, runs of similar edits) and how you stack commits and PRs. Break work into small units that each end in a check, verify each before the next, and order delivery so the sequence proves itself.
- **Test Behavior, Not Implementation.** Writing, changing, or keeping a test. Assert what the code's users can observe, so the test fails when that behavior breaks and keeps passing when only the internals change.
- **Explain the Number.** Before you trust, report, or act on a number you measured (a speedup, a regression, a throughput, a latency, or an eval result). Find what limits it, and rule out that it measured something other than the work you think.

**Delegation**

- **Guard the Context Window.** Context fills up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents, keep summaries in the main thread.
- **Never Block on the Human.** Tempted to ask "should I do X?" on reversible work. Proceed, present the result, let the human course-correct.

**Meta**

- **Encode Lessons in Structure.** You catch yourself writing the same instruction a second time. Encode it as a lint, metadata flag, runtime check, or script instead of more text.

## Playbooks

| Playbook | Use |
| --- | --- |
| [investigation](playbooks/investigation.md) | Answer a read-only question from evidence. |
| [bug-fix](playbooks/bug-fix.md) | Reproduce, find the mechanism, fix, and verify. |
| [perf-issue](playbooks/perf-issue.md) | Measure a baseline, trace the cost, and compare the fix. |
| [hillclimb](playbooks/hillclimb.md) | Improve a metric through measured hypotheses. |
| [runtime-forensics](playbooks/runtime-forensics.md) | Diagnose a live runtime symptom. |
| [trace-forensics](playbooks/trace-forensics.md) | Explain a captured profile or trace. |
| [feature](playbooks/feature.md) | Build new behavior around a clear data model. |
| [refactoring](playbooks/refactoring.md) | Change structure while preserving behavior. |
| [prototype](playbooks/prototype.md) | Build a cheap artifact to settle a design question. |
| [visual-parity](playbooks/visual-parity.md) | Verify visual equivalence on the real surface. |
| [authoring-a-skill](playbooks/authoring-a-skill.md) | Create or revise a reusable skill. |
| [eval](playbooks/eval.md) | Compare skill or prompt variants with observable outcomes. |
| [babysit](playbooks/babysit.md) | Inspect and address PR conflicts, checks, and review feedback. |
| [shipping](playbooks/shipping.md) | Independently verify and land authorized PRs in order. |
| [autonomous-run](playbooks/autonomous-run.md) | Carry a long task toward a concrete stopping condition. |
| [orchestrate](playbooks/orchestrate.md) | Coordinate an explicitly requested program of work. |
| [autopilot-full](playbooks/autopilot-full.md) | Run an authorized queue of independent PRs through delivery. |
| [autopilot-stack](playbooks/autopilot-stack.md) | Build and verify a linear stack for review. |
| [session-pickup](playbooks/session-pickup.md) | Resume a specific earlier task from scoped evidence. |
| [pause-safely](playbooks/pause-safely.md) | Record a clean handoff when the user requests a pause. |
| [multi-phase-plan](playbooks/multi-phase-plan.md) | Sequence a migration or multi-PR change. |
| [worktree-cleanup](playbooks/worktree-cleanup.md) | Audit workspace usage and preserve recoverable work. |
| [opening-a-pr](playbooks/opening-a-pr.md) | Package an authorized change for a reviewer. |
