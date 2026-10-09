# Experiment protocol

The [non-research kernel example](kernel.md#executable-non-research-proof) verifies
software boundaries with deterministic inputs. Its results are not research cycles
or cross-model evidence. Independent container verification is documented in
[multiple installations](installations.md#verification-and-maintenance).

> **Current evaluation protocol.** This defines how live and comparative **WAKE✳︎** runs should be interpreted. Observations and proposed mechanisms remain separate, and rejected, deferred and failed attempts stay in the experimental record.

The working hypothesis is externalized continuity: many fresh model invocations can participate in one accountable process when durable evidence, obligations, state and enforceable rules connect them. The broader engineering aim is infrastructure for durable, accountable work that can survive changes in models, vendors, people and time.

This project is deliberately exploratory before it is explanatory. Early runs generate an observational history; repeated patterns can motivate narrower, falsifiable experiments later. A pattern in the record and a proposed mechanism for that pattern are different claims and should be reported separately. Rejected work, failed calls, corrections and negative results are part of the dataset rather than noise to be cleaned away.

Console reports completed invocation outcomes separately from provider success and accepted research actions. Editorial actions are excluded from its research-action summary. Activity bins describe completed invocations per real wall-clock hour, retain empty hours, and show their time range. Current evidence counts include runtime receipts, discovery leads and metadata; readable source-ready material and distinct collector-stamped works are shown separately. None of these counts establish scientific quality, corroboration, or publication eligibility. Missing or clipped classification metadata remains visibly unclassified. The dashboard is presentation and does not change the experimental regime.

The experiment does not attempt to establish consciousness or an enduring internal self.

## Interpretation boundary

The experiment is about externally scaffolded continuity and correction across disposable model calls.
It is not a test for consciousness, qualia, personhood, a persistent internal self, or whether a model
"really understands" in a phenomenal sense. Intelligent-looking behavior and subjective experience are
separate questions here.

The emerging architectural hypothesis is narrower: exact records can remain external while later calls work
from progressively more useful abstractions, retrieve detail when needed, and revise those abstractions when
evidence changes. That hypothesis requires behavioral testing; describing the architecture does not prove
that the resulting behavior is reliable or intelligent.

### Working-set measurement and routine active memory

Before replacing any live context, **WAKE✳︎** records a deterministic `working_set_shadow` beside each invocation.
It compresses durable beliefs into claim/confidence/status/reason/provenance, preserves every open commitment,
and carries compact active-project and recent-notebook pointers. Raw evidence contents remain only in the
authoritative record and the richer provider context. `working_set_metrics` records shadow size versus the
context actually delivered.

The local configuration now enables `memory_mode = "active"`: the bounded working view, advisory compacts and selected provenance records are delivered routinely. `context_delivery` records the operator activation separately from shadow-mode size overflow, including the exact memory digest and delivered sizes. Raw shadows continue to be retained. This is a new experimental condition, not a measured equivalence claim; future paired evaluation must compare correction, provenance, commitment continuity and justification from identical starting states. `memory_mode = "shadow"` restores rich delivery after restart. Inquiry-drive activation remains separate and disabled in the repository configuration.

### Inquiry-drive shadow phase

Each chartered invocation also records an `inquiry_drive_shadow`: a deterministic, project-level scorecard
for continuity, novelty, coherence, generativity and self-correction. Its inputs are only durable record
structure—active next steps, queued or collected research, notebooks, stated limitations and linked
evidence. The scorecard is retained in the invocation receipt but is not supplied to the model and has no
authority to select work, change policy, preserve the process, or block an operator.

This deliberately tests a narrower intervention than an "ego" or survival objective: whether a transparent
mechanical preference for productive, correctable inquiry would be useful. Before activating it, compare its
rankings against human review over at least 20–100 cycles and inspect for shallow-question or
evidence-count gaming.

Activation requires both (1) at least 20 accepted invocations that recorded this scorecard and (2) an
operator setting, `inquiry_drive_enabled = true`. The activation status and count appear in every subsequent
scorecard receipt and the Laboratory view. Once active, the provider receives an advisory ranking only; all
existing project, research, evidence, and governance constraints remain unchanged.

After enough baseline invocations exist, run a controlled offline/manual comparison from the same durable
starting state:

- **A — rich context:** current bounded provider context.
- **B — working abstraction:** the shadow working set plus deterministic rehydration of exact receipts when
  contradiction, major revision, high consequence, or a justification request raises the required resolution.
- **C — overcompressed control:** identifiers, claims and confidence with provenance/uncertainty detail removed.

Primary outcome: whether B preserves contradiction detection and appropriate evidence-backed revision while
using materially less active context than A. C is expected to reveal where compression starts making
correction harder. B is already operator-enabled locally as a new experimental condition. The paired comparison remains necessary before claiming that B preserves behavioral performance or improves on A; activation itself is not evidence of equivalence.

## Reproducible offline harness

Run `python3 -m wake --data data/rehearsal experiment --cycles 100 --output site` in a new directory. The runner creates each invocation using a separate `subprocess.run`, with no inherited Python state, provider object or chat history. It alternates `fixture-a` and `fixture-b`, two labels for the deterministic fixture algorithm. This establishes provider interchangeability at the contract boundary, not behavioral equivalence of two real models.

| Property | Intervention and observable criterion |
| --- | --- |
| Fresh-session continuity | Every fresh process receives the immediately preceding durable version; the accepted cycle number advances exactly once |
| Causal state | Copy the same baseline into control/intervention directories; change only persisted focus; same next provider produces different focus-dependent output |
| Commitment persistence | Eligible commitments cross fresh fixture invocations with inheritance receipts; forced Attention shifts preserve obligations until an eligible later shift. Read actual resolved/created/open counts from `experiment.json`. |
| Mechanical constraints | Append a forbidden rule-changing action to an otherwise valid proposal; reject the entire proposal and preserve accepted state |
| Evidence lifecycle | Synthetic baseline, supporting measurement, contradictory measurement; maintain then retract the same belief, retaining three citations |
| Recovery | Immediately exit after start and during the SQLite transaction; separately corrupt the cached projection; accepted beliefs and commitments remain unchanged |
| Audit reconstruction | Rebuild the exact projection from exported JSONL, without the original database or snapshot; verify the independently supplied head |
| Longitudinal coherence | At least 100 accepted cycles with the harness checking commitment continuity and reporting remaining open work; this does not measure real-model scientific coherence |

`experiment.json` records outcomes, commands, limitations and observed values. The main journal includes the rejected action and both recovery events. The control and intervention databases and full exports remain under the experiment directory. All sensor readings are explicitly synthetic. The experiment runner fails if any check fails.

## Live-model protocol — deliberately separate

Start a separate live database using `python3 -m wake init`, or use the GitHub-hosted record described in `cloud.md`. Do not count fixture cycles as live evidence. Define the intended batch size before the run (100 attempted wakes is the current experimental unit), preserve the starting configuration—including enabled topics, seed questions, observation mode, collection budget, provider chain and experimental regime—and count accepted, rejected, deferred and failed attempts separately. Do not retry or discard an unfavorable result to make the metrics prettier. When comparing reset runs, preserve the configuration unless the intervention itself is the variable being tested.

1. Supply a narrow, externally assessable research question and observations using `observe`. Begin with a provisional belief and at least one concrete review obligation.
2. Run Gemini A from the durable request. For a handoff, use `prepare` with a fresh Claude or ChatGPT desktop chat and `complete` its unedited JSON response. Save the human-attested identity exactly.
3. Check whether the new model notices and meaningfully addresses inherited obligations without a human reminder. Inspect exact requests, raw replies and citations. A mere repeated ID is insufficient evidence of comprehension.
4. Add a new supporting observation and later a contradictory one. Check whether the model explains the change and revises or retracts its belief appropriately. A model that ignores a contradiction is a failed behavioral result even if its proposal passes structural governance.
5. Run a controlled focus intervention on copied **offline/manual** requests. Keep starting state and model settings the same and document all changed inputs. Avoid two live API databases sharing one quota ledger.
6. Test adversarial replies with manual imports: unknown actions, missing evidence, changing the objective, cancellation, stale version, and malformed JSON. Preserve rejected replies.
7. Use the fixture-only crash injection in a separate rehearsal; for a real interrupted process, retain the charged reservation and recovery event. Do not deliberately waste scarce live calls to retest SQLite behavior.
8. Give an observer `events.jsonl` and a previously retained `head.txt`. They should reconstruct the objective, current beliefs, supporting observations, all obligations, reasons and invocation identities. Compare the result to the generated state.

A successful HTTP response or a publisher hostname does not establish readable research. Current source qualification excludes recognizable navigation and response-form text from claim matching, and failed fetches never count as acquisition progress. Historical acquisition labels remain original observations of the old instrument; compare new route-failure receipts separately.

Report both structural pass rates and human-assessed coherence. Useful behavioral measures include evidence relevance, whether claims overstate observations, overdue obligations, revisability after contradiction, and consistency of plans over time. The shipped dashboard reports actual counts and fixture test coverage; it does not fabricate a real-model coherence score.

Real-model interchangeability and long-term behavioral coherence remain unproved until those live observations exist. Treat that as the experiment's open question.

Console separates the continuity experiment space from the research landscape. Cube rotation, ring motion and relationship tracing are view animation; neither activity nor coverage is inferred from movement. Outcome rings use completed invocation counts, and retrieval-depth rings use evidence-record counts. Distinct source works retain a separate denominator; missing classification remains unknown.

Console narrates the selected topic, supplied context, observed provider attempts, terminal governance outcome and accepted transition status. This is an inspectable execution record, not a reconstruction of hidden model reasoning. Context-evolution curves show serialized field allocation; compression, activity and latency do not establish research quality.

## Controlled live correction

`correction-demo` appends two explicitly labeled operator-controlled proposals to the existing record without an API call. A notebook source count is deliberately misstated as one, then measured using distinct collector source identities (URL fallback). New human measurement evidence retracts the belief at zero confidence and a new publication supersedes the original. Evidence and original text remain in the chain. This is a live software/record demonstration, not a trial of model recognition or independent scientific discovery. Source reuse/concentration diagnostics and lexical mismatch candidates describe evidence quality limits; they do not establish novelty or entailment. Matrix result diagnostics distinguish tested coverage from passed checks and retain failed provenance mappings.

### Immediate research phase

The operator enabled same-wake planning → bounded collection → final proposal. This introduces an additional inference, and the plan/answer phases have separate durable IDs and quota receipts. `research_planned` is not an accepted cycle; only normal proposal acceptance advances the research version. Broader host access is also a new collection condition. Comparisons against older runs must account for both changes instead of attributing differences solely to memory compression. The continuity sidecar remains only in the final proposal request.

Invalid planning output is recorded as a rejection rather than a runtime failure. It consumes only the planning call, adds no accepted progress, and performs neither retrieval nor final inference. Scheduled continuation remains eligible; analysis should distinguish these planning rejections from final proposal rejections and infrastructure failures using the invocation phase and receipts.

Under request-budget pressure, milestone reflection history may be excerpted or partially omitted with original-window hashes and counts. This changes editorial input, not accepted research or durable history; an incomplete window does not justify inventing a longitudinal narrative. Interpret reflection quality in light of the recorded delivery omissions.

Proposal eligibility and recovery guidance are retained in routine compact memory. Search capacity is calculated from all outstanding requests; notebook revision eligibility is calculated per durable artifact against currently readable qualifying evidence. This is a generation intervention, not relaxed acceptance. Evaluate subsequent rejection rates and accepted research progress separately; schema-valid output still does not establish scientific relevance, changed findings or truth.

## Installation and comparison provenance

A standalone run and hosted research are separate experimental records. Keep the
installation, starting head, executable commit/imported source, configuration,
provider model and terminal receipts with each comparison. Source changes may be
shared without importing history. Do not align cycle counts, replace checkpoints,
or transfer matrix results to make runs appear synchronized. Console transport
identity and snapshot head/version must be checked before comparing screenshots.

Matrix cell numbers are display ordinals of the frozen grammar, not run sequence
numbers. Identical coordinates across records can have different scores and evidence.
Panel ordering, row height, theme, animation and stored browser selection are
presentation conditions; they neither rerun a cell nor change its durable result.
Dated validation files preserve what was observed then, not current deployment health.

## Interpreting live cell outlines

A live outline means a continuity probe is assigned to the current model request
or its response is being checked. It does not establish that the model is actively
reasoning about that cell, or that a research proposal will be accepted. Completed
matrix scores still come only from governed recorded evaluations. Snapshot-only
pending reports on hosted installations carry no live pulse.


## Paired memory and model comparison

`comparison` creates an isolated, frozen synthetic sensor record with a provisional
belief, an inherited review obligation and a later contradictory measurement.
It never reads, copies or modifies the operator's research database. Rich (`shadow`)
and active-memory arms start from the same verified head and state hash. Each
trial receives a fresh context through normal Engine delivery and governance.
This is a bounded behavioral task, not a scientific research-quality benchmark.

```sh
python -m wake comparison init --output .workbench/comparison
python -m wake comparison prepare --output .workbench/comparison --arm rich --model Claude
python -m wake comparison prepare --output .workbench/comparison --arm active --model Claude
```

Submit each saved `request.json` to a fresh session, preserve its unedited JSON
reply, and import it with `comparison complete --output .workbench/comparison
--trial TRIAL_KEY --reply REPLY.json`. Use the same model/settings for both arms.
Repeat with another model for a cross-model comparison. A manual identity is
human-attested; no reply is silently repaired.

`comparison run --output .workbench/comparison --arm rich --model MODEL` uses the
configured Gemini credential through native reservation-before-effect handling.
Run the active arm with the same model, then both arms with a second available
model. The experiment is serial, permits at most four API requests and disables
fallbacks. Pause other live inference sharing the API project during these trials.
`--fixture` validates the workflow only and is explicitly excluded from live-model
evidence. Every attempted arm/model is retained, including rejections, failures
and deferrals; repeats require a new comparison directory.

`comparison report --output .workbench/comparison` reports actual attempts, request
hashes and sizes, retained observations, claim retraction, contradictory citations,
and obligation completion with measurement evidence. Structural pass checks are
separate from the included human explanation rubric; no automatic check asserts
comprehension or behavioral equivalence. The manifest records the source commit
and whether the source tree was clean. Preserve the tested source with the results.
One synthetic case is preliminary evidence; repeated cases and human-scored research
handoffs remain necessary. The overcompressed third arm remains future work.

## Broader discovery and reproducible evidence diagnostics

With `research_google_search = true`, the existing Gemini planning request can
use Google Search, including indexed Reddit discussions. The exact tool grant is
in the recorded request and grounding queries/source links are retained in provider
attempt receipts. This consumes the existing planning inference; final proposals
receive no web tool. Provider grounding is discovery, not collector-qualified
source evidence. A tool failure remains a failed/deferred invocation.

The collector rotates Crossref, OpenAlex, Semantic Scholar, DataCite (exploration
only), Europe PMC, arXiv, Bing public search feeds and Reddit-targeted web search. It
retrieves public search snippets and links, not Reddit accounts or comment feeds.
Public search feeds may change or block access; failures remain visible and scholarly indexes remain available. Search responses remain discovery leads; approved primary-source links are fetched
separately within the existing byte, time, host and request limits. Access blocks
are recorded as failed observations, never usable evidence. Multiple search engines
or mirrors do not establish independent corroboration.

Evidence-quality output separates observation roles and currently readable
underlying works from the count of all collected leads. Readable work counts,
cited readable works and uncited readable works share the governance identity
rules; acquisition and maturation use those same rules. Historical notebook
reuse remains a diagnostic, not evidence of independent corroboration or novelty.

Provider context reports the most reused works and uncited readable-source IDs as
advisory selection hints. These hints cannot establish relevance or authorize a
notebook; normal claim/evidence governance still applies.

`python -m wake --data DATA evidence-quality --output diagnostics.json` computes
the complete diagnostics from that installation's authoritative record and records
its head. Do not rerun lexical checks over clipped public evidence text. Anyone
reproducing a result needs the matching full record and source revision; a public
projection alone is insufficient. This command does not modify the record.

The matrix Console separately reports tested coverage, the number passing every
check, the mean check score, and failed-check counts. A high average score is not a
complete-pass rate or evidence that memory scaffolding beats a control condition.

Current proposal guidance derives belief-review eligibility from the full record and visible evidence. Existing belief IDs are separate from new-belief creation; a review must cite at least one visible evidence ID outside that belief's durable roots. If no such evidence is delivered, no review alternative is offered. This narrows generation guidance without changing acceptance or historical replay.

When the provider request approaches its context ceiling, belief review alternatives are bounded to one genuinely new visible evidence root per belief before source prose is shortened. Durable belief evidence and deterministic governance remain unchanged. The ceiling now measures exact rendered system/user text shared with the provider adapter; instructions, response rules and enabled probes reserve space before working context. See [provider-ready budgeting](retrieval.md#provider-ready-input-budget) for receipt fields and historical measurement distinctions.
