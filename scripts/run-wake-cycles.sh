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

  # Capture a timestamp immediately before dispatch, then identify the manual
  # run created by this invocation. Sequential execution avoids ambiguity.
  started_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  if ! gh workflow run "$WORKFLOW" --repo "$REPO" --ref master; then
    echo "[$i/$count] Dispatch failed; stopping." >&2
    exit 1
  fi

  run_id=""
  for _ in {1..24}; do
    run_id="$(
      gh run list         --repo "$REPO"         --workflow "$WORKFLOW"         --event workflow_dispatch         --branch master         --limit 10         --json databaseId,createdAt         --jq ".[] | select(.createdAt >= \"$started_at\") | .databaseId"         | head -n 1
    )"

    [[ -n "$run_id" ]] && break
    sleep "$POLL_SECONDS"
  done

  if [[ -z "$run_id" ]]; then
    echo "[$i/$count] Could not locate the dispatched run; stopping." >&2
    exit 1
  fi

  echo "[$i/$count] Watching GitHub run $run_id..."
  if ! gh run watch "$run_id" --repo "$REPO" --exit-status; then
    echo "[$i/$count] Run $run_id failed; stopping. No further cycles dispatched." >&2
    gh run view "$run_id" --repo "$REPO" --web 2>/dev/null || true
    exit 1
  fi

  echo "[$i/$count] Run $run_id completed successfully."
done

echo
echo "WAKE✳︎: all $count requested cycle(s) completed successfully."
