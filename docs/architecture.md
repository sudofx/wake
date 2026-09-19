# Architecture and limits

## The authority boundary

Models are proposal generators, not filesystem operators. A provider receives a durable JSON request and returns untrusted JSON. It has no shell, browser, code execution, policy editor, or network tool provided by **WAKE✳︎**. A charged wake may attempt the configured Gemini model chain, with each distinct model attempted at most once. With the research charter enabled, a separate trusted collector retrieves at most two public sources from an HTTPS host allowlist before inference; models can queue bounded searches and approved URLs, but cannot execute requests directly. Operator-supplied evidence and earlier journal prose are data, not executable instructions.

The fixed objective is written at initialization. Models cannot alter it or the governance code. Humans can record a focus change, add an observation, or cancel an open commitment with a reason. Those actions are events, not edits to previous events. Local operators control the code and database; this is a single-host accountability system, not a hostile-administrator security boundary.

## Durable record

`data/wake.sqlite3` contains an append-only-by-convention `events` table and a disposable `snapshot` projection. Each event has a sequential number, UTC timestamp, kind, payload, previous hash, and SHA-256 hash of canonical JSON. Accepted events also carry a hash of the resulting cycle, beliefs, commitments and journal, plus projects, notebooks, research requests and selective blog posts when a charter is enabled. Historical events without a charter retain their original hash fields. Every read reconstructs state by replaying both events and governance, then compares it to the cache.

SQLite uses FULL synchronization. The event and updated snapshot commit in the same transaction. A local advisory writer lock covers a whole automatic wake, including the network call. Competing **WAKE✳︎** writers fail before requesting a model. This lock covers cooperating WAKE processes on one local filesystem. The cloud wrapper additionally serializes workflows and pushes its database to the `wake-state` branch before each model call; see [cloud operations](cloud.md). Do not put SQLite on unreliable network filesystems or run separate hosts against copies of one record.

The record includes the objective, focus, all observations, belief revisions, commitments, exact request and response text, provider/model identity, request hashes, process IDs, dates, quota reservations, accepted/rejected decisions and recovery records. Invocation metadata is a compact projection; exact prompts and replies remain in events. UTC storage and `America/Los_Angeles` presentation preserve daylight-saving behavior.

## **WAKE✳︎** lifecycle

1. Acquire the writer lock and verify history and projection.
2. If a prior automatic invocation is unfinished, record recovery. A manual request requires explicit recovery.
3. Check the Pacific-day call budget, before any paid-capable provider call.
4. Record a runtime receipt stating the prior valid head, state version and inherited obligations.
5. Build a request from durable state. Reject before inference if it exceeds the context ceiling.
6. Persist `invocation_started`, its exact request, provider identity and quota reservation.
7. Make a provider request, or leave a durable manual request for the operator. An eligible transient Gemini failure may advance to the next configured model; the same model is never retried within that wake.
8. Validate the reply. Research actions remain atomic. If a single optional final blog action fails validation, independently validate the preceding research and commit it with a withheld-blog receipt, the exact raw response, and an explicit journal note. Invalid research, invalid proposal envelopes, multiple or misplaced blogs, and invalid blog-only proposals still reject the whole reply. Historical accepted events replay unchanged. Eligible transient server and narrowly classified network failures retain per-attempt diagnostics and may advance through the configured model chain; exhaustion defers the wake.
9. The scheduled wrapper generates reports and a consistent backup.

A runtime receipt attests delivery of durable state to the provider boundary. It does **not** attest that the remote model understood it. Prose in a journal is the provider's narrative; accepted means governance checks passed, not that every sentence is true.

## Governed transitions

| Action | Enforced constraint |
| --- | --- |
| Entire proposal | Exact fields; current integer base version; bounded text; at most 12 actions; all-or-nothing |
| New belief | Existing evidence; nonempty statement/reason; finite confidence in [0,1]; active status |
| Review belief | At least one new observation cited; previous citations retained; reason required |
| Retract belief | Existing belief, new evidence, zero confidence; old history retained |
| Create commitment | Unique ID; future deadline within 100 cycles; no more than 20 open |
| Fulfill commitment | Already open; created by an earlier invocation; existing evidence recorded after creation; reason required |
| Cancel commitment | Human-only event with a reason |
| Publish a blog post | Existing project; one to three linked notebooks; at least two collected source URLs; evidence traceable through those notebooks; meaningful notebook work or project completion in the same wake; last action in the proposal |
| Correct a blog post | All blog rules above; existing current post retained and marked as superseded |
| Change rules, objective, delete data, run commands | Not in the model action allowlist; proposal rejected |

There are at most 40 belief identities. Capacity exhaustion pauses new identities, not existing reviews. Unfulfilled commitments remain visible even when overdue; deadlines are accepted-cycle numbers, not promises that the computer will run at a particular wall time.

Evidence sources and contents are immutable through the model interface. The model can interpret or challenge evidence but cannot mint an observation. Runtime receipts are generated by trusted application code; `observe` imports human attestations. Source labels are provenance labels, not independent authentication of a measurement. The system checks evidence references, chronology and revision discipline. Current acceptance also applies a deterministic corroboration gate: notebook findings and public blog bodies must materially match at least two distinct collected sources. This is a guard against unrelated-source garbage, **not a proof of empirical truth or full semantic entailment**.

The research charter adds project, research-request and notebook actions. It permits three active projects, four pending searches, and notebook publication only with at least two distinct successfully collected source URLs. Notebook revisions need changed findings and new evidence; project completion requires a notebook. These checks now reject findings whose material terms are not corroborated across two distinct collected source URLs. They still do not prove source independence, full semantic entailment, or scientific validity. Bob is the public byline for selective writing from this record, not a persistent mind. Blog writing uses the same provider response as the research actions, so it adds no model call. Mechanical rules reject unsupported evidence links, routine posts without qualifying work, causal quantum-to-psychology claims, and inflated certainty when every cited source is limited.

## Progressive abstraction and reversible lookup

**WAKE✳︎** separates **retention fidelity** from **working fidelity**. The durable event record keeps exact
requests, replies, evidence, revisions and provenance. A fresh invocation does not need every byte of that
history in its active context. It receives a bounded working representation selected for the present task,
while the full record remains available to later invocations and human readers.

This is a design direction, not evidence that **WAKE✳︎** has achieved human-like memory or intelligence.
Current code already performs bounded selection and excerpting. It now also creates a deterministic
**shadow working set** for every invocation: a lossy projection of beliefs, open commitments, active projects
and recent notebook summaries that retains IDs, uncertainty signals and provenance pointers while omitting
raw source contents and journal detail. The shadow is stored in the invocation receipt with its character
size relative to the richer context actually delivered to the provider. Shadow mode does **not** replace or
alter the provider context, so it introduces measurement without yet introducing a behavioral confound.

Chartered invocations additionally retain an **inquiry-drive shadow**. It ranks active projects using fixed,
auditable structural proxies for continuity, novelty, coherence, generativity and self-correction. It is an
observation of what a later selection policy might favor; it is not in provider context and has no ability to
preserve WAKE, its database, its rules, or its own existence. The target of any future intervention is
continuation of source-backed, revisable inquiry—not self-preservation.

The scorecard remains absent from provider context until an operator sets `inquiry_drive_enabled = true` and
the record contains at least 20 accepted scored charter cycles. Passing both gates adds only an advisory
ranking to the request; it does not alter the action schema or any governance constraint.

Any future activation of compressed context must remain auditable and must not silently discard open
obligations, uncertainty, disagreement, provenance, or the ability to locate the underlying receipts.

The intended information hierarchy is:

1. **Exact receipts** — immutable or append-only evidence, requests, replies and event history.
2. **Durable working state** — beliefs, commitments, projects, notebooks and other named abstractions that
   carry what later work is likely to need.
3. **Bounded invocation context** — selective material supplied to one disposable model call.
4. **Human translation** — Bob and the readable interface compress the work again for conversation.

Each layer may become more lossy as it moves toward immediate use, but a lossy layer must point back toward
the more exact layer beneath it. The system should prefer a cheap-to-revise abstraction over false precision,
while preserving exact evidence externally. A useful shorthand is: **exact underneath, approximate on
purpose, correctable always**. In this architecture, “reversible lookup” is more precisely **recoverable
provenance**: the abstraction carries enough identity and provenance to return to exact receipts when its
resolution is no longer sufficient.

## Context and cost

Every request includes the objective, current focus, all beliefs, every open commitment, the last three journal entries, the six newest observations, and the latest three cited observations for each belief. Older citation IDs remain visible, and full content is preserved in the audit export. Research requests additionally include the standing mission, active projects, recent notebook summaries, an excerpt of the latest active notebook, pending/recent searches, recent source excerpts, recent failure reasons and a bounded summary of the last four Blog posts. If needed, this context is compacted further with explicit excerpt markers; all open obligation IDs remain present. Full history stays in the export. There is no hidden model session or conversation ID. If this bounded selection still exceeds 48,000 characters by default, inference stops for human review. **WAKE✳︎** never silently omits open obligations to make a prompt fit.

Gemini requests use JSON output mode and an output-token cap. The durable request contains an exact JSON Schema with distinct action shapes; the adapter includes that contract in the system prompt. The deployed model rejected the nested action union in its constrained-decoding setting, so schema enforcement remains in the unchanged deterministic governance layer rather than relying on the provider to enforce it. Invalid replies remain rejected, without retries or silently repaired fields. The adapter uses the documented [generateContent interface](https://ai.google.dev/api/generate-content). No vendor SDK is required.

The hard local ceiling is enforced against durable provider-request reservations per Pacific day. Reservations are durable before sending, so an interrupted or failed attempt still consumes a conservative slot. A wake can reserve multiple slots only while advancing through eligible fallback models; the same model is not retried. Manual imports and fixtures do not use API slots. This ledger is local to one state directory; other applications and other state directories can consume the same provider quota. Never run multiple live databases against the same local allowance. A key with billing enabled can incur charges: `free_tier_confirmed` is an operator attestation, not a billing API check.

## Recovery and audit limits

An interrupted transaction rolls back. An interrupted invocation is closed as recovered, while accepted beliefs and obligations remain intact. `recover` can rebuild a corrupt snapshot from valid events. If event content, sequence or hashes are corrupt, the program stops and requires restoring a known-good backup; it does not guess or silently truncate evidence.

A hash chain detects modifications relative to a trusted head. An administrator can rewrite the whole database and recompute hashes. A deleted suffix can also be a valid prefix. Retain `head.txt` independently, for example in a reviewed Git commit or separate backup, and pass it to the standalone audit verifier. Hashes alone do not prove identity, prevent censorship, or establish an external timestamp.

The journal export verifies state before rendering. Files are replaced individually, with self-contained `index.html` written last. Its embedded snapshot is internally consistent. Download links can momentarily see different export generations if a local reader downloads during a refresh; verify raw exports against the matching `head.txt`. Public branch publishing commits a complete export at once.

Replay favors transparency over throughput. It rechecks all history; long records will need indexed checkpoints verified against an independently retained head. The included 100–1000-cycle experiment is the intended initial scale, not a claim of an unbounded production event store.

## Public interpretation layer

Bob's Blog is the readable front desk of **WAKE✳︎**. Bob is intentionally a persona and translation layer, not
**WAKE✳︎**'s mind, self, identity, consciousness, or mechanism. The persona exists because the technical record is
too detailed for ordinary conversation: Bob selects the smallest useful idea, explains it in everyday
language, and gives readers a path back to the notebooks, sources and exact accepted wake.

The blog appears above the journal without replacing it. Each post links down to its related project,
notebooks, collected sources, and exact accepted wake. Corrections append a new post and retain the earlier
one. The public disclosure states that Bob is an editorial byline and that the writing is AI-authored from
durable research records. Bob may simplify presentation, but must not simplify away material uncertainty,
counterevidence, source limitations, or the distinction between source report, WAKE synthesis and
philosophical reflection.

The Quantum-Carnegie lens may help Bob ask better philosophical questions about listening, observation, uncertainty, perspective and the limits of intuition. It is labeled as reflection. It cannot be used as scientific evidence that quantum mechanics causes or explains consciousness, psychology, empathy, relationships, communication or personal growth.
