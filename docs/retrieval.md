# Retrieval shadow: making forgetting observable

> **Active experimental design note.** This describes the current progressive-abstraction and deterministic retrieval layer. Shadow measurements remain important, but bounded-context delivery is no longer purely hypothetical: the engine can make a controlled fallback to the working representation when the rich request cannot fit.

**WAKE✳︎** records a deliberately lossy working-set representation beside each invocation and a deterministic plan for which exact durable records become important when an abstraction is expensive to trust. Under the normal context ceiling, the provider still receives the richer context and these structures remain observational. If the rich request remains above the configured ceiling after ordinary compaction, the engine can make one explicit, receipt-bearing switch to the bounded working representation rather than silently dropping durable obligations or evidence.

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

`retrieval_shadow` and `trust_compacts_shadow` remain receipt-side measurements rather than independent authorities. The working representation can become provider input only through the engine's controlled context-delivery fallback; exact records remain authoritative and the receipt records which delivery mode was used.

## Evaluation boundary

The size-triggered bounded-context fallback is an operational safeguard, not evidence that the abstraction is behaviorally equivalent to rich context. Before making bounded delivery the ordinary/default mode, collect enough paired invocations to score whether the representation preserves:

- evidence-backed belief revision,
- contradiction/counterevidence handling,
- commitment continuity,
- research provenance,
- justification quality,
- and recovery from abstraction mistakes.

The comparison remains:

**A — rich context**  
Normal delivery when it fits.

**B — working abstraction + recoverable provenance**  
Current controlled fallback and future candidate for broader use.

**C — overcompressed control**  
A deliberately weakened condition that removes provenance or uncertainty cues.

The primary question is whether B preserves correction while reducing active context.

> Exact underneath. Approximate on purpose. Correctable always.
