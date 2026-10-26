---
name: interrogate
description: "Adversarially review a diff from multiple available perspectives and synthesize actionable findings. Use for interrogate, stress-test, or multi-model review requests."
---

Read the [Codex runtime adapter](../poteto-mode/references/codex-adapter.md) once per session before using this skill. Its tool, model, history, and authorization mappings apply to all linked instructions.

# Interrogate

Review the requested change. Do not apply fixes unless the user also authorized them.

1. Resolve the exact files, diff, and base from the request and repository. State the intended behavior from the user's goal, code, and existing PR description. Inspect enough surrounding code to judge real callers.
2. Read [the reviewer prompt](references/reviewer-prompt.md), [the rubric](references/rubric.md), and [the code-quality lens](references/code-quality-review.md).
3. Use the interrogate reviewers panel when native delegation is available and permitted. With no configuration, use two separate sessions inheriting the host model. Give each the same intent, scoped diff, context paths, and read-only brief. Same-model sessions are not a multi-model review. If a requested different model is unavailable, report that limitation.
4. Validate findings against source and real failure conditions. Merge duplicates, track who raised each issue, and investigate contradictions. Agreement is supporting evidence, not proof.
5. Read [the lead-judgment guidance](references/lead-judgment.md). Classify findings as Act on, Consider, Noted, or Dismissed with a concrete reason. Prioritize actual correctness, security, and maintenance consequences under the stated goal.

Return intent, reviewers actually used, actionable findings with tight source locations and failure scenarios, other material findings, dismissals, and disagreements. Drop empty sections. When delegation is unavailable, perform a single-agent adversarial review and say so.
