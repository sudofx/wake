# WAKE✳︎ glossary

Use this page when a technical term in the other guides is unfamiliar. The
definitions describe the current WAKE implementation, not broader industry
definitions. The wake entries describe its conceptual language rather than an API.

| Term | Plain-language meaning |
| --- | --- |
| **Accepted cycle** | A research attempt whose proposed changes passed WAKE's rules and were recorded. A workflow can succeed even when its attempt is rejected or deferred. |
| **Application** | The rules and behavior for a particular kind of work. Research is WAKE's current application. |
| **Ask Bob** | An opt-in local reader experiment for bounded questions over published evidence. Conversation and reader self-reports never become accepted research or proof of comprehension. See [setup and limits](ask-bob.md). |
| **Inspection interface** | Static text, a resource manifest and reproducible evidence for an independent observer. It offers reading access without research or execution authority. See [inspection](inspection.md). |
| **Authority / authoritative record** | The one database allowed to decide a node’s current state. The current installation has one governed record per node; its aggregate Console is a view, not another authority. |
| **Blocked / red** | The runtime cannot continue without operator or agent action. |
| **Bob** | The byline for selected plain-language summaries of already-recorded research. Bob does not make research decisions or change the record. |
| **Child node** | One of three internal worker processes assigned to a parent. It owns a governed record, exchanges bounded material with its siblings and parent, and stops when the installation controller exits. |
| **Context** | The bounded information included in one model request. It can be smaller than the full record, but it keeps links to the exact sources it summarizes. |
| **Experimental research topic** | An operator-supplied starting question labeled with an experiment ID. Models can formulate projects and challenge assumptions within it; it grants no additional operational authority. See [research expansion](research-expansion.md). |
| **Continuity matrix** | A versioned set of structured probes enabled automatically for native research initialization and every reset. It uses the same model response as research and does not make another provider call. |
| **Discovery lead** | A search result or index entry that may help locate a source. It is not itself qualifying research evidence. |
| **Decision State Capsule** | An optional, disposable selection of records relevant to one question, bound to an exact version and head. The full audit capsule stays in the receipt; a smaller model-facing view may refer to its hash while retaining source identities, availability, corrections and caveats. It is neither authoritative state nor proof that recall helped. See [decision memory](retrieval.md#optional-decision-relevant-recall). |
| **Task-specific context** | A disposable view containing the information and instructions needed for the current planning or proposal phase. Equal facts can share a supplied-record pointer; exact history, obligations and source rules remain intact. See [context compaction](retrieval.md#make-room-without-losing-the-record). |
| **Decision-memory shadow** | A measured hypothetical selection stored in invocation receipts, outside the actual provider request. It adds no model call. It is independent of the older rich/active working-memory setting. |
| **Evidence** | A collected, readable source or recorded observation. WAKE checks provenance and structure; this does not prove that a claim is true. |
| **Gateway** | The retained multi-container setup’s hostname router and landing page. The current installation instead has one controller and one web server. |
| **Governance** | The deterministic rules that check a model's proposal before WAKE accepts changes. |
| **Group / parent node** | The current installation has three parent worker processes, each with three children. Each node owns a record; the installation controller owns their shared lifecycle and API queue. Earlier container groups are compatibility paths. |
| **Installation controller** | The process supervising all internal nodes, the shared model-request queue, and one web server. It owns lifecycle, not a merged research record. |
| **Whole installation** | The complete unified WAKE website, including journal, research and shared Bob blog. Its Console adds installation observations above the normal panels. Source records remain attributed to their nodes. |
| **Public mirror** | The latest locally generated public export uploaded for hosting. It has a snapshot date, no live execution claim, and no local operator authority. |
| **RESET** | The uppercase operator command that destroys active data without making a backup, initializes cycle zero, and leaves research stopped. Existing manual exports survive. |
| **Kernel** | The reusable WAKE layer for records, decisions, transitions, receipts and replay. It does not contain research-specific policy. |
| **Operational resilience** | Keeping effects valid, bounded and inspectable during specified failures; it is not a promise that external providers recover. See [checks and limits](resilience.md). |
| **Effect barrier failure** | A required checkpoint or permission check failed before a provider effect. The call is prevented; this differs from provider failure or governance rejection. |
| **Projection** | A disposable view of the record for a website or Console. It can be rebuilt and is never the authority. |
| **Proposal** | A model's suggested changes. A proposal is untrusted until governance checks it. |
| **Quantum Wake Function** | A philosophical metaphor: the wavefunction describes what might happen; the wake function describes how what happened shapes what can happen next. It is not an established mathematical object, physical law, or implemented computational function. See [why WAKE](why-wake.md) for the scientific limits. |
| **Quota standby / purple** | A provider limit makes affected requests temporarily ineligible. Gemini daily-quota recovery begins at 23:55 Pacific, no more than once per five minutes; short limits follow their retry interval. Other eligible requests use the same serial queue. |
| **Receipt** | A durable account of an attempt or decision. New proposal and provider receipts record Who, What, Where, Why, How, and When in hash-bound attribution; older missing details stay unspecified. See [receipt attribution](kernel.md#receipt-attribution). |
| **Wake metaphor** | The image of a disturbance left by passage through water: evidence of the past that can influence what follows. In WAKE, durable records carry consequences into future bounded context; this does not imply consciousness or a persistent personal identity. See [why WAKE](why-wake.md). |

The usual flow is:

```text
record → bounded context → model proposal → governance decision → transition → receipt
```

See [architecture and limits](architecture.md) for the full trust model and
[public mirror publishing](cloud.md) or [standalone operation](standalone.md) for the
operator procedures.

- **Initial publication** — the durable introductory Bob article. Worker groups
  synthesize `group-wake-introduction` from every parent and child and publish the
  same text in each record. Its WAKE01 checkpoint is separate from research progress.
  The older solo `wake-introduction` contract remains replayable.
- **Editorial sequence** — Bob's article number, separate from every member's
  research count. Three posts are scheduled per 100 aggregate accepted wakes (34, 67, 100),
  or after a recorded operator correction. Missed milestones remain due; one
  catch-up covers accumulated work. All members supply inputs even when progress
  differs. Bob’s language guidance does not alter research evidence rules.
- **Editorial rendering receipt** — a versioned description and hashes linking
  the exact provider response to its article. Rendering adds citation punctuation
  and the Summary heading from explicitly supplied paragraphs and references; it
  cannot invent attribution or scientific support.
- **Editorial continuity** — bounded context from Bob's previous accepted story
  and the current supplied records, helping a later article revisit open questions.
  It does not establish scientific progress or change research selection.
- **RSS** — a feed reader's way to check `blog.xml` for new Bob articles without
  giving this website an email address. The feed contains published, dated work.
- **Editorial correction** — a new model-written article that supersedes an older
  explanation while retaining its text, references and invocation. It changes no
  research result or scientific evidence.
- **First-post exception** — explicit operator permission for the exact first
  group introduction only. It is consumed once per member and cannot accept
  research, create scientific evidence or authorize later posts.

### Public mirror

A dated, read-only website exported from container records and uploaded to
`wake-public`. GitHub Pages serves that artifact; it has no research executor,
or operator controls. An explicitly configured hosted light observes the GitHub
batch separately from the dated research snapshot. Native node records remain authority, whether
the owning controller runs locally or in a GitHub Actions container.

### Hosted continuation

A research run explicitly asks the GitHub API to start its successor. A separate
completion-event workflow repairs failed handoffs. This is independent of cron.
Both use stable workflow identity and run numbers to avoid duplicate successors.
Quota waits preserve API capacity for controls; a failed batch with no successor
for fifteen minutes is shown as stalled, rather than indefinitely recovering.
Encrypted blocks transport complete native records between disposable runners;
they are not a second governance engine. See [hosted operation](cloud.md#run-research-on-github-without-a-laptop).

### Container reset

An explicit operator action on the selected installation. It leaves research
stopped and enrolls an empty continuity campaign. Publishing never resets records.
Historical hosted checkpoints and archives remain preserved.

Bob’s public articles use plain prose, including the built-in welcome. Public display removes legacy heading markers
without rewriting historical receipts.

**Lossless storage compression:** a smaller physical encoding that reconstructs the exact original record bytes. It is distinct from a model summary, which can omit detail. See [kernel storage](kernel.md#physical-storage-and-compatibility).

**Zero-cycle reset:** an operator action that clears active research progress and
starts a fresh enabled continuity campaign. It leaves research stopped or paused
until explicitly started; see [reset operation](standalone.md).

### Hosted activity relay

A read-only connection showing sampled node stages and confirmed provider-call
activity from the hosted installation. It keeps one short-lived public view,
clears on stale data, and contains no research bodies or controls. Unlike the
Actions light, it observes native worker activity. Research counts remain dated
exports. See [live hosted activity](cloud.md#watch-live-hosted-node-activity).
