#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="$ROOT/examples/offline-fixture-journal"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

DATA="$WORK/data"
SITE="$WORK/site"

cd "$ROOT"
python3 -m wake --data "$DATA" experiment --cycles 100 --output "$SITE"
python3 -m wake audit --events "$SITE/events.jsonl" --head "$SITE/head.txt"

mkdir -p "$TARGET"
find "$TARGET" -mindepth 1 -maxdepth 1 ! -name README.md -exec rm -rf {} +
cp -a "$SITE"/. "$TARGET"/
cp "$DATA/experiment.json" "$TARGET/experiment.json"

echo "Regenerated offline fixture journal from the current exporter."
echo "Target: $TARGET"
