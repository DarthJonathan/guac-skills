#!/usr/bin/env python3
"""Install this skill bundle without replacing existing skills."""

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile

sys.dont_write_bytecode = True
from verify import validate_package


def fingerprint(folder):
    return {
        str(path.relative_to(folder)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in folder.rglob('*') if path.is_file()
    }


def install(target, dry_run=False):
    package = Path(__file__).resolve().parent
    errors = validate_package(package)
    if errors:
        raise ValueError('Invalid package:\n' + '\n'.join(errors))
    source = package / 'skills'
    pending = []
    unchanged = []
    conflicts = []
    for skill in sorted(source.iterdir()):
        if not skill.is_dir():
            continue
        destination = target / skill.name
        if destination.exists() or destination.is_symlink():
            if (destination.is_dir() and not destination.is_symlink()
                    and fingerprint(skill) == fingerprint(destination)):
                unchanged.append(skill.name)
            else:
                conflicts.append(str(destination))
        else:
            pending.append(skill)
    if conflicts:
        raise FileExistsError('Existing skills differ; nothing was installed:\n' + '\n'.join(conflicts))
    if dry_run:
        print('Would install', len(pending), 'skills;', len(unchanged), 'already identical.')
        return
    if not pending:
        print('All', len(unchanged), 'skills are already installed and identical.')
        return
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.pstack-install-', dir=target) as temporary:
        staging = Path(temporary)
        for skill in pending:
            shutil.copytree(skill, staging / skill.name)
        installed = []
        try:
            for skill in pending:
                destination = target / skill.name
                if destination.exists() or destination.is_symlink():
                    raise FileExistsError('Destination changed during installation: ' + str(destination))
                os.rename(staging / skill.name, destination)
                installed.append(skill.name)
        except OSError:
            print('Installed before interruption:', ', '.join(installed), file=sys.stderr)
            print('Existing destinations were preserved. Rerun to finish.', file=sys.stderr)
            raise
    print('Installed', len(installed), 'skills in', target)
    print('Invoke $poteto-mode in Codex. Restart Codex if the skills do not appear.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, type=Path,
                        help='Codex skills directory, for example ~/.agents/skills or <repo>/.agents/skills')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        install(args.target.expanduser().resolve(), args.dry_run)
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
