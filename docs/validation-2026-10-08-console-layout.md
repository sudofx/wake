# Console layout and provider overlay validation — 2026-10-08

Scope: local presentation changes only. No hosted publication, runtime promotion,
operator restart, provider calls or record import was performed.

## Verified behavior

- Panel #001 fills the workspace row, overriding a saved narrow size. The other
  17 numbered panels start at minimum width when no saved layout exists.
- Panel #002 preserves its dragged order and chosen width after refresh.
- Reset restores the default order and widths in place without page navigation.
- Toolbar actions sit below headings and align left at 1440, 900 and 390 pixels.
- Provider request and returned-proposal phases have distinct visual indications.
  Reduced motion remains static; disconnected activity clears the live overlay.

## Evidence

The Python suite passed all 468 tests. The browser regression in
`tests/browser/console-layout.cjs` passed against a generated offline fixture,
including actual pointer dragging, refresh, reset and runtime phase transitions.
Provider phases were simulated at the read-only HTTP boundary; this proves UI
behavior, not observation of a real model invocation.

The final installed image `wake-layout-candidate:local` passed the native
`linux/arm64` container acceptance test with networking disabled. Recreating the
temporary installation retained the exact audit prefix and advanced fixture
cycles from 2 to 5. Its authority verified before and after recreation.

The existing operator installation was refreshed through canonical atomic
standalone publication. Its record head stayed
`97c693a44bff572155f929ef7b8fe6912c9199fda249579dc9fc79be1e25b37a`.
A browser check of the actual LAN Console confirmed #001 full-row and #002
minimum-width geometry. Research was already blocked by its context ceiling;
that state was preserved. The existing process lacks the optional live activity
capability, so live provider animation there requires a future updated runtime.

The browser check used a fresh browser context. Existing browser layout
preferences remain valid; use Reset to apply the new minimum-width defaults.
