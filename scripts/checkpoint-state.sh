#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

BRANCH="wake-state"
TMP="$(mktemp -d)"
trap 'git worktree remove --force "$TMP" >/dev/null 2>&1 || true; rm -rf "$TMP"' EXIT

test -f data/wake.sqlite3 || {
    echo "ERROR: no local data/wake.sqlite3" >&2
    exit 1
}

# Export projections from the actual local database first.
python3 -m wake export --output site >/dev/null

LOCAL_HEAD="$(python3 -m wake status | python3 -c 'import json,sys; print(json.load(sys.stdin)["head"])')"

git fetch origin "+refs/heads/$BRANCH:refs/remotes/origin/$BRANCH"
START_REMOTE="$(git rev-parse "origin/$BRANCH")"
REMOTE_HEAD="$(git show "origin/$BRANCH:head.txt" | tr -d '[:space:]')"

[[ "$LOCAL_HEAD" != "$REMOTE_HEAD" ]] || {
    echo "✓ Local durable state already matches wake-state"
    exit 0
}

# The current remote durable head must occur in the locally exported history.
python3 - "$REMOTE_HEAD" site/events.jsonl <<'PY'
import json, sys

remote_head, path = sys.argv[1:]
found = False

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        if json.loads(line)["hash"] == remote_head:
            found = True
            break

if not found:
    raise SystemExit(
        "ERROR: remote durable head is not present in local history; refusing checkpoint"
    )
PY

echo "→ Checkpointing local durable state..."

git worktree add --detach "$TMP" "origin/$BRANCH" >/dev/null

rm -rf "$TMP/data" "$TMP/site"
cp -R data "$TMP/data"
cp -R site "$TMP/site"
cp site/state.json "$TMP/state.json"
cp site/events.jsonl "$TMP/events.jsonl"
cp site/head.txt "$TMP/head.txt"

git -C "$TMP" add --force data/wake.sqlite3 site state.json events.jsonl head.txt
git -C "$TMP" -c user.name=wake-human -c user.email=wake-human@users.noreply.github.com \
    commit -m "Record human durable WAKE state" >/dev/null

# Refuse the push if wake-state moved while this checkpoint was being built.
git fetch origin "+refs/heads/$BRANCH:refs/remotes/origin/$BRANCH" >/dev/null
NOW_REMOTE="$(git rev-parse "origin/$BRANCH")"

if [[ "$NOW_REMOTE" != "$START_REMOTE" ]]; then
    echo "ERROR: wake-state changed during checkpoint; refusing push." >&2
    echo "  started: $START_REMOTE" >&2
    echo "  now:     $NOW_REMOTE" >&2
    exit 1
fi

git -C "$TMP" push origin "HEAD:refs/heads/$BRANCH"

echo "✓ Durable state checkpointed"
echo "  head: $LOCAL_HEAD"
