# guac-skills

## Pstack for Codex — unofficial fork

**This is an unofficial fork of [pstack](https://github.com/cursor/plugins/tree/99b609a72323b70204eab407c622f436e858e112/pstack), originally created by Lauren Tan (poteto) in cursor/plugins.** This fork adapts that work independently for Codex. It is not an official release from the upstream pstack project, Cursor, or OpenAI.

Fork version 0.15.32-codex.5 is based on upstream version 0.15.32 and commit 99b609a72323b70204eab407c622f436e858e112. The original MIT license and Lauren Tan's copyright notice are preserved in LICENSE. UPSTREAM.json records the source, exact revision, and fork relationship.

The main goal is to write less, higher-quality code. The skills teach an agent to understand a system, choose clear data structures and interfaces, compare approaches when useful, review changes critically, and verify real behavior.

The package contains 59 skills: all 58 upstream entry points (34 workflows and 24 engineering principles), plus the fork's scala-akka-best-practices skill. Poteto mode routes among 23 playbooks. The original MIT license and attribution are preserved.

## Install as a Codex plugin

Download and extract the ZIP, or clone a copy of this directory. From its root:

~~~bash
codex plugin marketplace add .
codex plugin add pstack-codex@pstack-codex-marketplace
~~~

This installs the skills together as the named Pstack for Codex (fork) plugin. They will be available on your next turn. Start with $poteto-mode, or select the plugin's skill in the picker. Restart Codex if a client has not refreshed its skills.

The marketplace catalog is .agents/plugins/marketplace.json. It resolves the plugin from the same directory using a relative path, so it works after the folder is moved, unzipped, or cloned on another computer. Codex maintains the installed cache and enabled state.

If an older CLI does not expose plugin add, add the marketplace and use the desktop app's Plugins directory to choose Pstack for Codex (unofficial fork) as the source and install the plugin. See the official [plugin packaging documentation](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually).

## Optional loose-skill installation

Use Python 3.9 or later. From this package directory, install the skills for your user:

~~~bash
python3 install.py --target "$HOME/.agents/skills"
~~~

For one repository instead:

~~~bash
python3 install.py --target /absolute/path/to/repo/.agents/skills
~~~

Honor an existing configured skills location if your Codex installation uses one. Add --dry-run to preview the installation. The installer validates the bundle, keeps all sibling references together, skips identical installed skills, and refuses the entire operation if any destination contains a differing skill.

Codex normally detects local skill changes automatically. Restart it if the new skills do not appear. See the official [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) for discovery locations and invocation.

The Python installer is an alternative for loose skills. It does not register a marketplace. Choose the native plugin installation or the loose-skill installation to avoid duplicate entries for the same skills.

## Share or commit this fork

This directory is the repository root. Keep the hidden .agents and .codex-plugin directories when committing or sharing it. The plugin manifests, marketplace catalog, attribution, installer, tests, and packaging script are included. Local caches, installed dependencies, and build outputs are excluded from the release ZIP.

To build a fresh shareable archive:

~~~bash
python3 scripts/package.py
~~~

The result is dist/pstack-codex.zip. A recipient extracts it and runs the two native install commands above.

After you commit and push these files to DarthJonathan/guac-skills, recipients can install this fork with:

~~~bash
codex plugin marketplace add DarthJonathan/guac-skills
codex plugin add pstack-codex@pstack-codex-marketplace
~~~

The plugin metadata points to this fork at https://github.com/DarthJonathan/guac-skills. Keep the upstream attribution, MIT license, and UPSTREAM.json. Refresh a configured Git source with codex plugin marketplace upgrade pstack-codex-marketplace.

This package is prepared for local installation and future GitHub distribution. The plugin files have not been committed or pushed by this workflow, and no public Plugins Directory listing has been created.

## Start here

~~~text
$poteto-mode Fix this bug. Reproduce it, find the root cause, and verify the result.
~~~

| Skill | Main job |
| --- | --- |
| $poteto-mode | Own the engineering workflow and select a playbook. |
| $how / $why | Explain behavior and investigate the rationale behind it. |
| $architect | Settle caller usage, types, interfaces, and ownership. |
| $arena | Compare competing attempts, choose a base, and combine good ideas. |
| $swarm | Cover distinct slices or a declared race with one consolidated report. |
| $interrogate | Adversarially review a diff and judge the findings. |
| $tdd / verification skills | Prove behavior through tests, live workflows, or formal verification. |
| $benchmark-checklist | Check whether a performance number measures the intended work. |
| $no-comments / $typescript-best-practices / $scala-akka-best-practices | Improve code quality for the relevant language and runtime. |
| $reflect / $correct / $automate-me | Capture lessons, prevent recurring mistakes, or create a personal mode. |
| $unslop / $technical-writing | Improve the clarity of prose and documentation. |
| $poteto-help | Choose a skill or understand the package. |

The remaining entry points are listed in UPSTREAM.json. Each skill includes UI metadata. Upstream explicit-only invocation is preserved for 57 skills; setup-pstack retains automatic discovery. The fork's Scala and Akka skill also supports automatic discovery. Poteto mode can read and route to the other skills.

### Scala and Akka addition

[scala-akka-best-practices](skills/scala-akka-best-practices/SKILL.md) contains a detailed, source-specific case catalog extracted from both user-provided silver-server review-comment exports. The 5,790-case catalog accounts for all 6,087 comments across 1,052 PRs. It preserves actual method and type names, business predicates, account/product/region distinctions, numeric thresholds, failure windows, rollout sequences, alternatives, changes of view, and unresolved questions.

The [case index](skills/scala-akka-best-practices/references/pattern-index.md) routes across 13 overlapping topics. A read-only Python helper searches exact symbols and phrases, opens individual cases, and retrieves PR threads including supporting context. Each case retains source stance and exact comment or explicitly labeled diff-context evidence. The row ledger distinguishes extracted cases, acknowledgements, context, test evidence, and other material; it does not silently turn every source row into a rule.

This addition includes source-specific comment wording and selected original code excerpts. Incidental identities and portions of repetitive operational dumps are omitted; their extraction limits are recorded. The full JSONL exports and application checkout are not required at runtime. The source cases are historical evidence, including proposals later withdrawn or revised, and are checked against the target code before use. They are recorded separately from the original pstack inventory.

~~~text
$scala-akka-best-practices Find the matching source cases, preserve their exact conditions and follow-up comments, and review this change.
~~~

## Codex adaptations

- Cursor slash invocations become Codex $skill-name invocations.
- Native Codex subagents replace Cursor Task calls. Agent files become explicit prompt references. Writers use separate directories or worktrees, and the available concurrency limit controls fan-out.
- Every role inherits the current model and reasoning effort by default. Optional user-selected overrides use models actually supported by the session. Multiple sessions on one model are labeled accurately.
- Setup writes ordinary pstack JSON. Skills explicitly read it; it does not masquerade as an always-applied host rule or edit config.toml.
- Chat-history workflows use scoped Codex chat tools, the current conversation, or explicitly supplied transcripts.
- PR workflows respect the user's publishing and merge scope, actual branch names, draft preferences, and existing work.
- User-requested later continuations use Codex automation tools. An ordinary task does not silently create a recurring schedule.
- The worktree audit is a read-only Python helper. It does not fetch, mine chat stores, or delete. It preserves tracked, untracked, ignored, locked, and unknown work for review.

Read the [runtime adapter](skills/poteto-mode/references/codex-adapter.md) for the complete mapping. The package does not install providers, credentials, external connections, or schedules.

## Dependencies and limits

The skill instructions are Markdown. Optional helpers need their respective runtimes:

- Statechart helpers use Node.js. Real model checking needs Java and TLC. PNG rendering uses the dependencies declared in the helper.
- The optional PR watcher and orchestration CLI use Bun and the declared dependencies in skills/poteto-mode/scripts/package.json. Run bun install --frozen-lockfile in that directory before using them. Their bootstrap reports missing dependencies rather than installing them automatically. Live GitHub operations also need an available authenticated forge integration or gh.
- The installer and worktree audit use Python 3.9 or later. The shell wrappers expect a Unix-like environment.

The dormant Cursor-only Benny automation pack is excluded. make-bot-ui can build an interface for an existing authorized webhook; it cannot provision an inbound Codex webhook. A requested multi-model panel depends on the models and delegation features the host actually exposes.

## Validation

Completed on 2026-10-26:

| Check | Result |
| --- | --- |
| Official Codex skill validator | 59 passed. |
| Skill metadata, invocation policies, manifests, configuration, and relative Markdown links | Passed. |
| Installer and audit behavior tests | 4 passed, including conflicting installations and ignored/locked worktrees. |
| Archive and link-validation tests | 2 passed, including hidden marketplace files, extraction validation, exclusion of local files, and Scala syntax versus actual Markdown links. |
| Source-case lookup tests | 3 passed: filtering, exact evidence, PR correction context, pagination, and invalid input. |
| Native Codex plugin installation | Installed and enabled; all 59 cached skills matched the local fork. |
| Upstream statechart suite | 50 passed, 0 failed, 100 skipped because TLC or rendering dependencies were unavailable. |
| JavaScript and TypeScript syntax | 38 files passed; TypeScript was transformed for syntax checking. |
| Shell syntax and decision-log smoke test | Passed. |

The Bun-dependent test suites, TypeScript type checking, and live GitHub actions were not exercised. The Scala/Akka skill has a source extraction and independent review record, with all three reviewers and the primary agent approving the same final artifact hashes after repairs; this is separate from an end-to-end execution of the full pstack workflows. The statechart tests ran with offline package resolution and workspace-local caches. Validation details are recorded in validation.json.

From this directory, reproduce the package and local utility checks with:

~~~bash
python3 verify.py
python3 -m unittest discover -s tests -v
~~~
