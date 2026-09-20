#!/usr/bin/env bash
# WAKE✳︎ MAINTAINER NOTE
#
# Create a local-only, immutable analysis snapshot from the durable wake-state
# branch.  The checked-out data/ and site/ directories can be stale or belong
# to an in-progress local investigation, so this script always reads the cloud
# record that the Actions workflow has durably checkpointed.
#
# Snapshots intentionally live under analysis/, which is gitignored: they are
# evidence preserved for a local analytical session, not new application
# source.  A date-plus-accepted-cycle name makes the provenance visible without
# relying on a mutable "latest" directory.

set -euo pipefail

usage() {
  echo "Usage: $0 [YYYY-MM-DD]" >&2
  echo "Fetches wake-state and saves analysis/YYYY-MM-DD-<accepted-cycles>." >&2
  exit 64
}

[[ $# -le 1 ]] || usage
# Permit an explicit date for a retrospective archive, but do not accept a
# free-form path component that could place the snapshot outside analysis/.
snapshot_date="${1:-$(date +%F)}"
[[ "$snapshot_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || usage

root="$(git rev-parse --show-toplevel)"
cd "$root"

command -v python3 >/dev/null 2>&1 || {
  echo "Error: python3 is required to validate the durable record." >&2
  exit 69
}

echo "→ Fetching wake-state..."
# Force-update only the local remote-tracking ref.  This never changes the
# current branch or cloud history; it makes the archive source explicit below.
git fetch origin +refs/heads/wake-state:refs/remotes/origin/wake-state

# Count accepted invocations from the same exact ref that will be archived.
# State version normally equals this count, but the status check is the more
# direct statement of what the directory name represents.
accepted="$(git show origin/wake-state:state.json | python3 -c '
import json, sys
state = json.load(sys.stdin)
print(sum(1 for item in state.get("invocations", {}).values() if item.get("status") == "accepted"))
')"
[[ "$accepted" =~ ^[0-9]+$ ]] || {
  echo "Error: could not determine accepted wake cycles from wake-state." >&2
  exit 65
}

destination="analysis/${snapshot_date}-${accepted}"
if [[ -e "$destination" ]]; then
  # Never merge with or overwrite a prior export: an incomplete or mistaken
  # archive should remain visible rather than silently replacing evidence.
  echo "Error: snapshot already exists: $destination" >&2
  echo "Choose another date argument only when creating a distinct local archive." >&2
  exit 73
fi

mkdir -p analysis
mkdir "$destination"

echo "→ Archiving durable record to $destination..."
# git archive copies the complete branch tree (SQLite database, hash/event
# exports, and published site) without checking it out or changing wake-state.
git archive origin/wake-state | tar -x -C "$destination"

# Validate the copy after extraction.  The accepted-count comparison guards
# against an accidental source/archive mismatch, while SQLite quick_check
# catches a truncated or corrupt database.
# A failed check deliberately leaves the directory intact for human inspection
# rather than deleting potentially useful forensic evidence.
python3 - "$destination/state.json" "$destination/data/wake.sqlite3" "$accepted" <<'PY'
import json
import sqlite3
import sys

state_path, database_path, expected_accepted = sys.argv[1:]
state = json.load(open(state_path))
accepted = sum(1 for item in state.get("invocations", {}).values() if item.get("status") == "accepted")
if accepted != int(expected_accepted):
    raise SystemExit("archive changed while it was being saved; no snapshot was reported")
if sqlite3.connect(database_path).execute("PRAGMA quick_check").fetchone()[0] != "ok":
    raise SystemExit("SQLite integrity check failed")
print(f"✓ Analysis snapshot saved: {state_path.rsplit('/', 1)[0]}")
print(f"  Accepted wake cycles: {accepted}")
print(f"  Durable version: {state.get('version')}")
PY
