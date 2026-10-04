# WAKE✳︎ implementation guidance

WAKE✳︎ is infrastructure for durable, accountable work across interchangeable intelligences. In this repository, that infrastructure is currently realized as a WAKE research application running on the sudofx kernel; it must not grow a competing authority engine.

## Current authority model

The live hosted record is `data/sudofx.sqlite` on `wake-state`.

The legacy `data/wake.sqlite3` chain is migration evidence only. It may be verified, imported, archived, and used by offline compatibility tests, but new operational truth must not be split between the legacy store and sudofx.

Principle:

> one authoritative database → everything else is a view, query, migration source, or export.

## Domain boundary

WAKE-specific concepts belong above the sudofx kernel:

- research topics and seed questions
- research projects and notebooks
- evidence qualification and publication policy
- Bob
- Attention
- inquiry-drive experiments
- acquisition/reframe rules
- scientific-source qualification
- experimental regimes and Time Dilation

Do not move these concepts into generic sudofx governance merely to simplify WAKE code.

### WAKE✳︎ / Bob presentation boundary

The current WAKE✳︎ research application owns the journal, projects, notebooks, evidence, decisions,
commitments, technical record, research progress accounting and institutional voice. These are application
concerns layered on WAKE✳︎'s durable-work infrastructure, not the identity of the kernel itself. Institutional
first-person grammar does not imply a person, persona, identity, consciousness or subjective experience.

Bob is confined to Bob's Blog as a reader-facing translation persona. Bob may summarize and simplify already
durable WAKE✳︎ work, but must never write the journal, gate an accepted research transition, move Attention,
count as research progress, fulfill commitments, alter evidence, or steer project selection. A Bob draft may be
withheld without rejecting otherwise valid research. Keep Bob's Summary respectful, especially simple and
plain-language, with no child-oriented label.


`wake/sudofx_application.py` is the application contract bridge.
`wake/sudofx_store.py` is the transitional Store interface backed by sudofx authority.
`wake/application_policy.py` owns WAKE domain governance.
`wake/event_format.py` owns stable WAKE event identity bytes and hashes.
`wake/domain_events.py` owns deterministic WAKE event reduction without storage authority.
`wake/store.py` is legacy SQLite compatibility only; normal runtime/domain code must not import it.

## Migration discipline

Every Phase E change must preserve replayable meaning.

When replacing a legacy path:

1. verify the legacy event/state source before importing it;
2. preserve the exact migration provenance and historical head;
3. route post-migration mutations through sudofx application actions;
4. keep legacy code read-only where it remains necessary for migration verification;
5. prove behavioral or replay equivalence before deleting compatibility machinery;
6. never maintain two writable authoritative stores.

A migration convenience is not sufficient reason to weaken governance, provenance, or failure visibility.

## Runtime branches

- `master` — development source and documentation
- `wake-runtime` — explicitly promoted live executable
- `wake-state` — authoritative sudofx SQLite checkpoint
- `wake-live` — disposable public projection

Research must be stopped before promoting new runtime code.

GitHub Actions is execution infrastructure, not application authority.

## Provider boundary

Providers receive bounded context and return untrusted proposals.

Provider failures, quota pressure, deferrals, malformed output, and rejections must remain visible and must not fabricate accepted research.

Generic provider-attempt lifecycle, context-delivery evidence, interruption recovery, durability-barrier-before-effect ordering, and provider-neutral invocation accounting belong to sudofx runtime primitives. WAKE may classify its provider-specific exceptions and apply Gemini/fallback quota policy, but it must not reimplement the generic execution boundary in parallel.

No model/provider receives arbitrary filesystem, database, governance, or policy authority through WAKE.

## Presentation boundary

GitHub Pages, Bob, MAP, metrics, journal views, workflow summaries, and `wake-live` are derived presentation.

Never read them back as operational truth.

Public labels should use configured human-facing topic labels rather than leaking internal machine IDs where a label exists.

## Documentation synchronization

When code materially changes migration status, authority, operator workflows, context delivery, provider accounting, or research governance, update the canonical prose in the same work:

- `README.md` — current repository-level picture
- `docs/architecture.md` — authority and trust boundaries
- `docs/cloud.md` — current hosted operating procedure
- `docs/experiment.md` — experimental interpretation
- `docs/retrieval.md` — progressive abstraction/retrieval behavior

`docs/validation.md` is intentionally historical. Do not silently turn it into a rolling certification; add a new dated validation record if a new formal validation snapshot is needed.

When prose and implementation disagree, current code/tests are evidence of behavior, but the documentation mismatch is a defect to fix rather than a permanent disclaimer.


## Engine authority injection

Engine construction must name its authority.

Operational code injects the store returned by `open_authoritative_store(...)`.
Legacy compatibility tests may pass `store_factory=Store` explicitly. `Engine` itself must not import or construct the legacy Store.
Do not restore an implicit `Store(directory)` fallback: forgetting store injection must fail rather than silently creating a second `wake.sqlite3`.

Fresh initialization is native sudofx initialization. The legacy Store is opened only when an actual pre-migration `wake.sqlite3` exists and must be verified/imported.
