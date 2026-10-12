"""Preview or append operator source corrections to an explicitly paused installation."""
import argparse
import json
from pathlib import Path
from wake.authority import open_authoritative_store
from wake.research_reviews import weak_notebook_reviews


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    root = Path(args.data)
    control = json.loads((root / '.wake-runner-control.json').read_text())
    if control.get('research') != 'paused':
        parser.error('Pause research before reviewing this installation')
    store = open_authoritative_store(root, allow_initialize=False)
    try:
        with store.lock():
            if store.record.incomplete_invocations():
                parser.error('Drain unfinished invocations before applying reviews')
            state = store.load()
            reviews = [r for r in weak_notebook_reviews(state)
                       if f"{r['notebook']}@{r['revision']}" not in state.get('research_reviews', {})]
            for review in reviews:
                if args.apply:
                    store.append('scientific_review_recorded', review)
            print(json.dumps({'applied': args.apply, 'reviews': reviews}, ensure_ascii=False))
    finally:
        store.close()


if __name__ == '__main__':
    main()
