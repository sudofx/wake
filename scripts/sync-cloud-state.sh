#!/usr/bin/env bash
# WAKE✳︎ MAINTAINER NOTE
#
# Synchronizes the authoritative cloud record with the local checkout.
# wake-state contains one durable product: data/wake.sqlite3. Public/site
# projections are disposable views published elsewhere and are not mirrored
# by this script.

set -euo pipefail

if (( $# == 1 )) && [[ "$1" == "--full" ]]; then
  echo "→ --full is retained for compatibility; wake-state is SQLite-only."
elif (( $# != 0 )); then
  echo "Usage: ./scripts/sync-cloud-state.sh [--full]" >&2
  echo "  Sync the authoritative SQLite record from wake-state." >&2
  exit 64
fi

ROOT="$(git rev-parse --show-toplevel)"
REF="origin/wake-state"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cd "$ROOT"

echo "→ Fetching wake-state..."
# Fetch only the durable-state branch tip. Git transfers objects incrementally;
# no tags or unrelated branch history are requested here.
git fetch --no-tags origin +refs/heads/wake-state:refs/remotes/origin/wake-state

# Compare the actual SQLite Git blob rather than a legacy sidecar head.txt.
# If the bytes already match, avoid rewriting the large local database.
remote_blob="$(git rev-parse "$REF:data/wake.sqlite3")"
if [[ -f "$ROOT/data/wake.sqlite3" ]]; then
  local_blob="$(git hash-object "$ROOT/data/wake.sqlite3")"
  if [[ "$local_blob" == "$remote_blob" ]]; then
    echo "✓ Durable cloud state already current; nothing to copy."
    echo "Cloud SQLite blob: $remote_blob"
    exit 0
  fi
fi

echo "→ Exporting authoritative cloud record..."
git archive "$REF" data/wake.sqlite3 | tar -x -C "$STAGE"

echo "→ Verifying required state..."
test -f "$STAGE/data/wake.sqlite3"

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

echo
echo "✓ Authoritative wake-state synced locally"
echo "  data/wake.sqlite3"
echo
echo "Cloud SQLite blob: $remote_blob"
