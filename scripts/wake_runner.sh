#!/usr/bin/env bash
# Compatibility entry point matching the documented .sh spelling.
exec "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)/wake_runner" "$@"
