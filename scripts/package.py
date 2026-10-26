#!/usr/bin/env python3
"""Build a distributable ZIP containing this fork's plugin and local marketplace."""

import argparse
from pathlib import Path
import sys
import zipfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import validate_package

FILES = {
    'README.md', 'LICENSE', 'UPSTREAM.json', 'validation.json',
    'plugin.json', '.codex-plugin/plugin.json',
    '.agents/plugins/marketplace.json', '.gitignore', '.gitattributes',
    'verify.py', 'install.py', 'scripts/package.py',
}
DIRECTORIES = ('skills', 'tests')
EXCLUDED_PARTS = {'__pycache__', 'node_modules', '.git', '.venv', 'dist'}


def build(output):
    problems = validate_package(ROOT)
    if problems:
        raise ValueError('Invalid package:\n' + '\n'.join(problems))
    candidates = {ROOT / name for name in FILES}
    for directory in DIRECTORIES:
        candidates.update((ROOT / directory).rglob('*'))
    files = []
    for path in sorted(candidates):
        relative = path.relative_to(ROOT)
        if path.is_symlink():
            raise ValueError('Refusing to package a symlink: ' + str(relative))
        if (not path.is_file() or EXCLUDED_PARTS.intersection(relative.parts)
                or path.suffix in ('.pyc', '.pyo') or path.name == '.DS_Store'):
            continue
        if path.resolve() == output.resolve():
            raise ValueError('Output must not replace a packaged source file.')
        files.append(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + '.tmp')
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in files:
                archive.write(path, Path(ROOT.name) / path.relative_to(ROOT))
        with zipfile.ZipFile(temporary) as archive:
            corrupt = archive.testzip()
            if corrupt:
                raise ValueError('Archive integrity check failed: ' + corrupt)
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print('Created', output, 'with', len(files), 'files.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist/pstack-codex.zip')
    args = parser.parse_args()
    try:
        build(args.output.expanduser().resolve())
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
