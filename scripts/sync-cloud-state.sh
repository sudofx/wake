#!/usr/bin/env bash
# WAKE✳︎ MAINTAINER NOTE
#
# Synchronizes the authoritative cloud record with local files. Routine sync is
# deliberately narrow: the SQLite record is durable authority; site/ and the
# large JSON exports are derived views and need not be recopied before a batch.
#
# Use --full only when a complete local mirror of the published cloud state is
# actually needed.

set -euo pipefail

FULL=0
if (( $# == 1 )) && [[ "$1" == "--full" ]]; then
  FULL=1
elif (( $# != 0 )); then
  echo "Usage: ./scripts/sync-cloud-state.sh [--full]" >&2
  echo "  default  Sync the authoritative SQLite record + head only." >&2
  echo "  --full   Also sync derived state/events exports and the generated site." >&2
  exit 64
fi

ROOT="$(git rev-parse --show-toplevel)"
REF="origin/wake-state"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cd "$ROOT"

echo "→ Fetching wake-state..."
# Fetch only the branch tip we need. Git transfers objects incrementally; no tags
# or unrelated branch history are requested here.
git fetch --no-tags origin +refs/heads/wake-state:refs/remotes/origin/wake-state

# A matching durable head means the local authoritative record is already
# current. Avoid re-archiving and rewriting a 50+ MB SQLite file in that case.
remote_head="$(git show "$REF:head.txt")"
if [[ -f "$ROOT/head.txt" ]] && [[ "$(cat "$ROOT/head.txt")" == "$remote_head" ]] && (( ! FULL )); then
  echo "✓ Durable cloud state already current; nothing to copy."
  echo "Cloud head: $remote_head"
  exit 0
fi

if (( FULL )); then
  echo "→ Exporting complete cloud mirror..."
  git archive "$REF" data/wake.sqlite3 state.json events.jsonl head.txt site | tar -x -C "$STAGE"
else
  echo "→ Exporting authoritative cloud record..."
  git archive "$REF" data/wake.sqlite3 head.txt | tar -x -C "$STAGE"
fi

echo "→ Verifying required state..."
test -f "$STAGE/data/wake.sqlite3"
test -f "$STAGE/head.txt"

python3 - "$STAGE/data/wake.sqlite3" <<'PY'
import sqlite3, sys
db = sqlite3.connect(f"file:{sys.argv[1]}?mode=ro", uri=True)
result = db.execute("PRAGMA quick_check").fetchone()[0]
db.close()
if result != "ok":
    raise SystemExit(f"SQLite verification failed: {result}")
print("  SQLite: ok")
PY

echo "→ Replacing local authoritative record..."
mkdir -p "$ROOT/data"
mv "$STAGE/data/wake.sqlite3" "$ROOT/data/wake.sqlite3"
cp "$STAGE/head.txt" "$ROOT/head.txt"

if (( FULL )); then
  echo "→ Replacing derived exports and generated site..."
  rm -rf "$ROOT/site"
  mv "$STAGE/site" "$ROOT/site"
  cp "$STAGE/state.json"   "$ROOT/state.json"
  cp "$STAGE/events.jsonl" "$ROOT/events.jsonl"
fi

# Keep cloud-state root files out of local git status without changing .gitignore.
for f in /state.json /events.jsonl /head.txt; do
    grep -qxF "$f" "$ROOT/.git/info/exclude" 2>/dev/null ||
        echo "$f" >> "$ROOT/.git/info/exclude"
done

echo
if (( FULL )); then
  echo "✓ Full wake-state mirror synced locally"
  echo "  data/wake.sqlite3"
  echo "  site/"
  echo "  state.json"
  echo "  events.jsonl"
  echo "  head.txt"
else
  echo "✓ Authoritative wake-state synced locally"
  echo "  data/wake.sqlite3"
  echo "  head.txt"
  echo "  (derived site/state/events skipped; use --full when needed)"
fi
echo
echo "Cloud head: $remote_head"
