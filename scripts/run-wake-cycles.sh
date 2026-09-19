#!/usr/bin/env bash
# WAKE✳︎ MAINTAINER NOTE
#
# Operator loop for sequential GitHub wake runs. Stop visibly on failures or quota boundaries so automation never conceals a broken experiment.
#
# Comments document operational intent and failure boundaries so maintenance does not accidentally weaken the experiment.

set -uo pipefail

# Run 1-500 WAKE✳︎ cycles sequentially through GitHub Actions.
# Requires: gh authenticated for sudofx/wake.
#
# Usage:
#   scripts/run-wake-cycles.sh N

readonly REPO="sudofx/wake"
readonly WORKFLOW="wake.yml"
readonly MAX_CYCLES=500
readonly POLL_SECONDS=5
readonly RETRY_SECONDS=15

usage() {
  echo "Usage: $0 N   (N must be an integer from 1 to $MAX_CYCLES)" >&2
  exit 64
}

[[ $# -eq 1 ]] || usage
[[ "$1" =~ ^[0-9]+$ ]] || usage

count=$((10#$1))
(( count >= 1 && count <= MAX_CYCLES )) || usage

command -v gh >/dev/null 2>&1 || {
  echo "Error: GitHub CLI (gh) is not installed or not on PATH." >&2
  exit 69
}

gh auth status >/dev/null 2>&1 || {
  echo "Error: gh is not authenticated. Run: gh auth login" >&2
  exit 77
}

echo "WAKE✳︎: running $count cycle(s) sequentially (hard limit: $MAX_CYCLES)."

for ((i = 1; i <= count; i++)); do
  while true; do
  echo
  echo "[$i/$count] Dispatching WAKE✳︎ cycle..."

  # Retry transient dispatch failures. The batch should stop only when a
  # WAKE✳︎ workflow itself reports a real failure (such as an API limit).
  dispatch_token="batch-$(hostname 2>/dev/null | tr -cd '[:alnum:]._-' | cut -c1-32)-$-$i-$(date -u +%s)-$RANDOM"

  until gh workflow run "$WORKFLOW" --repo "$REPO" --ref master -f "dispatch_token=$dispatch_token"; do
    echo "[$i/$count] Dispatch failed transiently; retrying in $RETRY_SECONDS seconds..." >&2
    sleep "$RETRY_SECONDS"
  done

  run_id=""
  while [[ -z "$run_id" ]]; do
    run_id="$(
      gh run list \
        --repo "$REPO" \
        --workflow "$WORKFLOW" \
        --event workflow_dispatch \
        --branch master \
        --limit 100 \
        --json databaseId,displayTitle \
        --jq ".[] | select(.displayTitle == \"WAKE✳︎ $dispatch_token\") | .databaseId" \
        | head -n 1
    )"

    [[ -n "$run_id" ]] || sleep "$POLL_SECONDS"
  done

  echo "[$i/$count] Watching GitHub run $run_id..."
  while true; do
    status="$(gh run view "$run_id" --repo "$REPO" --json status --jq '.status' 2>/dev/null || true)"
    if [[ -z "$status" ]]; then
      echo "[$i/$count] GitHub connection interrupted; retrying in $RETRY_SECONDS seconds..." >&2
      sleep "$RETRY_SECONDS"
      continue
    fi
    [[ "$status" == "completed" ]] && break
    sleep "$POLL_SECONDS"
  done

  conclusion=""
  while [[ -z "$conclusion" ]]; do
    conclusion="$(gh run view "$run_id" --repo "$REPO" --json conclusion --jq '.conclusion' 2>/dev/null || true)"
    [[ -n "$conclusion" ]] || {
      echo "[$i/$count] GitHub connection interrupted while reading result; retrying in $RETRY_SECONDS seconds..." >&2
      sleep "$RETRY_SECONDS"
    }
  done

  if [[ "$conclusion" == "cancelled" ]]; then
    job_count="$(gh api "repos/$REPO/actions/runs/$run_id/jobs" --jq '.total_count' 2>/dev/null || true)"
    if [[ "$job_count" == "0" ]]; then
      echo "[$i/$count] Run $run_id was cancelled before any job started; retrying this cycle." >&2
      sleep "$RETRY_SECONDS"
      continue
    fi
  fi

  if [[ "$conclusion" != "success" ]]; then
    echo >&2
    echo "WAKE✳︎ stopped at requested cycle $i/$count because run $run_id ended with: $conclusion" >&2
    echo "Completed cycles before stop: $((i - 1))/$count" >&2
    echo "This is a confirmed workflow failure. Check its output; an API/model daily limit is an expected reason to stop." >&2
    exit 1
  fi

  # A quota-exhausted wake is intentionally a successful GitHub workflow so it
  # does not page the operator. Read the published operation receipt and stop
  # this local batch instead of dispatching hundreds of no-op cycles.
  quota_exhausted="$(
    gh api "repos/$REPO/contents/site/operation.json?ref=wake-state" \
      --jq '.content' 2>/dev/null \
      | tr -d '\n' \
      | base64 --decode 2>/dev/null \
      | jq -r 'select(.quota_exhausted == "free_tier_daily") | .quota_exhausted' 2>/dev/null \
      || true
  )"
  if [[ "$quota_exhausted" == "free_tier_daily" ]]; then
    echo
    echo "WAKE✳︎ stopped cleanly at requested cycle $i/$count: all available Gemini free-tier daily quotas are exhausted."
    echo "No remaining cycles will be dispatched. Resume after the provider quota window resets."
    exit 0
  fi

  echo "[$i/$count] Run $run_id completed successfully."
  break
  done
done

echo
echo "WAKE✳︎: all $count requested cycle(s) completed successfully."
