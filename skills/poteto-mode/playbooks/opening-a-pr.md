### Opening a PR

Use this when the user's task includes publishing a PR. For local-only work, finish with the local result and verification.

1. Inspect the actual base, branch, worktree, diff, repository instructions, and existing PRs. Preserve unrelated and uncommitted work. Reuse a suitable attached managed worktree or create an isolated one when needed. Do not reset a dirty branch or discard files as a shortcut.
2. Run the adapter's code cleanup pass and a relevant no-comments pass. Verify behavior and run the repository's required checks for the touched paths.
3. Commit according to the user's request and repository conventions. Prefer coherent, reviewable units. Do not rewrite shared history without authorization.
4. Draft a title and body around the problem and resulting behavior. Use the repository's PR template. For a simple change, a short explanation plus actual validation is enough; for a complex change, include important scope and tradeoffs. Use technical-writing and unslop when helpful.
5. Use the available forge integration or gh. Match the user's draft/ready preference and the repository's conventions. For a stack, target the actual parent branch and report the chain. Do not assume trunk is named main.
6. Read the created PR back to confirm its URL, base, state, and head. Attach it with the Codex attachment tool when available. Include every created PR.
7. Continue other authorized work. Opening a PR alone does not authorize a merge, team messages, or a recurring monitor. Use Babysit when the user asked for PR follow-through, and Shipping when landing is authorized.

Reply with the PR link, resulting behavior, verification, and any material review gap.
