---
name: arena
description: "Compare multiple attempts at the same design, implementation, or artifact, choose a base, and combine the strongest coherent parts. Use for arena requests."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Arena

Compare alternatives under one goal rather than averaging incompatible designs.

1. Frame the deliverable and a rubric with three to six concrete criteria. Give candidates the same task and grounding. Read the arena runners panel from pstack configuration; absent a panel, use two inherited-model candidates when delegation is available.
2. Give each candidate its own worktree or output directory. Use permitted native subagents with self-contained briefs, output paths, and a short rationale. Queue work to respect the host's concurrency limit.
3. After candidates finish, read every artifact. When available, use a separate read-only judge chosen from the arena cross-judge pool to score path-labeled candidates against the rubric. Prefer an explicitly configured different model only when supported and authorized. A sequential self-review is labeled as such.
4. Choose the base that best meets the rubric and gives future maintainers the clearest boundaries. Investigate disagreements rather than treating a vote as proof.
5. Review losing candidates for worthwhile ideas and integrate only those that fit the chosen design. If candidates already converge, record that and omit unnecessary grafts. If they diverge because the task is ambiguous, improve the framing.
6. Verify the final synthesized artifact. A passing original candidate does not prove that the combined version works.

Return the artifact and a concise synthesis note: rubric, candidates actually completed, base, judge result or limitation, grafts, rejected tradeoffs, and verification. A missing candidate remains a gap. With no delegation capability, compare sequential alternatives and disclose that limitation.
