# Retrieval shadow: making forgetting observable

**WAKE✳︎** already records a deliberately lossy working-set shadow beside each invocation. The next experimental step is to record the inverse operation too: **what exact durable records would need to come back if the abstraction became too expensive to trust?**

This is still shadow mode. The provider continues to receive the existing rich context. Retrieval planning is measured, not activated.

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

The live request must not contain `working_set_shadow`, `retrieval_shadow`, or `trust_compacts_shadow` during this phase.

## Exit condition for shadow mode

Do not activate working-set delivery plus rehydration merely because it is smaller.

First collect enough paired invocations to score whether the shadow representation would have preserved:

- evidence-backed belief revision,
- contradiction/counterevidence handling,
- commitment continuity,
- research provenance,
- justification quality,
- and recovery from abstraction mistakes.

The comparison remains:

**A — rich context**  
Current behavior.

**B — working abstraction + recoverable provenance**  
Future candidate.

**C — overcompressed control**  
A deliberately weakened condition that removes provenance or uncertainty cues.

The primary question is whether B preserves correction while reducing active context.

> Exact underneath. Approximate on purpose. Correctable always.
