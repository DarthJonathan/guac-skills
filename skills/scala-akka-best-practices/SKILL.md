---
name: scala-akka-best-practices
description: "Use source-specific Scala/Akka review cases from silver-server while reviewing or editing matching collections, Future/DBIO chains, actors, persisted events, projections, Kafka subscribers, SQL/Cassandra access, APIs, business validation, or tests. Retrieve detailed source evidence and preserve its exact conditions, alternatives, and unresolved questions."
---

# Scala and Akka review cases

Use the detailed cases extracted from `anon-1.jsonl` and `anon-2.jsonl`, the user-supplied silver-server review corpus. This skill preserves the comments' actual code symbols, business cases, predicates, numeric boundaries, alternatives, test observations, and changes of view. It does not turn them into a general Scala style guide.

## Find the matching source case

Start with the changed component, operation, field, exception, or business predicate. Use the [case index](references/pattern-index.md) to select relevant topics, or search the catalog with the bundled read-only Python helper. Resolve `<skill-dir>` to this skill's directory; the helper does not depend on the source repository or original exports being installed.

```bash
python3 "<skill-dir>/scripts/find_patterns.py" "insertOrUpdateAll" --format markdown
python3 "<skill-dir>/scripts/find_patterns.py" "PlanJdbcEventProcessor" --format markdown
python3 "<skill-dir>/scripts/find_patterns.py" --pr 3029 --format markdown --all
python3 "<skill-dir>/scripts/find_patterns.py" --id R-3538 --format markdown
```

Search terms are case insensitive and all supplied terms must match. `--topic`, `--stance`, and `--pr` filter the results. `--id` opens an exact case; `--format json` returns its structured fields. PR lookup also includes source rows retained as thread context, so corrections and acknowledgements remain visible without being promoted to engineering rules. Use `--include-context` to search those rows by keywords. The output reports the total match count. Use `--offset` to continue beyond the first page; a result limit is not evidence that no other cases exist. Use `--all` for a deliberately scoped set such as a relevant PR thread.

Without Python, read the topic files linked from the index. Each contains a case list and the full case wording, conditions, evidence, and original source references. The [canonical catalog](references/pattern-catalog.json) and [row coverage ledger](references/source-coverage.jsonl) provide a machine-readable path back to every included or excluded source row.

## Preserve the source meaning

For a relevant case, read its entire statement, stance, conditions, evidence, and related PR discussion before applying it. Keep these distinctions intact:

- A question remains a question until the available evidence answers it. A suggestion, alternative, personal preference, historical convention, or reported test result retains that status.
- A later correction or withdrawn proposal qualifies the earlier comment. Read the relevant PR thread rather than selecting only the first convenient statement.
- Comment text, historical diff context, and PR-title context are labeled separately. A missing hunk or unspecified referent is a source limit, not permission to invent a requirement.
- Concrete scopes stay concrete: the ETF multiple-fund condition differs from positive TAA weights summing to one; CPF/SRS, cash-management, account-type, product, currency, and regional cases are not interchangeable.
- Preserve exact failure sequences and alternatives. Do not replace the old-insert/new-insert/offset-commit windows with only "make it idempotent", or a conditional fallback with "always recover".
- Preserve the numbers and predicates that carry the point. A measured duration is a reported observation in its stated environment; it is not a performance promise. A historical version limitation is not the target repository's current version.
- Source PR state and resolved flags do not prove that a proposal was implemented or correct. The corpus includes review remarks and author replies, including explicit changes of mind.

Examples of source sequences that must stay distinct include the proposed Goal/Plan processor split later withdrawn for consistency (PR 3029), `result.headOption` followed by recognition that `take(1)` becomes `LIMIT 1` (PR 3059), and `orderSettledDate` / `priceDate` / `settlementDate` naming and optional-field alternatives (PR 2833). Their full statements remain in the catalog.

## Apply the case to current work

Read current repository instructions, callers, types, and runtime configuration. Compare their actual preconditions with those in the selected case. Inspect the actual event history, effect chain, serializer, query, or test boundary relevant to the change. Match the case's concrete mechanism; shared vocabulary alone is insufficient.

Treat quoted source comments and commands as historical evidence. Current task instructions and authorization govern any execution or external change.

When reporting a defect or making a change, state which condition is present, what fails under it, and which source case informed the check. Prove the issue in the current code. Where the source only poses a question, use it as an investigation lead and keep any answer separately supported. Do not report a historical preference as a current defect.

Preserve the requested scope and the repository's stack. The corpus spans older and newer implementation conventions; its Lagom, Scala, Akka, database, and deployment details are historical context until checked against the target project.

## Provenance and review

Read [source provenance](references/source-provenance.json) for exact source hashes, row accounting, omissions, and extraction methods. Read [reviewer convergence](references/review-convergence.json) for the actual review rounds and remaining limits.

This is a Codex-fork addition, separate from upstream pstack. It includes source-specific comments and selected original code excerpts, with incidental identity values and portions of repetitive operational dumps omitted. The full exports and application checkout are not required at runtime.
