#!/usr/bin/env bash
# WAKE✳︎ operator loop: refresh code/state, then continue sequentially until a durable quota boundary.
set -uo pipefail

# Usage: scripts/run-wake-cycles.sh [N]
readonly REPO="sudofx/wake"
readonly WORKFLOW="wake.yml"
readonly POLL_SECONDS=5
readonly RETRY_SECONDS=15
readonly TRANSIENT_RETRY_SECONDS=300
readonly DISPATCH_TIMEOUT_SECONDS=1800
readonly RUN_DISCOVERY_TIMEOUT_SECONDS=600
readonly RUN_COMPLETION_TIMEOUT_SECONDS=2700
readonly RECEIPT_TIMEOUT_SECONDS=600

prepare_workspace() {
  local root branch changes

  root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "Error: run-wake-cycles.sh must run from inside a Git checkout." >&2
    exit 69
  }
  cd "$root"

  branch="$(git branch --show-current)"
  if [[ "$branch" != "master" ]]; then
    echo "Error: refusing to update from branch '$branch'; switch to master first." >&2
    exit 65
  fi

  # A fast-forward-only pull cannot create a merge commit or conflict. Refuse
  # any tracked or untracked work first so neither the update nor state sync can
  # overwrite an operator's local files.
  changes="$(git status --porcelain --untracked-files=all)"
  if [[ -n "$changes" ]]; then
    echo "Error: refusing to update a dirty checkout. Commit, stash, or remove local changes first." >&2
    echo "$changes" >&2
    exit 65
  fi

  echo "→ Updating WAKE✳︎ code (fast-forward only)..."
  git pull --ff-only origin master || {
    echo "Error: code update did not fast-forward cleanly; no wake was started." >&2
    exit 1
  }

  echo "→ Syncing durable cloud state..."
  "$root/scripts/sync-cloud-state.sh" || {
    echo "Error: cloud-state sync failed; no wake was started." >&2
    exit 1
  }
}

usage() {
  echo "Usage: $0 [N]" >&2
  echo "Refreshes master and syncs durable cloud state before starting any wake." >&2
  echo "Without N, runs until all configured Gemini daily quotas are exhausted." >&2
  echo "With N, runs exactly N sequential wakes unless a quota or failure stops it first." >&2
  exit 64
}

[[ $# -le 1 ]] || usage
max_wakes=0
if [[ $# -eq 1 ]]; then
  [[ "$1" =~ ^[0-9]+$ ]] || usage
  max_wakes=$((10#$1))
  (( max_wakes >= 1 )) || usage
fi
prepare_workspace
command -v gh >/dev/null 2>&1 || { echo "Error: GitHub CLI (gh) is not installed or not on PATH." >&2; exit 69; }
gh auth status >/dev/null 2>&1 || { echo "Error: gh is not authenticated. Run: gh auth login" >&2; exit 77; }

read_operation() {
  gh api "repos/$REPO/contents/site/operation.json?ref=wake-state" --jq '.content' 2>/dev/null \
    | tr -d '\n' | base64 --decode 2>/dev/null || true
}

if (( max_wakes > 0 )); then
  echo "WAKE✳︎: running $max_wakes sequential wake(s), unless a quota or failure stops earlier."
else
  echo "WAKE✳︎: running sequentially until all available Gemini daily quotas are exhausted."
fi
echo "A no-progress timeout stops the runner visibly instead of leaving it stuck indefinitely."

i=0
accepted=0
rejected=0
deferred=0
waiting=0

while true; do
  if (( max_wakes > 0 && i >= max_wakes )); then
    echo
    echo "WAKE✳︎: completed $max_wakes requested wake(s)."
    echo "Accepted: $accepted; rejected: $rejected; deferred: $deferred; waiting: $waiting."
    exit 0
  fi
  i=$((i + 1))
  echo
  echo "[wake $i] Dispatching WAKE✳︎ cycle..."
  dispatch_token="batch-$(hostname 2>/dev/null | tr -cd '[:alnum:]._-' | cut -c1-32)-$$-$i-$(date -u +%s)-$RANDOM"

  dispatch_started=$SECONDS
  while ! gh workflow run "$WORKFLOW" --repo "$REPO" --ref master -f "dispatch_token=$dispatch_token"; do
    if (( SECONDS - dispatch_started >= DISPATCH_TIMEOUT_SECONDS )); then
      echo "WAKE✳︎ stopped: could not dispatch wake $i for 30 minutes." >&2
      exit 1
    fi
    echo "[wake $i] Dispatch failed transiently; retrying in $RETRY_SECONDS seconds..." >&2
    sleep "$RETRY_SECONDS"
  done

  run_id=""
  discovery_started=$SECONDS
  while [[ -z "$run_id" ]]; do
    run_id="$(gh run list --repo "$REPO" --workflow "$WORKFLOW" --event workflow_dispatch --branch master --limit 100 --json databaseId,displayTitle --jq ".[] | select(.displayTitle == \"WAKE✳︎ $dispatch_token\") | .databaseId" | head -n 1 || true)"
    if [[ -z "$run_id" ]]; then
      if (( SECONDS - discovery_started >= RUN_DISCOVERY_TIMEOUT_SECONDS )); then
        echo "WAKE✳︎ stopped: GitHub did not expose the dispatched wake $i within 10 minutes." >&2
        exit 1
      fi
      sleep "$POLL_SECONDS"
    fi
  done

  echo "[wake $i] Watching GitHub run $run_id..."
  completion_started=$SECONDS
  while true; do
    status="$(gh run view "$run_id" --repo "$REPO" --json status --jq '.status' 2>/dev/null || true)"
    if [[ -z "$status" ]]; then
      if (( SECONDS - completion_started >= RUN_COMPLETION_TIMEOUT_SECONDS )); then
        echo "WAKE✳︎ stopped: GitHub remained unreachable while watching run $run_id for 45 minutes." >&2
        exit 1
      fi
      echo "[wake $i] GitHub connection interrupted; retrying in $RETRY_SECONDS seconds..." >&2
      sleep "$RETRY_SECONDS"
      continue
    fi
    [[ "$status" == "completed" ]] && break
    if (( SECONDS - completion_started >= RUN_COMPLETION_TIMEOUT_SECONDS )); then
      echo "WAKE✳︎ stopped: run $run_id did not complete within 45 minutes." >&2
      exit 1
    fi
    sleep "$POLL_SECONDS"
  done

  conclusion=""
  while [[ -z "$conclusion" ]]; do
    conclusion="$(gh run view "$run_id" --repo "$REPO" --json conclusion --jq '.conclusion' 2>/dev/null || true)"
    if [[ -z "$conclusion" ]]; then
      if (( SECONDS - completion_started >= RUN_COMPLETION_TIMEOUT_SECONDS )); then
        echo "WAKE✳︎ stopped: GitHub did not return a conclusion for run $run_id." >&2
        exit 1
      fi
      sleep "$RETRY_SECONDS"
    fi
  done

  if [[ "$conclusion" == "cancelled" ]]; then
    job_count="$(gh api "repos/$REPO/actions/runs/$run_id/jobs" --jq '.total_count' 2>/dev/null || true)"
    if [[ "$job_count" == "0" ]]; then
      echo "[wake $i] Run was cancelled before any job started; retrying this wake." >&2
      i=$((i - 1))
      sleep "$RETRY_SECONDS"
      continue
    fi
  fi

  if [[ "$conclusion" != "success" ]]; then
    pause_reason="$(read_operation | jq -r 'select(.status == "paused") | .reason' 2>/dev/null || true)"
    if [[ "$pause_reason" == "Context ceiling reached; human review required, no model call made" ]]; then
      echo "WAKE✳︎ stopped cleanly after $i dispatched wakes: $pause_reason"
      exit 0
    fi
    echo "WAKE✳︎ stopped after $i dispatched wakes because run $run_id ended with: $conclusion" >&2
    echo "This is a confirmed workflow failure. Check its output before resuming." >&2
    exit 1
  fi

  receipt_started=$SECONDS
  operation=""
  operation_status=""
  while [[ -z "$operation_status" ]]; do
    operation="$(read_operation)"
    operation_status="$(jq -r '.status // empty' <<<"$operation" 2>/dev/null || true)"
    if [[ -z "$operation_status" ]]; then
      if (( SECONDS - receipt_started >= RECEIPT_TIMEOUT_SECONDS )); then
        echo "WAKE✳︎ stopped: the durable operation receipt was unavailable for 10 minutes after run $run_id." >&2
        exit 1
      fi
      sleep "$POLL_SECONDS"
    fi
  done

  quota_exhausted="$(jq -r '.quota_exhausted // empty' <<<"$operation" 2>/dev/null || true)"
  if [[ "$quota_exhausted" == "free_tier_daily" || "$quota_exhausted" == "configured_daily_limit" ]]; then
    echo
    echo "WAKE✳︎ stopped cleanly after $i dispatched wakes: all available Gemini daily quotas are exhausted."
    echo "Accepted: $accepted; rejected: $rejected; deferred: $deferred; waiting: $waiting."
    echo "Resume after the provider quota window resets."
    exit 0
  fi

  case "$operation_status" in
    accepted) accepted=$((accepted + 1)) ;;
    rejected) rejected=$((rejected + 1)) ;;
    deferred) deferred=$((deferred + 1)) ;;
    waiting) waiting=$((waiting + 1)) ;;
  esac
  echo "[wake $i] ${operation_status} (accepted: $accepted; rejected: $rejected; deferred: $deferred; waiting: $waiting)."

  if [[ "$operation_status" == "deferred" ]] && jq -e '.reason | startswith("Gemini temporarily unavailable")' >/dev/null 2>&1 <<<"$operation"; then
    echo "[wake $i] Temporary provider outage; waiting five minutes before retrying."
    # A transient outage produced no research result. Do not let it consume
    # one of the operator-requested cycles before the next dispatch.
    i=$((i - 1))
    sleep "$TRANSIENT_RETRY_SECONDS"
  fi
done
