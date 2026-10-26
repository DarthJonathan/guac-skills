import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'skills/poteto-mode/scripts/worktree-audit.py'
SKILL_NAMES = {path.parent.name for path in (ROOT / 'skills').glob('*/SKILL.md')}
LOOKUP = ROOT / 'skills/scala-akka-best-practices/scripts/find_patterns.py'


def run(*args, check=True):
    result = subprocess.run([str(arg) for arg in args], capture_output=True, text=True)
    if check and result.returncode:
        raise AssertionError(result.stdout + result.stderr)
    return result


def git(repo, *args):
    return run('git', '-C', repo, '-c', 'core.hooksPath=/dev/null',
               '-c', 'commit.gpgsign=false', '-c', 'user.name=Port Test',
               '-c', 'user.email=port-test@example.invalid', *args)


class InstallerTests(unittest.TestCase):
    def test_dry_run_install_and_repeat(self):
        with tempfile.TemporaryDirectory(prefix='pstack-install-test-') as directory:
            target = Path(directory) / 'skills with spaces'
            run(sys.executable, ROOT / 'install.py', '--target', target, '--dry-run')
            self.assertFalse(target.exists())
            result = run(sys.executable, ROOT / 'install.py', '--target', target)
            self.assertIn(f'Installed {len(SKILL_NAMES)} skills', result.stdout)
            self.assertEqual({path.parent.name for path in target.glob('*/SKILL.md')}, SKILL_NAMES)
            self.assertTrue((target / 'poteto-mode/references/codex-adapter.md').is_file())
            result = run(sys.executable, ROOT / 'install.py', '--target', target)
            self.assertIn('already installed and identical', result.stdout)

    def test_conflict_preserves_existing_skill_and_installs_nothing(self):
        with tempfile.TemporaryDirectory(prefix='pstack-conflict-test-') as directory:
            target = Path(directory) / 'skills'
            existing = target / 'poteto-mode'
            existing.mkdir(parents=True)
            sentinel = existing / 'SKILL.md'
            sentinel.write_text('User-maintained skill.\n')
            result = run(sys.executable, ROOT / 'install.py', '--target', target, check=False)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(sentinel.read_text(), 'User-maintained skill.\n')
            self.assertEqual([path.name for path in target.iterdir()], ['poteto-mode'])


class AuditTests(unittest.TestCase):
    def test_audit_preserves_work_and_reports_ignored_locked_and_unmerged_trees(self):
        with tempfile.TemporaryDirectory(prefix='pstack-audit-test-') as directory:
            directory = Path(directory)
            repo = directory / 'repo'
            repo.mkdir()
            git(repo, 'init', '-b', 'main')
            (repo / '.gitignore').write_text('ignored/\n')
            (repo / 'app.txt').write_text('baseline\n')
            git(repo, 'add', '.gitignore', 'app.txt')
            git(repo, 'commit', '-m', 'baseline')
            clean = directory / 'clean tree'
            dirty = directory / 'tree with ignored work'
            locked = directory / 'locked tree'
            unmerged = directory / 'unmerged tree'
            for branch, path in [('clean', clean), ('dirty', dirty), ('locked', locked), ('unmerged', unmerged)]:
                git(repo, 'worktree', 'add', '-b', branch, path)
            (dirty / 'ignored').mkdir()
            asset = dirty / 'ignored/keep.bin'
            asset.write_bytes(b'valuable ignored data')
            git(repo, 'worktree', 'lock', locked)
            (unmerged / 'app.txt').write_text('unmerged work\n')
            git(unmerged, 'add', 'app.txt')
            git(unmerged, 'commit', '-m', 'unmerged behavior')
            before = git(repo, 'worktree', 'list', '--porcelain').stdout
            report = json.loads(run(sys.executable, AUDIT, '--base', 'main', '--json', repo).stdout)
            rows = {Path(row['path']).name: row for row in report['worktrees']}
            self.assertEqual(rows[clean.name]['bucket'], 'review-merged')
            self.assertEqual(rows[dirty.name]['bucket'], 'hold-work')
            self.assertEqual(rows[locked.name]['bucket'], 'hold-locked')
            self.assertEqual(rows[unmerged.name]['bucket'], 'review-unmerged')
            self.assertEqual(rows[clean.name]['app_usage'], 'not checked')
            self.assertEqual(asset.read_bytes(), b'valuable ignored data')
            self.assertEqual(git(repo, 'worktree', 'list', '--porcelain').stdout, before)
            self.assertTrue(all(path.is_dir() for path in (clean, dirty, locked, unmerged)))

    def test_bad_repository_fails_without_reporting_a_clean_worktree(self):
        with tempfile.TemporaryDirectory(prefix='pstack-missing-repo-') as directory:
            result = run(sys.executable, AUDIT, '--json', directory, check=False)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, '')


class SourceCaseLookupTests(unittest.TestCase):
    def make_catalog(self, directory):
        directory = Path(directory)
        quote = 'Keep `mapAsync(1)` here.\nA result is not the same as an acknowledgement: α > 0.\n"status": "FAILED"'

        def case(identifier, line, pr, title, stance, topics, statement):
            return {'id': identifier, 'title': title, 'stance': stance, 'topics': topics,
                    'context': 'Synthetic lookup fixture', 'concern': None,
                    'requested_change': statement, 'constraints': [],
                    'evidence': [{'file': 'fixture.jsonl', 'line': line,
                                  'comment_id': line, 'pr_id': pr, 'quote': statement}]}

        records = [case('C1', 1, 7, 'mapAsync question', 'open-question', ['kafka-streams'], quote),
                   case('C2', 2, 7, 'Separate write', 'explanation', ['database'], 'Second source case.'),
                   case('C3', 4, 8, 'mapAsync alternative', 'suggestion', ['async-effects'], 'Other thread.')]
        path = directory / 'catalog.json'
        path.write_text(json.dumps({'patterns': records}))
        context = [case('CTX1', 3, 7, 'Correction', 'thread-context', [], 'The earlier suggestion was withdrawn.')]
        (directory / 'thread-context.json').write_text(json.dumps(context))
        return path, quote

    def test_filters_keep_exact_source_wording(self):
        with tempfile.TemporaryDirectory(prefix='case-lookup-test-') as directory:
            catalog, quote = self.make_catalog(directory)
            result = json.loads(run(sys.executable, LOOKUP, 'MAPASYNC', '--topic', 'kafka-streams',
                                    '--stance', 'open-question', '--format', 'json', '--catalog', catalog).stdout)
            self.assertEqual(result['total_matches'], 1)
            self.assertEqual(result['patterns'][0]['id'], 'C1')
            self.assertEqual(result['patterns'][0]['evidence'][0]['quote'], quote)
            literal = json.loads(run(sys.executable, LOOKUP, '"status": "FAILED"', '--format', 'json',
                                     '--catalog', catalog).stdout)
            self.assertEqual([item['id'] for item in literal['patterns']], ['C1'])

    def test_pr_lookup_includes_correction_context_in_source_order(self):
        with tempfile.TemporaryDirectory(prefix='case-thread-test-') as directory:
            catalog, _ = self.make_catalog(directory)
            result = json.loads(run(sys.executable, LOOKUP, '--pr', '7', '--all',
                                    '--format', 'json', '--catalog', catalog).stdout)
            self.assertEqual([item['id'] for item in result['patterns']], ['C1', 'C2', 'CTX1'])
            self.assertEqual(result['patterns'][-1]['stance'], 'thread-context')
            exact = json.loads(run(sys.executable, LOOKUP, '--id', 'CTX1', '--format', 'json',
                                   '--catalog', catalog).stdout)
            self.assertEqual([item['id'] for item in exact['patterns']], ['CTX1'])

    def test_pagination_empty_result_and_invalid_limit_are_explicit(self):
        with tempfile.TemporaryDirectory(prefix='case-page-test-') as directory:
            catalog, _ = self.make_catalog(directory)
            before = catalog.read_bytes()
            result = json.loads(run(sys.executable, LOOKUP, '--limit', '1', '--offset', '1',
                                    '--format', 'json', '--catalog', catalog).stdout)
            self.assertEqual((result['total_matches'], result['returned']), (3, 1))
            self.assertEqual(result['patterns'][0]['id'], 'C2')
            empty = json.loads(run(sys.executable, LOOKUP, 'absent-query', '--format', 'json',
                                   '--catalog', catalog).stdout)
            self.assertEqual((empty['total_matches'], empty['patterns']), (0, []))
            invalid = run(sys.executable, LOOKUP, '--limit', '0', '--catalog', catalog, check=False)
            self.assertEqual(invalid.returncode, 2)
            self.assertEqual(catalog.read_bytes(), before)


class PackagingTests(unittest.TestCase):
    def test_scala_type_application_is_not_a_link_and_authored_missing_link_still_fails(self):
        with tempfile.TemporaryDirectory(prefix='source-link-test-') as directory:
            source = Path(directory) / 'fork'
            shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns('.git', 'node_modules', '__pycache__', 'dist'))
            fixture = source / 'skills/scala-akka-best-practices/references/patterns/link-fixture.md'
            fixture.write_text('# Source fixture\n\n> `column[String]("status")`\n\n```scala\nwire[Service](components)\n```\n')
            run(sys.executable, source / 'verify.py')
            fixture.write_text(fixture.read_text() + '\n[Authored missing reference](missing-reference.md)\n')
            result = run(sys.executable, source / 'verify.py', check=False)
            self.assertEqual(result.returncode, 1)
            self.assertIn('missing-reference.md', result.stderr)

    def test_archive_is_installable_and_excludes_local_files(self):
        with tempfile.TemporaryDirectory(prefix='pstack-package-test-') as directory:
            directory = Path(directory)
            source = directory / 'fork'
            shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns('.git', 'node_modules', '__pycache__', 'dist'))
            (source / '.env').write_text('SYNTHETIC_TEST_VALUE=do-not-package\n')
            (source / 'node_modules').mkdir()
            (source / 'node_modules/local.txt').write_text('local dependency\n')
            archive_path = directory / 'release.zip'
            run(sys.executable, source / 'scripts/package.py', '--output', archive_path)
            with zipfile.ZipFile(archive_path) as archive:
                names = set(archive.namelist())
                self.assertIn('fork/.agents/plugins/marketplace.json', names)
                self.assertIn('fork/.codex-plugin/plugin.json', names)
                self.assertIn('fork/plugin.json', names)
                self.assertIn('fork/LICENSE', names)
                self.assertNotIn('fork/.env', names)
                self.assertFalse(any('/node_modules/' in name or '/.git/' in name for name in names))
                archive.extractall(directory / 'extracted')
            extracted = directory / 'extracted/fork'
            run(sys.executable, extracted / 'verify.py')
            catalog = json.loads((extracted / '.agents/plugins/marketplace.json').read_text())
            entry = catalog['plugins'][0]
            plugin = (extracted / entry['source']['path']).resolve()
            self.assertEqual(plugin, extracted.resolve())
            self.assertEqual({path.parent.name for path in (plugin / 'skills').glob('*/SKILL.md')}, SKILL_NAMES)


if __name__ == '__main__':
    unittest.main()
