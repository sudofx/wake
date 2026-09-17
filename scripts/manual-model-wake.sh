#!/usr/bin/env bash
set -euo pipefail

# WAKE✳︎ manual-model cycle
#
# Usage:
#   ./scripts/manual-model-wake.sh
#   ./scripts/manual-model-wake.sh "Claude / human-attested"
#
# Requires:
#   git
#   python3
#   gh (authenticated to GitHub)
#
# Workflow:
#   remote wake-state
#       ↓
#   local data/ + site/
#       ↓
#   WAKE prepare
#       ↓
#   [PAUSE FOR HUMAN / EXTERNAL MODEL]
#       ↓
#   response.json
#       ↓
#   WAKE complete
#       ↓
#   export
#       ↓
#   wake-state
#       ↓
#   GitHub Pages publish-only
#       ↓
#   final local resync

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

MODEL="${1:-ChatGPT / human-attested}"
STATE_BRANCH="wake-state"
REQUEST="$ROOT/request.json"
RESPONSE="$ROOT/response.json"

TMP_WORKTREE=""
START_REMOTE=""

cleanup() {
    rm -f "$REQUEST" "$RESPONSE"

    if [[ -n "$TMP_WORKTREE" && -d "$TMP_WORKTREE" ]]; then
        git worktree remove --force "$TMP_WORKTREE" >/dev/null 2>&1 || true
    fi
}

trap cleanup EXIT INT TERM

echo
echo "WAKE✳︎ manual-model cycle"
echo "Model: $MODEL"
echo

# ------------------------------------------------------------
# 1. Synchronize durable cloud state → local
# ------------------------------------------------------------

echo "→ Fetching $STATE_BRANCH..."
git fetch origin "+refs/heads/$STATE_BRANCH:refs/remotes/origin/$STATE_BRANCH"

START_REMOTE="$(git rev-parse "origin/$STATE_BRANCH")"

echo "→ Checking local durable state..."

REMOTE_HEAD="$(git show "origin/$STATE_BRANCH:head.txt" | tr -d '[:space:]')"
LOCAL_HEAD=""

if [[ -f data/wake.sqlite3 ]]; then
    LOCAL_HEAD="$(python3 -m wake status | python3 -c 'import json,sys; print(json.load(sys.stdin)["head"])')"
fi

if [[ -n "$LOCAL_HEAD" && "$LOCAL_HEAD" != "$REMOTE_HEAD" ]]; then
    echo "ERROR: Local WAKE durable state differs from origin/$STATE_BRANCH." >&2
    echo "  local:  $LOCAL_HEAD" >&2
    echo "  remote: $REMOTE_HEAD" >&2
    echo "Run ./scripts/checkpoint-state.sh or ./scripts/sync-cloud-state.sh deliberately." >&2
    exit 1
fi

echo "→ Synchronizing data/ and site/..."

rm -rf data site

git archive "origin/$STATE_BRANCH" data site | tar -x

test -f data/wake.sqlite3 || {
    echo "ERROR: wake-state contains no data/wake.sqlite3" >&2
    exit 1
}

echo "✓ Local durable state synchronized"

# ------------------------------------------------------------
# 2. Prepare manual invocation
# ------------------------------------------------------------

echo
echo "→ Preparing manual invocation..."

PREPARE_OUTPUT="$(
    python3 -m wake prepare \
        --model "$MODEL" \
        --output "$REQUEST"
)"

echo "$PREPARE_OUTPUT"

INVOCATION_ID="$(
    python3 -c '
import json, sys
print(json.load(sys.stdin)["id"])
' <<< "$PREPARE_OUTPUT"
)"

test -n "$INVOCATION_ID" || {
    echo "ERROR: Could not determine invocation ID" >&2
    exit 1
}

# ------------------------------------------------------------
# 3. HUMAN HANDOFF
# ------------------------------------------------------------

echo
echo "============================================================"
echo "PAUSED — HUMAN MODEL HANDOFF"
echo "============================================================"
echo
echo "Invocation:"
echo "  $INVOCATION_ID"
echo
echo "1. Open a NEW / TEMP / INCOGNITO model conversation."
echo
echo "2. Paste the complete contents of:"
echo
echo "     $REQUEST"
echo
echo "3. Save the model's UNEDITED JSON response as:"
echo
echo "     $RESPONSE"
echo
echo "4. Return here and press ENTER."
echo
echo "============================================================"
echo

read -r -p "Press ENTER after response.json exists... "

if [[ ! -f "$RESPONSE" ]]; then
    echo
    echo "ERROR: response.json does not exist:"
    echo "  $RESPONSE"
    exit 1
fi

python3 -m json.tool "$RESPONSE" >/dev/null || {
    echo "ERROR: response.json is not valid JSON" >&2
    exit 1
}

# ------------------------------------------------------------
# 4. Complete invocation
# ------------------------------------------------------------

echo
echo "→ Completing $INVOCATION_ID..."

python3 -m wake complete \
    --id "$INVOCATION_ID" \
    --file "$RESPONSE"

# ------------------------------------------------------------
# 5. Export updated site
# ------------------------------------------------------------

echo
echo "→ Exporting updated WAKE site..."

python3 -m wake export --output site

# ------------------------------------------------------------
# 6. Protect against concurrent cloud changes
# ------------------------------------------------------------

echo
echo "→ Checking remote state has not changed..."

git fetch origin "+refs/heads/$STATE_BRANCH:refs/remotes/origin/$STATE_BRANCH"

CURRENT_REMOTE="$(git rev-parse "origin/$STATE_BRANCH")"

if [[ "$CURRENT_REMOTE" != "$START_REMOTE" ]]; then
    echo
    echo "ERROR: wake-state changed while the manual model was running."
    echo
    echo "Started from:"
    echo "  $START_REMOTE"
    echo
    echo "Remote is now:"
    echo "  $CURRENT_REMOTE"
    echo
    echo "Nothing was pushed."
    echo "Re-sync and repeat the manual cycle."
    exit 1
fi

# ------------------------------------------------------------
# 7. Publish durable state without touching master
# ------------------------------------------------------------

echo
echo "→ Publishing durable state..."

TMP_WORKTREE="$(mktemp -d "${TMPDIR:-/tmp}/wake-manual.XXXXXX")"

git worktree add \
    --detach \
    "$TMP_WORKTREE" \
    "origin/$STATE_BRANCH" >/dev/null

mkdir -p "$TMP_WORKTREE/data"

cp data/wake.sqlite3 \
   "$TMP_WORKTREE/data/wake.sqlite3"

cp site/events.jsonl \
   site/state.json \
   site/head.txt \
   "$TMP_WORKTREE/"

rm -rf "$TMP_WORKTREE/site"
cp -R site "$TMP_WORKTREE/site"

git -C "$TMP_WORKTREE" add \
    -f \
    data/wake.sqlite3 \
    events.jsonl \
    state.json \
    head.txt \
    site

if git -C "$TMP_WORKTREE" diff --cached --quiet; then
    echo "ERROR: manual cycle produced no durable changes" >&2
    exit 1
fi

git -C "$TMP_WORKTREE" \
    -c user.name=wake-bot \
    -c user.email=wake-bot@users.noreply.github.com \
    commit \
    -m "Record manual $MODEL wake cycle"

# Lease prevents overwriting a newer wake-state if it changed
# between the second fetch and this push.

git -C "$TMP_WORKTREE" push \
    --force-with-lease="refs/heads/$STATE_BRANCH:$START_REMOTE" \
    origin \
    "HEAD:refs/heads/$STATE_BRANCH"

PUBLISHED_SHA="$(git -C "$TMP_WORKTREE" rev-parse HEAD)"

echo "✓ Durable state published: ${PUBLISHED_SHA:0:7}"

# Worktree is no longer needed.
git worktree remove --force "$TMP_WORKTREE"
TMP_WORKTREE=""

# ------------------------------------------------------------
# 8. Trigger GitHub Pages rebuild WITHOUT another Gemini call
# ------------------------------------------------------------

echo
echo "→ Triggering publish-only GitHub workflow..."

gh workflow run wake.yml \
    --ref master \
    -f publish_only=true \
    -f reset=false

echo "✓ Publish workflow dispatched"

# ------------------------------------------------------------
# 9. Fully re-sync from authoritative remote state
# ------------------------------------------------------------

echo
echo "→ Re-synchronizing local durable state..."

git fetch origin "+refs/heads/$STATE_BRANCH:refs/remotes/origin/$STATE_BRANCH"

rm -rf data site

git archive "origin/$STATE_BRANCH" data site | tar -x

echo "✓ Local data/ and site/ match origin/$STATE_BRANCH"

# ------------------------------------------------------------
# 10. Finish
# ------------------------------------------------------------

echo
echo "============================================================"
echo "WAKE✳︎ manual cycle complete"
echo
echo "Invocation: $INVOCATION_ID"
echo "Model:      $MODEL"
echo "State:      ${PUBLISHED_SHA:0:12}"
echo
echo "GitHub Pages publish has been dispatched."
echo "============================================================"
echo
