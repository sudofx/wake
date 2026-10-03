#!/usr/bin/env python3
"""Build the static Pages shell from the disposable wake-live projection."""

import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

from wake.report import export

LIVE_URL = "https://raw.githubusercontent.com/sudofx/wake/wake-live/live.json"


def main():
    request = urllib.request.Request(
        LIVE_URL,
        headers={"User-Agent": "WAKE-pages/1", "Cache-Control": "no-cache"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.load(response)
    result = export(None, ROOT / "site", browser_only=True, projection=payload)
    print(json.dumps({"status": "published-shell", **result}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
