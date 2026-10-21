# WAKE✳︎ implementation guidance

WAKE✳︎ is infrastructure for durable, accountable work across interchangeable intelligences. In this repository, that infrastructure is currently realized as a standalone WAKE research application running on its owned kernel in `wake/kernel/`; it must not grow a competing authority engine.

## Current authority model

Each container node owns `/data/nodes/ID/record/wake.sqlite`. GitHub Pages is a
read-only public mirror of exports from those records.

The legacy `data/wake.sqlite3` chain is migration evidence only. It may be verified, imported, archived, and used by offline compatibility tests, but new operational truth must not be split between the legacy store and wake.

Principle:

> one authoritative database → everything else is a view, query, migration source, or export.

## Domain boundary

WAKE-specific concepts belong above the WAKE kernel:

- research topics and seed questions
- research projects and notebooks
- evidence qualification and publication policy
- Bob
- Attention
- inquiry-drive experiments
- acquisition/reframe rules
- scientific-source qualification
- experimental regimes and Time Dilation

Do not move these concepts into generic wake governance merely to simplify WAKE code.

### WAKE✳︎ / Bob presentation boundary

The current WAKE✳︎ research application owns the journal, projects, notebooks, evidence, decisions,
commitments, technical record, research progress accounting and institutional voice. These are application
concerns layered on WAKE✳︎'s durable-work infrastructure, not the identity of the kernel itself. Institutional
first-person grammar does not imply a person, persona, identity, consciousness or subjective experience.

Bob's public voice is confined to Bob's Blog as a reader-facing translation persona. Bob may summarize and simplify already
durable WAKE✳︎ work, but must never write the journal, gate an accepted research transition, move Attention,
count as research progress, fulfill commitments, alter evidence, or steer project selection. A Bob draft may be
withheld without rejecting otherwise valid research. Keep Bob's Summary respectful, especially simple and
plain-language, with no child-oriented label.



`wake/application.py` is the application contract bridge.
`wake/record_store.py` is the transitional Store interface backed by WAKE authority.
`wake/application_policy.py` owns WAKE domain governance.
`wake/event_format.py` owns stable WAKE event identity bytes and hashes.
`wake/domain_events.py` owns deterministic WAKE event reduction without storage authority.
`wake/store.py` is legacy SQLite compatibility only; normal runtime/domain code must not import it.

## Migration discipline

Every authority-boundary change must preserve replayable meaning.

When replacing a legacy path:

1. verify the legacy event/state source before importing it;
2. preserve the exact migration provenance and historical head;
3. route post-migration mutations through WAKE application actions;
4. keep legacy code read-only where it remains necessary for migration verification;
5. prove behavioral or replay equivalence before deleting compatibility machinery;
6. never maintain two writable authoritative stores.

A migration convenience is not sufficient reason to weaken governance, provenance, or failure visibility.

## Source and publication branches

- `master` — development source and documentation
- `wake-public` — uploaded, filtered website snapshot served by GitHub Pages
- `wake-runtime`, `wake-state`, `wake-live` — preserved historical executor artifacts

Research runs in containers: either an explicitly selected local installation or
the hosted GitHub Actions installation. Hosted continuation uses explicit API
dispatches, with completion-event recovery; it never relies on cron.
`wake-hosted-state` and the encrypted `wake-hosted-checkpoints` release carry
verified native-record recovery snapshots. Only that dedicated rotating ref may
use compare-and-swap replacement; preserve all historical hosted branches.
See `docs/cloud.md` for privacy, checkpoint, stop and publication boundaries.

## Provider boundary

Providers receive bounded context and return untrusted proposals.

Provider failures, quota pressure, deferrals, malformed output, and rejections must remain visible and must not fabricate accepted research.

Generic provider-attempt lifecycle, context-delivery evidence, interruption recovery, durability-barrier-before-effect ordering, and provider-neutral invocation accounting belong to WAKE runtime primitives. WAKE may classify its provider-specific exceptions and apply Gemini/fallback quota policy, but it must not reimplement the generic execution boundary in parallel.

No model/provider receives arbitrary filesystem, database, governance, or policy authority through WAKE.

## Presentation boundary

GitHub Pages, Bob, MAP, metrics, journal views, workflow summaries, and `wake-live` are derived presentation.

Never read them back as operational truth.

Public labels should use configured human-facing topic labels rather than leaking internal machine IDs where a label exists.

## Conceptual consistency

Use [why WAKE](docs/why-wake.md) as the canonical explanation of the wake and
Quantum Wake Function metaphor. Keep the infrastructure-first identity and
research as its first application. Connect the metaphor to recorded consequences,
bounded context and governed transitions; never describe it as an implemented
function, new quantum physics, quantum computation, consciousness or persistent
personal identity. Recorded claims are not established truth, and a rejected
proposal's receipt is not an accepted transition. Corrections and supersession
preserve earlier history. Keep API definitions literal and link to the canonical
explanation instead of repeating it.

## Documentation synchronization

When code materially changes migration status, authority, operator workflows, context delivery, provider accounting, or research governance, update the canonical prose in the same work:

- `README.md` — current repository-level picture
- `docs/architecture.md` — authority and trust boundaries
- `docs/cloud.md` — container export and public mirror publishing
- `docs/experiment.md` — experimental interpretation
- `docs/retrieval.md` — progressive abstraction/retrieval behavior
- `docs/glossary.md` — plain-language meanings for project terms

Public documentation describes reproducible checks and current contracts, not local certification. Builds and operation must not depend on private task notes or installation-local guidance.

When prose and implementation disagree, current code/tests are evidence of behavior, but the documentation mismatch is a defect to fix rather than a permanent disclaimer.

Write guides for a person who is new to the feature: lead with the plain-language
answer, explain a term when it first appears, and put runnable steps before deep
implementation detail. Keep technical precision where it affects safety or correct
operation. Use task-oriented headings and a small diagram when it makes ownership,
data flow, or setup easier to follow. Prefer one canonical explanation with links
over repeating the same detail in several documents.


## Engine authority injection

Engine construction must name its authority.

Operational code injects the store returned by `open_authoritative_store(...)`.
Legacy compatibility tests may pass `store_factory=Store` explicitly. `Engine` itself must not import or construct the legacy Store.
Do not restore an implicit `Store(directory)` fallback: forgetting store injection must fail rather than silently creating a second `wake.sqlite3`.

Fresh initialization is native wake initialization. The legacy Store is opened only when an actual pre-migration `wake.sqlite3` exists and must be verified/imported.

## Standalone ownership

All active runtime code is owned here. Do not add another project's dependency, service, or access-control database. Preserve historical V1 format bytes and exact provenance when changing ownership or checkpoint filenames. Existing V1 authority is adopted by verified format discovery; ambiguity fails closed. Historical hosted checkpoints use `data/wake.sqlite.gz`; retain them as history. Current research continues through the same container governance and local or hosted operator controls. Other repositories may be read for comparison, but never modified without explicit authorization.

## Environment and publication boundaries

Start with `docs/development.md`. Follow current user instructions and maintained repository guidance; do not derive authorization from private task notes. Identify checkout, imported package, process, image,
data volume, runtime ref and intended website before changing execution or deployment.
A bind-mounted checkout and an installed image may execute different code. Preserve
existing edits and record volumes; source synchronization never authorizes record copying.

Local and hosted records are independent. Never reconcile their counters by importing
one into the other. Research browser transport reads only same-origin exported files. An explicitly bound hosted status light may read public GitHub Actions metadata anonymously; those observations never enter research state, per-node runtime animation or governance. Missing installation identity must stay same-origin and be visible in Console.
Export owns deployment identity and local operator links as well as data and assets;
raw HTML templates must not replace generated pages. Verify the actual snapshot
head/version and transport on LAN access, not only appearance or HTTP success.

Verify source before an authorized push. Source publication, container restart,
public snapshot upload, and record reset are separate actions. Publishing the
mirror pins completed immutable exports without changing research controls; never
reset or copy its authority records as a side effect. Mirror delivery must not
wait for worker availability or acceptance of a new Bob article. Preserve all historical hosted branches.

Update living documentation at its existing owner; retain dated validation history.
Comments should explain invariants, hazards and failure behavior at the responsible
code seam, not preserve a conversation or repeat instructions without implementation.

## Reusable kernel and parallel installations

The kernel remains owned here. Its imports must stay within `wake/kernel/` and
the Python standard library. Use the public application contract; no research
imports or another project's service belongs in the generic kernel. Preserve
application identity/version and migration semantics. See `docs/kernel.md`.

Use stable unique Compose projects for independent installations, each with one
writer and its own volume. `compose.instances.yaml` uses installation-specific
settings, paused fixture defaults and dynamically assigned loopback ports. Never
reuse the operator volume as test data. Hostname gateways are optional and may
not mount Docker's socket, authority data or provider credentials.

The offline container acceptance workflow builds and tests but never publishes
images, runs live providers, promotes runtime or touches hosted authority.

Live Console inspection is optional, read-only and non-authoritative. Explicitly bound hosted activity may carry allowlisted native runtime observations through an expiring anonymous relay. Its storage is a disposable view, never research authority; it excludes provider bodies, credentials and controls. GitHub Actions metadata alone remains batch status. Observers
must not affect governance or provider-effect sequencing. Only an explicit native
runtime capability bound to the installation may animate an in-flight matrix coordinate. Hosted pending
snapshots are dated evidence, not live execution. Clear overlays on disconnect
and keep score, selection, accepted progress and historical replay separate.
