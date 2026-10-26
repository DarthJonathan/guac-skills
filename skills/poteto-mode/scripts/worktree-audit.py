#!/usr/bin/env python3
"""Read-only local Git worktree audit. Never reads chats, fetches, or deletes."""

import argparse
import json
import os
from pathlib import Path
import subprocess


def git(repo, *args, check=True):
    result = subprocess.run(
        ['git', '-C', str(repo), *args], capture_output=True, text=True,
        env={**os.environ, 'GIT_OPTIONAL_LOCKS': '0'},
    )
    if check and result.returncode:
        raise ValueError(result.stderr.strip() or 'Git command failed.')
    return result


def commit(repo, ref):
    result = git(repo, 'rev-parse', '--verify', '--end-of-options', ref + '^{commit}', check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def audit(repo, base=None):
    git(repo, 'rev-parse', '--git-dir')
    if not base:
        default = git(repo, 'symbolic-ref', '--short', 'refs/remotes/origin/HEAD', check=False).stdout.strip()
        base = next((candidate for candidate in (default, 'origin/main', 'origin/master', 'main', 'master')
                     if candidate and commit(repo, candidate)), None)
    if not base or not (base_sha := commit(repo, base)):
        raise ValueError('No local base ref found. Pass --base <ref>; fetch explicitly if needed.')
    records = []
    current = {}
    for field in git(repo, 'worktree', 'list', '--porcelain', '-z').stdout.split('\0'):
        if not field:
            if current:
                records.append(current)
                current = {}
            continue
        key, _, value = field.partition(' ')
        current[key] = value
    if current:
        records.append(current)
    rows = []
    for entry in records[1:]:
        path = Path(entry['worktree'])
        head = entry.get('HEAD')
        merged_result = git(repo, 'merge-base', '--is-ancestor', head, base_sha, check=False) if head else None
        merged = (merged_result.returncode == 0 if merged_result and merged_result.returncode in (0, 1) else None)
        status = git(path, 'status', '--porcelain=v1', '-z', '--untracked-files=all', '--ignored=matching', check=False)
        items = [item for item in status.stdout.split('\0') if item]
        dirty = None if status.returncode else bool(items)
        if 'locked' in entry:
            bucket = 'hold-locked'
        elif dirty is None or merged is None:
            bucket = 'hold-unknown'
        elif dirty:
            bucket = 'hold-work'
        else:
            bucket = 'review-merged' if merged else 'review-unmerged'
        size = subprocess.run(['du', '-sk', str(path)], capture_output=True, text=True)
        size_kib = int(size.stdout.split()[0]) if size.returncode == 0 and size.stdout.split() else None
        rows.append({
            'path': str(path), 'branch': entry.get('branch'), 'head': head,
            'merged_by_ancestry': merged, 'has_tracked_untracked_or_ignored_work': dirty,
            'size_kib': size_kib, 'locked': 'locked' in entry,
            'app_usage': 'not checked', 'pr_state': 'not checked', 'bucket': bucket,
        })
    rows.sort(key=lambda row: row['size_kib'] if row['size_kib'] is not None else -1, reverse=True)
    return {'base': base, 'base_sha': base_sha, 'primary': records[0]['worktree'] if records else None,
            'note': 'Local refs only. Chat use and PR state need separate checks. No bucket authorizes deletion.',
            'worktrees': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-b', '--base')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('repo', nargs='?', default='.', type=Path)
    args = parser.parse_args()
    try:
        report = audit(args.repo.resolve(), args.base)
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print('Base:', report['base'], report['base_sha'])
        print(report['note'])
        print('SIZE_KIB\tMERGED\tHAS_WORK\tBUCKET\tWORKTREE')
        for row in report['worktrees']:
            print('\t'.join(str(value) for value in (
                row['size_kib'], row['merged_by_ancestry'],
                row['has_tracked_untracked_or_ignored_work'], row['bucket'], row['path'])))


if __name__ == '__main__':
    main()
