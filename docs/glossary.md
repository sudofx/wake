# WAKE✳︎ glossary

Use this page when a technical term in the other guides is unfamiliar. The
definitions describe the current WAKE implementation, not broader industry
definitions. The wake entries describe its conceptual language rather than an API.

| Term | Plain-language meaning |
| --- | --- |
| **Accepted cycle** | A research attempt whose proposed changes passed WAKE's rules and were recorded. A workflow can succeed even when its attempt is rejected or deferred. |
| **Application** | The rules and behavior for a particular kind of work. Research is WAKE's current application. |
| **Authority / authoritative record** | The one database allowed to decide what state is current for an installation. Each local or hosted installation has its own. |
| **Blocked / red** | The runtime cannot continue without operator or agent action. |
| **Bob** | The byline for selected plain-language summaries of already-recorded research. Bob does not make research decisions or change the record. |
| **Child node** | One of three independent local researchers assigned to a parent node. It has its own record and can exchange findings only with its siblings and parent. |
| **Context** | The bounded information included in one model request. It can be smaller than the full record, but it keeps links to the exact sources it summarizes. |
| **Continuity matrix** | An optional, versioned set of structured probes. It uses the same model response as research and does not make another provider call. |
| **Discovery lead** | A search result or index entry that may help locate a source. It is not itself qualifying research evidence. |
| **Evidence** | A collected, readable source or recorded observation. WAKE checks provenance and structure; this does not prove that a claim is true. |
| **Gateway** | The local group landing page. It lists parent and child nodes and routes the browser to a selected node; it does not own their research records. |
| **Governance** | The deterministic rules that check a model's proposal before WAKE accepts changes. |
| **Group / parent node** | A local runner setup with numbered parent containers and three independent child nodes per parent. Each node keeps its own record. Network exchange provides optional context; a node can continue if another is unavailable. |
| **Kernel** | The reusable WAKE layer for records, decisions, transitions, receipts and replay. It does not contain research-specific policy. |
| **Projection** | A disposable view of the record for a website or Console. It can be rebuilt and is never the authority. |
| **Proposal** | A model's suggested changes. A proposal is untrusted until governance checks it. |
| **Quantum Wake Function** | A philosophical metaphor: the wavefunction describes what might happen; the wake function describes how what happened shapes what can happen next. It is not an established mathematical object, physical law, or implemented computational function. See [why WAKE](why-wake.md) for the scientific limits. |
| **Quota standby / purple** | A provider reported a quota limit. WAKE keeps scheduling retries, so it may return to normal research when a model has capacity. A configured hard daily cap can instead wait until the Pacific reset. |
| **Receipt** | A durable account of an attempt or decision. New proposal and provider receipts record Who, What, Where, Why, How, and When in hash-bound attribution; older missing details stay unspecified. See [receipt attribution](kernel.md#receipt-attribution). |
| **Wake metaphor** | The image of a disturbance left by passage through water: evidence of the past that can influence what follows. In WAKE, durable records carry consequences into future bounded context; this does not imply consciousness or a persistent personal identity. See [why WAKE](why-wake.md). |

The usual flow is:

```text
record → bounded context → model proposal → governance decision → transition → receipt
```

See [architecture and limits](architecture.md) for the full trust model and
[hosted operation](cloud.md) or [standalone operation](standalone.md) for the
operator procedures.

- **Initial publication** — the durable introductory Bob article. Worker groups
  synthesize `group-wake-introduction` from every parent and child and publish the
  same text in each record. Its WAKE01 checkpoint is separate from research progress.
  The older solo `wake-introduction` contract remains replayable.
- **First-post exception** — explicit operator permission for the exact first
  group introduction only. It is consumed once per member and cannot accept
  research, create scientific evidence or authorize later posts.
- **Passenger** — private container Markdown for installation-wide operational
  assessments and inert change proposals. It is advisory, cannot authorize work,
  and stays out of public context and exports. Named groups share the project-root
  file; its first-publication receipt contains facts rather than a model assessment. See
  [the operating contract](development.md#first-run-publication-and-passenger).

### Fresh hosted reset

Hosted Reset verifies the old authority and retains its exact checkpoint on a
`wake-archive-*` branch before initializing a small new database. The native
initialization receipt records the archive branch, commit and prior domain head.
Active research cycles, provider accounting and continuity results start at zero;
the fresh continuity campaign is enabled without a provider call. Historical
records stay in the archive rather than accumulating inside the new database.
Local in-place resets retain their history and are a separate operation.

Bob’s public articles use plain prose, including the built-in welcome. Markdown
is confined to Passenger. Public display removes legacy heading markers without
rewriting historical receipts.

**Lossless storage compression:** a smaller physical encoding that reconstructs the exact original record bytes. It is distinct from a model summary, which can omit detail. See [kernel storage](kernel.md#physical-storage-and-compatibility).

**Zero-cycle reset:** an operator action that clears active research progress and
starts a fresh enabled continuity campaign. It leaves research stopped or paused
until explicitly started; see [reset operation](standalone.md).
