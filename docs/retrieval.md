# Routine memory and retrieval: making forgetting observable

The [kernel contract](kernel.md) distinguishes generic envelope replay from
application state reconstruction. Application IDs share a record revision when
installed together; independent installations must select separate records.

## Internal nodes and Console aggregation

In the current one-container installation, three parents and nine children each
own a record and receive bounded context through the research application. Shared
notes and repeated source material retain their original attribution; another
node's use of the same source does not create independent evidence. The kernel
retrieval and authority boundaries are unchanged.

`installation.json` combines exported node projections for inspection. It cannot
replace a node's record or become operational truth. The Console selects a node's
complete view; the public mirror shows dated exports rather than live execution.
[Standalone setup](standalone.md#run-one-installation-container) owns that transport
and operator contract. Archives for import/export remain separate from public views.

## In plain language

The full record keeps exact history. A model receives a smaller working view so
the request stays useful and within a size limit. When detail is needed, the
request can point back to exact records. If required material still will not fit,
WAKE stops before calling the model rather than silently dropping obligations.

```mermaid
flowchart LR
  F[(Full durable record)] -->|select and summarize| W[Bounded working context]
  W --> M[Model request]
  M --> R[Receipt records what was delivered]
  W -. exact IDs and provenance .-> F
```

The shortened view is not a second database, and it is not semantic memory. It
does not reliably detect contradictions or decide what is true.

Project source handoffs exclude unreadable payloads and prefer a qualifying
underlying work not yet cited in a belief or notebook over a newer repeat or
mirror of incorporated material. The bounded unincorporated-source window uses
the same preference while preserving domain fairness. Repeated works remain
available when fresh works are absent. This orders delivery; it does not change
evidence eligibility, establish novelty or rewrite historical citations.

The configured `memory_mode = "active"` promotes derived working views into routine provider input. Every invocation carries compact belief state, all open commitments, active projects and recent notebook pointers, plus `context.memory` containing advisory compacts and selected durable records. Recent operator observations and retractions with their newest counterevidence take priority, followed by excerpt boundaries, due work, revisions and source handoffs. Up to eight retrieved records and eight compacts are delivered; fields are excerpted at 900 characters and compact rules at 320. Omission counts/digests, missing references, exact record hashes and retained evidence roots expose the limits. This is a deterministic bounded retrieval policy, not semantic contradiction detection.

Collected source prose follows the existing qualifying-source rehydration budget (up to three records at 1,800 characters in active mode and four distinct repository URLs in total). Collector records outside visible source delivery carry pointers without content. Human falsifiers keep their provenance and can support belief review without becoming scientific notebook sources. Recent notebook evidence roots are included in the active retrieval plan so synthesis and publication allowlists remain usable.

The complete request is checked again after same-wake research links and final proposal instructions are added. Under pressure, source excerpts shorten first to 900 and then to 400 characters. Duplicate retrieved belief prose points to the mandatory belief working set; prose may shorten to 80 characters. Optional advisory compacts shorten and then reduce in number, with omission counts and a digest, retaining challenged hints first. Visible evidence IDs, mandatory belief provenance roots and open commitments remain present. If that request still exceeds the ceiling, emergency compaction shortens planned queries to readable excerpts, replaces their URLs with request hashes, and keeps the active-memory trust instructions and final proposal instructions. If the exact request still cannot fit, no model call is made. The standalone scheduler keeps its website available with a `blocked` runtime status until an operator reviews the budget and restarts it.

Numbered containers created by the local `wake_runner` exchange a bounded set of
readable source observations and one concise, attributed notebook finding per peer
over their private group bridge. A source packet carries the source URL and
collected content plus its originating instance, evidence ID, application head,
version and content hash. The receiving WAKE appends each valid item to its own
record as a peer-origin source observation, then applies its usual source
qualification and claim-support rules before allowing citation. The notebook
finding is an attributed lead, never a local claim or citation ID; full notebooks,
topic lists, projects and record authority are not shared. The normal research
context includes peer notes and selected peer sources alongside local sources,
without instructing the model to seek a particular connection. Fetching and
importing peer material makes no provider call. The local bridge trusts its
operator-created members and is not cryptographic remote attestation. Solo,
Codespace and hosted installations do not participate.

Grouped local Gemini model requests also use the local gateway as a best-effort
FIFO call coordinator. It serializes provider requests and applies per-model
spacing, but it carries no research data or durable state. If the gateway is
unreachable, a member proceeds without coordination; leases expire if a member
stops during a request. This scheduling layer does not join solo, Codespace or
hosted installations.

The active-memory fit also bounds milestone editorial history, including when final research links arrive after its initial fit. It clips editorial prose to 80 characters, omits auxiliary editorial project/notebook/search windows, and retains as many of the latest four, two or one accepted wakes as fit; zero is permitted when necessary. Previous-reflection identity and milestone remain, alongside the original history hash, original window counts and omitted counts. Repeated fits preserve that original hash. These omissions affect only disposable editorial context, not the durable record or the current research working set. The existing hard ceiling still fails closed if protected context cannot fit.

`memory_mode = "shadow"` restores rich delivery with the established size-triggered fallback after runtime restart. The raw shadow builders remain unchanged in both modes. Derived memory neither rewrites history nor changes governance; the authoritative database remains the single source of truth. Active requests receive a final emergency fit after same-wake plan details and proposal instructions are attached. That fit preserves compact trust instructions and request identities; requests still above the exact provider ceiling stop before inference.

Console’s browser overview is a separate disposable presentation projection. Its bounded graph and record excerpts are never read back into provider context or retrieval decisions. IDs, explicit relationship pointers and record-head provenance support deeper inspection through Console’s complete record workspace; missing overview records do not imply missing authoritative records.

Current source eligibility requires nonempty readable collected material. Publisher menus and response forms cannot make a source synthesis-ready or supply claim-support tokens. Historical raw observations remain available for exact inspection; stricter current qualification does not invalidate historical replay. Derived evidence-quality diagnostics include unreadable cited-source IDs.

### Browser views and exact detail

Open the homepage, Blog or journal normally. Reader pages download a recent
overview of at most 256 KiB. Select a story, source, notebook or invocation to fetch
its exact exported detail. Use **Load older** below a list to fetch another page.
Recent-overview limits are labelled; complete history and state exports remain
available through their explicit archive links. An overview does not count as the
complete record and is never used to reconstruct authority.

Generic application observability also separates complete-history counts from
bounded recent lists; zero or negative recent limits omit those lists. Its failure
diagnostics are derived evidence, never provider context or recovery authority.
See [operational indicators](resilience.md#use-separate-indicators).

Console and its process view share `research-overview.json`; opening a wake's
context or response fetches its detail under `research-details/`. The complete
`research-data.json` export remains available separately. Detail errors are visible
and retryable. A record-detail packet that belongs to a different reader snapshot
is rejected with a reload instruction. Ordinary refreshes check the small export
head rather than downloading the accumulated archive again.

These files are produced together in a disposable website generation. HTTP
serving reads completed exports and bounded observations, never a record database
or provider. Stopped, stale or missing workers therefore cannot gate access to
completed pages. Missing exports remain visibly missing; no replacement research
or synthetic progress is inferred.

## Why this exists

Progressive abstraction only stays epistemically safe if compression remains correctable.

A useful architecture therefore needs two deterministic questions:

1. What can leave active context?
2. What conditions should cause exact resolution to return?

The retrieval shadow answers the second question without pretending that a deterministic rule can understand semantic contradiction.

## Current deterministic signals

The planner records bounded candidates for:

- **excerpt boundary** — a belief claim or retention reason was clipped in the working abstraction;
- **belief retracted** — the current durable state says a belief was retracted;
- **notebook revised** — a research notebook has been materially revised under newer evidence;
- **commitment near due** — an open commitment is within two cycles of its due cycle;
- **unincorporated evidence** — recent durable non-runtime evidence is not yet represented by a belief or notebook.

Each candidate records IDs and provenance pointers only. Evidence contents remain in the authoritative durable record.

## What it does *not* claim

The deterministic planner does **not** claim to detect contradiction, importance, truth, consciousness, intent, or subjective uncertainty.

“New contradiction or counterevidence” remains a semantic judgment. A later controlled design may let a model request exact rehydration for that reason, but the request must itself become a receipt.

## Invocation receipt

Each invocation should now retain:

- `working_set_shadow`
- `retrieval_shadow`
- working-set size versus delivered-context size
- retrieval candidate count
- number of exact evidence IDs the planner would rehydrate
- counts by deterministic trigger
- `trust_compacts_shadow`: candidate operational rules, their evidence roots, and their deterministic reopen hooks.

`retrieval_shadow` and `trust_compacts_shadow` remain receipt-side measurements. Active mode derives provider memory from them without making either authoritative. `context_delivery` records `memory_mode`, `activation_reason`, `memory_digest`, retrieved-record count and measured request sizes; `request_hash` identifies the exact full request. No extra model call is made.

## Evaluation boundary

Routine active delivery is operator-enabled, and the size-triggered fallback remains an operational safeguard. Neither proves behavioral equivalence to rich context. Paired evaluation remains necessary to score whether the representation preserves:

- evidence-backed belief revision,
- contradiction/counterevidence handling,
- commitment continuity,
- research provenance,
- justification quality,
- and recovery from abstraction mistakes.

The comparison remains:

**A — rich context**  
Delivery in shadow mode when it fits.

**B — working abstraction + recoverable provenance**  
Routine active delivery and the controlled overflow fallback, distinguished by receipt activation reason.

**C — overcompressed control**  
A deliberately weakened condition that removes provenance or uncertainty cues.

The primary question is whether B preserves correction while reducing active context.
The executable [paired comparison](experiment.md#paired-memory-and-model-comparison)
implements A and B from one frozen synthetic record, with native context/receipt
handling and separate structural checks and human explanation scoring. C and repeated
human-scored research handoffs remain future work.

> Exact underneath. Approximate on purpose. Correctable always.

Console wake inspection includes bounded delivered-context field names, the full observed system instructions and recorded request, request identity, provider-attempt metadata and terminal receipt identity. It does not reconstruct absent start events or treat context receipt presence as proof that a proposal was accepted. Source-depth drilldowns show cited records in the bounded graph; overall evidence counts may exceed that displayed population.

Console carries recorded context-delivery measurements alongside complete observed requests. Compression plots use the reported retained-request ratio. Allocation plots group selected delivered fields as objectives, constraints, frontier and results; excluded fields and the bounded event population are explicitly described.

Console also exposes the exact provider-response text retained by terminal events. Rejected responses remain unaccepted output; parsed proposal summaries are views of that output and never replayed as accepted actions. The UI labels missing response events and any recording-time bounding.

## Verified replay seeds

Signed checkpoints materialize the WAKE application projection once instead of replaying its entire event-log prefix on every checkpoint resume. `replay-checkpoint` verifies the independently retained signature and boundary, then incrementally applies later semantic events and checks their recorded application result digests. It exports derived state without changing the database or ordinary startup. `verify-checkpoint` performs the slower genesis audit, including complete provider/access journals. The signed-prefix trust boundary is explicit: fast replay cannot prove untouched interior prefix bytes or later provider/access events. Complete original history is always retained for audit. Compact source concentration counters in normal provider context help expose repeated material without conflating diversity with truth.

Active delivery avoids copying evidence prose twice: retrieved records use `content_location` to identify the corresponding readable entry in `context.evidence`. If the request still exceeds the ceiling, extended recovery prose is replaced with explicit omission markers, hashes and retained project/frame/observation pointers. All belief identities, evidence roots and open commitments remain intact. If this bounded request still does not fit, the provider is not called.

Same-wake research plans are recorded before fetching. The collector can follow bounded metadata routes immediately instead of requiring another scheduled cycle. The final request prioritizes newly collected source IDs, including when no active project exists yet, then rebuilds scientific-source allowlists. Retrieval failures remain observations with `scope = failed`; discovery/metadata cannot become notebook evidence merely because they arrived in the same wake. Further pressure reduction excerpts source/working prose explicitly while preserving visible identities, evidence roots and request hashes anchoring shortened retrieval instructions.

An attached planning project must be active, delivered in context and in the requested topic. A question with no eligible project uses an empty project ID without implicitly reopening historical work. Invalid plans remain rejected receipts and stop that wake before retrieval; the scheduler may continue with a fresh planning invocation.

Routine and emergency views retain full-record queue counts, exact visible project identities, notebook-specific new-evidence IDs and the last two rejection/failure reasons with targeted recovery guidance. The contract is refreshed after evidence rehydration, so new same-wake sources may enable a revision without losing prior notebook identity. Omitted notebook prose cannot make an existing artifact appear new. This guidance is operational context rather than research evidence, and the original append-only record remains unchanged.

When Attention selects a parked topic while all three project slots are occupied, the provider contract offers one exact parking transition first. A due editorial checkpoint remains separate. This temporary generation restriction avoids unrelated commitments or synthesis attempts before capacity recovery; governance still decides whether the proposed transition is valid.

## Inspecting delivery across installations

Memory receipts describe the record that produced them. A local Console reads its
installation's same-origin `research-data.json`; public mirrors read their uploaded
public projection. Confirm the displayed head/version and export mode before using
a screenshot to assess retrieval or memory behavior. Shared code and shared topics
do not make histories interchangeable. Missing context events in a bounded overview
are a presentation gap, not proof that invocation evidence has been lost. Use the
matching installation's complete record tools to resolve it. See [development](development.md).

## Inspection metadata

`recorded_activity` is a dated view of pending invocation/cell identity. It is not
retrieved as operational context and does not authorize continuing a pending wake.
The optional container activity channel is ephemeral and is never replayed into
research memory, matrix results or history. Its live pulse is not a score.

Retrieved projects, notebooks, search records and commitments already delivered in
working fields use explicit `content_location` pointers instead of duplicate prose.
Their exact retrieval hashes, status and evidence roots remain in memory receipts;
records outside the visible working set retain their delivered value. This fit is
idempotent and changes only the provider view. The final ceiling remains mandatory,
and an impossible protected context still fails before any provider call.

Current proposal guidance derives belief-review eligibility from the full record and visible evidence. Existing belief IDs are separate from new-belief creation; a review must cite at least one visible evidence ID outside that belief's durable roots. If no such evidence is delivered, no review alternative is offered. This narrows generation guidance without changing acceptance or historical replay.

When the provider request approaches its context ceiling, belief review alternatives are bounded to one genuinely new visible evidence root per belief before source prose is shortened. Where eligibility overlaps, reviews share a root so equivalent schema branches merge; all offered belief IDs and their new-evidence requirement remain. This prevents repeated schema alternatives from crowding out an enabled continuity sidecar. Durable belief evidence and deterministic governance remain unchanged.

Under final context pressure, the engine can replace verbose core instructions with
a concise equivalent before reducing source text. Active-memory instructions may
also use concise wording preserving trust, correction, omission and citation rules.
Application, probe and operator-question instructions and the response schema
remain intact. The delivery
receipt records the compaction; durable evidence roots, obligations and governance
are unchanged. Requests that still cannot fit fail before inference.

Under extreme final-envelope pressure, omission explanations use concise,
human-readable labels. Every category remains represented; unknown labels stay
verbatim. This reduces delivery metadata rather than omitting a test, evidence
identity, provenance root or obligation. Exact delivered requests remain recorded.

A retrieved record with a full-record `content_location` pointer may omit fields
that exactly duplicate that supplied working record. Retrieval hashes and the
pointer remain; every omitted field stays in the named working record. Different
source provenance or evidence roots remain explicit instead of being merged or
discarded. Records outside the supplied working view retain their values.


## Provider-ready input budget

`max_context_chars` bounds the exact model-visible **system plus user text**, in
characters. It is WAKE's application safety budget, not a vendor token-window
limit and not the size of an escaped HTTP JSON body. The engine and Gemini adapter
share `provider_input_text`: compact JSON is rendered identically without expanding
Unicode or inserting display whitespace into the context or response contract.
The adapter refuses an oversized request before any network call, including when
called outside the engine. Fallback models receive the same rendered text.

Every fit includes the complete instruction/response contract and enabled
continuity packet before calculating the remaining working-context allowance.
That allowance covers all other context fields, including retrieved memory,
working beliefs, source handoffs and omission metadata. There is no separate
unaccounted schema or final-link surcharge. The final fit runs again after planning
links and allowlists have been refreshed. Protected provenance and obligations
remain governed by the existing retention rules; impossible requests still fail
closed. An optional probe that cannot fit remains untested rather than receiving
a fabricated result.

New invocation receipts carry `context_delivery.provider_input_budget`, with a
versioned measurement basis, exact rendered-input hash and size, reserved
instruction/probe sizes, working-context allowance and usage, and remaining room.
Provider-attempt receipts record the matching rendered-input hash/size. These
receipts let inspection distinguish compaction from transport formatting and
prove which text was attempted. Historical `delivered_request_chars`,
`rich_context_chars` and `request_compression_ratio` retain their compact internal
JSON-envelope meaning; use the new `provider_input_compression_ratio` to compare
rich and delivered model-visible text. Transport bytes and vendor-reported token
usage remain separate provider measurements. No extra provider call is required.

Group Bob requests carry bounded attributed excerpts from every member, with
record heads and versions identifying their dated origins. Excerpting must not drop
a member or let the model infer missing facts. These summaries are editorial
context rather than imported qualifying evidence. Native invocation receipts retain
the exact delivered public request and model response. Inputs include notebook
and revision identifiers, dates, claim labels, limitations and source/record links.
Whole older stories and prose may be omitted to fit; remaining identifiers are
retained, and an oversized source URL is omitted rather than truncated into a
false link. Recent attempts are selected by recorded time. Articles cite supplied
story IDs; operator correction feedback and a bounded prior-draft excerpt reserve
room inside the same provider input ceiling. See the
[editorial contract](development.md#first-run-publication-and-passenger).

Later group requests also compare current supplied story packets with the last
accepted article's captured inputs and include bounded excerpts of that article.
These differences describe the delivered records, not semantic novelty or verified
scientific progress. Optional prior prose is shortened or omitted before current
member summaries and citation identities. Earlier Bob prose remains presentation,
never qualifying evidence. See [reader continuity](development.md#reader-experience-and-editorial-continuity).

Passenger text, including its factual first-publication receipt, never enters
research memory, retrieval or trust compacts. A
separate bounded private advisory request may read its latest assessments as
lower-trust data. It cannot supply scientific evidence, policy or authorization;
private output stays outside the public record. See
[the advisory privacy boundary](development.md#first-run-publication-and-passenger).

Model-context summaries do not replace exact durable requests or responses. Storage-version 13 dictionaries compress repeated text losslessly; this changes storage, not delivered context or retrieval policy. See [kernel storage](kernel.md#physical-storage-and-compatibility).

The final proposal schema is rebuilt after quality-policy and measured-result context are attached, even when queue constraints have not changed. Non-tested claim results are empty strings; tested eligibility comes only from visible measured reproductions. Both rich and compact instructions require copying the current version without incrementing it, and recovery guidance retains these specific rejection remedies.

Under forward quality policy, notebook proposals supply structured claims and omit the duplicate `findings` field. WAKE renders findings from those exact statements and support IDs before validation. Historical proposals with supplied findings remain valid only when they match the claims exactly; conflicting prose is never repaired. Source support and accepted-cycle accounting retain their existing checks.

Source delivery compacts the parsed source packet rather than cutting serialized JSON. Bounded views preserve source classification and select exact substantive prose ahead of titles, authors and PDF front matter. Escaped JSON stays within the provider budget, and successive shortening retains a quotation surface. These are incomplete derived views; full source records, IDs, provenance and exact-passage validation remain authoritative.
