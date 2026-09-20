#!/usr/bin/env bash
# WAKE✳︎ operator loop: continue sequentially until a durable quota boundary.
set -uo pipefail

# Usage: scripts/run-wake-cycles.sh
readonly REPO="sudofx/wake"
readonly WORKFLOW="wake.yml"
readonly POLL_SECONDS=5
readonly RETRY_SECONDS=15
readonly TRANSIENT_RETRY_SECONDS=300
readonly DISPATCH_TIMEOUT_SECONDS=1800
readonly RUN_DISCOVERY_TIMEOUT_SECONDS=600
readonly RUN_COMPLETION_TIMEOUT_SECONDS=2700
readonly RECEIPT_TIMEOUT_SECONDS=600

usage() {
  echo "Usage: $0" >&2
  echo "Runs sequential WAKE✳︎ cycles until all configured Gemini daily quotas are exhausted." >&2
  exit 64
}

[[ $# -eq 0 ]] || usage
command -v gh >/dev/null 2>&1 || { echo "Error: GitHub CLI (gh) is not installed or not on PATH." >&2; exit 69; }
gh auth status >/dev/null 2>&1 || { echo "Error: gh is not authenticated. Run: gh auth login" >&2; exit 77; }

read_operation() {
  gh api "repos/$REPO/contents/site/operation.json?ref=wake-state" --jq '.content' 2>/dev/null \
    | tr -d '\n' | base64 --decode 2>/dev/null || true
}

echo "WAKE✳︎: running sequentially until all available Gemini daily quotas are exhausted."
echo "A no-progress timeout stops the runner visibly instead of leaving it stuck indefinitely."

i=0
accepted=0
rejected=0
deferred=0
waiting=0

while true; do
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
    sleep "$TRANSIENT_RETRY_SECONDS"
  fi
done
