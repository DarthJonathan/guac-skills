#!/usr/bin/env python3
"""Find source-specific review cases without loading the whole catalog."""

import argparse
import json
from pathlib import Path
import sys


CATALOG = Path(__file__).resolve().parents[1] / 'references/pattern-catalog.json'


def searchable_text(value):
    if isinstance(value, dict):
        return '\n'.join(str(key) + '\n' + searchable_text(item) for key, item in value.items())
    if isinstance(value, list):
        return '\n'.join(searchable_text(item) for item in value)
    return '' if value is None else str(value)


def source_label(evidence):
    return f"{evidence['file']}:{evidence['line']} · comment {evidence['comment_id']}"


def markdown(record):
    context = record['context']
    if isinstance(context, dict):
        context = '; '.join(f'{key}: {value}' for key, value in context.items())
    lines = [f"## {record['id']} — {record['title']}", '',
             f"**Source stance:** {record['stance']}", '',
             '**Context:**', '']
    lines.extend('> ' + line for line in context.splitlines())
    lines.append('')
    if record.get('concern'):
        lines.extend(['**Concern stated in the source:** ' + record['concern'], ''])
    lines.extend(['**Source-preserving request, proposal, or question:**', ''])
    lines.extend('> ' + line for line in record['requested_change'].splitlines())
    lines.append('')
    if record.get('constraints'):
        lines.extend(['**Conditions and limits:**', ''])
        lines.extend('- ' + item for item in record['constraints'])
        lines.append('')
    for evidence in record['evidence']:
        label = source_label(evidence)
        if evidence.get('pr_id') is not None:
            label += f" · PR {evidence['pr_id']}"
        if evidence.get('created_on'):
            label += ' · ' + evidence['created_on'][:10]
        lines.extend(['**Evidence:** ' + label, ''])
        if evidence.get('inline_path'):
            lines.extend(['Source path: `' + evidence['inline_path'] + '`', ''])
        if evidence.get('quote') and evidence['quote'] != record['requested_change']:
            lines.extend('> ' + line for line in evidence['quote'].splitlines())
            lines.append('')
        if evidence.get('context_quote'):
            lines.extend(['**Explicit source context (' + evidence['context_field'] + '):**', ''])
            lines.extend('> ' + line for line in evidence['context_quote'].splitlines())
            lines.append('')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='*', help='Require every term or quoted phrase, ignoring case.')
    parser.add_argument('--id', action='append', default=[], help='Select an exact case ID; repeatable.')
    parser.add_argument('--topic', action='append', default=[], help='Select a topic; repeatable, matches any.')
    parser.add_argument('--stance', action='append', default=[], help='Select a source stance; repeatable.')
    parser.add_argument('--pr', type=int, action='append', default=[], help='Select source PR threads; repeatable.')
    parser.add_argument('--include-context', action='store_true', help='Also search source rows retained as thread context. PR lookup always includes them.')
    parser.add_argument('--limit', type=int, default=12)
    parser.add_argument('--all', action='store_true', help='Return every match rather than a limited page.')
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--format', choices=['list', 'markdown', 'json'], default='list')
    parser.add_argument('--catalog', type=Path, default=CATALOG)
    args = parser.parse_args()
    if args.limit < 1 or args.offset < 0:
        parser.error('--limit must be positive and --offset must be nonnegative.')
    try:
        catalog = json.loads(args.catalog.read_text())
        records = catalog['patterns'] if isinstance(catalog, dict) else catalog
        if not isinstance(records, list):
            raise ValueError('Expected an array of patterns.')
        if args.pr or args.include_context or args.id:
            context_path = args.catalog.with_name('thread-context.json')
            if context_path.is_file():
                records = records + json.loads(context_path.read_text())
        records = sorted(records, key=lambda record: (min((item['file'], item['line']) for item in record['evidence']), record['id']))
        matches = []
        terms = [term.casefold() for term in args.query]
        for record in records:
            if args.id and record['id'] not in args.id:
                continue
            if args.topic and not set(args.topic).intersection(record['topics']):
                continue
            if args.stance and record['stance'] not in args.stance:
                continue
            if args.pr and not any(item.get('pr_id') in args.pr for item in record['evidence']):
                continue
            searchable = searchable_text(record).casefold()
            if all(term in searchable for term in terms):
                matches.append(record)
        stop = None if args.all else args.offset + args.limit
        selected = matches[args.offset:stop]
        if args.format == 'json':
            print(json.dumps({'total_matches': len(matches), 'offset': args.offset,
                              'returned': len(selected), 'patterns': selected},
                             indent=2, ensure_ascii=False))
        else:
            print(f'Showing {len(selected)} of {len(matches)} matching cases (offset {args.offset}).')
            for record in selected:
                if args.format == 'markdown':
                    print('\n' + markdown(record))
                else:
                    sources = ', '.join(source_label(item) for item in record['evidence'])
                    print(f"{record['id']} [{record['stance']}] {record['title']}\n  {sources}")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
