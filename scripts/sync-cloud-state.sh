#!/usr/bin/env bash
set -euo pipefail

if (( $# != 0 )); then
  echo "Error: sync-cloud-state.sh does not run WAKE✳︎ cycles or accept a cycle count." >&2
  echo "To run cycles: ./scripts/run-wake-cycles.sh N" >&2
  echo "To sync cloud state afterward: ./scripts/sync-cloud-state.sh" >&2
  exit 64
fi

ROOT="$(git rev-parse --show-toplevel)"
REF="origin/wake-state"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cd "$ROOT"

echo "→ Fetching wake-state..."
git fetch origin +refs/heads/wake-state:refs/remotes/origin/wake-state

echo "→ Exporting complete cloud record..."
git archive "$REF" | tar -x -C "$STAGE"

echo "→ Verifying required state..."
test -f "$STAGE/data/wake.sqlite3"
test -f "$STAGE/state.json"
test -f "$STAGE/events.jsonl"
test -f "$STAGE/head.txt"
test -d "$STAGE/site"

python3 - "$STAGE/data/wake.sqlite3" <<'PY'
import sqlite3, sys
db = sqlite3.connect(f"file:{sys.argv[1]}?mode=ro", uri=True)
result = db.execute("PRAGMA quick_check").fetchone()[0]
db.close()
if result != "ok":
    raise SystemExit(f"SQLite verification failed: {result}")
print("  SQLite: ok")
PY

echo "→ Replacing local cloud-state copy..."

rm -rf "$ROOT/data" "$ROOT/site"
mv "$STAGE/data" "$ROOT/data"
mv "$STAGE/site" "$ROOT/site"

cp "$STAGE/state.json"   "$ROOT/state.json"
cp "$STAGE/events.jsonl" "$ROOT/events.jsonl"
cp "$STAGE/head.txt"     "$ROOT/head.txt"

# Keep cloud-state root files out of local git status without changing .gitignore.
for f in /state.json /events.jsonl /head.txt; do
    grep -qxF "$f" "$ROOT/.git/info/exclude" 2>/dev/null ||
        echo "$f" >> "$ROOT/.git/info/exclude"
done

echo
echo "✓ Full wake-state synced locally"
echo "  data/"
echo "  site/"
echo "  state.json"
echo "  events.jsonl"
echo "  head.txt"
echo
echo "Cloud head: $(cat "$ROOT/head.txt")"
