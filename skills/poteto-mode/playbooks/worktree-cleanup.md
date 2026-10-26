### Worktree and simulator cleanup

1. Run scripts/worktree-audit.sh [-b <base-ref>] [repo-path] from this skill's directory. The helper only reads local Git metadata and size. It never fetches, reads chats, or deletes. Its --json form records exact paths and SHAs. Pass the PR base explicitly when needed.
2. Check usage through available Codex artifact and thread tools. A review-merged bucket means only that the head is an ancestor of the local base. It does not prove that the app no longer uses the checkout, that local refs are current, or that a squash merge is represented.
3. Preserve tracked, untracked, ignored, and unpublished work. A failed status read or missing path is unknown, never clean. Locked worktrees stay held. Inspect any candidate's actual contents and purpose.
4. For a managed worktree attached to this chat, prefer Codex's archive_worktree tool. It saves a recoverable snapshot and enforces ownership checks. Preserve needed ignored files separately. Do not use raw removal to bypass a tool's refusal.
5. For an unmanaged checkout, act only within the user's cleanup authorization after checking usage and recoverability. Do not force removal of uncommitted or unknown work. Do not delete worktrees owned by unrelated chats.
6. Simulator or cache cleanup is a separate scope. Inventory the specific requested resource and preserve user data. A request to inspect worktree size does not authorize deleting simulators or application state.

Reply with space reclaimed when measured, what was archived or removed, and each held candidate with its concrete reason.
