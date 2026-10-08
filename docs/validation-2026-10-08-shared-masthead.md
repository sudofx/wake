# Shared masthead validation — 2026-10-08

Implementation: local commit `dbac671`. No hosted code, workflows or records were changed.

The masthead now has one geometry owner, `wake/assets/masthead.css`. Export normalizes
headers and relative navigation across full and browser-only artifacts. The shared theme
controller defaults to system preference and persists deliberate choices per origin.
Console navigation remains an unboxed glyph. Runtime status uses a small lamp and
accessible descriptions instead of a text pill. Touch hold previews other controls;
tapping the lamp explains status. Optional live-activity capability cannot erase otherwise
available runtime status. Reading panes remain selectable.

## Evidence

- All 468 Python tests passed, including full/fast export asset resolution, nested reading
  navigation, unchanged authority during export and execution of the production theme
  controller with system changes, manual choice, storage updates and unavailable storage.
- `tests/browser/masthead.cjs` passed in headless Chrome against an independent generated
  fixture. It compares actual geometry and typography across eight pages, both themes
  and widths 1440, 900, 390 and 320. It checks transparent/borderless Console navigation,
  no link underline, theme switch ordering, yellow paused and green running lamps,
  touch descriptions with accessible associations, keyboard activation, theme persistence
  and selection behavior. It waits for each page's initial requests to settle before
  measuring, and fails on browser/script/request errors.
- The installed ARM64 image passed `scripts/test_container.py` with networking disabled
  and a fixture provider. Container recreation retained the exact event prefix and
  continued accepted fixture transitions. Private endpoints remained unavailable.
- The existing `wake` container received a complete snapshot through `standalone.publish`,
  using its own store and atomic publication switch. Its head stayed
  `97c693a44bff572155f929ef7b8fe6912c9199fda249579dc9fc79be1e25b37a`.
  Both new shared assets returned HTTP 200. Chrome verified the actual LAN Console at
  `192.168.1.74:8080`: light theme, compact blocked lamp and touch description.

The local runtime was already blocked by the context ceiling before publication. It
remained blocked afterward. No provider call, research restart, context-budget change,
record transfer or hosted operation was performed by the UI publication. Temporary
container tests used independent volumes and removed only their own resources.

## Reproducing the browser check

Generate a standalone fixture with `Engine.initialize()` and `report.export()` into an
isolated temporary directory. Add `notebooks/chrome-test.html` with `_reading_page()`
and run `_deployment_site(..., standalone=True)` again to normalize the nested page.
Serve that directory with a static HTTP server whose `/runtime.json` contains
`{"state":"paused"}`. Never point this test at a working authority directory or hosted
site. The running-lamp check intercepts that fixture endpoint in the browser only.

Run `node tests/browser/masthead.cjs <fixture-base-URL>` with Playwright installed.
`PLAYWRIGHT_MODULE` can name its package directory; `CHROME_EXECUTABLE` can name an
installed Chrome binary. The script leaves a mobile screenshot in
`/tmp/wake-shared-masthead-mobile.png` for visual inspection. It does not use model APIs.
