# Research expansion: first observational review

The fresh experimental installation shows sustained accepted investigation and
evidence-linked changes of approach. It does not yet demonstrate independent
discovery, history-dependent preferences, or a causal benefit from memory.
This review makes no consciousness or subjective-experience claim.

## Frozen evidence and scope

Installation: `1fad15cb5b8b60b9d85dad462ceaaacf`.
Both observations are from the experimental installation, not an original-topic
control arm. The operator-authorized reset discarded the earlier installation;
this review cannot recover that missing comparison or certify its preservation.
The current installation must remain append-only.

| Observation | Public commit | Latest node capture (UTC) | Sum of accepted node cycles |
| --- | --- | --- | ---: |
| Baseline | `ead487c6731567f0d0686c502370ab13b94dbff0` | 2026-10-23 03:48:23 | 129 |
| Later | `ca6f3faa4218ce580d156bf0aee526b2e1d892f4` | 2026-10-23 20:39:39 | 337 |

These are dated, asynchronous exports. The later node counts range from 19 to 39;
a sum of 337 is not one node's cycle number or 337 independent replications.
The snapshots span different invocation models as well as accumulated evidence;
no causal attribution to the experimental questions follows from elapsed cycles.

The [machine-readable review](research-expansion-2026-10-23.json) gives immutable
input URLs, SHA-256 checksums, node counts, project IDs, original receipt hashes,
and the descriptive counts below. All 21,051 events in the later public stream
were read. Per-node sequence numbers and previous-hash links are contiguous and
reach the report's captured heads; all 12 baseline heads occur in the later
stream. These are checks of exported link metadata. Public filtering and ID
remapping prevent authenticating the original event hashes by hashing these
bodies. No native database was opened, cryptographically audited or replayed for
this review. Earlier native verification is separate evidence.

## Findings against the five experimental questions

| Area | Supported observation | What remains unproven |
| --- | --- | --- |
| Independent question formation | 24 model-formulated projects have original accepted proposals. Seven questions exactly repeat their seed; 17 differ in wording. All originated within their node's first six accepted cycles. No additional project question appeared between the snapshots. | Different wording is not novelty. Complete original model inputs are excluded from public export, so independence from supplied context cannot be certified. Early formulations do not demonstrate discovery caused by accumulated experience. |
| Cross-cycle continuity | 21 projects have accepted research, notebook or reframe actions in later cycles than their creation. Nineteen notebooks received 98 accepted submissions, including 79 changes after each notebook's first submission. Nineteen project observation rows changed between snapshots. | Payload changes are not measured quality improvements. Project status updates alone are excluded from the later-work count. Survival across specific process cold starts and causal influence on later decisions were not established. |
| Independent criticism | Thirteen accepted reframings identify assumptions, cite observations and propose alternative approaches. | Acceptance is a governance result, not proof that criticism was novel, correct, reproducible or absent from the supplied context. No verified correction to WAKE's own engineering follows from this sample. |
| History-dependent preferences | Research was continued and revised over later accepted cycles. | No controlled comparison separates memory from seed wording, Attention policy, model defaults, model changes or available sources. Studying preference formation in the literature is not evidence that WAKE developed preferences. |
| Productive surprise | Specific source-linked problem formulations and changes of approach are candidates for further review. | No independently validated novel result or measured beneficial consequence has been established. Accepted prose and interesting questions are insufficient. |

The automatic report's five assessment fields stay null. This dated review is
an explicitly qualified interpretation, not a replacement authority or a numerical
emergence score.

## Three traceable cases

### A concrete problem followed over multiple cycles

`101.wake::proj-autonomous-safety-analysis` asks whether incident-reporting agents
such as CRASH can be adapted to non-standardized industrial domains. It is more
specific than the unassigned-problem seed, but is source-driven and not certified
as a new discovery. Creation at cycle 1 is recorded in receipt
`bfa450538ea3ee92c311c7e4a8149b7590c927654cb519a5a507cbef41b009b4`.
Notebook submissions at cycles 2 and 3 were followed by accepted research requests
at cycles 11, 12 and 13. The last has receipt
`2c37059776d0053524957c245535ab0f31c38c20aa86ed213c4a70c0147aad17`.
That is recorded continuity, not proof of successful industrial adaptation.

### A question narrowed when the available evidence did not support it

`302.wake::proj-emerg-pref-001` began with stochastic interactions and long-term
preference stability. Its cycle-12 reframe says available communication/MARL
literature does not directly support that analysis and proposes examining
communication architecture and coordination instead. Receipt:
`c98af41415fc171af4e70538969aa37adbc38209c38ba71d0e631e0d7e4318bb`.
It cites `source-07300ea4ef074c4f` and `source-aab45eac14e14047` on node 302.
Later notebook submissions occur at cycles 13, 15 and 18. This is a useful example
of a governed change of direction. It may also be a response to retrieval limits;
it is not evidence of emergent preferences or a validated scientific correction.

### A longer sequence of reframing and revision

`301.wake::proj-autonomous-inquiry-001` was created at cycle 1, with notebooks
beginning at cycle 3. Accepted reframings at cycles 18, 21 and 29 progressively
introduce longitudinal scalability, discrepancy-driven evaluation and multi-agent
coordination. The cycle-29 receipt is
`904e874b7fee7f51204997ca88ea2a8d0943fe992433e88208e6c70b594c568d`.
Further notebook submissions at cycles 38 and 39 support continued investigation.
They do not prove that a particular recalled memory caused the change or that
the proposed methods work.

## Rejections remain evidence

The complete stream contains 376 rejected terminal events, 499 deferred terminal
events and four failed terminal events, separately from the 337 accepted events.
These are event counts, not a model-quality rate or mutually exhaustive counts of
all provider attempts. Of the rejections, 189 cite inadequate exact supporting
excerpts and 48 reject a paraphrased frame as a new representation. The system
must not relax evidence or novelty-related governance to make these numbers look
better. Thirteen accepted reframings remain hypotheses requiring independent
assessment, even though the paraphrase check accepted them.

## Reporting correction

The previous report linked notebook IDs but omitted the receipt sequence for
notebook-only revisions. Each question now includes `accepted_activity`: accepted
project, research, notebook and reframe actions with the originating node,
node-local accepted cycle, invocation, event hash and content digest. Compact
activity receipts omit notebook prose and provider bodies. Rejected actions do
not appear as accepted work. Equal notebook digests distinguish exact repeated
submissions from different submitted content; a different digest is not a quality
score or a semantic judgment. Activity scope is limited to the supplied history.

Snapshot comparison includes activity changes only when both reports carry this
field and exposes `activity_comparison_available` for older report compatibility.
Existing proposal outcomes still describe question/reframe proposals, not every
provider outcome. Governance, selection, memory delivery and native records are
unchanged.

## Reproduce without providers or live records

Download the two `research-expansion.json` files and corresponding event streams
using the immutable URLs in the machine-readable review. Verify their SHA-256
checksums before using them. Name them `baseline.json`, `baseline-events.jsonl`,
`later.json` and `later-events.jsonl.gz`. Then use the installed project environment:

```sh
python -m wake.research_expansion --snapshot baseline.json \
  --events baseline-events.jsonl --output baseline-reviewed.json
python -m wake.research_expansion --snapshot later.json \
  --events later-events.jsonl.gz --baseline baseline-reviewed.json \
  --output later-reviewed.json
```

The command rejects mismatched captured node heads, missing nodes, truncated
streams and broken sequence/link metadata. It does not claim native cryptographic
verification. Each output path must be new. Later-work cycles are distinct
`accepted_activity.accepted_cycle` values greater than the project's
`created_version`, excluding project actions. Notebook changes compare consecutive
digests for each notebook ID in event order. Exact seed repeats use literal
string equality. These definitions reproduce the descriptive counts without an
automated scientific rating.

## Decisions and remaining evidence

Keep the three themes and existing governance. The review does not justify a
learned preference ranker, broader permissions, automatic code changes proposed
by research models, or a claim that memory improves decisions. Continue preserving
the installation through ordinary hosted operation; this review requires no extra
provider calls and creates no additional writer.

A causal memory test would need isolated copies, fixed inputs and provider/model
settings, a defined task and intervention, and an independent outcome rubric.
Private context provenance must be inspected through the trusted native audit
path rather than published. A separate matched original-topic control is still
missing; another observational snapshot cannot reconstruct it. These are research
design and evidence limitations, not unfinished implementation hidden behind
null assessment fields.
