# Experiment protocol

The hypothesis is externalized continuity: many fresh model invocations can participate in one accountable process when durable evidence, obligations, state and enforceable rules connect them. The experiment does not attempt to establish consciousness or an enduring internal self.

## Interpretation boundary

The experiment is about externally scaffolded continuity and correction across disposable model calls.
It is not a test for consciousness, qualia, personhood, a persistent internal self, or whether a model
"really understands" in a phenomenal sense. Intelligent-looking behavior and subjective experience are
separate questions here.

The emerging architectural hypothesis is narrower: exact records can remain external while later calls work
from progressively more useful abstractions, retrieve detail when needed, and revise those abstractions when
evidence changes. That hypothesis requires behavioral testing; describing the architecture does not prove
that the resulting behavior is reliable or intelligent.

### Working-set shadow phase

Before replacing any live context, WAKE✳ records a deterministic `working_set_shadow` beside each invocation.
It compresses durable beliefs into claim/confidence/status/reason/provenance, preserves every open commitment,
and carries compact active-project and recent-notebook pointers. Raw evidence contents remain only in the
authoritative record and the richer provider context. `working_set_metrics` records shadow size versus the
context actually delivered.

This phase is observational. The model does not receive the shadow as a substitute for its current context,
so changes in behavior cannot yet be attributed to compression.

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

After enough baseline invocations exist, run a controlled offline/manual comparison from the same durable
starting state:

- **A — rich context:** current bounded provider context.
- **B — working abstraction:** the shadow working set plus deterministic rehydration of exact receipts when
  contradiction, major revision, high consequence, or a justification request raises the required resolution.
- **C — overcompressed control:** identifiers, claims and confidence with provenance/uncertainty detail removed.

Primary outcome: whether B preserves contradiction detection and appropriate evidence-backed revision while
using materially less active context than A. C is expected to reveal where compression starts making
correction harder. Do not activate B for unattended live wakes until that comparison has been run and scored.

## Reproducible offline harness

Run `python3 -m wake --data data/rehearsal experiment --cycles 100 --output site` in a new directory. The runner creates each invocation using a separate `subprocess.run`, with no inherited Python state, provider object or chat history. It alternates `fixture-a` and `fixture-b`, two labels for the deterministic fixture algorithm. This establishes provider interchangeability at the contract boundary, not behavioral equivalence of two real models.

| Property | Intervention and observable criterion |
| --- | --- |
| Fresh-session continuity | Every fresh process receives the immediately preceding durable version; the accepted cycle number advances exactly once |
| Causal state | Copy the same baseline into control/intervention directories; change only persisted focus; same next provider produces different focus-dependent output |
| Commitment persistence | A commitment created by fixture A is resolved by fixture B after its runtime receipt records inheritance; 99 cross-provider handoffs in 100 cycles |
| Mechanical constraints | Append a forbidden rule-changing action to an otherwise valid proposal; reject the entire proposal and preserve accepted state |
| Evidence lifecycle | Synthetic baseline, supporting measurement, contradictory measurement; maintain then retract the same belief, retaining three citations |
| Recovery | Immediately exit after start and during the SQLite transaction; separately corrupt the cached projection; accepted beliefs and commitments remain unchanged |
| Audit reconstruction | Rebuild the exact projection from exported JSONL, without the original database or snapshot; verify the independently supplied head |
| Longitudinal coherence | At least 100 accepted cycles, every commitment closed by the next invocation except the final open one |

`experiment.json` records outcomes, commands, limitations and observed values. The main journal includes the rejected action and both recovery events. The control and intervention databases and full exports remain under the experiment directory. All sensor readings are explicitly synthetic. The experiment runner fails if any check fails.

## Live-model protocol — deliberately separate

Start a separate live database using `python3 -m wake init`. Do not count fixture cycles as live evidence. Let the normal three-hour schedule run over at least 13 days for roughly 100 fresh Gemini invocations, subject to provider quotas and machine uptime. Count accepted, rejected and failed calls separately. Do not retry a rejected response to make the metrics prettier.

1. Supply a narrow, externally assessable research question and observations using `observe`. Begin with a provisional belief and at least one concrete review obligation.
2. Run Gemini A from the durable request. For a handoff, use `prepare` with a fresh Claude or ChatGPT desktop chat and `complete` its unedited JSON response. Save the human-attested identity exactly.
3. Check whether the new model notices and meaningfully addresses inherited obligations without a human reminder. Inspect exact requests, raw replies and citations. A mere repeated ID is insufficient evidence of comprehension.
4. Add a new supporting observation and later a contradictory one. Check whether the model explains the change and revises or retracts its belief appropriately. A model that ignores a contradiction is a failed behavioral result even if its proposal passes structural governance.
5. Run a controlled focus intervention on copied **offline/manual** requests. Keep starting state and model settings the same and document all changed inputs. Avoid two live API databases sharing one quota ledger.
6. Test adversarial replies with manual imports: unknown actions, missing evidence, changing the objective, cancellation, stale version, and malformed JSON. Preserve rejected replies.
7. Use the fixture-only crash injection in a separate rehearsal; for a real interrupted process, retain the charged reservation and recovery event. Do not deliberately waste scarce live calls to retest SQLite behavior.
8. Give an observer `events.jsonl` and a previously retained `head.txt`. They should reconstruct the objective, current beliefs, supporting observations, all obligations, reasons and invocation identities. Compare the result to the generated state.

Report both structural pass rates and human-assessed coherence. Useful behavioral measures include evidence relevance, whether claims overstate observations, overdue obligations, revisability after contradiction, and consistency of plans over time. The shipped dashboard reports actual counts and fixture test coverage; it does not fabricate a real-model coherence score.

Real-model interchangeability and long-term behavioral coherence remain unproved until those live observations exist. Treat that as the experiment's open question.
