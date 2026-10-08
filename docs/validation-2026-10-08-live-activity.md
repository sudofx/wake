# Live Console activity validation — 2026-10-08

Local candidate only. No push, hosted operation or external WAKE provider call.
The operator's running container and volume were not replaced or used as fixtures.

## Verified behavior

- Engine observation reports actual public stages and the coordinate delivered
  with the proposal request. It clears activity in `finally`; failures in the
  display observer do not change governance or accepted state.
- The read-only, uncached runtime endpoint advertises live activity explicitly,
  with a runtime identity, sampled time and successful-publication generation.
- Console polls that optional local channel every three seconds and refreshes
  snapshots after publication changes, including outcomes without a version bump.
- The production cube renderer overlays a green live outline independently of
  score and selected cell. Reduced motion renders a static mark. Hidden/collapsed
  views stop live animation; connection failure or expired samples clears it.
- Hosted projections preserve dated pending invocation/cell identity with
  `active: false`. Hosted/missing deployment identities do not poll runtime or
  display the live capability legend.

Eight focused tests execute actual engine, HTTP handler, exporter and browser
code. They protect exact coordinate assignment, failure cleanup, observer isolation,
optional capability validation, same-origin transport, sample expiry, independent
selection/score rendering, reduced motion and complete exported script assets.
The full repository suite passed **466 tests**.

## Actual packaged and browser paths

Candidate image manifest:
`sha256:92aac330f758d931320d782830bb9934adfbe766c29e3d249f9a04096248f18c`.
Both ARM64 (native) and AMD64 (emulated) passed interruption/recreation and exact
history-prefix tests with networking disabled. Those tests ran from `/tmp`,
importing the installed package instead of the source tree in `/app`.

This uncovered and fixed omitted nested wheel assets. Icons, backgrounds and
previews now ship with the installed package. Console export also explicitly
copies the new activity script. These are distinct package/export custody checks.

A separate disposable container used an installed-package fixture delayed before
its response. The browser showed live cell #003 while recorded coverage remained
2/343, with the independent inspection selection preserved. On the final candidate,
completion showed `RUNTIME IDLE`, updated recorded coverage and no live outline.
A later active #005 probe was interrupted by removing only that disposable test
container; the browser changed to execution status unknown and hid the live outline,
label and capability legend. Light-theme rendering and lack of horizontal overflow
were inspected. Fixture containers and test volumes were removed afterward.

## Limits

This is sampled inspection, not model cognition or a guarantee that short phases
will be visible between polls. Live indications never imply accepted research.
GitHub workflows were not run and the hosted Console was not deployed. The current
operator container needs updated runtime execution to expose this capability;
new assets alone cannot add telemetry to an already imported Python process.
