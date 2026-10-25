# Let WAKE adopt a small improvement autonomously

WAKE can generate, measure and adopt a bounded context-selection policy without
any person proposing or reviewing each change. It runs between invocations in
the existing engine and records decisions on the same native node authority.

The first permission is deliberately small: change the selector from
alphabetical project order to deadline priority **within the current Attention
topic**. This is behavior adaptation through a versioned policy, not unrestricted
Python rewriting. The deterministic planner uses native commitments and related
notebook pointers; it does not call a model or claim to have learned scientific
truth. Arbitrary Python proposals retain the separate [comparison workflow](improvements.md).

## Run the complete demonstration

```sh
python -m wake improve autonomous-demo --output /tmp/wake-autonomous-example
```

Open `autonomous.html` in that directory. This creates a new native fixture,
seeds two synthetic projects and a commitment, then runs the real engine. WAKE
generates the policy proposal, compares it, adopts it, and delivers context for
the promised project. No person supplies the adaptation proposal or reviews it.
A later synthetic research step remains subject to ordinary governance; adoption
does not fulfill commitments or add research progress. The example calls no model.
Its new directory is never reused or reset and no production authority is opened.

## Grant the installed runtime permission once

For a selected installation, set these root settings in its configuration:

```toml
decision_memory_mode = "active"
autonomous_context_improvement = true
```

The default grant is false. Models cannot change it. This is deployment setup,
not approval of each change: after installation and enablement, generation,
evaluation, adoption, monitoring and rollback run unattended at invocation
boundaries. Enabling creates an explicit configuration event; older histories
are not assigned a policy retroactively. Turning it off restores the effective
baseline selector while preserving all recorded policies and decisions.

For hosted installations, the compatible runtime must first pass CI and be
explicitly promoted through the existing runtime binding. Its `hosted-runtime.json`
entry may then grant `autonomous_context_improvement: true` with active decision
memory. The immutable workflow policy owns the grant. Missing grants write false
into restored configuration so an old checkpoint cannot silently re-enable it.
Changing source alone does not activate a feature in a pinned running revision.

## What an autonomous change must prove

The installed `autonomous-context@1` contract allows exactly one field:

| Field | Allowed values | Maximum adoption |
| --- | --- | --- |
| `selector` | `alphabetical`, `deadline-priority` | One forward adoption for this contract |

The planner produces the single permitted alternative when native open
commitments approach their deadlines. Each proposal includes native record IDs
and digests, the prior policy revision, accepted version and exact native head.
It cannot supply code, an evaluator, a score threshold, a model, permissions,
quota, Attention changes or a new objective. Extra fields are rejected.

Governance recomputes the supplied measurements from installed code. The
candidate must pass all 12 development and 60 randomized holdout cases and
strictly improve both sets. It must also make a better choice on the **current
native state**. A synthetic score gain alone is insufficient. If alphabetical
selection already picks the promised project, the trial is rejected for no native
gain and the policy stays unchanged. Failed trials are visible, and retries are
spaced by at least ten accepted research cycles. No fresh research means no
repeated attempt at the same state.

A measurement exception is recorded as an error class and quarantines this
adaptation before adoption. Baseline research can continue; record integrity
failures remain fatal outside this computation-only containment boundary.

These are selection-task measurements, not established gains in general
intelligence or scientific reasoning. The holdout comes from the same published
task family. This contract can saturate: once the single change is adopted, it
does not invent further permissions or manufacture improvements.

## Automatic monitoring and rollback

Before a subsequent invocation, the runtime checks the active selector against
the installed context guardrail. A selection mismatch or execution fault rolls
back to the baseline and quarantines the change. Fault receipts preserve digests
and error classes, not private context bodies. Replay does not need to reproduce
an old exception after its code is fixed.

There is also an outcome monitor. It compares eight delivered-context research
outcomes before adoption with eight afterward, matching provider, successful
model and proposal phase. A drop of at least two accepted outcomes triggers
rollback and quarantine. Quota deferrals, transport failures, editorial work,
other models and undelivered capsules are excluded. If no comparable baseline
exists, this monitor makes no claim; the context guardrail still operates.
This is a conservative operational observation, not causal proof of improvement
or regression. Quarantined changes are never retried under this contract.

## Authority and recovery

Configuration, trials, adoption and rollback are versioned application events
on each node's existing `wake.sqlite`. They use the normal writer lock and kernel
governance. The policy update and trial result are one atomic transition. They
never create another writable research authority, edit executable files, alter
older events, move Attention, change scientific qualification, spend model quota,
fulfill commitments or advance accepted research cycles.

The next invocation records the revision of the policy actually delivered in its
decision-memory context. A restart reads the recorded policy rather than repeating
an adoption. A crash before an atomic event commits leaves the old policy; a crash
afterward leaves the recorded new one. There is no source patch to finish applying.
`wake status`, `wake audit` and per-node research projections expose adaptation
status. Public projections remain dated observations, not authority.

The evaluator and interpreter meanings for version 1 must remain replayable.
New tasks, additional parameters or a wider change allowance require a new
versioned contract and deployment capability; a model cannot authorize that
expansion. The generic kernel remains independent of these research policies.

## Verify

```sh
python -m unittest discover -s tests -p test_autonomous_context.py -v
python -m unittest discover -s tests -p test_hosted_batch.py -v
```

These exercise native automatic adoption and delivery, rejection of forged scores
and extra permissions, unchanged historical prefixes/research counters, restart,
revocation, guardrail rollback, matched-outcome rollback and hosted grant handling.
