# Source-specific review case index

5,790 cases from 6,087 source comments, with 6,087 rows accounted for. Topic labels are overlapping navigation categories, not claims about prevalence.

Use the lookup script to search concrete symbols and read source evidence. Read the full relevant PR thread when a statement is revised, conditional, or refers to an earlier comment.

```bash
python3 scripts/find_patterns.py "PlanJdbcEventProcessor"
python3 scripts/find_patterns.py --pr 3029 --format markdown --all
python3 scripts/find_patterns.py --id R-3538 --format markdown
```

Paths in these examples are relative to this skill directory.

| Topic | Source cases | Read for |
| --- | ---: | --- |
| [scala-collections](patterns/scala-collections.md) | 375 | Scala syntax, Option, collections, ordering, and allocation |
| [async-effects](patterns/async-effects.md) | 390 | Future and DBIO composition, timeouts, and concurrency |
| [actor-state](patterns/actor-state.md) | 435 | Commands, entity state, validation, and compare-and-set |
| [persistence-evolution](patterns/persistence-evolution.md) | 229 | Events, snapshots, serializers, and historical evolution |
| [projections-delivery](patterns/projections-delivery.md) | 426 | Readside freshness, replay, delivery, and partial writes |
| [kafka-streams](patterns/kafka-streams.md) | 167 | Partition keys, subscribers, streams, and consumer groups |
| [database](patterns/database.md) | 360 | Slick, PostgreSQL, Cassandra, keys, queries, and indexes |
| [api-types-json](patterns/api-types-json.md) | 1,842 | API contracts, DTOs, sealed variants, JSON, and defaults |
| [errors-observability](patterns/errors-observability.md) | 646 | Exceptions, retries, logs, metrics, and runtime configuration |
| [testing](patterns/testing.md) | 350 | Test contracts, fixtures, serialization matrices, and observed results |
| [rollout-operations](patterns/rollout-operations.md) | 654 | Migration, release order, CI, probes, and operations |
| [domain-validation](patterns/domain-validation.md) | 2,848 | Specific business predicates, products, account types, and calculations |
| [design-scope](patterns/design-scope.md) | 1,368 | Component ownership, naming, abstractions, and change scope |

## Source records and review status

- [Canonical machine-readable catalog](pattern-catalog.json).
- [Per-source-row coverage ledger](source-coverage.jsonl).
- [Additional source thread context](thread-context.json), included automatically by PR lookup.
- [Source provenance and exact-quote validation](source-provenance.json).
- [Reviewer convergence record](review-convergence.json).
