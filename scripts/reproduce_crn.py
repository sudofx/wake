"""Run an offline equilibrium reproduction; optional native receipt in a paused installation."""
import argparse
import json
from pathlib import Path
from wake.reproduction import reproduce, result_id


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--data')
    args = parser.parse_args()
    report = reproduce()
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + '\n')
    if args.data:
        from wake.authority import open_authoritative_store
        root = Path(args.data)
        if json.loads((root/'.wake-runner-control.json').read_text()).get('research') != 'paused':
            parser.error('Pause research before recording a reproduction')
        store = open_authoritative_store(root, allow_initialize=False)
        try:
            with store.lock():
                if store.record.incomplete_invocations(): parser.error('Drain unfinished invocations first')
                if result_id(report) not in store.load().get('reproductions', {}):
                    store.append('reproduction_recorded', {'actor': 'operator', 'report': report})
        finally: store.close()
    print(json.dumps({'id': result_id(report), 'passed': report['acceptance']['passed'],
                      'errors': [r['total_variation_error'] for r in report['runs']], 'output': str(target.resolve())}))
    return 0 if report['acceptance']['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
