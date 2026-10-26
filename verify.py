#!/usr/bin/env python3
"""Validate this generated package with Python's standard library."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate_package(root):
    errors = []
    try:
        provenance = json.loads((root / 'UPSTREAM.json').read_text())
        manifest = json.loads((root / 'plugin.json').read_text())
        compatibility = json.loads((root / '.codex-plugin/plugin.json').read_text())
        if manifest['name'] != compatibility['name'] or manifest['version'] != compatibility['version']:
            errors.append('Plugin manifests disagree.')
        marketplace = json.loads((root / '.agents/plugins/marketplace.json').read_text())
        entries = marketplace.get('plugins', [])
        if not marketplace.get('name') or len(entries) != 1:
            errors.append('Expected one named local marketplace entry.')
        else:
            entry = entries[0]
            source = entry.get('source', {})
            relative = source.get('path', '')
            if (entry.get('name') != manifest['name']
                    or source.get('source') != 'local'
                    or not relative.startswith('./')
                    or (root / relative).resolve() != root.resolve()):
                errors.append('Local marketplace must resolve to this plugin root.')
            if entry.get('policy', {}).get('installation') != 'AVAILABLE' or not entry.get('category'):
                errors.append('Local marketplace policy or category is missing.')
            if entry.get('policy', {}).get('authentication') != 'ON_INSTALL':
                errors.append('Unexpected marketplace authentication policy.')
        inventory = provenance['skills'] + provenance.get('fork_skills', [])
        expected = {entry['name']: entry for entry in inventory}
        if len(expected) != len(inventory):
            errors.append('Skill inventory contains duplicate names.')
        actual = {path.parent.name for path in (root / 'skills').glob('*/SKILL.md')}
        if expected.keys() != actual:
            errors.append('Skill inventory differs from UPSTREAM.json.')
        if not (root / 'LICENSE').is_file():
            errors.append('LICENSE is missing.')
        for name in sorted(actual):
            skill = root / 'skills' / name
            content = (skill / 'SKILL.md').read_text()
            match = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: (".*")\n---\n', content)
            if not match:
                errors.append(name + ': invalid generated frontmatter.')
                continue
            description = json.loads(match[2])
            if match[1] != name or not description or len(description) > 1024 or '<' in description or '>' in description:
                errors.append(name + ': invalid name or description.')
            metadata = (skill / 'agents/openai.yaml').read_text()
            ui = {}
            for line in metadata.splitlines():
                field = re.match(r'  (display_name|short_description|default_prompt): (".*")$', line)
                if field:
                    ui[field[1]] = json.loads(field[2])
            if set(ui) != {'display_name', 'short_description', 'default_prompt'}:
                errors.append(name + ': incomplete UI metadata.')
            elif not 25 <= len(ui['short_description']) <= 64 or '$' + name not in ui['default_prompt']:
                errors.append(name + ': invalid UI metadata.')
            explicit = 'allow_implicit_invocation: false' in metadata
            if explicit != expected[name]['explicit_only']:
                errors.append(name + ': invocation policy differs from the recorded inventory.')
        onboarding = manifest['extensions']['com.openai']['onboardingSkill']
        if not (root / onboarding).is_file():
            errors.append('Onboarding skill is missing.')
        for path in (root / 'skills').rglob('*.md'):
            text = path.read_text()
            source_cases = root / 'skills/scala-akka-best-practices/references/patterns'
            if path.is_relative_to(source_cases):
                text = '\n'.join(line for line in text.splitlines() if not line.startswith('>'))
            text = re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', text)
            text = re.sub(r'`+[^`\n]*`+', '', text)
            for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)', text):
                target = target.strip().strip('<>')
                if not target or target.startswith(('#', '/', '~', '$')) or '<' in target or '>' in target:
                    continue
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                relative = unquote(parsed.path)
                if not relative:
                    continue
                resolved = (path.parent / relative).resolve()
                if not resolved.is_relative_to(root.resolve()):
                    errors.append(str(path.relative_to(root)) + ': link escapes package: ' + target)
                elif not resolved.exists():
                    errors.append(str(path.relative_to(root)) + ': missing link: ' + target)
        example = json.loads((root / 'skills/poteto-mode/references/pstack-models.example.json').read_text())
        if example['schema_version'] != 1 or not isinstance(example['roles'], dict) or not isinstance(example['panels'], dict):
            errors.append('Invalid pstack configuration example.')
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(str(error))
    return errors


if __name__ == '__main__':
    problems = validate_package(Path(__file__).resolve().parent)
    if problems:
        print('\n'.join(problems), file=sys.stderr)
        sys.exit(1)
    count = len(list((Path(__file__).resolve().parent / 'skills').glob('*/SKILL.md')))
    print(f'Valid: {count} skills, invocation policies, UI metadata, manifests, local marketplace, configuration, and local Markdown links.')
