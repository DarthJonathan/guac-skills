### Pause safely

Use this only when the user explicitly asks to pause or stop. Context compaction alone is not a request to pause.

1. Stop at a safe boundary. Avoid starting new work and send a hold to any active native workers.
2. Preserve the files and useful process state. Do not discard edits or create a PR, push, or commit merely to manufacture a clean tree. Use a recoverable snapshot or commit when already authorized or requested.
3. Record a resume note with the goal, constraints, exact paths and branch, completed work, verification, outstanding work, and the first next action. Link an existing decision trail instead of duplicating it.
4. If a native goal or automation is active, update its status using the appropriate host tool only as the user's request permits.

Reply with the handoff location, preserved state, and how to resume.
