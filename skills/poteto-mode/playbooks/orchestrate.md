### Orchestrate

Use this for an explicitly requested program that spans many units, PRs, or sessions. A task one agent can complete in the current session uses Autonomous run instead.

#### Frame and place

Name the done condition, units, dependencies, budget, review gates, and landing authority. Give each branch or output directory one writer. The receiving chat coordinates the program using native subagents when available and permitted. Do not assume remote VMs, nested agent depth, or a particular concurrency cap.

Keep the program's state in a user-requested location or work/pstack/orchestrate/<project>/ in the workspace. No private agent store path is assumed. The optional upstream Bun helper can manage this store:

    bun <installed-poteto-mode>/scripts/orch/orch.ts --store <absolute-store> <command>

Check its --help and declared dependencies before use. It manages bookkeeping, not agent creation or scheduling. Plain TSV and JSON remain valid records when the helper is unavailable.

Keep a unit table, a verification ledger keyed by PR and SHA, an ordered frontier, completion pointers, standing constraints, user decisions, and a decision trail. Derive status from those records.

#### Brief

Every worker receives the goal, permitted paths, its exact checkout and SHA, relevant context, acceptance criteria, verification command, forbidden actions, and report contract. Pass the current standing constraints. Scope the brief to the actual unit. Do not paste a large scaffold for a one-command task.

Workers report status, exact artifact identity, commands run, observed results, gaps, and deviations. A verifier who did not write the code checks high-risk behavioral work. Record whether different sessions or different models actually ran.

#### Run and reconcile

1. Pilot one representative unit to test the brief, environment, and evidence contract.
2. Run a rolling window within the host's concurrency limit. Isolate writers and relay dependency evidence to downstream work.
3. Drain completion reports at useful boundaries. Account for every worker. A missing result remains a gap.
4. Integrate verified work in dependency order. Recheck evidence when the patch, build inputs, or base changes. Mutate stack topology through one designated owner.
5. Use native read-only status and available artifacts to inspect liveness. Do not restart a worker just to check it. Retry a failed unit at most twice with an evidence-backed change in scope or method, then replan or report the dependency.
6. Create a later continuation or monitor only when the user requested that schedule. Preserve notification intent; keep unchanged state quiet unless periodic reporting was requested.
7. On a user stop, hold workers and leave a durable handoff. On completion, reconcile units, artifacts, current verdicts, and outstanding gates against the real result.

Publishing, external communication, merging, force-pushes, deployments, and deletion remain within the user's actual authorization. Record an unmet gate and work around independent tasks when possible. Do not manufacture approval from an agent countersign.

Reply with the done condition and counts from the records, delivered units, exact PR links and verdicts, unresolved gaps, and the store and trail paths.
