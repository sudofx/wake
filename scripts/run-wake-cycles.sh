#!/usr/bin/env bash
set -uo pipefail

# Run 1-100 WAKE✳︎ cycles sequentially through GitHub Actions.
# Requires: gh authenticated for sudofx/wake.
#
# Usage:
#   scripts/run-wake-cycles.sh N

readonly REPO="sudofx/wake"
readonly WORKFLOW="wake.yml"
readonly MAX_CYCLES=100
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
  echo
  echo "[$i/$count] Dispatching WAKE✳︎ cycle..."

  # Retry transient dispatch failures. The batch should stop only when a
  # WAKE✳︎ workflow itself reports a real failure (such as an API limit).
  started_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  until gh workflow run "$WORKFLOW" --repo "$REPO" --ref master; do
    echo "[$i/$count] Dispatch failed transiently; retrying in $RETRY_SECONDS seconds..." >&2
    sleep "$RETRY_SECONDS"
    started_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  done

  run_id=""
  while [[ -z "$run_id" ]]; do
    run_id="$(
      gh run list         --repo "$REPO"         --workflow "$WORKFLOW"         --event workflow_dispatch         --branch master         --limit 10         --json databaseId,createdAt         --jq ".[] | select(.createdAt >= \"$started_at\") | .databaseId"         | head -n 1
    )"

    [[ -n "$run_id" ]] || sleep "$POLL_SECONDS"
  done

  echo "[$i/$count] Watching GitHub run $run_id..."
  if ! gh run watch "$run_id" --repo "$REPO" --exit-status; then
    echo >&2
    echo "WAKE✳︎ stopped at requested cycle $i/$count because run $run_id failed." >&2
    echo "Completed cycles before stop: $((i - 1))/$count" >&2
    echo "Check this workflow output; an API/model daily limit is an expected reason to stop." >&2
    exit 1
  fi

  echo "[$i/$count] Run $run_id completed successfully."
done

echo
echo "WAKE✳︎: all $count requested cycle(s) completed successfully."
