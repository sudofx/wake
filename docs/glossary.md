# WAKE✳︎ glossary

Use this page when a technical term in the other guides is unfamiliar. The
definitions describe the current WAKE implementation, not broader industry
definitions.

| Term | Plain-language meaning |
| --- | --- |
| **Accepted cycle** | A research attempt whose proposed changes passed WAKE's rules and were recorded. A workflow can succeed even when its attempt is rejected or deferred. |
| **Application** | The rules and behavior for a particular kind of work. Research is WAKE's current application. |
| **Authority / authoritative record** | The one database allowed to decide what state is current for an installation. Each local or hosted installation has its own. |
| **Context** | The bounded information included in one model request. It can be smaller than the full record, but it keeps links to the exact sources it summarizes. |
| **Discovery lead** | A search result or index entry that may help locate a source. It is not itself qualifying research evidence. |
| **Evidence** | A collected, readable source or recorded observation. WAKE checks provenance and structure; this does not prove that a claim is true. |
| **Governance** | The deterministic rules that check a model's proposal before WAKE accepts changes. |
| **Kernel** | The reusable WAKE layer for records, decisions, transitions, receipts and replay. It does not contain research-specific policy. |
| **Projection** | A disposable view of the record for a website or Console. It can be rebuilt and is never the authority. |
| **Proposal** | A model's suggested changes. A proposal is untrusted until governance checks it. |
| **Receipt** | A durable account of an attempt or decision, including what was requested and whether it was accepted, rejected or deferred. |
| **Standby / purple** | A recoverable wait caused by provider quota pressure. WAKE retries on its schedule. A configured hard daily cap waits for the Pacific reset. |
| **Blocked / red** | The runtime cannot continue without operator or agent action. |
| **Continuity matrix** | An optional, versioned set of structured probes. It uses the same model response as research and does not make another provider call. |
| **Bob** | The byline for selected plain-language summaries of already-recorded research. Bob does not make research decisions or change the record. |

The usual flow is:

```text
record → bounded context → model proposal → governance decision → transition → receipt
```

See [architecture and limits](architecture.md) for the full trust model and
[hosted operation](cloud.md) or [standalone operation](standalone.md) for the
operator procedures.
